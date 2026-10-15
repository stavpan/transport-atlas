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


def unclip(fig):
    """Let annotations cross the axes edge instead of vanishing.

    `ax.annotate` defaults to `clip_on=True`, so a label placed just outside its axes is
    silently cut off. Every figure is swept here before it is written — the tight bounding
    box on save then expands to include the text, which is what we want. Tick labels and
    axis labels are left alone (matplotlib manages those).
    """
    from matplotlib.text import Annotation
    for ax in fig.get_axes():
        for t in ax.texts:
            if isinstance(t, Annotation) and t.get_clip_on():
                t.set_clip_on(False)


def save(fig, name: str):
    unclip(fig)
    for ext in ("svg", "pdf", "png"):
        fig.savefig(OUT / (name + "." + ext), facecolor="white")
    plt.close(fig)
    print("   " + name)


def save_anim(name: str, fig, update, frames, fps: int = 20, dpi: int = 115, hold: int = 12):
    """Write an animation twice: `name`.webp (what the site and the vault embed) and
    `name`.gif (a compatibility fallback, downscaled and frame-thinned to stay small).

    `update(i)` receives the values of `frames` and must redraw the artists of `fig`.
    Every animation also gets a static *poster* (`save()`, a filmstrip), which is what the
    PDF build uses.
    """
    from matplotlib.animation import FuncAnimation, PillowWriter
    seq = list(frames)
    if hold:                       # linger on the last frame: the eye needs a moment
        seq = seq + [seq[-1]] * hold
    anim = FuncAnimation(fig, update, frames=seq, interval=1000.0 / fps, blit=False)
    gif = OUT / (name + ".gif")
    webp = OUT / (name + ".webp")
    unclip(fig)
    anim.save(str(gif), writer=PillowWriter(fps=fps), dpi=dpi,
              savefig_kwargs={"facecolor": "white"})
    plt.close(fig)
    try:
        made = _webp_and_slim_gif(gif, webp)
    except ImportError:                                   # pragma: no cover
        made = " (no pillow: gif only)"
    print("   %s.webp (%.0f KB) + .gif (%.0f KB)%s"
          % (name, webp.stat().st_size / 1024, gif.stat().st_size / 1024,
             "" if not made else made))


def _webp_and_slim_gif(gif_path, webp_path):
    """Animated WebP at full quality, plus a small GIF fallback (60% size, every 3rd frame)."""
    from PIL import Image
    im = Image.open(gif_path)
    frames, duration = [], 80
    try:
        while True:
            duration = im.info.get("duration", duration)
            frames.append(im.convert("RGB").copy())
            im.seek(im.tell() + 1)
    except EOFError:
        pass
    if not frames:
        return " (no frames)"
    frames[0].save(webp_path, format="WEBP", save_all=True, append_images=frames[1:],
                   duration=duration, loop=0, quality=68, method=6)
    w, h = frames[0].size
    small = [f.resize((int(w * 0.6), int(h * 0.6)), Image.LANCZOS)
             .quantize(colors=48, method=Image.MEDIANCUT, dither=Image.Dither.NONE)
             for f in frames[::3]]
    small[0].save(gif_path, save_all=True, append_images=small[1:], duration=duration * 3,
                  loop=0, optimize=True)
    return ""


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



def is_fresh(name: str) -> bool:
    """True when every output of `name` already exists and is newer than the code that makes it.

    This is what makes a rebuild cheap: editing one note does not regenerate 43 figures.  Pass
    `--force` (or name the figures explicitly) to override.
    """
    exts = [".svg", ".pdf", ".png"] + ([".webp", ".gif"] if name.startswith("anim-") else [])
    outs = [OUT / (name + e) for e in exts]
    if not all(p.exists() for p in outs):
        return False
    fn = REGISTRY[name]
    mod = sys.modules.get(fn.__module__)
    srcs = [Path(__file__)]
    if mod is not None and getattr(mod, "__file__", None):
        srcs.append(Path(mod.__file__))
    newest_code = max(p.stat().st_mtime for p in srcs if p.exists())
    return min(p.stat().st_mtime for p in outs) > newest_code


def main(argv):
    if "-l" in argv or "--list" in argv:
        for n in ORDER:
            print(n)
        return 0
    force = "--force" in argv or "-f" in argv
    names = [a for a in argv if not a.startswith("-")] or ORDER
    unknown = [n for n in names if n not in REGISTRY]
    if unknown:
        print("unknown figure(s): " + ", ".join(unknown))
        return 2
    if not force and not [a for a in argv if not a.startswith("-")]:
        names = [n for n in names if not is_fresh(n)]
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


