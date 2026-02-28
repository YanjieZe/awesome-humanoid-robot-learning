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
