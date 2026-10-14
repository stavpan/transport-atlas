---
title: CFL, stiffness & time integration
blurb: Why explicit steps are limited by the fastest wave, why implicit steps are limited by nothing — and how to choose between them.
depth: 2
tags: [CFL, stability, stiffness, IMEX, backward Euler]
---

# CFL, stiffness & time integration

> **One-line picture.** An explicit step may not let information jump more than one cell; an implicit
> step may, but it must solve a system. Stiffness is the gap between the fastest and slowest
> timescales — and it decides which of the two you can afford.
>
> **Prerequisites.** [discretisation & stability](01-discretization-consistency-stability-convergence.md) ·
> **Leads to.** [operator splitting & coupling](05-operator-splitting-and-multiphysics-coupling.md),
> [linear solvers](06-linear-solvers-and-preconditioning.md)

![**Figure 25.** Stability regions and the Courant condition. Forward Euler is confined to a disc;
backward Euler covers the entire left half-plane. Stiff transport pushes the eigenvalues far left, which
is why explicit methods are impossible there and implicit methods are cheap in stability terms —
though not in cost.](../../figures/stability-regions.svg)

## L1 · The two limits

* **Advection (hyperbolic):** the CFL condition $|U|\Delta t/\Delta x\le1$ (in $d$ dimensions roughly
  $\le1/\sqrt d$ for multidimensional explicit schemes). It is a *domain-of-influence* statement: the
  numerical solution may not use information from farther than a wave can travel in one step.
* **Diffusion (parabolic):** $\Delta t\le\Delta x^2/(2D)$. This is far harsher: halving $\Delta x$
  quadruples the number of steps, and in $d$ dimensions the time step scales as $\Delta x^2/d$.
* **Reaction:** the fastest rate constant sets an explicit limit, $\Delta t\lesssim1/k_{\max}$, which can
  be nanoseconds in combustion while the flame takes milliseconds to evolve.

**Stiffness ratio** $\lambda_{\max}/\lambda_{\min}$ measures the separation. Stiff systems are not
unstable *per se*, but explicit schemes pay the fastest scale to resolve the slowest — a ratio that can
reach $10^{12}$ in reactive transport.

## L2 · The schemes, and what each buys

| Scheme | Order | Stability | Best for |
|---|---|---|---|
| forward Euler | 1 | $|1+\lambda\Delta t|\le1$ | cheap, non-stiff, adjoint-ish |
| backward Euler | 1 | L-stable (no limit) | stiff, unconditionally stable, dissipative |
| Crank–Nicolson | 2 | A-stable, not L-stable | second order; can ring on stiff transients |
| explicit RK4 | 4 | limited region | accuracy for non-stiff smooth problems |
| IMEX (e.g. RK-IMEX) | 2–3 | implicit stiff part, explicit transport | advection–diffusion–reaction |
| BDF2/BDF3 | 2–3 | stiffly stable, L-stable variants | long-time stiff simulation |
| exponential integrators | 2–4 | exact for linear stiff part | reaction–diffusion, oscillatory stiff |
| Rosenbrock | 2–4 | L-stable | stiff with moderate nonlinearity |

The decisive distinction is **A-stability vs L-stability**: A-stable schemes control growth; L-stable
schemes also damp the fastest modes to zero, which is what you want when the fast mode is irrelevant
physics (stiff chemistry) — Crank–Nicolson's failure to do so is the famous source of ringing.

## L3 · What the mathematics guarantees

* **Dahlquist's barriers.** No explicit linear multistep method is A-stable above order 2; A-stable
  linear multistep methods cannot exceed order 2 unless they sacrifice something (BDF up to 6 is
  stiffly stable rather than A-stable). This is why high-order stiff integration goes to implicit
  Runge–Kutta or exponential methods.
* **Order reduction.** For stiff problems the *observed* order of implicit schemes often drops, because
  the error constants are amplified by the stiff eigenvalues; measure the rate, do not assume it.
* **Stability ≠ accuracy.** An explicit scheme below its stability limit may still be wildly inaccurate
  in phase (see [numerical dispersion](03-numerical-diffusion-and-dispersion-error.md)). Separating the
  two questions is the most valuable habit in numerical transport.
* **Adaptive stepping needs a proper error estimate** (embedded pairs, or step doubling) and a *relative*
  tolerance: concentrations spanning decades need per-species scaling.

## L4 · Practicalities

* **Choose by the dimensionless groups**: diffusion-dominated $\to$ implicit; advection-dominated $\to$
  explicit with a CFL-based step; reactive $\to$ implicit chemistry (per-cell, cheaply vectorised);
  mixed $\to$ IMEX.
* **Never let the CFL number silently exceed 1** in an explicit advection step; it is a stability
  violation, not an accuracy warning.
* **Adaptive initial steps** matter in transient problems; start small and let the controller grow.
* **Report the CFL and diffusion numbers** with every result — they are as important as the grid size.
* **Benchmarks**: linear advection and diffusion with analytic solutions, the ROBER stiff kinetics
  problem, and step-size convergence studies
  ([V&V](12-verification-validation-and-benchmarks.md)).

## Checks

1. Why is the diffusive limit quadratic in $\Delta x$ while the advective limit is linear? *(Diffusion
   propagates as $\sqrt{Dt}$; resolving it requires $\Delta t\sim\Delta x^2/D$.)*
2. What extra property does L-stability give over A-stability? *(Damping of fast modes — no ringing on
   stiff transients.)*
3. Why can an accurate scheme still be useless? *(Phase errors make wave speeds wrong even when
   amplitudes are right.)*

## See also

[Discretisation & stability](01-discretization-consistency-stability-convergence.md) ·
[Numerical diffusion & dispersion](03-numerical-diffusion-and-dispersion-error.md) ·
[Operator splitting & coupling](05-operator-splitting-and-multiphysics-coupling.md) ·
[Stability figure in context](../01-foundations/06-spectral-and-green-function-view.md)
