#!/usr/bin/env python3
"""
md2odt.py — render an Otrobonita whitepaper (.md) into WhitepaperTemplate.odt.

Keeps the template's styles.xml untouched, so output matches the published
back catalogue exactly. Everything is filled from the Markdown.

Regenerating over an existing file KEEPS the cover image already in it, so a
cover swapped in by hand survives every rebuild. Pass --reset-cover to go back
to the template's placeholder.

Usage:
    python md2odt.py <paper.md> <out.odt> [--template T.odt] [--reset-cover]

Markdown subset (see WHITEPAPER-STYLE-CONTRACT.md):
    # Title                     -> cover title (48pt)
    ### Subtitle                -> cover subtitle
    **Author:** / **Series:**   -> front matter, rendered as cover reason-line
    ## / ### / ####             -> Heading 1 / 2 / 3
    paragraphs, **bold**, *italic*, `code`, [text](url)
    > blockquote                -> indented, bold-emphasised pull quote
    - bullets / 1. numbered
    | pipe | tables |
    ---                         -> ignored (section break)
    <!-- comments -->           -> stripped
"""

import argparse
import html
import re
import shutil
import sys
import zipfile
from pathlib import Path

# ---------------------------------------------------------------- styles used

BODY = "Standard"
H = {2: "Heading_20_1", 3: "Heading_20_2", 4: "Heading_20_3", 5: "Heading_20_4"}
SPAN_BOLD = "T5"          # font-weight:bold          (from template)
SPAN_STING = "T6"         # 13pt bold italic          (from template)

# automatic styles this script adds on top of the template's own
EXTRA_STYLES = """
<style:style style:name="WPQuote" style:family="paragraph" style:parent-style-name="Standard">
  <style:paragraph-properties fo:margin-left="0.8cm" fo:margin-right="0.8cm"
      fo:margin-top="0.25cm" fo:margin-bottom="0.25cm" fo:text-indent="0cm"
      fo:border-left="0.06cm solid #141b21" fo:padding-left="0.35cm"/>
</style:style>
<style:style style:name="WPBullet" style:family="paragraph" style:parent-style-name="Standard">
  <style:paragraph-properties fo:margin-left="0.6cm" fo:margin-bottom="0.12cm"
      fo:text-indent="-0.3cm"/>
</style:style>
<style:style style:name="WPCode" style:family="paragraph" style:parent-style-name="Standard">
  <style:paragraph-properties fo:margin-left="0.5cm" fo:margin-top="0.1cm"
      fo:margin-bottom="0.1cm"/>
  <style:text-properties style:font-name="Liberation Mono" fo:font-size="9.5pt"/>
</style:style>
<style:style style:name="WPCodeSpan" style:family="text">
  <style:text-properties style:font-name="Liberation Mono" fo:font-size="9.5pt"/>
</style:style>
<style:style style:name="WPItalic" style:family="text">
  <style:text-properties fo:font-style="italic"/>
</style:style>
<style:style style:name="WPLink" style:family="text">
  <style:text-properties fo:color="#1a4f7a" style:text-underline-style="solid"
      style:text-underline-width="auto" style:text-underline-color="font-color"/>
</style:style>
<style:style style:name="WPTable" style:family="table">
  <style:table-properties style:width="17.2cm" table:align="margins"/>
</style:style>
<style:style style:name="WPTableCol" style:family="table-column">
  <style:table-column-properties style:use-optimal-column-width="true"/>
</style:style>
<style:style style:name="WPTableHeadCell" style:family="table-cell">
  <style:table-cell-properties fo:padding="0.12cm"
      fo:border-bottom="0.04cm solid #141b21" fo:border-top="none"
      fo:border-left="none" fo:border-right="none"/>
</style:style>
<style:style style:name="WPTableCell" style:family="table-cell">
  <style:table-cell-properties fo:padding="0.12cm"
      fo:border-bottom="0.002cm solid #cccccc" fo:border-top="none"
      fo:border-left="none" fo:border-right="none"/>
</style:style>
<style:style style:name="WPTableHead" style:family="paragraph" style:parent-style-name="Standard">
  <style:paragraph-properties fo:margin-bottom="0cm"/>
  <style:text-properties fo:font-weight="bold" fo:font-size="10pt"/>
</style:style>
<style:style style:name="WPTableBody" style:family="paragraph" style:parent-style-name="Standard">
  <style:paragraph-properties fo:margin-bottom="0cm"/>
  <style:text-properties fo:font-size="10pt"/>
</style:style>
"""

# ------------------------------------------------------------------- inline


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def inline(text: str) -> str:
    """Convert inline Markdown to ODF spans. Order matters: code first."""
    out, i = [], 0
    pattern = re.compile(
        r"`([^`]+)`"                       # 1 code
        r"|\*\*(.+?)\*\*"                  # 2 bold
        r"|(?<!\*)\*([^*]+?)\*(?!\*)"      # 3 italic
        r"|\[([^\]]+)\]\(([^)]+)\)"        # 4 text, 5 href
    )
    for m in pattern.finditer(text):
        out.append(esc(text[i:m.start()]))
        if m.group(1) is not None:
            out.append(f'<text:span text:style-name="WPCodeSpan">{esc(m.group(1))}</text:span>')
        elif m.group(2) is not None:
            out.append(f'<text:span text:style-name="{SPAN_BOLD}">{inline(m.group(2))}</text:span>')
        elif m.group(3) is not None:
            out.append(f'<text:span text:style-name="WPItalic">{inline(m.group(3))}</text:span>')
        else:
            href = esc(m.group(5)).replace("&", "&amp;") if "&amp;" not in esc(m.group(5)) else esc(m.group(5))
            out.append(
                f'<text:a xlink:type="simple" xlink:href="{href}">'
                f'<text:span text:style-name="WPLink">{inline(m.group(4))}</text:span></text:a>'
            )
        i = m.end()
    out.append(esc(text[i:]))
    return "".join(out)


def para(text: str, style: str = BODY) -> str:
    return f'<text:p text:style-name="{style}">{inline(text)}</text:p>'


# -------------------------------------------------------------------- parser


def strip_comments(md: str) -> str:
    return re.sub(r"<!--.*?-->", "", md, flags=re.DOTALL)


def parse(md: str):
    """Return (meta, blocks). meta holds cover fields; blocks are body items."""
    md = strip_comments(md)
    lines = md.split("\n")
    meta = {"title": "", "subtitle": "", "frontmatter": []}
    blocks = []

    i = 0
    # ---- cover: first "# " is the title, first "### " after it the subtitle
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("# ") and not meta["title"]:
            meta["title"] = ln[2:].strip()
            i += 1
            continue
        if ln.startswith("### ") and meta["title"] and not meta["subtitle"] and not blocks:
            meta["subtitle"] = ln[4:].strip()
            i += 1
            continue
        if re.match(r"^\*\*(Author|A part of the series|Series|Reading order|"
                    r"Document Version|Evidence status|Revision note)", ln):
            meta["frontmatter"].append(ln.strip())
            i += 1
            continue
        if ln.strip() in ("---", "") and not blocks and not any(
            l.strip() and not l.startswith("**") for l in lines[:i]
            if not l.startswith("#")
        ):
            i += 1
            continue
        break

    # ---- body
    buf = []

    def flush():
        if buf:
            blocks.append(("p", " ".join(buf).strip()))
            buf.clear()

    while i < len(lines):
        ln = lines[i]
        s = ln.strip()

        if not s:
            flush()
            i += 1
            continue

        m = re.match(r"^(#{2,5})\s+(.*)$", s)
        if m:
            flush()
            blocks.append(("h", (len(m.group(1)), m.group(2).strip())))
            i += 1
            continue

        if s.startswith("```"):
            flush()
            i += 1
            code = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            blocks.append(("code", code))
            continue

        if s.startswith(">"):
            flush()
            q = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                q.append(lines[i].strip().lstrip(">").strip())
                i += 1
            blocks.append(("quote", " ".join(x for x in q if x)))
            continue

        if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|?$", lines[i + 1].strip()):
            flush()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                raw = lines[i].strip().strip("|")
                if not re.match(r"^[\s:|-]+$", raw):
                    rows.append([c.strip() for c in raw.split("|")])
                i += 1
            blocks.append(("table", rows))
            continue

        if re.match(r"^([-*]|\d+\.)\s+", s):
            flush()
            items = []
            while i < len(lines):
                t = lines[i].strip()
                mm = re.match(r"^(?:[-*]|\d+\.)\s+(.*)$", t)
                if mm:
                    items.append(mm.group(1))
                    i += 1
                elif t and not re.match(r"^(#{1,5}\s|>|\||```)", t) and items:
                    items[-1] += " " + t          # continuation line
                    i += 1
                else:
                    break
            blocks.append(("list", items))
            continue

        if re.match(r"^-{3,}$", s):
            flush()
            i += 1
            continue

        buf.append(s)
        i += 1

    flush()
    return meta, blocks


# ------------------------------------------------------------------ renderer


def render_body(blocks) -> str:
    out = []
    for kind, val in blocks:
        if kind == "h":
            lvl, txt = val
            out.append(
                f'<text:h text:style-name="{H.get(lvl, H[5])}" '
                f'text:outline-level="{lvl - 1}">{inline(txt)}</text:h>'
            )
        elif kind == "p":
            out.append(para(val))
        elif kind == "quote":
            out.append(
                f'<text:p text:style-name="WPQuote">'
                f'<text:span text:style-name="{SPAN_STING}">{inline(val)}</text:span></text:p>'
            )
        elif kind == "list":
            for it in val:
                out.append(para("• " + it, "WPBullet"))
        elif kind == "code":
            for cl in val:
                out.append(f'<text:p text:style-name="WPCode">{esc(cl) or "<text:s/>"}</text:p>')
        elif kind == "table":
            out.append(render_table(val))
    return "".join(out)


def render_table(rows) -> str:
    if not rows:
        return ""
    ncol = max(len(r) for r in rows)
    parts = [f'<table:table table:name="T{id(rows) % 9999}" table:style-name="WPTable">']
    parts.append(f'<table:table-column table:style-name="WPTableCol" '
                 f'table:number-columns-repeated="{ncol}"/>')
    for ri, row in enumerate(rows):
        cell_s = "WPTableHeadCell" if ri == 0 else "WPTableCell"
        para_s = "WPTableHead" if ri == 0 else "WPTableBody"
        parts.append("<table:table-row>")
        for ci in range(ncol):
            txt = row[ci] if ci < len(row) else ""
            parts.append(
                f'<table:table-cell table:style-name="{cell_s}" office:value-type="string">'
                f'<text:p text:style-name="{para_s}">{inline(txt)}</text:p>'
                f'</table:table-cell>'
            )
        parts.append("</table:table-row>")
    parts.append("</table:table>")
    return "".join(parts)


# -------------------------------------------------------------------- cover


def build_cover(tpl_body: str, meta: dict) -> str:
    """Reuse the template's cover XML verbatim, swapping only the text."""
    start = tpl_body.index("<draw:frame")
    end = tpl_body.index("<text:h ")
    cover = tpl_body[start:end]

    # title (48pt) — template has two T4 spans; collapse to one
    cover = re.sub(
        r'(<text:p text:style-name="P7">).*?(</text:p>)',
        lambda m: m.group(1) + f'<text:span text:style-name="T4">{inline(meta["title"])}</text:span>' + m.group(2),
        cover, count=1, flags=re.DOTALL,
    )
    # subtitle (T1, 18pt italic)
    cover = re.sub(
        r'(<text:span text:style-name="T1">).*?(</text:span>)',
        lambda m: m.group(1) + inline(meta["subtitle"]) + m.group(2),
        cover, count=1, flags=re.DOTALL,
    )
    # reason line (T2, 12pt) — the series line only. Reading order and version
    # belong in the paper's front matter, not on the cover; the hand-built
    # covers for papers 1 and 3 set this precedent and renders must match them.
    reason = next(
        (re.sub(r"\*\*(.+?)\*\*", r"\1", f).strip()
         for f in meta["frontmatter"]
         if f.startswith(("**A part of the series:", "**Series:"))),
        "",
    )
    cover = re.sub(
        r'(<text:span text:style-name="T2">).*?(</text:span>)',
        lambda m: m.group(1) + inline(reason) + m.group(2),
        cover, count=1, flags=re.DOTALL,
    )
    return cover


# --------------------------------------------------------------------- main


def extract_cover(path: Path):
    """Return (href, bytes) for the cover image of an existing .odt, or None.

    The cover is the first embedded picture in the document. Regenerating a
    paper must not discard a cover the author swapped in by hand, so this is
    read before the template overwrites anything.
    """
    if not path.is_file():
        return None
    try:
        with zipfile.ZipFile(path) as z:
            xml = z.read("content.xml").decode("utf-8")
            m = re.search(r'<draw:image[^>]*xlink:href="(Pictures/[^"]+)"', xml)
            if not m:
                return None
            href = m.group(1)
            if href not in z.namelist():
                return None
            return href, z.read(href)
    except (zipfile.BadZipFile, KeyError):
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("out")
    ap.add_argument("--template", default=str(Path(__file__).with_name("WhitepaperTemplate.odt")))
    ap.add_argument("--reset-cover", action="store_true",
                    help="use the template's cover image instead of keeping the one "
                         "already in the output file")
    a = ap.parse_args()

    md = Path(a.source).read_text(encoding="utf-8")
    meta, blocks = parse(md)
    if not meta["title"]:
        sys.exit(f"error: no '# Title' line found in {a.source}")

    # Capture the author's cover BEFORE the template is copied over the output.
    kept_cover = None if a.reset_cover else extract_cover(Path(a.out))

    with zipfile.ZipFile(a.template) as z:
        tpl = z.read("content.xml").decode("utf-8")

    head = tpl[: tpl.index("<office:body>")]
    head = head.replace("</office:automatic-styles>", EXTRA_STYLES + "</office:automatic-styles>")

    tpl_body = tpl[tpl.index("<office:body>"):]
    seq_end = tpl_body.index("</text:sequence-decls>") + len("</text:sequence-decls>")
    preamble = tpl_body[tpl_body.index("<office:text"): seq_end]

    xml = (
        head
        + "<office:body>"
        + preamble
        + build_cover(tpl_body, meta)
        + render_body(blocks)
        + "</office:text></office:body></office:document-content>"
    )

    # Point the cover frame at the author's image and carry its bytes across,
    # so a regeneration never silently reverts a hand-swapped cover.
    if kept_cover:
        kept_href, kept_bytes = kept_cover
        xml = re.sub(r'(<draw:image[^>]*xlink:href=")Pictures/[^"]+(")',
                     lambda m: m.group(1) + kept_href + m.group(2), xml, count=1)

    shutil.copyfile(a.template, a.out)
    # rewrite content.xml inside the copy
    tmp = Path(a.out).with_suffix(".tmp.zip")
    with zipfile.ZipFile(a.out) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        zout.writestr("mimetype", "application/vnd.oasis.opendocument.text",
                      compress_type=zipfile.ZIP_STORED)
        written = {"content.xml", "mimetype"}
        if kept_cover:
            zout.writestr(kept_href, kept_bytes)
            written.add(kept_href)
        for item in zin.infolist():
            if item.filename in written:
                continue
            zout.writestr(item, zin.read(item.filename))
        zout.writestr("content.xml", xml.encode("utf-8"))
    tmp.replace(a.out)

    heads = sum(1 for k, _ in blocks if k == "h")
    tbls = sum(1 for k, _ in blocks if k == "table")
    cover = "cover kept" if kept_cover else "cover from template"
    print(f"{Path(a.out).name}: {heads} headings, {tbls} tables, {len(blocks)} blocks, {cover}")


if __name__ == "__main__":
    main()
