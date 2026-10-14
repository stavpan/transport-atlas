---
title: Advection
blurb: Passive transport of a scalar by a bulk velocity field — the first-order term that carries everything else, and the hardest term to discretise honestly.
depth: 1
tags: [hyperbolic, first order, characteristics, conservation form, CFL]
---

# Advection

> **One-line picture.** A leaf on a river is not swimming. Whatever is dissolved or suspended in
> the flow goes wherever the flow goes — and the flow does not care what it is carrying.
>
> **Prerequisites.** [material derivative](../01-foundations/02-material-derivative.md) ·
> **Leads to.** [convection & buoyancy](02-convection-and-buoyancy.md),
> [boundary layers](04-boundary-layers.md), [shocks](../06-beyond/01-conservation-laws-and-shocks.md).
> **In the equation:** the first-order term $\mathbf{u}\cdot\nabla c$ or $\nabla\cdot(\mathbf{u}c)$.

![**Figure 10.** The three personalities of scalar transport. Advection translates a profile without changing it; diffusion spreads it without moving it; together they shift *and* smear. The fourth panel is what you measure downstream: a breakthrough curve whose shape reveals the Péclet number.](../../figures/advection-vs-diffusion.svg)

## L1 · Being carried versus spreading

Put a drop of dye in a still glass: it spreads by diffusion, in every direction, slowly. Put the
same drop in a river: it travels downstream while spreading. The travelling part is advection —
passive entrainment of stuff by the bulk motion of a carrier fluid.

| Word | Who moves the stuff? | Self-driven? |
|---|---|---|
| **advection** | the bulk velocity field | no — the field exists for other reasons |
| **diffusion** | molecular randomness | no — happens even at rest |
| **convection** | the transported quantity itself | yes — heat creates the flow that carries the heat |

Advection is the great equaliser: it does not care whether the cargo is salt, heat, momentum,
radioactivity, a pathogen or a probability density. It only cares that a velocity field exists.

## L2 · The term, and how to solve it

$$\underbrace{\partial_tc+\nabla\cdot(\mathbf{u}c)=0}_{\text{conservative}}
\qquad\Longleftrightarrow\qquad
\underbrace{\partial_tc+\mathbf{u}\cdot\nabla c=-c\,\nabla\cdot\mathbf{u}}_{\text{advective}} .$$

For incompressible flow the two are identical — which is why the distinction is so often
forgotten, and why codes that advect concentration in compressible flow get the wrong answer
across shocks.

The exact solution is the **method of characteristics**: along $\dot{\mathbf{x}}=\mathbf{u}(\mathbf{x},t)$
the concentration is constant, $c(\mathbf{x},t)=c_0\big(\mathbf{X}(0;\mathbf{x},t)\big)$, where
$\mathbf{X}$ is the backward trajectory. Advection is *pure relabelling of parcels* — no
exchange, no smoothing, no loss.

| Variant | Equation | Behaviour |
|---|---|---|
| constant velocity | $\partial_tc+U\partial_xc=0$ | rigid translation |
| divergence-free field | $\partial_tc+\mathbf{u}\cdot\nabla c=0$ | parcels preserve volume; all $L^p$ conserved |
| compressible field | $\partial_t\rho+\nabla\cdot(\rho\mathbf{u})=0$ | density changes as parcels compress |
| nonlinear (Burgers) | $\partial_tu+u\partial_xu=0$ | characteristics collide: shock in finite time |
| self-advection | $\partial_t\mathbf{u}+\mathbf{u}\cdot\nabla\mathbf{u}=\cdots$ | the field carries itself: turbulence |

## L3 · What the mathematics guarantees

* **Invariants.** $\int c\,\mathrm{d}V$ is constant; in divergence-free flow every $L^p$ norm, and
  both the maximum and the minimum, are preserved. Advection is reversible and has *no smoothing
  whatsoever*.
* **No self-repair.** Nothing is damped, so sharp fronts never soften on their own. Conversely,
  smooth data stay smooth only if $\mathbf{u}$ is smooth. At a discontinuity the limit is
  non-unique: you need an **entropy condition**
  ([shocks](../06-beyond/01-conservation-laws-and-shocks.md)).
* **Gradient catastrophe.** For inviscid Burgers, smooth data break at
  $t^*=-1/\min_x\partial_xu_0(x)$ — the first time two characteristics meet. Afterwards only a
  weak solution exists, and *diffusion is what selects the physical one*. This is why numerical
  diffusion sometimes quietly saves a simulation and sometimes quietly ruins it.
* **Passive is an assumption, not a definition.** Real scalars feed back: heat changes density and
  drives motion ([convection](02-convection-and-buoyancy.md)); combustion releases heat; particles
  alter rheology. "Passive scalar" is a limit, valid when feedback is dynamically negligible.
* **Vorticity is advected, not created.** In inviscid barotropic flow the vorticity equation is
  advection plus stretching, and circulation is conserved (Kelvin). Vorticity is manufactured at
  boundaries and by baroclinicity — nowhere else.

## L4 · Numerics: why advection is where schemes are judged

Advection has no self-correcting mechanism, so it exposes every flaw in a discretisation.

* **CFL.** Explicit schemes need $U\Delta t/\Delta x\le1$ (upwind) or $\le1/\sqrt d$: a statement
  about domains of influence, not about accuracy ([CFL & stiffness](../07-numerics/02-cfl-stiffness-and-time-integration.md)).
* **Centred schemes ring; upwind schemes smear.** By Godunov's theorem, a *linear monotone* scheme
  is at best first-order accurate, so escaping the trade-off requires nonlinearity —
  [limiters, TVD and WENO](../07-numerics/04-limiters-tvd-and-weno.md).
* **Read the error.** Damping error $=$ numerical diffusion (fronts thicken); phase error $=$
  numerical dispersion (wiggles trail the front). Both are catalogued in the
  [error portrait](../07-numerics/03-numerical-diffusion-and-dispersion-error.md).
* **Semi-Lagrangian** schemes beat the CFL limit by tracing characteristics backwards, but they
  leak mass unless made conservative — fatal in climate and reservoir modelling.
* **Boundaries.** Outflow must be characteristic-aware (Danckwerts/zero-gradient), or a plume
  reflects off the edge of the world
  ([boundary conditions](../01-foundations/04-pde-taxonomy-and-boundary-conditions.md)).
* **Frontiers.** Conservative advection on the sphere and on unstructured meshes; learned
  advection operators (translation is exactly what generic neural surrogates get worst —
  [operator learning](../07-numerics/11-machine-learning-and-operator-learning.md)); advection
  with [memory](../06-beyond/04-memory-viscoelastic-and-hereditary.md).

## Words that collide

> **Advection vs convection:** [words that collide #2](../09-polysemy/02-convection.md).
> **Dispersion** in numerics is the phase error above; in hydrogeology it is mechanical spreading
> ([#1](../09-polysemy/01-dispersion.md)). **"Transport"** alone may mean advection, or the whole
> equation.

## Checks

1. In a steady, divergence-free 2-D flow, can a tracer maximum grow? *(No: pure advection
   preserves the range and every $L^p$ norm.)*
2. Why can no linear monotone scheme be second-order accurate? *(Godunov: second-order accuracy
   requires new extrema, which monotonicity forbids unless the limiter is nonlinear.)*
3. Where does the entropy condition come from physically? *(Microscopic viscosity or diffusion:
   the physically realised weak solution must dissipate energy.)*

## See also

[Convection & buoyancy](02-convection-and-buoyancy.md) ·
[Vorticity & pressure](03-incompressible-flow-vorticity-and-pressure.md) ·
[Shear dispersion](06-shear-dispersion-taylor-aris.md) ·
[Conservation laws & shocks](../06-beyond/01-conservation-laws-and-shocks.md) ·
[Upwinding, TVD & WENO](../07-numerics/04-limiters-tvd-and-weno.md)

| coupled to a wave | $\partial_tc+c\,\partial_xu=0$ | wave steepening, gas dynamics |
