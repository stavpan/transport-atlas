---
title: Numerics & inversion
blurb: How to solve transport equations honestly, how to know when you have failed, and how to get parameters back out of data.
depth: 2
tags: [index, numerics, solvers, inversion]
---

# Numerics & inversion

Everything in this atlas eventually meets a computer. This category is the discipline of that meeting:
stability before accuracy, verification before validation, and uncertainty before reporting.

| # | Note | The one thing it gives you |
|---|---|---|
| 1 | [Discretisation, stability & convergence](01-discretization-consistency-stability-convergence.md) | the three questions, and the family tree of schemes |
| 2 | [CFL, stiffness & time integration](02-cfl-stiffness-and-time-integration.md) | why explicit steps are limited, implicit steps are not, and what stiffness costs |
| 3 | [Numerical diffusion & dispersion](03-numerical-diffusion-and-dispersion-error.md) | the two errors every scheme commits, and how to measure them |
| 4 | [Limiters, TVD & WENO](04-limiters-tvd-and-weno.md) | sharp fronts without ringing; beating Godunov's barrier |
| 5 | [Operator splitting & multiphysics coupling](05-operator-splitting-and-multiphysics-coupling.md) | solving coupled physics piecewise without introducing instability |
| 6 | [Linear solvers & preconditioning](06-linear-solvers-and-preconditioning.md) | the elliptic solve inside every implicit step |
| 7 | [Nonlinear solvers & continuation](07-nonlinear-solvers-and-continuation.md) | Newton, its failure modes, and how homotopy rescues them |
| 8 | [Mesh, adaptivity & parallel decomposition](08-mesh-adaptivity-moving-domains-and-parallel.md) | putting resolution where the action is; splitting the work |
| 9 | [Particle & Monte Carlo methods](09-particle-and-monte-carlo-methods.md) | when to stop meshing and start walking |
| 10 | [Inverse problems & data assimilation](10-inverse-problems-and-data-assimilation.md) | getting coefficients out of data, with honest uncertainty |
| 11 | [Machine learning & operator learning](11-machine-learning-and-operator-learning.md) | where learning helps, and the failures that matter |
| 12 | [Verification, validation & benchmarks](12-verification-validation-and-benchmarks.md) | manufactured solutions, convergence rates, and the standard test cases |
| 13 | [Structure-preserving discretisations](13-structure-preserving-discretizations.md) | schemes that respect conservation, positivity and entropy by construction |

![**Figure F.** Stability and the Courant condition: forward Euler lives in a small disc while backward
Euler covers the whole stable half-plane — which is why stiff transport must be implicit.](../../figures/stability-regions.svg)

## The order to read them in

1. **Understand the operator** ([discretisation](01-discretization-consistency-stability-convergence.md))
   and your regime ([dimensionless numbers](../01-foundations/05-dimensionless-numbers.md)).
2. **Pick the time treatment** ([CFL & stiffness](02-cfl-stiffness-and-time-integration.md)) and the
   spatial scheme ([limiters](04-limiters-tvd-and-weno.md) if sharp features exist).
3. **Make the algebra work** ([linear](06-linear-solvers-and-preconditioning.md) and
   [nonlinear solvers](07-nonlinear-solvers-and-continuation.md)).
4. **Make it scale** ([mesh & parallel](08-mesh-adaptivity-moving-domains-and-parallel.md)).
5. **Prove it** ([V&V](12-verification-validation-and-benchmarks.md)) before believing any physics.
6. **Then invert** ([inverse problems](10-inverse-problems-and-data-assimilation.md)) — remembering that
   inversion inherits every weakness of the forward solver.

> **The one habit that prevents most disasters:** separate *stability* from *accuracy*. A stable scheme can
> be wrong by a factor of two; an accurate scheme can be unstable and produce nothing. Diagnose which
> problem you have before changing anything.
