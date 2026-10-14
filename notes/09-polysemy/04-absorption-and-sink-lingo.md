---
title: Words that collide 4 — absorption, sinks & flux lingo
blurb: Absorption versus adsorption, source versus sink, flux (physical) versus flux (numerical), and the boundary-condition names everybody misuses.
depth: 2
tags: [polysemy, absorption, source, sink, flux, boundary conditions]
---

# Absorption, sinks, flux and boundary lingo

> **Why this note exists.** These words appear in every transport paper and mean different things in
> adjoining fields. Misusing them changes the physics — often silently.
>
> **Prerequisites.** [sorption](../04-interaction/07-sorption-and-retardation.md),
> [boundary conditions](../01-foundations/04-pde-taxonomy-and-boundary-conditions.md)

## The collisions

| Word | Meaning A | Meaning B (and C) |
|---|---|---|
| **absorption** | uptake into the *bulk* of another phase (CO₂ into water) | in optics/radiative transfer, conversion of radiative energy into internal energy |
| **adsorption** | attachment to a *surface* | — |
| **sink** | volumetric removal term ($f<0$) | a well in a flow field; an absorbing boundary |
| **source** | volumetric addition ($f>0$) | an inflow boundary; a point injection |
| **flux** | physical flux, $\mathbf J$ (per area per time) | **numerical flux** at a cell face (a reconstruction, not a physical quantity) |
| **Danckwerts condition** | zero-gradient outflow | sometimes loosely used for any outflow treatment |
| **Robin / third kind** | a relation between flux and state, $-k\partial_nT=h(T-T_\infty)$ | "convective boundary condition" (which is a *model of a film*, not a fluid-dynamic fact) |
| **Cauchy condition** | state **and** flux prescribed | often conflated with Robin |
| **outflow / efflux** | mass leaving the domain | "outflow boundary", which in some codes means *inflow allowed where the flow reverses* |

## Why the distinctions matter

* **Absorption is a volumetric process; adsorption is interfacial.** A model that treats an interfacial
  process as a volumetric sink cannot represent saturation, competition or surface area — and gets the
  wrong scaling with particle size.
* **A source term is not a boundary condition.** Injecting "1 kg/s" via a boundary flux and via a
  volumetric source differ in where the mass appears: near the boundary (with a boundary layer) or in the
  bulk. Choose the one that matches the physics.
* **Numerical flux is not physical flux.** Comparing "fluxes" from a report and from a code often mixes
  these; only the physical flux has units of transported quantity per area per time, and only it appears
  in a mass balance.
* **Robin is a closure, not a law.** The heat-transfer coefficient $h$ contains the boundary layer; the
  same $h$ cannot be reused at a different $\mathrm{Re}$, $\mathrm{Pr}$ or geometry without a correlation.

## The trap

> "Loss to the walls" can be modelled as a sink, a boundary flux, or a Robin condition, and the three give
> *different* answers: which one is right depends on whether the transport resistance is in the bulk or in
> a surface layer. Ask "where is the resistance?" before writing the term.

## See also

[Absorption, dissolution & interfacial transfer](../04-interaction/08-absorption-dissolution-and-interfacial-transfer.md) ·
[Sorption & retardation](../04-interaction/07-sorption-and-retardation.md) ·
[Boundary conditions](../01-foundations/04-pde-taxonomy-and-boundary-conditions.md) ·
[Reaction kinetics & sinks](../04-interaction/01-reaction-kinetics-and-sinks.md)
