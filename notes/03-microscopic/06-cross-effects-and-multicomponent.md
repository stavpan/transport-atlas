---
title: Cross-effects & multicomponent diffusion
blurb: Soret, Dufour, thermophoresis, and Maxwell–Stefan — what happens when gradients of different quantities drive each other's fluxes.
depth: 4
tags: [Soret, Dufour, thermophoresis, Maxwell-Stefan, uphill diffusion]
---

# Cross-effects & multicomponent diffusion

> **One-line picture.** Forces do not act in isolation: a temperature gradient can drag mass, a
> concentration gradient can drag heat, and in a mixture of three species one component can move
> *up* its own gradient.
>
> **Prerequisites.** [diffusion](01-diffusion.md),
> [constitutive relations](../01-foundations/03-constitutive-relations.md) · **Leads to.**
> [charged transport](07-charged-and-electrochemical-transport.md),
> [linear response](../01-foundations/09-linear-response-and-memory.md)

## L1 · Forces and fluxes come in families

In a system with several gradients, the flux of each conserved quantity depends on *all* the
forces. The thermodynamic skeleton is $\mathbf{J}_i=\sum_j L_{ij}\mathbf{X}_j$ with $L$ symmetric
(Onsager) and positive semidefinite (second law). Two consequences follow immediately:

* **Cross-effects appear** wherever a force of one type drives a flux of another.
* **They come in reciprocal pairs** — you cannot have one without the other.

The practical reason to care is that *measured* transport coefficients are not the intrinsic ones:
a "diffusion coefficient" measured in a temperature gradient is a mixture of $D$ and the Soret
coefficient, and a "thermal conductivity" measured in a concentration gradient includes Dufour.

## L2 · The named effects

| Effect | Force → flux | Where it matters |
|---|---|---|
| Soret (thermodiffusion) | $\nabla T\to$ mass flux | isotope separation, mantle differentiation, polymer characterisation |
| Dufour | $\nabla c\to$ heat flux | combustion, mixtures with large $\mathrm{Le}$ |
| Thermophoresis | $\nabla T\to$ particle drift | soot deposition, aerosol sampling |
| Diffusiophoresis | $\nabla c\to$ particle drift | drying films, chromatography |
| Seebeck / Peltier | $\nabla T\leftrightarrow$ current | thermoelectrics |
| Maxwell–Stefan | species friction | distillation, membranes, electrolyte transport |
| Osmosis | $\nabla c\to$ solvent flow | membranes, cells, desalination |

**Maxwell–Stefan** is the honest multicomponent formulation: rather than assigning a diffusion
coefficient to each species independently, it balances the driving force on each species against
*friction with every other species*,

$$\nabla\mu_i=-\sum_{j\neq i}\frac{x_j}{\mathcal{D}_{ij}}(\mathbf{v}_i-\mathbf{v}_j),$$

The concentration-based "Fickian" diffusivity matrix you fit afterwards is a derived object with
built-in non-ideality (activity coefficients) and can have negative eigenvalues — producing
**uphill diffusion**, where a component moves from low to high concentration. This is not a
paradox: Fick's law is a special case, not a law of nature.

## L3 · What the mathematics guarantees

* **Onsager symmetry pins the cross-coefficients together.** Measure Soret accurately and you know
  the Dufour coefficient; wrong-sign pairs violate the second law.
* **Curie's principle limits what can appear.** In isotropic media, linear coupling of different
  tensorial order is forbidden — which is why Soret produces *no* cross-effect with viscous stress,
  but interfaces and anisotropy break the restriction and produce new effects.
* **Stability can be broken by cross-effects.** Double-diffusive instability (warm salty water) and
  Soret-driven convection arise even when each individual gradient is diffusively stable: the
  *difference* in diffusivities is the instability mechanism.
* **Negative eigenvalues are physical.** Uphill diffusion appears in non-ideal mixtures and
  electrolytes; codes that assume a positive-definite scalar diffusivity silently misbehave here.

## L4 · Numerics

* **Use Maxwell–Stefan when species counts change** (reactive, multicomponent or non-ideal
  systems); use Fick when the mixture is dilute and near-ideal.
* **Consistency conditions.** In a closed system, the diffusive fluxes must sum to zero
  ($\sum\mathbf{J}_i=0$) and mass fractions must stay bounded — small inconsistencies produce slow
  drift and negative concentrations.
* **Watch stiffness.** Cross-effects couple the energy and species equations, forming stiff systems
  that need implicit treatment ([time integration](../07-numerics/02-cfl-stiffness-and-time-integration.md)).
* **Benchmarks**: the Soret-driven Benard problem, ternary diffusion in ideal and non-ideal
  mixtures, and standard electrolyte test problems
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Cross-effects in ion channels and nanofluidics; thermodiffusion in crowded
  biological media; coupled transport in battery and fuel-cell electrodes.

## Checks

1. Can a temperature gradient drive mass without any concentration gradient? *(Yes — Soret; and its
   reciprocal, Dufour, drives heat with a concentration gradient.)*
2. Is uphill diffusion a violation of the second law? *(No: the relevant force is the chemical
   potential gradient, which still points downhill.)*
3. Why do you need a matrix, not a number, for a ternary mixture? *(Each species' flux depends on
   every other species' force.)*

## See also

[Charged & electrochemical transport](07-charged-and-electrochemical-transport.md) ·
[Constitutive relations](../01-foundations/03-constitutive-relations.md) ·
[Linear response & memory](../01-foundations/09-linear-response-and-memory.md) ·
[Double diffusion in geoscience](../08-bridges/04-geoscience-and-climate.md)
