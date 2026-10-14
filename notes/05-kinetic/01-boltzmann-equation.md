---
title: The Boltzmann equation
blurb: Transport before the continuum — the distribution function, collisions, the H-theorem, and how Navier–Stokes emerges from it.
depth: 4
tags: [Boltzmann, kinetic theory, H-theorem, Chapman-Enskog, moments]
---

# The Boltzmann equation

> **One-line picture.** Give up fields and track how many molecules are at each position with each
> velocity. Add collisions. Viscosity, conduction and diffusion fall out of the averages.
>
> **Prerequisites.** [Knudsen & rarefied transport](../03-microscopic/05-knudsen-and-rarefied-transport.md) ·
> **Leads to.** [BGK & Vlasov](02-bgk-vlasov-and-plasma-kinetics.md),
> [lattice-Boltzmann](06-lattice-boltzmann-and-particle-kinetics.md)

## L1 · The object and the equation

The fundamental object is the distribution $f(\mathbf{x},\mathbf{v},t)$: density of molecules in
*phase space*. Its evolution balances free flight against collisions:

$$\partial_tf+\mathbf{v}\cdot\nabla_{\mathbf x}f+\frac{\mathbf F}{m}\cdot\nabla_{\mathbf v}f=\mathcal C[f],$$

and the continuum fields are its moments:
$\rho=\int mf\,\mathrm d\mathbf v$, $\rho\mathbf u=\int m\mathbf v f\,\mathrm d\mathbf v$,
$\rho e=\int\frac12m|\mathbf v-\mathbf u|^2f\,\mathrm d\mathbf v$. You bother because the continuum
equations fail when $\mathrm{Kn}$ is not small, when geometry is smaller than the mean free path, or
when the *tail* of the velocity distribution drives the physics (evaporation, threshold chemistry,
plasma instabilities).

## L2 · Collisions, invariants, closure

Collisions conserve mass, momentum and energy — the **collision invariants** — which is exactly why
moment equations reproduce the continuum conservation laws. But moments generate a **hierarchy**
(density → velocity → pressure tensor → heat flux → …): the kinetic version of the closure problem
([Mori–Zwanzig](../01-foundations/09-linear-response-and-memory.md)). Two standard closures:

* **Chapman–Enskog** expands in $\mathrm{Kn}$; first order returns Navier–Stokes with *computable*
  coefficients ($\mu\propto\sqrt T$, $k$, $D$ in terms of collision integrals).
* **Grad / moment methods** assume a distribution shape (Hermite expansion about a Maxwellian) and
  truncate; higher moments add non-physical modes unless regularised.

**H-theorem (1872):** collisions force $H=\int f\ln f\,\mathrm d\mathbf v$ to decrease, equilibrium is
Maxwell–Boltzmann, and entropy production is $\ge0$ — the microscopic origin of the second law and of
the positivity of every transport coefficient.

## L3 · What the mathematics guarantees

* **Conservation is exact for any admissible collision operator**, which is why lattice-Boltzmann and
  moment methods are conservative by construction.
* **Equilibrium and stability.** The Maxwellian is the unique equilibrium; linearised collisions have
  negative-definite structure, so the kinetic equation is stable — and with it the dissipative
  continuum equations it generates.
* **Second order is dangerous.** Burnett/super-Burnett equations lose hyperbolicity and can violate
  the second law: kinetic theory is authoritative, its continuum truncations are not.
* **Phenomena with no continuum analogue**: velocity slip, temperature jump, the Knudsen flow-rate
  minimum, thermal transpiration, and rarefied-gas non-Newtonian behaviour in shocks.

## L4 · Numerics

* **DSMC** solves it directly by Monte Carlo flight and stochastic collisions — the reference method
  for $\mathrm{Kn}\gtrsim0.1$, with cost set by collisions not cells.
* **Discrete-velocity methods** (lattice-Boltzmann style) are efficient at low $\mathrm{Ma}$ with
  well-understood accuracy ([lattice-Boltzmann](06-lattice-boltzmann-and-particle-kinetics.md)).
* **Conservation and positivity must be enforced**: naive collision discretisations give negative
  populations and violate H.
* **Benchmarks**: shock structure, Couette flow across a wide $\mathrm{Kn}$ range, the Knudsen minimum
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Hypersonic rarefied aerodynamics, fusion edge plasmas, granular gases, quantum kinetic
  equations ([quantum & condensed matter](../08-bridges/10-quantum-and-condensed-matter.md)).

## Checks

1. Why do moment equations conserve mass and momentum regardless of closure? *(Collision invariants.)*
2. What does the H-theorem buy macroscopically? *(Entropy production $\ge0$ and positivity of transport
   coefficients.)*
3. Why are Burnett equations rarely used? *(Loss of hyperbolicity; possible second-law violation.)*

## See also

[BGK & Vlasov](02-bgk-vlasov-and-plasma-kinetics.md) ·
[Knudsen & rarefied transport](../03-microscopic/05-knudsen-and-rarefied-transport.md) ·
[Fokker–Planck & Kramers](03-fokker-planck-and-kramers.md) ·
[Lattice-Boltzmann](06-lattice-boltzmann-and-particle-kinetics.md)
