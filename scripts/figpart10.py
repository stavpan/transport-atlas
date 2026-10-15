"""Part 10 — the recurring machinery: equilibria, stability, bifurcation, chaos,
criticality, scaling, noise, and the intersections.  Also the generative 'panta rhei'
artwork used on the site's front page.
"""
import numpy as np
import matplotlib.pyplot as plt

from figlib import (figure, save, tidy, plain, arrow, box,
                    INK, MUTED, BLUE, TEAL, VIOLET, AMBER, ROSE, SLATE, GREEN, SKY)


@figure("energy-landscape-stability")
def fig_energy_landscape():
    """Stationary points, stability, and the landscape shortcut."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 4.2),
                               gridspec_kw={"width_ratios": [1.25, 1]})
    x = np.linspace(-2.55, 2.55, 800)
    V = 0.25 * x ** 4 - 0.9 * x ** 2 + 0.32 * x
    tidy(a); a.plot(x, V, color=INK, lw=2.2)
    for r in np.roots([1.0, 0.0, -1.8, 0.32]):
        if abs(r.imag) < 1e-9:
            rr = r.real
            a.plot([rr], [0.25 * rr ** 4 - 0.9 * rr ** 2 + 0.32 * rr], "o",
                   color=BLUE if rr > 0 else ROSE, ms=8, zorder=5)
    a.annotate("stable minimum\n$V''>0$: perturbations return", (1.29, -0.6),
               xytext=(0.04, 0.20), textcoords="axes fraction",
               fontsize=9, color=BLUE, arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.2))
    a.annotate("unstable maximum\n$V''<0$: perturbations grow", (0.13, -0.08),
               xytext=(0.60, 0.97), textcoords="axes fraction",
               fontsize=9, color=ROSE, arrowprops=dict(arrowstyle="->", color=ROSE, lw=1.2))
    a.set_ylim(-0.85, 1.45)
    a.set_title("Energy landscape: $\\dot{x}=-V'(x)$")
    a.set_xlabel("state $x$"); a.set_ylabel("$V(x)$")

    # phase line underneath: arrows show the flow
    xl = np.linspace(-2.5, 2.5, 500)
    f = -(xl ** 3 - 1.8 * xl + 0.32)
    tidy(b, grid=False)
    b.plot(xl, f, color=VIOLET, lw=2.0)
    b.axhline(0, color="#9aa3b2", lw=1)
    for x0 in np.linspace(-2.4, 2.4, 17):
        v = -(x0 ** 3 - 1.8 * x0 + 0.32)
        b.annotate("", xy=(x0 + 0.16 * np.sign(v), 0), xytext=(x0, 0),
                   arrowprops=dict(arrowstyle="-|>", color=BLUE if v > 0 else ROSE,
                                   lw=1.6, mutation_scale=11))
    b.set_title("The same information, one dimension down")
    b.set_xlabel("state $x$"); b.set_ylabel("$\\dot{x}$"); b.set_yticks([])
    b.text(0, 0.62, "arrows = where the flow goes;\nzero crossings = stationary points",
           fontsize=8.6, color=MUTED, ha="center", style="italic")
    save(fig, "energy-landscape-stability")


@figure("linear-stability-zoo")
def fig_linear_zoo():
    """The four linear phase portraits — all of stability theory in one panel."""
    A_map = [("stable node\n$\\lambda_1,\\lambda_2<0$", [[-1, 0], [0, -0.45]], BLUE),
             ("stable spiral\n$\\mathrm{Im}\\,\\lambda\\neq0$", [[-0.35, -1], [1, -0.35]], TEAL),
             ("saddle\n$\\lambda_1>0>\\lambda_2$", [[1, 0], [0, -0.6]], ROSE),
             ("centre\n$\\mathrm{Re}\\,\\lambda=0$", [[0, -1], [1, 0]], AMBER)]
    fig, axs = plt.subplots(1, 4, figsize=(12.4, 3.5))
    x = np.linspace(-1, 1, 21)
    y = np.linspace(-1, 1, 21)
    X, Y = np.meshgrid(x, y)
    for ax, (title, A, col) in zip(axs, A_map):
        A = np.array(A, float)
        U = A[0, 0] * X + A[0, 1] * Y
        V = A[1, 0] * X + A[1, 1] * Y
        n = np.hypot(U, V) + 1e-9
        tidy(ax, grid=False)
        ax.streamplot(x, y, U, V, color=col, density=1.05, linewidth=1.1,
                      arrowsize=0.9, zorder=2)
        ax.plot([0], [0], "o", color=INK, ms=5, zorder=3)
        ax.set_title(title, fontsize=9.6)
        ax.set_xticks([]); ax.set_yticks([])
        ax.set_xlim(-1, 1); ax.set_ylim(-1, 1)
    fig.suptitle("Linearise, look at the eigenvalues: the whole local theory",
                 fontsize=11.5, weight="bold", y=1.04)
    save(fig, "linear-stability-zoo")


@figure("bifurcation-diagrams")
def fig_bifurcation():
    """The four elementary ways a fixed point can be created or destroyed."""
    r = np.linspace(-1.05, 1.05, 400)
    rp = r[r >= 0]
    rn = r[r <= 0]
    fig, axs = plt.subplots(1, 4, figsize=(12.6, 3.6))

    a = axs[0]
    tidy(a, grid=False)
    a.plot(rn, np.sqrt(-rn), color=BLUE, lw=2.2)
    a.plot(rn, -np.sqrt(-rn), color=ROSE, lw=2.0, ls=(0, (4, 3)))
    a.axvline(0, color=MUTED, lw=0.9); a.axhline(0, color=MUTED, lw=0.9)
    a.set_title("saddle-node\n$\\dot{x}=r+x^2$", fontsize=10)
    a.text(-0.95, 0.62, "annihilation\nat $r=0$", fontsize=8.4, color=MUTED, style="italic")

    b = axs[1]
    tidy(b, grid=False)
    b.plot(r, r, color=BLUE, lw=2.2)
    b.plot(rp, rp, color=ROSE, lw=2.0, ls=(0, (4, 3)))
    b.plot(rn, np.zeros_like(rn), color=BLUE, lw=2.2)
    b.plot(rp, np.zeros_like(rp), color=ROSE, lw=2.0, ls=(0, (4, 3)))
    b.axvline(0, color=MUTED, lw=0.9); b.axhline(0, color=MUTED, lw=0.9)
    b.set_title("transcritical\n$\\dot{x}=rx-x^2$", fontsize=10)
    b.text(-1.0, 0.72, "the two branches\nswap roles", fontsize=8.4, color=MUTED, style="italic")

    c = axs[2]
    tidy(c, grid=False)
    c.plot(rn, np.zeros_like(rn), color=BLUE, lw=2.2)
    c.plot(rp, np.zeros_like(rp), color=ROSE, lw=2.0, ls=(0, (4, 3)))
    c.plot(rp, np.sqrt(rp), color=BLUE, lw=2.2)
    c.plot(rp, -np.sqrt(rp), color=BLUE, lw=2.2)
    c.axvline(0, color=MUTED, lw=0.9); c.axhline(0, color=MUTED, lw=0.9)
    c.set_title("pitchfork\n$\\dot{x}=rx-x^3$", fontsize=10)
    c.text(-1.0, 0.72, "symmetry breaking:\none branch becomes two", fontsize=8.4,
           color=MUTED, style="italic")

    d = axs[3]
    tidy(d, grid=False)
    d.plot(rn, np.zeros_like(rn), color=BLUE, lw=2.2)
    d.plot(rp, np.zeros_like(rp), color=ROSE, lw=2.0, ls=(0, (4, 3)))
    d.plot(rp, 0.95 * np.sqrt(rp), color=TEAL, lw=2.2)
    d.fill_between(rp, 0, 0.95 * np.sqrt(rp), color=TEAL, alpha=0.12)
    d.axvline(0, color=MUTED, lw=0.9); d.axhline(0, color=MUTED, lw=0.9)
    d.set_title("Hopf\n$r=$ cycle amplitude$^2$", fontsize=10)
    d.text(-1.0, 0.72, "a fixed point gives birth\nto a self-sustained cycle", fontsize=8.4,
           color=MUTED, style="italic")

    for ax in axs:
        ax.set_xlabel("control parameter $r$", fontsize=9)
        ax.set_xlim(-1.05, 1.05); ax.set_ylim(-0.75, 0.95)
    axs[0].set_ylabel("attractor $x$")
    fig.suptitle("Bifurcations: stable branch solid, unstable branch dashed",
                 fontsize=11.5, weight="bold", y=1.05)
    save(fig, "bifurcation-diagrams")


@figure("routes-to-chaos")
def fig_routes_to_chaos():
    """Period doubling in the logistic map, and the Lyapunov exponent that sees it."""
    rs = np.linspace(2.45, 4.0, 1700)
    x = np.full(rs.size, 0.4)
    for _ in range(1400):
        x = rs * x * (1.0 - x)
    hist = np.empty((280, rs.size))
    for i in range(280):
        x = rs * x * (1.0 - x)
        hist[i] = x
    H, xe, re_ = np.histogram2d(np.repeat(rs, 280), hist.T.ravel(),
                                bins=[rs, np.linspace(0, 1, 420)])

    xl = np.full(rs.size, 0.4)
    lam = np.zeros(rs.size)
    for _ in range(600):
        xl = rs * xl * (1.0 - xl)
    for _ in range(3000):
        xl = rs * xl * (1.0 - xl)
        lam += np.log(np.abs(rs * (1.0 - 2.0 * xl)))
    lam /= 3000.0

    fig, (a, b) = plt.subplots(1, 2, figsize=(11.6, 4.1),
                               gridspec_kw={"width_ratios": [1.15, 1]})
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list("f", ["#ffffff", "#c7dcff", "#1f6feb", "#0b2447", "#12002e"])
    a.imshow(H.T, origin="lower", aspect="auto", cmap=cmap,
             extent=[rs[0], rs[-1], 0, 1], interpolation="nearest")
    a.set_title("The logistic map $x\\mapsto r\\,x(1-x)$: the period-doubling cascade")
    a.set_xlabel("growth parameter $r$"); a.set_ylabel("attractor $x$")
    a.grid(False)
    for r0, lab in [(3.0, "$2$-cycle"), (3.449, "$4$"), (3.544, "$8$"), (3.5699, "onset of chaos")]:
        a.axvline(r0, color="#ffffff", lw=0.8, alpha=0.6)
    a.text(3.57, 0.4, "chaos", color="#ffffff", fontsize=9, weight="bold")
    a.text(2.62, 0.82, "fixed point", color=INK, fontsize=8.5)
    a.text(3.02, 0.06, "period 2  $\\to$  4  $\\to$  8  $\\to\\cdots$", color=INK, fontsize=8.5,
           rotation=0)

    tidy(b)
    b.plot(rs, lam, color=VIOLET, lw=1.6)
    b.axhline(0, color=MUTED, lw=1.0)
    b.fill_between(rs, lam, 0, where=lam > 0, color=ROSE, alpha=0.22)
    b.set_title("Lyapunov exponent $\\lambda(r)=$ average local stretching")
    b.set_xlabel("growth parameter $r$"); b.set_ylabel("$\\lambda$")
    b.annotate("$\\lambda<0$: predictable\n(periodic windows)", (3.15, -1.05), (2.6, -1.95),
               fontsize=8.8, color=BLUE, arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.1))
    b.annotate("$\\lambda>0$: chaos;\nwindows reopen ($\\lambda<0$)", (3.86, 0.45), (3.45, 1.0),
               fontsize=8.8, color=ROSE, arrowprops=dict(arrowstyle="->", color=ROSE, lw=1.1))
    b.set_ylim(-2.4, 1.25)
    save(fig, "routes-to-chaos")
