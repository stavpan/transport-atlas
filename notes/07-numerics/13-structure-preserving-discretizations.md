---
title: Structure-preserving discretisations
blurb: Schemes that respect the physics by construction — conservation, positivity, entropy stability, and discrete analogues of the theorems.
depth: 4
tags: [conservation, positivity, entropy stability, mimetic, geometric integrators]
---

# Structure-preserving discretisations

> **One-line picture.** Instead of hoping a scheme behaves, engineer it so the discrete equations satisfy
> the *theorems*: conservation, a maximum principle, an entropy inequality.
>
> **Prerequisites.** [discretisation & stability](01-discretization-consistency-stability-convergence.md),
> [entropy & variational structure](../01-foundations/07-entropy-and-variational-structure.md) ·
> **Leads to.** [limiters, TVD & WENO](04-limiters-tvd-and-weno.md),
> [linear solvers](06-linear-solvers-and-preconditioning.md)

## L1 · What "structure" means here

A conservative PDE has invariants and inequalities. Structure-preserving (or *mimetic*, *compatible*,
*geometric*) discretisations reproduce them exactly on the discrete level:

| Structure | Discrete requirement | Consequence |
|---|---|---|
| conservation | flux form with one flux per face | telescoping sums: exact mass balance |
| duality | discrete divergence $=$ negative adjoint of gradient | symmetric matrices, correct null space |
| maximum principle | monotone stencil (M-matrix) | positivity, boundedness |
| entropy inequality | discrete entropy flux/ dissipation | nonlinear stability |
| energy/kinetic-energy conservation | skew-symmetric convection | honest turbulence statistics |
| symplecticity / time reversal | symplectic or reversible integrators | long-time fidelity in Hamiltonian limits |
| curl/div identities | discrete de Rham complex | $\nabla\!\cdot\!\nabla\times=0$ exactly (MHD, EM) |
| well-balancedness | hydrostatic states preserved | lakes at rest, stratified flow, gravity balances |

## L2 · How it is achieved

* **Finite volume** gives conservation automatically; add limiters for positivity
  ([limiters](04-limiters-tvd-and-weno.md)), and well-balanced source discretisations for gravity.
* **Mixed/hybrid FEM** uses compatible element pairs so that the discrete gradient, divergence and curl
  are adjoints — the reason staggered (MAC) grids work so well for incompressible flow.
* **Summation-by-parts (SBP) + SAT** operators provide discrete integration by parts with weak boundary
  conditions, giving provable stability; add entropy-conservative fluxes for nonlinear stability.
* **Convex splitting and JKO-type schemes** make gradient flows energy-monotone
  ([optimal transport](../06-beyond/10-optimal-transport-and-gradient-flows.md)).
* **Symplectic integrators** preserve the Hamiltonian structure of the reversible part, which is why
  long-time molecular dynamics does not drift.

## L3 · What the mathematics guarantees

* **Discrete conservation is exact**, not asymptotic: mass errors are zero to round-off, which is the only
  standard acceptable for climate, reservoir and reactive transport.
* **Entropy stability implies nonlinear stability**: with a discrete entropy inequality you get a bound
  independent of the grid, without any linearisation.
* **Positivity and bounds come from monotonicity**, which is a nonlinear property that linear stability
  analysis cannot see.
* **Compatibility prevents spurious modes**: exactly satisfying discrete vector identities removes the
  checkerboard pressures and divergence drifts of naive discretisations.
* **The cost is design complexity**: structure-preserving schemes are harder to implement, may limit
  attainable order, and often need special boundary treatments.

## L4 · Practicalities

* **Start from the invariants you care about** and choose the scheme to preserve them: mass first,
  then positivity, then entropy.
* **Test the structure directly**: run conservation and bound checks as unit tests, not as
  post-hoc analysis.
* **Combine structures**: SBP + limiters + well-balanced sources is the modern recipe for geophysical
  transport.
* **Beware of mixed-order errors:** preserving a structure at second order while using a fourth-order
  interior flux requires matched interface treatments.
* **Benchmarks**: hydrostatic balance tests, conservation audits over long integrations, posivity tests
  for reactive transport, and entropy production checks in turbulent flows
  ([V&V](12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Entropy-stable schemes for MHD and relativistic flows; compatible discretisations on
  unstructured/polyhedral meshes; structure-preserving learned discretisations.

## Checks

1. Why does a flux-form finite-volume scheme conserve exactly? *(Summed face fluxes telescope; interior
   fluxes cancel while boundary fluxes match the stored mass change.)*
2. What does the discrete de Rham complex prevent? *(Spurious modes and divergence/curl drift in
   Maxwell/MHD and incompressible flow.)*

## See also

[Linear solvers & preconditioning](06-linear-solvers-and-preconditioning.md) ·
[Limiters, TVD & WENO](04-limiters-tvd-and-weno.md) ·
[Entropy & variational structure](../01-foundations/07-entropy-and-variational-structure.md) ·
[Optimal transport & gradient flows](../06-beyond/10-optimal-transport-and-gradient-flows.md)
