---
title: Machine learning & operator learning
blurb: Where learning genuinely helps transport modelling — PINNs, neural operators, learned closures — and where it quietly fails.
depth: 4
tags: [PINN, neural operator, FNO, DeepONet, learned closure, surrogate]
---

# Machine learning & operator learning

> **One-line picture.** Learning can approximate solution *operators*, accelerate expensive sub-models, or
> discover closures — but transport has structural properties (conservation, positivity, causality) that
> a naive network will happily violate.
>
> **Prerequisites.** [inverse problems & data assimilation](10-inverse-problems-and-data-assimilation.md) ·
> **Leads to.** [machine learning & data bridges](../08-bridges/07-machine-learning-and-data.md),
> [verification & benchmarks](12-verification-validation-and-benchmarks.md)

## L1 · Four distinct uses (do not blur them)

| Use | What is learned | Example |
|---|---|---|
| **Surrogate / emulator** | map from parameters to outputs | replace a reservoir simulator in an optimisation loop |
| **Operator learning** | map from *functions* to functions (PDE solution operators) | DeepONet, Fourier Neural Operator (FNO), graph neural operators |
| **Physics-informed solving** | the solution itself, constrained by residuals | PINNs for inverse problems with sparse data |
| **Closure / subgrid modelling** | unresolved terms from resolved ones | turbulence, subgrid dispersion, kinetic closures |

These have very different accuracy requirements: surrogates need interpolation accuracy, operator learners
need generalisation across parameter families, closures need *structural* consistency (conservation,
realisability) — the hardest bar.

## L2 · What works, and what does not

**Works well:**
* Spectral-bias-free representations for smooth operator families (FNO-type models) on regular grids.
* Acceleration of repeated many-query problems: design optimisation, UQ, control, real-time forecasting.
* Learned closures *with* hard physical constraints: divergence-free architectures, conservative
  parameterisations, or learning the *correction* to a trusted closure.

**Works poorly (or requires care):**
* Extrapolation to unseen regimes (a network trained at $\mathrm{Re}=10^3$ does not know turbulence at
  $10^6$).
* Translation-dominated advection: generic architectures struggle with the exact translation symmetry
  that characteristics-based methods give for free
  ([advection](../02-bulk/01-advection.md)).
* Long-horizon rollouts: small errors compound; energy can grow or decay spuriously unless the model is
  structurally stable.
* Sharp fronts and shocks: spectral bias smooths what must remain discontinuous — combine with limiters
  or characteristic-aware layers ([limiters](04-limiters-tvd-and-weno.md)).

## L3 · What the mathematics guarantees (and does not)

* **Universal approximation is not generalisation.** Approximating on the training distribution says
  nothing about behaviour outside it; error bounds for operator learning exist but require assumptions on
  the operator family.
* **Symmetry and conservation must be built in.** Equivariant/graph architectures and constrained losses
  help; hard constraints (projection to divergence-free fields, conservative flux forms) help more.
* **PINNs are an inverse-problem tool**, not a replacement for solvers: they shine with sparse data and
  unknown parameters, and struggle with stiff, multiscale or high-frequency transport unless the
  architecture encodes the asymptotics.
* **Data assimilation meets learning**: learned models act as priors/regularisers in inversion, which is
  why the same "residual + data" loss appears in both communities
  ([inverse problems](10-inverse-problems-and-data-assimilation.md)).

## L4 · Practicalities

* **Judge by extrapolation, stability and conservation**, not by offline test error: report long rollouts,
  mass/energy drift, and performance on a held-out physical regime.
* **Structure-preserving hybridisation** is the pragmatic route: keep the trusted solver, learn the
  expensive or under-resolved piece, and enforce the invariants explicitly.
* **Data efficiency**: use simulation-generated data, exploit symmetries, and start from a numerical
  baseline so the network learns a correction rather than the whole physics.
* **Benchmarks**: Burgers, Darcy flow with random coefficients, Navier–Stokes at moderate $\mathrm{Re}$,
  and turbulence closures with reported *a posteriori* metrics
  ([V&V](12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Learned closures that provably respect the second law; operator learning on unstructured
  meshes and spheres; differentiable simulation; foundation models for multiphysics.

## Checks

1. Why do generic networks struggle with advection? *(Exact translation symmetry is hard to represent;
   characteristics-aware designs or spectral layers are needed.)*
2. What must a learned turbulence closure preserve to be usable? *(Conservation, realisability and
   correct scaling — otherwise long simulations drift.)*

## See also

[Machine learning & data](../08-bridges/07-machine-learning-and-data.md) ·
[Inverse problems & data assimilation](10-inverse-problems-and-data-assimilation.md) ·
[Operator & equation catalogue](../10-appendix/03-operator-and-equation-catalog.md)
