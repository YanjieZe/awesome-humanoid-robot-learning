#!/usr/bin/env python3
"""
Insert curated entries into README.md, keeping each section sorted newest first.

Usage:
  python3 scripts/insert_papers.py results.json [more.json ...]

Each JSON file is a list of objects:
  {"id": "2605.12345", "include": true, "sections": ["Locomotion"],
   "line": "- [arXiv 2026.05](https://arxiv.org/abs/2605.12345), Title"}
Entries whose arXiv ID already appears in README.md are skipped. IDs with include=false
are appended to scripts/excluded_ids.txt so fetch_arxiv.py does not return them again.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
EXCLUDED = ROOT / "scripts" / "excluded_ids.txt"
ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})")
MONTH_RE = re.compile(r"^- 🌟?\[[^\]]*?(20\d{2})\.(\d{2})\]")


def sort_key(line):
    """Comparable key: arXiv ID if present, else end of the YYYY.MM month, else None."""
    m = ID_RE.search(line)
    if m:
        yymm, num = m.group(1).split(".")
        return (int(yymm), int(num))
    m = MONTH_RE.match(line)
    if m:
        return (int(m.group(1)[2:] + m.group(2)), 99999)
    return None


def section_bounds(lines, name):
    start = next(i for i, l in enumerate(lines) if l.strip() == f"## {name}")
    end = next((i for i in range(start + 1, len(lines))
                if lines[i].startswith("## ") or lines[i].startswith("# ")), len(lines))
    while end > start + 1 and not lines[end - 1].startswith("- "):
        end -= 1
    return start + 1, end


def insert(lines, section, line):
    lo, hi = section_bounds(lines, section)
    key = sort_key(line)
    pos = hi
    for i in range(lo, hi):
        k = sort_key(lines[i])
        if lines[i].startswith("- ") and k is not None and k < key:
            pos = i
            break
    lines.insert(pos, line)


def main():
    lines = README.read_text().split("\n")
    seen = set(ID_RE.findall("\n".join(lines)))
    sections = {l[3:].strip() for l in lines if l.startswith("## ")}
    added, rejected = 0, []
    for path in sys.argv[1:]:
        for e in json.loads(Path(path).read_text()):
            if not e.get("include") or not e.get("line"):
                rejected.append(e["id"])
                continue
            if e["id"] in seen:
                continue
            for sec in e["sections"]:
                if sec not in sections:
                    print(f"unknown section {sec!r} for {e['id']}", file=sys.stderr)
                    continue
                insert(lines, sec, e["line"].strip())
            seen.add(e["id"])
            added += 1
    README.write_text("\n".join(lines))
    old = set(EXCLUDED.read_text().split()) if EXCLUDED.exists() else set()
    EXCLUDED.write_text("\n".join(sorted(old | set(rejected), reverse=True)) + "\n")
    print(f"added {added} papers, {len(set(rejected) - old)} newly excluded")


if __name__ == "__main__":
    main()
