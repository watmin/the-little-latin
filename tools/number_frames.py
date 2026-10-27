#!/usr/bin/env python3
"""Add stable {#g-NN} bookmark markers above Question|Answer tables that lack one.

Usage: tools/number_frames.py docs/liber-i/01-salve.md [...]
- Never renumbers existing markers.
- A file with no markers is numbered g-01, g-02, ... in order.
- In a file that already has markers, a new table gets the previous marker
  plus a letter suffix (g-03 -> g-03a), so published links never move.
  Tables before the first marker get g-00a, g-00b, ...
"""
import re, string, sys

HEADER = re.compile(r"^\|\s*Question\s*\|\s*Answer\s*\|\s*$")
MARK = re.compile(r"^\{#g-(\d{2}[a-z]*)\}\s*$")

def process(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    used = {m[1] for l in lines if (m := MARK.match(l))}
    fresh = not used
    n, prev, out = 0, "00", []
    for l in lines:
        if (m := MARK.match(l)):
            prev = m[1]
        elif HEADER.match(l):
            j = len(out) - 1
            while j >= 0 and not out[j].strip():
                j -= 1
            if not (j >= 0 and MARK.match(out[j])):
                if fresh:
                    n += 1; new = f"{n:02d}"
                else:
                    base = prev[:2]
                    new = next(base + s for s in string.ascii_lowercase if base + s not in used)
                used.add(new); prev = new
                out += [f"{{#g-{new}}}", ""]
        out.append(l)
    open(path, "w", encoding="utf-8").write("\n".join(out))
    print(f"{path}: {len(used)} group markers")

for p in sys.argv[1:]:
    process(p)
