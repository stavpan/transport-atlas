---
title: Delay & retarded transport
blurb: When the cause lags the effect — delay differential equations are just transport along a characteristic, and they explain oscillations, chaos and brain rhythms.
depth: 3
tags: [delay, DDE, retarded, Hopf, Mackey-Glass, memory]
---

# Delay & retarded transport

> **One-line picture.** A delay is not a new ingredient: plug flow with a transit time *is* a delay, and
> every delay differential equation is a transport equation whose history has been integrated out. The
> cost of removing the spatial dimension is that the state becomes a function, not a number.
>
> **Prerequisites.** [Memory, viscoelasticity & Cattaneo](04-memory-viscoelastic-and-hereditary.md),
> [Material derivative](../01-foundations/02-material-derivative.md) ·
> **Leads to.** [Cognitive science & mind](../11-universality/03-cognitive-science-and-mind.md),
> [Social behaviour, economics & language](../11-universality/04-social-behaviour-economics-language.md)

## L1 · Why lags are everywhere

Signals, materials and organisms take time to respond: an axon conducts in milliseconds, a gene
transcribes in minutes, a driver reacts in ~1 s, an epidemic incubates for days, an immune system
responds in weeks. Model any of them with an instantaneous response and you will miss the qualitative
behaviour — which is, remarkably often, *oscillation*.

Delays are the most economical generator of oscillation known: a simple negative feedback with a lag
produces ringing, and enough lag produces chaos. That single mechanism underlies neural rhythms, laser
pulsations, traffic waves, physiological cycles and control-system instability.

## L2 · The structure, and the identity that makes it transport

A scalar delay differential equation (DDE) is $\dot u=f(u(t),u(t-\tau))$; with spatial transport it
becomes a **delay PDE**, $\partial_tu+\mathbf{u}\!\cdot\!\nabla u=f(u,u_\tau)$. The key observation is
that a delay *is* a translation along a characteristic:

$$\text{plug flow: } u(t-\tau)=u(x-u_0\tau,\,t)\quad\Longrightarrow\quad
\underbrace{\partial_tu+u_0\partial_xu=f(u,u(x-L,t))}_{\text{transport with a spatial shift}} .$$

So a DDE is a transport equation in disguise: the "memory" of the lumped model is the spatial profile
that the advection equation carries. Two consequences:

* **Memory is transport with the space removed.** A single delay is a delta memory kernel; a
  distribution of delays is a general memory kernel; and a power-law kernel gives a fractional
  derivative ([memory & viscoelasticity](04-memory-viscoelastic-and-hereditary.md)). DDEs, Volterra
  equations, fractional equations and transport-with-drift are four notations for one structure.
* **Distributed delays = transport in an internal coordinate.** Maturation delays, age-structured
  populations and transit-time distributions obey genuine transport equations in *age* or *transit time*:

$$\partial_tn+\partial_an=D\partial_a^2n-\mu(a)n,\qquad n(0,t)=\int\beta(a)n(a,t)\,\mathrm da
\qquad\text{(a McKendrick–von Foerster equation).}$$

That is why the same mathematics describes epidemiology (SEIR with incubation), cell biology (cell-cycle
models), pharmacokinetics (transit compartments) and chemical reactors (residence-time distributions).

| Model | Lag | Behaviour |
|---|---|---|
| Mackey–Glass (haematopoiesis) | blood-cell maturation | period-doubling route to chaos |
| delayed logistic / Wright | reproduction | Hopf oscillation, long-period cycles |
| optimal-velocity traffic model | driver reaction time | stop-and-go waves, jam propagation |
| neural field with axonal delay | conduction velocity | travelling waves, spindle rhythms, epileptiform waves |
| laser with optical feedback | cavity round trip | pulsations, low-dimensional chaos |
| machining / control loops | sensing + actuation | chatter, instability |
| drift-diffusion with delayed evidence | decision lag | oscillations in choice dynamics |

## L3 · What the mathematics guarantees

* **The state is a function, not a number.** A DDE needs a *history* $u(\theta)$, $\theta\in[-\tau,0]$, as
  initial datum; solutions exist by the **method of steps**, and the flow is a semigroup — but on the
  space of histories $C([-\tau,0])$, which is infinite-dimensional. Every intuitive statement about
  "state" must be re-read accordingly.
* **The spectrum is infinitely rich.** Linearising gives a *transcendental* characteristic equation
  (e.g. $\lambda=a+be^{-\lambda\tau}=0$), so there are **infinitely many eigenvalues**, finitely many in
  any right half-plane. For scalar linear DDEs they can be written exactly with the **Lambert $W$
  function**, $\lambda=a+\tfrac1\tau W(b\tau e^{-a\tau})$. Stability is decided by the rightmost
  eigenvalue — and by how it moves with $\tau$.
* **Delay destabilises, and creates stability pockets.** Negative feedback plus lag gives a Hopf
  bifurcation: oscillation appears from nothing. As $\tau$ increases further the pair can *re-stabilise*
  and destabilise again — stability switches that are impossible in any finite-dimensional ODE system, and
  are the origin of physiological and engineering cycling.
* **Delay can select a wavelength.** In a transported system with a delayed boundary condition, resonance
  occurs when the delay matches a spatial period ($L=u_0\tau$): delay imposes a *length scale*, creating
  patterns where the instantaneous model has none. This is delay-induced pattern formation — distinct from
  [Turing's mechanism](../04-interaction/04-reaction-diffusion-and-turing.md), though it can cooperate
  with it.
* **Causality decides well-posedness.** *Retarded* equations (delay in the lower-order terms) are
  well-posed with a history; *neutral* equations need more regularity and can be delicate; *advanced*
  equations (the state depending on the future) are ill-posed for the initial-value problem — the
  anti-causal case, and the reason you cannot simply reverse an advection with delay.

## L4 · Numerics

* **Method of steps** for small $\tau$; **continuous Runge–Kutta** with dense output for moderate delays;
  **pseudospectral collocation in the history interval** (Chebyshev nodes) for high accuracy and spectra
  — this converts the DDE into an ODE system plus coupling conditions, and is the standard production
  approach.
* **Expect spurious eigenvalues.** Discretising an infinite-dimensional spectrum always invents some:
  refine and re-check that the rightmost eigenvalues converge before trusting a stability verdict.
* **Delay PDEs need characteristic-aware treatment.** The delayed term is a history *along the
  characteristic*; store and interpolate the history with high order, or you will inject dissipation and
  artificial dispersion into a hyperbolic problem.
* **Estimating $\tau$ from data is possible** — delay-embedding (Takens' theorem) reconstructs the
  dynamics from a single time series; mutual information, autocorrelation and wavelet methods give
  practical estimates. This is the entry point to data-driven dynamics and to
  [cognitive time series](../11-universality/03-cognitive-science-and-mind.md).
* **Benchmarks**: delayed logistic equation (Hopf at $\tau=\pi/2$); Mackey–Glass period doubling to chaos;
  delayed optimal-velocity traffic waves; Lang–Kobayashi laser dynamics; neural-field travelling waves
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).

## Checks

1. Why is a DDE "just transport"? *(Plug flow makes $u(t-\tau)=u(x-u_0\tau,t)$: the delay is a spatial
   shift, and the memory of the lumped model is the profile the advection equation carries.)*
2. What makes the spectrum infinite, and how do you solve it exactly for a scalar linear DDE? *(The
   $e^{-\lambda\tau}$ term; via the Lambert $W$ function.)*
3. Give a behaviour a delayed system has that no finite-dimensional ODE can. *(Stability switches as
   $\tau$ grows: an infinite sequence of stable and unstable intervals.)*

## See also

[Memory, viscoelasticity & Cattaneo](04-memory-viscoelastic-and-hereditary.md) ·
[Cognitive science & mind](../11-universality/03-cognitive-science-and-mind.md) ·
[Social behaviour, economics & language](../11-universality/04-social-behaviour-economics-language.md) ·
[Networks, society & traffic](../08-bridges/09-networks-society-and-traffic.md)

