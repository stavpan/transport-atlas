"""Part 8 — radiative transfer, and the deepest bridge: diffusion as gradient flow."""
import numpy as np
import matplotlib.pyplot as plt

from figlib import (figure, save, tidy, INK, MUTED, BLUE, TEAL, VIOLET, AMBER,
                          ROSE, GREEN, SKY)


@figure("radiative-transfer")
def fig_radiative():
    """Extinction, angular structure, and the two asymptotic limits."""
    fig, axs = plt.subplots(1, 3, figsize=(11.4, 3.6))
    a = tidy(axs[0])
    tau = np.linspace(0, 5, 400)
    for al, col in [(0.0, BLUE), (0.5, TEAL), (0.9, VIOLET)]:
        a.plot(tau, np.exp(-(1 - al) * tau), color=col, label="$\\omega_0=%g$" % al)
    a.set_xlabel("optical depth $\\tau=\\int\\kappa\\,\\mathrm{d}s$")
    a.set_ylabel("$I/I_0$")
    a.set_title("extinction\nBeer–Lambert $I=I_0e^{-\\tau}$;\n"
                "scattering ($\\omega_0>0$) keeps energy in the beam")
    a.legend(fontsize=8.5)
    a = tidy(axs[1])
    mu = np.linspace(-1, 1, 400)
    for tau0, col in [(0.5, BLUE), (2.0, TEAL), (10.0, VIOLET)]:
        I = 1.0 / (1 + 0.5 * tau0 * (1 + mu)) + 0.4 * np.exp(-tau0 * (1 + mu))
        a.semilogy(mu, np.maximum(I, 1e-3), color=col, label="$\\tau_0=%g$" % tau0)
    a.set_xlabel("$\\mu=\\cos\\theta$"); a.set_ylabel("intensity (Planck units)")
    a.set_title("angular structure\nforward peak sharpens with $\\tau$;\n"
                "isotropy only deep inside an optically thick medium")
    a.legend(fontsize=8.5)
    a = tidy(axs[2])
    tt = np.logspace(-1, 2.5, 300)
    a.loglog(tt, 1.0 / tt ** 2, color=ROSE, ls="--", label="thick: diffusion $\\sim1/\\tau^2$")
    a.loglog(tt, np.exp(-tt), color=BLUE, label="thin: ballistic $e^{-\\tau}$")
    a.loglog(tt, 1.0 / (1 + 0.8 * tt) ** 2, color="#111827", lw=1.5, label="interpolated flux")
    a.set_xlabel("optical thickness $\\tau_0$"); a.set_ylabel("flux (arb. units)")
    a.set_title("two limits, one equation\nthin: rays stream; thick: radiation diffuses;\n"
                "the crossover is where numerics hurt")
    a.legend(fontsize=8.5)
    fig.tight_layout()
    save(fig, "radiative-transfer")


@figure("optimal-transport-vs-diffusion")
def fig_ot_diffusion():
    """Two ways to move a density: transport (along the optimal map) vs diffusion."""
    rng = np.random.default_rng(5)
    n = 6000
    x0 = np.concatenate([rng.normal(-2.6, 0.35, n // 2), rng.normal(2.6, 0.35, n // 2)])
    x1 = rng.normal(0.0, 1.25, n)
    s0, s1 = np.sort(x0), np.sort(x1)
    grid = np.linspace(-6, 6, 400)
    fig, axs = plt.subplots(1, 2, figsize=(10.4, 4.2))
    a = tidy(axs[0])
    for frac, col, lab in [(0.0, "#111827", "$t=0$"), (0.5, VIOLET, "$t=0.5$"),
                           (1.0, TEAL, "$t=1$")]:
        xs = (1 - frac) * s0 + frac * s1                    # exact W2 geodesic in 1-D
        a.hist(xs, bins=grid, density=True, histtype="step", lw=2.0, color=col, label=lab)
    a.set_title("transport: the Brenier map $T_t=(1-t)x_0+t\\,x_1$\n"
                "moves each parcel; mass never crosses itself")
    a.set_xlabel("$x$"); a.set_ylabel("density")
    a.legend(fontsize=8.5)
    a = tidy(axs[1])
    h = grid[1] - grid[0]
    rho = np.histogram(x0, bins=grid, density=True)[0]
    ent = []
    ts = np.linspace(0, 1, 25)
    for t in ts:
        sig = np.sqrt(2 * 0.35 ** 2 + 4 * t * 0.6)
        p = np.convolve(rho, np.exp(-grid ** 2 / (2 * sig ** 2)), mode="same")
        p = np.maximum(p, 1e-12)
        ent.append(-np.sum(p * np.log(p)) * h)
    a.plot(ts, np.array(ent) - ent[-1], color=BLUE, lw=2.4, label="heat flow: exponential decay")
    entg = []
    for t in ts:
        xs = (1 - t) * s0 + t * s1
        p = np.histogram(xs, bins=grid, density=True)[0]
        p = np.maximum(p, 1e-12)
        entg.append(-np.sum(p * np.log(p)) * h)
    a.plot(ts, np.array(entg) - entg[-1], color=VIOLET, lw=2.4,
           label="W$_2$ geodesic: convex in $t$")
    a.set_xlabel("interpolation parameter $t$")
    a.set_ylabel("entropy (offset)")
    a.set_title("displacement convexity\n"
                "diffusion is *steepest descent of entropy in the Wasserstein metric*\n"
                "(Jordan–Kinderlehrer–Otto, 1998)")
    a.legend(fontsize=8.5, loc="lower left")
    fig.tight_layout()
    save(fig, "optimal-transport-vs-diffusion")
