---
title: Limiters, TVD & WENO
blurb: How to get sharp fronts without ringing — monotonicity, flux limiters, and the nonlinear machinery that beats Godunov's order barrier.
depth: 3
tags: [TVD, WENO, limiters, MUSCL, monotonicity]
---

# Limiters, TVD & WENO

> **One-line picture.** Second-order accuracy creates new maxima; monotonicity forbids them. The escape
> is to make the scheme *nonlinear*: switch to first order exactly where a front needs it.
>
> **Prerequisites.** [numerical diffusion & dispersion](03-numerical-diffusion-and-dispersion-error.md) ·
> **Leads to.** [structure-preserving schemes](13-structure-preserving-discretizations.md),
> [conservation laws & shocks](../06-beyond/01-conservation-laws-and-shocks.md)

## L1 · The idea

Godunov's theorem says no linear monotone scheme exceeds first order. So build a nonlinear one: compute a
high-order flux, then **limit** it by comparing it with lower-order fluxes at the same face. Where the
solution is smooth, the high-order flux is used and you get accuracy; where it is sharply varying, the
limiter pulls the scheme back toward monotone first order, and no new extrema appear.

## L2 · The machinery

* **TVD (total variation diminishing):** $\mathrm{TV}(c^{n+1})\le\mathrm{TV}(c^n)$ with
  $\mathrm{TV}=\sum_i|c_{i+1}-c_i|$. Sufficient for monotonicity and no new extrema.
* **MUSCL / slope limiters:** reconstruct cell values with slopes, then limit the slope (minmod,
  superbee, van Leer, MC). One function per face, cheap and robust.
* **Flux limiters:** write the flux as a blend $\phi(r)$ of first- and second-order fluxes, with
  $r$ the ratio of consecutive gradients; TVD requires $\phi$ in a specific region (Sweby diagram).
* **ENO/WENO:** use the smoothest of several candidate stencils (ENO) or a weighted combination (WENO),
  giving high order in smooth regions and essentially no oscillation at discontinuities.
* **Positivity-preserving and maximum-principle-preserving limiters** extend the same logic to keep
  concentrations non-negative and bounded — essential for reactive transport.

## L3 · What the mathematics guarantees

* **Second-order TVD is impossible** for a *linear* scheme; TVD methods are nonlinear by construction.
* **Order loss at extrema.** TVD schemes clip smooth extrema, degrading local accuracy to first order
  there; WENO recovers full order in smooth regions including extrema, at higher cost.
* **Convergence to the entropy solution.** Provided the scheme is conservative and consistent, TVD/ENO
  schemes converge to the weak entropy solution of the conservation law
  ([shocks](../06-beyond/01-conservation-laws-and-shocks.md)).
* **Positivity is separate from monotonicity** and must be checked independently when source terms or
  diffusion are present.

## L4 · Practicalities

* **Choose the limiter by symptom**: minmod (diffusive but robust), van Leer/MC (balanced),
  superbee (sharp but can clip), WENO5 (smooth flows with occasional sharpness).
* **Limiters interact badly with implicit solvers** (nonsmooth functions frustrate Newton): use active-set
  detection or frozen limiters during the nonlinear iteration
  ([nonlinear solvers](07-nonlinear-solvers-and-continuation.md)).
* **Do not silence physical oscillations.** Oscillations in the *exact* solution (dispersive waves) must
  not be removed by a limiter — that is over-limiting, and it changes the physics.
* **Benchmarks**: Zalesak disk, Sod shock tube, the double Mach reflection, and tracer advection with
  positivity requirements ([V&V](12-verification-validation-and-benchmarks.md)).

## Checks

1. Which theorem forces limiters to be nonlinear? *(Godunov's order barrier.)*
2. What is the price of TVD at smooth extrema? *(Order reduction to first order there.)*

## See also

[Conservation laws & shocks](../06-beyond/01-conservation-laws-and-shocks.md) ·
[Numerical diffusion & dispersion](03-numerical-diffusion-and-dispersion-error.md) ·
[Structure-preserving discretisations](13-structure-preserving-discretizations.md)
