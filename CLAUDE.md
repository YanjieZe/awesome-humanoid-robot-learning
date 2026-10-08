# CLAUDE.md

## Project Overview

A curated list of academic papers about **humanoid robot learning**, maintained as a single `README.md`. Papers are categorized by task and sorted by date (newest first) within each section.

## Sections (in order)

1. Loco-Manipulation and Whole-Body-Control
2. Manipulation
3. Teleoperation
4. Locomotion
5. Navigation
6. State Estimation
7. Sim-to-Real
8. Hardware Design
9. Simulation Benchmark
10. Physics-Based Character Animation
11. Human Motion Analysis and Synthesis

## Adding a Paper

Each entry follows this format:

```
- [<venue> <YYYY.MM>](<url>), <Paper Title>
```

Optional suffixes:
- `, [website](<project-page-url>)` — if a project page exists
- `🌟` prefix — if code is open-sourced

**Venue prefix examples:** `arXiv 2026.02`, `ICLR 2026`, `CoRL 2025`, `ICRA 2025`, `website 2025.11`

**Ordering:** Within each section, entries are sorted by date descending (newest first), then by arXiv ID descending for the same month.

**Section choice:** Pick the section that best matches the paper's primary task. A paper may appear in multiple sections if it spans topics (e.g., both Loco-Manipulation and Sim-to-Real).

## Commit Style

Commit messages are short and descriptive, e.g.:
- `Add <Paper Name> paper`
- `Add <Venue> <Paper Name>`
- `Update <Paper Name> paper to new arXiv version`

## Workflow

After adding new papers, automatically commit and push to the remote repository.

## Daily arXiv Update

A cloud routine runs this every day. To run it by hand:

1. `python3 scripts/fetch_arxiv.py --days 4 -o /tmp/candidates.json` — humanoid papers not yet in README.md or `scripts/excluded_ids.txt`
2. Judge each candidate with `scripts/curation_guide.md` and write a results JSON
   (`[{"id", "include", "sections", "line"}]`)
3. `python3 scripts/insert_papers.py results.json` — inserts into the right sections in sorted order and records rejected IDs in `scripts/excluded_ids.txt`
4. `python3 scripts/generate_growth.py` — refreshes `assets/paper_growth*.png` (needs matplotlib)
5. Commit README.md, `scripts/excluded_ids.txt` and `assets/paper_growth*.png` as `Add N papers from arXiv (YYYY-MM-DD)` and push
