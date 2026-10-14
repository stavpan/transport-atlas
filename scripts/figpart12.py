"""Part 12 — self-organised criticality and synchronisation."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from figlib import (figure, save, tidy, plain, arrow, box,
                    INK, MUTED, BLUE, TEAL, VIOLET, AMBER, ROSE, SLATE, GREEN, SKY)


@figure("soc-avalanche-statistics")
def fig_soc_avalanches():
    """A slowly driven, dissipative sandpile: power laws without tuning."""
    rng = np.random.default_rng(11)
    L = 64
    g = np.zeros((L, L), dtype=np.int64)
    sizes = []
    for drop in range(13000):
        g[rng.integers(L), rng.integers(L)] += 1
        s = 0
        for _ in range(20000):
            un = g >= 4
            c = int(un.sum())
            if c == 0:
                break
            s += c
            g -= 4 * un
            g[1:, :] += un[:-1, :]
            g[:-1, :] += un[1:, :]
            g[:, 1:] += un[:, :-1]
            g[:, :-1] += un[:, 1:]
        if drop >= 2000 and s > 0:
            sizes.append(s)
    sizes = np.array(sizes, float)

    edges = np.logspace(0, np.log10(sizes.max() + 1), 30)
    cnt, _ = np.histogram(sizes, bins=edges)
    dens = cnt / np.diff(edges) / sizes.size
    mid = np.sqrt(edges[1:] * edges[:-1])
    good = (cnt >= 25) & (mid > 3)

    fig, (a, b) = plt.subplots(1, 2, figsize=(11.2, 4.2),
                               gridspec_kw={"width_ratios": [1.1, 1]})
    tidy(a)
    a.loglog(mid[good], dens[good], "o", color=BLUE, ms=5, label="measured avalanches")
    fit = np.polyfit(np.log(mid[good]), np.log(dens[good]), 1)
    a.loglog(mid[good], np.exp(fit[1]) * mid[good] ** fit[0], color=ROSE, lw=1.8,
             label="power law, $\\tau_{fit}=%.2f$" % (-fit[0]))
    a.set_title("Where sandpiles live: at the critical slope")
    a.set_xlabel("avalanche size $s$ (topplings)"); a.set_ylabel("$P(s)$")
    a.legend(fontsize=8.6)
    a.annotate("the tail is cut off not by a\nscale in the physics, but by the\nsize of the box: $s\\lesssim L^D$",
               (sizes.max() * 0.5, dens[good][-3] * 3), (7.0, 1e-6), fontsize=8.5,
               color=MUTED, arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.0))
    a.text(1.4, 1.5e-3, "$\\tau\\approx1.2$: the same exponent as\nearthquakes, forest fires, "
           "neuronal\navalanches and solar flares", fontsize=8.6, color=VIOLET)

    a2 = b
    a2.set_title("The pile that never settles")
    im = a2.imshow(g, cmap="magma", interpolation="nearest", origin="lower")
    a2.grid(False); a2.set_xticks([]); a2.set_yticks([])
    cb = plt.colorbar(im, ax=a2, fraction=0.045, pad=0.02)
    cb.set_label("grains (never $\\geq 4$ for long)", fontsize=8.4)
    a2.text(0.02, 0.96, "driven so slowly that nothing happens;\nrelaxed so fast that everything "
            "can happen:\nno parameter is tuned, yet the statistics\nare scale-free",
            transform=a2.transAxes, va="top", fontsize=8.4, color="#ffffff")
    save(fig, "soc-avalanche-statistics")


@figure("kuramoto-synchronisation")
def fig_kuramoto():
    """Coupled oscillators: a threshold, a phase transition, and an order parameter."""
    rng = np.random.default_rng(5)
    N, gamma, dt = 400, 0.5, 0.02
    w = np.clip(gamma * np.tan(np.pi * (rng.random(N) - 0.5)), -25, 25)
    Kc = 2.0 * gamma

    def evolve(K, steps, th):
        for _ in range(steps):
            z = np.exp(1j * th).mean()
            th = th + dt * (w + K * abs(z) * np.sin(np.angle(z) - th))
        return th

    Ks = np.linspace(0.0, 3.0, 40)
    rs = []
    for K in Ks:
        th = evolve(K, 4000, rng.uniform(0, 2 * np.pi, N))
        vals = []
        for _ in range(500):
            z = np.exp(1j * th).mean()
            vals.append(abs(z))
            th = evolve(K, 1, th)
        rs.append(np.mean(vals))
    rs = np.array(rs)

    fig = plt.figure(figsize=(12.2, 4.0))
    gs = fig.add_gridspec(1, 3, width_ratios=[1.5, 1, 1], wspace=0.28)
    a = fig.add_subplot(gs[0])
    tidy(a)
    Kt = np.linspace(Kc, 3.0, 200)
    a.plot(Kt, np.sqrt(np.maximum(1.0 - Kc / Kt, 0)), color=MUTED, lw=1.6, ls=(0, (4, 3)),
           label="theory $r=\\sqrt{1-K_c/K}$")
    a.plot(Ks, rs, "o-", color=BLUE, lw=2.0, ms=4, label="simulation, $N=400$")
    a.axvline(Kc, color=ROSE, lw=1.1)
    a.set_title("Kuramoto: order appears at a threshold")
    a.set_xlabel("coupling $K$"); a.set_ylabel("order parameter $r=|\\langle e^{i\\theta}\\rangle|$")
    a.legend(fontsize=8.5, loc="upper left")
    a.text(Kc + 0.06, 0.06, "$K_c=2/\\pi g(0)=2\\gamma$", fontsize=9, color=ROSE, rotation=90,
           va="bottom")
    a.annotate("below threshold the spread of\nnatural frequencies wins", (0.45, 0.03), (0.55, 0.42),
               fontsize=8.4, color=MUTED, arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.0))

    for j, (K, ttl) in enumerate([(0.4, "below $K_c$: incoherent"),
                                  (2.5, "above $K_c$: locked cluster")]):
        ax = fig.add_subplot(gs[j + 1])
        th = evolve(K, 4000, rng.uniform(0, 2 * np.pi, N))
        c = np.clip((w + 3.0) / 6.0, 0, 1)
        ax.scatter(np.cos(th), np.sin(th), c=c, cmap="turbo", s=11, alpha=0.85)
        ax.add_patch(Circle((0, 0), 1, fill=False, color="#c9cfda", lw=1.0))
        plain(ax, (-1.25, 1.25), (-1.25, 1.25))
        ax.set_title(ttl, fontsize=10)
        ax.text(0, 1.02, "colour = natural frequency $\\omega$", fontsize=8, color=MUTED,
                ha="center")
    save(fig, "kuramoto-synchronisation")
