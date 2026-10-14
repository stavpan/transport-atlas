---
title: Constitutive relations
blurb: The closure step — Fick, Fourier, Newton, Darcy, Ohm — and the entropy constraint that decides which of them may exist.
depth: 2
tags: [closure, Fick, Fourier, Onsager, entropy production]
---

# Constitutive relations (closure)

> **One-line picture.** A balance law says what is conserved but nothing about what the
> substance does. A constitutive law is the empirical bet that closes the gap — and every such
> bet is a bet about a range of validity.
>
> **Prerequisites.** [balance laws & flux](01-balance-laws-and-flux.md) · **Leads to.**
> [diffusion](../03-microscopic/01-diffusion.md), [conduction](../03-microscopic/03-conduction.md),
> [Darcy flow](../02-bulk/08-porous-media-and-darcy.md)

## L1 · What it is, in words

"Nothing is lost" is true but empty: it does not say whether heat crawls or races through
copper. To use the balance law you must add a statement of what materials do when pushed out
of equilibrium. People mill flour down a chute, crowd through a doorway, queue at a checkout:
the *rule of flow* is a property of the material and the situation, not of arithmetic.

Two features are striking: the rules are almost always *flow proportional to a gradient*, and
the constant of proportionality is the only thing distinguishing copper from air.

## L2 · The catalog

$$\text{flux}=-\,(\text{transport property})\times\nabla(\text{potential})$$

| Domain | Law | Coefficient | Typical value |
|---|---|---|---|
| mass: $\mathbf{J}=-D\nabla c$ | Fick (1855) | $D$ | $10^{-9}$ m²/s in water |
| heat: $\mathbf{q}=-k\nabla T$ | Fourier (1822) | $k$; $\alpha=k/\rho c_p$ | 0.6 W/m·K water, 400 copper |
| momentum: $\boldsymbol\tau=\mu(\nabla\mathbf{u}+\nabla\mathbf{u}^{\!\top})$ | Newton/Stokes | $\mu$, $\nu$ | $10^{-3}$ Pa·s water |
| porous: $\mathbf{q}=-(K/\mu)\nabla p$ | Darcy (1856) | permeability $K$ | $10^{-12}$ m² sand |
| charge: $\mathbf{i}=-\sigma\nabla\phi$ | Ohm (1827) | $\sigma$ | $6\times10^7$ S/m copper |
| ions: Nernst–Planck + Soret | — | $D$, $s$ | — |
| radiation (thick limit) | Rosseland | $\kappa$ | — |
| elasticity: $\boldsymbol\sigma=\mathbb{C}:\boldsymbol\varepsilon$ | Hooke | $\mathbb{C}$ | — |

Anisotropy turns scalars into tensors: laminated rock transports far faster along bedding, so
$K$ becomes a symmetric positive-definite matrix, and groundwater dispersion becomes a tensor
aligned with the flow — [shear dispersion](../02-bulk/06-shear-dispersion-taylor-aris.md).

## L3 · What the mathematics guarantees (and forbids)

**Entropy production fixes the signs.** Write fluxes and forces as vectors, $\mathbf{J}=L\mathbf{X}$.
The second law demands $\dot S=\mathbf{X}^{\!\top}L\mathbf{X}\ge0$ for every admissible
$\mathbf{X}$, so $L$ must be symmetric positive semidefinite. This one inequality is why
diffusivity, conductivity and viscosity are positive and why flux–force matrices are symmetric.

**Onsager reciprocity (1931).** $L_{ij}=L_{ji}$: cross-effects are forced symmetries, not
optional extras. Soret (a temperature gradient drives mass) pairs with Dufour (a concentration
gradient drives heat); Seebeck pairs with Peltier —
[cross-effects](../03-microscopic/06-cross-effects-and-multicomponent.md).

**Curie's principle.** In an isotropic medium, a linear law cannot couple a scalar force to a
vector flux. Interfaces and anisotropy break this — which is why surface-driven phenomena
(Marangoni, slip, thermophoresis) look exotic.

**Where linearity dies.** Newtonian viscosity above $\mathrm{Wi}\sim1$; Fick when
$\mathrm{Kn}$ is not small; Fourier in ballistic phonon transport; Darcy at high $\mathrm{Re}$
(Forchheimer) or in tight pores (Klinkenberg). Then go kinetic
([Boltzmann](../05-kinetic/01-boltzmann-equation.md),
[Knudsen](../03-microscopic/05-knudsen-and-rarefied-transport.md)) or nonlocal
([memory & viscoelasticity](../06-beyond/04-memory-viscoelastic-and-hereditary.md)).

## L4 · Numerics, limits, frontiers

* **Eddy diffusivity is not a law.** Turbulent transport is *closed*, not derived; the
  gradient-diffusion hypothesis fails in buoyant plumes (counter-gradient fluxes). All of
  $k$–$\varepsilon$, LES subgrid models and learned closures live here —
  [turbulence](../02-bulk/05-turbulence-and-eddy-diffusivity.md).
* **Coefficients are the hard part.** Much practical work is the inverse problem: infer
  $D(\mathbf{x})$ from measured concentrations —
  [inverse problems](../07-numerics/10-inverse-problems-and-data-assimilation.md).
* **Homogenisation** replaces a heterogeneous medium by an effective tensor and states exactly
  when that is legal — [upscaling](../06-beyond/08-homogenization-and-upscaling.md).
* **Frontiers.** Closures that provably respect the second law; nonlocal constitutive models
  for dense suspensions and rare gases; constitutive learning from force fields.

## Words that collide

> **Diffusivity vs conductivity vs permeability:** a diffusivity is property/storage
> ($D=k/\rho c_p$), permeability only becomes a fluid property after dividing by $\mu$.
> **Constitutive law vs equation of state:** flux versus force, or state versus state.

## Checks

1. Why must $D>0$? *(Otherwise entropy decreases and the maximum principle fails.)*
2. When must Fick's law fail? *($\mathrm{Kn}\gtrsim0.1$; ballistic phonons; polymers with memory.)*
3. Which coupling lets a temperature gradient drive a mass flux, and what is its Onsager partner?
   *(Soret; Dufour.)*

## See also

[Diffusion](../03-microscopic/01-diffusion.md) ·
[Conduction](../03-microscopic/03-conduction.md) ·
[Entropy & variational structure](07-entropy-and-variational-structure.md) ·
[Dimensionless numbers](05-dimensionless-numbers.md) ·
[Equation catalogue](../10-appendix/03-operator-and-equation-catalog.md)
