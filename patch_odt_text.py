#!/usr/bin/env python3
"""
patch_odt_text.py — surgically replace a text string inside .odt files.

Rewrites only content.xml; Pictures/, styles.xml and everything else are copied
through byte-for-byte. Use this when a paper's .odt already contains manual work
(a swapped cover image, hand-tuned layout) that a full re-render would destroy.

Usage:
    python patch_odt_text.py "old text" "new text" file1.odt [file2.odt ...]
    python patch_odt_text.py --dry-run "old" "new" *.odt

Notes:
  - Matching is on the literal text as stored in content.xml. If a run is split
    across formatting spans the match can fail; the script reports 0 hits rather
    than pretending it worked. Edit the cover text box in LibreOffice instead.
  - Close the file in LibreOffice first. A lock file (.~lock.<name>#) next to the
    document means it is open, and the script refuses to touch it.
"""

import shutil
import sys
import zipfile
from pathlib import Path


def patch(path: Path, old: str, new: str, dry: bool) -> int:
    lock = path.with_name(f".~lock.{path.name}#")
    if lock.exists():
        print(f"  SKIP  {path.name} — open in LibreOffice (lock file present)")
        return -1

    with zipfile.ZipFile(path) as z:
        xml = z.read("content.xml").decode("utf-8")
        items = [(i, z.read(i.filename)) for i in z.infolist()]

    hits = xml.count(old)
    if hits == 0:
        print(f"  MISS  {path.name} — string not found, left untouched")
        return 0
    if dry:
        print(f"  would patch {path.name} — {hits} hit(s)")
        return hits

    xml = xml.replace(old, new)
    tmp = path.with_suffix(".patch.tmp")
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        zout.writestr("mimetype", "application/vnd.oasis.opendocument.text",
                      compress_type=zipfile.ZIP_STORED)
        for info, data in items:
            if info.filename in ("content.xml", "mimetype"):
                continue
            zout.writestr(info, data)
        zout.writestr("content.xml", xml.encode("utf-8"))
    shutil.move(str(tmp), str(path))
    print(f"  ok    {path.name} — {hits} hit(s) replaced")
    return hits


def main() -> None:
    args = sys.argv[1:]
    dry = "--dry-run" in args
    args = [a for a in args if a != "--dry-run"]
    if len(args) < 3:
        sys.exit(__doc__)

    old, new, files = args[0], args[1], args[2:]
    total = 0
    skipped = 0
    for f in files:
        r = patch(Path(f), old, new, dry)
        if r < 0:
            skipped += 1
        else:
            total += r
    print(f"\n{total} replacement(s) across {len(files) - skipped} file(s)"
          + (f", {skipped} skipped (open)" if skipped else ""))


if __name__ == "__main__":
    main()
