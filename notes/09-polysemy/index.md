---
title: Words that collide
blurb: Polysemy in transport — the handful of words that mean different things in neighbouring fields, and the traps they set.
depth: 1
tags: [index, polysemy, terminology]
---

# Words that collide

Transport phenomena is a subject assembled from several disciplines that independently invented the same
mathematics and then gave it incompatible names. This short category dismantles the most expensive
collisions — the ones that change the physics if you guess wrong.

| Note | The collision |
|---|---|
| [1 · Dispersion](01-dispersion.md) | four meanings: porous-media spreading, Taylor shear dispersion, wave dispersion, numerical phase error |
| [2 · Convection](02-convection.md) | heat-transfer conversation, buoyancy-driven flow, meteorological vertical transport, and "the convective term" (which is advection) |
| [3 · Diffusion & conduction](03-diffusion-and-conduction.md) | one equation, six names (diffusion, conduction, viscous diffusion, migration, relaxation, pseudo-diffusion) |
| [4 · Absorption, sinks & flux](04-absorption-and-sink-lingo.md) | absorption vs adsorption, source vs sink, physical vs numerical flux, Robin vs Cauchy vs outflow |

## The general rule

> Before writing an equation, ask three questions: **what is conserved?**, **what is the flux law?**, and
> **what is happening on the boundary?** Almost every terminological collision dissolves into one of
> these three, and almost every modelling error is a wrong answer to one of them.

Two further habits that prevent most confusion:

* **Name coefficients by their function**, not their symbol: "$D$ has units m²/s and relates mass flux to
  a concentration gradient" — then check that your symbol carries the same meaning in the paper you are
  reading.
* **Say which frame and which form** you are using — Lagrangian or Eulerian, conservative or advective.
  Half of all disagreements about "advection versus convection" are really disagreements about those two
  choices ([material derivative](../01-foundations/02-material-derivative.md)).

## See also

[Balance laws & flux](../01-foundations/01-balance-laws-and-flux.md) ·
[Constitutive relations](../01-foundations/03-constitutive-relations.md) ·
[Boundary conditions](../01-foundations/04-pde-taxonomy-and-boundary-conditions.md) ·
[Operator & equation catalogue](../10-appendix/03-operator-and-equation-catalog.md)
