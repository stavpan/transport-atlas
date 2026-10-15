"""Part 4 — numerical behaviour: scheme error portraits and stability regions."""
import numpy as np
import matplotlib.pyplot as plt

from figlib import (figure, save, tidy, INK, MUTED, BLUE, TEAL, VIOLET, AMBER,
                          ROSE, GREEN, SLATE)


@figure("numerical-error-portrait")
def fig_numerical():
    """The two unavoidable sins of discretising advection: smearing and ringing."""
    fig, axs = plt.subplots(1, 3, figsize=(11.2, 3.7))
    Nc, CFL = 64, 0.8
    x = (np.arange(Nc) + 0.5) / Nc
    c0 = np.exp(-((x - 0.25) ** 2) / 0.0025)
    nsteps = int(2.0 / (CFL / Nc))          # exactly two periodic crossings
    steps = {
        "upwind: 1st order": lambda u: (1 - CFL) * u + CFL * np.roll(u, 1),
        "Lax-Wendroff: 2nd order": lambda u: (u - CFL / 2 * (np.roll(u, -1) - np.roll(u, 1))
                                             + CFL ** 2 / 2 * (np.roll(u, -1) - 2 * u
                                                               + np.roll(u, 1))),
    }
    a = tidy(axs[0])
    a.plot(x, c0, color="#111827", lw=1.4, ls="--", label="exact (wrapped twice)")
    for (name, step), col in zip(steps.items(), [BLUE, GREEN]):
        u = c0.copy()
        for _ in range(nsteps):
            u = step(u)
        a.plot(x, u, color=col, label=name, alpha=0.9)
    a.legend(fontsize=8, loc="upper left")
    a.set_ylim(-0.25, 1.15); a.set_xlim(0.05, 0.6)
    a.set_title("after two periodic crossings\n$N=64$, CFL $=0.8$")
    a.set_xlabel("$x$"); a.set_ylabel("$c$")
    a.text(0.03, 0.06, "numerical diffusion vs numerical dispersion",
           transform=a.transAxes, fontsize=8.5, color=MUTED)
    a = tidy(axs[1])
    th = np.linspace(0, np.pi, 400)
    amp = {"upwind": np.abs(1 - CFL * (1 - np.exp(-1j * th))),
           "central": np.abs(1 - 1j * CFL * np.sin(th)),
           "Lax-Wendroff": np.abs(1 - CFL / 2 * (np.exp(1j * th) - np.exp(-1j * th))
                                  + CFL ** 2 / 2 * (np.exp(1j * th) - 2 + np.exp(-1j * th)))}
    a.axhline(1.0, color="#111827", ls="--", lw=1.2, label="exact (neutral)")
    for (name, g), col in zip(amp.items(), [BLUE, ROSE, GREEN]):
        a.plot(th / np.pi, g, color=col, label=name)
    a.legend(fontsize=8, loc="lower left")
    a.set_ylim(0.6, 1.4)
    a.set_xlabel("wavenumber $k\\Delta x/\\pi$"); a.set_ylabel("$|G|$")
    a.set_title("amplitude portrait\n$|G|>1$ for any $k$ $\\Rightarrow$ unconditional blow-up")
    a = tidy(axs[2])
    ph_ex = th
    ph_up = -np.unwrap(np.angle(1 - CFL * (1 - np.exp(-1j * th))))
    ph_lw = -np.unwrap(np.angle(1 - CFL / 2 * (np.exp(1j * th) - np.exp(-1j * th))
                                + CFL ** 2 / 2 * (np.exp(1j * th) - 2 + np.exp(-1j * th))))
    a.plot(th / np.pi, ph_ex, color="#111827", ls="--", lw=1.2, label="exact $\\omega=kU$")
    a.plot(th / np.pi, ph_up, color=BLUE, label="upwind")
    a.plot(th / np.pi, ph_lw, color=GREEN, label="Lax-Wendroff")
    a.legend(fontsize=8, loc="upper left")
    a.set_xlabel("$k\\Delta x/\\pi$"); a.set_ylabel("phase advance per step")
    a.set_title("phase portrait\nlag $=$ every wave travels at the wrong speed")
    fig.tight_layout()
    save(fig, "numerical-error-portrait")


@figure("stability-regions")
def fig_stability():
    """Where a time integrator is stable, and what that means for stiff transport."""
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 4.2))
    th = np.linspace(0, 2 * np.pi, 600)
    a = tidy(axs[0])
    a.add_patch(plt.Circle((-1, 0), 1, color=BLUE, alpha=0.12))
    a.plot(-1 + np.cos(th), np.sin(th), color=BLUE, lw=1.8, label="forward Euler (explicit)")
    a.plot([-50, 0], [0, 0], color=ROSE, lw=2.2, label="backward Euler: whole $\\mathbb{C}^-$")
    a.plot([-1, 0], [0, 0], color=SLATE, ls=":", lw=1.4)
    a.axhline(0, color="#9aa3b2", lw=0.8); a.axvline(0, color="#9aa3b2", lw=0.8)
    a.set_xlim(-3.4, 1.4); a.set_ylim(-2.0, 2.0)
    a.set_xlabel("Re $z=\\lambda\\Delta t$"); a.set_ylabel("Im $z$")
    a.set_title("stability regions\nstiff $\\lambda$ pushes $z$ far left: explicit dies")
    a.legend(fontsize=8, loc="lower left")
    a = tidy(axs[1])
    cfl = np.linspace(0.01, 1.2, 400)
    a.plot(cfl, np.abs(1 - cfl * (1 - np.exp(-1j * np.pi))), color=BLUE, label="upwind, $k\\Delta x=\\pi$")
    a.plot(cfl, np.abs(1 - 1j * cfl * np.sin(np.pi)), color=ROSE, label="central, $k\\Delta x=\\pi$")
    a.axhline(1.0, color="#111827", ls="--", lw=1.2, label="marginal")
    a.axvline(1.0, color=MUTED, ls=":", lw=1)
    a.text(1.01, 0.62, "CFL $=1$", fontsize=8.5, color=MUTED)
    a.set_xlabel("CFL number $U\\Delta t/\\Delta x$"); a.set_ylabel("$|G|$")
    a.set_title("the Courant condition is a *stability* statement\n"
                "not a resolution statement: accuracy is a separate battle")
    a.legend(fontsize=8, loc="lower right")
    fig.tight_layout()
    save(fig, "stability-regions")
