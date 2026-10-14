---
title: Free boundaries, level sets & phase fields
blurb: Interfaces that move, merge and split — the three families of methods, and why the interface is usually the whole problem.
depth: 3
tags: [free boundary, level set, phase field, Cahn-Hilliard, Mullins-Sekerka]
---

# Free boundaries, level sets & phase fields

> **One-line picture.** When the location of a boundary is an *output* rather than an input, you must
> either track it, or embed it in a function that merges and splits without complaining.
>
> **Prerequisites.** [phase change & Stefan](../04-interaction/09-phase-change-and-stefan.md),
> [Hamilton–Jacobi & viscosity solutions](02-hamilton-jacobi-and-viscosity-solutions.md) · **Leads to.**
> [accretion & surface growth](../04-interaction/11-accretion-ablation-and-surface-growth.md)

## L1 · The problem and the three philosophies

Free boundaries appear throughout this atlas: melting fronts, corrosion surfaces, Hele-Shaw fingers,
crack tips, tumour boundaries, dendrites, dewetting films, and the support edge of nonlinear diffusion.

| Approach | Interface is | Strengths | Weaknesses |
|---|---|---|---|
| front tracking | explicit markers moved with physics | sharpest accuracy, exact jumps | fails on topology change; remeshing |
| level set | zero contour of $\phi(\mathbf x,t)$ | merging/splitting free; natural for HJ motion | reinitialisation, volume loss, thin-interface care |
| phase field | diffuse, width $\varepsilon$ | variational, energy-based, fully coupled | width tied to grid; curvature errors at low resolution |

## L2 · The equations

* **Level set:** $\partial_t\phi+V|\nabla\phi|=0$ — a Hamilton–Jacobi equation; use upwind/ENO schemes
  and reinitialise by solving $|\nabla\phi|=1$ in a narrow band. Curvature flow $V=-\kappa$ is the
  paradigm case.
* **Allen–Cahn (non-conserved):** $\partial_t\phi=-M(-\kappa^2\nabla^2\phi+f'(\phi))$, an $L^2$ gradient
  flow of a double-well free energy.
* **Cahn–Hilliard (conserved):** $\partial_tc=\nabla\!\cdot\!(M\nabla\mu)$,
  $\mu=f'(c)-\kappa^2\nabla^2c$ — an $H^{-1}$ gradient flow, giving spinodal decomposition and
  coarsening.
* **Mullins–Sekerka:** the sharp-interface limit. Diffusion drives long-wavelength growth, surface
  energy stabilises short wavelengths, and the balance selects the pattern scale — the reason dendrite
  spacing is what it is.

## L3 · What the mathematics guarantees

* **Variational structure**: Allen–Cahn and Cahn–Hilliard are gradient flows, so free energy decreases
  monotonically — the property a numerical scheme should preserve
  ([entropy & variational structure](../01-foundations/07-entropy-and-variational-structure.md)).
* **Γ-convergence**: as $\varepsilon\to0$ the diffuse energy converges to a perimeter functional and
  minimisers converge to minimisers. Phase fields are therefore *models*, not just numerical tricks.
* **Maximum principles differ**: Allen–Cahn has one; Cahn–Hilliard (fourth order) does not, so discrete
  solutions can leave $[-1,1]$ unless positivity-preserving schemes are used.
* **Surface energy is what makes the problem well-posed**: with zero surface tension the Mullins–Sekerka
  instability is ill-posed at short wavelengths.
* **Topology is not preserved** by level sets and phase fields — a feature (coalescence, branching) and
  a hazard if you expected one connected interface.

## L4 · Numerics

* **Level sets**: high-order upwinding (WENO), narrow-band reinitialisation, sub-cell interface
  reconstruction for accurate fluxes and volume.
* **Phase fields**: resolve $\varepsilon$ with 4–8 cells; use convex splitting or energy-stable schemes,
  or coarsening statistics come out wrong.
* **Volume conservation** is the standard failure mode of level sets and naive phase fields.
* **Benchmarks**: Zalesak's disk, bubble merger and Rayleigh–Taylor, Cahn–Hilliard coarsening
  exponents, diffuse-interface Stefan
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Coupled flow–phase field–elasticity for fracture; peridynamic damage; learned interface
  kinetics; large-scale multiphase flow with phase change.

## Checks

1. Which method handles a merging droplet with no special code? *(Level set or phase field.)*
2. What sets the dendrite spacing? *(Balance of diffusive growth and surface-energy stabilisation.)*
3. Why tie the phase-field width to the grid? *(Otherwise the effective surface energy and mobility are
   resolution-dependent.)*

## See also

[Phase change & Stefan](../04-interaction/09-phase-change-and-stefan.md) ·
[Hamilton–Jacobi & viscosity solutions](02-hamilton-jacobi-and-viscosity-solutions.md) ·
[Nonlinear diffusion & porous medium](06-nonlinear-diffusion-and-porous-medium.md) ·
[Structure-preserving discretisations](../07-numerics/13-structure-preserving-discretizations.md)
