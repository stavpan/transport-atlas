"""Part 6 — shear dispersion and diffusion-driven pattern formation."""
import numpy as np
import matplotlib.pyplot as plt

from figlib import (figure, save, tidy, INK, MUTED, BLUE, TEAL, VIOLET, AMBER,
                          ROSE, GREEN, SKY)


@figure("taylor-aris")
def fig_taylor_aris():
    """Shear dispersion: how a velocity gradient becomes extra diffusion."""
    fig, axs = plt.subplots(1, 2, figsize=(9.8, 4.2))
    a = tidy(axs[0])
    y = np.linspace(-1, 1, 200)
    u = 1.5 * (1 - y ** 2)
    a.plot(u, y, color=BLUE, lw=2.4, label="Poiseuille profile $u(y)$")
    a.fill_betweenx(y, 0, u, color=BLUE, alpha=0.10)
    for y0, col in [(-0.7, ROSE), (0.7, GREEN)]:
        a.annotate("", (1.5 * (1 - y0 ** 2), y0), (0.3, y0 * 0.2),
                   arrowprops=dict(arrowstyle="->", color=col, lw=1.3))
    a.text(0.85, 0.62, "cross-stream diffusion", color=GREEN, fontsize=8.5)
    a.text(0.85, -0.88, "cross-stream diffusion", color=ROSE, fontsize=8.5)
    a.set_xlabel("$u$"); a.set_ylabel("$y$ (half-width $a$)")
    a.set_title("the mechanism (G. I. Taylor, 1953)\n"
                "fast centre, slow walls, coupled by molecular diffusion")
    a = tidy(axs[1])
    tt = np.logspace(-2, 4, 600)
    target = 1.0 + 1.0 / 48.0            # D + a^2U^2/(48D), dimensionless
    a.semilogx(tt, 1 + (target - 1) * (1 - np.exp(-tt / 0.35)), color=VIOLET, lw=2.4,
               label="$D_{\\mathrm{eff}}(t)$")
    a.axhline(1.0, color=BLUE, ls="--", lw=1.5, label="bare molecular $D$")
    a.axhline(target, color=ROSE, ls="--", lw=1.5, label="$D+a^2U^2/(48D)$")
    a.set_xlabel("time (units of $a^2/D$)")
    a.set_ylabel("effective $D_{\\mathrm{eff}}/D$")
    a.set_title("what a tracer test actually measures\n"
                "early: molecular; late: Fickian again, with a far larger $D$")
    a.legend(fontsize=8.5, loc="center right")
    fig.tight_layout()
    save(fig, "taylor-aris")


@figure("turing-patterns")
def fig_turing():
    """Diffusion-driven instability: the counter-intuitive heart of morphogenesis."""
    fig, axs = plt.subplots(1, 2, figsize=(9.8, 4.2))
    a = tidy(axs[0])
    k = np.linspace(0.01, 3.0, 400)
    f_u, f_v, g_u, g_v = 1.0, -2.0, 2.0, -3.0
    for Dv, col in [(1.0, BLUE), (5.0, TEAL), (20.0, VIOLET)]:
        Du = 1.0
        tr = f_u + g_v - (Du + Dv) * k ** 2
        detr = (f_u - Du * k ** 2) * (g_v - Dv * k ** 2) - f_v * g_u
        sigma = 0.5 * (tr + np.sqrt(np.maximum(tr ** 2 - 4 * detr, 0)))
        a.plot(k, sigma, color=col, label="$D_v/D_u=%g$" % Dv)
    a.axhline(0, color="#111827", ls="--", lw=1.2)
    a.set_ylim(-1.6, 0.35)
    a.set_xlabel("wavenumber $k$"); a.set_ylabel("growth rate $\\sigma(k)$")
    a.set_title("dispersion relation of a Turing instability\n"
                "diffusion *destabilises*: only a band of $k$ grows")
    a.legend(fontsize=8.5, loc="lower left")
    n, steps = 128, 3000
    Du2, Dv2, F, K = 0.16, 0.08, 0.035, 0.065
    u = np.ones((n, n)); v = np.zeros((n, n))
    rng = np.random.default_rng(3)
    u[50:78, 50:78] = 0.5
    v[50:78, 50:78] = 0.25
    v += 0.02 * rng.random((n, n))

    def lap(z):
        return (np.roll(z, 1, 0) + np.roll(z, -1, 0) + np.roll(z, 1, 1)
                + np.roll(z, -1, 1) - 4 * z)

    for _ in range(steps):
        uvv = u * v * v
        u = u + Du2 * lap(u) - uvv + F * (1 - u)
        v = v + Dv2 * lap(v) + uvv - (F + K) * v
    b = axs[1]
    b.imshow(v, cmap="magma", interpolation="bilinear")
    b.set_xticks([]); b.set_yticks([]); b.grid(False)
    b.set_title("Gray–Scott simulation on 128$^2$\n"
                "the same nonlinearity that writes zebra stripes")
    b.set_xlabel("self-organised spots: no template, no boundary data")
    fig.tight_layout()
    save(fig, "turing-patterns")
