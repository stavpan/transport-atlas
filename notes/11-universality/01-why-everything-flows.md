---
title: Why everything flows
blurb: The rigorous core of the universality claim — five structures, what each one is a theorem about, and what it silently assumes.
depth: 4
tags: [universality, continuity, semigroup, gradient flow, optimal control, renormalisation]
---

# Why everything flows

> **One-line picture.** Five structures, and almost every quantitative model of change has at least one of
> them: a *balance* of a countable quantity, a *generator* of a random process, a *functional* that is
> being minimised, an *optimality* principle, or a *symmetry*. Each yields a transport equation, and the
> rest of the atlas applies.
>
> **Prerequisites.** [Balance laws & flux](../01-foundations/01-balance-laws-and-flux.md),
> [Entropy & variational structure](../01-foundations/07-entropy-and-variational-structure.md) ·
> **Leads to.** [The translation lookup](../11-universality/02-decision-tree-and-lookup.md),
> [Limits of the claim](../11-universality/09-limits-of-the-claim.md)

## L1 · The claim, stated so that it can be checked

The honest version of "everything can be described by this mathematics" is:

> **If you can name a quantity, and account for every change in it as movement across boundaries plus
> creation/destruction, then you have a transport model. If in addition the movement is driven by a
> random process, a potential, an entropy, an optimality principle or a symmetry, then you have one of
> the five standard *types* of transport model — with classification, well-posedness theory, error
> analysis and universality classes already worked out.**

That is a statement about *models*, not about the world, and it is decidable in each case: either you can
write the balance, the generator, the functional, the objective or the symmetry — or you cannot. When you
can, this atlas is your toolbox. When you cannot, [note 9](../11-universality/09-limits-of-the-claim.md)
says why.

The striking part is how often you can. Density of cars on a road, probability of a belief, calcium ions
in a spine, wealth in a population, sentences in a corpus, packets in a router, neurons in a field of
thousands, eigenvalues of a random matrix, energy in a climate model, information in a business
forecast — all of them have been *written down* in one of the five forms, and each time the mathematics
transferred wholesale.

## L2 · The five universal structures

| # | Structure | What you supply | What you get | Family |
|---|---|---|---|---|
| 1 | **Balance / continuity** | a countable quantity + local exchange | $\partial_t\mu+\nabla\!\cdot\!(\mu\mathbf v)=\sigma$ (measure-valued) | advection, dispersion, conservation laws, population balances |
| 2 | **Generator of a random process** | transition rules (jump, diffuse, or both) | forward equation for the law: master equation, Fokker–Planck, Kolmogorov | diffusion, queues, epidemics, chemical kinetics, RL, MCMC |
| 3 | **Functional to be minimised** | an energy/entropy + a metric | gradient flow; Lyapunov decay; stability | heat flow, Cahn–Hilliard, porous medium, ML training, variational inference |
| 4 | **Optimality / control** | a cost and dynamics | Hamilton–Jacobi–Bellman (value) + dual density flow (MFG) | optimal control, RL, optimal transport, Schrödinger bridges, economics |
| 5 | **Symmetry** | invariance of the action/functional | conservation laws, constraints, reciprocity, exponents | Noether, gauge theory, scaling laws, Onsager |

Two *meta-structures* ride on top:

* **Coarse-graining (renormalisation).** Whenever you cannot resolve everything, you eliminate variables —
  and the price is memory and noise ([Mori–Zwanzig](../01-foundations/09-linear-response-and-memory.md)). Iterating that
  step gives the renormalisation group: fixed points of coarse-graining are **universality classes**, which
  is *why* a magnetic alloy, a fluid interface and certain bacteria colonies share exponents.
* **Information–entropy bookkeeping.** Any bounded observer of a stochastic system must lose information at
  a rate set by dissipation: fluctuation theorems (Jarzynski, Crooks) and Landauer's principle are the
  transport equations of *knowledge* about a system ([limits note](../11-universality/09-limits-of-the-claim.md)).

**Structure 1 is the widest, and the reason is trivial.** Suppose $\mu_t$ is any family of measures (or
densities, or counts) and suppose that the only way mass changes in a region is that it crosses the
boundary or is created inside. Then for every smooth test function $\varphi$,

$$\frac{\mathrm{d}}{\mathrm{d}t}\int\varphi\,\mathrm d\mu_t
=\int\nabla\varphi\cdot\mathbf v\,\mathrm d\mu_t+\int\varphi\,\sigma\,\mathrm d\mu_t ,$$

which *is* the continuity equation in weak form. No smoothness, no differentiability, no grid, no
metric — Dirac masses, empirical distributions, graph measures and percolation clusters all qualify. This
is the single most useful sentence in the atlas: **if your quantity is countable and moves locally, you
already have a transport equation** — you have only to identify the velocity (or the jump kernel) and the
source.

## L3 · What is a theorem, what is a model, what is a heuristic

Being precise here is what separates a real universality claim from wishful thinking.

| Structure | Status | Conditions, caveats |
|---|---|---|
| 1 · balance ⟹ continuity (weak form) | **theorem** | exact for measure-valued solutions; identifying $\mathbf v$ (or a jump kernel) is the modelling step. Pure jumps give *nonlocal* transport, not an advection equation |
| 2 · Markov process ⟹ forward equation | **theorem** (Feller semigroups) | the law's equation is the dual of the generator: diffusion ⟹ parabolic, jumps ⟹ master equation, Lévy ⟹ fractional, mixtures ⟹ Liouville + reset (PDMP). *Kramers–Moyal* shows Fokker–Planck is exact only for continuous paths with finite first two moments |
| 3 · functional ⟹ gradient flow | **theorem *if* the structure exists** | needs a Lyapunov functional *and* a metric; De Giorgi/JKO/$\Gamma$-convergence give existence, contraction, convergence. Many systems are *not* gradient flows; the general split is reversible + dissipative (GENERIC/metriplectic) |
| 4 · optimality ⟹ HJB (+ dual flow) | **theorem** under regularity | dynamic programming for deterministic and stochastic control (viscosity solutions); mean-field games need monotonicity for uniqueness; optimal transport is the static dual, Schrödinger bridges the entropic version |
| 5 · symmetry ⟹ conservation | **theorem** (Noether I & II) | conservation laws; *constraints* from the second theorem; reciprocity (Onsager) and exponents (dimensional analysis + RG) |
| meta · coarse-graining ⟹ RG | **heuristic in general, theorem in specific models** | fixed points of coarse-graining explain universality classes; exponents come with corrections, and mean-field theory is exact only above the upper critical dimension |
| meta · information loss | **theorem** (fluctuation theorems, Landauer) | dissipation sets the rate at which an observer loses information about a stochastic system |

**Three silent assumptions to check every single time.**

1. **Range of influence.** Local PDE, nonlocal kernel, or network edges? This choice is not cosmetic: it
   changes the boundary data, the well-posedness theory and the solver
   ([nonlocal operators](../06-beyond/03-nonlocal-and-fractional-operators.md)).
2. **Is your state Markovian?** If the future depends on the past beyond the current state, the density you
   wrote is incomplete: either enlarge the state (include age, history, internal variables) or carry
   memory — which converts a diffusion into a Volterra/fractional problem
   ([memory](../06-beyond/04-memory-viscoelastic-and-hereditary.md),
   [delay](../06-beyond/16-delay-and-retarded-transport.md)).
3. **Is the measured density the modelled density?** Observation has its own transport (sampling bias,
   aggregation bias, instrument response). Skipping this step is what makes many social-science and
   epidemiological fits look better — or worse — than they are
   ([inverse problems](../07-numerics/10-inverse-problems-and-data-assimilation.md)).

**And two honest warnings.**

* **Non-identifiability.** Different microscopic mechanisms can generate the *same* macroscopic transport
  (same drift, same diffusion). Transport equations are therefore excellent for prediction and poor for
  mechanism — unless you design experiments that separate them
  ([measurement](../10-appendix/05-measurement-and-experiments.md)).
* **Mean-field breakdown.** Every transport model assumes fluctuations average out. In finite populations,
  low copy numbers and small systems they do not, and you must return to the stochastic description. This is
  the exact analogue of the **Knudsen number**: the ratio of the microscopic correlation scale to the system
  scale, and the criterion for whether the continuum description is even defined.

## L4 · How to perform the translation (a checklist you can run)

1. **Name the quantity** with units, and say whether it is extensive (total), per-capita, or relative.
2. **Write the balance**: what crosses boundaries, and what is created or destroyed? If you cannot, there is
   no transport model — this is [balance laws & flux](../01-foundations/01-balance-laws-and-flux.md) and nothing more.
3. **Identify the driver**: gradient (constitutive law), randomness (generator), optimality (control),
   symmetry (conservation), or memory (kernel / fractional derivative).
4. **Identify the geometry**: Euclidean, Wasserstein, Fisher–Rao, graph, manifold. The metric decides which
   functional decreases and which numerical method is stable.
5. **Non-dimensionalise**, find the regime, classify the operator
   ([general classification](../01-foundations/10-general-pde-classification.md)).
6. **Find the invariants and the Lyapunov functional** — or prove that none exists; then look for oscillatory
   or limit-cycle behaviour and expect phase error to dominate your numerics.
7. **Choose numerics from the structure**, not from habit
   ([discretisation](../07-numerics/01-discretization-consistency-stability-convergence.md)).
8. **State the validity range**, including the mean-field/Knudsen condition from L3, and say what you would do
   if it failed.

> [!warning] Trap
> A successful translation is not a proof of mechanism. It buys you decades of mathematics — stability,
> well-posedness, error estimates, universality classes — but it never tells you that the underlying
> mechanism *is* a diffusive flow. Two models with the same transport behaviour are indistinguishable from
> macroscopic data alone, and that is an identifiability statement, not a mystery.

## Checks

1. When does the law of a Markov chain satisfy a *diffusion* equation? *(Only when paths are continuous with
   finite first two moments; otherwise it satisfies a master/kinetic equation — jumps, memory and fractional
   operators in general.)*
2. Which structure do a Hamiltonian system and a Brusselator oscillator have? *(Neither is a gradient flow:
   the first is volume-preserving transport (Liouville), the second has limit cycles and no Lyapunov
   functional — so no monotone functional and no automatic contraction.)*
3. What is the social-science analogue of the Knudsen number? *(System size relative to the interaction
   correlation length: with few agents per scale, mean-field descriptions fail and agent-based stochastic
   simulation is required.)*
4. Why are universality exponents usually not theorems? *(They need renormalisation-group arguments or limit
   theorems, available for specific models; in general they are asymptotic hypotheses with corrections.)*

## See also

[The decision tree & lookup](../11-universality/02-decision-tree-and-lookup.md) ·
[Limits of the claim](../11-universality/09-limits-of-the-claim.md) ·
[Entropy & variational structure](../01-foundations/07-entropy-and-variational-structure.md) ·
[Variational principles & Noether](../06-beyond/15-variational-principles-and-noether.md) ·
[Optimal transport & gradient flows](../06-beyond/10-optimal-transport-and-gradient-flows.md)


