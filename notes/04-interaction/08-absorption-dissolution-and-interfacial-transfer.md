---
title: Absorption, dissolution & interfacial transfer
blurb: Getting mass across an interface — Henry's law, two-film theory, penetration theory, and the enhancement that reaction adds.
depth: 2
tags: [absorption, dissolution, mass transfer coefficient, two-film, Henry]
---

# Absorption, dissolution & interfacial transfer

> **One-line picture.** Two phases in contact exchange mass until the *chemical potentials* match.
> The rate is limited by how fast molecules can cross two thin films.
>
> **Prerequisites.** [diffusion](../03-microscopic/01-diffusion.md) ·
> **Leads to.** [phase change & Stefan](09-phase-change-and-stefan.md),
> [engineering devices](../08-bridges/06-engineering-devices.md)

## L1 · What "mass transfer coefficient" hides

CO₂ dissolves in water; oxygen dissolves in blood; a tablet dissolves in the stomach. In each case
mass crosses a phase boundary, and the rate is written as

$$\dot m = k_L\,a\,(c^*-c),\qquad k_L=\frac{D}{\delta},$$

where $c^*$ is the concentration *that would be in equilibrium* with the gas (Henry's law,
$c^*=p/H$), $a$ is interfacial area per unit volume, and $\delta$ is the effective film thickness.
The coefficient $k_L$ is not fundamental: it is a *compressed* description of the boundary layer on
the liquid side (and often a second film on the gas side).

## L2 · Where $k_L$ comes from

| Model | Picture | Result | Use |
|---|---|---|---|
| two-film (Whitman) | stagnant films both sides | $1/K_{\rm ov}=1/k_G+1/(Hk_L)$ | design of absorbers |
| penetration (Higbie) | fresh elements exposed for time $t_e$ | $k_L=2\sqrt{D/(\pi t_e)}$ | short contact, bubbles |
| surface-renewal (Danckwerts) | elements replaced randomly | $k_L=\sqrt{Ds}$ | falling films, stirred tanks |
| boundary-layer | laminar film on a wall | $k_L\propto D^{2/3}$ | pipe flow, flat plates |
| Kolmogorov/turbulent | eddies sweep the interface | $k_L\propto(D/\nu)^{1/2}$ or $D^{2/3}$ | oceans, reactors |

Two robust scaling facts: $k_L$ grows with diffusivity ($k_L\propto D^{1/2}$ to $D^{2/3}$), and it
grows with stirring — which is why the same physical absorption can be limited by diffusion in a
still glass and by interfacial area in a sparged column.

## L3 · What the mathematics guarantees

* **Interface conditions are the crux.** The equilibrium relation at the interface (Henry,
  Raoult, partition coefficient) sets $c^*$; the fluxes must be equal and opposite. Using the wrong
  "continuity" condition (concentration instead of chemical potential) is the classic modelling error.
* **Reaction enhances absorption.** If the dissolved species reacts in the liquid film, the
  concentration gradient steepens: the enhancement factor $E$ ranges up to
  $E\approx\sqrt{Dk_2c_B}/k_L$ for fast second-order reactions (used in CO₂ scrubbing). The
  mathematics is *reactive* boundary layer theory.
* **Dissolution coupled to transport** produces shrinking particles (Noyes–Whitney kinetics plus
  diffusion), moving interfaces, and in extreme cases
  [free-boundary problems](../06-beyond/09-free-boundaries-level-sets-and-phase-field.md).
* **Nonlinearity and hysteresis** appear when the equilibrium relation is nonlinear (solubility
  changes with composition, salting-out effects) or when history matters (glasses, hydrates).

## L4 · Numerics and measurement

* **Do not resolve the film.** Films are often micrometres; use a two-film boundary condition with a
  measured $k_L$ rather than a mesh down to nano-scale.
* **Mass balances must include the interfacial area** ($a$, m²/m³): forgetting it is the standard
  error in multiphase reactor models.
* **Multiphase solvers** (VOF, level set, phase field) resolve the interface movement and need
  consistent mass transfer and surface tension
  ([free boundaries](../06-beyond/09-free-boundaries-level-sets-and-phase-field.md)).
* **Measurement**: wetted-wall columns, stirred cells, and the classic Danckwerts plot for
  $k_L$ extraction ([measurement](../10-appendix/05-measurement-and-experiments.md)).
* **Frontiers.** CO₂ capture with reactive solvents; oxygen transfer in bioreactors at high cell
  density; interfacial transport in microfluidic and nanoporous systems.

## Checks

1. Why is $k_L$ larger in a stirred vessel? *(Thinner films and surface renewal: $\delta$ smaller,
   renewal rate $s$ larger.)*
2. Why can reaction *increase* the absorbed flux beyond the physical limit? *(It consumes the
   dissolved species inside the film, steepening the gradient: the enhancement factor.)*
3. What is the correct interfacial condition? *(Equality of chemical potentials, i.e. the partition
   relation — not equality of concentrations.)*

## See also

[Sorption & retardation](07-sorption-and-retardation.md) ·
[Phase change & Stefan](09-phase-change-and-stefan.md) ·
[Heat–mass–momentum analogy](../08-bridges/01-analogy-and-circuit-models.md) ·
[Engineering devices](../08-bridges/06-engineering-devices.md)
