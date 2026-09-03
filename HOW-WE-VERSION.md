# How we version

One page. This is the public rule for citing and shipping papers in this
repository.

## What a version number means

Same as the README:

- **Major** — the argument changed, or a claim was retracted.
- **Minor** — a section, exhibit, or measured result was added.
- **Patch** — clarity, typos, link rot.

Bump the version in the paper’s front matter and in the filename when a
canonical `.md` exists (`<slug>-vX.Y.md`). Git history is the archive. There
are no DOIs.

## How to cite

Title, year, site URL, version. Example:

> Karlsson, J. (2026). *Hunting the Facts* (v1.0). Otrobonita AI Labs.
> https://otrobonita.com/whitepapers/hunting-the-facts

The website HTML is generated from the versioned Markdown when Markdown exists.
The PDF is the designed artefact, exported from the ODT.

## Two edit surfaces

| Surface | Owns |
|---|---|
| `*.md` | Argument and wording for the web, agents, and diffs |
| `*.odt` → PDF | Page design, cover, widows, figure placement |

After an argument pass in Markdown, run `md2odt.py` and re-export PDF.
After a design pass in Writer, run `odt2md.py` and diff the `.md` before you
ship HTML.

If `.md` and `.odt` disagree, stop. Do not ship, and do not let a script choose
a winner.

Some published papers (the two interviews) currently have ODT/PDF only. Treat
the PDF as the citable artefact until a `.md` exists and has been diffed
against that ODT.

## What `versions/` is

A draft drawer. It is not present on every paper. Cover experiments and
superseded titles may live there. Do not treat `versions/` as the public
index; the README tables are.

## Website vs this repository

[otrobonita.com/whitepapers](https://otrobonita.com/whitepapers) is the reading
copy. Paths on the site are flatter than Git (`/whitepapers/<slug>`). PDF and
cover paths on the site sometimes omit the `miscellaneous/` prefix. Change
those together if you rename a folder here.
