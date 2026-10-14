---
title: Mesh, adaptivity & parallel decomposition
blurb: Where to put the grid points, how to move them, and how to split the work across machines without losing conservation.
depth: 3
tags: [AMR, adaptivity, moving mesh, ALE, domain decomposition, MPI, halo]
---

# Mesh, adaptivity & parallel decomposition

> **One-line picture.** Transport lives in thin regions: fronts, boundary layers, interfaces, plumes.
> Resolution must follow the action — and the work must be split so that the splits look seamless.
>
> **Prerequisites.** [discretisation & stability](01-discretization-consistency-stability-convergence.md) ·
> **Leads to.** [particle & Monte Carlo methods](09-particle-and-monte-carlo-methods.md),
> [structure-preserving discretisations](13-structure-preserving-discretizations.md)

## L1 · Where the difficulty goes

* **Boundary layers** need wall-normal clustering ($10^{2}$–$10^{4}$ grid stretch), not uniform refinement.
* **Shock and reaction fronts** are $O(1)$–$O(10)$ cells thick regardless of domain size: adaptive
  refinement (AMR) or moving meshes are the only affordable answers.
* **Interfaces** (phase change, free surfaces, faults) need either body-fitted meshes (accurate, hard to
  remesh) or embedded methods (easy, with cut-cell stability problems).
* **Multiphase plume fronts** in groundwater can require refinement where nothing is happening yet,
  because the plume will arrive later: error estimators must be predictive, not reactive.

## L2 · The techniques

| Technique | Idea | Prerequisite |
|---|---|---|
| $h$-refinement (AMR) | split cells flagged by an error indicator | hierarchical mesh (quadtree/octree) + hanging-node handling |
| $p$-refinement | raise the polynomial degree locally | high-order element library |
| $r$-adaptivity / moving mesh | move nodes toward the action | mesh motion PDE + remapping |
| ALE | mesh moves with the interface, bulk stays Eulerian | conservative remapping between meshes |
| immersed boundary | fixed grid, forces/blocks applied near the interface | stable cut-cell or regularisation |
| overset / Chimera | multiple overlapping grids | interpolation in the overlap region |

**Error indicators** are the heart of adaptivity: gradient- or curvature-based (cheap), residual-based
(justified for FEM), goal-oriented/adjoint-based (targets a specific output quantity — the most
powerful and most expensive). For transport, the interesting outputs (breakthrough time, peak
concentration) are *not* well targeted by gradient indicators, so adjoint methods pay off.

## L3 · What the mathematics guarantees

* **Convergence and optimality**: adaptive FEM converges at the optimal rate for the true error when the
  indicator is equivalent to the error (reliability and efficiency); this theory exists for elliptic
  problems and is partly open for transport-dominated cases.
* **Conservation across refinement interfaces** requires flux matching and careful hanging-node
  treatment, or mass leaks. Refinement conservatively and test it by integrating a tracer.
* **Remapping must be conservative and monotone** (donor-cell, or high-order with limiters); otherwise
  moving meshes destroy positivity and mass — a classic ALE failure.
* **Parallel partition quality** determines cost: load balance, communication volume and the halo depth
  (which must match the stencil width) are the knobs.

## L4 · Practicalities

* **Domain decomposition (MPI)** with halo/ghost cells: exchange before each stencil evaluation; use
  non-blocking sends and combine messages to reduce latency. For a 5-point stencil, one layer of ghosts
  suffices; a WENO5 stencil needs three.
* **Partition once, communicate often**: use graph partitioners (METIS/ParMETIS) and keep partitions
  fixed unless load changes.
* **Time-step synchronisation** is the hidden cost of local refinement in explicit schemes: refined
  regions need smaller $\Delta t$ (sub-cycling) or the whole simulation slows down.
* **Always test parallel correctness**: identical results on 1, 2 and 8 ranks (bitwise if possible),
  conservation across partitions, and weak/strong scaling curves.
* **Benchmarks**: the SPE10 field for AMG/AMR, lid-driven cavity with AMR, and shock diffraction
  ([V&V](12-verification-validation-and-benchmarks.md)).

## Checks

1. What must be exchanged at partition boundaries, and how wide? *(Ghost/halo values, as wide as the
   stencil requires.)*
2. Why does local refinement slow explicit simulations? *(The time step follows the smallest cell,
   unless sub-cycling is implemented.)*

## See also

[Linear solvers & preconditioning](06-linear-solvers-and-preconditioning.md) ·
[Accretion & surface growth](../04-interaction/11-accretion-ablation-and-surface-growth.md) ·
[Structure-preserving discretisations](13-structure-preserving-discretizations.md)
