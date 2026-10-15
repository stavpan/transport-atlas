---
title: Chaos and predictability
blurb: Determinism without predictability — stretching and folding, Lyapunov exponents and times, what is actually computable, and how to avoid crying chaos at every irregular signal.
depth: 4
tags: [mechanisms, chaos, Lyapunov, predictability, attractor, forecasting]
---

# Chaos and predictability

> **One-line picture.** Chaos is *deterministic stretching and folding*: no randomness in the law, but
> exponential amplification of ignorance in the state. It converts an arbitrarily small uncertainty into
> a large one within a predictable time — the **Lyapunov time** — and that time is a measurable property
> of the system, not a philosophical attitude.
>
> **Prerequisites.** [Nonlinearity & mode coupling](04-nonlinearity-and-mode-coupling.md),
> [Random walks, Langevin, response](../01-foundations/08-random-walks-langevin-response.md) ·
> **Leads to.** [Phase transitions & criticality](06-phase-transitions-and-criticality.md),
> [Inverse problems & data assimilation](../07-numerics/10-inverse-problems-and-data-assimilation.md)

## L1 · The everyday version

Weather forecasts fail not because the equations are wrong but because the atmosphere *stretches*
differences between two nearly identical states until they become O(1). A butterfly's flap does not
cause the storm; here is the honest version: **two states that agree to within measurement precision
today will disagree completely in a finite, computable time** — about ten days for weather, about a
second for a cup of turbulence, about an hour for the rotation of an irregular moon.

Three things chaos is *not*:

* **not noise** — the rule has no random numbers; rerun the same simulation and you get the same answer;
* **not unpredictability of everything** — *statistics* (averages, distributions, spectra) often remain
  predictable long after individual trajectories are lost, which is why climate is predictable and
  weather is not;
* **not the same as turbulence** — chaos can be low-dimensional (three variables suffice), whereas
  [turbulence](../02-bulk/05-turbulence-and-eddy-diffusivity.md) is spatiotemporal chaos with an
  enormous number of active modes. The *mechanism* (stretching) is shared; the bookkeeping is not.

## L2 · Stretching, folding, and the Lyapunov exponent

Take two copies of a system with initial separation $\varepsilon$. Chaotic flow does two things:
it **stretches** (separations grow) and **folds** (they are bent back into the bounded region where the
motion lives). Stretching alone makes the separation grow as $\varepsilon e^{\lambda t}$, where
$\lambda$ is the **largest Lyapunov exponent**; folding is what keeps the motion bounded while making it
aperiodic and mixing.

* $\lambda\le0$: nearby states converge — predictable, periodic or steady;
* $\lambda>0$: nearby states diverge exponentially — the **predictability horizon** is
  $t_h\sim\frac{1}{\lambda}\ln(\Delta/\varepsilon)$;
* the **Lyapunov time** $t_\lambda=1/\lambda$ is the natural clock: after a few of them, nothing about
  the trajectory survives.

![**Figure R5.** Chaos in the Lorenz system. Left: two trajectories started $10^{-6}$ apart trace the
same butterfly but cease to be the same trajectory. Right: the separation grows exponentially (dashed
line: slope = the Lyapunov exponent $\lambda\approx0.91$) until it saturates at the size of the
attractor. Here the Lyapunov time is about 1.1 time units, so $10^{-6}$ becomes O(1) in about 14 of
them.](../../figures/chaos-sensitive-dependence.svg)

![**Animation A5.** Two trajectories started $10^{-6}$ apart, drawn as they evolve. The
separation grows exponentially until it saturates: after the Lyapunov time the two copies
agree about nothing except the statistics.](../../figures/anim-lorenz-divergence.webp)

Lyapunov times across the sciences, as commonly quoted (see the [bibliography](11-bibliography.md) for
provenance) — the spread of *fourteen orders of magnitude* is the point:

| System | Order of the Lyapunov time |
|---|---|
| Rotation of the moon Hyperion (tumbling) | about 36 days |
| Solar system (orbital chaos) | 5 million years (Pluto: 20 Myr) |
| Chemical reaction with oscillations | minutes (5.4 minutes quoted for a specific chaotic reaction) |
| Hydrodynamic ("a cup of water") | about 1–2 seconds |
| Molecular dynamics of argon | $\sim10^{-11}$ s (a few tens of picoseconds) |

The same mathematics appears as a growing, then saturating, separation curve; the practical question is
always *which* exponent and *at what amplitude the saturation sets in*, because that ratio is the
horizon.

![**Figure R6.** The standard road into chaos: the logistic map's period-doubling cascade (left), and the
Lyapunov exponent that *sees* it (right, red where positive). Note the windows inside the chaotic band
where $\lambda<0$ again: order is not abolished, it recurs at infinitely many parameter values. The same
cascade, with the same Feigenbaum constants, appears in a dripping tap, a driven pendulum and a
convection loop.](../../figures/routes-to-chaos.svg)

## L3 · The formal apparatus, and what it buys

* **Definitions.** For a flow on a compact invariant set, take the linearised flow along an orbit,
  reorthonormalise repeatedly, and the growth rates are the Lyapunov spectrum
  $\lambda_1\ge\lambda_2\ge\cdots$. Chaos means $\lambda_1>0$; the sum of the exponents is the mean
  divergence of the flow and, by **Pesin's identity**, the sum of the *positive* exponents equals the
  Kolmogorov–Sinai entropy — the rate at which the system creates information about its own initial
  condition.
* **Attractors can be fractal.** The Kaplan–Yorke formula turns the spectrum into an effective
  dimension, which is how a continuous system acquires a non-integer geometry — the strange attractor.
* **Shadowing.** A computed chaotic trajectory is *not* the true one, but the shadowing lemma (and its
  numerical versions) shows it usually follows a *true* trajectory from slightly different initial data.
  This is why chaotic simulations still produce correct *statistics* while saying nothing about the
  particular orbit — the single most useful idea here for anyone who runs a code.
* **Routes.** Period doubling (Feigenbaum universality), intermittency, and quasi-periodicity
  (Ruelle–Takens) are the generic roads; each has its own scaling signatures, all measurable.
* **Control and synchronisation.** A positive exponent is not a sentence: tiny, well-timed parametric
  kicks stabilise a chosen orbit (*chaos control*, OGY), and two chaotic systems can lock their states
  when coupled (*chaos synchronisation*) — the idea behind some secure-communication schemes.

## L4 · Using chaos honestly

1. **Estimate exponents with care.** Integrate the variational (or adjoint) equations and reorthonormalise
   (QR) each step; discard transients; check convergence in time and with initial condition. A single
   finite-time exponent is a number, not a verdict — its *fluctuations* are often as large as its mean.
2. **Never diagnose chaos from a wiggly signal.** Finite data from noisy, non-stationary or
   periodic-with-irregular-amplitude systems can masquerade as chaotic. Use surrogate-data tests, report
   the convergence of $\lambda$, and prefer a mechanism (stretching in a known model) to a visual
   impression.
3. **Separate the two horizons.** There is a *dynamical* horizon (Lyapunov time) and a *model-error*
   horizon (parameter and closure errors growing along the same stretched directions). In practice model
   error dominates: forecasting systems are limited by the second long before the first.
4. **Exploit ensembles.** Since individual trajectories are lost, the useful product is a distribution:
   ensembles quantify the spread, and data assimilation anchors it to observations
   ([inverse problems](../07-numerics/10-inverse-problems-and-data-assimilation.md)).
5. **Treat the statistics as the deliverable.** Spectral slopes, transport coefficients and rare-event
   rates are a chaotic system's real output; the individual trajectory is an implementation detail.