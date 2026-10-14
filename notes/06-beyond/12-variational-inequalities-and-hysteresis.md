---
title: Variational inequalities & hysteresis
blurb: Transport with a switch — complementarity, obstacle problems, contact, and materials whose response depends on which way you came.
depth: 4
tags: [variational inequality, obstacle problem, hysteresis, contact, Coulomb friction]
---

# Variational inequalities & hysteresis

> **One-line picture.** Sometimes the physics is an inequality, not an equation: flow stops below a
> threshold, contact only pushes, and a path once taken is partly remembered.
>
> **Prerequisites.** [entropy & variational structure](../01-foundations/07-entropy-and-variational-structure.md),
> [non-Newtonian rheology](../02-bulk/09-non-newtonian-rheology.md) · **Leads to.**
> [microcontinuum continua](11-microcontinuum-and-generalized-continua.md),
> [engineering devices](../08-bridges/06-engineering-devices.md)

## L1 · The problem class

Many transport problems are *inequalities*: you minimise energy subject to a constraint, and the
constraint is active in some unknown region that must be found as part of the solution.

* **Obstacle problem**: a membrane pressed by a rigid body; the contact region is unknown.
* **Contact and friction**: Coulomb friction means the tangential stress is bounded — slip occurs only
  when the bound is reached (and stops when it is not). The set of sliding points is an output.
* **Bingham/yield-stress flow**: below $\tau_y$ the material does not flow (unyielded plug).
* **Coating, infiltration, saturation**: flow switches on/off as drying or wetting fronts pass.
* **Phase transitions with hysteresis**: a "switching" state that depends on the loading direction
  (magnetic, ferroelectric, shape-memory, adsorption hysteresis).

All are of the form: minimise energy, subject to an inequality constraint, with an unknown active set.
The mathematical machinery is **complementarity**: for each point, either the constraint is slack and
the equation holds, or the constraint is active and the inequality holds — never both violations.

## L2 · What the mathematics provides

| Structure | Continuous form | Discrete analogue |
|---|---|---|
| obstacle | $u\ge\psi$, $-\Delta u-f\ge0$, $(u-\psi)(-\Delta u-f)=0$ | linear complementarity problem |
| contact | normal gap $\ge0$, pressure $\ge0$, product $=0$ | active-set or semismooth Newton |
| Coulomb friction | $\|\mathbf t\|\le\mu p_n$, slip only if equality | return-mapping, proximal splitting |
| yield stress | $\|\boldsymbol\tau\|\le\tau_y$ or rate $=0$ | augmented Lagrangian |
| hysteresis | rate-independent memory operator | Preisach/play operators, sweeping processes |

Hysteresis deserves a separate sentence: a **rate-independent** memory means the response depends on the
*sequence and extrema* of the driving, not on the speed. Quantitatively this needs operators
(Preisach, Prandtl–Ishlinskii, play/hysterons) rather than differential equations in time — a genuinely
different mathematical structure from everything else in this atlas.

## L3 · What the mathematics guarantees

* **Existence via convexity.** Variational inequalities inherit existence and uniqueness from convex
  minimisation over a closed convex set. Non-convex versions (damage, plasticity with softening) may
  lose uniqueness — which is physical (localisation), not a defect of the theory.
* **Regularity is limited by the free set.** Solutions are typically only Lipschitz/Hölder across the
  boundary of the active set: the active-set boundary behaves like a free boundary
  ([free boundaries](09-free-boundaries-level-sets-and-phase-field.md)).
* **Monotone operators and damping.** Many quasi-static problems with hysteresis are *dissipative*, and
  this gives stability in the sense of maximal monotone operators (sweeping processes).
* **Hysteresis breaks the state-function assumption.** Constitutive laws must carry internal variables
  whose evolution is constrained by inequalities, so the material state is not a function of the current
  strain (or concentration) alone.

## L4 · Numerics

* **Semismooth Newton** (with active-set detection) and **primal–dual active-set methods** are the
  standard solvers; they converge superlinearly when implemented carefully
  ([nonlinear solvers](../07-numerics/07-nonlinear-solvers-and-continuation.md)).
* **Regularisation** (bi-viscosity, penalty, smoothed friction) makes problems differentiable but biases
  the answer; report the regularisation parameter and check sensitivity.
* **Augmented Lagrangians / proximal splitting** (ADMM) handle contact and yield-stress flow robustly and
  keep the constraint exactly satisfied.
* **Benchmark cases**: the obstacle problem with a known obstacle, Bingham flow in a channel (plug
  width), and classical friction contact tests
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Coupled contact with transport (fractured reservoirs, drying/wetting hysteresis in
  soils); Preisach-type models calibrated from data; sweeping-process theory for rate-independent
  systems; non-smooth optimisation at scale.

## Checks

1. What does complementarity mean concretely for a contact problem? *(Either the surfaces are separated
   with zero pressure, or they touch with positive pressure — never negative gaps or pressures.)*
2. Why is hysteresis not a differential equation in time? *(It is rate-independent: the response depends
   on the loading *path*, not on its speed.)*
3. Why must yield-stress solvers find an active set? *(The unyielded region is unknown and must be
   determined as part of the solution.)*

## See also

[Non-Newtonian rheology](../02-bulk/09-non-newtonian-rheology.md) ·
[Free boundaries, level sets & phase field](09-free-boundaries-level-sets-and-phase-field.md) ·
[Nonlinear solvers & continuation](../07-numerics/07-nonlinear-solvers-and-continuation.md) ·
[Engineering devices](../08-bridges/06-engineering-devices.md)
