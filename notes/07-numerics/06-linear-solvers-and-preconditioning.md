---
title: Linear solvers & preconditioning
blurb: The elliptic solve inside every implicit step — Krylov methods, multigrid, preconditioners, and why transport problems are hard for them.
depth: 3
tags: [Krylov, CG, GMRES, multigrid, preconditioner, AMG]
---

# Linear solvers & preconditioning

> **One-line picture.** Every implicit time step hides an elliptic problem whose solution is *global*:
> a change anywhere affects everywhere. Solving it quickly is the difference between a usable code and
> an unusable one.
>
> **Prerequisites.** [CFL & time integration](02-cfl-stiffness-and-time-integration.md) ·
> **Leads to.** [nonlinear solvers & continuation](07-nonlinear-solvers-and-continuation.md),
> [mesh, adaptivity & parallel](08-mesh-adaptivity-moving-domains-and-parallel.md)

## L1 · What is being solved, and why it is hard

Implicit transport steps produce $A\mathbf x=\mathbf b$ with $A$ sparse but ill-conditioned. Sources of
difficulty:

* **Anisotropy**: a dispersion tensor with $\alpha_L/\alpha_T\sim100$ makes the operator very anisotropic;
  pointwise smoothers fail, and convergence degrades with the anisotropy squared.
* **High contrast**: permeability or conductivity spanning $10^6$ across cells (layers, fractures)
  destroys simple preconditioners.
* **Convection dominance**: the matrix loses symmetry (and often positive definiteness), so CG is out.
* **Coupling**: multiphysics adds blocks (flow–geomechanics) with very different scales.

## L2 · The toolbox

| Method | Requires | Use for |
|---|---|---|
| CG | symmetric positive definite | diffusion/elliptic, preconditioned |
| GMRES (restarted) | nonsymmetric | advection–diffusion, coupled blocks |
| BiCGSTAB / IDR | nonsymmetric | cheaper per iteration alternative to GMRES |
| multigrid (geometric) | structured hierarchy | elliptic, optimal $O(N)$ |
| algebraic multigrid (AMG) | matrix only | unstructured, high-contrast coefficients |
| domain decomposition (Schwarz) | partition | parallel scaling, adds coarse space |
| FFT / spectral | periodic, constant coefficients | ideal reference, fast Poisson |
| direct sparse (LU) | $O(N^{1.5})$ fill | small 2-D, ill-conditioned, robustness |

**Preconditioning is the whole game.** Practical rules: use AMG for elliptic blocks, incomplete LU or
line-relaxation for anisotropic advection–diffusion, block preconditioners (SIMPLE, Schur complement
approximations) for coupled flow, and always monitor the *true residual*.

## L3 · What the mathematics guarantees

* **Krylov convergence depends on the spectrum**, not the size: clustered eigenvalues converge in a few
  iterations. Preconditioning is the art of clustering.
* **Optimal complexity**: multigrid converges in a grid-independent number of iterations for ideal
  elliptic problems — the only method that does.
* **Eigenvalue-based judgement fails for non-normal operators**: transient growth is real, and
  convergence can stall even with nice eigenvalues. Monitor residuals, not spectra.
* **Saddle-point systems** (incompressible flow, mixed formulations) need block preconditioners;
  naive diagonal preconditioning ignores the physics of the Schur complement and converges slowly.

## L4 · Practicalities

* **Start with a good discretisation**: a conservative, well-scaled operator is easier to solve than a
  badly scaled one. Non-dimensionalise variables before assembly.
* **Solve to a tolerance that matters**: inexact solves within a Newton iteration should be tightened as
  Newton converges (Eisenstat–Walker), otherwise you waste effort or lose quadratic convergence.
* **Monitor**: iterations per solve, true residual history, and the condition estimate. A change in
  iteration counts is often the first sign of a modelling or meshing bug.
* **Parallelism**: strong scaling is limited by preconditioner scalability; multigrid coarse solves and
  domain-decomposition coarse spaces are the usual bottlenecks.
* **Benchmarks**: 2-D/3-D Poisson with high contrast, the SPE10 permeability field, and lid-driven
  cavity at increasing Reynolds number ([V&V](12-verification-validation-and-benchmarks.md)).

## Checks

1. Why is CG inappropriate for advection-dominated transport? *(The matrix is nonsymmetric.)*
2. Why does geometric multigrid beat Krylov methods on elliptic problems? *(Grid-independent iteration
   count: $O(N)$ total work.)*

## See also

[CFL & stiffness](02-cfl-stiffness-and-time-integration.md) ·
[Mesh, adaptivity & parallel decomposition](08-mesh-adaptivity-moving-domains-and-parallel.md) ·
[Structure-preserving discretisations](13-structure-preserving-discretizations.md)
