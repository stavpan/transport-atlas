"""Part 2 — dimensionless numbers: timescales, regime maps, Knudsen ladder."""
import numpy as np
import matplotlib.pyplot as plt

from figlib import (figure, save, tidy, plain, arrow,
                          INK, MUTED, BLUE, TEAL, VIOLET, AMBER, ROSE, GREEN, SKY)


@figure("battle-of-timescales")
def fig_timescales():
    """A dimensionless number is a ratio of these bars."""
    fig, ax = plt.subplots(figsize=(8.8, 4.0))
    L, U, D, k, alpha = 1.0, 1.0, 1e-9, 1e-3, 1e-7
    items = [
        ("advection  $t_a=L/U$", L / U, BLUE),
        ("reaction  $t_r=1/k$", 1 / k, AMBER),
        ("diffusion  $t_d=L^2/D$   (solute, water, 1 m)", L ** 2 / D, VIOLET),
        ("conduction  $t_c=L^2/\\alpha$   (heat, steel, 1 m)", L ** 2 / alpha, ROSE),
        ("radiation  $t_\\gamma=L/c$", L / 3e8, TEAL),
    ]
    y = np.arange(len(items))
    ax.barh(y, [np.log10(v) for _, v, _ in items],
            color=[c for *_, c in items], alpha=.85, height=.55)
    ax.set_yticks(y)
    ax.set_yticklabels([n for n, _, _ in items])
    ax.set_xlabel("time to cross 1 m  —  $\\log_{10}(t\\,/\\,1\\,$s$)$")
    for yi, (_, v, _) in zip(y, items):
        s = "%.2g s" % v if v >= 1 else "%.1e s" % v
        ax.text(np.log10(v) + 0.15, yi, s, va="center", fontsize=9, color=INK)
    ax.set_xlim(-9.4, 10.8)
    for t, lab in ((3600, "1 hour"), (3.15e7, "1 year"), (3.15e9, "1 century")):
        ax.axvline(np.log10(t), color=MUTED, ls=":", lw=1)
        ax.text(np.log10(t) + .1, -0.6, lab, color=MUTED, fontsize=8, rotation=90)
    ax.set_title("Dimensionless numbers are ratios of these bars\n"
                 "molecular transport is hopeless over metres and effortless over microns")
    tidy(ax)
    save(fig, "battle-of-timescales")


@figure("regime-map-pe-da")
def fig_regime_map():
    """Where a problem lives decides how you must solve it."""
    fig, ax = plt.subplots(figsize=(7.8, 5.6))
    pe = np.logspace(-2, 6, 220)
    da = np.logspace(-3, 5, 220)
    PE, DA = np.meshgrid(pe, da)
    mesh = ax.pcolormesh(PE, DA, np.log10(DA) - np.log10(PE), shading="auto",
                         cmap="coolwarm", alpha=0.2)
    mesh.set_rasterized(True)          # keeps the SVG small (33 MB otherwise)
    ax.contour(PE, DA, DA - 1, levels=[0], colors=[AMBER], linewidths=1.6)
    ax.contour(PE, DA, PE - 1, levels=[0], colors=[BLUE], linewidths=1.6)
    ax.contour(PE, DA, DA * PE - 1, levels=[0], colors=[ROSE], linewidths=1.2, ls="--")
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.text(2e-2, 2e-3, "diffusion wins\n($\\mathrm{Pe}<1$)", color=BLUE, fontsize=9.5)
    ax.text(2e3, 3e-3, "advection wins\n($\\mathrm{Pe}>1,\\ \\mathrm{Da}<1$)",
            color=BLUE, fontsize=9.5)
    ax.text(1e-1, 5e2, "reaction wins\n($\\mathrm{Da}>1$)", color=AMBER, fontsize=9.5)
    ax.text(1.5e-3, 4e-1, "transient plume", color=MUTED, fontsize=8.5, rotation=-30)
    for x, y, lab in [(2e4, 1e-2, "river tracer"), (1e-1, 1e-1, "pore-scale solute"),
                      (3e-2, 3e3, "flame"), (5e1, 5e-1, "capillary uptake"),
                      (8e-1, 8e-1, "boundary-layer reaction"),
                      (2e2, 2e2, "catalytic reactor")]:
        ax.plot([x], [y], "k.", ms=7)
        ax.annotate(lab, (x, y), textcoords="offset points", xytext=(7, -3),
                    fontsize=8.5, color=INK)
    ax.set_xlabel("$\\mathrm{Pe}=UL/D$    advection / diffusion")
    ax.set_ylabel("$\\mathrm{Da}=kL^2/D=t_d/t_r$    transport / reaction")
    ax.set_title("A regime map is a map of numerical strategies\n"
                 "it tells you which term you may neglect — and which one will bite")
    save(fig, "regime-map-pe-da")


@figure("knudsen-regimes")
def fig_knudsen():
    """Kn = mean free path / device size, and what valid equation each regime has."""
    fig, axs = plt.subplots(1, 4, figsize=(11.2, 3.2))
    rng = np.random.default_rng(7)
    regimes = [("continuum\n$\\mathrm{Kn}<0.01$", 0.06, 16, BLUE,
                "Euler / Navier-Stokes,\nno-slip, Fick, Fourier"),
               ("slip / rarefied\n$0.01-0.1$", 0.16, 9, TEAL,
                "NS + slip & temperature\njump boundary conditions"),
               ("transition\n$0.1-10$", 0.55, 4, AMBER,
                "no hydrodynamic closure;\nDSMC, moment methods"),
               ("free molecular\n$\\mathrm{Kn}>10$", 1.6, 2, ROSE,
                "ballistic molecules,\nPoisson noise")]
    for ax, (title, mfp, nstep, col, eq) in zip(axs, regimes):
        plain(ax, (0, 1), (0, 1))
        ax.add_patch(plt.Rectangle((0.02, 0.02), 0.96, 0.96, fill=False, ec="#9aa3b2", lw=1.2))
        for _ in range(7):
            p = rng.random(2) * 0.9 + 0.05
            pts = [p.copy()]
            for _ in range(nstep):
                ang = rng.random() * 2 * np.pi
                p = p + mfp * 0.55 * np.array([np.cos(ang), np.sin(ang)])
                p = np.clip(p, 0.03, 0.97)
                pts.append(p.copy())
            pts = np.array(pts)
            ax.plot(pts[:, 0], pts[:, 1], color=col, lw=1.0, alpha=0.75)
        ax.set_title(title, fontsize=9.5, color=col)
        ax.text(0.5, -0.14, eq, ha="center", va="top", fontsize=8, color=INK,
                transform=ax.transAxes)
    fig.suptitle("Knudsen number $\\mathrm{Kn}=\\lambda/L$: how many collisions a molecule "
                 "has before it crosses the device", fontsize=11, y=1.06)
    save(fig, "knudsen-regimes")
