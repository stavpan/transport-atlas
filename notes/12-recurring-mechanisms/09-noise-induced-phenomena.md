---
title: Noise-induced phenomena
blurb: Chance as a mechanism, not a nuisance — noise-selected states, stochastic resonance, rectification, rare events, and the thermodynamic bookkeeping of small systems.
depth: 4
tags: [mechanisms, noise, stochastic, Fokker-Planck, Kramers, stochastic resonance, large deviations]
---

# Noise-induced phenomena

> **One-line picture.** Add randomness to a nonlinear system and you do not merely blur it: you *change*
> it. Noise can select which state survives, amplify a signal you could not otherwise hear, turn
> symmetric fluctuations into directed motion, and set the rate of events that would otherwise never
> happen. Noise is a mechanism with its own catalogue of effects.
>
> **Prerequisites.** [Random walks, Langevin, response](../01-foundations/08-random-walks-langevin-response.md),
> [Fokker–Planck & Kramers](../05-kinetic/03-fokker-planck-and-kramers.md) ·
> **Leads to.** [Stochastic PDEs & random media](../06-beyond/07-stochastic-pdes-and-random-media.md),
> [the intersections map](10-intersections-map.md)

## L1 · Five things noise *does*

1. **It melts order.** A double-welled system with modest noise has two peaks in its stationary
   distribution; raise the noise and the peaks merge into one. The "state" was not destroyed by a change
   of parameters but by a change of *randomness*.
2. **It assists weak signals (stochastic resonance).** A signal too small to flip a bistable system does
   nothing when the noise is zero, drowns when the noise is huge — and, at an intermediate noise level,
   produces a clean periodic response. The system's signal-to-noise ratio is *maximal at nonzero noise*:
   less noise is not always better. Proposed for glacial cycles, observed in neurons, lasers, sensors and
   even human perception.
3. **It rectifies (ratchets).** With broken spatial symmetry and fluctuation that is out of equilibrium,
   random kicks produce systematic directed transport — the principle behind molecular motors and
   artificial Brownian ratchets, where the naive second-law objection is answered by the fact that the
   noise is not in equilibrium with the load.
4. **It selects and switches.** In multi-stable systems noise sets the *rate* of transitions between
   states (Kramers' law) and therefore the residence times: chemistry's reaction rates, nucleation of
   droplets, magnetic memory, and the spiking of neurons are all noise-driven escape problems.
5. **It makes bookkeeping exact.** For small systems, fluctuations are not a correction but the physics,
   and relations like Jarzynski's and Crooks' convert nonequilibrium work distributions into free-energy
   differences: thermodynamics becomes *measurable* in single-molecule experiments.

## L2 · The mechanisms in equations

| Effect | Mechanism | Where it shows up |
|---|---|---|
| Noise-induced transition | noise shifts the *maxima* of the stationary density $p\propto e^{-V/D}$ | [chemical bistability](../04-interaction/03-autocatalysis-and-oscillations.md), lasers, climate subsystems |
| Escape / reaction rate | Kramers: $\;k\sim e^{-\Delta V/D}$ (prefactor from curvature) | [nucleation](../04-interaction/09-phase-change-and-stefan.md), protein folding, switching |
| Stochastic resonance | periodic modulation + barrier crossing synchronised by noise | ice ages, sensory neurons, ring-laser gyroscopes |
| Ratchet drift | broken symmetry + nonequilibrium fluctuations | molecular motors, particle separation |
| Noise-induced pattern | multiplicative noise destabilises a uniform state | [stochastic PDEs](../06-beyond/07-stochastic-pdes-and-random-media.md), ecology, vegetation stripes |
| Noise-driven cascade | amplification of rare excursions along unstable directions | [SOC avalanches](06-phase-transitions-and-criticality.md), power grids |

![**Figure R10.** Two faces of noise. Left: raising the noise intensity melts a two-peaked stationary
distribution into a single-peaked one — a *noise-induced transition*, not a parameter change. Right:
stochastic resonance — the signal-to-noise ratio at the signal frequency (computed here from a real
simulation of a periodically forced bistable system) peaks at an intermediate noise level, so an optimal
amount of noise makes a sub-threshold signal detectable.](../../figures/noise-induced-transitions.svg)

## L3 · The apparatus: Fokker–Planck, Euler–Maruyama, and large deviations

* **Two languages, one process.** The stochastic ODE (Langevin) and the equation for the probability
  density (Fokker–Planck) are the same statement; noise appearing *multiplied* by the state makes them
  subtly different statements, because the choice of stochastic calculus (Itô vs Stratonovich) is a
  modelling decision about how the noise is correlated in time. Pick by the physics — white-noise idealisation
  or finite correlation time — then be consistent, because the two conventions give different drift.
* **Stationary states are variational.** For additive noise, the stationary density is
  $p(x)\propto e^{-V(x)/D}$: the system occupies states according to an exponential of the landscape. This
  is why "noise melts order" is a *quantitative* statement — the peaks survive until $D$ compares with the
  barrier between them.
* **Rare events are exponential.** Kramers' theory gives the escape rate from a well as
  $k\simeq\frac{\omega_0\omega_b}{2\pi\gamma}e^{-\Delta V/D}$: an exponential in the barrier over the noise,
  with a prefactor from the curvatures. The **mean first-passage time** is the reciprocal of that rate, and
  it is the quantity that matters for reliability, ageing and memory lifetime.
* **Large deviation theory is the rigorous version.** Freidlin–Wentzell theory identifies, in the small-noise
  limit, the *most probable path* out of a basin (the instanton / minimum action path) and proves an
  exponential scaling of probabilities — the same machinery that produces the Arrhenius law as a theorem
  rather than a heuristic.
* **Noise can bifurcate.** The stationary density can change *shape* (peaks appearing or disappearing —
  a phenomenological bifurcation) at a noise value where the deterministic system changes nothing at all.
  It is essential to distinguish this from a dynamical bifurcation of the random attractor: they need not
  coincide, and conflating them produces nonsense.
* **Fluctuation theorems close the books.** Jarzynski's equality $\langle e^{-W/k_BT}\rangle=e^{-\Delta F/k_BT}$
  and the Crooks relation give exact results for driven, far-from-equilibrium systems: irreversibility
  becomes a measurable asymmetry in the statistics of work — with the [arrow of time](../13-panta-rhei/04-irreversibility-and-the-arrow-of-time.md)
  appearing as a ratio of forward and backward probabilities.

## L4 · Simulating noise without fooling yourself

1. **Choose the right integrator and order.** Euler–Maruyama is strong order $1/2$ and weak order 1;
   Milstein and higher-order schemes restore accuracy when the noise is multiplicative; additive-noise
   problems are usually handled by the exponential (exact) integrator for the linear part plus a stochastic
   convolution. Verify strong *and* weak convergence separately — they mean different things.
2. **Do not estimate tails from a histogram.** Rare events are estimated by their *rate*: fit
   $\ln p$ against $1/D$, or use importance sampling / splitting / instanton calculations. A histogram with
   three counts in the last bin is not evidence of anything.
3. **Beware the timestep as a physical parameter.** A too-large $\Delta t$ silently changes the effective
   noise amplitude and the drift (Itô correction), moving the stationary distribution. Refine $\Delta t$
   until the stationary statistics stop changing.
4. **Use common random numbers** for comparisons (same noise realisations across parameter values), and
   multilevel Monte Carlo for expectations of smooth functionals: it converts an $O(\epsilon^{-2})$ cost
   into nearly $O(\epsilon^{-1})$.
5. **Report the noise model, not just its amplitude.** White vs coloured, additive vs multiplicative,
   independent vs shared across components: each changes the answer qualitatively, and in spatially
   extended systems the *spatial* correlation of the noise decides whether patterns are nucleated or merely
   roughened ([stochastic PDEs](../06-beyond/07-stochastic-pdes-and-random-media.md)).