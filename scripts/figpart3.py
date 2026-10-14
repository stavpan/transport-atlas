"""Part 3 — advection-diffusion-reaction and conservation laws."""
import numpy as np
import matplotlib.pyplot as plt

from figlib import (figure, save, tidy, arrow,
                          INK, MUTED, BLUE, TEAL, VIOLET, AMBER, ROSE, GREEN)


@figure("advection-vs-diffusion")
def fig_adv_diff():
    """Same equation, three personalities: shift, spread, shift-and-spread."""
    fig, axs = plt.subplots(2, 2, figsize=(10.2, 6.4))
    x = np.linspace(-3, 8, 800)
    U, D = 1.0, 0.06
    a = tidy(axs[0, 0])
    for t, c in [(0, "#111827"), (1.0, BLUE), (2.0, TEAL), (3.0, VIOLET)]:
        g = np.exp(-((x - U * t) ** 2) / 0.08)
        a.plot(x, g, color=c, alpha=0.9, label="t=%g" % t)
    a.legend(loc="upper left", ncol=2)
    a.set_title("pure advection: $\\partial_t c+U\\partial_x c=0$\nthe shape is frozen; only the axis moves")
    a.text(0.05, 0.06, "vertical derivative never smooths", transform=a.transAxes,
           fontsize=8.5, color=MUTED)
    a = tidy(axs[0, 1])
    for t, c in [(0.05, "#111827"), (0.5, BLUE), (1.5, TEAL), (3.0, VIOLET)]:
        g = np.exp(-x ** 2 / (4 * D * t)) / np.sqrt(4 * np.pi * D * t)
        a.plot(x, g, color=c, alpha=0.9, label="t=%g" % t)
    a.legend(loc="upper right")
    a.set_title("pure diffusion: $\\partial_t c=D\\partial_x^2 c$\n"
                "area is conserved, peak decays as $t^{-1/2}$, width grows as $t^{1/2}$")
    a.text(0.05, 0.55, "residence time across $L$: $L^2/D$", transform=a.transAxes,
           fontsize=8.5, color=MUTED)
    a = tidy(axs[1, 0])
    for t, c in [(0.25, "#111827"), (1.0, BLUE), (2.0, TEAL)]:
        g = np.exp(-((x - U * t) ** 2) / (4 * D * t)) / np.sqrt(4 * np.pi * D * t)
        a.plot(x, g, color=c, alpha=0.9, label="t=%g" % t)
    a.legend(loc="upper left")
    a.set_title("advection + diffusion ($\\mathrm{Pe}=UL/D\\approx 17$)\n"
                "the two terms commute here — but not once $D$ or $U$ vary")
    x2 = np.linspace(-0.5, 4, 600)
    del x2
    a2 = tidy(axs[1, 1])
    tt = np.linspace(0.05, 3, 400)
    for Pe, c in [(100, VIOLET), (20, TEAL), (5, AMBER), (1, ROSE)]:
        d = 1.0 / Pe
        arg = (1.0 - tt) / np.sqrt(4 * d * tt)
        a2.plot(tt, 0.5 * np.array([erfc_approx(v) for v in arg]), color=c,
                label="$\\mathrm{Pe}=%g$" % Pe)
    a2.set_xlabel("time after injection"); a2.set_ylabel("$c/c_0$ at $x=L$")
    a2.set_title("breakthrough curve at the outlet\n"
                 "low Pe: smeared and early; high Pe: sharp and plug-like")
    a2.legend(loc="lower right")
    a2.axvline(1.0, color=MUTED, ls=":", lw=1)
    a2.text(1.02, 0.05, "ideal plug arrival $t=L/U$", fontsize=8, color=MUTED, rotation=90)
    fig.tight_layout()
    save(fig, "advection-vs-diffusion")


def erfc_approx(z):
    """erfc without scipy (Abramowitz & Stegun 7.1.26-ish, ~1e-7 accurate)."""
    t = 1.0 / (1.0 + 0.3275911 * abs(z))
    poly = t * (0.254829592 + t * (-0.284496736 + t * (1.421413741 +
                t * (-1.453152027 + t * 1.061405429))))
    e = poly * np.exp(-z * z)
    return e if z >= 0 else 2.0 - e


@figure("conservation-law-shocks")
def fig_shock():
    """Scalar conservation laws: flux functions, characteristics, entropy solutions."""
    fig, axs = plt.subplots(1, 3, figsize=(11.0, 3.7))
    c = np.linspace(0, 1, 300)
    f = c * (1 - c)
    a = tidy(axs[0])
    a.plot(c, f, color=BLUE)
    for c0, col, lab in [(0.2, ROSE, "shock (fast $\\to$ slow)"), (0.8, GREEN, "rarefaction")]:
        a.plot([c0, 0.5], [f[np.argmin(abs(c - c0))], f[np.argmin(abs(c - 0.5))]],
               color=col, ls="--", lw=1.6, label=lab)
    a.set_xlabel("$c$ (density of cars)"); a.set_ylabel("$f(c)=c(1-c)$")
    a.set_title("flux function\nchord slope $=f'(c)=$ shock speed")
    a.legend(loc="upper center", fontsize=8)
    a = tidy(axs[1])
    for x0 in np.linspace(0, 1, 9):
        a.plot([x0, x0 + 0.55], [0, 1], color=BLUE, lw=1.1)
    for x0 in np.linspace(0.6, 1.05, 4):
        a.plot([x0, x0 + 0.9 * (1 - x0)], [0, 1], color=GREEN, lw=1.1, ls="--")
    a.plot([0.62, 1.0], [0, 1], color=ROSE, lw=2.4)
    a.set_xlabel("$x$"); a.set_ylabel("$t$")
    a.set_title("characteristics\nvelocity $f'(c)$ depends on the data")
    a = tidy(axs[2])
    x = np.linspace(-1, 2, 600)
    step = 0.5 * (1 - np.tanh(40 * x))
    a.plot(x, step, color="#111827", label="$t=0$")
    sh = 0.5 * (1 - np.tanh(60 * (x - 0.25 * 1.5)))
    a.plot(x, sh, color=ROSE, label="shock solution", ls="--")
    a.plot(x, 0.5 * (1 - np.tanh(8 * (x - 0.0))) * 0.0 + np.clip((x + 0.5) / 1.5, 0, 1),
           color=GREEN, label="rarefaction solution")
    a.set_xlabel("$x$"); a.set_ylabel("$c$")
    a.set_title("weak solutions\nentropy condition picks the physical one")
    a.legend(fontsize=8, loc="center right")
    fig.tight_layout()
    save(fig, "conservation-law-shocks")
