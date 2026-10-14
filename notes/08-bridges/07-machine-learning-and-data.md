---
title: Transport in machine learning & data
blurb: Diffusion models are reverse-time diffusion equations; graph diffusion ranks the web; optimal transport measures distributions — the atlas is inside modern ML.
depth: 3
tags: [diffusion models, score matching, PageRank, attention, optimal transport]
---

# Transport in machine learning & data

> **One-line picture.** Modern generative models *are* transport equations solved backwards in time; and
> graph diffusion is the same Laplacian you met in heat conduction.
>
> **Prerequisites.** [random walks & Langevin](../01-foundations/08-random-walks-langevin-response.md),
> [optimal transport](../06-beyond/10-optimal-transport-and-gradient-flows.md)

## L1 · Four places where transport theory is the theory

| ML object | Transport equation behind it | Why it matters |
|---|---|---|
| Diffusion model (DDPM, score-based) | forward noising SDE + reverse-time Fokker–Planck | sampling = solving an SDE backwards; score $=\nabla\log p$ |
| Flow matching / continuous normalising flows | continuity equation $\partial_t\rho+\nabla\!\cdot(\rho\mathbf v)=0$ | learn a velocity field that transports a prior into data |
| Graph neural networks / PageRank | graph Laplacian diffusion, random walk with teleport | smoothing, ranking, consensus; heat kernel on graphs |
| Optimal transport in ML | Wasserstein distance, Sinkhorn | distribution comparison, domain adaptation, generative loss |

The key mathematical statements: the **Fokker–Planck equation** governs how a probability density evolves
under noise; running it backwards requires the *score* $\nabla\log p_t$, which is what a network learns;
and the reverse-time SDE is a legitimate transport equation in exactly the sense of this atlas
([Fokker–Planck & Kramers](../05-kinetic/03-fokker-planck-and-kramers.md)).

## L2 · Why the atlas's concepts keep appearing

* **Entropy and free energy**: variational inference minimises a Kullback–Leibler divergence, i.e. a
  relative entropy — the same functional that drives diffusion
  ([entropy & variational structure](../01-foundations/07-entropy-and-variational-structure.md)).
* **JKO and Wasserstein**: sampling schemes can be written as Wasserstein gradient flows of a free energy,
  including Langevin dynamics and its accelerated variants.
* **Stability and stiffness**: training diffusion models means integrating stiff SDEs; discretisation
  choices (Euler–Maruyama vs higher order) visibly change sample quality
  ([SDE integrators](../01-foundations/08-random-walks-langevin-response.md)).
* **Conservation and structure**: flow-based models are *exactly* continuous transports (invertible), and
  their architecture must be divergence-free-friendly to control the density change — the same
  compatibility requirement as incompressible-flow discretisations
  ([structure-preserving](../07-numerics/13-structure-preserving-discretizations.md)).

## L3 · The reverse direction: ML inside transport modelling

* **Operator learning** accelerates repeated PDE solves ([operator learning](../07-numerics/11-machine-learning-and-operator-learning.md)).
* **Learned closures** for turbulence and subgrid dispersion — with the caveat that they must respect
  conservation and realisability.
* **Surrogates inside inversion and data assimilation**, replacing expensive forward solves
  ([inverse problems](../07-numerics/10-inverse-problems-and-data-assimilation.md)).
* **Graph diffusion** for network transport: the same Laplacian governs heat on meshes, diffusion maps for
  manifold learning, and influence propagation in social networks
  ([networks, society & traffic](09-networks-society-and-traffic.md)).

## L4 · Practice and pitfalls

* **Never evaluate a generative model without a metric tied to the transport**: probability-flow ODE
  residuals, Wasserstein distances between sample and data distributions, and mode coverage.
* **Respect the dimensional analysis**: noise schedules and step sizes behave like diffusion numbers
  ($\Delta t$ vs $\Delta x^2/D$); rescaling data changes what "stable step" means.
* **Watch for the physics-free failure mode**: a generative model can produce density where the
  conservation law forbids it. Structural constraints must be enforced, not hoped for.
* **Benchmarks**: analytic Gaussian transports (exact Wasserstein/entropy), Lorenz-96 assimilation, and
  Darcy-flow operator benchmarks ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).

## Checks

1. What does a diffusion model learn, in transport language? *(The score, hence the drift of the
   reverse-time Fokker–Planck flow that transports noise into data.)*
2. Which functional does both variational inference and heat flow minimise? *(Relative entropy.)*

## See also

[Fokker–Planck & Kramers](../05-kinetic/03-fokker-planck-and-kramers.md) ·
[Optimal transport & gradient flows](../06-beyond/10-optimal-transport-and-gradient-flows.md) ·
[Machine learning & operator learning](../07-numerics/11-machine-learning-and-operator-learning.md) ·
[Networks, society & traffic](09-networks-society-and-traffic.md)
