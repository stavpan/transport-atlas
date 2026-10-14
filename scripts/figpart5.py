"""Part 5 — molecular transport (Green / walkers / MSD) and buoyancy convection."""
import numpy as np
import matplotlib.pyplot as plt

from figlib import (figure, save, tidy, plain, INK, MUTED, BLUE, TEAL, VIOLET,
                          AMBER, ROSE, GREEN, SKY)


@figure("diffusion-suite")
def fig_diffusion():
    """Three views of one random walk: Green's function, walkers, MSD."""
    fig, axs = plt.subplots(1, 3, figsize=(11.4, 3.7))
    x = np.linspace(-3.2, 3.2, 600)
    a = tidy(axs[0])
    for t, col in [(0.04, "#111827"), (0.35, BLUE), (1.0, TEAL), (2.5, VIOLET)]:
        a.plot(x, np.exp(-x ** 2 / (4 * t)) / np.sqrt(4 * np.pi * t), color=col,
               label="$t=%.2g$" % t)
    a.legend(loc="upper left")
    a.set_title("Green's function of $\\partial_t c=D\\partial_x^2 c$\n"
                "peak $\\propto t^{-1/2}$, width $\\propto t^{1/2}$, area constant")
    a.set_xlabel("$x/\\sqrt{D}$"); a.set_ylabel("$c\\sqrt{D}$")
    a = tidy(axs[1])
    rng = np.random.default_rng(11)
    n, steps = 5, 4000
    walk = np.cumsum(rng.choice([-1.0, 1.0], size=(n, steps)), axis=1)
    tt = np.arange(steps + 1) / steps
    for i in range(n):
        a.plot(tt, np.concatenate([[0], walk[i]]), lw=1.0, alpha=0.85)
    a.plot(tt, np.sqrt(tt), color="#111827", ls="--", lw=1.6,
           label="$\\pm\\sqrt{t}$: typical spread")
    a.plot(tt, -np.sqrt(tt), color="#111827", ls="--", lw=1.6)
    a.legend(loc="upper left")
    a.set_title("individual walkers\neach step is reversible; the spread is not")
    a.set_xlabel("time (units of $\\Delta x^2/D$)"); a.set_ylabel("displacement")
    a = tidy(axs[2])
    t = np.logspace(-1, 3, 200)
    for alpha, col, lab in [(0.6, BLUE, "subdiffusive $\\alpha=0.6$"),
                            (1.0, "#111827", "normal $\\alpha=1$"),
                            (1.5, TEAL, "superdiffusive $\\alpha=1.5$"),
                            (2.0, ROSE, "ballistic $\\alpha=2$")]:
        a.plot(t, t ** alpha, color=col, label=lab)
    a.set_xscale("log"); a.set_yscale("log")
    a.legend(loc="upper left", fontsize=8.5)
    a.set_title("mean squared displacement\nall four are called 'diffusion'; "
                "only $\\alpha=1$ is Fickian")
    a.set_xlabel("$t$"); a.set_ylabel("$\\langle x^2\\rangle$")
    fig.tight_layout()
    save(fig, "diffusion-suite")


@figure("rayleigh-benard")
def fig_rayleigh():
    """Buoyancy convection: onset, cells, and the resulting transport law."""
    fig, axs = plt.subplots(1, 2, figsize=(9.8, 4.2))
    a = plain(axs[0], (0, 10), (0, 5))
    a.add_patch(plt.Rectangle((0.4, 0.6), 9.2, 0.45, color=ROSE, alpha=0.35))
    a.add_patch(plt.Rectangle((0.4, 4.0), 9.2, 0.45, color=BLUE, alpha=0.35))
    a.text(5.0, 0.82, "hot plate   $T=T_0+\\Delta T$", ha="center", fontsize=9,
           color="#9f1239")
    a.text(5.0, 4.22, "cold plate   $T=T_0$", ha="center", fontsize=9, color="#1e40af")
    for x0 in (0.9, 5.0, 9.1):
        for r in (0.9, 1.5, 2.05):
            a.add_patch(plt.Circle((x0, 2.5), r, fill=False, ec=GREEN, lw=1.3))
    for x0 in (2.95, 7.05):
        for r in (0.9, 1.5, 2.05):
            a.add_patch(plt.Circle((x0, 2.5), r, fill=False, ec=AMBER, lw=1.3, ls="--"))
    a.annotate("rising plume", (0.95, 3.5), (1.7, 3.95), fontsize=8.5, color=GREEN,
               arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.1))
    a.annotate("descending sheet", (7.0, 1.6), (8.1, 0.95), fontsize=8.5, color=AMBER,
               arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.1))
    a.set_title("Rayleigh–Bénard rolls (cross-section)\n"
                "cell width $\\sim$ layer depth; motion costs no external forcing")
    a = tidy(axs[1])
    Ra = np.logspace(3, 12, 400)
    a.loglog(Ra, np.maximum(1, 0.18 * Ra ** (1 / 3)), color=BLUE,
             label="$\\mathrm{Nu}=0.18\\,\\mathrm{Ra}^{1/3}$ (soft turbulence)")
    a.loglog(Ra, np.maximum(1, 0.05 * Ra ** 0.30), color=TEAL, ls="--",
             label="$\\mathrm{Nu}\\sim\\mathrm{Ra}^{0.3}$ (hard turbulence)")
    a.axvline(1708, color=ROSE, ls="--", lw=1.6)
    a.text(1900, 1.25, "$\\mathrm{Ra}_c\\approx1708$\nconduction below:\nno motion at all",
           fontsize=8.5, color=ROSE)
    a.set_xlabel("Rayleigh number $\\mathrm{Ra}=g\\beta\\Delta T L^3/(\\nu\\alpha)$")
    a.set_ylabel("Nusselt number $\\mathrm{Nu}$")
    a.set_title("the payoff: an instability becomes a transport law\n"
                "convection is 'advection that drives itself'")
    a.legend(loc="upper left", fontsize=8.5)
    a.set_ylim(1, 3e3)
    fig.tight_layout()
    save(fig, "rayleigh-benard")
