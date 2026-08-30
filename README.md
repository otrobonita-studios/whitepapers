# Otrobonita Whitepapers

Research papers from Otrobonita AI Labs, published open for critique.

**Disagreement is the point.** Every paper here is versioned, and every version
stays available. If part of one is wrong — and some of it will be — open an
issue. Corrections and counter-arguments are credited in the revision history
of the paper they change.

License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — share it,
quote it, argue with it. Attribution is all that is asked.

---

## Series: Building RAG Before the Model Runs

Three stages that run *before inference* and silently cap the quality of
everything after them. Read in pipeline order.

| # | Paper | Stage | Version | Status |
|---|---|---|---|---|
| 1 | [Hunting the Facts](upstream/1-hunting-the-facts/) | Sourcing & acquisition | 1.0 | unpublished |
| 2 | [Human Slop In, AI Slop Out](upstream/2-human-slop-in-ai-slop-out/) | Preprocessing | 1.0 | unpublished |
| 3 | [A Chunky Size Fits Nobody](upstream/3-a-chunky-size-fits-nobody/) | Chunking | 1.0 | unpublished |

**The through-line.** Sourcing chooses a frame on reality — and that frame
decides both what the system can answer and whether the corpus becomes a
standalone specialist or a routed node in a mesh. Preprocessing preserves the
topology that frame requires. Chunking respects the topology preprocessing
preserved. Each stage can only succeed if the one before it was honest about
its constraints:

```
Frame  →  Topology  →  Chunks
```

**See it running.** The papers reference a live system:
[router.otrobonita.com](https://router.otrobonita.com) (the mesh — where any
specialist is asked), [spacetalks.otrobonita.com](https://spacetalks.otrobonita.com)
(Apollo, and the OCR healing exhibit),
[mark.otrobonita.com](https://mark.otrobonita.com) (Mark Twain).

---

## Repository layout

```
<series>/<n>-<paper-slug>/
├── <paper-slug>-vX.Y.md      ← canonical source
└── final/
    └── <paper-slug>-vX.Y.odt ← rendered for PDF export
```

The Markdown is canonical. If the `.md` and the `.odt` disagree, the Markdown
is right and the ODT needs re-rendering.

## Authoring

| File | Purpose |
|---|---|
| `WHITEPAPER-TEMPLATE.md` | Start here. Fill-in template with inline rules. |
| `WHITEPAPER-STYLE-CONTRACT.md` | Structure, heading ladder, vocabulary, pre-publication checklist. |
| `WhitepaperTemplate.odt` | Render target. Carries the house styles. |
| `md2odt.py` | Renders a paper `.md` into the ODT template. |

```bash
python md2odt.py upstream/1-hunting-the-facts/hunting-the-facts-v1.0.md \
                 upstream/1-hunting-the-facts/final/hunting-the-facts-v1.0.odt
```

The cover image is carried through as a placeholder — swap it in LibreOffice,
then export to PDF. Everything else is filled from the Markdown.

## Versioning

Papers are living documents. Versions are meaningful, not decorative:

- **Major** — the argument changed, or a claim was retracted
- **Minor** — a section, exhibit, or measured result was added
- **Patch** — clarity, typos, link rot

The repo is the archival record: a paper is cited by title, year and the site,
and the exact wording of any version is recoverable from its tag. No DOIs —
minting one per release is overhead this readership never uses.

## The authoring team

Every paper names its own. Across the series:

- **Jesper Karlsson** — concept, thesis, structure, and accountability for
  every final call.
- **Assisting models** — drafting support, fact-checking, handling of
  uncertainty and counter-evidence, independent critique, and adversarial
  review. Named per paper; never inherited between papers.
