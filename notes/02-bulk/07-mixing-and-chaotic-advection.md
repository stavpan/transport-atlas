---
title: Mixing & chaotic advection
blurb: Stretching and folding without randomness — Lagrangian chaos, mixing rates, coherent structures, and how jets and plumes transport by entrainment.
depth: 3
tags: [mixing, chaotic advection, Lyapunov, LCS, entrainment, jets]
---

# Mixing & chaotic advection

> **One-line picture.** Perfectly smooth, deterministic flow can mix like a random one. The trick
> is not randomness but *stretching and folding* — the baker's transformation performed by the
> fluid itself.
>
> **Prerequisites.** [advection](01-advection.md), [turbulence](05-turbulence-and-eddy-diffusivity.md) ·
> **Leads to.** [chaotic mixing in applications](../08-bridges/06-engineering-devices.md),
> [anomalous diffusion](../03-microscopic/08-anomalous-diffusion.md)

## L1 · Mixing without randomness

Stir a cup slowly at low Reynolds number — honey, not water — and the fluid comes back to where it
started when you reverse the stroke. It looks reversible. Do it many times with a slight twist
each stroke and suddenly the dye is smeared everywhere, irreversibly, even though the flow is
laminar, steady in time and utterly deterministic. That is **Lagrangian chaos**: trajectories
separate exponentially even when the velocity field is smooth and simple.

Mixing has two stages, and confusing them causes most mistakes:

1. **Stirring** — kinematics. Stretch the interface between fluids; this *increases the area*
   available for molecular diffusion. No mass is mixed yet.
2. **Diffusion** — physics. Molecules must actually cross the interface; only then is mixing
   complete. Stirring shortens the distance they must cross, from millimetres to nanometres.

So a "perfectly mixed" tank is one where the striation thickness is small enough that diffusion
finishes on the time scale you care about — a *quantitative* criterion, not a hand-wave.

## L2 · How to measure mixing and transport by entrainment

| Quantity | Meaning |
|---|---|
| strain rate / stretching rate | local rate at which material lines grow |
| Lyapunov exponent $\lambda$ | $\delta(t)\sim\delta_0e^{\lambda t}$ for neighbouring parcels |
| Poincaré map | stroboscopic view; its fixed points organise the chaos |
| striation thickness $s(t)$ | distance across which diffusion must act; $s\sim s_0e^{-\lambda t}$ |
| Lyapunov (finite-time) exponents | local diagnostics for real, non-uniform flows |
| coherent structures (LCS) | ridges of the finite-time Lyapunov field: barriers to transport |

A practical rule of thumb: for a scalar to be uniform at scale $\ell$ you need
$t_{\rm mix}\approx\lambda^{-1}\ln(L/\ell)$ — *logarithmic* in the scale ratio, which is why
stirring is so effective.

**Jets, plumes and wakes** are the large-scale cousins of mixing: momentum-driven jets entrain
ambient fluid at a rate set by the shear-layer velocity ratio, buoyancy-driven plumes entrain in
proportion to a buoyancy flux, and wakes entrain in proportion to drag. They all share the same
signature: velocity and concentration profiles become **self-similar** downstream, with widths
growing linearly and centre-line values decaying as a power law,

$$u_c\sim x^{-1/3}\ (\text{jet}),\qquad u_c\sim x^{-1/2},\ w_c\sim x^{-1/3}\ (\text{plume}),$$

which is nothing but a statement that entrainment is the dominant transport mechanism there.

## L3 · What the mathematics guarantees

* **Exponential separation under bounded velocity fields is possible,** and generically occurs in
  2-D time-periodic and 3-D steady incompressible flows. Chaos needs no turbulence.
* **Advection alone cannot mix.** It rearranges; diffusion completes the job. This is why
  Reynolds-number-free microfluidic devices can be designed to mix using chaotic advection
  [with no turbulence at all].
* **Barriers exist.** In incompressible 2-D flow, streamlines are invariant curves; with time
  dependence, KAM tori and LCS remain *transport barriers*, and transport between regions is
  organised by the hyperbolic invariant manifolds that are responsible for lobe dynamics.
* **Batchelor scaling.** In a smooth chaotic flow, the scalar spectrum develops a $k^{-1}$ range
  above the stirring scale, sharpening gradients until diffusion takes over at the Batchelor
  scale — the reason we call turbulence a mixer but not a pure mixer.

## L4 · Numerics

* **Numerical diffusion is the enemy** in mixing studies: a first-order scheme's artificial
  diffusion can destroy the striations that carry the physics. Use high-order or spectral
  advection, or particle tracking, if you care about interfaces.
* **Particle tracking and lobe analysis** are the standard tools: integrate trajectory equations
  for many seeds, then compute finite-time Lyapunov exponents on the cloud
  ([particle methods](../07-numerics/09-particle-and-monte-carlo-methods.md)).
* **Mixing measures for validation**: decay of variance ("intensity of segregation"), striation
  thickness distributions, and Poincaré sections.
* **Frontiers.** Optimal mixing protocols (controlling the flow to maximise mixing for a given
  energy input) and mixing in [graph/network analogues](../08-bridges/09-networks-society-and-traffic.md);
  chaotic advection interacting with [memory or yield stress](../02-bulk/09-non-newtonian-rheology.md).

## Checks

1. Why does stirring not mix by itself? *(It rearranges the interface; molecules still have to
   cross it.)*
2. Why is $t_{\rm mix}$ logarithmic in the scale ratio? *(Stretching is exponential, so the
   distance to be diffused shrinks exponentially.)*
3. What is an LCS in one sentence? *(A ridge of the finite-time Lyapunov field — a moving barrier
   that material does not cross.)*

## See also

[Turbulence & eddy diffusivity](05-turbulence-and-eddy-diffusivity.md) ·
[Shear dispersion](06-shear-dispersion-taylor-aris.md) ·
[Networks, society & traffic](../08-bridges/09-networks-society-and-traffic.md)
