---
title: Kinetic & radiative transport
blurb: Beyond the continuum — distribution functions, collisions, plasmas, probability densities and radiation.
depth: 3
tags: [index, kinetic theory, radiation]
---

# Kinetic & radiative transport

The previous categories all assumed a continuum: densities and fields varying smoothly in space. This
category removes that assumption. When the mean free path is not small (rarefied gases, plasmas,
nanoscale heat), or when the transported quantity *is* a probability density, the state is a distribution
in phase space and the equation is kinetic.

| # | Note | The one thing it gives you |
|---|---|---|
| 1 | [The Boltzmann equation](01-boltzmann-equation.md) | distribution functions, collision invariants, the H-theorem, and Chapman–Enskog |
| 2 | [BGK, Vlasov & plasma kinetics](02-bgk-vlasov-and-plasma-kinetics.md) | relaxation models, Landau damping, why dissipation needs no collisions |
| 3 | [Fokker–Planck & Kramers escape](03-fokker-planck-and-kramers.md) | drift–diffusion in probability space; barrier crossing |
| 4 | [Radiative transfer & neutron transport](04-radiative-transfer.md) | directional transport with in-scattering: an integro-differential equation |
| 6 | [Lattice-Boltzmann & particle kinetics](06-lattice-boltzmann-and-particle-kinetics.md) | solving kinetics directly: LBM, DSMC and friends |

![**Figure D.** The Knudsen ladder: as the mean free path grows relative to the device, the hydrodynamic
closure is lost and only kinetic descriptions survive.](../../figures/knudsen-regimes.svg)

## The through-line

Every note here is obtained from a *distribution* by taking moments, and every one faces the same
**closure problem**: the equation for a moment depends on the next moment up
([Boltzmann](01-boltzmann-equation.md) → [BGK/Vlasov](02-bgk-vlasov-and-plasma-kinetics.md)). The
practical hierarchy is:

* **Resolve the distribution**: DSMC, lattice-Boltzmann, PIC, discrete velocity — accurate, expensive.
* **Truncate with a model**: BGK relaxation, Grad-13 moments, Braginskii anisotropic transport.
* **Take the hydrodynamic limit**: Navier–Stokes, Fourier and Fick with coefficients computed by
  Chapman–Enskog — valid only when $\mathrm{Kn}$ is small.

The same structure describes light and neutrons ([radiative transfer](04-radiative-transfer.md)) and
probability densities ([Fokker–Planck](03-fokker-planck-and-kramers.md)) — three applications that share
not a single physical concept beyond the mathematics itself.

> **Reading tip.** If you understand one note in this category thoroughly, make it
> [Fokker–Planck & Kramers](03-fokker-planck-and-kramers.md): it connects to diffusion, to stochastic
> processes, to reaction rates and to modern machine learning
> ([diffusion models](../08-bridges/07-machine-learning-and-data.md)).
