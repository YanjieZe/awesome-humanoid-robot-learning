#!/usr/bin/env python3
"""
Insert curated entries into README.md, keeping each section sorted newest first.

Usage:
  python3 scripts/insert_papers.py results.json [more.json ...]

Each JSON file is a list of objects:
  {"id": "2605.12345", "include": true, "sections": ["Locomotion"],
   "line": "- [arXiv 2026.05.16](https://arxiv.org/abs/2605.12345), Title"}
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
DATE_RE = re.compile(r"^- 🌟?\[[^\]]*?(20\d{2})\.(\d{2})(?:\.(\d{2}))?\]")


def paper_date(line):
    """Return the month, optional day, and arXiv sequence used for older entries."""
    source = ID_RE.search(line)
    sequence = int(source.group(1).split(".")[1]) if source else 99999
    date = DATE_RE.match(line)
    if date:
        year, month, day = date.groups()
        return int(year[2:] + month), int(day) if day else None, sequence
    if source:
        return int(source.group(1)[:4]), None, sequence
    return None


def newer(first, second):
    if first[0] != second[0]:
        return first[0] > second[0]
    if first[1] is not None and second[1] is not None and first[1] != second[1]:
        return first[1] > second[1]
    return first[2] > second[2]


def section_bounds(lines, name):
    start = next(i for i, l in enumerate(lines) if l.strip() == f"## {name}")
    end = next((i for i in range(start + 1, len(lines))
                if lines[i].startswith("## ") or lines[i].startswith("# ")), len(lines))
    while end > start + 1 and not lines[end - 1].startswith("- "):
        end -= 1
    return start + 1, end


def insert(lines, section, line):
    lo, hi = section_bounds(lines, section)
    key = paper_date(line)
    pos = hi
    for i in range(lo, hi):
        k = paper_date(lines[i])
        if lines[i].startswith("- ") and k is not None and newer(key, k):
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
