---
title: Sedimentation, deposition & filtration
blurb: Particles that fall and stick — settling velocities, hindered settling, filter cakes, deposition velocity and resuspension.
depth: 2
tags: [settling, Stokes, Rouse, filtration, deposition, aerosols]
---

# Sedimentation, deposition & filtration

> **One-line picture.** Suspended particles have their own drift velocity relative to the fluid, and
> they accumulate wherever the flow deposits them. Two sentences, and a whole industry.
>
> **Prerequisites.** [diffusion](../03-microscopic/01-diffusion.md), [advection](../02-bulk/01-advection.md) ·
> **Leads to.** [wells & breakthrough](12-wells-injection-efflux-and-breakthrough.md),
> [engineering devices](../08-bridges/06-engineering-devices.md)

## L1 · Settling: a drift term, not a diffusion

For a small sphere in a viscous fluid, gravity balances drag:

$$v_s=\frac{(\rho_p-\rho)g\,d^2}{18\mu}\quad\text{(Stokes)},\qquad
\mathbf{v}_s=v_s\,\hat{\mathbf{g}} .$$

Sedimentation is therefore *advection with an extra velocity*: the transport equation gains a
gravitational flux $\mathbf{J}_{\rm sed}=c\mathbf{v}_s$, linear in $c$ and always in the same
direction. Nothing exotic — until concentration rises, when particles hinder each other
($v_s\to v_s(1-\phi)^n$, Richardson–Zaki), and when turbulence competes with settling to set a
vertical profile (the Rouse profile: $c(z)\propto(z/h)^{-{\rm Ro}}$).

## L2 · Deposition, resuspension and filtration

Deposition is a *boundary* phenomenon: the rate at which particles stick to a wall is written as a
deposition velocity $k_d$ (m/s) and enters as a Robin condition

$$-D\partial_nc=k_dc \quad\text{at the wall}.$$

| Mechanism | Dominant particles | Deposition velocity |
|---|---|---|
| Brownian diffusion | $<0.1\ \mu$m | increases as size decreases |
| interception / impaction | $1-10\ \mu$m | peaks at a few microns |
| sedimentation | $>10\ \mu$m | increases with $d^2$ |
| electrostatic attraction/repulsion | all charged | depends on surface charge, ionic strength |
| resuspension | any deposited | threshold shear stress |

The famous **minimum in deposition efficiency at ~0.3 µm** is *why* this size is the hardest for
respiratory protection, and why fine-particle air pollution penetrates deep into the lungs.

**Filtration** adds a growing, moving boundary: the filter cake accumulates and its hydraulic
resistance increases (Darcy flow through a compressible porous medium), which is why constant-pressure
filtration shows declining flux ($t/V$ linear vs $V$), and why cross-flow filtration exists at all.

## L3 · What the mathematics guarantees

* **Settling is a first-order term, so it needs upwinding.** Numerically, sedimentation behaves like
  advection and inherits all its pathologies (oscillations, numerical diffusion) and its fixes
  ([limiters](../07-numerics/04-limiters-tvd-and-weno.md)).
* **Polydispersity creates continuous spectra of velocities.** The transport equation becomes a
  population balance (integro-differential in size) with size-dependent transport — the natural home
  of [nonlocal operators](../06-beyond/03-nonlocal-and-fractional-operators.md) and of
  moment methods.
* **Hindered settling and flux-limiting.** In a batch column, the well-known Kynch theory derives
  from a *conservation law* with a non-convex flux $c\,v_s(c)$: the result is shocks and rarefactions
  that predict the appearance of a clear interface and of a rising sludge blanket
  ([conservation laws & shocks](../06-beyond/01-conservation-laws-and-shocks.md)).
* **Deposition competes with diffusion and reaction** at surfaces, producing the standard
  resistances-in-series structure: mass transfer to the wall, surface reaction, and (for filtration)
  the cake resistance.

## L4 · Numerics and measurement

* **Do not model deposition as a negative source in the bulk.** Deposition is a boundary flux; smearing
  it into the volume destroys the near-wall profile, which is usually the whole point of the model.
* **Moving boundaries for cakes and sludge**. A growing deposit changes the domain; use moving meshes
  or [level sets](../06-beyond/09-free-boundaries-level-sets-and-phase-field.md).
* **Benchmarks**: Stokes settling of a monodisperse suspension (analytic Kynch solution),
  constant-pressure filtration ($t/V$ plots), and the Rouse profile in a channel
  ([measurement](../10-appendix/05-measurement-and-experiments.md)).
* **Frontiers.** Microplastic transport in oceans; deposition in the lung (dosimetry); electrokinetic
  deposition; cake compressibility in membrane bioreactors.

## Checks

1. Why is deposition a boundary condition rather than a source term? *(Particles must reach the wall
   before they can stick; the physics lives in the near-wall flux.)*
2. Why does deposition efficiency have a minimum near 0.3 µm? *(Diffusion dominates below, impaction
   above; neither is efficient in between.)*
3. Why does a sludge-blanket interface appear spontaneously? *(Non-convex flux in a conservation law:
   shocks form without any external trigger.)*

## See also

[Advection](../02-bulk/01-advection.md) ·
[Conservation laws & shocks](../06-beyond/01-conservation-laws-and-shocks.md) ·
[Wells & breakthrough](12-wells-injection-efflux-and-breakthrough.md) ·
[Measurement & experiments](../10-appendix/05-measurement-and-experiments.md)
