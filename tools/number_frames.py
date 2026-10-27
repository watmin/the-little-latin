#!/usr/bin/env python3
"""Give stable {#f-NNN} anchors to Question|Answer frame rows that lack one.

Usage: tools/number_frames.py docs/liber-i/01-salve.md [...]
- Never renumbers existing anchors.
- A file with no anchors is numbered 001, 002, ... in order.
- In a file that already has anchors, an unanchored row gets the previous
  anchor plus a letter suffix (f-012 -> f-012a, f-012b), so published links
  never move. Rows before the first anchor get f-000a, f-000b, ...
"""
import re, string, sys

HEADER = re.compile(r"^\|\s*Question\s*\|\s*Answer\s*\|\s*$")
SEP = re.compile(r"^\|[-\s|:]+\|\s*$")
ANCHOR = re.compile(r"^\| \{#f-(\d{3}[a-z]*)\} ")

def process(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    existing = [m[1] for l in lines if (m := ANCHOR.match(l))]
    used = set(existing)
    fresh = not existing
    n, prev, in_frames = 0, "000", False
    for i, l in enumerate(lines):
        if HEADER.match(l):
            in_frames = True; continue
        if in_frames and SEP.match(l):
            continue
        if in_frames and l.startswith("|"):
            m = ANCHOR.match(l)
            if m:
                prev = m[1]; continue
            if fresh:
                n += 1; new = f"{n:03d}"
            else:
                base = re.match(r"\d{3}", prev)[0]
                new = next(base + s for s in string.ascii_lowercase if base + s not in used)
            used.add(new); prev = new
            lines[i] = f"| {{#f-{new}}} " + l[1:].lstrip()
            continue
        in_frames = False
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    print(f"{path}: {len(used)} anchors")

for p in sys.argv[1:]:
    process(p)
