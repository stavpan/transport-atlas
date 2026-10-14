---
title: Transport in geoscience & climate
blurb: Mantle convection, groundwater, permafrost, sea ice and the atmosphere — transport on Earth's scales, where the dimensionless numbers are enormous.
depth: 2
tags: [geoscience, climate, mantle, groundwater, sea ice, convection]
---

# Transport in geoscience & climate

> **One-line picture.** Earth is a set of coupled transport problems spanning 18 orders of magnitude in
> length, with $\mathrm{Ra}$, $\mathrm{Re}$ and $\mathrm{Pe}$ far beyond anything a laboratory can reach.
>
> **Prerequisites.** [convection & buoyancy](../02-bulk/02-convection-and-buoyancy.md),
> [porous media & Darcy](../02-bulk/08-porous-media-and-darcy.md)

## L1 · Five transport systems that make a planet

| System | Dominant transport | Characteristic numbers |
|---|---|---|
| mantle convection | solid-state creep ($\mu_{\rm eff}\sim10^{21}$ Pa·s) | $\mathrm{Ra}\sim10^{7}$–$10^{9}$, $\mathrm{Pr}\to\infty$ |
| outer core | magnetohydrodynamic convection | $\mathrm{Rm}\sim10^{3}$ (dynamo action) |
| groundwater & aquifers | Darcy flow + dispersion + sorption | $\mathrm{Pe}>10^{4}$, $\mathrm{Da}$ from $10^{-3}$ to $10^{2}$ |
| atmosphere & ocean | advection, radiation, phase change | $\mathrm{Re}\sim10^{8}$–$10^{9}$, $\mathrm{Ra}$ huge, $\mathrm{Le}\neq1$ |
| cryosphere (ice sheets, sea ice, permafrost) | nonlinear viscous flow + phase change | Stefan numbers, Glen's flow law $n\approx3$ |

## L2 · What transport theory contributes

* **Mantle convection is Rayleigh–Bénard at infinite Prandtl number** with temperature-dependent
  viscosity: an instability whose pattern (plumes versus sheets) is a *transport* question, and whose
  time scale (hundreds of millions of years) is set by the diffusion of heat through the lithosphere.
* **Groundwater**: the same Darcy/ADE machinery as engineering, with the added twist that heterogeneity
  is multiscale and often gives non-Fickian (heavy-tailed) breakthrough. Upscaling of random fields is a
  core geoscience activity ([homogenisation](../06-beyond/08-homogenization-and-upscaling.md),
  [stochastic PDEs](../06-beyond/07-stochastic-pdes-and-random-media.md)).
* **Climate**: radiative transfer (Planck, absorption bands, scattering) plus convection sets the
  radiative-convective equilibrium profile; the atmosphere is a heat engine transporting energy from the
  tropics poleward by eddies, and the ocean transports heat by a slow thermohaline circulation. Both are
  advection–diffusion problems with strongly scale-dependent eddy diffusivities
  ([turbulence](../02-bulk/05-turbulence-and-eddy-diffusivity.md)).
* **Ice**: creep of ice is a nonlinear (Glen) viscous flow, so ice sheets are *nonlinear* transport
  problems whose surface evolves as a free boundary
  ([nonlinear diffusion](../06-beyond/06-nonlinear-diffusion-and-porous-medium.md)).
* **Permafrost and gas hydrates** combine phase change, flow and heat transport with strong feedbacks
  ([phase change & Stefan](../04-interaction/09-phase-change-and-stefan.md)).

## L3 · Transport thinking that reshapes predictions

* **Eddy diffusivity is the crux of climate prediction.** The transport of heat by unresolved eddies must
  be parameterised; failures here dominate uncertainty in climate sensitivity.
* **Groundwater models are only as good as their heterogeneity**. Effective dispersion coefficients are
  asymptotic quantities, often not reached at field scales — so "non-Fickian" is the norm, not an anomaly
  ([shear dispersion](../02-bulk/06-shear-dispersion-taylor-aris.md)).
* **Subsidence and induced seismicity** show that transport changes the solid: coupling flow with
  poroelasticity is mandatory for aquifer and reservoir management
  ([subsidence](../04-interaction/13-subsidence-and-poroelasticity.md)).
* **CO₂ storage** requires coupled multi-phase flow, dissolution, geochemistry and geomechanics — a
  pointed example of multiphysics coupling stability
  ([splitting & coupling](../07-numerics/05-operator-splitting-and-multiphysics-coupling.md)).

## L4 · Practice

* **Scale analysis before simulation**: for a 1000 km basin, $1000$ Myr, $10^{-6}$ m²/s hydraulic
  diffusivity, the transport time is set by diffusion and not by any assumed velocity.
* **Never trust a single realisation** for heterogeneous media: ensembles and UQ are required
  ([stochastic PDEs](../06-beyond/07-stochastic-pdes-and-random-media.md)).
* **Conservation audits** are non-negotiable at climate scale: mass and energy budgets must close to
  machine precision over century-scale integrations
  ([structure-preserving schemes](../07-numerics/13-structure-preserving-discretizations.md)).

## Checks

1. Why is mantle convection a Rayleigh–Bénard problem with an enormous Prandtl number? *(Inertia is
   negligible compared to viscous forces in a creeping solid — the momentum equation is essentially
   balance-dominated.)*
2. Why is "the" dispersion coefficient not a material property in an aquifer? *(Heterogeneity is
   multiscale; dispersion is an asymptotic, scale-dependent quantity.)*

## See also

[Convection & buoyancy](../02-bulk/02-convection-and-buoyancy.md) ·
[Porous media & Darcy](../02-bulk/08-porous-media-and-darcy.md) ·
[Subsidence & poroelasticity](../04-interaction/13-subsidence-and-poroelasticity.md) ·
[Homogenisation & upscaling](../06-beyond/08-homogenization-and-upscaling.md)
