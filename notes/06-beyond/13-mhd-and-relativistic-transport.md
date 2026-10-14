---
title: MHD & relativistic transport
blurb: Transport when the medium is magnetised or moving near light speed — frozen fields, reconnection, accretion and causal thermodynamics.
depth: 4
tags: [MHD, dynamo, reconnection, relativistic, accretion]
---

# MHD & relativistic transport

> **One-line picture.** Couple transport to electromagnetism or relativity and new constraints appear:
> the field freezes into the fluid, and time becomes a coordinate you may not neglect.
>
> **Prerequisites.** [incompressible flow](../02-bulk/03-incompressible-flow-vorticity-and-pressure.md),
> [BGK & Vlasov](../05-kinetic/02-bgk-vlasov-and-plasma-kinetics.md) · **Leads to.**
> [plasma & astrophysics](../08-bridges/05-plasma-and-astrophysics.md)

## L1 · Magnetohydrodynamics

Navier–Stokes plus Maxwell, with momentum gaining the Lorentz force and the field being transported by
the flow:

$$\partial_t\mathbf B=\nabla\times(\mathbf u\times\mathbf B)+\eta\nabla^2\mathbf B,\qquad
\mathbf J=\frac{1}{\mu_0}\nabla\times\mathbf B .$$

* **Ideal MHD ($\eta\to0$): Alfvén's frozen-flux theorem.** Field lines move with the fluid; magnetic
  tension acts like a stiff spring. Consequences: Alfvén waves, magnetosonic shocks, and the
  impossibility of changing field *topology* by smooth motion.
* **Resistive MHD: reconnection.** Lines can break and rejoin, releasing magnetic energy — solar flares,
  coronal heating, tokamak sawteeth. Classical (Sweet–Parker) rates are too slow; fast reconnection
  (Petschek, plasmoid-mediated) remains an active research area.

The **dynamo problem**: how does a rotating, convecting conductor sustain a field against resistive
decay? Answered for the geodynamo and solar dynamo mainly by simulation plus mean-field closures — and
those closures are exactly the eddy-viscosity-style approximations of
[Mori–Zwanzig](../01-foundations/09-linear-response-and-memory.md).

## L2 · Relativistic and astrophysical highlights

| Setting | Transport feature |
|---|---|
| accretion disc | turbulent stress (an $\alpha$-disc closure) moves matter inward, energy outward |
| relativistic fluid | pressure contributes inertia; heat flux and bulk viscosity are frame-dependent |
| cosmic rays | energy-dependent $D(E)$ in magnetic turbulence produces spectral hardening |
| photon diffusion (Rosseland in a moving medium) | radiative viscosity and damping |
| neutrino transport | sets neutron-star cooling and nucleosynthesis |

Two lessons transfer back to ordinary engineering: **anisotropic transport** (magnetised media conduct
far better along field lines than across — structurally like layered porous media), and **closure by
mean-field theory**, with the same scientific status as engineering turbulence models.

## L3 · What the mathematics guarantees

* **Frozen flux** is a sharp statement about what ideal MHD cannot do; topology changes require
  non-ideal terms.
* **A divergence constraint**: $\nabla\cdot\mathbf B=0$ must be enforced (constrained transport,
  projection, or divergence cleaning) or solutions drift — the magnetic analogue of
  incompressibility.
* **Richer discontinuities**: slow, intermediate (Alfvén) and fast shocks plus rotational
  discontinuities, so MHD Riemann solvers are considerably more intricate than gas-dynamic ones.
* **Relativistic causality forbids naive constitutive laws.** Fourier's law with one temperature is
  acausal and unstable in relativistic fluids; causal (Israel–Stewart) or kinetic treatments are
  required — the same failure mode as
  [hyperbolic heat conduction](04-memory-viscoelastic-and-hereditary.md).

## L4 · Numerics

* **Constrained transport** keeps $\nabla\cdot\mathbf B$ at machine zero; projection is costlier and less
  robust. HLLD-type solvers plus GLM cleaning are the standard toolkit, and naive central schemes fail
  at low plasma $\beta$.
* **Dynamos need extremely long integrations** (resistive times are huge): implicit/exponential
  integrators and strict conservation are mandatory.
* **Relativistic codes** struggle with conservative-to-primitive inversion (a fragile root-find) and with
  neutrino/radiation coupling.
* **Benchmarks**: Orszag–Tang vortex, Brio–Wu shock tube, Christensen dynamo benchmarks, relativistic
  shock tubes ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Plasmoid-mediated reconnection; planetary and stellar dynamos; GR-MHD for mergers;
  kinetic corrections where MHD fails.

## Checks

1. What does frozen flux forbid, and what restores topology change? *(It forbids topology change;
   resistivity/reconnection restores it.)*
2. Why is the divergence constraint like incompressibility? *(Both constrain a vector field and require
   an extra enforcement mechanism.)*
3. Why does Fourier's law fail relativistically? *(It is acausal: signals would exceed $c$.)*

## See also

[BGK & Vlasov](../05-kinetic/02-bgk-vlasov-and-plasma-kinetics.md) ·
[Plasma & astrophysics](../08-bridges/05-plasma-and-astrophysics.md) ·
[Memory, viscoelasticity & Cattaneo](04-memory-viscoelastic-and-hereditary.md) ·
[Structure-preserving discretisations](../07-numerics/13-structure-preserving-discretizations.md)
