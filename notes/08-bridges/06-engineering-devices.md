---
title: Transport in engineering devices
blurb: Batteries, reactors, heat exchangers, chips, membranes, additive manufacturing — where the atlas pays rent.
depth: 2
tags: [batteries, reactors, heat exchangers, membranes, manufacturing, semiconductors]
---

# Transport in engineering devices

> **One-line picture.** Every device that works is a solved transport problem; every device that fails
> usually violates a transport assumption (a hot spot, a depleted electrode, a fouled surface).
>
> **Prerequisites.** [analogy & circuit models](01-analogy-and-circuit-models.md),
> [reaction kinetics](../04-interaction/01-reaction-kinetics-and-sinks.md)

## L1 · Six workhorses and their transport cores

| Device | Transport core | Failure mode if neglected |
|---|---|---|
| lithium-ion battery | P2D/Newman model: Nernst–Planck + porous-electrode kinetics | lithium plating, thermal runaway, capacity fade |
| fuel cell / electrolyser | two-phase flow in porous electrodes + membrane transport | flooding, dry-out, hot spots |
| chemical reactor | residence-time distribution + reaction + heat transfer | runaway, hot spots, poor selectivity |
| heat exchanger | convection correlations + fouling + two-phase boiling | underperformance (film resistances dominate) |
| semiconductor chip | drift–diffusion + phonon transport + contact resistance | electromigration, thermal throttling |
| membrane separation | solution–diffusion + concentration polarisation | flux decline, fouling, selectivity loss |
| additive manufacturing | melt-pool Marangoni flow + solidification + residual stress | porosity, distortion, residual stress |
| catalytic converter | pore diffusion + surface kinetics (Thiele modulus) | light-off delay, poisoning |

## L2 · Dimensionless groups are the design language

* **Thiele modulus** $\phi=L\sqrt{k/D}$: reaction versus diffusion in a catalyst pellet — sets whether the
  pellet is used efficiently (effectiveness factor $\eta=\tanh\phi/\phi$).
* **Biot number** $\mathrm{Bi}=hL/k$: whether a body is isothermal or has internal gradients, i.e. whether
  a lumped model is valid.
* **Fourier number** $\mathrm{Fo}=\alpha t/L^2$: thermal penetration in transient processes (brazing,
  quenching, batteries at high rate).
* **Damköhler and Péclet**: whether a reactor is transport-limited or kinetics-limited
  ([dimensionless cards](../10-appendix/02-dimensionless-number-cards.md)).
* **Sherwood/Nusselt correlations**: the standard route from geometry to transfer coefficient, with the
  analogy to momentum ([heat–mass–momentum analogy](01-analogy-and-circuit-models.md)).

## L3 · Failure modes as transport pathologies

* **Thermal runaway** in a battery is a positive feedback: temperature raises reaction rate (Arrhenius),
  which raises heat release, which raises temperature — and the coupling is stiff, requiring implicit,
  fully coupled simulation ([stiffness](../07-numerics/02-cfl-stiffness-and-time-integration.md)).
* **Concentration polarisation** at a membrane or electrode is a boundary-layer phenomenon: neglecting it
  over-predicts current limits and under-predicts voltage losses.
* **Hot spots in catalysis** appear where pore diffusion and reaction conspire; the same Thiele analysis
  that predicts pellet efficiency predicts ignition.
* **Fouling and scaling** are slow, history-dependent surface processes with hysteresis
  ([accretion & surface growth](../04-interaction/11-accretion-ablation-and-surface-growth.md)).

## L4 · Practice

* **Start with a network model** (resistances, capacitances, Thiele/Biot/Fourier), then simulate only
  where the lumped model fails. Most device engineering is won at this stage.
* **Couple multiphysics implicitly** where feedback is strong (batteries, combustion, phase change) and
  use stabilised partitioned schemes where it is weak
  ([splitting & coupling](../07-numerics/05-operator-splitting-and-multiphysics-coupling.md)).
* **Validate against standard protocols**: C-rate cycling for batteries, GHSV and conversion/selectivity
  for reactors, LMTD/NTU and $\epsilon$-NTU data for heat exchangers.
* **Use the verification suite routinely**: manufactured solutions plus device-level benchmarks
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).

## Checks

1. Why does the Thiele modulus determine catalyst utilisation? *(It compares reaction rate to pore
   diffusion; large $\phi$ confines reaction to a thin outer shell.)*
2. When is a lumped-capacitance model valid? *(Small Biot number: internal gradients negligible.)*

## See also

[Heat–mass–momentum analogy & circuits](01-analogy-and-circuit-models.md) ·
[Conduction](../03-microscopic/03-conduction.md) ·
[Absorption & interfacial transfer](../04-interaction/08-absorption-dissolution-and-interfacial-transfer.md) ·
[Structure-preserving discretisations](../07-numerics/13-structure-preserving-discretizations.md)
