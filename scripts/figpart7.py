"""Part 7 — moving fronts (reaction-diffusion & Stefan) and barrier escape."""
import numpy as np
import matplotlib.pyplot as plt

from figlib import (figure, save, tidy, INK, MUTED, BLUE, TEAL, VIOLET, AMBER,
                          ROSE, GREEN, SKY)


@figure("fronts-and-stefan")
def fig_fronts():
    """Two moving fronts: a reaction-diffusion wave and a phase boundary."""
    fig, axs = plt.subplots(1, 2, figsize=(9.8, 4.2))
    a = tidy(axs[0])
    x = np.linspace(-25, 70, 1200)
    for t, col in [(2, "#111827"), (8, BLUE), (18, TEAL), (32, VIOLET)]:
        a.plot(x, 1.0 / (1 + np.exp((x - 2 * t) / 1.0)), color=col, label="$t=%g$" % t)
    a.annotate("$c=2\\sqrt{Dk}$ is selected\nby the leading edge,\nnot by the bulk",
               (2 * 18 + 8, 0.2), (2 * 18 + 14, 0.62), fontsize=8.5, color=VIOLET,
               arrowprops=dict(arrowstyle="->", color=VIOLET, lw=1.1))
    a.set_xlabel("$x$"); a.set_ylabel("$c$")
    a.set_title("Fisher–KPP travelling wave\n$\\partial_t c=D\\partial_x^2 c+kc(1-c)$")
    a.legend(fontsize=8.5, loc="center right")
    a = tidy(axs[1])
    lam = 0.7
    for t, col in zip([0.25, 1.0, 2.25, 4.0], ["#111827", BLUE, TEAL, VIOLET]):
        s = 2 * lam * np.sqrt(t)
        xx = np.linspace(0, 2.6, 500)
        a.plot(xx, np.maximum(0.0, 1 - (s - xx) / max(s, 1e-9)), color=col,
               label="$t=%.2f$" % t)
    a2 = a.twinx()
    tt = np.linspace(0.01, 4.2, 300)
    a2.plot(tt, 2 * lam * np.sqrt(tt), color=ROSE, lw=2.2, ls="--")
    a2.set_ylabel("interface position $s$", color=ROSE)
    a2.tick_params(colors=ROSE); a2.grid(False)
    a.text(1.6, 0.83, "$s(t)=2\\lambda\\sqrt{\\alpha t}$\nlatent heat slows the\n"
           "boundary to a $\\sqrt{t}$ crawl", fontsize=8.5, color=ROSE)
    a.set_xlabel("$x$"); a.set_ylabel("$T$")
    a.set_title("Stefan problem (one-phase melting)\n"
                "a free boundary whose position is an output, not an input")
    a.legend(fontsize=8, loc="lower right")
    fig.tight_layout()
    save(fig, "fronts-and-stefan")


@figure("kramers-escape")
def fig_kramers():
    """Barrier crossing: Fokker-Planck in a double well, and Arrhenius' law."""
    fig, axs = plt.subplots(1, 2, figsize=(9.8, 4.2))
    x = np.linspace(-2.2, 2.2, 400)
    V = 0.5 * (x ** 2 - 1) ** 2
    D, dx = 0.05, x[1] - x[0]
    dV = np.gradient(V)
    dt = 0.2 * dx ** 2 / D
    a = tidy(axs[0])
    a.plot(x, V, color=MUTED, lw=1.6, label="potential $V(x)$")
    rho = np.exp(-(x + 1) ** 2 / 0.02)
    rho /= rho.sum() * dx
    for n, col in [(0, "#111827"), (150, BLUE), (600, TEAL), (2500, VIOLET)]:
        r = rho.copy()
        for _ in range(n):
            r[1:-1] -= dt * np.gradient(dV[1:-1] * r[1:-1] - D * np.gradient(r)[1:-1] / dx) / dx
            r[0] = r[-1] = 0.0
        a.plot(x, r * 3.2 + 0.02, color=col, label="density, %d steps" % n)
    a.set_ylim(0, 1.35)
    a.set_xlabel("$x$"); a.set_ylabel("$V$    (densities offset and scaled)")
    a.set_title("overdamped Fokker–Planck in a double well\n"
                "probability leaks over the barrier: the escape problem")
    a.legend(fontsize=8, loc="upper center")
    a = tidy(axs[1])
    b = np.linspace(1, 12, 300)
    for T, col in [(1.0, BLUE), (0.5, TEAL), (0.25, VIOLET)]:
        a.semilogy(b, np.exp(-b / T), color=col, label="$k_BT=%g$" % T)
    a.set_xlabel("barrier height $\\Delta V$"); a.set_ylabel("rate (arb. units)")
    a.set_title("Kramers / Arrhenius law:  $k\\sim e^{-\\Delta V/k_BT}$\n"
                "the same exponential governs reaction rates, nucleation,\n"
                "battery ageing and protein folding")
    a.legend(fontsize=8.5)
    fig.tight_layout()
    save(fig, "kramers-escape")
