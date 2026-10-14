---
title: Discretisation, stability & convergence
blurb: The three questions of numerical transport — is my scheme consistent, is it stable, does it converge? — and the families of discretisations you can choose from.
depth: 2
tags: [finite volume, finite element, spectral, consistency, Lax-Richtmyer]
---

# Discretisation, stability & convergence

> **One-line picture.** Replace derivatives by differences (or fluxes, or basis functions), then prove
> three things: the discrete equations approximate the continuous ones, small errors do not grow, and
> therefore the answer converges.
>
> **Prerequisites.** [PDE taxonomy](../01-foundations/04-pde-taxonomy-and-boundary-conditions.md) ·
> **Leads to.** [CFL & stiffness](02-cfl-stiffness-and-time-integration.md),
> [numerical diffusion](03-numerical-diffusion-and-dispersion-error.md),
> [structure-preserving schemes](13-structure-preserving-discretizations.md)

## L1 · The logic

Three words govern everything:

* **Consistency** — the discretisation reproduces the PDE as $\Delta x,\Delta t\to0$ (check with a Taylor
  expansion; the leading leftover terms are the *truncation error*, which also tells you the *order*).
* **Stability** — errors do not grow without bound. Test by von Neumann analysis (eigenvalues of the
  amplification matrix, $|G(k)|\le1$), the energy method, or boundedness of the discrete semigroup.
* **Convergence** — the discrete solution approaches the true one. The **Lax–Richtmyer equivalence
  theorem** ties it together: *consistency $+$ stability $\iff$ convergence* for linear problems.

**Modified equations** are the practitioner's shortcut: Taylor-expand the scheme *as if it were exact*
and read off which PDE it actually solves. This is where "numerical viscosity" comes from — the
leading error term often looks exactly like a diffusion term, with a coefficient you did not choose.

## L2 · The families, and what each is good at

| Family | Conserves? | Geometry | Strengths | Weaknesses |
|---|---|---|---|---|
| finite difference | not automatically | structured grids | simplest, high order possible | geometry, conservation |
| finite volume | **exactly** (flux form) | any (unstructured) | conservation, shocks, multiphase | reconstruction needed for accuracy |
| finite element | exactly (weak form) | any, adaptive | elliptic problems, error theory | monotonicity not automatic |
| spectral | yes (globally) | simple domains | exponential accuracy for smooth data | Gibbs for discontinuities |
| spectral element / DG | yes | any | high order + geometry + hp-adaptivity | complexity, CFL for explicit DG |
| lattice-Boltzmann / particle | exactly (by construction) | particle-based | complex geometry, kinetic regimes | noise, low-Mach limits |
| neural / operator learning | not guaranteed | mesh-free | speed after training | accuracy guarantees, extrapolation |

The rule of thumb that runs through this atlas: **discretise the conserved form and let the fluxes
enforce conservation**; then add monotonicity/positivity constraints where the physics demands them.

## L3 · What the mathematics guarantees

* **Order and error estimates.** For a consistent scheme of order $p$ in space and $q$ in time, the error
  scales as $O(\Delta x^p+\Delta t^q)$ *provided* the solution is smooth enough — and provided stability
  holds. The smoothness clause is where high-order methods fail (see
  [limiters](04-limiters-tvd-and-weno.md)).
* **Stability is a property of the operator, not the grid.** Non-normal operators (advection with
  strong shear, MHD at low $\beta$) can be *asymptotically* but not *transiently* stable: eigenvalues are
  misleading. Use the pseudospectrum or the energy method.
* **the discrete maximum principle.** Monotone stencils (M-matrices) guarantee positivity and bounds;
  this is a nonlinear property that a linear stability analysis cannot see.
* **Verification needs more than convergence.** Check the *rate* by refinement studies (grid convergence
  index), and check conservation and symmetry properties that the scheme should preserve
  ([V&V](12-verification-validation-and-benchmarks.md)).

## L4 · Practicalities

* **Choose the discretisation from the operator's type**, not from taste: elliptic $\to$ FEM/FV with
  multigrid; parabolic $\to$ implicit stepping; hyperbolic $\to$ conservative FV with limiters; kinetic
  $\to$ particle/discrete-velocity methods.
* **Order reduction** is common: boundary closures, variable coefficients and nonlinearity can knock a
  nominally fourth-order scheme down to second. Measure the observed rate.
* **Conservation in practice**: sum the fluxes across the whole domain and compare with the change of
  mass; a mismatch means a bug, not "numerical diffusion".
* **Represent the geometry honestly**: body-fitted, cut-cell, immersed boundary or overset grids each
  trade accuracy against complexity.
* **Benchmarks**: manufactured solutions (the only test with a known answer), the lid-driven cavity,
  Taylor–Green vortex, and shock tubes
  ([V&V](12-verification-validation-and-benchmarks.md)).

## Checks

1. Which two conditions give convergence for linear problems? *(Consistency and stability — Lax–Richtmyer.)*
2. Why can eigenvalues of the amplification matrix be dangerously misleading? *(Non-normal operators can
   grow transiently while all eigenvalues are stable.)*
3. What is the modified equation of first-order upwind advection? *(Advection plus a diffusion term with
   $D_{\rm num}=\frac{U\Delta x}{2}(1-\mathrm{CFL})$.)*

## See also

[CFL, stiffness & time integration](02-cfl-stiffness-and-time-integration.md) ·
[Numerical diffusion & dispersion](03-numerical-diffusion-and-dispersion-error.md) ·
[Verification, validation & benchmarks](12-verification-validation-and-benchmarks.md) ·
[Structure-preserving discretisations](13-structure-preserving-discretizations.md)
