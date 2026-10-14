---
title: Symbol glossary
blurb: Every symbol used in this atlas, with units, meaning, and the clashes that cause real mistakes.
depth: 2
tags: [glossary, symbols, units, reference]
---

# Symbol glossary

> **How to read this.** Symbols clash across disciplines — the point of this table is to flag the
> dangerous ones explicitly. Units are SI unless stated.

## Fields and states

| Symbol | Meaning | Units | Watch out |
|---|---|---|---|
| $c$ | concentration (mass or moles per volume) | kg/m³, mol/m³ | in kinetics $c$ may be dimensionless saturation |
| $C$ | dimensionless concentration | — | sometimes heat capacity |
| $T$ | temperature | K | in plasma physics $T$ is often in eV |
| $p$ | pressure | Pa | in poroelasticity $p$ is *pore* pressure |
| $\rho$ | density | kg/m³ | $\rho_b$ = bulk density of a porous medium |
| $\theta$ | porosity / void fraction | — | also used for temperature in heat-transfer texts |
| $\phi$ | potential; volume fraction; level-set function | V or — | triple use, always define |
| $S$ | saturation; source term; storativity | —, kg/(m³s), — | in hydrogeology $S$ = storativity |
| $u,v,w$ | velocity components | m/s | $u$ may also be a generic unknown |

## Transport coefficients

| Symbol | Meaning | Units | Watch out |
|---|---|---|---|
| $D$ | diffusion coefficient | m²/s | $D_{\rm eff}$, $D_L$, $D_T$, $D_K$ variants |
| $k$ | thermal conductivity | W/(m·K) | **also** a reaction rate constant |
| $\alpha$ | thermal diffusivity $k/\rho c_p$ | m²/s | **also** dispersivity, and the fractional order in $D_t^\alpha$ |
| $\nu$ | kinematic viscosity | m²/s | sometimes $\mu/\rho$, sometimes a wave frequency |
| $\mu$ | dynamic viscosity | Pa·s | **also** chemical potential |
| $K$ | permeability | m² | **also** a kinetic constant, and hydraulic conductivity when multiplied by $\rho g/\mu$ |
| $K_d$ | distribution coefficient (sorption) | m³/kg | dimensionless variants exist |
| $L$ | length scale | m | be explicit: which length? |
| $\lambda$ | mean free path; relaxation time; eigenvalue | m, s, 1/s | overused — define it every time |

## Operators and dimensionless numbers

| Symbol | Meaning | Notes |
|---|---|---|
| $\mathrm{D}/\mathrm{D}t$ | material derivative | $\partial_t+\mathbf u\cdot\nabla$ |
| $\nabla\cdot$ | divergence | flux balance |
| $\nabla^2$, $\Delta$ | Laplacian | $\Delta$ also means a *change* |
| $(-\Delta)^{\beta/2}$ | fractional Laplacian | nonlocal, $\beta=2$ local |
| $D_t^{\alpha}$ | Caputo fractional time derivative | memory |
| $\mathrm{Pe},\mathrm{Re},\mathrm{Ra},\mathrm{Da},\mathrm{Kn},\mathrm{Nu},\mathrm{Sh},\mathrm{Pr},\mathrm{Sc}$ | see [cards](02-dimensionless-number-cards.md) | each has more than one definition in the wild |
| $\varepsilon$ | dissipation rate; interface width; small parameter | m²/s³, m, — |
| $\eta$ | Kolmogorov scale; efficiency | m, — | also dynamic viscosity in some texts! |
| $\tau$ | stress; relaxation time | Pa, s | same symbol, different tensorial order |

## The five most dangerous clashes

1. **$\mu$**: viscosity (fluid mechanics) vs chemical potential (thermodynamics).
2. **$k$**: thermal conductivity vs reaction rate constant.
3. **$\alpha$**: thermal diffusivity vs dispersivity vs fractional order vs volume fraction (rare).
4. **$K$**: permeability vs equilibrium constant vs bulk modulus in $\mathrm{K}$-$ \varepsilon$.
5. **$\eta$**: Kolmogorov scale vs efficiency vs dynamic viscosity (in older German literature).

> **Habit worth forming.** Every note in this atlas states the units at least once. If you are reading a
> paper and a coefficient's units are not stated, that is not a stylistic quirk — it is a modelling
> ambiguity you will have to resolve before you can compare anything.

## See also

[Constitutive relations](../01-foundations/03-constitutive-relations.md) ·
[Dimensionless number cards](02-dimensionless-number-cards.md) ·
[Operator & equation catalogue](03-operator-and-equation-catalog.md)
