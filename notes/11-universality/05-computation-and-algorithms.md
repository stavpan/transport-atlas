---
title: Computation & algorithms
blurb: Dijkstra as Hamilton–Jacobi, PageRank as diffusion, gradient descent as a gradient flow, sampling as transport of measures — and why that is useful.
depth: 3
tags: [algorithms, Hamilton-Jacobi, graph-diffusion, SGD, MCMC, diffusion-models]
---

# Computation & algorithms

> **One-line picture.** Many of the algorithms you already use are discretisations of transport equations —
> shortest paths are arrival-time fields, PageRank is a stationary density, training is a gradient flow, and
> sampling is transport of a measure. Reading them that way gives you convergence rates, stability theory and
> intuition for free.
>
> **Prerequisites.** [Hamilton–Jacobi & viscosity solutions](../06-beyond/02-hamilton-jacobi-and-viscosity-solutions.md),
> [Optimal transport & gradient flows](../06-beyond/10-optimal-transport-and-gradient-flows.md) ·
> **Leads to.** [Information, statistics & inference](07-information-statistics-and-inference.md),
> [Machine learning & data](../08-bridges/07-machine-learning-and-data.md)

## L1 · Three identities worth memorising

1. **Dijkstra = Hamilton–Jacobi.** The distance-to-goal field $T(\mathbf x)$ satisfies the eikonal equation
   $|\nabla T|=1/c$. Dijkstra's algorithm is a *monotone upwind sweep* — the discrete version of fast marching —
   and its correctness proof is the discrete maximum principle. A\* adds an admissible heuristic, which is a
   viscosity subsolution bound guiding the sweep.
2. **PageRank = diffusion.** The stationary distribution of a random walk with teleportation is the resolvent
   of a transport operator, $\pi\propto(I-\alpha P)^{-1}\mathbf 1$: teleportation is a source term, the damping
   factor is a mean free path, and personalised PageRank is the Green function of that operator.
3. **Training = gradient flow.** Gradient descent is $\dot\theta=-\nabla L$; stochastic gradient descent adds
   noise, giving a **Fokker–Planck equation for the distribution of parameters**; and momentum methods are
   second-order ODEs — accelerated methods are damped oscillators with a specific damping schedule.

## L2 · The lookup, algorithm by algorithm

| Algorithm | Transport form | What you get from the analogy |
|---|---|---|
| Dijkstra, A\*, fast marching, level sets | eikonal / Hamilton–Jacobi | monotonicity ⟹ correctness; upwind schemes; low CFL |
| graph diffusion, label propagation, consensus | heat equation on a graph | mixing time $\sim1/\lambda_2$; Cheeger bottlenecks |
| PageRank, personalised PageRank, Katz centrality | resolvent $(I-\alpha P)^{-1}$ | damping ⟹ finite memory; Green-function interpretation |
| Jacobi / Gauss–Seidel / SOR / multigrid | smoothing iterations for an elliptic operator | why multigrid wins (it is a mode-dependent filter) |
| gradient descent, Newton, momentum, Adam | gradient flow (+ noise, + inertia) | Lyapunov descent, stability limits, step-size rules |
| SGD, Langevin, stochastic optimisation | Fokker–Planck / Langevin | stationary distributions, escape rates, noise scale |
| Metropolis, Gibbs, HMC, NUTS | transport of measures with a target invariant density | mixing times, spectral gaps, symplectic structure |
| score-based / diffusion models, flow matching | forward noising SDE + reverse-time SDE / continuity equation | exact sampling by solving a transport equation |
| variational inference, ELBO, Wasserstein VI | KL gradient flow (Fisher–Rao or Wasserstein) | geometry-appropriate optimisers; convergence rates |
| belief propagation, message passing, GNNs | discrete transport of messages on a factor graph | convergence as a diffusion on the factor graph |
| dynamic programming, value iteration, RL | Bellman = discrete Hamilton–Jacobi; continuous RL = HJB | value functions as arrival-time-like fields |
| replicator dynamics, evolutionary algorithms | transport in frequency space with Fisher metric | natural-gradient structure; ESS, Fisher's theorem |
| queueing networks (M/M/1, heavy traffic) | birth–death master equation ⟹ reflected Brownian motion | heavy-traffic limit is a transport approximation |
| optimal transport, Sinkhorn, Wasserstein GAN | Monge–Kantorovich + entropic regularisation | geometry of distributions; convex formulations |
| attention in transformers | a *nonlocal* smoothing/conditional-expectation operator (kernel or OT interpretations proposed) | caution: an interpretation, not an identity |

## L3 · What the transport reading actually gives you

* **Convergence rates become spectral statements.** Mixing time of a Markov chain $\sim1/\lambda_2$ of the
  graph Laplacian; the Cheeger inequality bounds it by bottlenecks; gradient-flow convergence follows from
  strong convexity, and *sampling* rates from log-Sobolev and Poincaré inequalities. So "convergence proofs" in
  optimisation and sampling are transport theorems in disguise
  ([entropy & variational structure](../01-foundations/07-entropy-and-variational-structure.md)).
* **Monotonicity gives correctness.** Monotone, consistent discretisations of Hamilton–Jacobi converge to the
  viscosity solution ([HJ](../06-beyond/02-hamilton-jacobi-and-viscosity-solutions.md)) — which is exactly why
  Dijkstra-style sweeps are correct, why fast marching works, and why an *inadmissible* heuristic in A\* breaks
  optimality.
* **Stability limits are CFL conditions.** Step-size limits, momentum stability regions and "learning-rate
  warm-up" are the same phenomena as in explicit integration of stiff equations: the fast modes set the step,
  and the slow physics sets the timescale you care about
  ([CFL & stiffness](../07-numerics/02-cfl-stiffness-and-time-integration.md)).
* **Samplers are transport with an invariant measure.** MCMC/Langevin convergence is the statement that the
  empirical measure is transported into the target; HMC works *because* of symplectic structure, so changing
  the integrator changes the algorithm's validity
  ([variational principles & Noether](../06-beyond/15-variational-principles-and-noether.md)).
* **Honest caveat — no free lunch.** NP-hardness is combinatorial. Nothing in this note makes hard problems
  easy; the transport reading makes them *interpretable*, sometimes gives rates, and reliably supplies good
  diagnostics. When the continuous limit is poor (small graphs, few samples, strong heterogeneity), discrete
  structure dominates — the computational version of the
  [Knudsen condition](01-why-everything-flows.md).

## L4 · Practice

* **Design from the continuum limit, then verify at the discrete level.** Choose step sizes, dampings and
  scheduling from the continuum stability analysis, then confirm empirically — the scaling is usually right and
  the constants usually need calibration.
* **Preserve the structure you rely on**: flux-form/mass-conserving updates for diffusion solvers, symplectic
  integrators for HMC, monotone updates for arrival-time fields, doubly-stochastic transitions when you need
  uniform stationarity.
* **Use transport diagnostics in the loop**: effective spectral gap by power iteration; residual history for
  elliptic solvers; ESS and autocorrelation for samplers; energy/loss Lyapunov monitoring for training — a
  sudden loss spike is the discrete analogue of a violated energy inequality, not bad luck.
* **Implement with the right tools**: graph Laplacians via sparse Cholesky or AMG; fast marching on grids and
  meshes for eikonal problems; FFT for translation-invariant kernels and convolution quadrature for memory;
  sparse OT/Sinkhorn with entropic regularisation for distribution-valued objectives.
* **Benchmarks**: mixing times on graphs against $\lambda_2$ predictions; eikonal test media with analytic
  travel times; density estimation against exact 1-D transport; sampler accuracy versus solver step count;
  solver-versus-spectral-method comparisons on the same PDE.

## Checks

1. Why is Dijkstra's algorithm correct — in transport language? *(It is a monotone upwind scheme for the eikonal
   equation; monotone, consistent schemes converge to the viscosity solution.)*
2. What is the transport interpretation of PageRank's damping factor? *(A finite mean free path: the resolvent
   $(I-\alpha P)^{-1}$ truncates the walk's memory, giving a well-defined stationary density.)*
3. Why does momentum help, in equation language? *(It turns first-order descent into a damped second-order
   oscillator, whose damping schedule sets the convergence rate.)*
4. When does the continuous-limit intuition fail? *(Small graphs, few samples, strong heterogeneity — when
   discrete structure, not transport geometry, governs behaviour.)*

## See also

[Hamilton–Jacobi & viscosity solutions](../06-beyond/02-hamilton-jacobi-and-viscosity-solutions.md) ·
[Optimal transport & gradient flows](../06-beyond/10-optimal-transport-and-gradient-flows.md) ·
[Information, statistics & inference](07-information-statistics-and-inference.md) ·
[Machine learning & data](../08-bridges/07-machine-learning-and-data.md) ·
[Networks, society & traffic](../08-bridges/09-networks-society-and-traffic.md)

