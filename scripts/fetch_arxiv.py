#!/usr/bin/env python3
"""
Fetch candidate humanoid papers from arXiv that are not yet in README.md.

No dependencies beyond the standard library.
Usage:
  python3 scripts/fetch_arxiv.py --days 3                 # last 3 days
  python3 scripts/fetch_arxiv.py --since 2026-03-14       # since a date
  python3 scripts/fetch_arxiv.py --since 2026-03-14 --until 2026-04-01 -o out.json

Prints (or writes) a JSON list of {id, title, authors, abstract, published,
categories, comment} for papers whose title or abstract mentions humanoids and
whose arXiv ID is not already in README.md or scripts/excluded_ids.txt. The candidates still need
a human (or Claude) to judge relevance and pick a section.
"""

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
EXCLUDED = ROOT / "scripts" / "excluded_ids.txt"  # reviewed and rejected; skip next time
API = "http://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
PAGE = 500
TERMS = [
    'humanoid', 'humanoids', 'biped', 'bipedal', '"whole-body"', '"whole body"',
    '"loco-manipulation"', '"motion tracking"', '"motion retargeting"',
    '"physics-based character"', '"simulated character"',
    '"Unitree G1"', '"Unitree H1"',
]
QUERY = (
    "(" + " OR ".join(f"{f}:{t}" for t in TERMS for f in ("ti", "abs")) + ") AND "
    "(cat:cs.RO OR cat:cs.LG OR cat:cs.AI OR cat:cs.CV OR cat:cs.GR OR cat:eess.SY)"
)


def existing_ids():
    text = README.read_text() + (EXCLUDED.read_text() if EXCLUDED.exists() else "")
    return set(re.findall(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", text)) | \
        set(re.findall(r"^(\d{4}\.\d{4,5})", text, re.M))


def fetch(start_dt, end_dt):
    window = f"submittedDate:[{start_dt:%Y%m%d%H%M} TO {end_dt:%Y%m%d%H%M}]"
    query = f"{QUERY} AND {window}"
    results, start = [], 0
    while True:
        params = urllib.parse.urlencode({
            "search_query": query, "start": start, "max_results": PAGE,
            "sortBy": "submittedDate", "sortOrder": "descending",
        })
        for attempt in range(5):
            try:
                with urllib.request.urlopen(f"{API}?{params}", timeout=60) as r:
                    root = ET.fromstring(r.read())
                break
            except Exception as e:  # arXiv API is flaky; back off and retry
                print(f"retry {attempt}: {e}", file=sys.stderr)
                time.sleep(5 * (attempt + 1))
        else:
            raise RuntimeError("arXiv API failed")
        entries = root.findall("a:entry", NS)
        for e in entries:
            raw_id = e.findtext("a:id", "", NS).rsplit("/", 1)[-1]
            results.append({
                "id": re.sub(r"v\d+$", "", raw_id),
                "title": " ".join(e.findtext("a:title", "", NS).split()),
                "authors": [a.findtext("a:name", "", NS) for a in e.findall("a:author", NS)],
                "abstract": " ".join(e.findtext("a:summary", "", NS).split()),
                "published": e.findtext("a:published", "", NS)[:10],
                "categories": [c.get("term") for c in e.findall("a:category", NS)],
                "comment": " ".join((e.findtext("arxiv:comment", "", NS) or "").split()),
            })
        total = int(root.findtext("{http://a9.com/-/spec/opensearch/1.1/}totalResults", "0"))
        start += PAGE
        if not entries or start >= total:
            break
        time.sleep(3)  # arXiv asks for >=3s between requests
    return results


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--days", type=int, help="look back N days from now")
    p.add_argument("--since", help="YYYY-MM-DD (inclusive)")
    p.add_argument("--until", help="YYYY-MM-DD (exclusive), default now")
    p.add_argument("-o", "--output", help="write JSON here instead of stdout")
    args = p.parse_args()

    now = datetime.now(timezone.utc)
    end = datetime.fromisoformat(args.until).replace(tzinfo=timezone.utc) if args.until else now
    if args.since:
        start = datetime.fromisoformat(args.since).replace(tzinfo=timezone.utc)
    else:
        start = end - timedelta(days=args.days or 3)

    # Query month by month so no single query hits arXiv's result cap.
    papers, cur = {}, start
    while cur < end:
        nxt = min(cur + timedelta(days=31), end)
        for paper in fetch(cur, nxt):
            papers[paper["id"]] = paper
        cur = nxt
        time.sleep(3)

    seen = existing_ids()
    out = sorted((x for x in papers.values() if x["id"] not in seen),
                 key=lambda x: x["id"], reverse=True)
    data = json.dumps(out, indent=1, ensure_ascii=False)
    if args.output:
        Path(args.output).write_text(data)
        print(f"{len(out)} new candidates ({len(papers) - len(out)} already listed) -> {args.output}",
              file=sys.stderr)
    else:
        print(data)


if __name__ == "__main__":
    main()
