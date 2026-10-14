---
title: Inverse problems & data assimilation
blurb: Getting parameters out of data — ill-posedness, regularisation, adjoints, Kalman filters, and the discipline of admitting uncertainty.
depth: 4
tags: [inverse problem, Tikhonov, adjoint, Kalman, 4D-Var, Bayesian]
---

# Inverse problems & data assimilation

> **One-line picture.** Forward problems smooth; inverse problems amplify. Every measurement noise
> becomes a reconstruction artefact unless you regularise — and every claim needs an uncertainty.
>
> **Prerequisites.** [PDE taxonomy & well-posedness](../01-foundations/04-pde-taxonomy-and-boundary-conditions.md) ·
> **Leads to.** [machine learning & operator learning](11-machine-learning-and-operator-learning.md),
> [measurement & experiments](../10-appendix/05-measurement-and-experiments.md)

## L1 · Why inversion is hard

Determining $D(\mathbf x)$, a source term, or an initial condition from concentration measurements is
typically **ill-posed**: small data errors produce large parameter errors, many parameter fields explain
the data equally well, and the solution may not depend continuously on the data. Classic demonstration:
the backward heat equation, which is the Fourier face of ill-posedness
([spectral view](../01-foundations/06-spectral-and-green-function-view.md)).

The practical consequences in transport are well known: fitting a dispersion coefficient to a
preasymptotic plume gives a length-dependent "coefficient"; fitting a Soret coefficient without
controlling for Dufour gives a mixture.

## L2 · The main approaches

| Approach | Formulation | Typical use |
|---|---|---|
| Tikhonov / ridge | $\min\|A\mathbf m-\mathbf d\|^2+\lambda\|\mathbf m-\mathbf m_0\|^2$ | smooth parameter fields |
| total variation | $\ell^1$ of gradients | sharp interfaces (layered media) |
| truncated SVD / L-curve | discard small singular directions | diagnosing resolution |
| adjoint gradient descent | compute $\nabla_{\mathbf m}J$ by solving one adjoint PDE | large-scale inversion, 4D-Var |
| ensemble Kalman (EnKF) | propagate an ensemble, update with data | sequential data assimilation |
| particle filter | weighted samples of the posterior | strongly nonlinear dynamics |
| Bayesian MCMC / variational inference | posterior $p(\mathbf m\vert \mathbf d)$ | full uncertainty quantification |
| deep-learning surrogates | amortise the forward solve | real-time control, repeating inversions |

**Adjoint methods** deserve emphasis: one linear solve of the adjoint equation gives the gradient of the
objective with respect to *all* parameters — the reason industrial reservoir and atmospheric inversions
are feasible at all. They also expose the same numerical hazards as the forward problem (see below).

## L3 · What the mathematics guarantees

* **Regularisation restores well-posedness**, and the choice of $\lambda$ encodes prior information: it is
  a modelling decision, not a numerical knob.
* **Resolution analysis is possible and necessary**: the resolution matrix $R$ (how much of each true
  parameter appears in the estimate) and the model covariance tell you what the data can and cannot
  resolve. Report them.
* **Adjoints invert the *discrete* equations, not the PDE**: a nonconservative forward scheme produces a
  biased gradient. Code the adjoint of the code, and verify gradients against finite differences.
* **Uncertainty quantification needs a prior and a likelihood**: point estimates without intervals are
  not scientific claims, especially for exponential sensitivities (Arrhenius, Kramers escape).

## L4 · Practicalities

* **Always verify the gradient** (Taylor test / finite-difference check) before running a large
  optimisation; gradient errors are the most common cause of "the inversion does not work".
* **Choose the regulariser by the physics**: layered media and fractures need sparsity-promoting
  penalties, not smoothness.
* **Multi-scale and gradient-based coarse-to-fine strategies** beat brute-force inversion for
  heterogeneous fields.
* **Report predictive uncertainty** by propagating the posterior through the forward model, not by
  quoting the parameter uncertainty alone.
* **Benchmarks**: the 1-D tracer column inversion, the Henry problem parameter identification, and
  standard 4D-Var/EnKF testbeds (Lorenz-63/96)
  ([V&V](12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Physics-informed and operator-learning surrogates inside inversion loops; inversion of
  unstable systems ("inverting the arrow of time" with learned priors); joint inversion of coupled
  physics (heat, mass, mechanics).

## Checks

1. Why does fitting a Fickian $D$ to a preasymptotic plume give a length-dependent coefficient? *(The
   model is wrong in that regime: the fit absorbs the model error into the parameter.)*
2. What does one adjoint solve give you? *(The gradient of the objective with respect to all parameters.)*
3. Why must the adjoint match the discrete forward scheme? *(Otherwise the computed gradient is not the
   gradient of the discrete objective, and optimisation stalls.)*

## See also

[Measurement & experiments](../10-appendix/05-measurement-and-experiments.md) ·
[Machine learning & operator learning](11-machine-learning-and-operator-learning.md) ·
[Sorption & retardation](../04-interaction/07-sorption-and-retardation.md) ·
[Wells, injection & breakthrough](../04-interaction/12-wells-injection-efflux-and-breakthrough.md)
