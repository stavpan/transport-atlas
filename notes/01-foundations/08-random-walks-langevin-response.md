---
title: Random walks, Langevin & response
blurb: Where smooth diffusion comes from microscopic randomness, why friction and noise are one thing, and how to simulate SDEs without lying.
depth: 2
tags: [Brownian, Langevin, fluctuation-dissipation, SDE, Einstein]
---

# Random walks, Langevin & the fluctuation–dissipation theorem

> **One-line picture.** Diffusion is not a fundamental law — it is what randomness looks like
> when you refuse to watch the randomness. And friction is inseparable from the noise that
> accompanies it.
>
> **Prerequisites.** [diffusion](../03-microscopic/01-diffusion.md) · **Leads to.**
> [Fokker–Planck](../05-kinetic/03-fokker-planck-and-kramers.md),
> [anomalous diffusion](../03-microscopic/08-anomalous-diffusion.md)

![**Figure 9.** Three views of one random walk: the Green function spreading, individual walkers with typical $\pm\sqrt{t}$ spread, and the MSD for normal, sub-, super- and ballistic transport.](../../figures/diffusion-suite.svg)

## L1 · Randomness in, smoothness out

A drunkard steps at random, yet the *distribution* of drunkards spreads smoothly and
predictably — exactly as the diffusion equation says. A drop of ink is the same story with
$10^{20}$ walkers. The deterministic PDE emerges from a probabilistic rule, and its coefficient
measures the steps, not the fluid.

## L2 · From a coin flip to Fick's law

A walker hopping $\pm a$ every $\tau$ obeys
$p_{n+1}(x)=\tfrac12p_n(x-a)+\tfrac12p_n(x+a)$, and the limit $a^2/2\tau\to D$ gives

$$\partial_tp=D\,\partial_x^2p,\qquad\langle x^2\rangle=2Dt\ \text{(1-D)},\quad
D=\frac{a^2}{2\tau}.$$

That limit *is* Fick's second law, and the Green function is Gaussian because of the central
limit theorem. Langevin keeps the dynamics instead of the distribution:

$$m\frac{\mathrm{d}v}{\mathrm{d}t}=-\gamma v+\xi(t),\qquad
\langle\xi(t)\xi(t')\rangle=2\gamma k_BT\,\delta(t-t').$$

Drag and random kicks are **not independent**: whatever removes energy must also supply it. The
overdamped limit gives the **Einstein relation** $D=k_BT/\gamma$, and with Stokes drag the
**Stokes–Einstein** formula $D=k_BT/(6\pi\mu a)$ for $\mathrm{Re}\ll1$.

## L3 · What the mathematics guarantees

* **Fokker–Planck.** The Langevin equation implies
  $\partial_tp=-\nabla\!\cdot\!(p\mathbf{F}/\gamma)+\nabla\!\cdot\!(D\nabla p)$, whose steady
  state is Boltzmann's $p\propto e^{-V/k_BT}$: detailed balance in one line.
* **Fluctuation–dissipation theorem.** The noise spectrum is fixed by the dissipation and the
  temperature (Johnson–Nyquist noise from resistance, Brownian motion from viscosity), which
  is also the microscopic origin of Onsager reciprocity —
  [linear response](09-linear-response-and-memory.md).
* **Second law from reversibility.** Trajectories are reversible; entropy growth is a statement
  about distributions and coarse-graining. Loschmidt's paradox dissolves here.
* **Anomalies are generic.** Heavy-tailed waiting times give subdiffusion, heavy-tailed jumps
  give superdiffusion, correlated velocities give ballistic motion —
  [CTRW](../03-microscopic/08-anomalous-diffusion.md).

## L4 · Numerics and frontiers

* **Integrators.** Euler–Maruyama (strong order 1/2), Milstein (order 1). Decide whether you
  need strong convergence (trajectories) or weak (statistics) — it changes the scheme.
* **Itô vs Stratonovich.** With multiplicative noise the two conventions differ by a drift term.
  Choose by how the noise arises in the physical limit, then stay consistent.
* **Monte Carlo cost** is $N^{-1/2}$ in *any* dimension: particle methods win in high dimensions
  and lose in low ones ([particle methods](../07-numerics/09-particle-and-monte-carlo-methods.md)).
* **Rare events** (escape, nucleation, failure) live in exponential tails; direct simulation
  never sees them — importance sampling, forward flux sampling and
  [Kramers theory](../05-kinetic/03-fokker-planck-and-kramers.md) are the tools.
* **Machine learning.** Score-based generative models are reverse-time diffusion SDEs: this
  atlas's Fokker–Planck, entropy and optimal-transport theory is their foundation.

## Checks

1. Why can $D$ and the friction not be chosen independently? *(FDT: both come from the same
   molecular collisions, $D=k_BT/\gamma$.)*
2. A 1 µm bead in water at 300 K: how long to diffuse one micron? *($D\approx4\times10^{-13}$
   m²/s, so tens of seconds — the reason micron-scale biology needs active transport.)*

## See also

[Diffusion](../03-microscopic/01-diffusion.md) ·
[Brownian motion & Einstein relations](../03-microscopic/02-brownian-motion-and-einstein-relations.md) ·
[Fokker–Planck & Kramers](../05-kinetic/03-fokker-planck-and-kramers.md) ·
[Linear response & memory](09-linear-response-and-memory.md)
