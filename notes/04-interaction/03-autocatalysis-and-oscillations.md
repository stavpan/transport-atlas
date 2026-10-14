---
title: Autocatalysis & oscillations
blurb: Reactions that speed themselves up, clocks and waves that need no clockwork — excitability, limit cycles, and what happens when a Lyapunov function disappears.
depth: 3
tags: [autocatalysis, oscillation, limit cycle, excitable, BZ reaction]
---

# Autocatalysis & oscillations

> **One-line picture.** A reaction that produces its own catalyst accelerates itself; couple two of
> those with opposite signs and you get a clock. Nothing oscillates but the chemistry.
>
> **Prerequisites.** [reaction kinetics](01-reaction-kinetics-and-sinks.md) ·
> **Leads to.** [reaction–diffusion & Turing](04-reaction-diffusion-and-turing.md),
> [fronts & travelling waves](05-fronts-and-travelling-waves.md)

## L1 · Why oscillations are surprising

Most of this atlas is about things running downhill: entropy up, free energy down, gradients
smoothed. Oscillating chemistry violates that picture — the concentration of a species rises and
falls forever, without any external clock. The resolution is that a Lyapunov function is *not
guaranteed*: nonlinear systems can possess stable limit cycles instead of fixed points, and then the
"arrow" is replaced by a closed orbit.

The ingredients are always the same: **positive feedback** (autocatalysis, or inhibition of an
inhibitor) plus **delayed negative feedback** (depletion of a reactant), and enough nonlinearity to
keep the oscillation bounded.

## L2 · The archetypes

| Model | Skeleton | Behaviour |
|---|---|---|
| logistic growth | $\dot c=kc(1-c/K)$ | autocatalytic saturation; sigmoid approach to $K$ |
| Lotka–Volterra | $\dot x=x(a-by),\ \dot y=y(-c+dx)$ | conservative cycles (not a limit cycle) |
| Brusselator | feedback between two species | canonical limit-cycle oscillator |
| Oregonator | Belousov–Zhabotinsky reduction | clock reaction, excitable waves |
| glycolysis (Sel'kov) | product activates its own production | biochemical oscillations |
| excitable media (FHN) | fast activator, slow inhibitor | threshold behaviour, pulses, spiral waves |
| calcium dynamics | channels with feedback | intracellular waves |

The practical difference between an *oscillator* and an *excitable* medium is whether small
perturbations die out (excitable: they must exceed a threshold) or grow into a full cycle
(oscillatory).

## L3 · What the mathematics guarantees

* **Limit cycles are attractors.** For a stable limit cycle, trajectories converge to the orbit
  regardless of initial conditions: amplitude and frequency are properties of the dynamics, not of
  the data. (Contrast Lotka–Volterra, where the amplitude depends on the initial condition —
  structurally unstable.)
* **Hopfn bifurcations create them.** A fixed point loses stability as a parameter crosses a
  critical value and a small-amplitude cycle is born; the Poincaré–Andronov–Hopfn normal form gives
  the frequency at onset. This is the standard route in chemical and biological oscillators.
* **No Lyapunov function exists.** Consequently: no maximum principle, no monotone functional, no
  automatic contraction. Numerical schemes have no free nonlinear stability; check invariant regions
  explicitly.
* **Excitable media support waves and spirals.** A threshold-plus-refractory structure (as in
  cardiac tissue) gives travelling pulses, spiral waves and, if the medium is large enough,
  turbulence-like breakup — the mechanism of cardiac fibrillation and of chemical wave chaos.
* **Sensitivity to parameters is the norm.** Period and amplitude depend on rate constants
  exponentially (Arrhenius), so small temperature changes can switch a system from steady to
  oscillatory — which is exactly why biological clocks are temperature-compensated by design.

## L4 · Numerics

* **Long integration times are unavoidable.** Statistics of the cycle require many periods; error
  accumulates as *phase* drift rather than amplitude growth, so diagnostics must be
  phase-aware (Poincaré sections, period detection).
* **Stiffness and multiple time scales** (fast activator, slow inhibitor) demand implicit or
  IMEX schemes ([time integration](../07-numerics/02-cfl-stiffness-and-time-integration.md));
  explicit schemes are limited by the fastest scale and can spend all their effort there.
* **Positivity matters.** Oscillatory kinetics with negative excursions in a numerical scheme
  destroys the dynamics: use positivity-preserving or log-space integration.
* **Benchmarks**: Oregonator period/amplitude curves, FHN pulse speed, and spiral-wave tip
  trajectories ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Stochastic oscillations at low copy numbers; oscillatory dynamics coupled to flow
  (oscillating chemical reactors); control of fibrillation; single-cell clocks in tissues.

## Checks

1. Why is Lotka–Volterra *not* a genuine oscillator in the engineering sense? *(Its cycles depend on
   initial conditions: no attracting limit cycle, structurally unstable.)*
2. What is the difference between oscillatory and excitable? *(Excitable needs a suprathreshold
   perturbation to fire; oscillatory does not.)*
3. Which structural feature makes the analysis so much harder here than for diffusion?
   *(Absence of a Lyapunov function: no monotonicity, no maximum principle.)*

## See also

[Reaction kinetics](01-reaction-kinetics-and-sinks.md) ·
[Reaction–diffusion & Turing](04-reaction-diffusion-and-turing.md) ·
[Fronts & travelling waves](05-fronts-and-travelling-waves.md) ·
[Entropy & variational structure](../01-foundations/07-entropy-and-variational-structure.md)
