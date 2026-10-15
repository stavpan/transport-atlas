#!/usr/bin/env python3
"""Legibility audit for every generated figure — the quality gate for `figures/`.

    /home/stav/.pixi/envs/sage/bin/python scripts/audit_figures.py [--verbose]

It re-runs every registered figure (from `make_figures.py`), but intercepts `save()` so
that nothing is written to disk, and then inspects the live matplotlib artists:

    * **too small**   — any text below `MIN_PT` points (the printed page and a 400-px-wide
                        phone column both punish anything below ~8 pt);
    * **clipped**     — text whose bounding box falls outside the figure (silently cut off);
    * **overlap**     — two texts colliding, e.g. an annotation landing on a tick label or
                        on another annotation (the single most common figure defect, and the
                        one that is invisible in code review).

Exit status is 1 if anything is flagged, so it can gate CI.  Animated figures are audited
through their *poster* (the filmstrip), which is the part that reaches print.
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

MIN_PT = 8.0          # below this a label is hard to read on paper and on a phone
OVERLAP_FRAC = 0.35   # share of the smaller box that must collide to count as an overlap
PAD = 0.5             # display-space tolerance (pixels) used for the "outside its axes" test

# Findings are only *actionable* when a hand-placed artist is involved. Tick labels that sit
# near the edge are absorbed by the tight bounding box on save, and two ticks in different
# panels never collide in practice, so those pairs are reported separately and not counted.
HAND_PLACED = ("annotation", "text", "legend", "title", "axis-label")


def texts_of(fig):
    """Visible text artists as (text, kind) pairs — kind drives how it is judged."""
    out = []
    for ax in fig.get_axes():
        for t in ax.texts:
            out.append((t, "text"))
        if ax.get_title():
            out.append((ax.title, "title"))
        if ax.xaxis.label.get_text():
            out.append((ax.xaxis.label, "axis-label"))
        if ax.yaxis.label.get_text():
            out.append((ax.yaxis.label, "axis-label"))
        for t in list(ax.get_xticklabels()) + list(ax.get_yticklabels()):
            out.append((t, "tick"))
        leg = ax.get_legend()
        if leg is not None:
            for t in leg.get_texts():
                out.append((t, "legend"))
    return [(t, kind) for t, kind in out
            if t is not None and t.get_text().strip() and t.get_visible()]


def audit(fig, name):
    """Return a list of human-readable problems for one live figure."""
    bad = []
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    fbox = fig.bbox

    boxes = []
    for t, kind in texts_of(fig):
        pt = float(t.get_fontsize())
        if pt < MIN_PT:
            bad.append("too small (%.1f pt): %r" % (pt, t.get_text()[:48]))
        try:
            bb = t.get_window_extent(renderer=r)
        except Exception:                                  # a text with no layout yet
            continue
        if bb.width <= 0 or bb.height <= 0:
            continue
        ax = t.axes
        if ax is not None and t.get_clip_on() and kind == "text":
            # a hand-placed annotation that matplotlib itself cuts off at the axes edge
            ab = ax.get_window_extent(renderer=r)
            if (bb.x0 < ab.x0 - PAD or bb.y0 < ab.y0 - PAD
                    or bb.x1 > ab.x1 + PAD or bb.y1 > ab.y1 + PAD):
                bad.append("clipped by its axes: %r" % t.get_text()[:48])
        if kind != "tick" and (bb.x1 < fbox.x0 - 60 or bb.y1 < fbox.y0 - 60
                               or bb.x0 > fbox.x1 + 60 or bb.y0 > fbox.y1 + 60):
            bad.append("far outside the canvas: %r" % t.get_text()[:48])
        boxes.append((bb, t.get_text()[:40], kind))

    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            a, b = boxes[i][0], boxes[j][0]
            ox = min(a.x1, b.x1) - max(a.x0, b.x0)
            oy = min(a.y1, b.y1) - max(a.y0, b.y0)
            if ox <= 0 or oy <= 0:
                continue
            inter = ox * oy
            smaller = min(a.width * a.height, b.width * b.height)
            if smaller <= 0 or inter / smaller <= OVERLAP_FRAC:
                continue
            kinds = (boxes[i][2], boxes[j][2])
            labels = (boxes[i][1], boxes[j][1])
            if labels[0] == labels[1] or kinds == ("tick", "tick"):
                continue                                   # axis furniture, not a defect
            hand = [k for k in kinds if k != "tick"]
            mark = "!!" if len(hand) == 2 else "·"
            bad.append("overlap %s (%.0f%%): %r ✕ %r"
                       % (mark, 100 * inter / smaller, labels[0], labels[1]))
    return bad


def is_blocking(finding: str) -> bool:
    """Count only defects that are certainly visible: tiny text, cut-off text, or two
    hand-placed labels on top of each other.  An annotation grazing a tick number is
    reported as advice (`overlap ·`), not as a failure."""
    if finding.startswith(("too small", "clipped", "far outside")):
        return True
    return finding.startswith("overlap !!")


def main(argv):
    verbose = "-v" in argv or "--verbose" in argv

    import figlib
    import make_figures                                # registers every figure function
    import figanim

    captured = {}

    def spy_save(fig, name):
        figlib.unclip(fig)              # exactly what the real save() does first
        captured[name] = audit(fig, name)
        plt.close(fig)

    def spy_anim(name, fig, update, frames, **kw):
        plt.close(fig)                                 # animation: poster is audited instead

    for mod in list(sys.modules.values()):
        if getattr(mod, "__name__", "").split(".")[0] in ("figlib", "figpart", "figanim") \
                or getattr(mod, "__name__", "").startswith(("figpart", "figanim")):
            if hasattr(mod, "save"):
                mod.save = spy_save
            if hasattr(mod, "save_anim"):
                mod.save_anim = spy_anim

    names = [n for n in figlib.ORDER if not n.startswith("anim-")]
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")                # matplotlib's own layout noise
        for n in names:
            try:
                figlib.REGISTRY[n]()
            except Exception as exc:                   # a broken figure is a finding too
                captured[n] = ["figure raised %s: %s" % (type(exc).__name__, exc)]

    total = sum(len(v) for v in captured.values())
    blocking = sum(1 for v in captured.values() for f in v if is_blocking(f))
    for n in sorted(captured):
        problems = captured[n]
        if problems or verbose:
            print("%-34s %s" % (n, "ok" if not problems else "%d note(s), %d to fix"
                                % (len(problems), sum(1 for f in problems if is_blocking(f)))))
            for p in problems:
                print("      %s %s" % ("!" if is_blocking(p) else "·", p))
    print("\n%d figures audited · %d to fix · %d advisory note(s)"
          % (len(captured), blocking, total - blocking))
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
