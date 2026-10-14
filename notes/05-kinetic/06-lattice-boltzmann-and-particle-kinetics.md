---
title: Lattice-Boltzmann & particle kinetics
blurb: Solving transport by moving populations instead of fields — the lattice-Boltzmann method, DSMC, and when particle methods beat meshes.
depth: 4
tags: [lattice-Boltzmann, DSMC, particle methods, mesoscale, kinetic solvers]
---

# Lattice-Boltzmann & particle kinetics

> **One-line picture.** Instead of discretising the continuum equations, discretise the *kinetic*
> ones: let populations stream on a lattice and collide locally. Continuum behaviour emerges, and
> boundaries become trivial.
>
> **Prerequisites.** [Boltzmann equation](01-boltzmann-equation.md) ·
> **Leads to.** [particle & Monte Carlo methods](../07-numerics/09-particle-and-monte-carlo-methods.md),
> [machine learning & operator learning](../07-numerics/11-machine-learning-and-operator-learning.md)

## L1 · The idea

The lattice-Boltzmann method (LBM) keeps a small set of velocity directions per grid node, with
populations $f_i$ (density of molecules moving in direction $i$). Each step is two lines:

$$\text{stream: } f_i(\mathbf{x}+\mathbf{c}_i\Delta t)=f_i^*(\mathbf{x}),\qquad
\text{collide: } f_i^*=f_i-\frac{\Delta t}{\tau}\left(f_i-f_i^{\rm eq}\right),$$

with $f^{\rm eq}$ a discretised Maxwellian. Density and momentum are the moments
$\rho=\sum_if_i$, $\rho\mathbf{u}=\sum_i\mathbf{c}_if_i$ — so **conservation is exact by
construction**. In the limit of small $\Delta t$ and small $\mathrm{Ma}$, a Chapman–Enskog expansion
recovers the incompressible Navier–Stokes equations with viscosity $\nu=c_s^2(\tau-\Delta t/2)$.

Why it became popular: purely local operations (ideal for GPUs), simple handling of complex
geometry and porous media, natural multiphase and thermal extensions, and kinetic fidelity that lets
it reach $\mathrm{Kn}\sim0.1$.

## L2 · The particle/kinetic zoo

| Method | Discretises | Best for | Weakness |
|---|---|---|---|
| **LBM** | velocity space on a lattice | incompressible flow, porous media, multiphase | low $\mathrm{Ma}$; boundary and compressibility limits |
| **DSMC** | molecules directly | rarefied gas, $\mathrm{Kn}\gtrsim0.1$ | noise; cost scales with collisions |
| **SPH** | field values at particles | free-surface flow, astrophysics, impacts | consistency at boundaries; artificial viscosity |
| **PIC** | distribution via macroparticles | plasmas, kinetic transport | noise; energy conservation |
| **vortex / blob methods** | vorticity in Lagrangian elements | wakes, high-$\mathrm{Re}$ external flow | viscous and boundary treatment |
| **DPD** | coarse-grained particles with soft forces | polymer and mesoscale fluids | parameters fitted, not derived |
| **Brownian dynamics** | overdamped stochastic particles | colloids, biomolecules | no hydrodynamics unless added |

The unifying theme: **the transport operator is implemented as motion**, so there is no numerical
diffusion from differencing a convective term — the price is statistical noise and a different kind
of consistency error.

## L3 · What the mathematics guarantees

* **Consistency via Chapman–Enskog**: LBM reproduces Navier–Stokes at second order in $\Delta x$ for
  small $\mathrm{Ma}$, with a *known* error structure (compressibility error $O(\mathrm{Ma}^2)$).
* **Exact conservation and positivity** of populations under many collision models (BGK with care,
  MRT/entropic models always), plus an H-theorem for entropic variants — which is why stability at
  high $\mathrm{Re}$ is achievable with the right collision operator.
* **Boundary conditions are kinetic**, so slip, thermal transpiration and contact angle emerge from
  wall rules instead of being imposed — a genuine advantage for micro- and multiphase flows.
* **Noise is a physical statement.** Particle methods approximate a distribution, so fluctuations are
  real and scale as $N^{-1/2}$; this makes them natural for problems where fluctuations *matter*
  ([stochastic PDEs](../06-beyond/07-stochastic-pdes-and-random-media.md)).

## L4 · Numerics

* **Resolution rules**: LBM needs $\Delta t$ tied to $\Delta x$ (diffusive scaling) and $\mathrm{Ma}$
  small; DSMC needs cells smaller than the mean free path and enough particles per cell.
* **Coupling hierarchies**: hybrid continuum–kinetic solvers switch method by local $\mathrm{Kn}$;
  getting the interface conservative and noise-free is the hard part.
* **Verification**: LBM against Poiseuille and lid-driven cavity; DSMC against shock structure and
  Couette; SPH against hydrostatic and dam-break tests
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Performance**: LBM is bandwidth-bound and GPU-friendly; particle methods need sorting and
  neighbour lists, so spatial partitioning dominates the cost
  ([mesh, adaptivity & parallel](../07-numerics/08-mesh-adaptivity-moving-domains-and-parallel.md)).
* **Frontiers.** Learned collision operators ([ML & operator learning](../07-numerics/11-machine-learning-and-operator-learning.md));
  GPU-native hybrid solvers; LBM for multiphase flows with phase change; DSMC for hypersonic flight.

## Checks

1. How does a purely local algorithm produce a viscous continuum? *(Chapman–Enskog: the relaxation time
   τ sets the viscosity.)*
2. What is the main cost of particle methods? *(Noise: error decays only as $N^{-1/2}$.)*
3. Why does LBM handle complex geometry so well? *(Boundary conditions are local rules on populations;
   no body-fitted mesh is required.)*

## See also

[The Boltzmann equation](01-boltzmann-equation.md) ·
[Knudsen & rarefied transport](../03-microscopic/05-knudsen-and-rarefied-transport.md) ·
[Particle & Monte Carlo methods](../07-numerics/09-particle-and-monte-carlo-methods.md) ·
[Structure-preserving discretisations](../07-numerics/13-structure-preserving-discretizations.md)
