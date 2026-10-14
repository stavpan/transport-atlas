---
title: Mathematics itself
blurb: Transport as the connective tissue of mathematics — geometric flows, semigroups, Dirichlet forms, Markov categories, discrete exterior calculus.
depth: 4
tags: [ricci-flow, geometric-flows, semigroup, Markov-category, discrete-exterior-calculus]
---

# Mathematics itself

> **One-line picture.** Transport is not only *used by* mathematics — it *is* a large part of mathematics:
> geometric flows are heat equations for shapes, semigroups and Dirichlet forms are the general theory behind
> "every Markov process has a PDE", and category theory gives transport a compositional semantics.
>
> **Prerequisites.** [Variational principles & Noether](../06-beyond/15-variational-principles-and-noether.md),
> [Optimal transport & gradient flows](../06-beyond/10-optimal-transport-and-gradient-flows.md) ·
> **Leads to.** [Limits of the claim](09-limits-of-the-claim.md)

## L1 · The claim for mathematics

Four independent bridges, each of which is a *research area* rather than a metaphor:

1. **Geometry is diffusion.** Curvature can be made to flow by a heat-type equation, and the resulting flows
   solve classification problems in topology. Shape, in this view, is a slowly relaxing field.
2. **Analysis is the theory of generators.** Hille–Yosida, Dirichlet forms and martingale problems give a
   bijection (under mild conditions) between well-behaved Markov processes and their generators: *every* such
   process has a transport equation, and *every* suitable operator generates one.
3. **Probability is composition of transports.** Markov kernels form a *symmetric monoidal category* with a
   copy/discard structure: conditioning, Bayesian inversion and independence become categorical operations, and
   this "Markov category" framework gives rigorous, compositional semantics to probabilistic programs and
   graphical models.
4. **Discrete geometry keeps Stokes' theorem exactly.** Discrete exterior calculus (DEC) builds operators on
   meshes so that $\nabla\!\cdot\!\nabla\times=0$, the divergence theorem and the de Rham complex hold
   *identically* — transport theory and discrete mathematics joined at the definition.

## L2 · The structures

| Mathematical object | Transport formulation | Why it matters |
|---|---|---|
| Ricci flow $\partial_tg=-2\mathrm{Ric}$ | heat equation for the metric | Perelman's entropy monotonicity; Poincaré conjecture |
| mean-curvature flow | $L^2$ gradient flow of area | interface motion, image segmentation |
| harmonic map flow | gradient flow of Dirichlet energy | maps between manifolds |
| Yang–Mills / Lüscher gradient flow | gradient flow in gauge-field space | stochastic quantisation; used in lattice QCD |
| heat kernel | propagator of the Laplacian | recovers area, curvature, Euler characteristic |
| spectral geometry | eigenvalues of $\Delta_g$ | "can one hear the shape of a drum?"; isospectral manifolds |
| semigroups & generators | $e^{tL}$; Hille–Yosida | the general theory behind parabolic PDEs |
| Dirichlet forms | energy forms for Markov processes | symmetric Markov processes, Fukushima's theory |
| martingale problem | generator + law of a process | Stroock–Varadhan: PDE ↔ probability |
| gradient flows in metric spaces | $W_2$/$L^2$/$H^{-1}$ descent | Ambrosio–Gigli–Savaré unify ODE, PDE, optimisation |
| $\Gamma$-convergence | variational limits of functionals | why singular limits (sharp interfaces) are rigorous |
| optimal transport | Monge–Kantorovich problem | geometry of measures; Wasserstein space is a metric space |
| min-cost flow, assignment, EMD | discrete optimal transport | combinatorial optimisation *is* transport on graphs |
| Markov categories | Markov kernels as morphisms | compositional probability, Bayesian inversion |
| discrete exterior calculus | mimetic operators on meshes | exact discrete Stokes/divergence; structure preservation |
| information geometry | Fisher–Rao manifold | statistics as geometry (Čencov's theorem) |

## L3 · What the mathematics guarantees

* **Generators and processes are in bijection (up to technicalities).** Hille–Yosida gives well-posed parabolic
  evolution for a huge class of operators; Dirichlet forms characterise symmetric Markov processes (with the
  Beurling–Deny decomposition separating local diffusion from jumps). So "every Markov process has a transport
  equation, and most reasonable operators generate one" is a theorem, not a slogan — and the *type* of the
  generator (local vs jump, order of the symbol) classifies the transport
  ([general classification](../01-foundations/10-general-pde-classification.md)).
* **Geometric flows carry Lyapunov functionals.** Perelman's entropy is monotone under Ricci flow, exactly as the
  free energy is monotone under a gradient flow; monotonicity is what rules out bad singularities and gives
  long-time structure. Blow-up analysis near singularities uses *parabolic rescaling* — the same
  self-similarity technique as Stefan and Barenblatt
  ([key derivations](../10-appendix/04-key-derivations.md)).
* **Transport geometry is a genuine metric space.** Wasserstein space is geodesic; the Benamou–Brenier
  formulation makes optimal transport a fluid-dynamics problem; displacement convexity gives contraction.
  Combinatorial transport (min-cost flow, assignment) is the *graph* version, so the algorithms of combinatorial
  optimisation and of measure geometry are two implementations of one theory.
* **Categories give transport a semantics.** Markov categories make composition, conditioning, independence and
  almost-sure reasoning structural, so probabilistic programs and graphical models inherit a precise algebra —
  and Bayesian inversion becomes a categorical operation rather than an ad-hoc formula.
* **Discrete geometry can be exact.** In discrete exterior calculus, Stokes' theorem, the de Rham complex and the
  identities $\nabla\!\cdot\!\nabla\times=0$ hold identically on a mesh. This is the mathematical backbone of the
  structure-preserving discretisations used throughout the numerics part
  ([structure-preserving schemes](../07-numerics/13-structure-preserving-discretizations.md)).
* **Transport data under-determines geometry.** Heat-kernel asymptotics recover area, curvature and Euler
  characteristic, but isospectral non-isometric manifolds exist: "can one hear the shape of a drum?" has the
  answer *no*. Even in pure geometry, the transport description is not a complete invariant — a good emblem for
  the whole atlas ([limits of the claim](09-limits-of-the-claim.md)).

## L4 · Practice

* **Use mimetic/DEC discretisations** when exact discrete theorems matter; use finite elements when you need
  energy minimisation; use level sets or phase fields for mean-curvature flow.
* **Monitor the Lyapunov functional numerically** — Perelman entropy for Ricci flow, area for MCF, energy for
  harmonic maps: it is a diagnostic that transfers straight from transport theory into geometry codes.
* **Spectral numerics** answer geometric questions: compute Laplace eigenvalues and compare with known spectra
  (spheres, tori, hyperbolic surfaces) to test both the discretisation and the geometry.
* **Optimal-transport solvers** (Sinkhorn, network simplex, semi-discrete methods) are now standard tools in
  geometry, statistics and machine learning alike — 1-D and graph cases have exact algorithms worth using as
  tests.
* **Benchmarks**: mean-curvature flow of a circle (exact solution); eigenvalues on the sphere against
  $\ell(\ell+1)/R^2$; discrete Stokes tests on random meshes; Sinkhorn versus exact transport on graphs;
  conservation of symplectic/contact structures in geometric integrators.

## Checks

1. Which theorem turns "Markov process" into "transport equation" in general? *(Hille–Yosida/Dirichlet-form
   theory: the generator of a Feller semigroup, with local diffusion and jump parts classified by its symbol.)*
2. What plays the role of a Lyapunov functional in Ricci flow? *(Perelman's entropy — monotone, and the key to
   excluding bad singularities.)*
3. Why is combinatorial min-cost flow a transport problem? *(It is Monge–Kantorovich on a graph: capacities and
   costs replace densities and distances.)*
4. What does the existence of isospectral non-isometric manifolds say about transport descriptions?
   *(They under-determine geometry: even complete spectral/transport data need not fix the object.)*

## See also

[Optimal transport & gradient flows](../06-beyond/10-optimal-transport-and-gradient-flows.md) ·
[Variational principles & Noether](../06-beyond/15-variational-principles-and-noether.md) ·
[Structure-preserving discretisations](../07-numerics/13-structure-preserving-discretizations.md) ·
[Information, statistics & inference](07-information-statistics-and-inference.md) ·
[Limits of the claim](09-limits-of-the-claim.md)

