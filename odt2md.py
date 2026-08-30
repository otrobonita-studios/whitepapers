#!/usr/bin/env python3
"""
odt2md.py — extract an Otrobonita paper .odt into Markdown.

The .odt is the authoring surface: page flow, widows, and where a figure lands
relative to its caption are only visible there. The .md is derived from it — a
diffable, greppable, linkable reading copy, and the source the website pages
are generated from.

Usage:
    python odt2md.py <paper.odt> <out.md>

How structure is recovered
--------------------------
LibreOffice renames automatic styles (P9, P15, P21…) on every save, and the
numbers move, so style *names* are worthless as a signal. What survives is the
parent style each automatic style inherits from. This script resolves that
chain and maps the base style to Markdown.

That makes headings, body text, tables and lists reliable. It does NOT recover
roles applied as direct formatting — a pull quote that is simply an indented
paragraph is indistinguishable from body text.

So four roles need a NAMED paragraph style in LibreOffice, not direct
formatting. All four already exist in Writer:

    Quote      →  > blockquote      (Swedish UI: Citat)
    Caption    →  *italic caption*  (Swedish UI: Bildtext)
    Heading 1-4→  ## through #####  (Swedish UI: Rubrik 1-4)

and a paragraph whose runs are entirely bold becomes a **lead line**.

Apply the style from the sidebar instead of hitting the bold or indent button,
and extraction is lossless. Anything else still comes through as body text —
nothing is lost, it just arrives flat.
"""

import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

NS = {
    'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
    'style':  'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
    'text':   'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
    'table':  'urn:oasis:names:tc:opendocument:xmlns:table:1.0',
    'draw':   'urn:oasis:names:tc:opendocument:xmlns:drawing:1.0',
    'fo':     'urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0',
    'xlink':  'http://www.w3.org/1999/xlink',
}


def q(tag):
    p, l = tag.split(':')
    return '{%s}%s' % (NS[p], l)


# Base style -> role. Swedish and English UI names both appear because the
# base style is named by whichever locale created the document.
BASE_ROLES = {
    'heading_1': 'h1', 'rubrik_1': 'h1', 'title': 'h1',
    'heading_2': 'h2', 'rubrik_2': 'h2',
    'heading_3': 'h3', 'rubrik_3': 'h3',
    'heading_4': 'h3', 'rubrik_4': 'h3',
    'quote': 'quote', 'citat': 'quote', 'quotations': 'quote',
    'block_quotation': 'quote', 'wpquote': 'quote',
    'caption': 'caption', 'bildtext': 'caption', 'illustration': 'caption',
    'wpcode': 'code',
}


def norm(name):
    return re.sub(r'_20_', '_', (name or '')).strip().lower().replace(' ', '_')


class Doc:
    def __init__(self, path):
        with zipfile.ZipFile(path) as z:
            self.content = ET.fromstring(z.read('content.xml'))
            try:
                self.styles = ET.fromstring(z.read('styles.xml'))
            except KeyError:
                self.styles = None
        self.parent, self.bold_spans = {}, set()
        for root in (self.content, self.styles):
            if root is None:
                continue
            for container in ('office:automatic-styles', 'office:styles'):
                c = root.find(q(container))
                if c is None:
                    continue
                for st in c.findall(q('style:style')):
                    name = st.get(q('style:name'))
                    self.parent[name] = st.get(q('style:parent-style-name'))
                    if st.get(q('style:family')) == 'text':
                        for pel in st:
                            if pel.get(q('fo:font-weight')) == 'bold':
                                self.bold_spans.add(name)

    def role_of(self, el):
        """Walk the parent chain, stopping at the first level with a role.

        Stopping early matters: Heading 4 inherits from Heading inherits from
        Standard, and walking to the root would classify every subhead as body
        text.
        """
        if el.tag == q('text:h'):
            lvl = int(el.get(q('text:outline-level')) or 1)
            return {1: 'h1', 2: 'h2'}.get(lvl, 'h3')
        name, depth = el.get(q('text:style-name')), 0
        while name and depth < 8:
            role = BASE_ROLES.get(norm(name))
            if role:
                return role
            name, depth = self.parent.get(name), depth + 1
        return 'body'

    def text_of(self, el, mark=True):
        parts = []
        if el.text:
            parts.append(el.text)
        for ch in el:
            t = ch.tag
            if t == q('text:s'):
                parts.append(' ' * int(ch.get(q('text:c')) or '1'))
            elif t in (q('text:tab'),):
                parts.append(' ')
            elif t == q('text:line-break'):
                parts.append('\n')
            elif t == q('draw:frame'):
                img = ch.find(q('draw:image'))
                if img is not None:
                    parts.append('\n<!-- image: %s -->\n'
                                 % (img.get(q('xlink:href')) or '?'))
            elif t == q('text:span'):
                inner = self.text_of(ch, mark)
                st = ch.get(q('text:style-name'))
                if mark and st in self.bold_spans and inner.strip():
                    parts.append('**%s**' % inner)
                else:
                    parts.append(inner)
            elif t == q('text:a'):
                parts.append('[%s](%s)' % (self.text_of(ch, mark),
                                           ch.get(q('xlink:href')) or ''))
            else:
                parts.append(self.text_of(ch, mark))
            if ch.tail:
                parts.append(ch.tail)
        return ''.join(parts)


def convert(path):
    doc = Doc(path)
    body = doc.content.find(q('office:body')).find(q('office:text'))

    # Single-row tables are layout boxes; let their paragraphs flow as prose.
    grid_children, layout = set(), set()
    for tbl in body.iter(q('table:table')):
        if len(tbl.findall(q('table:table-row'))) <= 1:
            layout.add(id(tbl))
            continue
        for sub in tbl.iter():
            grid_children.add(id(sub))

    list_items = set()
    for lst in body.iter(q('text:list')):
        for p in lst.iter(q('text:p')):
            list_items.add(id(p))

    out = []

    def emit(s=''):
        out.append(s)

    for el in body.iter():
        if el.tag == q('table:table'):
            if id(el) in layout:
                continue
            rows = [[' '.join(doc.text_of(c).split())
                     for c in r.findall(q('table:table-cell'))]
                    for r in el.findall(q('table:table-row'))]
            if not rows:
                continue
            w = max(len(r) for r in rows)
            emit()
            emit('| ' + ' | '.join(rows[0] + [''] * (w - len(rows[0]))) + ' |')
            emit('|' + '|'.join(['---'] * w) + '|')
            for r in rows[1:]:
                emit('| ' + ' | '.join(r + [''] * (w - len(r))) + ' |')
            emit()
            continue

        if el.tag not in (q('text:p'), q('text:h')) or id(el) in grid_children:
            continue

        raw = doc.text_of(el).strip()
        if not raw:
            continue
        role = doc.role_of(el)

        if role in ('h1', 'h2', 'h3'):
            raw = raw.replace('**', '').strip()

        if id(el) in list_items:
            emit('- ' + raw)
            continue
        if role == 'h1':
            emit(); emit('## ' + raw); emit()
        elif role == 'h2':
            emit(); emit('### ' + raw); emit()
        elif role == 'h3':
            emit(); emit('#### ' + raw); emit()
        elif role == 'quote':
            emit(); emit('> ' + raw); emit()
        elif role == 'caption':
            emit(); emit('*%s*' % raw.strip('*')); emit()
        else:
            # a paragraph that is bold end to end is a lead line
            stripped = raw.strip()
            if stripped.startswith('**') and stripped.endswith('**') \
                    and stripped.count('**') == 2:
                emit(stripped); emit()
            else:
                emit(raw); emit()

    md = re.sub(r'\n{3,}', '\n\n', '\n'.join(out)).strip() + '\n'
    return md, doc


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    md, doc = convert(src)
    dst.write_text(md, encoding='utf-8')
    heads = len(re.findall(r'^#{2,4} ', md, re.M))
    print('  %s: %d words, %d headings, %d tables, %d quotes, %d captions'
          % (dst.name, len(md.split()), heads,
             md.count('\n|---'), len(re.findall(r'^> ', md, re.M)),
             len(re.findall(r'^\*[^*]', md, re.M))))


if __name__ == '__main__':
    main()
