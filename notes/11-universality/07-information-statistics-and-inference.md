---
title: Information, statistics & inference
blurb: Bayesian updating as transport of measures, the Fisher–Rao geometry that makes natural gradient work, and large deviations as Hamilton–Jacobi.
depth: 4
tags: [information-geometry, Fisher, Bayes, large-deviations, Kalman, fluctuation]
---

# Information, statistics & inference

> **One-line picture.** Inference is transport of a *measure over hypotheses*: Bayes reweights it, filtering
> evolves it continuously, large deviations transport it into rare corners — and the space it moves in has a
> metric (Fisher–Rao) that is not a choice but a theorem.
>
> **Prerequisites.** [Information & statistics bridge](../08-bridges/07-machine-learning-and-data.md),
> [Optimal transport & gradient flows](../06-beyond/10-optimal-transport-and-gradient-flows.md) ·
> **Leads to.** [Computation & algorithms](05-computation-and-algorithms.md),
> [Limits of the claim](09-limits-of-the-claim.md)

## L1 · Two transport pictures of inference

1. **The measure picture.** A belief state is a probability measure over hypotheses; updating it is a
   *transport*: conditioning reweights (a measure-theoretic operation), sequential updating composes, and in
   continuous time the conditional measure solves a stochastic transport equation. Filtering is therefore a PDE
   for a measure, with observation noise as a source and drift as information flow.
2. **The geometry picture.** The set of distributions is a Riemannian manifold whose metric — the
   **Fisher information** — is *forced* by invariance requirements (Čencov's theorem). Distance in that metric
   measures statistical distinguishability; steepest descent in it is the **natural gradient**; and information
   *is* a metric, not a mere number.

Both pictures are transport statements, and both are used in practice: the first in filtering and data
assimilation, the second in optimisation and in every modern variational-inference algorithm.

## L2 · The structures

| Object | Transport structure | Content |
|---|---|---|
| Bayes' rule | reweighting of a measure (a change of measure) | posterior $\propto$ likelihood $\times$ prior; composition of transport maps |
| sequential Bayesian updating | flow of a measure; in continuous time the Kushner–Stratonovich/Zakai equations | nonlinear filtering as a stochastic PDE for the posterior |
| Kalman filter | exact Gaussian transport of the conditional measure | Riccati equation = transport of the covariance |
| variational inference / ELBO | KL gradient flow (Wasserstein or Fisher–Rao) | free-energy descent; mode-seeking caveats |
| Fisher information | metric on the space of distributions | Čencov uniqueness; Cramér–Rao bound $\mathrm{Var}\ge1/I(\theta)$ |
| natural gradient | gradient flow in Fisher–Rao geometry | parameterisation-invariant learning (KFAC, Shampoo) |
| maximum entropy | variational principle with a constraint | exponential families; conjugate duality |
| large deviations (Sanov) | rare event probabilities $\sim e^{-N\,\mathrm{KL}}$ | empirical measures converge by transport into atypical sets |
| Freidlin–Wentzell | small-noise diffusion exit | the rate function solves a **Hamilton–Jacobi** equation (vanishing viscosity) |
| fluctuation theorems | exact identities for entropy production | Jarzynski, Crooks; free-energy estimation from non-equilibrium work |
| Landauer's principle | erasure cost of information | information is physical: deletion dissipates |
| rate–distortion | constrained transport of a source distribution | Shannon's trade-off; Blahut–Arimoto akin to Sinkhorn iterations |
| PAC-Bayes, information bottleneck | KL-penalised transport objectives | generalisation and compression as transport costs |

The deepest bridge here is **large deviations = Hamilton–Jacobi**: the small-noise limit of a Fokker–Planck
equation is a Hamilton–Jacobi equation for the rate function, so probability theory's rare-event asymptotics and
the eikonal/arrival-time calculus are the same mathematics
([Hamilton–Jacobi](../06-beyond/02-hamilton-jacobi-and-viscosity-solutions.md)). That is also why WKB and
semiclassical physics share formulas with statistics.

## L3 · What is a theorem, what is a model

* **The geometry is forced.** Čencov's theorem: the Fisher metric is the only Riemannian metric on the space of
  distributions (up to scale) invariant under sufficient statistics. So information geometry is not a stylistic
  choice, and "natural gradient" is *the* parameterisation-invariant descent direction.
* **Accuracy has a geometric bound.** Cramér–Rao: $\mathrm{Var}(\hat\theta)\ge1/I(\theta)$. Maximum-likelihood
  estimators attain it asymptotically under regularity — accuracy limits are statements about curvature of the
  statistical manifold.
* **Filtering: one exact case, one hard case.** For linear-Gaussian models the Kalman filter is *exactly* optimal
  and the Riccati equation transports the covariance; the general nonlinear filtering problem is
  infinite-dimensional and intractable, so practical filters are approximations with known failure modes
  (divergence, particle degeneracy, curse of dimensionality).
* **Rare events are Hamilton–Jacobi.** Sanov's theorem (empirical measures) and Freidlin–Wentzell (small-noise
  exits) give *exact exponential rates*, and their rate functions solve Hamilton–Jacobi equations. The corollary
  is the profound one: the "cost" of an atypical outcome is a Kullback–Leibler distance — information and
  probability unified by a variational problem.
* **Non-equilibrium identities are exact — and treacherous.** Jarzynski's and Crooks' theorems hold exactly for
  any protocol, but the exponential average is dominated by rare trajectories, so estimates have enormous
  variance unless the protocol is slow or carefully designed. There is a genuine theory here: **thermodynamic
  length** is a Riemannian metric on state space, and minimum-dissipation protocols are geodesics — optimal
  control and transport geometry in the same statement.
* **Bayesian asymptotics are transport statements.** Under regularity the posterior concentrates at the true
  parameter (Bernstein–von Mises); under *misspecification* it concentrates on the Kullback–Leibler projection
  onto the model class — inference transports belief to the nearest distribution in information geometry, which
  is why misspecified models still "converge", just to the wrong place.
* **Priors are measures, and measures are geometry.** A prior is a choice of volume element; Jeffreys' prior is
  the Fisher volume element (invariant), while naive flat priors are not invariant under reparameterisation.
  The Lindley paradox and prior-sensitivity debates are downstream of this — a modelling choice, stated plainly.

## L4 · Practice

* **Natural gradient**: compute Fisher–vector products, use KFAC/Shampoo-style block approximations, and remember
  that Adam is a diagonal heuristic rather than a true Fisher method. Damp the Fisher when it is singular, and
  say which Fisher (empirical vs true) you used.
* **Filtering**: below ~10 dimensions particle filters are fine; above, use ensemble methods with localisation,
  or variational data assimilation. Degeneracy and divergence are common enough to deserve diagnostics
  ([data assimilation](../07-numerics/10-inverse-problems-and-data-assimilation.md)).
* **Variational inference**: $\mathrm{KL}(q\|p)$ is mode-seeking and underestimates variance; $\alpha$-divergences
  or Jeffreys-style objectives trade coverage; Wasserstein VI gives geometry-appropriate behaviour. Always report
  posterior *coverage*, not just point accuracy.
* **Rare events**: importance sampling with annealed proposals, splitting methods, forward flux sampling. The
  optimal exponential tilt is a KL projection (Csiszár's I-projection), so the numerics of rare events and the
  geometry of information are the same computation.
* **Free-energy estimation from non-equilibrium work**: use BAR/MBAR rather than plain Jarzynski, and design
  protocols with thermodynamic length in mind if you can.
* **Benchmarks**: Cramér–Rao versus empirical estimator variance; Kalman versus exact linear-Gaussian posteriors;
  Sanov rate versus simulated rare-event frequency; Jarzynski versus free-energy perturbation as a function of
  protocol length; posterior coverage tests.

## Checks

1. Why is the Fisher metric "the" geometry of statistical inference? *(Čencov's invariance theorem: it is the
   unique metric invariant under sufficient statistics.)*
2. What does the small-noise limit of a Fokker–Planck equation give, and why does that matter for statistics?
   *(A Hamilton–Jacobi equation for the rate function — the exact exponential cost of rare events, e.g. Sanov's
   $N\,\mathrm{KL}$.)*
3. Under model misspecification, to what does the posterior converge? *(To the KL projection of the truth onto
   the model class — the nearest distribution in information-geometric distance.)*
4. Why is Jarzynski's equality hard to use numerically? *(The exponential average is dominated by rare
   low-work trajectories; variance explodes for fast protocols — which is why optimal/geodesic protocols and
   BAR-type estimators exist.)*

## See also

[Computation & algorithms](05-computation-and-algorithms.md) ·
[Optimal transport & gradient flows](../06-beyond/10-optimal-transport-and-gradient-flows.md) ·
[Inverse problems & data assimilation](../07-numerics/10-inverse-problems-and-data-assimilation.md) ·
[Machine learning & data](../08-bridges/07-machine-learning-and-data.md) ·
[Limits of the claim](09-limits-of-the-claim.md)

