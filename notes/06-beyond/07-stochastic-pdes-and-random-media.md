---
title: Stochastic PDEs & random media
blurb: Transport with randomness inside the equation or inside the medium — Itô versus Stratonovich, effective coefficients, and new scaling laws.
depth: 4
tags: [SPDE, random media, Ito, KPZ, stochastic homogenisation]
---

# Stochastic PDEs & random media

> **One-line picture.** Two kinds of randomness: the medium's coefficients may be random fields, or the
> dynamics may be noise-driven. Both change the answer in ways that averaging coefficients cannot
> capture.
>
> **Prerequisites.** [random walks & Langevin](../01-foundations/08-random-walks-langevin-response.md) ·
> **Leads to.** [homogenisation & upscaling](08-homogenization-and-upscaling.md),
> [inverse problems & data assimilation](../07-numerics/10-inverse-problems-and-data-assimilation.md)

## L1 · Noise in the equation

* **Additive noise** — a fluctuating source (thermal, biological, observational).
* **Multiplicative noise** — the coefficient depends on the state, so the equation is not invariant
  under a change of variables and the **Itô and Stratonovich interpretations differ by a drift term**.
  State which you mean: the difference is physical, not philosophical.
* **Random coefficients (random media)** — $K(\mathbf x)$ or $D(\mathbf x)$ is a random field (e.g.
  log-normal hydraulic conductivity). The solution is random even with no time-dependent noise.

The central question for random media is what an effective coefficient *means*. It is defined by the
requirement that the **ensemble average** spreads diffusively, and it is generally **not** the average
of $K$: for log-normal fields the effective conductivity involves a geometric-type mean with variance
corrections, and the corrections grow with the medium's variability.

## L2 · Phenomena that exist only with randomness

Randomness does not merely add error bars; it creates **new scaling laws**.

* **KPZ surface growth**: $\partial_th=\nu\nabla^2h+\frac\lambda2|\nabla h|^2+\eta$ has universal
  exponents $1/3$ and $2/3$ — neither diffusion nor ballistic, and shared by flames, interfaces and
  bacterial colonies.
* **Stochastic advection–dispersion** with random $\mathbf u$ or $D$ gives non-Fickian plumes and
  heavy-tailed arrival times: the correct model is
  [anomalous transport](../03-microscopic/08-anomalous-diffusion.md), not a mis-measured $D$.
* **Dean's equation** shows hydrodynamic fluctuations generate long-range spatial correlations in
  density — fluctuations you might otherwise dismiss as noise.
* **Fluctuation–dissipation** ties the noise amplitude to the dissipative coefficient: you cannot
  choose temperature and diffusivity independently
  ([Langevin](../01-foundations/08-random-walks-langevin-response.md)).

## L3 · What the mathematics guarantees

* **Rough noise needs renormalisation.** Space–time white noise cannot be multiplied pointwise;
  nonlinear SPDEs such as KPZ require regularity structures/paracontrolled calculus to be well-defined.
  A modern analysis frontier with real physical content.
* **Itô vs Stratonovich** differ by a correction term of the form $\frac12\partial_cD$. Derive the
  convention from the physical limit (often Stratonovich for limits of physical processes; Itô for
  discrete-time and financial models), then stay consistent throughout the code.
* **Stochastic homogenisation is a theorem.** For divergence-form operators with stationary ergodic
  coefficients an effective tensor exists, but computing it requires the random *corrector* field — the
  stochastic counterpart of the deterministic cell problem
  ([homogenisation](08-homogenization-and-upscaling.md)).
* **Uncertainty in the answer is not uncertainty in the medium.** Averaged output is dominated by rare
  high-conductivity paths (percolation) or by rare low-conductivity barriers, so first-order
  perturbation theory can be qualitatively wrong.

## L4 · Numerics

* **Monte Carlo over realisations** is the baseline; multi-level and quasi-Monte Carlo reduce the
  $N^{-1/2}$ cost ([particle methods](../07-numerics/09-particle-and-monte-carlo-methods.md)).
* **Declare strong or weak convergence**: trajectory-accurate (strong) needs Itô–Taylor/Milstein; statistics
  (weak) needs cheaper schemes.
* **Random-field generation matters**: Gaussian fields by FFT or Karhunen–Loève; if the correlation
  length is under-resolved, the effective coefficient you measure is wrong.
* **Benchmarks**: 1-D log-normal aquifer arrival times, KPZ exponent recovery, and Itô/Stratonovich
  consistency tests ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Uncertainty quantification for transport prediction; data assimilation in random
  media; score-based generative models as reverse-time SPDEs
  ([ML & data](../08-bridges/07-machine-learning-and-data.md)).

## Checks

1. Why is the effective conductivity not the arithmetic mean? *(You average fluxes, not coefficients:
   harmonic/geometric-type means appear, with variance corrections.)*
2. What is the practical consequence of the Itô/Stratonovich choice? *(A drift correction that changes
   the mean transport.)*
3. Why is white-in-time nonlinear noise hard to define? *(Pointwise products of rough distributions are
   undefined; renormalisation is needed.)*

## See also

[Random walks, Langevin & response](../01-foundations/08-random-walks-langevin-response.md) ·
[Homogenisation & upscaling](08-homogenization-and-upscaling.md) ·
[Anomalous diffusion](../03-microscopic/08-anomalous-diffusion.md) ·
[Inverse problems & data assimilation](../07-numerics/10-inverse-problems-and-data-assimilation.md)
