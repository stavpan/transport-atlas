"""Part 1 — foundations: the balance law, the two descriptions, PDE taxonomy."""
import numpy as np
import matplotlib.pyplot as plt

from figlib import (figure, save, tidy, plain, arrow, box,
                          INK, MUTED, BLUE, TEAL, VIOLET, AMBER, ROSE, GREEN)


@figure("balance-control-volume")
def fig_balance():
    """The one sentence the whole atlas is an instance of."""
    fig, ax = plt.subplots(figsize=(8.6, 4.5))
    plain(ax, (0, 10), (0, 5.5))
    box(ax, (3.4, 1.5), 3.2, 2.3, "", fc="#eef4ff", ec=BLUE)
    ax.text(5.0, 2.65, "control volume\n$V$, surface $\\partial V$", ha="center",
            va="center", color=BLUE, fontsize=10)
    arrow(ax, (1.0, 3.5), (3.35, 3.5), BLUE, 2.2)
    ax.text(0.95, 3.75, "influx  $\\mathbf{J}\\cdot\\mathbf{n}<0$", fontsize=9.5, color=BLUE)
    arrow(ax, (6.65, 2.0), (9.05, 2.0), ROSE, 2.2)
    ax.text(7.05, 2.25, "efflux  $\\mathbf{J}\\cdot\\mathbf{n}>0$", fontsize=9.5, color=ROSE)
    arrow(ax, (5.0, 1.45), (5.0, 0.6), AMBER, 2.0)
    arrow(ax, (5.0, 0.6), (5.0, 1.45), GREEN, 2.0)
    ax.text(4.85, 1.0, "sinks", ha="right", fontsize=9.5, color=AMBER, va="center")
    ax.text(5.15, 1.0, "sources $f$", ha="left", fontsize=9.5, color=GREEN, va="center")
    ax.text(5.0, 5.0, r"$\frac{d}{dt}\int_V c\,\mathrm{d}V"
                      r"=-\oint_{\partial V}\mathbf{J}\cdot\mathbf{n}\,\mathrm{d}A"
                      r"+\int_V f\,\mathrm{d}V$", ha="center", fontsize=15)
    ax.text(5.0, 4.05, r"$\Longrightarrow\;\;\partial_t c+\nabla\cdot\mathbf{J}=f$"
                       r"   (every PDE in this atlas is an instance of this)",
            ha="center", fontsize=10.5, color=VIOLET)
    ax.text(5.0, 0.1, "things move, and nothing is lost",
            ha="center", fontsize=9.5, color=MUTED, style="italic")
    save(fig, "balance-control-volume")


@figure("lagrangian-eulerian")
def fig_lagrangian():
    """Follow the parcel vs watch the field."""
    fig, axs = plt.subplots(1, 2, figsize=(9.8, 4.1))
    X, Y = np.meshgrid(np.linspace(0, 4, 13), np.linspace(0, 3, 11))
    U = 1.0 + 0.35 * np.cos(Y) + 0.10 * X
    V = 0.35 * np.sin(X) - 0.15 * Y
    a = tidy(axs[0])
    a.streamplot(X, Y, U, V, color="#dfe3ea", density=1.0, linewidth=1.0,
                 arrowsize=0.7, zorder=1)
    t = np.linspace(0, 4.0, 400)
    for x0, y0 in [(0.3, 2.4), (0.5, 1.2), (1.1, 0.5)]:
        a.plot(x0 + 1.05 * t, y0 + 0.06 * np.sin(1.4 * t), color=BLUE, lw=1.8, zorder=4)
        a.plot([x0], [y0], "o", color=BLUE, ms=5, zorder=5)
    a.plot([2.1], [1.9], "o", color=ROSE, ms=6, zorder=6)
    a.add_patch(plt.Circle((2.1, 1.9), 0.24, fill=False, ec=ROSE, lw=2, zorder=6))
    a.annotate("a fluid parcel,\ncarrying its history", (2.1, 1.9), (2.2, 2.8),
               fontsize=9, color=ROSE, arrowprops=dict(arrowstyle="->", color=ROSE, lw=1.2))
    a.set_title("Lagrangian: follow the parcels\n$\\mathrm{D}c/\\mathrm{D}t$, pathlines")
    a.set_xlabel("$x$"); a.set_ylabel("$y$"); a.set_aspect("equal")
    b = tidy(axs[1])
    b.streamplot(X, Y, U, V, color="#dfe3ea", density=1.0, linewidth=1.0,
                 arrowsize=0.7, zorder=2)
    xx, yy = np.meshgrid(np.linspace(0.9, 2.6, 60), np.linspace(0.9, 2.3, 45))
    blob = np.exp(-((xx - 1.55) ** 2 + (yy - 1.55) ** 2) / 0.3)
    b.pcolormesh(xx, yy, blob, shading="auto", cmap="Blues", alpha=0.9, zorder=1)
    b.annotate("a fixed probe cell sees\nonly $\\partial c/\\partial t$", (1.55, 1.55),
               (2.3, 1.0), fontsize=9, color=VIOLET,
               arrowprops=dict(arrowstyle="->", color=VIOLET, lw=1.2))
    b.set_title("Eulerian: watch the field\n$\\partial c/\\partial t$, streamlines")
    b.set_xlabel("$x$"); b.set_ylabel("$y$"); b.set_aspect("equal")
    fig.suptitle(r"Two books of one story, linked by "
                 r"$\mathrm{D}/\mathrm{D}t=\partial_t+\mathbf{u}\cdot\nabla$",
                 fontsize=11.5, y=1.04)
    save(fig, "lagrangian-eulerian")


@figure("pde-taxonomy")
def fig_taxonomy():
    """Hyperbolic / parabolic / elliptic, side by side."""
    fig, axs = plt.subplots(1, 3, figsize=(10.6, 3.6))
    a = tidy(axs[0])
    for x0 in np.linspace(0, 1, 8):
        a.plot([x0, x0 + 0.6], [0, 1], color=BLUE, lw=1.2)
    for x0 in np.linspace(0.55, 1.0, 3):
        a.plot([x0, x0 + 1.15 * (1 - x0)], [0, 1], color=GREEN, lw=1.2, ls="--")
    a.plot([0.6, 1.0], [0, 1], color=ROSE, lw=2.4)
    a.text(0.04, 0.7, "rarefaction fan\n(characteristics spread)", color=GREEN, fontsize=8.6)
    a.text(0.6, 0.18, "shock: they collide", color=ROSE, fontsize=8.6, rotation=58)
    a.set_title("Hyperbolic\n$\\partial_t c+\\partial_x(uc)=0$", fontsize=10)
    a.set_ylabel("$t$")
    a = tidy(axs[1])
    x = np.linspace(-1.4, 1.4, 400)
    for tau, col in [(0.03, BLUE), (0.12, TEAL), (0.4, VIOLET)]:
        a.plot(x, np.exp(-x ** 2 / (4 * tau)) / np.sqrt(4 * np.pi * tau), color=col,
               label="$t=%.2f$" % tau)
    a.legend(loc="upper right")
    a.text(0.03, 0.66, "smooths, never sharpens;\nsignals spread\ninfinitely fast",
           transform=a.transAxes, color=MUTED, fontsize=8.6)
    a.set_title("Parabolic\n$\\partial_t c=D\\,\\partial_x^2 c$", fontsize=10)
    a = tidy(axs[2], grid=False)
    xx, yy = np.meshgrid(np.linspace(0, 1, 160), np.linspace(0, 1, 160))
    u = np.sin(np.pi * xx) * np.sinh(np.pi * yy) / np.sinh(np.pi)
    a.contourf(xx, yy, u, 12, cmap="Greens")
    a.contour(xx, yy, u, 12, colors="white", linewidths=0.4, alpha=0.7)
    a.set_title("Elliptic\n$-\\nabla\\cdot(k\\nabla T)=f$", fontsize=10)
    for a in axs:
        a.set_xlabel("$x$" + ("   ($t$ upward)" if a is not axs[2] else ""))
    axs[2].set_ylabel("$y$")
    fig.tight_layout()
    save(fig, "pde-taxonomy")
