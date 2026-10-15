"""Part 11 — chaos, criticality, scaling, and noise-induced phenomena."""
import numpy as np
import matplotlib.pyplot as plt

from figlib import (figure, save, tidy, plain, arrow, box,
                    INK, MUTED, BLUE, TEAL, VIOLET, AMBER, ROSE, SLATE, GREEN, SKY)


@figure("chaos-sensitive-dependence")
def fig_chaos():
    """Lorenz: the same law, two starts a millionth apart, and the horizon."""
    def run(s0, n=7000, dt=0.005):
        s = np.array(s0, float)
        out = np.empty((n, 3))
        for i in range(n):
            def f(y):
                return np.array([10.0 * (y[1] - y[0]),
                                 y[0] * (28.0 - y[2]) - y[1],
                                 y[0] * y[1] - (8.0 / 3.0) * y[2]])
            k1 = f(s); k2 = f(s + 0.5 * dt * k1)
            k3 = f(s + 0.5 * dt * k2); k4 = f(s + dt * k3)
            s = s + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
            out[i] = s
        return out

    A = run([1.0, 1.0, 1.0])
    B = run([1.0 + 1e-6, 1.0, 1.0])
    t = np.arange(A.shape[0]) * 0.005
    d = np.linalg.norm(A - B, axis=1)

    fig, (a, b) = plt.subplots(1, 2, figsize=(11.2, 4.3),
                               gridspec_kw={"width_ratios": [1.1, 1]})
    tidy(a, grid=False)
    a.plot(A[:, 0], A[:, 2], color=BLUE, lw=0.6, alpha=0.85)
    a.plot(B[:, 0], B[:, 2], color=ROSE, lw=0.6, alpha=0.85)
    a.set_title("Two trajectories of $\\dot{x}=10(y-x)$ etc., started $\\varepsilon=10^{-6}$ apart")
    a.set_xlabel("$x$"); a.set_ylabel("$z$")
    a.text(0.02, 0.96, "they trace the same butterfly,\nbut not at the same time",
           transform=a.transAxes, va="top", fontsize=8.6, color=MUTED, style="italic")

    tidy(b)
    b.semilogy(t, d, color=VIOLET, lw=1.8)
    b.semilogy(t, 1e-6 * np.exp(0.906 * t), color=MUTED, lw=1.2, ls=(0, (4, 3)),
               label=r"reference slope: $\lambda\approx0.91$")
    b.set_title("Separation grows exponentially — then saturates")
    b.set_xlabel("time $t$"); b.set_ylabel("$|\\delta|$")
    b.legend(fontsize=8.4, loc="upper left")
    b.annotate("Lyapunov time $t_\\lambda=1/\\lambda\\approx1.1$:\n"
               "$10^{-6}$ becomes $O(1)$ in $\\approx14$ time units",
               (20, 0.35), (0.30, 0.12), textcoords="axes fraction", fontsize=8.8,
               color=ROSE, ha="left", va="bottom",
               arrowprops=dict(arrowstyle="->", color=ROSE, lw=1.0))
    b.set_ylim(1e-7, 60)
    save(fig, "chaos-sensitive-dependence")


@figure("phase-transition-order-parameter")
def fig_phase_transition():
    """Order parameter, diverging susceptibility, and the hysteresis loop."""
    T = np.linspace(0.05, 1.6, 260)
    m = np.full(T.size, 0.6)
    for _ in range(400):
        m = np.tanh(m / T)
    Tc = 1.0

    fig, axs = plt.subplots(1, 3, figsize=(13.0, 3.9))

    a = axs[0]
    tidy(a)
    a.plot(T, m, color=BLUE, lw=2.4)
    a.axvline(Tc, color=MUTED, lw=1.0, ls=(0, (4, 3)))
    a.set_title("Order parameter dies at $T_c$", fontsize=10.5)
    a.set_xlabel("temperature $T/T_c$"); a.set_ylabel("order parameter $m$")
    a.annotate("$m\\sim(T_c-T)^{1/2}$\n($\\beta=\\frac{1}{2}$, mean field)", (0.9, 0.62), (0.14, 0.72),
               fontsize=8.8, color=BLUE, arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.1))
    a.text(1.06, 0.55, "disordered", fontsize=8.6, color=MUTED)

    b = axs[1]
    tidy(b)
    Tl = np.linspace(1.002, 1.6, 300)
    b.loglog(Tl - Tc, 1.0 / (Tl - Tc), color=ROSE, lw=2.2)
    b.loglog([3e-2, 3e-1], [33.3, 3.33], color=MUTED, lw=1.2, ls=(0, (4, 3)))
    b.text(4.5e-2, 9.5, "slope $-\\gamma=-1$", fontsize=8.6, color=MUTED, rotation=-30)
    b.set_title("Susceptibility diverges: $\\chi\\propto(T-T_c)^{-\\gamma}$", fontsize=10.5)
    b.set_xlabel("$T-T_c$"); b.set_ylabel("$\\chi$")
    b.text(3e-2, 60, "$\\gamma=1$\n(mean field)", fontsize=8.8, color=MUTED)
    b.text(4e-4, 2.2, "the system is infinitely\nsoft to a nudge here",
           fontsize=8.6, color=ROSE, style="italic")

    c = axs[2]
    tidy(c, grid=False)
    h = np.linspace(-0.9, 0.9, 2400)
    def sweep(hs):
        mm = 0.7 if hs[0] > 0 else -0.7
        path = []
        for hv in hs:
            for _ in range(6):
                mm += 0.02 * (0.45 * mm - mm ** 3 + hv)
            path.append(mm)
        return np.array(path)
    up = sweep(h)
    dn = sweep(h[::-1])
    c.plot(h, up, color=BLUE, lw=2.0, label="field increasing")
    c.plot(h[::-1], dn, color=ROSE, lw=2.0, ls=(0, (4, 3)), label="field decreasing")
    c.axhline(0, color=MUTED, lw=0.9); c.axvline(0, color=MUTED, lw=0.9)
    c.set_title("Hysteresis: two states remember the path", fontsize=10.5)
    c.set_xlabel("applied field $h$"); c.set_ylabel("response $m$")
    c.legend(loc="upper left", fontsize=8.2)
    c.annotate("stored memory:\nmetastable branch", (0.45, 0.75), (0.16, 1.12),
               fontsize=8.6, color=VIOLET, arrowprops=dict(arrowstyle="->", color=VIOLET, lw=1.0))
    save(fig, "phase-transition-order-parameter")


@figure("scaling-collapse")
def fig_scaling_collapse():
    """One curve pretending to be many: universal scaling functions and data collapse."""
    rng = np.random.default_rng(7)
    tau, D = 1.21, 1.9
    s = np.logspace(0, 5.2, 600)
    fig, (a, b) = plt.subplots(1, 2, figsize=(11.0, 4.1))
    tidy(a); tidy(b)
    cols = [BLUE, TEAL, VIOLET, AMBER]
    for L, col in zip([32, 64, 128, 256], cols):
        cut = L ** D
        p = s ** -tau * np.exp(-s / cut) * (1 + 0.35 * rng.standard_normal(s.size))
        p = np.clip(p, 1e-30, None)
        a.loglog(s * 4e-4, p / np.max(p) * 4e3, color=col, lw=1.4, alpha=0.9,
                 label="system size $L=%d$" % L)
        b.loglog(s / cut, p * cut ** (tau - 1), color=col, lw=1.4, alpha=0.9)
    a.set_title("Four systems, four different distributions")
    a.set_xlabel("avalanche size $s$"); a.set_ylabel("$P(s)$ (shifted for clarity)")
    a.legend(fontsize=8.4)
    a.text(1.2, 2.6e3, "$P(s)\\sim s^{-\\tau}F(s/L^D)$", fontsize=10, color=INK)

    xr = np.logspace(-1.2, 1.2, 200)
    b.loglog(xr, xr ** -tau * np.exp(-xr), color=INK, lw=1.6, ls=(0, (4, 3)))
    b.set_title("Divide $s$ by $L^D$ and rescale: one master curve")
    b.set_xlabel("scaled size $s/L^D$"); b.set_ylabel("$L^{\\tau-1}P(s)$")
    b.text(1.4e-1, 8e-3, "collapse — the shape is\nthe same everywhere:\n$\\tau\\approx1.2$, $D\\approx1.9$",
           fontsize=8.8, color=MUTED, style="italic")
    b.text(6, 4e-4, "finite size only cuts\nthe tail", fontsize=8.6, color=ROSE)
    save(fig, "scaling-collapse")


@figure("noise-induced-transitions")
def fig_noise_induced():
    """Noise is not just blur: it can select a state, or destroy one."""
    x = np.linspace(-2.2, 2.2, 700)
    V = 0.5 * (x ** 2 - 1.0) ** 2
    fig, (a, b) = plt.subplots(1, 2, figsize=(11.0, 4.1))
    tidy(a)
    a.plot(x, V, color=MUTED, lw=1.4, label="$V(x)=\\frac{1}{2}(x^2-1)^2$")
    for D, col in [(0.04, BLUE), (0.16, TEAL), (0.45, ROSE)]:
        p = np.exp(-V / D)
        p = p / p.max()
        a.plot(x, p * 0.75, color=col, lw=2.0, label="$D=%g$" % D)
    a.axhline(0, color="#c9cfda", lw=0.8)
    a.set_ylim(-0.04, 1.75)
    a.set_xlabel("state $x$"); a.set_ylabel("$V$ and stationary density $\\propto e^{-V/D}$")
    a.set_title("Raising the noise melts the bimodal state")
    a.legend(fontsize=8.4, loc="upper right")
    a.text(0.0, 1.58, "two-peaked: the order survives\nthe noise", fontsize=8.6, color=BLUE,
           ha="center")
    a.text(0.0, 0.28, "one-peaked: the noise\nselected the mixed state", fontsize=8.6,
           color=ROSE, ha="center")

    rng = np.random.default_rng(21)

    tidy(b)
    dt, n, Tspan = 0.05, 8192, 409.6
    tt = np.arange(n) * dt
    w0 = 2.0 * np.pi * 8.0 / Tspan
    Ds = np.logspace(np.log10(0.03), np.log10(0.95), 14)
    snr = []
    for D in Ds:
        xr = np.full(24, 0.6)
        acc = np.zeros(n)
        for i in range(n):
            xr = xr + dt * (xr - xr ** 3 + 0.12 * np.cos(w0 * tt[i])) \
                + np.sqrt(2.0 * D * dt) * rng.standard_normal(xr.size)
            acc[i] = xr.mean()
        P = np.abs(np.fft.rfft(acc - acc.mean())) ** 2
        bg = np.median(np.concatenate([P[2:6], P[11:40]]))
        snr.append((P[8] - bg) / bg)
    snr = np.array(snr)
    b.semilogx(Ds, snr, "o-", color=VIOLET, lw=2.0, ms=4.5)
    b.set_title("Stochastic resonance: noise makes a weak signal audible")
    b.set_xlabel("noise intensity $D$"); b.set_ylabel("signal-to-noise ratio at $\\omega_0$")
    kbest = int(np.argmax(snr))
    b.plot([Ds[kbest]], [snr[kbest]], "o", color=ROSE, ms=10, zorder=5)
    b.annotate("the signal is periodic but sub-threshold:\nno noise $\\to$ no response; "
               "a little noise $\\to$\nprobabilistic hopping in step with the signal;\n"
               "too much noise $\\to$ the signal drowns",
               (Ds[kbest], snr[kbest]), (0.40, 0.16), textcoords="axes fraction",
               fontsize=8.4, color=MUTED, ha="left", va="bottom",
               arrowprops=dict(arrowstyle="->", color=ROSE, lw=1.1))
    b.text(0.30, 0.9, "used to explain ice-age cycles,\nand hiding in neurons and sensors",
           fontsize=8.4, color=VIOLET, style="italic")
    save(fig, "noise-induced-transitions")
