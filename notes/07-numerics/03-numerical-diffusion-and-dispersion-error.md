---
title: Numerical diffusion & dispersion
blurb: The two errors every transport scheme commits — fronts that smear and waves that lag — how to measure them, and how to trade one for the other.
depth: 2
tags: [numerical diffusion, dispersion, modified equation, amplification factor]
---

# Numerical diffusion & dispersion

> **One-line picture.** A discretised advection operator is a *slightly different* operator. The
> difference always shows up as extra smoothing (diffusion) or wrong wave speed (dispersion) — or both.
>
> **Prerequisites.** [CFL & stiffness](02-cfl-stiffness-and-time-integration.md),
> [spectral view](../01-foundations/06-spectral-and-green-function-view.md) ·
> **Leads to.** [limiters, TVD & WENO](04-limiters-tvd-and-weno.md)

![**Figure 26.** The error portrait. Left: after two periodic crossings, upwind advection smears the pulse while Lax–Wendroff rings. Middle: the amplification factor $|G(k)|$ — above one means unconditional instability. Right: the phase portrait — a lag means every wave travels at the wrong speed.](../../figures/numerical-error-portrait.svg)

## L1 · Where the errors come from

Take first-order upwind for $\partial_tc+U\partial_xc=0$ and Taylor-expand as if the scheme were exact.
The **modified equation** is

$$\partial_tc+U\partial_xc=D_{\rm num}\partial_x^2c+\cdots,\qquad
D_{\rm num}=\frac{U\Delta x}{2}(1-\mathrm{CFL}) .$$

So upwinding is *advection plus diffusion* — the scheme solves the wrong PDE, albeit one that converges
to the right one as $\Delta x\to0$. Lax–Wendroff, by contrast, is exact to second order and therefore has
no leading diffusion term: what remains is *dispersion*, $\partial_x^3c$ terms that make waves travel at
slightly wrong speeds, producing oscillations behind sharp features.

| Scheme | Leading error | Symptom | CFL behaviour |
|---|---|---|---|
| upwind (1st) | $D_{\rm num}\partial_{xx}$ | smears fronts | $D_{\rm num}\to0$ as CFL $\to1$ |
| Lax–Friedrichs (1st) | large diffusion | very diffuse | — |
| Lax–Wendroff (2nd) | dispersive $\partial_{xxx}$ | wiggles/ringing | worst at CFL $=0.5$ |
| beam-warming (2nd upwind) | dispersive | asymmetric ringing | one-sided |
| implicit upwind (1st) | very large $D_{\rm num}$ | heavy smearing | $D_{\rm num}$ grows with CFL |
| spectral | exponential (smooth data) | Gibbs at discontinuities | — |

## L2 · The measurement framework

Work in Fourier space: the discrete amplification factor $G_{\rm num}(k)$ should equal $e^{-ikU\Delta t}$.
Two diagnostics follow:

* **Amplitude error** $1-|G|$: positive $=$ numerical diffusion. Integrate it over a step to get the
  "effective viscosity" of your scheme — a number you can compare against the physical $D$ (the ratio is
  what decides whether your scheme is acceptable at your Péclet number).
* **Phase error** $\arg G+ikU\Delta t$: nonzero $=$ numerical dispersion. It makes every wave travel at
  the wrong speed, which matters disproportionately when many waves interact (turbulence, acoustics).

A useful rule: *first-order schemes are accurate when the physical diffusion dominates*; when the
physical $\mathrm{Pe}$ is large, you must either use higher order with limiters, or accept that you are
simulating a diffusive problem you did not intend.

## L3 · What the mathematics guarantees

* **Godunov's order barrier.** A linear, monotone scheme is at most first order. Monotonicity
  (no new extrema, positivity) and second-order accuracy are mutually exclusive without nonlinearity —
  hence [limiters](04-limiters-tvd-and-weno.md).
* **Dissipation and dispersion are not free choices.** Any consistent scheme has an error operator whose
  leading term is one of these two forms; you choose the balance, not whether it appears.
* **Total variation.** TVD schemes prevent new extrema in space but may still be only first order at
  extrema (the classic limiter clipping problem at local maxima) — a second-order accurate *linear* TVD
  scheme does not exist.
* **Time-stepping contributes too.** Implicit schemes add their own damping (backward Euler is very
  diffusive); Crank–Nicolson has a weak phase error at large $\Delta t$. Analyse space and time errors
  together via $G_{\rm full}(k,\Delta t)$.

## L4 · Practicalities

* **Report the observed effective viscosity/dispersion** of your scheme, not just the grid size. Compare
  it to the physical coefficients: if $D_{\rm num}\gtrsim D$, you are simulating the scheme.
* **Mesh refinement studies must reveal the asymptotic order**; if order drops, find the culprit
  (boundaries, limiters, source terms, time splitting).
* **Do not compare against an analytic solution on a scaled grid without checking the CFL**; the error
  changes qualitatively with CFL (upwind is best at CFL $\to1$).
* **Diagnostics to keep in your workflow**: amplitude and phase portraits per scheme, and a convergence
  plot with error norms ($L^1$ to expose smearing, $L^\infty$ to expose ringing).
* **Benchmarks**: the Gaussian advection test (wrapped, with an exact answer), the Zalesak disk, and
  linear-advection convergence studies ([V&V](12-verification-validation-and-benchmarks.md)).

## Checks

1. What is the numerical diffusivity of first-order upwind, and when does it vanish? *($\frac{U\Delta
   x}{2}(1-\mathrm{CFL})$; it vanishes as CFL $\to1$.)*
2. Why does reducing $\Delta x$ not always reduce ringing? *(Second-order schemes have dispersive error
   that scales as $\Delta x^2$ but persists — and sharp features keep exciting it.)*
3. Why are $L^1$ and $L^\infty$ errors both needed? *($L^1$ measures smearing, $L^\infty$ exposes
   oscillations.)*

## See also

[CFL, stiffness & time integration](02-cfl-stiffness-and-time-integration.md) ·
[Limiters, TVD & WENO](04-limiters-tvd-and-weno.md) ·
[The spectral view](../01-foundations/06-spectral-and-green-function-view.md) ·
[Advection](../02-bulk/01-advection.md)
