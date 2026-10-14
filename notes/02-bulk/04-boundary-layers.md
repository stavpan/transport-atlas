---
title: Boundary layers
blurb: The thin region where transport is decided — Prandtl's idea, the heat–mass–momentum analogy, and matched asymptotics as a way of life.
depth: 3
tags: [Prandtl, Blasius, similarity, analogy, separation]
---

# Boundary layers

> **One-line picture.** Wherever a fast flow meets a surface, all the action is squeezed into a
> thin layer: outside it viscosity is irrelevant, inside it viscosity is the only thing that
> matters.
>
> **Prerequisites.** [advection](01-advection.md),
> [dimensionless numbers](../01-foundations/05-dimensionless-numbers.md) · **Leads to.**
> [turbulence](05-turbulence-and-eddy-diffusivity.md),
> [heat–mass–momentum analogy](../08-bridges/01-analogy-and-circuit-models.md)

## L1 · Prandtl's 1904 idea

At high Reynolds number, viscosity acts only in a thin layer near the wall, of thickness
$\delta\sim L/\sqrt{\mathrm{Re}}$, which gets *thinner* as the flow gets faster. Outside the layer
the flow is effectively inviscid and can be computed with potential theory; inside, viscous stress
balances inertia; the two are glued by matched asymptotics. The payoff: drag, heat transfer, mass
transfer and separation become properties of a few millimetres of fluid — the difference between a
wing that flies and a wing that stalls.

## L2 · The equations, and their scaling

With $\partial_y\sim1/\delta\gg\partial_x\sim1/L$, Navier–Stokes collapses to

$$u\partial_xu+v\partial_yu=-\frac{1}{\rho}\partial_xp+\nu\partial_y^2u,\qquad \partial_xu+\partial_yv=0,$$

with pressure *imposed by the outer flow* (because $\partial_yp\sim\delta/L$). For a flat plate this
has the Blasius similarity solution in $\eta=y\sqrt{U/(\nu x)}$:
$\delta\approx5x/\sqrt{\mathrm{Re}_x}$, $C_f\approx0.664/\sqrt{\mathrm{Re}_x}$.

| Layer | Diffusivity | Thickness | Wall quantity |
|---|---|---|---|
| velocity | $\nu$ | $\delta_v\sim L/\sqrt{\mathrm{Re}}$ | drag, $\tau_w$ |
| thermal | $\alpha$ | $\delta_T\sim\delta_v\mathrm{Pr}^{-1/3}$ | $\mathrm{Nu}$ |
| concentration | $D$ | $\delta_c\sim\delta_v\mathrm{Sc}^{-1/3}$ | $\mathrm{Sh}$ |

This is the origin of the **heat–mass–momentum analogy**: with $\mathrm{Pr}=\mathrm{Sc}=1$ the
three layers are identical, so one correlation serves all three
([circuit analogy](../08-bridges/01-analogy-and-circuit-models.md)).

## L3 · What the mathematics guarantees

* **Similarity is the default.** With no intrinsic length scale, the solution depends on $x$ and
  $y$ only through $\eta\propto y/\sqrt{\nu x/U}$; that is why such solutions exist and why
  numerical schemes converge quickly on them.
* **Separation is triggered, then inviscid.** An adverse pressure gradient drives the wall shear
  $\partial_yu|_{\rm wall}\to0$; beyond that point the layer detaches and the whole "outer flow
  plus thin layer" structure collapses. This is why stall cannot be predicted from potential flow.
* **Stability and transition.** Laminar layers become unstable (Tollmien–Schlichting waves, then
  turbulent spots) and the turbulent layer thickens as $x\mathrm{Re}^{-1/5}$ with much larger wall
  shear. Transition location is the hardest quantity in aerodynamics, set by tiny receptivity
  details.
* **Matched asymptotics is portable.** The same inner/outer split describes high-$\mathrm{Pe}$
  transport, thin reaction sheets, lubrication films and
  [sharp interfaces](../06-beyond/09-free-boundaries-level-sets-and-phase-field.md).

## L4 · Numerics

* **Never use uniform grids.** Wall-normal clustering or wall functions are mandatory; a uniform
  grid at $\mathrm{Re}=10^6$ is hopeless.
* **Near-wall resolution dominates the cost** of CFD: $y^+\lesssim1$ for low-Reynolds treatments,
  with wall-resolved LES scaling near $\mathrm{Re}^{1.8}$.
* **Wall functions** (log-law bridges) are cheap and treacherous: they fail in adverse pressure
  gradients, separation, and at high $\mathrm{Pr}$ or $\mathrm{Sc}$.
* **Verification cases**: Blasius skin friction, rotating-disk Nusselt, the Pohlhausen family
  ([benchmarks](../07-numerics/12-verification-validation-and-benchmarks.md)).

## Checks

1. At $\mathrm{Re}=10^6$ on a 1 m plate, how thick is the layer? *($\approx5$ mm — and that film
   sets the drag.)*
2. Why is pressure constant across the layer? *(Because $\partial_yp\sim\delta/L\ll1$; the outer
   flow dictates it.)*
3. Why does the analogy need $\mathrm{Pr}=\mathrm{Sc}=1$ to be exact? *(Only then do the three
   profiles coincide.)*

## See also

[Turbulence & eddy diffusivity](05-turbulence-and-eddy-diffusivity.md) ·
[Heat–mass–momentum analogy](../08-bridges/01-analogy-and-circuit-models.md) ·
[Engineering devices](../08-bridges/06-engineering-devices.md) ·
[Knudsen & rarefied transport](../03-microscopic/05-knudsen-and-rarefied-transport.md)
