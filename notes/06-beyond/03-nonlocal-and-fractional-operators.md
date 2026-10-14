---
title: Nonlocal & fractional operators
blurb: Transport where distant points talk to each other — fractional Laplacians, tempered jumps, nonlocal diffusion, peridynamics and how to solve them.
depth: 3
tags: [fractional, nonlocal, Levy, peridynamics, Caputo]
---

# Nonlocal & fractional operators

> **One-line picture.** Replace the Laplacian — which only listens to infinitesimal neighbours — by an
> integral over a neighbourhood, and transport acquires long jumps, long memory and new boundary
> physics.
>
> **Prerequisites.** [anomalous diffusion](../03-microscopic/08-anomalous-diffusion.md) ·
> **Leads to.** [microcontinuum continua](11-microcontinuum-and-generalized-continua.md),
> [stochastic PDEs](07-stochastic-pdes-and-random-media.md)

## L1 · Why nonlocality, and what it looks like

Local PDEs assume that what happens at a point depends only on derivatives *at* that point. For many
media this is false:

* **Space-fractional** operators replace $\nabla^2$ by $(-\Delta)^{\beta/2}$, an integral over jumps of
  length $r$ weighted like $r^{-d-\beta}$: infinite second moment, Lévy statistics.
* **Time-fractional** operators replace $\partial_t$ by Caputo derivatives $D_t^{\alpha}$: a power-law
  memory kernel, subdiffusion, non-exponential relaxation.
* **Nonlocal diffusion** $\partial_tc=\int K(\mathbf x,\mathbf y)[c(\mathbf y)-c(\mathbf x)]\,\mathrm d\mathbf y$
  is the general form; compactly supported kernels give finite-range coupling.
* **Peridynamics** applies the same idea to solids: force is a nonlocal functional over a horizon
  $\delta$, which removes the crack-tip singularity and lets cracks nucleate and branch naturally.

## L2 · The operators, side by side

| Operator | Definition | Effect |
|---|---|---|
| fractional Laplacian | $(-\Delta)^{\beta/2}u\propto\text{p.v.}\!\int\frac{u(x)-u(y)}{\|x-y\|^{d+\beta}}\mathrm dy$ | $\beta=2$ local; $\beta<2$ jumps |
| Caputo derivative | ${}^CD_t^{\alpha}u=\frac{1}{\Gamma(1-\alpha)}\int_0^t\frac{u'(s)}{(t-s)^{\alpha}}\mathrm ds$ | power-law memory, Mittag-Leffler decay |
| nonlocal diffusion | integral with kernel $K$ | tunable coupling range |
| peridynamic operator | $\int_{\mathcal H}\mathbf f(\mathbf u'-\mathbf u)\,\mathrm dV'$ | crack-friendly, finite horizon |
| tempered kernel | $e^{-\lambda r}r^{-d-\beta}$ | heavy tails with exponential truncation (physical) |

A master-form transport equation is then $\partial_t^{\alpha}c=D\nabla^{\beta}c+f$, with orders fitted
from measured MSD exponents ([anomalous diffusion](../03-microscopic/08-anomalous-diffusion.md)).

## L3 · What the mathematics guarantees

* **Boundary conditions change.** A fractional operator needs data *outside* the domain (a volume
  constraint); a local no-flux condition alone is meaningless. This is the biggest practical source of
  modelling error.
* **Spectra change.** Fractional eigenvalues scale as $k^{\beta}$ rather than $k^2$, so every
  relaxation-time and spectral-gap estimate in this atlas is modified.
* **Variational structure survives.** $(-\Delta)^{\beta/2}$ is the gradient of a convex functional, so
  energy methods, maximum principles and entropy estimates hold in modified form — which is why
  fractional problems are tractable, not merely exotic.
* **Limits are meaningful.** $\beta\to2$ and horizon $\delta\to0$ recover the classical equations, which
  is how nonlocal models are validated.

## L4 · Numerics

* **Dense matrices are fatal** ($O(N^2)$ memory): use Toeplitz structure, FFT for uniform constant
  coefficients, fast multipole for peridynamics, convolution quadrature for time-fractional operators.
* **Heterogeneous coefficients break FFT**; then hierarchical matrices or asymptotically compatible
  schemes are needed — the latter converge to the *local* limit as the horizon shrinks with the grid.
* **Monte Carlo sidesteps the matrices**: simulate the underlying jump process
  ([particle methods](../07-numerics/09-particle-and-monte-carlo-methods.md)).
* **Benchmarks**: fractional-Gaussian profiles, Barenblatt-type solutions, peridynamic crack benchmarks
  (Kalthoff–Winkler), Mittag-Leffler relaxation
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Tempered space–time fractional models; engineering-scale peridynamics; nonlocal
  phase-field and damage models; learning kernels from data.

## Checks

1. What changes about boundary conditions? *(Data over a neighbourhood outside the domain is required.)*
2. Why does the fractional spectrum go as $k^\beta$? *(Scale invariance of the kernel.)*
3. What does "asymptotically compatible" mean? *(Refining the grid while shrinking the horizon
   converges to the local equation.)*

## See also

[Anomalous diffusion](../03-microscopic/08-anomalous-diffusion.md) ·
[Microcontinuum & generalized continua](11-microcontinuum-and-generalized-continua.md) ·
[Stochastic PDEs & random media](07-stochastic-pdes-and-random-media.md) ·
[Particle & Monte Carlo methods](../07-numerics/09-particle-and-monte-carlo-methods.md)
