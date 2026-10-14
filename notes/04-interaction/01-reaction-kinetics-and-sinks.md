---
title: Reaction kinetics & chemical sinks
blurb: Orders, Arrhenius, autocatalysis, saturation and scavenging — the source term that makes transport equations nonlinear.
depth: 2
tags: [Arrhenius, kinetics, Michaelis-Menten, scavenging, stiff]
---

# Reaction kinetics & chemical sinks

> **One-line picture.** Put a local algebraic function on the right-hand side of the transport
> equation and everything can change: sharp fronts, multiple steady states, oscillations, and a
> stiffness problem for your solver.
>
> **Prerequisites.** [balance laws](../01-foundations/01-balance-laws-and-flux.md) ·
> **Leads to.** [autocatalysis](03-autocatalysis-and-oscillations.md),
> [reaction–diffusion & Turing](04-reaction-diffusion-and-turing.md),
> [fronts](05-fronts-and-travelling-waves.md)

## L1 · The rate laws, and what each one does

Reaction terms are **local** in space (no spatial derivatives) but usually **nonlinear** in
concentration. The order of the reaction is the exponent with which concentration enters:

| Rate law | Form | Characteristic behaviour |
|---|---|---|
| zero order | $R=k_0$ | constant production until a reactant runs out: linear growth |
| first order | $R=-k_1c$ | exponential decay, half-life $\ln2/k_1$ |
| second order | $R=-k_2c^2$ | decays as $1/t$; sharp fronts in space |
| bimolecular | $R=-kc_Ac_B$ | couples two species; quadratic in each |
| Michaelis–Menten / Hill | $R=-V_{\max}c/(K_m+c)$, $c^n/(K^n+c^n)$ | saturating (zero-order at high $c$, first-order at low $c$); Hill gives switch-like response |
| autocatalytic | $R=+kc(1-c)$ | growth that accelerates: fronts and travelling waves |
| Langmuir–Hinshelwood | $R\propto c/(1+Kc)^2$ | surface catalysis; can be non-monotone |
| scavenging (pseudo-first order) | $R=-k'c$ with $k'=k c_{\rm scav}$ | removal by an abundant partner: radical chemistry, quenching |

Temperature enters through **Arrhenius**: $k=Ae^{-E_a/(RT)}$. Doubling the rate roughly needs
$10$–$20$ K for typical $E_a$ — which is why combustion is nonlinear in the worst way, and why
biological rates are so temperature-sensitive.

## L2 · Why scavenging deserves its own name

A scavenger is a third species that removes your target by reaction — the OH radical removing a
pollutant, an antioxidant removing a radical, a chelator sequestering a metal. Two regimes matter:

* **Abundant scavenger** — the reaction is pseudo-first-order and you can forget the scavenger
  entirely; decay is exponential.
* **Depletable scavenger** — the removal rate slows as the scavenger is used up, producing
  non-exponential decay, and you must solve a coupled pair of PDEs
  ([cross-effects](../03-microscopic/06-cross-effects-and-multicomponent.md)).

Numerically, this is the classic first-order/second-order coupling problem: the same code structure,
two very different behaviours.

## L3 · What the mathematics guarantees

* **Comparison and positivity.** Monotone (decreasing) sinks preserve positivity and, with a
  maximum principle, let you bound solutions without solving them.
* **Multiple steady states.** Non-monotone kinetics or autocatalysis can produce several steady
  solutions — the classic $\mathrm{Da}$–$c$ hysteresis curve — with ignition and extinction points
  ([variational inequalities & hysteresis](../06-beyond/12-variational-inequalities-and-hysteresis.md)).
* **Competition between transport and reaction.** With $\mathrm{Da}\gg1$ the reaction is confined to
  thin sheets (flames, biofilms), producing boundary-layer structure; with $\mathrm{Da}\ll1$ the
  reaction is space-filling and transport-limited.
* **Stiffness.** Rate constants can exceed transport rates by many orders of magnitude (radical
  chemistry, combustion): eigenvalues of the reaction Jacobian span $10^{10}$, which forces
  implicit integration ([stiffness](../07-numerics/02-cfl-stiffness-and-time-integration.md)).

## L4 · Numerics

* **Treat sinks implicitly.** An explicit negative source can drive concentrations negative and blow
  up; implicit treatment is unconditionally positive for linear decay.
* **Operator splitting** separates transport and reaction, each with an appropriate method (Strang
  splitting for second order), at the cost of a commutator error that matters when both are fast
  ([splitting & coupling](../07-numerics/05-operator-splitting-and-multiphysics-coupling.md)).
* **Preserve positivity and invariant regions.** Adaptive time stepping driven by relative change
  (not absolute) is essential when concentrations span many decades; log-space formulations help.
* **Benchmarks**: the ROBER problem (classic stiff kinetics), the Oregonator, and Arrhenius
  ignition-delay correlations ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Learned kinetic mechanisms consistent with thermodynamics; multiscale coupling of
  quantum chemistry to reactor-scale transport; stochastic reaction networks at low copy numbers
  ([stochastic PDEs](../06-beyond/07-stochastic-pdes-and-random-media.md)).

## Checks

1. Which rate law gives exponential decay, and which gives a $1/t$ tail? *(First order; second
   order.)*
2. Why is Arhenius temperature dependence dangerous numerically? *(Small temperature errors produce
   exponentially large rate errors, coupling the energy equation to the chemistry very strongly.)*
3. When can a scavenging reaction be treated as first order? *(When the scavenger concentration is
   approximately constant — abundant or continuously replenished.)*

## See also

[Autocatalysis & oscillations](03-autocatalysis-and-oscillations.md) ·
[Reaction–diffusion & Turing](04-reaction-diffusion-and-turing.md) ·
[Fronts & travelling waves](05-fronts-and-travelling-waves.md) ·
[Time integration & stiffness](../07-numerics/02-cfl-stiffness-and-time-integration.md)
