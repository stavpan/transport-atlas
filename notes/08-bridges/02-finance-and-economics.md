---
title: Transport in finance & economics
blurb: Why Black–Scholes is a backward diffusion equation, how optimal transport prices risk, and what a mean-field game has to do with a PDE.
depth: 3
tags: [Black-Scholes, Kolmogorov, stochastic control, mean-field games, optimal transport]
---

# Transport in finance & economics

> **One-line picture.** A price is a transported quantity: it drifts and diffuses, and its expectation can
> be computed by solving the same equations as heat flow, backwards in time.
>
> **Prerequisites.** [random walks & Langevin](../01-foundations/08-random-walks-langevin-response.md),
> [optimal transport](../06-beyond/10-optimal-transport-and-gradient-flows.md)

## L1 · The same equations in a new costume

Model an asset price as a stochastic process $\mathrm{d}S=\mu S\,\mathrm{d}t+\sigma S\,\mathrm{d}W$. The
value $V(S,t)$ of a contingent claim satisfies, by Itô's lemma plus no-arbitrage,

$$\partial_tV+\tfrac12\sigma^2S^2\partial_{SS}V+rS\partial_SV-rV=0,$$

the **Black–Scholes equation**: a *backward* parabolic PDE, mathematically the diffusion equation with
drift, run backwards in time. Its Green function is the lognormal kernel; the Feynman–Kac formula turns
expectations into PDE solutions, which is why Monte Carlo and finite differences are interchangeable
pricing tools.

Correspondences worth memorising:

| Transport object | Financial object |
|---|---|
| diffusion coefficient | volatility $\sigma^2$ |
| advection velocity | risk-free drift under the risk-neutral measure |
| initial condition | terminal payoff (hence backward in time) |
| boundary condition | payoff at barriers / asymptotics in $S$ |
| backward Kolmogorov | pricing PDE (Feynman–Kac) |
| Fokker–Planck (forward) | density of prices / risk-neutral distribution |
| local vol / Dupire | state-dependent diffusivity fitted to option prices |
| optimal transport | model-independent bounds, calibration, risk measures |
| Wasserstein gradient flow | mean-field games, agent-based equilibrium dynamics |

**Dupire's equation** is the inverse-problem face: given option prices for all strikes and maturities,
recover $\sigma(S,t)$ — a coefficient-identification problem, structurally identical to inferring
$D(c)$ from breakthrough curves ([inverse problems](../07-numerics/10-inverse-problems-and-data-assimilation.md)).

## L2 · Optimal transport and mean-field games

Two modern bridges:

* **Model-independent pricing**: optimal transport gives bounds on derivative prices consistent with
  observed marginal distributions (Martingale optimal transport) — the geometry of moving mass
  constrained by no-arbitrage.
* **Mean-field games**: when many interacting agents each optimise while reacting to the aggregate
  distribution, the equilibrium is a *coupled system* of a forward Fokker–Planck (transport of the
  population) and a backward Hamilton–Jacobi equation (optimal control). This is precisely the
  forward/backward structure of optimal control in transport
  ([Hamilton–Jacobi](../06-beyond/02-hamilton-jacobi-and-viscosity-solutions.md)), and it is now used for
  traffic, epidemics, energy markets and crowd dynamics.

## L3 · Where the analogy is genuinely useful

* **Numerical methods transfer**: implicit schemes, spectral methods, and rare-event simulation were all
  developed in PDE transport and are standard in derivative pricing.
* **Structural insight transfers**: the absence of arbitrage is a *monotonicity/maximum-principle*
  statement; a pricing PDE that violates the maximum principle allows arbitrage in the model.
* **Inverse problems are the same species**: calibration is ill-posed, needs regularisation, and produces
  parameters that are unidentifiable in some directions — exactly as in aquifer parameter estimation.
* **Caveat**: financial models have *no physical conservation law* and no measured microscale; the
  analogy is mathematical, not physical, and the validity of a model is judged by market behaviour and
  stability, not by a second law.

## L4 · Practice

* Sharp price fronts (digital options, barriers, American exercise) reintroduce everything from
  [limiters](../07-numerics/04-limiters-tvd-and-weno.md): oscillation and smearing near kinks, and the need
  for free-boundary ([obstacle](../06-beyond/12-variational-inequalities-and-hysteresis.md)) methods for
  American options.
* Long-horizon and high-dimensional problems push toward [Monte Carlo and particle methods](../07-numerics/09-particle-and-monte-carlo-methods.md)
  and, recently, [operator learning](../07-numerics/11-machine-learning-and-operator-learning.md).

## Checks

1. Why is Black–Scholes a backward equation? *(It is a conditional expectation of a terminal payoff.)*
2. What is the transport analogue of volatility? *(A state-dependent diffusion coefficient — the same
   object as $D(\mathbf x)$ in a heterogeneous medium.)*

## See also

[Random walks, Langevin & response](../01-foundations/08-random-walks-langevin-response.md) ·
[Optimal transport & gradient flows](../06-beyond/10-optimal-transport-and-gradient-flows.md) ·
[Hamilton–Jacobi & viscosity solutions](../06-beyond/02-hamilton-jacobi-and-viscosity-solutions.md) ·
[Inverse problems & data assimilation](../07-numerics/10-inverse-problems-and-data-assimilation.md)
