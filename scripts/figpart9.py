"""Part 9 — the Fourier view and the engineering analogy of transport."""
import numpy as np
import matplotlib.pyplot as plt

from figlib import (figure, save, tidy, plain, arrow, box, INK, MUTED, BLUE, TEAL,
                    VIOLET, AMBER, ROSE, GREEN, SKY)


@figure("spectral-view")
def fig_spectral():
    """Every transport operator is a multiplication in Fourier space."""
    fig, axs = plt.subplots(1, 3, figsize=(11.4, 3.7))
    k = np.linspace(0, 3, 400)
    a = tidy(axs[0])
    a.plot(k, k, color=BLUE, label="advection $\\omega=kU$")
    a.plot(k, 2.0 * k, color=TEAL, ls="--", label="waves $\\omega=ck$")
    a.plot(k, np.zeros_like(k), color=ROSE, label="diffusion $\\omega=0$")
    a.set_xlabel("wavenumber $k$"); a.set_ylabel("Re $\\omega$ (oscillation)")
    a.set_title("frequency: what oscillates\n"
                "advection and waves carry a signal; diffusion does not")
    a.legend(fontsize=8.5)
    a = tidy(axs[1])
    a.plot(k, k ** 2, color=ROSE, lw=2.4, label="diffusion: $-Dk^2$")
    a.plot(k, 0.35 * k ** 4, color=VIOLET, ls="--", label="4th order (Cahn–Hilliard)")
    a.plot(k, np.zeros_like(k), color=BLUE, lw=2.4, label="advection: no damping")
    a.set_xlabel("wavenumber $k$"); a.set_ylabel("$-\\mathrm{Im}\\,\\omega$ (decay rate)")
    a.set_title("damping: what dies\nhigh $k$ dies first "
                "$\\Rightarrow$ diffusion is a low-pass filter")
    a.legend(fontsize=8.5)
    a = tidy(axs[2])
    a.plot(k, np.exp(-0.5 * k ** 2), color=ROSE, lw=2.4, label="exact diffusion")
    a.plot(k, np.ones_like(k), color=BLUE, lw=2.4, label="exact advection $|G|=1$")
    a.plot(k, np.abs(1 - 0.8 * (1 - np.exp(-1j * k))), color=GREEN, ls="--",
           label="upwind discretisation")
    a.set_xlabel("wavenumber $k\\Delta x$"); a.set_ylabel("amplitude factor")
    a.set_title("the same picture, discretised\na scheme *is* a modified\n"
                "dispersion relation: grids filter too")
    a.legend(fontsize=8.5)
    fig.tight_layout()
    save(fig, "spectral-view")


@figure("transport-analogy")
def fig_analogy():
    """Heat, mass and momentum transport: one idea in three costumes."""
    fig, axs = plt.subplots(1, 2, figsize=(10.4, 4.2))
    a = plain(axs[0], (0, 10), (0, 6))
    rows = [("heat", "$q=-k\\nabla T$", "$T$", "$\\mathrm{Nu}$", ROSE, "Fourier"),
            ("mass", "$J=-D\\nabla c$", "$c$", "$\\mathrm{Sh}$", BLUE, "Fick"),
            ("momentum", "$\\tau=\\mu\\nabla u$", "$u$", "$C_f$", GREEN, "Newton")]
    for i, (name, law, pot, dimless, col, who) in enumerate(rows):
        y = 4.5 - 1.6 * i
        box(a, (0.3, y), 1.5, 1.05, name, fc="white", ec=col, tc=col, fs=10)
        a.text(2.1, y + 0.52, law, fontsize=11, va="center")
        a.text(4.7, y + 0.52, "potential: " + pot, fontsize=9, va="center", color=MUTED)
        a.text(7.0, y + 0.52, "flux ratio: " + dimless, fontsize=9, va="center", color=MUTED)
        a.text(2.1, y - 0.02, who, fontsize=7.5, va="center", color=col)
    a.text(5.0, 0.55, "flux $=-$(transport property) $\\times$ $\\nabla$(potential)",
           ha="center", fontsize=11, color=INK)
    a.set_title("the analogy that built chemical engineering\n"
                "Reynolds · Prandtl · Chilton–Colburn · Bird–Stewart–Lightfoot")
    a = plain(axs[1], (0, 10), (0, 6))
    box(a, (0.4, 3.5), 2.7, 1.2, "thermal\n$\\Delta T$,  $R=L/(kA)$", fc="#fff1f2", ec=ROSE, fs=9)
    box(a, (3.65, 3.5), 2.7, 1.2, "electrical\n$\\Delta V$,  $R=L/(\\sigma A)$",
        fc="#eff6ff", ec=BLUE, fs=9)
    box(a, (6.9, 3.5), 2.7, 1.2, "hydraulic\n$\\Delta p$,  $R=8\\mu L/(\\pi r^4)$",
        fc="#f0fdf4", ec=GREEN, fs=9)
    for x0 in (3.1, 6.35):
        arrow(a, (x0, 4.1), (x0 + 0.55, 4.1), INK, 1.6)
    box(a, (2.6, 1.0), 4.8, 1.6,
        "series: $R_{\\rm tot}=\\sum_i R_i$\n"
        "parallel: $1/R_{\\rm tot}=\\sum_i 1/R_i$\n"
        "flux $=\\Delta$(potential)$/R_{\\rm tot}$", fc="#f8fafc", ec=MUTED, fs=9.5)
    arrow(a, (5.0, 3.4), (5.0, 2.75), MUTED, 1.6)
    a.set_title("circuit thinking\nevery *linear* steady transport problem is a\n"
                "resistor network — which is why finite-volume\n"
                "codes and bond graphs look the same")
    save(fig, "transport-analogy")

@figure("subsidence-poroelasticity")
def fig_subsidence():
    """Pumping a reservoir: drawdown diffuses, the ground sinks irreversibly."""
    fig, axs = plt.subplots(1, 2, figsize=(9.8, 4.2))
    a = tidy(axs[0])
    r = np.logspace(-1, 3.2, 400)
    for tt, col in [(0.05, "#111827"), (0.5, BLUE), (5.0, TEAL), (50.0, VIOLET)]:
        u = r ** 2 / (4 * tt)
        e1 = -0.5772 - np.log(u) + u - u ** 2 / 4 + u ** 3 / 18
        e1 = np.where(u < 1e-3, -np.log(u) - 0.5772, e1)
        a.semilogx(r, np.maximum(e1, 0), color=col, label="$t=%g$" % tt)
    a.set_xlabel("distance from the well, $r$")
    a.set_ylabel("drawdown $s$  (Theis well function)")
    a.set_title("pressure diffuses outward\nthe aquifer equation "
                "$\\partial_t s=(T/S)\\nabla^2 s$\nis literally the heat equation")
    a.legend(fontsize=8.5, loc="upper right")
    a = tidy(axs[1], grid=False)
    x = np.linspace(-6, 6, 400)
    bowl = -0.55 * np.exp(-x ** 2 / 9)
    a.fill_between(x, -1.35, -1.0, color="#dbeafe")
    a.text(-5.7, -1.28, "depleting reservoir layer", fontsize=8.5, color="#1e40af")
    a.plot(x, np.zeros_like(x), color=MUTED, lw=1.4, label="original ground surface")
    a.plot(x, bowl, color=ROSE, lw=2.4, label="after depletion: compaction bowl")
    for x0 in (-3.5, 0.0, 3.5):
        arrow(a, (x0, -0.98), (x0, -0.55 * np.exp(-x0 ** 2 / 9) - 0.03), SKY, 1.2)
    a.set_ylim(-1.45, 0.35)
    a.set_xticks([])
    a.set_ylabel("elevation")
    a.set_title("effective stress does the rest\n"
                "$\\sigma'=\\sigma-p$: lower pressure loads the matrix,\n"
                "which compacts — and mostly stays compacted")
    a.legend(fontsize=8.5, loc="lower left")
    fig.tight_layout()
    save(fig, "subsidence-poroelasticity")
