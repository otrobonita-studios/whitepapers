# Otrobonita Whitepapers

Research papers from Otrobonita AI Labs, published open for critique.

**Disagreement is the point.** Every paper here is versioned, and every version
stays available. If part of one is wrong — and some of it will be — open an
issue. Corrections and counter-arguments are credited in the revision history
of the paper they change.

License: [CC BY 4.0](LICENSE) — share it, quote it, argue with it. Attribution
is all that is asked. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to critique,
and [HOW-WE-VERSION.md](HOW-WE-VERSION.md) for how versions, Markdown, ODT, PDF,
and the website relate.

Published HTML: [otrobonita.com/whitepapers](https://otrobonita.com/whitepapers).

---

## Series: Building RAG Before the Model Runs

Three stages that run *before inference* and silently cap the quality of
everything after them. Read in pipeline order. “Upstream” in these papers is
that idea — work before the model runs — not a folder name.

| # | Paper | Stage | Version | Status | Site |
|---|---|---|---|---|---|
| 1 | [Hunting the Facts](building-rag-before-the-model-runs/1-hunting-the-facts/) | Sourcing & acquisition | 1.0 | published | [HTML](https://otrobonita.com/whitepapers/hunting-the-facts) |
| 2 | [Human Slop In, AI Slop Out](building-rag-before-the-model-runs/2-human-slop-in-ai-slop-out/) | Preprocessing | 1.0 | published | [HTML](https://otrobonita.com/whitepapers/human-slop-in-ai-slop-out) |
| 3 | [A Chunky Size Fits Nobody](building-rag-before-the-model-runs/3-a-chunky-size-fits-nobody/) | Chunking | 1.0 | published | [HTML](https://otrobonita.com/whitepapers/a-chunky-size-fits-nobody) |

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

## Series: Miscellaneous

Shorter papers on organisations, cost, and accountability. Not a numbered
pipeline.

| Paper | Version | Status | Site |
|---|---|---|---|
| [The Half-Ask](miscellaneous/the-half-ask/) | see `versions/` | published | [HTML](https://otrobonita.com/whitepapers/the-half-ask) |
| [The Bottleneck Has Moved](miscellaneous/the-bottleneck-has-moved/) | see `versions/` | published | [HTML](https://otrobonita.com/whitepapers/the-bottleneck-has-moved) |
| [Token Throughput as a Performance Indicator](miscellaneous/token-throughput/) | see `final/` | published | [HTML](https://otrobonita.com/whitepapers/token-throughput-as-performance-indicator) |
| [One Human, a Thousand Actions](miscellaneous/one-human-a-thousand-actions/) | 3.0 | published | [HTML](https://otrobonita.com/whitepapers/one-human-a-thousand-actions) |

---

## Series: Think Like an Agent

Interviews. These two currently ship as designed ODT/PDF (and site HTML). There
is no canonical `.md` in the tree yet.

| Paper | Status | Site |
|---|---|---|
| [An Interview with GPT 5.6](think-like-an-agent/an-interview-wtih-GPT-5.6-sol/) | published | [HTML](https://otrobonita.com/whitepapers/think-like-an-agent) |
| [An Interview with Grok 4.5](think-like-an-agent/an-interview-with-Grok-4.5/) | published | [HTML](https://otrobonita.com/whitepapers/an-interview-with-grok) |

The GPT 5.6 folder is spelled `an-interview-wtih-GPT-5.6-sol` (historical typo).
The live site PDF path uses that spelling. Do not rename the folder until
`otrobonita-official` `pdfPath` / `coverImage` are updated in the same change.

---

## Two surfaces, one paper

Argument and wording for the web live in `*.md` when a Markdown file exists —
that is what the site and agents can use. Page design, cover, widows, and
figure placement live in `final/*.odt` (or the paper folder’s `.odt`) and the
exported PDF.

- After an argument pass in Markdown, run `md2odt.py` and re-export PDF.
- After a design pass in Writer, run `odt2md.py` and diff the `.md` before you
  ship HTML.
- If `.md` and `.odt` disagree, **stop**. Do not pick a silent winner in a
  script.

`versions/` is a draft drawer where it exists. Papers 1 and 2 of the RAG series
have no `versions/` folder. The layout in `WHITEPAPER-STYLE-CONTRACT.md` that
starts at `public/whitepapers/<slug>/{versions,final}/` is aspirational; this
repository uses `<series>/<paper-slug>/`.

## Authoring

| File | Purpose |
|---|---|
| `WHITEPAPER-TEMPLATE.md` | Start here. Fill-in template with inline rules. |
| `WHITEPAPER-STYLE-CONTRACT.md` | Structure, heading ladder, vocabulary, pre-publication checklist. |
| `HOW-WE-VERSION.md` | What a version means, how to cite, what Git vs the site vs PDF is. |
| `CONTRIBUTING.md` | How to open a critique. |
| `WhitepaperTemplate.odt` | House styles for PDF. |
| `md2odt.py` | Markdown → ODT (argument pass). |
| `odt2md.py` | ODT → Markdown (design pass). |

```bash
python md2odt.py building-rag-before-the-model-runs/1-hunting-the-facts/hunting-the-facts-v1.0.md \
                 building-rag-before-the-model-runs/1-hunting-the-facts/final/hunting-the-facts-v1.0.odt
```

The cover image is carried through as a placeholder — swap it in LibreOffice,
then export to PDF.

## Versioning

Papers are living documents. Versions are meaningful, not decorative:

- **Major** — the argument changed, or a claim was retracted
- **Minor** — a section, exhibit, or measured result was added
- **Patch** — clarity, typos, link rot

Cite a paper by title, year, site URL, and version. Git history is the archive.
No DOIs — minting one per release is overhead this readership never uses.

## The authoring team

Every paper names its own. Across the series:

- **Jesper Karlsson** — concept, thesis, structure, and accountability for
  every final call.
- **Assisting models** — drafting support, fact-checking, handling of
  uncertainty and counter-evidence, independent critique, and adversarial
  review. Named per paper; never inherited between papers.
