"""Animated figures (`* .gif`), plus a static filmstrip poster for each one.

    /home/stav/.pixi/envs/sage/bin/python scripts/make_figures.py --gifs

Rationale. A dozen phenomena in this atlas *are* motion — stretching, locking, steepening,
avalanching — and a still frame cannot show them. Each animation here writes two things:

    <name>.gif                     for the web edition (inlined into the single-file build)
    <name>.svg / .pdf / .png       a filmstrip poster: the same thing in four panels, which is
                                   what the print build and the Obsidian vault use

Every animation is deterministic (fixed RNG seeds) so that CI reproduces it bit for bit.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, hsv_to_rgb

from figlib import (figure, save, save_anim, tidy, plain, arrow, box,
                    INK, MUTED, BLUE, TEAL, VIOLET, AMBER, ROSE, SLATE, GREEN, SKY)

PANTA = LinearSegmentedColormap.from_list(
    "panta", ["#070b18", "#1b1b4b", "#5b21b6", "#1f6feb", "#0d9488", "#f0b429", "#fff7d6"])
FLOW = LinearSegmentedColormap.from_list(
    "flow", ["#0b1020", "#123a6b", "#1f6feb", "#0d9488", "#a7f3d0"])
DIVERGING = LinearSegmentedColormap.from_list(
    "div", ["#1f6feb", "#7dd3fc", "#f8fafc", "#fda4af", "#e11d48"])


def filmstrip(name, title, panels, draw, figsize=(10.2, 2.9), note=""):
    """Poster for an animation: `panels` = [(snapshot, label), ...], `draw(ax, snap, first)`."""
    fig, axs = plt.subplots(1, len(panels), figsize=figsize, squeeze=False)
    for k, (snap, lab) in enumerate(panels):
        ax = axs[0][k]
        draw(ax, snap, k == 0)
        ax.set_title(lab, fontsize=9.5)
    fig.suptitle(title, fontsize=11.5, weight="bold", y=1.07)
    if note:
        fig.text(0.5, -0.07, note, ha="center", fontsize=8.6, color=MUTED)
    # a poster carries four raster panels; 110 dpi keeps the vector file, the PDF and the
    # final 3 MB print build honest without bloating either of them.
    import matplotlib as mpl
    old = mpl.rcParams["savefig.dpi"]
    mpl.rcParams["savefig.dpi"] = 110
    save(fig, name)
    mpl.rcParams["savefig.dpi"] = old


@figure("anim-flow-marbling")
def anim_marbling():
    """Chaotic advection in motion: a blob of dye folded into filaments."""
    rng = np.random.default_rng(2)
    n = 6000
    x = rng.uniform(-1.1, 1.1, n)
    y = rng.uniform(-1.1, 1.1, n)
    hue = np.clip((np.arctan2(y, x) + np.pi) / (2 * np.pi), 0, 1)
    a, G, T, dt = 0.62, 0.55, 0.9, 0.01
    nframes, per = 56, 30
    snaps = [(x.copy(), y.copy())]
    for f in range(nframes):
        for s in range(per):
            step = f * per + s
            cx = a if (int(step * dt / T) % 2 == 0) else -a
            dx, dy = x - cx, y
            r2 = dx * dx + dy * dy + 0.02
            xm, ym = x + 0.5 * dt * (-G * dy / r2), y + 0.5 * dt * (G * dx / r2)
            rm2 = (xm - cx) ** 2 + ym * ym + 0.02
            x = x + dt * (-G * ym / rm2)
            y = y + dt * (G * (xm - cx) / rm2)
            x = (x + 1.2) % 2.4 - 1.2
            y = (y + 1.2) % 2.4 - 1.2
        snaps.append((x.copy(), y.copy()))

    cols = hsv_to_rgb(np.stack([0.50 + 0.46 * hue, np.full(n, 0.85),
                                np.full(n, 0.98)], axis=-1))

    def draw(ax, snap, first):
        ax.set_facecolor("#08090f")
        ax.scatter(snap[0], snap[1], s=1.4, c=cols, marker=".", linewidths=0)
        ax.set_xlim(-1.15, 1.15); ax.set_ylim(-1.15, 1.15)
        ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values():
            s.set_color("#2a3448")

    fig, ax = plt.subplots(figsize=(5.8, 4.3))
    pts = ax.scatter(snaps[0][0], snaps[0][1], s=1.4, c=cols, marker=".", linewidths=0)
    ax.set_facecolor("#08090f")
    ax.set_xlim(-1.15, 1.15); ax.set_ylim(-1.15, 1.15)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color("#2a3448")
    ax.set_title("chaotic advection: two blinking vortices, one blob of dye", fontsize=10,
                 color=INK)

    def update(i):
        pts.set_offsets(np.column_stack(snaps[i]))
        return (pts,)

    save_anim("anim-flow-marbling", fig, update, range(len(snaps)), fps=14, hold=10)

    filmstrip("anim-flow-marbling", "Chaotic advection: stretching and folding, forever",
              [(snaps[0], "t = 0"), (snaps[18], "$t$"), (snaps[36], "$t$"),
               (snaps[-1], "$t$")],
              draw, figsize=(10.4, 2.85),
              note="pure kinematics — no forces: a smooth incompressible flow that never repeats. "
                   "The dye becomes infinitely thin filaments without ever mixing.")


@figure("anim-turing-growth")
def anim_turing():
    """A Turing pattern growing: seeds spread, fronts compete, a wavelength wins."""
    n, steps, dt = 170, 2600, 1.0
    Du, Dv, F, k = 0.16, 0.08, 0.035, 0.060
    rng = np.random.default_rng(8)
    u = np.ones((n, n))
    v = np.zeros((n, n))
    yy, xx = np.ogrid[:n, :n]
    for (cx, cy, r) in [(40, 40, 5), (130, 60, 4), (85, 120, 6), (60, 95, 4)]:
        m = (xx - cx) ** 2 + (yy - cy) ** 2 < r * r
        u[m] = 0.32
        v[m] = 0.27
    v += 0.02 * rng.random((n, n))

    nframes, per = 60, steps // 60
    snaps = []
    for f in range(nframes):
        for _ in range(per):
            lu = (np.roll(u, 1, 0) + np.roll(u, -1, 0) + np.roll(u, 1, 1)
                  + np.roll(u, -1, 1) - 4 * u)
            lv = (np.roll(v, 1, 0) + np.roll(v, -1, 0) + np.roll(v, 1, 1)
                  + np.roll(v, -1, 1) - 4 * v)
            uvv = u * v * v
            u = u + dt * (Du * lu - uvv + F * (1.0 - u))
            v = v + dt * (Dv * lv + uvv - (F + k) * v)
        snaps.append(v.copy())
    vmax = float(np.percentile(snaps[-1], 99.5))

    def draw(ax, snap, first):
        ax.grid(False); ax.set_xticks([]); ax.set_yticks([])
        ax.imshow(snap, cmap=PANTA, vmin=0, vmax=vmax, interpolation="bilinear", origin="lower")
        for s in ax.spines.values():
            s.set_visible(False)

    fig, ax = plt.subplots(figsize=(5.2, 4.4))
    im = ax.imshow(snaps[0], cmap=PANTA, vmin=0, vmax=vmax, interpolation="bilinear",
                   origin="lower")
    ax.grid(False); ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_title("Gray–Scott: two chemicals, one wavelength, endless wallpaper", fontsize=10)

    def update(i):
        im.set_data(snaps[i])
        return (im,)

    save_anim("anim-turing-growth", fig, update, range(nframes), fps=16, hold=10)

    filmstrip("anim-turing-growth", "Turing patterns: how a smooth state chooses a size",
              [(snaps[0], "seeded"), (snaps[15], "spreading"), (snaps[35], "competing"),
               (snaps[-1], "settled")], draw, figsize=(10.0, 3.1),
              note="each spot grows until its own depletion zone stops it: the wavelength is set "
                   "by a competition between two diffusion lengths, not by the seeds.")


@figure("anim-kuramoto-locking")
def anim_kuramoto():
    """Coupled oscillators locking as the coupling is turned up past the threshold."""
    rng = np.random.default_rng(5)
    N, gamma, dt = 300, 0.5, 0.02
    w = np.clip(gamma * np.tan(np.pi * (rng.random(N) - 0.5)), -25, 25)
    Kc = 2.0 * gamma
    th = rng.uniform(0, 2 * np.pi, N)
    nframes, per = 72, 60
    Ks, rs, ph = [], [], []
    for f in range(nframes):
        K = 2.7 * f / (nframes - 1)
        for _ in range(per):
            z = np.exp(1j * th).mean()
            th = th + dt * (w + K * abs(z) * np.sin(np.angle(z) - th))
        z = np.exp(1j * th).mean()
        Ks.append(K); rs.append(abs(z)); ph.append(np.exp(1j * th))
    Ks, rs = np.array(Ks), np.array(rs)
    cw = np.clip((w + 3.0) / 6.0, 0, 1)
    circle = np.linspace(0, 2 * np.pi, 240)

    def circle_ax(ax, j, label):
        z = ph[j]
        ax.scatter(z.real, z.imag, c=cw, cmap="turbo", s=13, alpha=0.9, linewidths=0)
        ax.plot(rs[j] * np.cos(circle), rs[j] * np.sin(circle), color=INK, lw=1.4, alpha=0.7)
        ax.plot([0, rs[j] * np.cos(np.angle(z.mean()))], [0, rs[j] * np.sin(np.angle(z.mean()))],
                color=ROSE, lw=2.2, solid_capstyle="round")
        ax.add_patch(plt.Circle((0, 0), 1, fill=False, color="#c9cfda", lw=0.9))
        plain(ax, (-1.18, 1.18), (-1.18, 1.18))
        ax.set_title(label, fontsize=9.5)

    fig, (a, b) = plt.subplots(1, 2, figsize=(8.8, 4.0),
                               gridspec_kw={"width_ratios": [1, 1.15]})
    a.set_aspect("equal")
    a.add_patch(plt.Circle((0, 0), 1, fill=False, color="#c9cfda", lw=0.9))
    sc = a.scatter(ph[0].real, ph[0].imag, c=cw, cmap="turbo", s=13, linewidths=0)
    ring, = a.plot([], [], color=INK, lw=1.4, alpha=0.7)
    meanv, = a.plot([], [], color=ROSE, lw=2.2, solid_capstyle="round")
    t0 = a.text(-1.14, 1.05, "K = 0.00   r = 0.00", fontsize=9, color=INK)
    plain(a, (-1.18, 1.18), (-1.18, 1.18))
    a.set_title("phases on the circle  (colour = natural frequency)", fontsize=9.5)

    tidy(b)
    b.plot(Ks, np.sqrt(np.maximum(1 - Kc / np.maximum(Ks, 1e-9), 0)), color=MUTED, lw=1.3,
           ls=(0, (4, 3)), label="$r=\\sqrt{1-K_c/K}$ (theory)")
    line, = b.plot([], [], color=BLUE, lw=2.2, label="simulated $N=300$")
    b.axvline(Kc, color=ROSE, lw=1.1)
    b.text(Kc + 0.05, 0.06, "$K_c=2/\\pi g(0)$", fontsize=9, color=ROSE, rotation=90,
           va="bottom")
    b.set_xlim(-0.05, 2.75); b.set_ylim(-0.02, 1.02)
    b.set_xlabel("coupling $K$"); b.set_ylabel("order parameter $r$")
    b.legend(fontsize=8.4, loc="upper left")
    b.set_title("order parameter vs coupling", fontsize=9.5)

    def update(i):
        z = ph[i]
        sc.set_offsets(np.column_stack([z.real, z.imag]))
        ring.set_data(rs[i] * np.cos(circle), rs[i] * np.sin(circle))
        mv = z.mean()
        meanv.set_data([0, abs(mv) * np.cos(np.angle(mv))], [0, abs(mv) * np.sin(np.angle(mv))])
        t0.set_text("K = %.2f   r = %.2f" % (Ks[i], rs[i]))
        line.set_data(Ks[:i + 1], rs[:i + 1])
        return sc, ring, meanv, t0, line

    save_anim("anim-kuramoto-locking", fig, update, range(nframes), fps=14, hold=10)

    fig2 = plt.figure(figsize=(10.2, 2.9))
    gs = fig2.add_gridspec(1, 4, wspace=0.22)
    for k, j in enumerate([0, 24, 48, nframes - 1]):
        circle_ax(fig2.add_subplot(gs[k]), j, "K = %.2f, r = %.2f" % (Ks[j], rs[j]))
    fig2.suptitle("Kuramoto: a sharp threshold, then a square-root rise in order",
                  fontsize=11.5, weight="bold", y=1.05)
    fig2.text(0.5, -0.06, "below $K_c$ the spread of natural frequencies wins; above it a locked "
               "cluster forms, with drifting outliers that no amount of coupling removes.",
               ha="center", fontsize=8.6, color=MUTED)
    save(fig2, "anim-kuramoto-locking")


@figure("anim-shock-formation")
def anim_shock():
    """Nonlinearity with no dissipation: a smooth wave steepens into a shock."""
    N, L, cfl = 900, 2 * np.pi, 0.4
    x = np.linspace(0, L, N, endpoint=False)
    dx = L / N
    u0 = np.sin(x)
    u = u0.copy()
    nframes, per = 60, 275
    snaps, times, t = [], [], 0.0
    for f in range(nframes):
        for _ in range(per):
            dt = cfl * dx / max(float(np.abs(u).max()), 1e-9)
            fh = 0.5 * u * u
            u = 0.5 * (np.roll(u, -1) + np.roll(u, 1)) \
                - 0.5 * (dt / dx) * (np.roll(fh, -1) - np.roll(fh, 1))
            t += dt
        snaps.append(u.copy()); times.append(t)

    def shock_pos(snap):
        return int(np.argmin(np.gradient(snap)))

    def draw(ax, snap, first, t=None):
        tidy(ax)
        ax.plot(x, u0, color=MUTED, lw=1.2, ls=(0, (4, 3)))
        ax.plot(x, snap, color=BLUE, lw=2.4)
        k = shock_pos(snap)
        if t is None or t > 0.55:
            ax.annotate("the shock", (x[k], snap[k]), (x[k] - 1.15, 0.72), fontsize=9.6,
                        color=ROSE, arrowprops=dict(arrowstyle="->", color=ROSE, lw=1.2))
        ax.set_ylim(-1.25, 1.25); ax.set_xlim(0, L)
        ax.set_xlabel("$x$"); ax.set_ylabel("$u$")
        ax.axhline(0, color="#c9cfda", lw=0.8)

    fig, ax = plt.subplots(figsize=(7.6, 3.8))
    (u0_line,) = ax.plot(x, u0, color=MUTED, lw=1.2, ls=(0, (4, 3)), label="initial profile")
    (line,) = ax.plot(x, u0, color=BLUE, lw=2.4, label="solution")
    note = ax.annotate("", (0, 0), (0, 0), fontsize=9.6, color=ROSE,
                       arrowprops=dict(arrowstyle="->", color=ROSE, lw=1.2))
    note.set_visible(False)
    tidy(ax)
    ax.axhline(0, color="#c9cfda", lw=0.8)
    ax.set_ylim(-1.25, 1.25); ax.set_xlim(0, L)
    ax.set_xlabel("$x$"); ax.set_ylabel("$u$")
    ax.legend(fontsize=8.6, loc="upper right")
    heading = ax.set_title("$u_t+u\\,u_x=0$ — nonlinearity with nothing to stop it",
                           fontsize=10.5)

    def update(i):
        snap, t = snaps[i], times[i]
        line.set_ydata(snap)
        k = shock_pos(snap)
        note.set_visible(t > 0.55)
        if t > 0.55:
            note.xy = (x[k], snap[k]); note.set_position((x[k] - 1.15, 0.72))
        heading.set_text("$u_t+u\\,u_x=0$   ·   t = %.2f   ·   characteristics collide at $t=1$"
                         % t)
        return line, note, heading

    save_anim("anim-shock-formation", fig, update, range(nframes), fps=16, hold=10)

    tsel = [0, int(0.55 * nframes), int(0.95 * nframes), nframes - 1]
    filmstrip("anim-shock-formation", "How a smooth wave makes its own discontinuity",
              [(snaps[j], "t ≈ %.1f" % times[j]) for j in tsel],
              lambda ax, snap, first, j=None: draw(ax, snap, first, t=1.0), figsize=(10.4, 2.9),
              note="inviscid Burgers, smooth initial data, no viscosity anywhere: the fast part of "
                   "the wave catches up the slow part at a finite time, and the solution ceases to "
                   "be differentiable — the reason conservation laws need weak solutions.")


@figure("anim-lorenz-divergence")
def anim_lorenz():
    """Two trajectories a millionth apart: the butterfly, and the horizon it destroys."""
    def run(s0, n, dt=0.005):
        s = np.array(s0, float)
        out = np.empty((n, 3))
        for i in range(n):
            def f(y):
                return np.array([10.0 * (y[1] - y[0]),
                                 y[0] * (28.0 - y[2]) - y[1],
                                 y[0] * y[1] - (8.0 / 3.0) * y[2]])
            k1 = f(s); k2 = f(s + 0.5 * dt * k1)
            k3 = f(s + 0.5 * dt * k2); k4 = f(s + dt * k3)
            s = s + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
            out[i] = s
        return out

    dt = 0.005
    A = run([1.0, 1.0, 1.0], 9000, dt)
    B = run([1.0 + 1e-6, 1.0, 1.0], 9000, dt)
    d = np.linalg.norm(A - B, axis=1)
    t = np.arange(A.shape[0]) * dt
    nframes = 64
    idx = [int(k * (A.shape[0] - 1) / (nframes - 1)) for k in range(nframes)]

    fig, (a, b) = plt.subplots(1, 2, figsize=(9.0, 4.0),
                               gridspec_kw={"width_ratios": [1.05, 1]})
    tidy(a, grid=False)
    la, = a.plot([], [], color=BLUE, lw=0.8, alpha=0.9, label="trajectory 1")
    lb, = a.plot([], [], color=ROSE, lw=0.8, alpha=0.9, label="trajectory 2 ($\\varepsilon=10^{-6}$)")
    a.set_xlabel("$x$"); a.set_ylabel("$z$")
    a.legend(fontsize=8.4, loc="upper right")
    a.set_title("the same laws, the same butterfly", fontsize=9.8)
    a.set_xlim(-22, 22); a.set_ylim(2, 48)

    tidy(b)
    ln, = b.semilogy([], [], color=VIOLET, lw=2.0)
    b.semilogy(t, 1e-6 * np.exp(0.906 * t), color=MUTED, lw=1.2, ls=(0, (4, 3)),
               label="slope $\\lambda\\approx0.91$")
    b.axvline(1.0 / 0.906, color=ROSE, lw=1.0)
    b.text(1.25, 2e-6, "Lyapunov time $t_\\lambda$", fontsize=8.8, color=ROSE, rotation=90,
           va="bottom")
    b.set_xlim(0, t[-1]); b.set_ylim(1e-7, 60)
    b.set_xlabel("time $t$"); b.set_ylabel("separation $|\\delta|$")
    b.set_title("then the separation saturates", fontsize=9.8)
    b.legend(fontsize=8.4, loc="lower right")
    stamp = b.text(0.04, 0.93, "", transform=b.transAxes, fontsize=9.4, color=INK)

    def update(i):
        k = idx[i]
        la.set_data(A[:k, 0], A[:k, 2])
        lb.set_data(B[:k, 0], B[:k, 2])
        ln.set_data(t[:k], d[:k])
        stamp.set_text("$t$ = %.1f"% t[k] + ("" if d[k] < 1 else "   —  horizons gone"))
        return la, lb, ln, stamp

    save_anim("anim-lorenz-divergence", fig, update, range(nframes), fps=16, hold=10)

    fig2, (c, e) = plt.subplots(1, 2, figsize=(10.0, 3.6))
    tidy(c, grid=False)
    c.plot(A[:, 0], A[:, 2], color=BLUE, lw=0.7, label="trajectory 1")
    c.plot(B[:, 0], B[:, 2], color=ROSE, lw=0.7, label="trajectory 2")
    c.set_xlabel("$x$"); c.set_ylabel("$z$"); c.legend(fontsize=8.6)
    c.set_title("same butterfly, different futures", fontsize=10)
    tidy(e)
    e.semilogy(t, d, color=VIOLET, lw=1.8)
    e.semilogy(t, 1e-6 * np.exp(0.906 * t), color=MUTED, lw=1.2, ls=(0, (4, 3)))
    e.annotate("exponential growth, $\\lambda\\approx0.91$", (16, 1.0), (7.0, 2e-4),
               fontsize=9, color=MUTED,
               arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.0))
    e.annotate("saturation at the size of the attractor", (30, 12), (11, 22), fontsize=9,
               color=ROSE, arrowprops=dict(arrowstyle="->", color=ROSE, lw=1.0))
    e.set_xlabel("time $t$"); e.set_ylabel("$|\\delta|$")
    e.set_title("why forecasting dies: the horizon is finite and computable", fontsize=10)
    fig2.tight_layout()
    save(fig2, "anim-lorenz-divergence")


@figure("anim-soc-avalanches")
def anim_soc():
    """A slowly driven sandpile: avalanches of every size, and a power law assembling itself."""
    rng = np.random.default_rng(11)
    L = 64
    g = np.zeros((L, L), dtype=np.int64)

    def drop():
        nonlocal g                       # the pile is rebound in place, not copied
        g[rng.integers(L), rng.integers(L)] += 1
        edge = np.zeros((L, L), bool)
        size = 0
        for _ in range(20000):
            un = g >= 4
            c = int(un.sum())
            if c == 0:
                break
            size += c
            edge |= un
            g -= 4 * un
            g[1:, :] += un[:-1, :]
            g[:-1, :] += un[1:, :]
            g[:, 1:] += un[:, :-1]
            g[:, :-1] += un[:, 1:]
        return size, edge

    for _ in range(1200):                      # relax into the critical state
        drop()

    nframes, per = 56, 55
    sizes, grids, tops, marked = [], [], [], []
    for f in range(nframes):
        seen = np.zeros((L, L), bool)
        sz = 0
        for _ in range(per):
            s, ed = drop()
            sz += s
            seen |= ed
        sizes.append(sz)
        grids.append(g.copy())
        marked.append(seen)

    real = np.array([s for s in sizes if s > 0], float)
    bins = np.logspace(0, np.log10(max(real.max(), 10) + 1), 22)
    mid = np.sqrt(bins[1:] * bins[:-1])

    mask_col = ((0.42, 0.05, 0.35), (1.0, 0.75, 0.15))

    def pile_ax(ax, snap, edge, title):
        ax.imshow(snap, cmap="magma", vmin=0, vmax=6, interpolation="nearest", origin="lower")
        ov = np.ma.masked_where(~edge, np.ones_like(snap, float))
        ax.imshow(ov, cmap=LinearSegmentedColormap.from_list("hot", mask_col),
                  interpolation="nearest", origin="lower", alpha=0.75, vmin=0, vmax=1)
        ax.grid(False); ax.set_xticks([]); ax.set_yticks([])
        ax.set_title(title, fontsize=9.5)

    fig, (a, b) = plt.subplots(1, 2, figsize=(9.0, 4.0),
                               gridspec_kw={"width_ratios": [1, 1.1]})
    im = a.imshow(grids[0], cmap="magma", vmin=0, vmax=6, interpolation="nearest",
                  origin="lower")
    ov = a.imshow(np.ma.masked_where(~marked[0], np.ones((L, L))),
                  cmap=LinearSegmentedColormap.from_list("hot", mask_col),
                  interpolation="nearest", origin="lower", alpha=0.75, vmin=0, vmax=1)
    a.grid(False); a.set_xticks([]); a.set_yticks([])
    a.set_title("the pile, and where it just collapsed", fontsize=9.5)

    tidy(b)
    (hl,) = b.loglog([], [], "o", color=BLUE, ms=4.5)
    (fit,) = b.loglog([], [], color=ROSE, lw=1.8)
    b.set_xlim(1, bins[-1]); b.set_ylim(2e-5, 2)
    b.set_xlabel("avalanche size $s$ (topplings)"); b.set_ylabel("$P(s)$")
    b.set_title("the distribution, as it assembles", fontsize=9.5)
    cap = b.text(0.03, 0.06, "", transform=b.transAxes, fontsize=9, color=INK)

    def hist(sz):
        v = sz[sz > 0]
        if v.size < 8:
            return np.array([]), np.array([]), 0.0
        cnt, _ = np.histogram(v, bins=bins)
        dens = cnt / np.diff(bins) / v.size
        ok = cnt >= 3
        if ok.sum() < 3:
            return mid[ok], dens[ok], 0.0
        slope = np.polyfit(np.log(mid[ok]), np.log(dens[ok]), 1)[0]
        return mid[ok], dens[ok], -slope

    def update(i):
        sub = np.array(sizes[:i + 1], float)
        im.set_data(grids[i])
        ov.set_data(np.ma.masked_where(~marked[i], np.ones((L, L))))
        m, dd, tau = hist(sub)
        hl.set_data(m, dd)
        if m.size:
            fit.set_data(m, np.exp(np.polyval(np.polyfit(np.log(m), np.log(dd), 1), np.log(m))))
            cap.set_text("%d drops   ·   fitted $\\tau$ = %.2f   ·   biggest: %d"
                         % (per * (i + 1), tau, int(sub.max())))
        else:
            cap.set_text("%d drops" % (per * (i + 1)))
        return im, ov, hl, fit, cap

    save_anim("anim-soc-avalanches", fig, update, range(nframes), fps=12, hold=10)

    fig2, (c, e) = plt.subplots(1, 2, figsize=(10.0, 3.7),
                                gridspec_kw={"width_ratios": [1, 1.15]})
    pile_ax(c, grids[-1], marked[-1], "the critical pile: one more grain may do nothing — or everything")
    tidy(e)
    cnt, _ = np.histogram(real, bins=bins)
    dens = cnt / np.diff(bins) / real.size
    ok = cnt >= 3
    e.loglog(mid[ok], dens[ok], "o", color=BLUE, ms=5)
    slope = np.polyfit(np.log(mid[ok]), np.log(dens[ok]), 1)[0]
    e.loglog(mid[ok], np.exp(np.polyval(np.polyfit(np.log(mid[ok]), np.log(dens[ok]), 1),
                                        np.log(mid[ok]))), color=ROSE, lw=1.8)
    e.set_xlabel("avalanche size $s$"); e.set_ylabel("$P(s)$")
    e.set_title("power law over three decades, $\\tau_{fit}=%.2f$" % (-slope), fontsize=10)
    e.annotate("the tail is cut off by the\nsize of the box, not by physics",
               (bins[-2], dens[ok][-1] * 4), (12, 4e-5), fontsize=8.8, color=MUTED,
               arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.0))
    fig2.suptitle("Self-organised criticality: slow drive, fast relaxation, no tuning",
                  fontsize=11.5, weight="bold", y=1.02)
    save(fig2, "anim-soc-avalanches")


@figure("anim-coarsening")
def anim_coarsening():
    """Spinodal decomposition: one length scale, growing as $t^{1/3}$ — scaling you can watch."""
    rng = np.random.default_rng(3)
    n = 128
    kx = np.fft.fftfreq(n) * 2 * np.pi
    KX, KY = np.meshgrid(kx, kx, indexing="ij")
    k2 = KX ** 2 + KY ** 2
    c = 0.02 * rng.standard_normal((n, n))
    dt, kappa, M = 0.5, 1.0, 1.0
    denom = 1.0 + dt * M * kappa * k2 ** 2
    nframes, per = 60, 44
    snaps, spectra = [], []
    for f in range(nframes):
        for _ in range(per):
            ch = np.fft.fft2(c)
            nl = np.fft.fft2(c ** 3 - c)
            ch = (ch - dt * M * k2 * nl) / denom
            c = np.fft.ifft2(ch).real
        snaps.append(c.copy())
        sh = np.abs(np.fft.fft2(c - c.mean())) ** 2 / c.size
        spectra.append(sh)

    tg = np.abs(np.sqrt(k2).ravel())
    kb = np.linspace(0.05, 2.2, 120)
    idxb = np.digitize(tg, kb)
    tspan = np.arange(1, nframes + 1) * per * dt

    def radial(sh):
        s = np.zeros(kb.size)
        for j in range(1, kb.size + 1):
            m = idxb == j
            if m.any():
                s[j - 1] = sh.ravel()[m].mean()
        return s

    def peak(sh):
        s = radial(sh)
        j = int(np.argmax(s[3:])) + 3
        return kb[j], s[j]

    def draw(ax, snap, first):
        ax.imshow(snap, cmap=DIVERGING, vmin=-1, vmax=1, interpolation="bilinear",
                  origin="lower")
        ax.grid(False); ax.set_xticks([]); ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)

    fig, (a, b) = plt.subplots(1, 2, figsize=(9.2, 4.0),
                               gridspec_kw={"width_ratios": [1, 1.1]})
    im = a.imshow(snaps[0], cmap=DIVERGING, vmin=-1, vmax=1, interpolation="bilinear",
                  origin="lower")
    a.grid(False); a.set_xticks([]); a.set_yticks([])
    for s in a.spines.values():
        s.set_visible(False)
    a.set_title("spinodal decomposition: up/down domains", fontsize=9.5)

    tidy(b)
    ln, = b.loglog([], [], color=BLUE, lw=1.8, label="$S(k)$ now")
    pk, = b.loglog([], [], "o", color=ROSE, ms=8, label="peak: the selected size")
    b.loglog(kb, 2.0e-4 * kb ** -3.0, color=MUTED, lw=1.1, ls=(0, (4, 3)),
             label="$k^{-3}$ (Porod-type, 2-D)")
    b.set_xlim(0.05, 2.2); b.set_ylim(1e-7, 3e-3)
    b.set_xlabel("wavenumber $k$"); b.set_ylabel("structure factor $S(k)$")
    b.legend(fontsize=8.2, loc="lower left")
    b.set_title("the peak walks to the left: domains grow", fontsize=9.5)
    stamp = b.text(0.04, 0.9, "", transform=b.transAxes, fontsize=9.2, color=INK)

    def update(i):
        im.set_data(snaps[i])
        s = radial(spectra[i])
        ln.set_data(kb, np.maximum(s, 1e-8))
        kp, vp = peak(spectra[i])
        pk.set_data([kp], [vp])
        size = 2 * np.pi / kp
        stamp.set_text("$t$ = %4d     domain size $\\sim$ %.0f cells" % (tspan[i], size))
        return im, ln, pk, stamp

    save_anim("anim-coarsening", fig, update, range(nframes), fps=14, hold=10)

    sel = [0, nframes // 3, 2 * nframes // 3, nframes - 1]
    filmstrip("anim-coarsening", "Coarsening: the pattern grows without changing its shape",
              [(snaps[j], "$t$ = %d" % tspan[j]) for j in sel], draw, figsize=(10.2, 2.9),
              note="a random mixture of two phases separates, then the domains merge: the "
                   "structure factor keeps its shape and moves as a whole — self-similarity in "
                   "time, the same collapse as in the finite-size scaling of the critical notes.")