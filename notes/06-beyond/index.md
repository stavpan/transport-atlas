---
title: Beyond classical PDEs
blurb: Where the classical framework ends — shocks, viscosity solutions, nonlocality, memory, stochasticity, free boundaries, optimal transport, MHD.
depth: 4
tags: [index, beyond PDEs, advanced]
---

# Beyond classical PDEs

The classical framework of this atlas assumes: a local, smooth-enough PDE, with a unique solution that
depends continuously on the data. Every one of those assumptions has a productive failure mode, and this
category collects them. These are the notes to read when a problem refuses to fit.

| # | Note | The assumption it breaks |
|---|---|---|
| 1 | [Conservation laws & shocks](01-conservation-laws-and-shocks.md) | smooth solutions exist; uniqueness of weak solutions |
| 2 | [Hamilton–Jacobi & viscosity solutions](02-hamilton-jacobi-and-viscosity-solutions.md) | differentiability of solutions |
| 3 | [Nonlocal & fractional operators](03-nonlocal-and-fractional-operators.md) | locality |
| 4 | [Memory, viscoelasticity & Cattaneo](04-memory-viscoelastic-and-hereditary.md) | instantaneous constitutive response |
| 6 | [Nonlinear diffusion & porous medium](06-nonlinear-diffusion-and-porous-medium.md) | infinite propagation speed; non-degenerate diffusivity |
| 7 | [Stochastic PDEs & random media](07-stochastic-pdes-and-random-media.md) | determinism; smooth coefficients |
| 8 | [Homogenisation & upscaling](08-homogenization-and-upscaling.md) | that one scale is enough |
| 9 | [Free boundaries, level sets & phase fields](09-free-boundaries-level-sets-and-phase-field.md) | that the domain is known |
| 10 | [Optimal transport & gradient flows](10-optimal-transport-and-gradient-flows.md) | that the right geometry is Euclidean |
| 11 | [Microcontinuum & generalized continua](11-microcontinuum-and-generalized-continua.md) | that a material point has no size |
| 12 | [Variational inequalities & hysteresis](12-variational-inequalities-and-hysteresis.md) | that behaviour is a function of the current state |
| 13 | [MHD & relativistic transport](13-mhd-and-relativistic-transport.md) | that the medium is unmagnetised and slow |

![**Figure E.** Characteristics, shocks and rarefactions: the picture that replaces "solutions are smooth"
once nonlinearity enters the flux.](../../figures/conservation-law-shocks.svg)

## How to use this category

Each note follows the same pattern: *state the classical assumption → show how it fails → give the
replacement theory → say what changes numerically*. If your problem has a sharp front and your solver
rings, start at [limiters](../07-numerics/04-limiters-tvd-and-weno.md) but understand
[shocks](01-conservation-laws-and-shocks.md). If a coefficient depends on the history, read
[memory](04-memory-viscoelastic-and-hereditary.md). If your meshes disagree, read
[homogenisation](08-homogenization-and-upscaling.md).

> **The unifying discovery of this category** is that most of these generalisations are *projections or
> limits* of one another: eliminating a fast variable gives memory
> ([Mori–Zwanzig](../01-foundations/09-linear-response-and-memory.md)); eliminating a small scale gives
> homogenisation; letting the horizon shrink recovers the local operator; and changing the metric turns
> diffusion into transport along geodesics
> ([one mathematics of transport](../08-bridges/11-unifying-mathematics-of-transport.md)).

## Three more ways to leave the classical framework

| # | Note | The assumption it breaks |
|---|---|---|
| 14 | [Integrable systems & solitons](14-integrable-systems-and-solitons.md) | that nonlinear dispersive waves must smear or break: Lax pairs, inverse scattering as a nonlinear Fourier transform, soliton resolution |
| 15 | [Variational principles & Noether](15-variational-principles-and-noether.md) | that dynamics needs equations rather than a functional: action, symmetries, constraints, symplectic transport, GENERIC |
| 16 | [Delay & retarded transport](16-delay-and-retarded-transport.md) | that the state is instantaneous: delay equations as transport along a characteristic, infinite spectra, delay-induced oscillations and patterns |

These three, plus [optimal transport & gradient flows](10-optimal-transport-and-gradient-flows.md), are what
the [universality part](../11-universality/index.md) leans on when it claims that the same structures govern
minds, markets, algorithms and pure mathematics.

