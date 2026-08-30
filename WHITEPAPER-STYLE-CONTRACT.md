# Whitepaper Style Contract

How an Otrobonita whitepaper is authored, structured, and rendered.
Companion to `WHITEPAPER-TEMPLATE.md`.

**Scope:** applies to every paper under `public/whitepapers/`.

---

## 1. Markdown is the source; ODT is a render target

Papers are authored in Markdown and rendered into `WhitepaperTemplate.odt`
for the PDF. The `.md` file is canonical — if the two disagree, the Markdown
is right and the ODT needs re-rendering.

This matters for agents: **an agent fills in `WHITEPAPER-TEMPLATE.md`, never
the `.odt` directly.**

The same holds for the author. Edit the `.md`, then run `md2odt.py` and export
the PDF from LibreOffice. Regeneration keeps a hand-swapped cover image, so the
only manual step is the export itself. Hand-editing the `.odt` body puts it out
of sync with the `.md` that generates the web page — that has happened three
times and was caught by luck each time. Editing ODT XML by hand produces style drift that is
invisible until the PDF is generated.

## 2. Repository layout

```
public/whitepapers/
├── WhitepaperTemplate.odt          ← render target
├── WHITEPAPER-TEMPLATE.md          ← authoring template (agents start here)
├── WHITEPAPER-STYLE-CONTRACT.md    ← this file
└── <paper-slug>/
    ├── versions/                   ← every draft .md, numbered
    └── final/                      ← shipped .odt, .pdf, cover, figures
```

Series papers nest one level deeper: `<series>/<paper-slug>/{versions,final}/`.

Slugs are kebab-case and derived from the title, not the subtitle:
`a-chunky-size-fits-nobody`, not `why-there-is-no-universal-chunking-strategy`.
**When a paper is renamed, the slug is renamed with it** — a stale slug is how
a stale citation survives review.

## 3. Document skeleton

Fixed order. Sections 1, 2, 6 and 7 are mandatory in every paper.

| # | Element | Required |
|---|---|---|
| 1 | Cover — title, subtitle, byline | yes |
| 2 | Front matter — author, series, reading order, version | yes |
| 3 | `If you read one section, read this one — the short version` | full-length only |
| 4 | Closing caveat + one-line sting | yes |
| 5 | Numbered body sections | yes |
| 6 | `About This Paper` — disagreement invite, cite, license | yes |
| 7 | `The authoring team` — human line, model line | yes |

The short version is required for full-length papers and omitted for
short-form ones (roughly under five pages), where it would only restate the
opening. *A Chunky Size Fits Nobody* carries one; *Hunting the Facts* and
*Human Slop In, AI Slop Out* do not, and should not.

The sting — the single line a reader repeats to a colleague — is required in
every paper regardless of length, and is not generated last as an afterthought.

## 4. Heading ladder

One typeface. Sizes descend monotonically.

| Level | Markdown | Font | Size | Weight | Colour |
|---|---|---|---|---|---|
| H1 | `##` | Inter | 16pt | bold | `#141b21` |
| H2 | `###` | Inter | 13pt | bold | `#141b21` |
| H3 | `####` | Inter | 12pt | bold | `#141b21` |
| H4 | `#####` | Inter | 11pt | bold italic | `#141b21` |

The document title (`#`) is cover-only and does not appear in the body flow.

> **Known defect in `WhitepaperTemplate.odt` — fix on next edit.**
> The shipped ODT uses four different typefaces across the ladder
> (H1 Inter, H2 Calibri, H3 Liberation Serif, H4 Liberation Sans), and
> H3 at 14pt renders *larger* than H2 at 13pt. Collapse all four to Inter
> with the sizes above.

## 5. Body text

One style: `Standard` — 115% line height, 0.3cm space after, no first-line
indent.

> **Known defect in `WhitepaperTemplate.odt` — fix on next edit.**
> The shipped ODT carries `P11`, `P12`, `P14`, `P17` and `P19` as paragraph
> styles whose parent is `Standard` with **zero property overrides** — they
> render identically to `Standard` and to each other. The Short Version uses
> `Standard` while the body uses `P14`, for no visual reason. An agent has no
> way to choose between them, so it will choose differently on every run.
> Delete the aliases; keep `Standard`.

Emphasis: `**bold**` for terms being defined and for the claim inside a
blockquote. `*italic*` for titles of works and for the exemplifier notes.
Never both.

## 6. Cover page

Title 48pt. Byline `Jesper Karlsson · Otrobonita AI Labs` at 11pt Inter.

> **Known defect in `WhitepaperTemplate.odt` — fix on next edit.**
> Cover text is set at `#dddddd` and `#eeeeee` — near-white, legible only
> against the dark cover image. Replacing the image with a light one makes
> the title invisible. Either bind the text colour to the image, or set the
> cover to draw its text over a guaranteed-dark scrim.

## 7. Shared vocabulary

Identical wording across every paper, so a reader crossing from one to the
next meets one language:

- Evidence status is always one of **`measured`** / **`simulated`** /
  **`illustrative`**. Predictions are pre-registered and labelled as such,
  never presented as results.
- A RAG is **`indexed for retrieval`** on a corpus — never *"trained on"* it.
- A corrupted value repeated faithfully by a model is a **grounding error**,
  not a generation error. The distinction is load-bearing; keep it.

## 8. Citation block

```
Cite as Karlsson, J. (<year>). <Title>. Otrobonita AI Labs.
otrobonita.com/whitepapers
```

No DOI. Minting one per release is bureaucracy the readership does not use;
the versioned repo is the archival record instead.

Two rules, both of which exist because they have already been broken:

1. **The cite title is copied from the paper's own `#` line.** A rename edits
   both in the same commit, or it is not finished.
2. **Do not inherit the model list** from a sibling paper. Attribution is not
   boilerplate.

## 9. Pre-publication checklist

Run before anything moves from `versions/` to `final/`:

- [ ] Title in the `Cite as` line matches the `#` heading character-for-character
- [ ] Slug matches the current title
- [ ] Reading order bolds this paper and names its siblings by current title
- [ ] Short version stands alone — no forward references, no pending clicks
- [ ] Every figure has a caption that reads without the image
- [ ] Model list reflects what actually assisted this paper
- [ ] Vocabulary spot-check: no "trained on"; predictions labelled as predictions
