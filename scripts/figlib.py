#!/usr/bin/env python3
"""
Generate every figure used by the Transport Atlas.

    /home/stav/.pixi/envs/sage/bin/python scripts/make_figures.py [name ...]
    /home/stav/.pixi/envs/sage/bin/python scripts/make_figures.py --list

Figure definitions live in figpart1..figpartN.py; each registers itself with the
@figure("name") decorator.  Every figure is written three times into ../figures:

    .svg  (web build)    .pdf (print build)    .png (200 dpi fallback)

LaTeX in labels uses TWO backslashes (ordinary Python strings).  If a label
renders wrong, run:  python3 scripts/fix_escapes.py scripts/make_figures.py
"""
from __future__ import annotations

import sys
import traceback
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
OUT = HERE.parent / "figures"
OUT.mkdir(exist_ok=True)

INK, MUTED, GRID = "#1f2430", "#6b7280", "#dfe3ea"
BLUE, TEAL, VIOLET = "#1f6feb", "#0d9488", "#7c3aed"
AMBER, ROSE, SLATE = "#d97706", "#e11d48", "#475569"
GREEN, SKY = "#15803d", "#0284c7"

matplotlib.rcParams.update({
    "figure.dpi": 110, "savefig.dpi": 200, "savefig.bbox": "tight",
    "font.size": 10, "font.family": "DejaVu Sans",
    "axes.edgecolor": "#9aa3b2", "axes.labelcolor": INK,
    "axes.titlesize": 11.5, "axes.titleweight": "bold", "axes.labelsize": 10,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "legend.frameon": False, "legend.fontsize": 9,
    "xtick.color": MUTED, "ytick.color": MUTED,
    "svg.fonttype": "none", "lines.linewidth": 2.0,
})

REGISTRY = {}
ORDER = []


def figure(name: str):
    """Register a zero-argument figure function under `name`."""
    def deco(fn):
        REGISTRY[name] = fn
        ORDER.append(name)
        return fn
    return deco


def save(fig, name: str):
    for ext in ("svg", "pdf", "png"):
        fig.savefig(OUT / (name + "." + ext), facecolor="white")
    plt.close(fig)
    print("   " + name)


def tidy(ax, grid=True):
    ax.set_axisbelow(True)
    if grid:
        ax.grid(True, alpha=0.9)
    else:
        ax.grid(False)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    return ax


def plain(ax, xlim=(0, 10), ylim=(0, 6)):
    ax.set_xticks([]); ax.set_yticks([]); ax.grid(False)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    return ax


def arrow(ax, p0, p1, color=INK, lw=1.8, rad=0.0, z=3, alpha=1.0):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=13, color=color,
                                 lw=lw, connectionstyle="arc3,rad=%s" % rad, zorder=z,
                                 alpha=alpha))


def box(ax, xy, w, h, text="", fc="white", ec=INK, lw=1.2, fs=9.5, tc=None):
    ax.add_patch(FancyBboxPatch(xy, w, h, boxstyle="round,pad=0.006,rounding_size=0.03",
                                linewidth=lw, edgecolor=ec, facecolor=fc, zorder=2))
    if text:
        ax.text(xy[0] + w / 2, xy[1] + h / 2, text, ha="center", va="center",
                fontsize=fs, color=tc or INK, zorder=3, linespacing=1.4)



def main(argv):
    if "-l" in argv or "--list" in argv:
        for n in ORDER:
            print(n)
        return 0
    names = [a for a in argv if not a.startswith("-")] or ORDER
    unknown = [n for n in names if n not in REGISTRY]
    if unknown:
        print("unknown figure(s): " + ", ".join(unknown))
        return 2
    print("writing %d figure(s) to %s" % (len(names), OUT))
    failed = 0
    for n in names:
        try:
            REGISTRY[n]()
        except Exception:
            failed += 1
            print("FAILED " + n)
            traceback.print_exc()
    print("%d/%d ok" % (len(names) - failed, len(names)))
    return 1 if failed else 0


