---
title: Recurring mechanisms
blurb: The nine shapes that keep reappearing — equilibria, stability, bifurcation, nonlinearity, chaos, criticality, scaling, duality, noise — with the intersections where something new is born.
depth: 2
tags: [index, mechanisms, theory, foundations, recurring]
---

# Recurring mechanisms: the shapes that keep coming back

Part [11](../11-universality/index.md) argued that the *same balance law* shows up everywhere. This
part is the other half of the argument: **the same nine mechanisms** ride on top of that law, and once
you can recognise them you can recognise the behaviour of a system you have never met.

They are not models. They are *verbs*: a system settles (**equilibrium**), resists a nudge
(**stability**), changes character when a knob turns (**bifurcation**), lets parts talk to each other
(**nonlinearity**), forgets its beginnings (**chaos**), organises itself at the edge (**criticality**),
looks the same at every zoom (**scaling**), is secretly another problem in disguise (**duality**), and
is pushed around by chance (**noise**).

| # | Mechanism | The question it answers | The signature |
|---|---|---|---|
| 1 | [Equilibria & critical points](01-equilibria-and-critical-points.md) | Where does it stop? | $\dot{x}=0$; a stationary profile; a balance of fluxes |
| 2 | [Linearisation & stability](02-linearization-and-stability.md) | Does it come back? | eigenvalues of a Jacobian; a growth-rate curve $\lambda(k)$ |
| 3 | [Bifurcation theory](03-bifurcation-theory.md) | When does its character change? | a branch appearing, splitting, or exchanging stability |
| 4 | [Nonlinearity & mode coupling](04-nonlinearity-and-mode-coupling.md) | How do parts talk? | harmonics, cascades, shocks, solitons |
| 5 | [Chaos & predictability](05-chaos-and-predictability.md) | How far can I look ahead? | a positive Lyapunov exponent; a strange attractor |
| 6 | [Phase transitions & criticality](06-phase-transitions-and-criticality.md) | Where does order appear, and how sharply? | diverging correlation length; power-law avalanches |
| 7 | [Scaling & self-similarity](07-scaling-and-self-similarity.md) | What is the shape, independent of size? | exponents; data collapse; $\pi$-groups |
| 8 | [Duality & transforms](08-duality-and-transforms.md) | Is this another problem in costume? | an exact map that swaps hard for easy |
| 9 | [Noise-induced phenomena](09-noise-induced-phenomena.md) | What does chance *do*? | escapes, resonances, noise-selected states |

![**Figure R1.** Two completely different mechanisms, drawn in one frame: the *landscape* view of
settling (left) and the same information as a one-dimensional flow (right). Almost every mechanism in
this part has a landscape version and a flow version.](../../figures/energy-landscape-stability.svg)

## How to use this part

* **Diagnostically.** You have a system that does something surprising. Walk the table top to bottom:
  find its equilibria, linearise, ask whether a parameter is near a bifurcation, ask whether the
  nonlinearity is mixing modes, ask whether a Lyapunov time has expired. Nine times in ten the surprise
  is one of these nine.
* **Constructively.** You want to *build* a model with a given behaviour. Go to the
  [intersections map](10-intersections-map.md): combining two mechanisms from this list is the standard
  way new phenomena are discovered — and the standard way papers get titles.
* **Sceptically.** Every mechanism here has a failure mode in which it is *asserted* rather than
  demonstrated: "it's a power law" (not necessarily critical), "it has a butterfly effect" (not
  necessarily chaotic), "it's self-organised criticality" (not necessarily self-organised). Each note
  carries its own suspicion list; the [bibliography](11-bibliography.md) marks which sources are
  primary, review, or popular.

> **The one-sentence version.** A transport system has a small repertoire of behaviours, and the
> mathematical tools for each are mature — so the usual reason a strange behaviour is misdiagnosed is
> not missing theory but a missing translation between the phenomenon and the mechanism.

## Relation to the rest of the atlas

These notes are deliberately *level-crossing*: each one starts as an L1 picture you could tell a
child, and ends at L4 with what a practitioner computes, the traps in the computation, and where the
theory is still open. Links point back to the concrete notes where the mechanism is doing actual work:
[convection](../02-bulk/02-convection-and-buoyancy.md) for bifurcation,
[Turing patterns](../04-interaction/04-reaction-diffusion-and-turing.md) for mode competition,
[turbulence](../02-bulk/05-turbulence-and-eddy-diffusivity.md) for cascades,
[anomalous diffusion](../03-microscopic/08-anomalous-diffusion.md) for scaling,
[stochastic PDEs](../06-beyond/07-stochastic-pdes-and-random-media.md) for noise,
[delay](../06-beyond/16-delay-and-retarded-transport.md) for memory.
