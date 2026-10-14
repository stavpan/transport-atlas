---
title: One mathematics of transport
blurb: The closing argument — continuity equations on measure spaces, gradient flows, semigroups and entropy, and why all the notes in this atlas are the same note.
depth: 4
tags: [unifying, measure, semigroup, gradient flow, entropy, Wasserstein]
---

# One mathematics of transport

> **One-line picture.** Every equation in this atlas is a continuity equation for something. Add a
> constitutive law, a metric and an entropy, and you have specified which *kind* of transport you mean.
>
> **Prerequisites.** the whole atlas, but especially
> [balance laws](../01-foundations/01-balance-laws-and-flux.md),
> [entropy & variational structure](../01-foundations/07-entropy-and-variational-structure.md),
> [optimal transport](../06-beyond/10-optimal-transport-and-gradient-flows.md)

## L1 · The common skeleton

**Level 1 — the balance law.** $\partial_tc+\nabla\cdot\mathbf J=f$. Exact, universal, geometry-free.

**Level 2 — the constitutive law.** $\mathbf J$ as a function of the state: Fick, Fourier, Newton, Darcy,
Ohm, Maxwell–Stefan, kinetic moments, or a memory integral. This step is where physics, empirical
parameters and *all* the error enter.

**Level 3 — the structure.** The same balance law with different structures gives qualitatively different
phenomena:

| Structure | Equation class | Behaviour |
|---|---|---|
| dissipation $+$ gradient law | parabolic | smoothing, maximum principle, entropy up |
| transport $+$ nonlinear flux | hyperbolic | shocks, entropy condition, finite speed |
| transport $+$ elliptic constraint | mixed | boundary layers, projection methods |
| nonlocal kernel | integro-differential | jumps, long range, new boundary conditions |
| memory kernel | Volterra / fractional | relaxation, ageing, non-exponential decay |
| variational inequality | complementarity | switching, active sets, hysteresis |
| stochastic | SDE/SPDE | fluctuation, scaling laws, rare events |

## L2 · The unifying objects

* **The continuity equation on measure space.** $\partial_t\mu+\nabla\cdot(\mu\mathbf v)=0$ makes sense for
  densities, dirac masses, empirical measures and graph measures alike — which is why discrete, continuum
  and stochastic transport share theorems.
* **Semigroups and generators.** Each transport equation defines a semigroup $e^{t\mathcal L}$; the
  generator $\mathcal L$ is the operator, and its spectral properties (spectral gap, decay rates) give the
  long-time behaviour ([spectral view](../01-foundations/06-spectral-and-green-function-view.md)).
* **Entropy and free energy.** A Lyapunov functional supplies stability, uniqueness and the large-time
  limit. Gradient-flow structure in the *right metric* is what makes the entropy decrease meaningful, and
  the metric is the physics: $L^2$, $H^{-1}$, or Wasserstein
  ([optimal transport](../06-beyond/10-optimal-transport-and-gradient-flows.md)).
* **Green–Kubo and Mori–Zwanzig.** Microscopic transport coefficients are equilibrium correlations;
  eliminating fast variables produces memory kernels and noise, which is why every "effective" model is an
  approximation of a projection ([linear response](../01-foundations/09-linear-response-and-memory.md)).
* **Asymptotic limits.** Kinetic → fluid (Chapman–Enskog), local → nonlocal (horizon → 0), stochastic →
  deterministic (law of large numbers), hyperbolic → parabolic (relaxation → 0). Most of the apparent
  diversity in this atlas collapses into a handful of such limits.

## L3 · The recurring trade-off

Everything practical in transport is the same trade:

$$\text{resolution} \;\longleftrightarrow\; \text{closure} \;\longleftrightarrow\; \text{cost}.$$

* Resolve the small scales: DNS, molecular dynamics, pore-scale simulation, direct kinetic solvers.
* Close them: eddy diffusivity, upscaled coefficients, effective reactions, memory kernels, learned
  closures.
* Pay the price somewhere: cost, accuracy, generality, or the validity range.

The dimensionless numbers tell you which branch you are on; the entropy inequality tells you which
closures are legal; and verification tells you whether you implemented it correctly.

## L4 · How to use this atlas

1. **Identify the conserved quantity**, then the flux law — that fixes the equation.
2. **Compute the dimensionless numbers** to learn which term dominates
   ([cards](../10-appendix/02-dimensionless-number-cards.md)).
3. **Find the structure** (parabolic, hyperbolic, nonlocal, variational, stochastic) to know which theorems
   and methods apply ([operator catalogue](../10-appendix/03-operator-and-equation-catalog.md)).
4. **Choose the scheme from the structure + regime**, not from habit
   ([discretisation](../07-numerics/01-discretization-consistency-stability-convergence.md)).
5. **Verify, then validate** ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).

## Checks

1. Name the three levels of the skeleton and say which one carries the physics. *(Balance law — universal;
   constitutive law — physics and error; structure — which theorems apply.)*
2. Why can the same equation be diffusion in one metric and transport in another? *(Because "steepest
   descent" depends on how you measure distance between states.)*

## See also

[Balance laws & flux](../01-foundations/01-balance-laws-and-flux.md) ·
[Entropy & variational structure](../01-foundations/07-entropy-and-variational-structure.md) ·
[Optimal transport & gradient flows](../06-beyond/10-optimal-transport-and-gradient-flows.md) ·
[Operator & equation catalogue](../10-appendix/03-operator-and-equation-catalog.md)
