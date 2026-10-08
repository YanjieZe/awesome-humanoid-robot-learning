#!/usr/bin/env python3
"""
Plot how many papers this list has, month by month, from README.md.

Dependencies: pip install matplotlib
Usage: python3 scripts/generate_growth.py

Writes assets/paper_growth.png (light) and assets/paper_growth_dark.png (dark).
Each paper is counted once even if it appears in several sections. The month comes
from the arXiv ID when there is one, else from a "YYYY.MM" near the start of the line;
year-only entries count as June of that year. Entries with no date are left out.
"""

import re
from collections import Counter
from datetime import date
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
ASSETS = ROOT / "assets"
START = (2023, 1)  # earlier papers are folded into the starting total

ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf|html)/(\d{2})(\d{2})\.\d{4,5}")
MONTH_RE = re.compile(r"\b((?:19|20)\d{2})\.(\d{2})\b")
YEAR_RE = re.compile(r"\b((?:19|20)\d{2})\b")
URL_RE = re.compile(r"\]\((\S+?)\)")

THEMES = {
    "light": {"surface": "#fcfcfb", "ink": "#0b0b0b", "ink2": "#52514e",
              "grid": "#e6e5e0", "series": "#2a78d6"},
    "dark": {"surface": "#1a1a19", "ink": "#ffffff", "ink2": "#c3c2b7",
             "grid": "#34332f", "series": "#3987e5"},
}


def paper_lines():
    lines = README.read_text().split("\n")
    start = next(i for i, l in enumerate(lines) if l.startswith("## "))
    end = next(i for i, l in enumerate(lines) if l.startswith("# Contact"))
    return [l for l in lines[start:end] if l.startswith("- ")]


def paper_month(line):
    m = ID_RE.search(line)
    if m:
        return 2000 + int(m.group(1)), int(m.group(2))
    head = line[:60]
    m = MONTH_RE.search(head)
    if m:
        return int(m.group(1)), int(m.group(2))
    m = YEAR_RE.search(head)
    if m:
        return int(m.group(1)), 6
    return None


def monthly_counts():
    papers = {}
    for line in paper_lines():
        m = ID_RE.search(line) or URL_RE.search(line)
        key = m.group(0) if m else line
        papers.setdefault(key, paper_month(line))
    dated = [ym for ym in papers.values() if ym]
    return Counter(dated), len(papers) - len(dated)


def months_between(a, b):
    y, m = a
    while (y, m) <= b:
        yield y, m
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)


def plot(counts, theme, path):
    t = THEMES[theme]
    today = date.today()
    months = list(months_between(START, (today.year, today.month)))
    xs = [date(y, m, 15) for y, m in months]
    new = [counts.get(ym, 0) for ym in months]
    base = sum(v for ym, v in counts.items() if ym < START)
    cum, total = [], base
    for n in new:
        total += n
        cum.append(total)

    plt.rcParams.update({"font.size": 10, "text.color": t["ink"],
                         "axes.labelcolor": t["ink2"], "xtick.color": t["ink2"],
                         "ytick.color": t["ink2"]})
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 5.6), sharex=True, dpi=200,
                                   gridspec_kw={"height_ratios": [3, 2], "hspace": 0.28})
    fig.patch.set_facecolor(t["surface"])

    for ax in (ax1, ax2):
        ax.set_facecolor(t["surface"])
        ax.grid(axis="y", color=t["grid"], linewidth=0.8)
        ax.set_axisbelow(True)
        for side in ("top", "right", "left"):
            ax.spines[side].set_visible(False)
        ax.spines["bottom"].set_color(t["grid"])
        ax.tick_params(length=0)

    # Cumulative total
    ax1.plot(xs, cum, color=t["series"], linewidth=2, solid_capstyle="round")
    ax1.fill_between(xs, cum, color=t["series"], alpha=0.10, linewidth=0)
    ax1.plot(xs[-1], cum[-1], "o", color=t["series"], markersize=6,
             markeredgecolor=t["surface"], markeredgewidth=2)
    ax1.annotate(f"{cum[-1]:,}", (xs[-1], cum[-1]), xytext=(-8, 6),
                 textcoords="offset points", ha="right", va="bottom",
                 color=t["ink"], fontweight="semibold", fontsize=11)
    ax1.set_ylim(0, cum[-1] * 1.15)
    ax1.set_title("Total papers in the list", loc="left", color=t["ink"],
                  fontsize=11, fontweight="semibold")

    # New papers per month; the current month is still filling up
    bars = ax2.bar(xs, new, width=22, color=t["series"], linewidth=0)
    bars[-1].set_alpha(0.4)
    peak = max(range(len(new) - 1), key=new.__getitem__)
    ax2.annotate(str(new[peak]), (xs[peak], new[peak]), xytext=(0, 3),
                 textcoords="offset points", ha="center", va="bottom",
                 color=t["ink2"], fontsize=9)
    ax2.set_title("New papers per month (latest month is partial)", loc="left",
                  color=t["ink"], fontsize=11, fontweight="semibold")
    ax2.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
    ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y.%m"))
    ax2.set_xlim(date(*START, 1), date(today.year + (today.month == 12), today.month % 12 + 1, 1))

    fig.text(0.125, 0.015, f"Papers dated before {START[0]}.{START[1]:02d} are counted in the "
             f"starting total. Updated {today:%Y-%m-%d}.", color=t["ink2"], fontsize=8)
    fig.savefig(path, facecolor=t["surface"], bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)


def main():
    counts, undated = monthly_counts()
    ASSETS.mkdir(exist_ok=True)
    plot(counts, "light", ASSETS / "paper_growth.png")
    plot(counts, "dark", ASSETS / "paper_growth_dark.png")
    print(f"{sum(counts.values())} dated papers ({undated} undated, not plotted)")


if __name__ == "__main__":
    main()
