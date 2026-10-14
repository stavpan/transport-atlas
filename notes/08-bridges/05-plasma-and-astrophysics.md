---
title: Transport in plasma & astrophysics
blurb: Where the continuum fails and gravity competes with pressure — kinetic transport, radiation, accretion and cosmic rays.
depth: 3
tags: [plasma, astrophysics, accretion, cosmic rays, reconnection]
---

# Transport in plasma & astrophysics

> **One-line picture.** Space is not empty and stars are not solid: astrophysical transport is kinetics,
> radiation and MHD competing on scales where the mean free path can exceed the system.
>
> **Prerequisites.** [BGK & Vlasov](../05-kinetic/02-bgk-vlasov-and-plasma-kinetics.md),
> [radiative transfer](../05-kinetic/04-radiative-transfer.md)

## L1 · The transport modes, and when each applies

| Environment | Mean free path vs size | Description needed |
|---|---|---|
| solar wind, corona | $\gg$ size along field lines | [Vlasov](../05-kinetic/02-bgk-vlasov-and-plasma-kinetics.md), kinetic instabilities |
| magnetosphere | comparable | hybrid kinetic–fluid, reconnection |
| tokamak core | small across field, huge along it | anisotropic (Braginskii) fluid + gyrokinetics |
| accretion disc (ISM) | small | MHD with turbulent stress closures |
| stellar interior | very small | radiation + convection (mixing-length closures) |
| supernova remnant | shock-dominated | MHD shocks, particle acceleration |
| neutron star, merger | quantum/general-relativistic | relativistic MHD, neutrino transport |

The organising principle is the same as everywhere in this atlas: **compare a mean free path (or
collision time) with the system size (or time) and choose the description accordingly.** The
astrophysical twist is that the comparison often comes out "neither", which is why hybrid and
asymptotic-preserving methods dominate the field.

## L2 · Three transport problems that organise the subject

* **Accretion discs.** Angular momentum must be transported outward for matter to spiral inward. Micro
  viscosity is far too small, so the transport is turbulent and described by a stress closure
  ($\alpha$-disc, or magnetorotational-instability-driven MHD turbulence). This is *exactly* an
  eddy-viscosity problem ([turbulence](../02-bulk/05-turbulence-and-eddy-diffusivity.md)) with the same
  scientific status (and the same caveats) as engineering closures.
* **Cosmic-ray transport.** Charged particles scatter on magnetic turbulence, diffusing with an
  energy-dependent $D(E)$; the advection–diffusion equation in *momentum* space becomes transport in
  phase space, producing spectral features observed at Earth.
* **Radiative transport in stars and atmospheres.** Photon diffusion in the interior (Rosseland limit) and
  line transfer in atmospheres (full RTE) determine stellar structure and the spectra we interpret —
  and in supernovae and neutron-star mergers the neutrino version determines the explosion and the
  elements produced ([radiative transfer](../05-kinetic/04-radiative-transfer.md)).

## L3 · Ideas that transfer back to engineering

* **Anisotropy is the rule**: transport coefficients along and across magnetic field lines differ by
  orders of magnitude, so tensor coefficients dominate the physics — as in layered porous media.
* **Nonlocal transport**: photon and neutrino transport, and non-local heat flux in laser plasmas, cannot
  be represented by a local gradient law at all.
* **Kinetic dissipation without collisions**: Landau damping shows that "dissipation" can be phase-space
  transport ([BGK & Vlasov](../05-kinetic/02-bgk-vlasov-and-plasma-kinetics.md)).
* **Instability-driven transport**: most astrophysical transport coefficients are set by instabilities
  rather than molecular properties, so they must be *computed*, not looked up.

## L4 · Practice

* **Never use a continuum code outside its mean-free-path validity**, especially across shocks and in low
  density plasma: the kinetic correction dominates the shock structure.
* **Conserve and constrain**: divergence cleaning for magnetic fields, exact conservation for
  relativistic solvers, and careful treatment of the conservative-to-primitive inversion.
* **Benchmarks**: Landau damping rates, the Orszag–Tang vortex, Blondin reconnection tests, and
  relativistic shock tubes ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Kinetic turbulence in the solar wind; reconnection in relativistic plasmas;
  neutrino transport in mergers; dynamo action across planetary and stellar regimes.

## Checks

1. Why is accretion-disc transport a closure problem? *(Micro viscosity is far too weak to move angular
   momentum; turbulent stress must be modelled.)*
2. What determines whether you need kinetics or MHD? *(The mean free path and gyro-radius compared with
   the gradient scale lengths.)*

## See also

[BGK & Vlasov / plasma kinetics](../05-kinetic/02-bgk-vlasov-and-plasma-kinetics.md) ·
[Radiation & neutron transport](../05-kinetic/04-radiative-transfer.md) ·
[MHD & relativistic transport](../06-beyond/13-mhd-and-relativistic-transport.md) ·
[Turbulence & eddy diffusivity](../02-bulk/05-turbulence-and-eddy-diffusivity.md)
