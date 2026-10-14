---
title: Turbulence & eddy diffusivity
blurb: How chaotic advection enhances transport by orders of magnitude, why closure is unavoidable, and what the energy cascade says about resolution.
depth: 3
tags: [Kolmogorov, cascade, RANS, LES, eddy diffusivity, closure]
---

# Turbulence & eddy diffusivity

> **One-line picture.** Turbulence is advection run wild: swirls of every size carry heat, mass
> and momentum far faster than molecules can — and no closed equation exists for how fast.
>
> **Prerequisites.** [convection & buoyancy](02-convection-and-buoyancy.md),
> [incompressible flow](03-incompressible-flow-vorticity-and-pressure.md) · **Leads to.**
> [mixing & chaotic advection](07-mixing-and-chaotic-advection.md),
> [ML & operator learning](../07-numerics/11-machine-learning-and-operator-learning.md)

## L1 · What is happening

Stir coffee: the swirls break into smaller swirls, and those into smaller ones, until viscosity
stops the smallest. Along the way they stretch and fold the fluid, transporting everything they
carry enormously faster than molecular diffusion — milk spreads through a cup in seconds where
diffusion alone would take hours. Two consequences dominate practice: transport is enhanced by
$10^3$–$10^6$ (eddy diffusivity $\gg$ molecular), and **that enhancement is not a material
property** — it depends on the flow, geometry and history, so it must be modelled.

## L2 · Cascade and the closure problem

**Kolmogorov (1941).** Energy enters at scale $L$, cascades through an inertial range, and
dissipates at the Kolmogorov scale

$$\eta=\left(\frac{\nu^3}{\varepsilon}\right)^{1/4}\!\sim L\,\mathrm{Re}^{-3/4},\qquad
E(k)\sim\varepsilon^{2/3}k^{-5/3}.$$

Hence a DNS needs $\sim\mathrm{Re}^{9/4}$ grid points and $\sim\mathrm{Re}^{3/4}$ time steps: about
$\mathrm{Re}^3$ work.

**Closure.** Averaging Navier–Stokes introduces the Reynolds stress

$$\partial_t\langle u_i\rangle+\langle u_j\rangle\partial_j\langle u_i\rangle
=-\partial_i\langle p\rangle/\rho+\nu\nabla^2\langle u_i\rangle-\partial_j\langle u_i'u_j'\rangle,$$

and the equations for $\langle u_i'u_j'\rangle$ involve triple correlations, forever. This is not
a technical gap but a structural fact — the same conclusion as
[Mori–Zwanzig](../01-foundations/09-linear-response-and-memory.md).

| Rung | Idea | Cost | What is hidden |
|---|---|---|---|
| RANS | model *all* fluctuations with $\nu_t$ | tiny | physics, inside constants |
| LES | resolve large eddies, model small | moderate | subgrid model error |
| DNS | resolve down to $\eta$ | $\mathrm{Re}^3$ | resolution error only |

**Eddy diffusivity** $D_t\sim u'\ell$ is the transport analogue of eddy viscosity, and rests on the
*gradient-diffusion hypothesis* — turbulent transport always down the mean gradient. It fails in
buoyant plumes and near walls, where counter-gradient fluxes appear.

## L3 · What the mathematics guarantees

* **Deterministic chaos, not noise.** Turbulence is a property of Navier–Stokes at high
  $\mathrm{Re}$; stochastic terms enter only when you average.
* **Scaling laws follow from hypotheses.** $-5/3$ rests on locality and self-similarity of the
  cascade; intermittency corrections (multifractals) show those hypotheses are approximate, with
  deviations growing with $\mathrm{Re}$.
* **Statistics are reproducible, trajectories are not.** Sensitivity to initial data forecloses
  pointwise prediction but not mean-field prediction — hence the engineering focus on means,
  variances and fluxes.
* **Anisotropy breaks universality.** Walls, stratification and rotation inject large-scale
  anisotropy; universal constants shift and logarithmic corrections appear.

## L4 · Numerics

* **Resolution follows the smallest active scale**: $\Delta x\approx\eta$ for DNS; inertial-range
  grids for LES; no scale resolution for RANS.
* **Numerical diffusion can masquerade as turbulence.** Coarse advection schemes act like extra
  eddy viscosity; evaluate a scheme by its *effective* viscosity in the inertial range.
* **Conservation matters.** Kinetic-energy-conserving (skew-symmetric) convection discretisations
  keep spectra honest; energy-manufacturing schemes give meaningless cascades.
* **Benchmarks**: decaying isotropic turbulence, channel flow at matched $\mathrm{Re}_\tau$,
  Rayleigh–Bénard at matched $\mathrm{Ra}$
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Learned closures with enforced symmetries and realizability; stochastic subgrid
  models derived from memory kernels; wall models beyond $\mathrm{Re}\sim10^{10}$ for geophysical
  and astrophysical flows.

## Checks

1. Why does DNS cost scale as $\mathrm{Re}^3$? *(Points $\sim\mathrm{Re}^{9/4}$ and steps
   $\sim\mathrm{Re}^{3/4}$.)*
2. When is a constant eddy diffusivity acceptable? *(Homogeneous, isotropic turbulence and mean
   fields only — never where counter-gradient transport occurs.)*
3. What is the single sentence version of the closure problem? *(Averaging creates a new unknown,
   whose equation creates another, without end.)*

## See also

[Mixing & chaotic advection](07-mixing-and-chaotic-advection.md) ·
[Shear dispersion](06-shear-dispersion-taylor-aris.md) ·
[Linear response & memory](../01-foundations/09-linear-response-and-memory.md) ·
[ML & operator learning](../07-numerics/11-machine-learning-and-operator-learning.md)
