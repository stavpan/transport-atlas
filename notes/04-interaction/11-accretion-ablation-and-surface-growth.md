---
title: Accretion, ablation & surface growth
blurb: Domains that grow or shrink — additive manufacturing, corrosion, fouling and residual stress, where the mesh must move with the material.
depth: 4
tags: [accretion, ablation, moving mesh, residual stress, corrosion]
---

# Accretion, ablation & surface growth

> **One-line picture.** Sometimes the interesting boundary is not where the material is, but where it
> *stops being*. Accretion adds mass to a surface; ablation removes it; both make the domain an
> unknown.
>
> **Prerequisites.** [phase change & Stefan](09-phase-change-and-stefan.md) ·
> **Leads to.** [free boundaries & phase field](../06-beyond/09-free-boundaries-level-sets-and-phase-field.md),
> [engineering devices](../08-bridges/06-engineering-devices.md)

## L1 · Growth versus removal

Two identical mathematical situations with opposite signs:

* **Accretion** — mass arrives at a surface and becomes part of the solid: crystal growth,
  electrodeposition, additive manufacturing, biofilm growth, snow accumulation, arterial plaque.
* **Ablation** — mass leaves: sublimation of a heat shield, laser machining, corrosion, dissolution,
  wear, glacier melt.

Both are described by a surface velocity along the normal,

$$\dot{\mathbf{x}}=v_n\mathbf{n},\qquad v_n\ \text{from a flux balance or a rate law},$$

so the *geometry* is an unknown and the domain changes shape as the solution proceeds. The essential
difference from melting/solidification is that new material arrives with its own **stress-free
reference configuration**, which is why growth generically leaves residual stress behind.

## L2 · The mechanisms and their rate laws

| Process | Rate law | Transport-limited by |
|---|---|---|
| electrodeposition | Butler–Volmer + mass transfer | ion transport in the electrolyte ([Nernst–Planck](06-chemotaxis-and-keller-segel.md)) |
| chemical vapour deposition | surface reaction + gas diffusion | boundary-layer mass transfer |
| corrosion | Tafel kinetics + ohmic drop | oxygen supply, passivation films |
| additive manufacturing | melt-pool solidification | heat conduction, Marangoni flow |
| biofilm growth | nutrient uptake × yield | substrate diffusion into the film |
| wear / erosion | threshold impact energy | local impact rate |
| scale/fouling | supersaturation kinetics | heat/mass transfer to the wall |

Common structure: **a surface reaction coupled to transport through a boundary layer**. This is why
these problems look like [conduction](../03-microscopic/03-conduction.md) with a Robin boundary whose coefficient
evolves, and why the same dimensionless groups ($\mathrm{Sh}$, $\mathrm{Da}$) reappear.

## L3 · What the mathematics guarantees

* **The moving-domain formulation is exact but awkward.** In the reference (material) frame the
  balance laws pick up the surface velocity; in the spatial frame the interface is a
  [free boundary](../06-beyond/09-free-boundaries-level-sets-and-phase-field.md). Choose by asking
  whether the *solid* or the *space* is the natural coordinate.
* **Morphological instability is generic.** Diffusion-limited growth is unstable to protrusions
  (Mullins–Sekerka, dendritic growth, electrodeposition dendrites, corrosion pits): flat surfaces
  grow bumps, bumps grow faster, and shapes like frost, dendrites and pits result. Stability requires
  surface energy, kinetics or transport obstacles.
* **Residual stress is a memory effect.** Material deposited at different times has different thermal
  or chemical histories, so the final body contains an internal state that depends on the *whole*
  deposition path — a reminder that transport problems can be path-dependent without being
  dissipative ([memory & viscoelasticity](../06-beyond/04-memory-viscoelastic-and-hereditary.md)).
* **Interface evolution is Hamilton–Jacobi-like.** Purely geometric front motion (uniform normal
  velocity plus curvature) reduces to an
  [eikonal/level-set equation](../06-beyond/02-hamilton-jacobi-and-viscosity-solutions.md) whose
  solutions may develop corners — needing viscosity solutions or level-set discretisations.

## L4 · Numerics

* **Arbitrary Lagrangian–Eulerian (ALE)** meshes move with the surface; remeshing is needed when
  distortion becomes extreme. Quality metrics and conservative remapping interpolate the solution
  between meshes.
* **Level-set / phase-field methods** avoid remeshing and handle topology changes (droplet mergers,
  pore closure) but require careful reinitialisation and ghost-fluid treatments.
* **Immersed-boundary / cut-cell** methods keep a fixed grid and modify stencils near the interface —
  cheap, but notorious for small-cell stability problems.
* **Benchmarks**: one-dimensional Stefan-type growth, dendritic tip velocity, galvanostatic
  deposition shape evolution, and additive-manufacturing melt-pool dimensions
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Coupled electro-chemo-mechanics in solid-state batteries (dendrites, fracture);
  growth of living tissue with residual stress; machine-learned interface kinetics.

## Checks

1. Why does growth generically leave residual stress, unlike melting? *(New material arrives in its own
   stress-free state; the mismatch must be stored elastically.)*
2. Why are protrusions unstable in diffusion-limited growth? *(They reach fresh reactants first — the
   Mullins–Sekerka mechanism.)*
3. Why does ALE need remeshing? *(The mesh distorts with the boundary; element quality degrades until
   the solve fails.)*

## See also

[Phase change & Stefan](09-phase-change-and-stefan.md) ·
[Moving meshes & parallel decomposition](../07-numerics/08-mesh-adaptivity-moving-domains-and-parallel.md) ·
[Hamilton–Jacobi & viscosity solutions](../06-beyond/02-hamilton-jacobi-and-viscosity-solutions.md) ·
[Engineering devices](../08-bridges/06-engineering-devices.md)
