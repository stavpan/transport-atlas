---
title: Particle & Monte Carlo methods
blurb: When to stop meshing — random walkers, SPH, DSMC, and the $N^{-1/2}$ law that governs every stochastic simulation.
depth: 3
tags: [Monte Carlo, particle, SPH, DSMC, random walk, variance reduction]
---

# Particle & Monte Carlo methods

> **One-line picture.** Represent the solution by particles that move — transport becomes motion, and
> the error becomes statistical.
>
> **Prerequisites.** [discretisation & stability](01-discretization-consistency-stability-convergence.md) ·
> **Leads to.** [lattice-Boltzmann & particle kinetics](../05-kinetic/06-lattice-boltzmann-and-particle-kinetics.md),
> [inverse problems](10-inverse-problems-and-data-assimilation.md)

## L1 · Why particles

Particle methods win when (i) the dimensionality is high, (ii) the domain moves or changes topology,
(iii) the physics is naturally stochastic, or (iv) advection dominates so strongly that a mesh-based
convective term would be pure numerical diffusion. They lose when you need high accuracy in a low-dimensional
smooth problem, or when you need exact conservation.

| Method | Particle represents | Transport implemented by |
|---|---|---|
| random walk / Brownian dynamics | probability mass | random displacements + drift |
| particle tracking | fluid parcels / tracer mass | integrating $\dot{\mathbf x}=\mathbf u+\text{noise}$ |
| SPH | field values at moving nodes | kernel interpolation, symmetric forces |
| DSMC | molecules | ballistic flight + stochastic collisions |
| PIC | phase-space distribution | pushing particles, depositing moments to a grid |
| MCMC | samples of a distribution | rejection/acceptance moves |
| multi-level MC | nested sample sets | averaging across mesh levels |

## L2 · The error law and how to beat it

The central fact: Monte Carlo error decays as $N^{-1/2}$ *independently of dimension* — the reason
particles are competitive in $d\ge4$ and hopeless in $d=1$ (where a spectral method gains orders of
magnitude more per unit work).

Ways to do better:

* **Variance reduction**: antithetic variates, control variates, importance sampling, stratification.
* **Quasi-Monte Carlo**: low-discrepancy sequences give nearly $O(N^{-1})$ for smooth integrands.
* **Multi-level Monte Carlo**: compute most samples on coarse grids, few on fine — reduces cost for a
  given error by orders of magnitude in random-media problems.
* **Hybridisation**: use particles only where they are needed (near shocks or interfaces) and a
  continuum solver elsewhere, with a conservative, low-noise interface.

## L3 · What the mathematics guarantees

* **Convergence in distribution, not pointwise**: particle methods approximate weak solutions; individual
  trajectories are not the answer, statistics are.
* **Consistency of the stochastic process with the PDE**: random walks with the right drift and variance
  converge to the corresponding Fokker–Planck solution (the basis of Monte Carlo diffusion solvers).
* **Conservation is statistical, not exact**: mass is conserved only in the mean, so long simulations need
  occasional resampling or weight control.
* **Stiffness appears as rare events**: escape and reaction events are exponentially unlikely, so the
  relevant statistics cannot be obtained by brute force
  ([Fokker–Planck & Kramers](../05-kinetic/03-fokker-planck-and-kramers.md)).

## L4 · Practicalities

* **Report the statistical error bar**, and use block averaging or autocorrelation analysis for
  time-correlated samples.
* **Seed and sample-size reproducibility** matter: specify the RNG and the number of realisations, and
  use common random numbers for comparisons between model variants.
* **Neighbour search dominates the cost** in SPH/DSMC/molecular dynamics: cell lists, Verlet lists and
  spatial sorting are essential ([parallel decomposition](08-mesh-adaptivity-moving-domains-and-parallel.md)).
* **Benchmarks**: the random-walk diffusion constant, DSMC shock structure, SPH dam break, and MCMC
  sampling of a known distribution ([V&V](12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Coupling to learned proposals (MCMC with neural surrogates); particle methods for
  nonlocal and fractional operators; differentiable particle simulations.

## Checks

1. Why do particle methods beat grid methods in high dimensions? *(The error is dimension-independent.)*
2. Why must you report a statistical error bar? *(The estimator is random: $N^{-1/2}$ with a prefactor
   that depends on variance, not just on $N$.)*

## See also

[Lattice-Boltzmann & particle kinetics](../05-kinetic/06-lattice-boltzmann-and-particle-kinetics.md) ·
[Stochastic PDEs & random media](../06-beyond/07-stochastic-pdes-and-random-media.md) ·
[Anomalous diffusion](../03-microscopic/08-anomalous-diffusion.md)
