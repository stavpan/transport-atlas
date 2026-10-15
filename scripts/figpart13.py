"""Part 13 — the intersections map, the generative artwork, and the arrow of time."""
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, hsv_to_rgb
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from figlib import (figure, save, tidy, plain, arrow, box,
                    INK, MUTED, BLUE, TEAL, VIOLET, AMBER, ROSE, SLATE, GREEN, SKY)

MECH = ["Nonlinearity", "Noise", "Delay", "Feedback", "Coupling",
        "Geometry", "Memory", "Conservation"]
KEY = {"pattern": TEAL, "crisis": ROSE, "memory": AMBER, "law": VIOLET, "control": BLUE}
CELLS = [
    (0, 0, "shocks, solitons,\nmode coupling", "law"),
    (0, 1, "stochastic bifurcation,\nnoise-induced jumps", "crisis"),
    (0, 2, "delay-induced oscillations\nand chaos", "crisis"),
    (0, 3, "multistability, hysteresis,\nlimit cycles", "pattern"),
    (0, 4, "pattern formation,\nsynchrony, chimera", "pattern"),
    (0, 5, "shock focusing,\ncaustics, breaking", "crisis"),
    (0, 6, "fractional fronts,\nsubdiffusive shocks", "memory"),
    (0, 7, "weak solutions, entropy\nconditions, shocks", "law"),
    (1, 1, "multiplicative noise,\nheavy tails", "crisis"),
    (1, 2, "transitions triggered\na distance away", "crisis"),
    (1, 3, "stochastic resonance,\nfluctuation theorems", "control"),
    (1, 4, "synchrony by common\nnoise; noise-assisted order", "pattern"),
    (1, 5, "random media,\nanomalous trapping", "memory"),
    (1, 6, "coloured noise,\nfractional FDT", "law"),
    (1, 7, "entropy production,\nsecond law as a budget", "law"),
    (2, 2, "long feedback trains,\nstate-dependent delay", "crisis"),
    (2, 3, "oscillator death,\ncoherence resonance", "pattern"),
    (2, 4, "anticipation,\ntraffic waves", "pattern"),
    (2, 5, "path memory in rays,\ndelayed advection", "memory"),
    (2, 6, "aging, retardation,\nretarded kernels", "memory"),
    (2, 7, "causality as a hard\nconstraint on laws", "law"),
    (3, 3, "nested loops, runaways,\nsaturating growth", "crisis"),
    (3, 4, "adaptive networks,\nattractor memory", "pattern"),
    (3, 5, "shape control,\nmorphoelasticity", "control"),
    (3, 6, "learning, plasticity,\nhysteretic response", "memory"),
    (3, 7, "control of conserved\nquantities; source terms", "control"),
    (4, 4, "network synchronisation,\nmetastable clusters", "pattern"),
    (4, 5, "geometry selects\nthe dynamics", "law"),
    (4, 6, "co-evolving networks,\nreinforcement", "memory"),
    (4, 7, "momentum and mass\nexchange", "law"),
    (5, 5, "hierarchies, fractals,\nconstrictions", "pattern"),
    (5, 6, "trapping, path\ndependence, fingerprints", "memory"),
    (5, 7, "Stokes theorems\non curved space", "law"),
    (6, 6, "hierarchical memory,\naging kernels", "memory"),
    (6, 7, "non-Markov thermo-\ndynamics with memory", "law"),
    (7, 7, "constraints, integrable\ntowers, selection rules", "law"),
]


@figure("intersections-matrix")
def fig_intersections():
    """Where two ideas meet, something neither contains appears."""
    n = len(MECH)
    fig, ax = plt.subplots(figsize=(13.4, 11.4))
    plain(ax, (-2.9, n + 0.15), (-2.0, n + 0.15))
    for k, m in enumerate(MECH):
        ax.text(-0.12, n - k - 0.5, m, ha="right", va="center", fontsize=10.5,
                color=INK, weight="bold")
        ax.text(k + 0.5, n + 0.02, m, ha="left", va="bottom", fontsize=9.5, color=INK,
                rotation=32, rotation_mode="anchor")
    for i, j, text, kind in CELLS:
        col = KEY[kind]
        r, c = n - j - 1, i
        ax.add_patch(FancyBboxPatch((c + 0.04, r + 0.05), 0.92, 0.90,
                                    boxstyle="round,pad=0.004,rounding_size=0.06",
                                    linewidth=1.3, edgecolor=col,
                                    facecolor=col, alpha=0.14, zorder=1))
        ax.text(c + 0.5, r + 0.5, text, ha="center", va="center", fontsize=8.0,
                color=INK, zorder=2, linespacing=1.35)
    for k, (kind, lbl) in enumerate([("pattern", "structure appears"),
                                     ("crisis", "new failure mode"),
                                     ("memory", "the past leaks in"),
                                     ("control", "noise/feedback used as a tool"),
                                     ("law", "a new conservation or constraint")]):
        ax.add_patch(FancyBboxPatch((-2.85, -0.62 - k * 0.19), 0.24, 0.13,
                                    boxstyle="round,pad=0.002,rounding_size=0.05",
                                    linewidth=1.2, edgecolor=KEY[kind], facecolor=KEY[kind],
                                    alpha=0.16))
        ax.text(-2.52, -0.555 - k * 0.19, lbl, va="center", fontsize=9.5, color=KEY[kind])
    ax.text(-2.85, -1.78, "Read the upper triangle only (combinations are symmetric); "
            "colour = the kind of thing that appears.  A curated map, not a measurement.",
            fontsize=9, color=MUTED, style="italic")
    save(fig, "intersections-matrix")


@figure("generative-flow-art")
def fig_flow_art():
    """Chaotic advection: a marbling machine made of two blinking vortices."""
    rng = np.random.default_rng(2)
    n = 40000
    x = rng.uniform(-1.15, 1.15, n)
    y = rng.uniform(-1.15, 1.15, n)
    ang = np.arctan2(y, x)
    a, G, T, dt, steps = 0.62, 0.55, 0.9, 0.01, 1900
    for s in range(steps):
        cx = a if (int(s * dt / T) % 2 == 0) else -a
        dx, dy = x - cx, y
        r2 = dx * dx + dy * dy + 0.02
        xm, ym = x + 0.5 * dt * (-G * dy / r2), y + 0.5 * dt * (G * dx / r2)
        dxm, dym = xm - cx, ym
        rm2 = dxm * dxm + dym * dym + 0.02
        x = x + dt * (-G * dym / rm2)
        y = y + dt * (G * dxm / rm2)
        x = (x + 1.2) % 2.4 - 1.2
        y = (y + 1.2) % 2.4 - 1.2

    R = 780
    rng2 = [[-1.2, 1.2], [-1.2, 1.2]]
    cnt, _, _ = np.histogram2d(x, y, bins=R, range=rng2)
    asum, _, _ = np.histogram2d(x, y, bins=R, range=rng2, weights=ang)
    am = (asum / np.maximum(cnt, 1e-9)).T
    c = cnt.T
    val = np.log1p(c) / np.log1p(c.max())
    hue = np.clip(0.50 + 0.44 * ((am + np.pi) / (2.0 * np.pi)) % 1.0, 0, 1)
    sat = np.where(c > 0, 0.94, 0.0)
    from matplotlib.colors import hsv_to_rgb
    rgb = hsv_to_rgb(np.stack([hue, sat, np.where(c > 0, 0.45 + 0.55 * val, 0.0)], axis=-1))

    fig, ax = plt.subplots(figsize=(7.6, 7.6))
    plain(ax, (-1.2, 1.2), (-1.2, 1.2))
    ax.set_facecolor("#ffffff")
    ax.imshow(rgb, origin="lower", extent=[-1.2, 1.2, -1.2, 1.2], interpolation="bilinear",
              zorder=1)
    ax.text(-1.15, -1.13, "chaotic advection:  two point vortices blinking in turn.\n"
            "The fluid folds, stretches and stirs itself —\n"
            "the same motion that marbles chocolate and rips apart plankton blooms.",
            fontsize=8.6, color="#dbe3f0", va="bottom")
    import matplotlib as mpl
    old_dpi = mpl.rcParams["savefig.dpi"]      # keep the embedded raster small
    mpl.rcParams["savefig.dpi"] = 95
    save(fig, "generative-flow-art")
    mpl.rcParams["savefig.dpi"] = old_dpi


@figure("reaction-diffusion-art")
def fig_reaction_diffusion():
    """Turing patterns: a smooth mixture that refuses to stay smooth."""
    n, steps, dt = 240, 11000, 1.0
    Du, Dv, F, k = 0.16, 0.08, 0.035, 0.060
    rng = np.random.default_rng(8)
    u = np.ones((n, n))
    v = np.zeros((n, n))
    yy, xx = np.ogrid[:n, :n]
    for (cx, cy, r) in [(58, 62, 7), (182, 92, 6), (122, 176, 8), (198, 196, 5), (86, 148, 5)]:
        m = (xx - cx) ** 2 + (yy - cy) ** 2 < r * r
        u[m] = 0.32
        v[m] = 0.27
    v += 0.02 * rng.random((n, n))
    for _ in range(steps):
        lu = np.roll(u, 1, 0) + np.roll(u, -1, 0) + np.roll(u, 1, 1) + np.roll(u, -1, 1) - 4 * u
        lv = np.roll(v, 1, 0) + np.roll(v, -1, 0) + np.roll(v, 1, 1) + np.roll(v, -1, 1) - 4 * v
        uvv = u * v * v
        u = u + dt * (Du * lu - uvv + F * (1.0 - u))
        v = v + dt * (Dv * lv + uvv - (F + k) * v)

    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list(
        "panta", ["#ffffff", "#fff3cd", "#f4b942", "#e8792b", "#0f9b8e", "#2b4c9b", "#3b1d6e"])

    fig, (a, b) = plt.subplots(1, 2, figsize=(12.0, 5.4),
                               gridspec_kw={"width_ratios": [1.15, 1]})
    a.grid(False); a.set_xticks([]); a.set_yticks([])
    a.imshow(v, cmap=cmap, interpolation="bilinear", origin="lower")
    a.set_title("Gray–Scott: two chemicals, one law, endless wallpaper")
    a.text(0.02, 0.02, "grown, never designed", transform=a.transAxes, fontsize=9,
           color="#ffffff")
    for s in a.spines.values():
        s.set_visible(False)

    tidy(b, grid=False)
    kk = np.linspace(0.0, 3.2, 500)
    J = np.array([[1.0, -1.0], [4.0, -3.0]])
    D = np.diag([0.1, 1.0])
    lam = np.array([np.linalg.eigvals(J - (k ** 2) * D).real.max() for k in kk])
    b.plot(kk, lam, color=INK, lw=2.2)
    b.axhline(0, color=MUTED, lw=1.0)
    band = (kk > np.sqrt(2.0)) & (kk < np.sqrt(5.0))
    b.fill_between(kk, 0, lam, where=band, color=ROSE, alpha=0.20)
    b.set_title("Why only some wavelengths survive")
    b.set_xlabel("wavenumber $k$"); b.set_ylabel("growth rate Re $\\lambda(k)$")
    kc = kk[int(np.argmax(lam))]
    b.plot([kc], [lam.max()], "o", color=ROSE, ms=8)
    for k0 in (np.sqrt(2.0), np.sqrt(5.0)):
        b.axvline(k0, color=ROSE, lw=0.9, ls=(0, (3, 3)))
    b.text(1.44, 0.062, "$k_1<k<k_2$ unstable", fontsize=8.8, color=ROSE)
    b.annotate("selected wavelength $\\Lambda=2\\pi/k_c\\approx%.1f$" % (2 * np.pi / kc),
               (kc, lam.max()), (1.7, -0.30), fontsize=8.8, color=INK,
               arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
    b.text(0.05, -0.55, "the uniform state is locally stable (Re$\\,\\lambda(0)<0$),\n"
           "yet diffusion destabilises a band of modes:\nTuring's 1952 insight — "
           "diffusion as a pattern maker,\nnot merely a smoother", fontsize=8.6,
           color=MUTED, style="italic")
    b.set_ylim(-0.78, 0.17)
    import matplotlib as mpl
    old_dpi = mpl.rcParams["savefig.dpi"]      # 240² pattern needs no 1500-px raster
    mpl.rcParams["savefig.dpi"] = 105
    save(fig, "reaction-diffusion-art")
    mpl.rcParams["savefig.dpi"] = old_dpi


@figure("irreversibility-arrow-of-time")
def fig_arrow_of_time():
    """Diffusion erases structure; the erasure is monotone and scale-selective."""
    rng = np.random.default_rng(4)
    N, D = 1024, 0.05
    x = np.linspace(-4.0, 4.0, N, endpoint=False)
    k = np.arange(1, 60)
    amp = rng.normal(0, 1, k.size) / k
    ph = rng.uniform(0, 2 * np.pi, k.size)
    ts = np.linspace(0.0, 2.4, 240)
    field = np.zeros((ts.size, N))
    for j, t in enumerate(ts):
        g = amp * np.exp(-D * k ** 2 * t)
        field[j] = np.sum(g[:, None] * np.cos(2 * np.pi * k[:, None] * x / 8.0
                                              + ph[:, None]), axis=0)

    fig, (a, b, c) = plt.subplots(1, 3, figsize=(13.4, 4.1),
                                  gridspec_kw={"width_ratios": [1.25, 1, 1]})
    a.grid(False)
    a.imshow(field, aspect="auto", origin="lower",
             cmap=LinearSegmentedColormap.from_list(
                 "warmdiv", ["#12318f", "#7fb2ff", "#ffffff", "#ffc07a", "#c2410c"]),
             extent=[0, 8, 0, ts[-1]], interpolation="bilinear")
    a.set_title("Run the clock forward: roughness dissolves")
    a.set_xlabel("space $x$"); a.set_ylabel("time $t$")
    a.text(0.04, 0.95, "read upwards, the same equation is\n'un-mixing' — possible on paper,\n"
           "never observed in a laboratory", transform=a.transAxes, va="top",
           fontsize=8.4, color="#ffe9c9")

    tidy(b)
    for t, col in [(0.5, BLUE), (1.5, TEAL), (3.0, VIOLET)]:
        b.semilogy(k ** 2, np.abs(amp) * np.exp(-D * k ** 2 * t), color=col, lw=1.8,
                   label="$t=%g$" % t)
    b.set_title("Decay $e^{-Dk^2t}$: fine scales die first")
    b.set_xlabel("$k^2$  (inverse length$^2$)"); b.set_ylabel("mode amplitude")
    b.legend(fontsize=8.4)
    b.text(0.03, 0.04, "a straight line here means the\ndecay rate is exactly $Dk^2$. "
           "Small scales vanish first — and they\nare the ones you cannot measure "
           "without noise.", transform=b.transAxes, fontsize=8.4, color=MUTED,
           style="italic", va="bottom")

    tidy(c)
    t2 = np.linspace(-0.4, 3.2, 400)
    sig2 = 0.01 + 2 * D * np.clip(t2, 0, None)
    S = 0.5 * np.log(2 * np.pi * np.e * sig2)
    c.plot(t2[t2 >= 0], S[t2 >= 0], color=VIOLET, lw=2.2)
    c.plot(t2[t2 <= 0], S[t2 <= 0], color=MUTED, lw=1.6, ls=(0, (4, 3)))
    c.axvline(0, color=INK, lw=1.1)
    c.set_title("Coarse-grained entropy only climbs")
    c.set_xlabel("time $t$   (dashed: extrapolated)"); c.set_ylabel("$S=-\\int p\\ln p\\,dx$")
    c.annotate("$S=\\frac{1}{2}\\ln(2\\pi e\\,\\sigma^2)$\n$\\sigma^2=\\sigma_0^2+2Dt$",
               (2.3, S[330]), (0.5, S[330] * 0.55), fontsize=8.6, color=VIOLET,
               arrowprops=dict(arrowstyle="->", color=VIOLET, lw=1.1))
    c.text(-0.36, S[0] - 0.85, "the microscopic law forbids\nnothing: a dropped plate could\n"
           "reassemble. It is the boundary\ncondition on the whole universe\nthat forbids it.",
           fontsize=8.3, color=MUTED)
    save(fig, "irreversibility-arrow-of-time")
