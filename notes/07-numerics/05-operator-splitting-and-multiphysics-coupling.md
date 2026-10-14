---
title: Operator splitting & multiphysics coupling
blurb: Solving coupled physics one piece at a time — Strang splitting, IMEX, and why partitioned coupling can be unstable when monolithic coupling is not.
depth: 3
tags: [splitting, Strang, IMEX, partitioned, monolithic, coupling]
---

# Operator splitting & multiphysics coupling

> **One-line picture.** Complex transport problems are sums of simple operators. Solve them in turn and
> you get a scheme that is only as good as the *commutator* you threw away.
>
> **Prerequisites.** [CFL & stiffness](02-cfl-stiffness-and-time-integration.md) ·
> **Leads to.** [inverse problems](10-inverse-problems-and-data-assimilation.md),
> [subsidence & poroelasticity](../04-interaction/13-subsidence-and-poroelasticity.md)

## L1 · Why split, and what it costs

Reaction–diffusion–advection, flow–geomechanics, radiation–hydrodynamics: each subproblem has its own
best method. Splitting lets you use them — but introduces an error proportional to the commutator
$[A,B]=AB-BA$ of the operators.

| Splitting | Steps | Order | Note |
|---|---|---|---|
| Lie–Trotter | $A$ then $B$ | 1 | simplest, cheapest |
| Strang | $A/2$, $B$, $A/2$ | 2 | standard for reaction–diffusion |
| IMEX | implicit stiff part, explicit transport | 2–3 | avoids splitting stiff chemistry |
| exponential | exact linear part + nonlinear corrector | 2–4 | good for stiff linear operators |

The commutator error matters exactly when both operators are fast — which is the physically interesting
regime. Diagnostics: compare a split scheme with a fully coupled solve on a test problem, and refine
$\Delta t$ to see whether the splitting error dominates.

## L2 · Coupling strategies for multiphysics

* **Monolithic (simultaneous):** solve all fields together in one Newton loop. Robust, but requires a
  coupled Jacobian and a coupled preconditioner.
* **Partitioned / staggered (sequential):** solve each physics in turn with data exchange. Modular and
  cheap, but may become *unstable* even when the continuous system is stable — the added-mass and
  added-stiffness instabilities of fluid–structure and poroelastic coupling are the classic examples.
* **Fixed-stress / drained- undrained splits** for poroelasticity: expose a parameter that makes the
  staggered scheme unconditionally stable while retaining accuracy.
* **Iterative coupling:** repeat the staggered step until convergence within the time step; one
  iteration ("loose coupling") is cheapest and least accurate.

| Coupling | Cost per step | Stability | Use when |
|---|---|---|---|
| monolithic | high | best | strong coupling, strong nonlinearity |
| fixed-stress / stabilised split | moderate | very good | poroelasticity (industry standard) |
| loose partitioned | low | conditional | weak coupling, exploratory work |
| IMEX in time | moderate | good | stiff reactions + transport |

## L3 · What the mathematics guarantees

* **Splitting order** follows from the Baker–Campbell–Hausdorff expansion: Strang is second order because
  the leading commutator term cancels by symmetry.
* **Conservation can be lost.** Splitting can break exact conservation laws unless each substep is
  conservative *and* the split is designed to preserve the invariant — a frequent silent bug in
  climate and reactive-transport codes.
* **Partitioned instability is a mathematical fact**, not an implementation bug: the coupling operator's
  spectrum can move into the unstable half-plane even though both subsystems are individually stable.
* **Positivity.** Splitting positive substeps does not guarantee positive results unless the substeps
  commute appropriately; check with the reaction–diffusion pair.

## L4 · Practicalities

* **Keep the splitting error below the discretisation error** and verify by refining in time only.
* **Prefer IMEX over splitting** for stiff reactions: it avoids the first-order splitting error that
  plagues fast-chemistry problems.
* **Stabilise partitioned schemes structurally** (fixed-stress, Robin transmission, Aitken relaxation)
  rather than by tuning under-relaxation parameters.
* **Benchmarks**: Mandel and Terzaghi problems (poroelasticity), reaction–diffusion with an analytic
  solution, and fluid–structure benchmarks (Turek–Hron)
  ([V&V](12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Adaptive split/non-split switching; learned coupling operators; error estimators that
  include the splitting error.

## Checks

1. Why is Strang splitting second order when Lie–Trotter is first? *(Symmetry cancels the leading
   commutator term.)*
2. When does a staggered scheme fail while both physics are stable? *(Strong coupling — added-mass or
   added-stiffness instability.)*

## See also

[CFL & time integration](02-cfl-stiffness-and-time-integration.md) ·
[Subsidence & poroelasticity](../04-interaction/13-subsidence-and-poroelasticity.md) ·
[Reaction kinetics & sinks](../04-interaction/01-reaction-kinetics-and-sinks.md) ·
[Structure-preserving discretisations](13-structure-preserving-discretizations.md)
