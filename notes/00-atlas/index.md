---
title: The Atlas
blurb: The brief master note — one balance law, four levels, and a machine-generated index of every note.
depth: 1
tags: [index, overview, reading paths]
---

# The Transport Atlas

> **One-line picture.** Almost every equation in this atlas is the same sentence:
> *things move, and nothing is lost.* The rest is bookkeeping: what moves (the flux),
> how it moves (the constitutive law), what it is made of (the state), and what pushes it.

Transport phenomena is the study of things that are **not in equilibrium** and therefore
move. Heat flows down a temperature gradient, salt spreads through water, momentum diffuses
across a shear layer, neutrons leak out of a reactor, probability drifts over a barrier,
traffic jams propagate upstream. The mathematics is astonishingly reusable, which is why
this atlas has a category of *bridges* to finance, biology, images, plasmas and machine learning.

::: epigraph
**πάντα ῥεῖ** · *all things flow*

All things flow — so the only honest way to describe anything is to say what moves, what carries it, and
what is conserved while it does. This atlas writes that sentence fifteen hundred ways; the
[Panta Rhei part](../13-panta-rhei/index.md) is the shortest of them.
:::

## The four levels

Every note is written as a ladder. Read only as far down as you need:

| Level | The question | Audience |
|---|---|---|
| **L1** | *What is it, in everyday words?* No mathematics. | curious beginner |
| **L2** | *Why does it happen, and what is the object?* Mechanism, the term in the equation, the dimensionless number. | undergraduate |
| **L3** | *What does the mathematics guarantee?* Well-posedness, spectra, limits, invariants, asymptotics. | graduate |
| **L4** | *What breaks, what is unsolved, how do you compute it?* Schemes, stability, open problems, structure. | practitioner |

The site is built four times: `dist/` (everything), and `dist/L1`, `dist/L2`, `dist/L3`
(the same notes with the deeper rungs trimmed away). Same URLs, shallower content.

## Reading paths

A few suggested routes; each is a chain of notes that only uses what came before.

* **"I know nothing yet."** [balance laws & flux](../01-foundations/01-balance-laws-and-flux.md) →
  [material derivative](../01-foundations/02-material-derivative.md) →
  [advection](../02-bulk/01-advection.md) → [diffusion](../03-microscopic/01-diffusion.md) →
  [constitutive relations](../01-foundations/03-constitutive-relations.md) →
  [dimensionless numbers](../01-foundations/05-dimensionless-numbers.md).
* **"I have a PDE and a computer."** [PDE taxonomy & boundary conditions](../01-foundations/04-pde-taxonomy-and-boundary-conditions.md) →
  [discretisation, consistency, stability](../07-numerics/01-discretization-consistency-stability-convergence.md) →
  [CFL & stiffness](../07-numerics/02-cfl-stiffness-and-time-integration.md) →
  [numerical diffusion](../07-numerics/03-numerical-diffusion-and-dispersion-error.md) →
  [limiters & WENO](../07-numerics/04-limiters-tvd-and-weno.md) →
  [solvers](../07-numerics/06-linear-solvers-and-preconditioning.md).
* **"Why is this all one subject?"** [spectral view](../01-foundations/06-spectral-and-green-function-view.md) →
  [entropy & variational structure](../01-foundations/07-entropy-and-variational-structure.md) →
  [random walks, Langevin, response](../01-foundations/08-random-walks-langevin-response.md) →
  [optimal transport & gradient flows](../06-beyond/10-optimal-transport-and-gradient-flows.md) →
  [one mathematics of transport](../08-bridges/11-unifying-mathematics-of-transport.md).
* **"Push me past ordinary PDEs."** [conservation laws & shocks](../06-beyond/01-conservation-laws-and-shocks.md) →
  [Hamilton–Jacobi & viscosity solutions](../06-beyond/02-hamilton-jacobi-and-viscosity-solutions.md) →
  [nonlocal & fractional](../06-beyond/03-nonlocal-and-fractional-operators.md) →
  [general classification](../01-foundations/10-general-pde-classification.md) →
  [higher order & dispersive](../01-foundations/11-higher-order-and-dispersive.md) →
  [dimensions & geometry](../01-foundations/12-dimensions-geometry-and-manifolds.md) →
  [integrable systems](../06-beyond/14-integrable-systems-and-solitons.md).
* **"Show me that this is everywhere."** [why everything flows](../11-universality/01-why-everything-flows.md) →
  [the lookup table](../11-universality/02-decision-tree-and-lookup.md) →
  [cognitive science & mind](../11-universality/03-cognitive-science-and-mind.md) →
  [algorithms](../11-universality/05-computation-and-algorithms.md) →
  [information & inference](../11-universality/07-information-statistics-and-inference.md) →
  [mathematics itself](../11-universality/08-mathematics-itself.md) →
  [limits of the claim](../11-universality/09-limits-of-the-claim.md).
* **"What keeps happening, everywhere?"** [equilibria & critical points](../12-recurring-mechanisms/01-equilibria-and-critical-points.md) →
  [linearisation & stability](../12-recurring-mechanisms/02-linearization-and-stability.md) →
  [bifurcation theory](../12-recurring-mechanisms/03-bifurcation-theory.md) →
  [nonlinearity & mode coupling](../12-recurring-mechanisms/04-nonlinearity-and-mode-coupling.md) →
  [chaos & predictability](../12-recurring-mechanisms/05-chaos-and-predictability.md) →
  [phase transitions & criticality](../12-recurring-mechanisms/06-phase-transitions-and-criticality.md) →
  [scaling](../12-recurring-mechanisms/07-scaling-and-self-similarity.md) →
  [duality & transforms](../12-recurring-mechanisms/08-duality-and-transforms.md) →
  [noise-induced phenomena](../12-recurring-mechanisms/09-noise-induced-phenomena.md) →
  [the intersections map](../12-recurring-mechanisms/10-intersections-map.md).
* **"Give me the theme, not the toolbox."** [Heraclitus and the river](../13-panta-rhei/01-heraclitus-and-the-river.md) →
  [beauty and the flow](../13-panta-rhei/02-beauty-and-the-flow.md) →
  [collective behaviour & synchrony](../13-panta-rhei/03-collective-behaviour-and-synchrony.md) →
  [irreversibility & the arrow of time](../13-panta-rhei/04-irreversibility-and-the-arrow-of-time.md) →
  [crossings & cross-fertilisation](../13-panta-rhei/05-crossings-and-cross-fertilisation.md) →
  [the river as a model](../13-panta-rhei/06-the-river-as-a-model.md).

## Universality: the strongest version of the claim

The atlas ends with a part devoted to the claim that this mathematics is not one subject among many but a
*common calculus of redistribution*: [Universality](../11-universality/index.md). Start with
[why everything flows](../11-universality/01-why-everything-flows.md) for the five structures that make a
model a transport model (balance, generator, functional, optimality, symmetry), then use the
[lookup table](../11-universality/02-decision-tree-and-lookup.md) to translate an object from *your* field.
The domain notes cover [mind and cognition](../11-universality/03-cognitive-science-and-mind.md),
[society, economics and language](../11-universality/04-social-behaviour-economics-language.md),
[algorithms](../11-universality/05-computation-and-algorithms.md),
[physics and field theory](../11-universality/06-physics-chemistry-and-field-theory.md),
[inference and information](../11-universality/07-information-statistics-and-inference.md) and
[mathematics itself](../11-universality/08-mathematics-itself.md) — and it ends, deliberately, with
[the limits of the claim](../11-universality/09-limits-of-the-claim.md), because a universality claim that
cannot state its boundaries is not a claim.

## The mechanisms that keep coming back

The atlas now has a part devoted not to *fields* but to **behaviours**: [recurring mechanisms](../12-recurring-mechanisms/index.md).
Nine of them — equilibria, linearisation and stability, bifurcation, nonlinearity and mode coupling, chaos,
criticality, scaling and self-similarity, duality and transforms, noise — each written as a ladder from a
child-sized picture at L1 to what a practitioner computes at L4, with its own suspicion list. The part ends
with the [intersections map](../12-recurring-mechanisms/10-intersections-map.md), which is the *generative*
piece: put two mechanisms in one equation and a named phenomenon appears (solitons, Turing patterns,
stochastic resonance, delay-induced chaos, avalanches), and a
[bibliography](../12-recurring-mechanisms/11-bibliography.md) marked by source type — primary, review,
sceptical — so that every claim can be checked rather than believed.

## Panta Rhei: the theme, taken seriously

Finally, a part named after the oldest version of the claim: [Panta Rhei](../13-panta-rhei/index.md) —
*all things flow*. It reads [Heraclitus' fragments](../13-panta-rhei/01-heraclitus-and-the-river.md) as a
question about identity under replacement, and answers it with the mathematics of this atlas (steady state,
Lagrangian structure, invariant measure). It takes [beauty](../13-panta-rhei/02-beauty-and-the-flow.md)
seriously enough to explain why flow makes patterns the eye trusts, treats
[synchrony](../13-panta-rhei/03-collective-behaviour-and-synchrony.md) as a transport problem for phase
density, gives the [arrow of time](../13-panta-rhei/04-irreversibility-and-the-arrow-of-time.md) its
transport statement, and finishes at the
[crossings](../13-panta-rhei/05-crossings-and-cross-fertilisation.md) — where one field's mechanism solves
another field's problem, including the cases where that went wrong — before closing on
[the river as a model](../13-panta-rhei/06-the-river-as-a-model.md).

## The map

Every figure here is generated from a script and audited for legibility (text is never below
8 pt, nothing is clipped, no two labels overlap), and seven of them are **animations** —
the phenomena that *are* motion, numbered A1–A7, which play in the web and single-file editions
and become four-panel filmstrips in print.

![**Figure 1.** Every note in the atlas, wired together. Colour marks the level at which a topic is first useful (blue L1, teal L2, violet L3, amber L4). The loops are real: homogenisation feeds subsidence, kinetic theory feeds turbulence closures, and optimal transport connects diffusion to geometry.](../../figures/concept-map.svg)

## Two habits that repay themselves

> **Trap number one: mistaking a *name* for an *equation*.** "Dispersion", "convection",
> "diffusion" and "absorption" each mean three or four different things in different
> communities. The [words that collide](../09-polysemy/index.md) notes exist to dismantle them.

> **Trap number two: forgetting the dimensions.** Before solving anything, form the
> dimensionless groups. They tell you which terms you may drop, how fine the grid must be,
> and whether your answer will be diffusion-like, wave-like or shock-like.
> See [dimensionless number cards](../10-appendix/02-dimensionless-number-cards.md).

## The catalogue

Every note, with a one-line description. It is generated from the notes themselves at build
time, so it is never out of date.

<!-- AUTO:CATALOG -->
