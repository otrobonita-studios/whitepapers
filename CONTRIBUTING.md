# Contributing

Critique is welcome. Drive-by rewrites of a paper are not.

## How to disagree

Open a GitHub Issue. In the first comment:

1. Quote the passage (title, version, and a short excerpt or heading).
2. Say whether you are correcting a **fact**, a **frame**, or a **citation**.
3. State the correction or counter-argument in one sitting. Links help; dumps
   of an alternate paper do not.

If the issue changes a paper, the revision history of that paper credits the
correction. Attribution for the original work remains [CC BY 4.0](LICENSE).

## What not to send as a pull request

- A new draft of someone else’s paper.
- Silent “fixes” to `.odt` XML or to generated `.md` without saying which
  surface you edited and what you diffed.
- License, branding, or tooling changes bundled with a critique.

If you want to contribute a **new** paper or a tooling fix, open an issue first
and wait for a maintainer to agree the scope.

## Tooling pull requests

Keep `md2odt.py` and `odt2md.py` as a two-way pipeline. If `.md` and `.odt`
disagree, the change must not pick a silent winner. See [HOW-WE-VERSION.md](HOW-WE-VERSION.md).
