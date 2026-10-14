---
title: Homogenisation & upscaling
blurb: Turning a messy microstructure into an effective law — cell problems, volume averaging, and the price of forgetting small scales.
depth: 3
tags: [homogenisation, upscaling, cell problem, effective medium, tortuosity]
---

# Homogenisation & upscaling

> **One-line picture.** If the microstructure is far finer than the question, replace it with one
> effective coefficient — computed from a *cell problem*, not from an average.
>
> **Prerequisites.** [porous media & Darcy](../02-bulk/08-porous-media-and-darcy.md) ·
> **Leads to.** [subsidence & poroelasticity](../04-interaction/13-subsidence-and-poroelasticity.md),
> [stochastic PDEs](07-stochastic-pdes-and-random-media.md)

## L1 · The idea and the small parameter

Rock, laminates, fabrics, battery electrodes: structure at scale $\ell\ll L$. Upscaling finds a
device-scale equation whose solution is the *average* of the true solution. The expansion parameter is
$\epsilon=\ell/L$.

* **Two-scale asymptotics** postulates $c(\mathbf x,\mathbf y)$ with $\mathbf y=\mathbf x/\epsilon$. The
  leading orders force the solution to be $\mathbf y$-independent; the next order gives the **cell
  problem** on a periodic cell and, from its solvability, the effective coefficient.
* **Volume averaging** averages the pore-scale equations over a representative elementary volume and
  closes them by assuming deviations are proportional to the macroscopic gradient.

For diffusion this yields $D_{\rm eff}$ from
$\nabla_{\mathbf y}\!\cdot\!\big(D(\mathbf y)(\mathbf e_i+\nabla_{\mathbf y}\chi_i)\big)=0$ with
periodic boundary conditions and corrector fields $\chi_i$. The same machinery yields Darcy's
permeability tensor, effective elastic moduli, and effective reaction rates inside reactive zones.

## L2 · What gets upscaled

| Micro-structure | Effective law | How |
|---|---|---|
| straight pores | Fick with $D_{\rm eff}=D\theta/\tau$ | tortuosity $\tau$, porosity $\theta$ |
| layered media | vector/tensor diffusion | arithmetic along layers, harmonic across |
| periodic geometry | tensor coefficient | cell problem |
| random log-normal media | corrected coefficient | stochastic homogenisation |
| fractures + matrix | two-domain (mobile/immobile) | exchange coefficient, hence memory |

**Double porosity** is the instructive case: when a fast pathway (fractures) coexists with a slow one
(matrix), the upscaled model is not a single advection–dispersion equation but a two-domain system with
an exchange term — exactly the memory structure that
[Mori–Zwanzig](../01-foundations/09-linear-response-and-memory.md) predicts when a slow subscale is
eliminated.

## L3 · What the mathematics guarantees

* **Convergence needs separation and ergodicity**, not merely "small": periodic homogenisation is a
  theorem, and stochastic homogenisation needs stationarity; without these, no effective coefficient
  exists.
* **Effective coefficients are not averages.** Across barriers the harmonic-type mean governs; along
  channels the arithmetic-type mean does. Confusing the two is the classic upscaling error.
* **Eliminating a subscale creates structure**: memory kernels, exchange fluxes and (with randomness)
  noise — not just a coefficient.
* **Validity is asymptotic in the *question*.** Upscaled models answer large-scale questions; the
  preasymptotic regime (transition between scales) is precisely where models and field data disagree.
* **Below the RVE size or a percolation threshold, no effective property exists** — properties
  fluctuate with the sample, which is why laboratory cores and field values often "disagree".

## L4 · Numerics

* **Compute correctors, not averages**, and validate with analytical bounds (Wiener, Hashin–Shtrikman).
* **Asymptotically compatible schemes** are mandatory for nonlocal/peridynamic upscaling
  ([nonlocal operators](03-nonlocal-and-fractional-operators.md)).
* **FE² (two-scale FE)** nests micro-solves inside macro elements: accurate, expensive, and an active
  target for surrogate and learned models
  ([ML & operator learning](../07-numerics/11-machine-learning-and-operator-learning.md)).
* **Benchmarks**: layered-media conductivity, periodic cell problems with analytic answers, and
  double-porosity breakthrough against a fine-scale reference
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Preasymptotic upscaling; upscaling with reactions and feedback that change the
  microstructure; upscaled geomechanics and multiphase flow.

## Checks

1. Why can an effective coefficient exceed the arithmetic mean of the constituents? *(Channel-like
   microstructure: fast paths dominate.)*
2. What does eliminating a slow subscale introduce? *(Memory/exchange terms, and noise in random media.)*
3. When does no effective property exist? *(Below the RVE size, or below a percolation threshold.)*

## See also

[Porous media & Darcy](../02-bulk/08-porous-media-and-darcy.md) ·
[Shear dispersion (Taylor–Aris)](../02-bulk/06-shear-dispersion-taylor-aris.md) ·
[Stochastic PDEs & random media](07-stochastic-pdes-and-random-media.md) ·
[Linear response & memory](../01-foundations/09-linear-response-and-memory.md)
