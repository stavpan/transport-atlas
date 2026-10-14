---
title: The intersections map
blurb: The generative move of this part — put two mechanisms in the same equation and watch a new phenomenon appear. A curated map, a list of named combinations, and a recipe for building models on purpose.
depth: 4
tags: [mechanisms, intersections, combinations, modelling, recipes, cross-fertilisation]
---

# The intersections map

> **One-line picture.** Every phenomenon in this atlas is (at least) two mechanisms sharing one equation.
> Once you can name the mechanisms separately, you can *build* the phenomenon deliberately: pick a base
> law, add one mechanism from column A and one from column B, check which dimensionless number decides
> the outcome, and the behaviour is usually recognisable before you compute anything.
>
> **Prerequisites.** Notes [1](01-equilibria-and-critical-points.md)–[9](09-noise-induced-phenomena.md)
> of this part — the map below is their intersection table ·
> **Leads to.** [Crossings & cross-fertilisation](../13-panta-rhei/05-crossings-and-cross-fertilisation.md),
> [the bibliography](11-bibliography.md)

## L1 · Why intersections are where the action is

Nothing interesting happens in a one-mechanism system: pure diffusion smooths, pure advection translates,
a pure oscillator oscillates forever. Each *single* mechanism is boringly predictable. Add a second and
the system acquires a *choice* — a threshold, a pattern, a wave, a crisis — and with the choice comes
everything worth studying.

This is not a metaphor. It is a fact about equations: a linear equation is a superposition of independent
modes (note [4](04-nonlinearity-and-mode-coupling.md)), and the moment two terms of different character
appear together their ratio becomes a dimensionless number that *classifies the behaviour*. That is what
all the cards in the [dimensionless-number appendix](../10-appendix/02-dimensionless-number-cards.md) are:
the names of the intersections.

## L2 · Reading the map

![**Figure R11.** The intersections map: rows and columns are the nine mechanisms of this part, the
cells are what appears when both are present in one model. Only the upper triangle is filled
(combinations are symmetric). Colour marks the *kind* of outcome, because that is usually the most
useful thing to know first: something structured appears, a new failure mode appears, memory enters, noise
or feedback becomes a tool, or an exact law constrains what is possible. It is a curated map, not a
measurement — but every cell on it has a literature.](../../figures/intersections-matrix.svg)

## L3 · Named combinations: the folk taxonomy

Almost every named phenomenon in transport-adjacent science is a two-mechanism sentence. Learning the
taxonomy is the cheapest form of expertise available.

| Combination | Named phenomenon | The equation that shows it |
|---|---|---|
| nonlinearity + dispersion | **solitons**, cnoidal waves | KdV, NLS ([integrable systems](../06-beyond/14-integrable-systems-and-solitons.md)) |
| nonlinearity + diffusion | **travelling fronts**, Fisher waves | $\partial_tu=u(1-u)+u_{xx}$ ([fronts](../04-interaction/05-fronts-and-travelling-waves.md)) |
| nonlinearity + diffusion + two species | **Turing patterns** | Gray–Scott, Schnakenberg ([reaction–diffusion](../04-interaction/04-reaction-diffusion-and-turing.md)) |
| nonlinearity + noise | **stochastic resonance**, noise-induced transitions | [note 9](09-noise-induced-phenomena.md) |
| nonlinearity + delay | **delay-induced chaos**, Mackey–Glass oscillations | [delay transport](../06-beyond/16-delay-and-retarded-transport.md) |
| nonlinearity + coupling | **synchronisation**, chimera states | [Kuramoto](../13-panta-rhei/03-collective-behaviour-and-synchrony.md) |
| nonlinearity + feedback | **limit cycles**, multistability, hysteresis | [variational inequalities](../06-beyond/12-variational-inequalities-and-hysteresis.md) |
| memory + diffusion | **anomalous (sub/super) diffusion** | fractional operators ([anomalous diffusion](../03-microscopic/08-anomalous-diffusion.md)) |
| memory + conservation | **non-Markov thermodynamics**, memory-dependent second law | [memory & viscoelasticity](../06-beyond/04-memory-viscoelastic-and-hereditary.md) |
| geometry + randomness | **anomalous transport in random media**, trapping | [homogenisation](../06-beyond/08-homogenization-and-upscaling.md) |
| geometry + coupling | **metastability, clustering on networks** | [networks & traffic](../08-bridges/09-networks-society-and-traffic.md) |
| scaling + noise | **extreme-value statistics, first-passage scaling** | [scaling note 7](07-scaling-and-self-similarity.md) |
| thresholds + slow drive | **self-organised criticality**, avalanches | [criticality note 6](06-phase-transitions-and-criticality.md) |

## L4 · A recipe for building a model on purpose

1. **Write the base balance law** — the one sentence everything else modifies
   ([balance laws](../01-foundations/01-balance-laws-and-flux.md)). Name the density and the flux.
2. **Add exactly one mechanism from the diagonal.** Now you have a working model with a known behaviour:
   diffusion smooths, advection translates, reaction saturates, coupling synchronises.
3. **Add the mechanism you actually care about**, and immediately form the dimensionless number that
   compares it with the first: this is the parameter whose value *classifies* the regime
   ([dimensionless cards](../10-appendix/02-dimensionless-number-cards.md)). If no such number exists,
   the two mechanisms are not in competition — check the units again.
4. **Ask the map what should appear.** Structure? Crisis? Memory? If the model does something the map does
   not predict, you have either made an error or found something — and the map tells you which literature
   to consult in either case.
5. **Verify the intersection experimentally.** Change the mechanism's strength by a factor of ten and
   confirm that the phenomenon follows the dimensionless number rather than the raw parameters. That
   single test distinguishes a real intersection from a coincidence of one parameter set.

Two warnings, both learned the hard way. First, **three-mechanism systems are where surprises live**: the
map's cells are pairwise, but reality is usually a triangle (nonlinearity + noise + delay; geometry +
randomness + coupling), and the triangle is genuinely harder. Second, **do not confuse a naming scheme
with an explanation**: the map tells you where to look, not what *causes* what. Causality still has to be
argued — by intervention, by scaling, or by an experiment.

Three habits make the map pay:

* **Read the cells as *sentences*.** "Nonlinearity × Dispersion = solitons" means: form an equation with
  a steepening term and a spreading term of comparable strength, and the hump becomes a particle. The
  *named phenomenon* is the sentence's subject; the mechanism pair is its grammar.
* **Colour first, details later.** If a problem shows a *new failure mode*, look for a crisis
  intersection (noise, delay, geometry, feedback); if it shows *structure*, look for a pattern
  intersection (nonlinearity, coupling, geometry); if it shows *memory*, look for delay or memory entering
  a transport law.
* **The diagonal is a trap.** "Nonlinearity × Nonlinearity" is not two mechanisms; it is one mechanism
  squared, and the phenomena on the diagonal (mode coupling, mixed noise, nested feedback) are the hardest
  to model because there is no separation of scales to exploit.