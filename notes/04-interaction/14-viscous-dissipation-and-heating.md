---
title: Viscous dissipation & heating
blurb: Irreversible loss of mechanical energy to heat — the term that closes the energy budget, sets the Kolmogorov scale, and makes high-speed flow hot.
depth: 2
tags: [dissipation, Brinkman, viscous heating, entropy production, Joule]
---

# Viscous dissipation & heating

> **One-line picture.** Stir honey and your arm gets tired and the honey warms up. Ordered kinetic
> energy has been degraded into random thermal motion, and there is no way back.
>
> **Prerequisites.** [incompressible flow & vorticity](../02-bulk/03-incompressible-flow-vorticity-and-pressure.md) ·
> **Leads to.** [turbulence](../02-bulk/05-turbulence-and-eddy-diffusivity.md),
> [entropy & variational structure](../01-foundations/07-entropy-and-variational-structure.md)

## L1 · The one-way street

Dissipation is the *irreversible* conversion of mechanical energy to internal energy. It appears in
the momentum equation as friction and in the energy equation as a source:

$$\rho c_p\left(\partial_tT+\mathbf{u}\cdot\nabla T\right)=\nabla\cdot(k\nabla T)+\Phi,\qquad
\Phi=2\mu\,\mathbf{D}:\mathbf{D},\qquad \mathbf{D}=\tfrac12(\nabla\mathbf{u}+\nabla\mathbf{u}^{\top}).$$

The same quantity, integrated over the flow, is the *dissipation rate*
$\varepsilon=2\nu\langle\mathbf{D}:\mathbf{D}\rangle$, which sets the smallest scale of turbulence,
$\eta=(\nu^3/\varepsilon)^{1/4}$ ([turbulence](../02-bulk/05-turbulence-and-eddy-diffusivity.md)) and
fixes the high-wavenumber end of the energy spectrum.

Related heating terms that are usually lumped with it: **Joule heating** $\mathbf{J}\cdot\mathbf{E}$ in
current-carrying fluids and solids, **dielectric heating**, and **ohmic losses** in
[Nernst–Planck](../03-microscopic/07-charged-and-electrochemical-transport.md) systems.

## L2 · When does it matter?

| Situation | Criterion | Why dissipation matters |
|---|---|---|
| ordinary water flow | $\mathrm{Br}\ll1$ | neglect it; heating is immeasurable |
| high-speed gas | $\mathrm{Ma}\gg1$ | adiabatic wall temperature exceeds freestream: thermal protection design |
| polymer processing | $\mathrm{Br}\sim O(1)$ | dissipation can dominate the melt temperature and change the viscosity (a *coupled* nonlinearity) |
| lubrication films | $\mathrm{Br}\gtrsim1$ | friction-generated heat thins the lubricant and can cause failure |
| Earth's mantle | — | viscous heating competes with radiogenic heating in the energy budget |
| rheometry | $\mathrm{Na}\sim1$ | shear heating biases measured viscosity: the classic instrument artifact |

The **Brinkman number** $\mathrm{Br}=\mu U^2/(k\Delta T)$ compares viscous heating to conducted heat,
and the **Nahme number** $\mathrm{Na}$ compares it to conduction in a channel.

## L3 · What the mathematics guarantees

* **Positivity and irreversibility.** $\Phi\ge0$ always: dissipation can only heat, never cool. This
  is why the entropy production inequality in
  [constitutive theory](../01-foundations/03-constitutive-relations.md) is automatic for Newtonian
  fluids.
* **Energy budget closure.** In the mechanical energy balance,
  $\frac{\mathrm{d}}{\mathrm{d}t}\int\frac{\rho}{2}|\mathbf{u}|^2=-\int\Phi+\text{work}$: dissipation
  is the sink that makes the equation consistent, and the exact quantity exchanged for heat.
* **Thermodynamic consistency requires different temperatures for different ingredients** in
  non-Newtonian and reacting flows; using a single $T$ blindly produces violations of the second law
  in strong shear.
* **Coupled feedback.** When viscosity is temperature-dependent (Arrhenius, polymer melts),
  dissipation and temperature form a positive feedback loop that can thermal-runaway — a genuine
  instability of [rheology](../02-bulk/09-non-newtonian-rheology.md), not a numerical artifact.

## L4 · Numerics

* **Include $\Phi$ implicitly or it will overshoot.** In high-speed and polymer flows $\Phi$ is a
  strong nonlinear source; explicit treatment makes the temperature spike.
* **Compressible codes must include the pressure-work and dissipation terms** to get wall
  temperatures and shock heating right; isothermal and incompressible formulations simply cannot
  capture them.
* **Verification**: manufactured solutions with prescribed heat sources, Couette-flow analytic
  temperature profiles, and shock-tube benchmarks (which include viscous and conduction terms)
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Dissipation in micro- and nano-flows (rarefied effects reduce it); coupling with
  chemical reactions in combustion (ignition by viscous heating); entropy-stable discretisations that
  bound the *numerical* dissipation
  ([structure-preserving schemes](../07-numerics/13-structure-preserving-discretizations.md)).

## Checks

1. Why can dissipation never cool a fluid? *($\Phi=2\mu\mathbf{D}:\mathbf{D}\ge0$: it is a sum of
   squares.)*
2. What sets the Kolmogorov scale? *(Balance of dissipation rate and viscosity:
   $\eta=(\nu^3/\varepsilon)^{1/4}$.)*
3. Why does shear heating bias rheometry? *(The sample heats itself; viscosity depends
   exponentially on temperature, so the measured value is not the isothermal one.)*

## See also

[Turbulence & eddy diffusivity](../02-bulk/05-turbulence-and-eddy-diffusivity.md) ·
[Entropy & variational structure](../01-foundations/07-entropy-and-variational-structure.md) ·
[Non-Newtonian rheology](../02-bulk/09-non-newtonian-rheology.md) ·
[Structure-preserving discretisations](../07-numerics/13-structure-preserving-discretizations.md)
