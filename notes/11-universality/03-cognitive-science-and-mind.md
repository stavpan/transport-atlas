---
title: Cognitive science & mind
blurb: Brains as transport systems — evidence accumulation, neural fields, free-energy descent, memory as relaxation, and where the mathematics is literal rather than metaphorical.
depth: 3
tags: [cognitive-science, drift-diffusion, predictive-coding, neural-field, memory, attention]
---

# Cognitive science & mind

> **One-line picture.** A brain is not a set of instantaneous wires: it accumulates noisy evidence over
> time, spreads activity across tissue, diffuses chemicals through nanometre gaps, and holds *distributions*
> over hypotheses. Every one of those is a transport process — and in several cases the equation was fitted
> to neural or behavioural data long before anyone called it transport.
>
> **Prerequisites.** [Fokker–Planck & Kramers](../05-kinetic/03-fokker-planck-and-kramers.md),
> [Delay & retarded transport](../06-beyond/16-delay-and-retarded-transport.md) ·
> **Leads to.** [Social behaviour, economics & language](04-social-behaviour-economics-language.md),
> [Information, statistics & inference](07-information-statistics-and-inference.md)

## L1 · Why the mind is a transport system

Four independent reasons, in increasing order of literality:

1. **Decisions take time and vary.** Responses are distributed, not deterministic, and reaction-time
   *distributions* have a characteristic right-skewed shape. The canonical explanation is noisy evidence
   accumulating until it crosses a threshold — a first-passage problem for a diffusion.
2. **Activity is spatially extended.** Cortex is a sheet with short-range excitation, longer-range inhibition
   and conduction delays; its coarse-grained activity obeys integro-differential **neural-field** equations
   whose solutions include travelling waves, persistent bumps and patterns.
3. **Signalling molecules physically diffuse.** Neurotransmitter across a 20 nm cleft, calcium in a spine,
   IP₃ through astrocytic networks, potassium in extracellular space: ordinary diffusion–reaction problems
   with measurable coefficients. Cortical spreading depression — the slow chemical wave behind migraine aura —
   is a textbook reaction–diffusion wave.
4. **Beliefs are distributions.** Under uncertainty the evolving object is a measure over hypotheses;
   Bayesian updating, variational inference and message passing are transport of that measure, often with an
   explicit *optimality* structure (minimise surprise or expected cost).

## L2 · The canonical models, with their equations

### 1 · Evidence accumulation: the drift–diffusion model

$$\mathrm dx=\mu\,\mathrm dt+\sigma\,\mathrm dW,\qquad \text{decide when }x=\pm\theta,\qquad
\partial_tp=-\mu\,\partial_xp+\tfrac{\sigma^2}{2}\partial_x^2p .$$

The decision variable's density obeys a Fokker–Planck equation with absorbing boundaries; the observable is
the **first-passage-time distribution** (inverse-Gaussian-like), which predicts both the shape of
reaction-time distributions and the *error-RT relation*. The parameters have psychological names: drift $\mu$
= evidence quality; boundary $\theta$ = caution, so the **speed–accuracy trade-off** is literally a boundary
value; starting point = bias; and the **non-decision time** is exactly a
[delay](../06-beyond/16-delay-and-retarded-transport.md). This is the most quantitatively successful model
family in cognitive psychology — and it is a transport model.

### 2 · Why this is also statistically optimal

Accumulating **log-likelihood ratios** and stopping at a threshold is Wald's sequential probability ratio
test: optimal in the sense of minimising expected sample size for a given error rate. So the psychological
model is the control-theoretic *optimum* of an inference problem — the same intersection of transport and
optimality that appears in mean-field games ([finance & economics](../08-bridges/02-finance-and-economics.md)).

**Attention enters as precision.** Raising precision lowers $\sigma$: in this formalism, paying attention is
literally *reducing the diffusion coefficient* of the decision variable, and it sharpens the effective
drift-to-noise ratio in exactly the way signal-detection theory's $d'$ describes.

### 3 · Predictive coding and the free-energy principle

Variational inference replaces an intractable posterior with the closest tractable one,
$q^*=\arg\min_q\mathrm{KL}\big(q\,\|\,p(\cdot\mid\text{data})\big)$; gradient descent on that functional is a
gradient flow ([entropy & variational structure](../01-foundations/07-entropy-and-variational-structure.md)).
Predictive coding implements it as precision-weighted prediction-error dynamics between hierarchical levels;
**active inference** adds actions, turning the problem into stochastic optimal control with a
Hamilton–Jacobi–Bellman structure ([Hamilton–Jacobi](../06-beyond/02-hamilton-jacobi-and-viscosity-solutions.md)).

> [!warning] Trap
> The *mathematics* of variational free energy is standard and rigorous; the claim that brains literally
> implement it is a **modelling hypothesis**, not a theorem. It is attractive because one functional
> unifies perception, action and learning — but its predictions are often under-determined, rival accounts
> (reinforcement learning, Bayesian sampling, direct posterior coding) make overlapping predictions, and
> distinguishing them experimentally is an open problem. Treat it as a framework that generates models.

### 4 · Neural fields, delayed loops and brain rhythms

Continuum descriptions of cortex (Amari, Wilson–Cowan) read

$$\partial_tu(\mathbf x,t)=-u+\int w(\mathbf x-\mathbf y)\,S\big(u(\mathbf y,t-\tau)\big)\,\mathrm d\mathbf y+I(\mathbf x,t),$$

an integro-differential transport equation with a **delay built into the kernel**. Its solution repertoire
covers a lot of neuroscience:

* **Persistent bumps** — working memory as a stationary (or slowly drifting) state of a transport equation.
* **Travelling pulses and waves** — propagation with conduction delay; delay selects wavelength and rhythm,
  the standard story for spindle- and alpha-band activity ([delay](../06-beyond/16-delay-and-retarded-transport.md)).
* **Turing-type patterns** — Ermentrout and Cowan's explanation of the *geometric* form of elementary visual
  hallucinations follows from the symmetries of a cortical pattern-forming instability: one of the most
  striking quantitative predictions of a reaction–diffusion model in neuroscience
  ([Turing patterns](../04-interaction/04-reaction-diffusion-and-turing.md)).
* **Excitable spiral waves** — the mathematical cousin of cardiac arrhythmias, used to model
  epileptiform activity ([fronts](../04-interaction/05-fronts-and-travelling-waves.md)).

And the reduction to a *density* is exact in a limit: for many weakly coupled spiking neurons, the population
density in (voltage, conductance) space satisfies a Fokker–Planck equation with the synaptic input entering
as drift and diffusion. The brain, at that level of description, *is* a transport system.

### 5 · Memory: attractors, decay, and the statistics of synapses

* **Retrieval as relaxation.** In Hopfield-type networks memories are minima of an energy functional and recall
  is a descent flow — the same gradient-flow structure as phase ordering, with metastable states, slow
  relaxation, and a storage capacity near $0.138N$ for random Hebbian patterns. Retrieval is transport in
  state space, governed by spin-glass mathematics.
* **Forgetting as fractional relaxation.** Empirical retention curves follow *power laws* (Wickelgren, Wixted)
  rather than exponentials — and power-law relaxation is the signature of memory kernels and fractional
  derivatives ([memory & viscoelasticity](../06-beyond/04-memory-viscoelastic-and-hereditary.md)). A single
  exponential requires one time constant; memory has a broad spectrum, which is what a fractional law encodes.
* **Consolidation as two-compartment transport.** Fast (hippocampal) and slow (cortical) stores exchanging
  information is a two-reservoir transport problem in which the exchange rate and replay schedule set the
  retention statistics — the "complementary learning systems" picture in transport language.
* **Synapses as a distribution.** Plasticity rules are stochastic updates, so the *distribution* of synaptic
  weights evolves by a Fokker–Planck equation whose stationary state reproduces the observed heavy-tailed
  weight distributions. Learning and forgetting are drift and diffusion in weight space.

### 6 · Semantic networks: diffusion on a graph

Represent knowledge as a graph of concepts. Then "spreading activation" (Collins & Loftus) is *diffusion on a
graph*, with the graph Laplacian replacing $\nabla^2$; priming is pre-activation (a non-zero initial
condition), semantic distance is resistance (graph distance), and reaction times in word recognition scale
with how quickly activation arrives. The same operator gives the smoothing, the mixing time and the spectral
gap ([computation & algorithms](05-computation-and-algorithms.md)), so vocabulary-size effects, category
fluency and the shape of semantic spaces all inherit the mathematics of transport on networks.

This is where cognitive science meets [networks & traffic](../08-bridges/09-networks-society-and-traffic.md):
a concept network behaves like any other transport network — bottlenecks, hubs, spectral gaps — and the
statistical regularities of language (Zipf's law) come from preferential-attachment growth, i.e. from a
multiplicative stochastic transport in frequency space
([social behaviour, economics & language](04-social-behaviour-economics-language.md)).

### 7 · Cognitive maps: eigenmodes and the successor representation

Navigation provides two unusually crisp transport structures:

* **Grid cells as Laplacian eigenmodes.** Models in which grid-cell firing patterns emerge as *eigenvectors
  of the spatial transition matrix* (equivalently of a graph Laplacian on the environment) reproduce the
  observed hexagonal lattices. Grid fields are then literally the eigenmodes of diffusion on the environment —
  the same objects as the vibrational modes of a drum
  ([dimensions & geometry](../01-foundations/12-dimensions-geometry-and-manifolds.md)).
* **The successor representation.** The expected discounted future occupancy of states,
  $M=(I-\gamma T)^{-1}$, is the **resolvent** of the transition operator: a Green function for a discounted
  transport problem. Value learning and predictive maps then become algebra of transport operators, and
  planning becomes a transport computation rather than a tree search.

Navigation as optimal control adds the Hamilton–Jacobi branch: shortest-path and travel-time fields satisfy an
eikonal equation, so *both* hemispheres of the atlas — diffusion and optimality — describe what the same
circuitry appears to do ([Hamilton–Jacobi](../06-beyond/02-hamilton-jacobi-and-viscosity-solutions.md)).

### 8 · Psychophysics: thresholds as first-passage statistics

Signal-detection theory says that discriminability is separation over noise, $d'=\Delta\mu/\sigma$. In the
diffusion picture that is a statement about two first-passage problems: hit and false-alarm rates are the
probabilities that a noisy accumulator with one drift or the other reaches a boundary first. Consequences that
are actually used: the psychometric function is a diffusion-to-threshold curve; just-noticeable differences
scale with the inverse square root of Fisher information
([information & inference](07-information-statistics-and-inference.md)); and response bias is a shift in the
starting point. Weber's law itself emerges when noise scales with stimulus magnitude — a *multiplicative*
noise model, the same mathematical feature that generates lognormal and power-law distributions elsewhere in
this atlas ([social behaviour, economics & language](04-social-behaviour-economics-language.md)).

Physical transport closes the loop at the small end: synaptic cleft diffusion (20–30 nm, microseconds), spine
calcium microdomains, and dendritic cable filtering are ordinary diffusion problems whose coefficients are
measured, and they set the time constants that appear as "non-decision time" in the behavioural models above.

## L3 · What is established, what is a framework, what is a hypothesis

Calibration matters more here than anywhere else in the atlas, because cognitive science attracts
over-claiming. The honest scorecard:

| Claim | Status |
|---|---|
| Reaction-time *distributions* from a noisy accumulator with absorbing boundaries | **quantitatively validated** across many tasks; neural ramping correlates (e.g. parietal/premotor build-up) |
| Log-likelihood accumulation is optimal (SPRT) | **theorem** (Wald), given known likelihoods and stable evidence statistics |
| Precision modulates effective diffusion (attention as $\sigma\downarrow$) | **well-supported modelling claim**, with direct experimental manipulations of noise |
| Neural fields generate waves, bumps and Turing patterns | **validated** where measured (wave speeds, persistent activity); the mapping of hallucination geometry to cortical coordinates is an interpretation, not a measurement |
| Spiking-network activity ⇒ exact Fokker–Planck in a limit | **theorem** under exchangeability and neglected correlations; finite-size effects and synchrony are the corrections |
| Free-energy/active-inference framework | **rigorous mathematics, hypothesis about brains** — predictions often under-determined |
| Hopfield capacity $\approx0.138N$ | **theorem** for random Hebbian patterns; modified for structured/correlated ones |
| Power-law forgetting implies fractional diffusion | **partly an inference**: power laws constrain the exponent, not the mechanism — mixtures of exponentials and lognormal spectra mimic them too |
| Grid fields as Laplacian eigenmodes | **one successful model among competitors** — it reproduces hexagonality but does not uniquely identify the circuit |
| Successor representation $=(I-\gamma T)^{-1}$ | **mathematical identity** for discounted occupancy; the cognitive claim is that brains compute it |

**Two structural warnings.**

* **Identifiability.** Several distinct mechanisms (different boundaries, collapsing thresholds, variable
  drift, non-decision time) can produce nearly identical reaction-time distributions. Unless the experiment
  separates them, the fitted parameters are not evidence about mechanism
  ([inverse problems](../07-numerics/10-inverse-problems-and-data-assimilation.md)).
* **Mean-field breakdown.** The exact density equation needs many similar neurons and weak correlations. In
  small circuits, in synchronised bursts, or in pathological states, correlations are the physics — and you must
  simulate spiking networks or use fluctuation-corrected closures. This is the neural version of the
  [Knudsen number](01-why-everything-flows.md).

## L4 · Practice: how this is actually done

* **Fitting decision models.** Use the first-passage density for the likelihood (analytic for
  drift–diffusion, numeric else), hierarchical Bayesian estimation for group-level parameters, and — for quick
  work — quantile or "EZ" estimators. Standard pitfalls: right-censored and contaminated responses (model them
  with a mixture), confounding of non-decision time with boundary separation, and reporting fits without
  parameter-recovery checks.
* **Simulating SDEs**: Euler–Maruyama with small steps, or exact sampling for special cases; check the
  empirical first-passage distribution against theory before trusting parameter recovery
  ([random walks & Langevin](../01-foundations/08-random-walks-langevin-response.md)).
* **Neural fields**: translation-invariant kernels make FFT convolution natural; delay terms require stored,
  interpolated history; travelling-wave stability is analysed with Evans functions; delay-induced rhythms come
  from pseudospectral analysis of the delayed spectrum
  ([delay](../06-beyond/16-delay-and-retarded-transport.md)).
* **Spiking-network densities**: solve the voltage Fokker–Planck equation with a refractory reset (a boundary
  condition that returns probability to the reset value), which conserves total probability exactly — a good
  test of any implementation. Validate the mean-field reduction against direct network simulations at several
  network sizes.
* **Latent dynamics from data**: state-space models (Kalman/particle filters), delay embedding for single
  series (Takens), dimensionality reduction as transport to a latent space. Remember that the *observed* density
  is not the latent one — observation transport must be modelled explicitly
  ([data assimilation](../07-numerics/10-inverse-problems-and-data-assimilation.md)).
* **Benchmarks**: posterior-predictive checks on RT distributions (not just means); wave-speed and
  pattern-wavelength comparisons for neural fields; FP-versus-network firing-rate agreement; eigenvalue
  structure of grid fields; Hopfield capacity curves.

## Checks

1. In the drift–diffusion model, what psychological construct is the *boundary*? *(Caution / response
   threshold: it sets the speed–accuracy trade-off.)*
2. Why is "attention = increasing precision" a statement about a diffusion coefficient? *(Precision is inverse
   variance; lowering $\sigma$ raises $d'$ — attention changes the noise term of the accumulator.)*
3. What is the neural analogue of the Knudsen number? *(Network size relative to correlation length: small
   circuits and strong synchrony invalidate the mean-field density description.)*
4. Why does a power-law forgetting curve *not* prove fractional diffusion? *(Power laws are reproducible by
   other broad-spectrum mechanisms; they constrain the exponent, not the mechanism.)*

## See also

[Delay & retarded transport](../06-beyond/16-delay-and-retarded-transport.md) ·
[Fokker–Planck & Kramers](../05-kinetic/03-fokker-planck-and-kramers.md) ·
[Social behaviour, economics & language](04-social-behaviour-economics-language.md) ·
[Computation & algorithms](05-computation-and-algorithms.md) ·
[Limits of the claim](09-limits-of-the-claim.md)



