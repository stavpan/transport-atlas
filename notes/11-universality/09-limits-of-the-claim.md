---
title: Limits of the claim
blurb: Where the universality argument is a theorem, where it is a model, and where it is only a metaphor — the honest boundary conditions.
depth: 3
tags: [limits, philosophy-of-science, identifiability, semantics, honesty]
---

# Limits of the claim

> **One-line picture.** The claim is that a balance law plus a driver generates *a* transport model for anything
> countable — not that the world is a PDE, not that such models are unique, and not that they capture meaning,
> purpose or agency. A claim that cannot state its limits is not a claim.
>
> **Prerequisites.** [Why everything flows](01-why-everything-flows.md) ·
> **Leads to.** back to [the universality index](index.md) with clearer eyes

## L1 · What is *not* being claimed

* **Not a physical theory of everything.** Transport equations describe the *redistribution* of quantities; they
  do not explain why the quantities exist, what they mean, or which of them matter.
* **Not that everything *is* a PDE.** Many systems are discrete, combinatorial, semantic or strategic. What is
  universal is that one can often *write a transport model* for a distribution over their states — a modelling
  statement, not an identity.
* **Not uniqueness.** Different mechanisms commonly produce the same macroscopic transport: the map from
  mechanism to equation is not injective.
* **Not a substitute for measurement.** A density you cannot observe is a theoretical object; without an
  operational definition, "the density" can be unfalsifiable
  ([inverse problems](../07-numerics/10-inverse-problems-and-data-assimilation.md)).
* **Not explanation.** Fitting a transport law predicts; it does not, by itself, explain. That gap is permanent
  and deserves a sentence in every paper.

## L2 · The gaps, itemised

| Gap | What it means | What can be done |
|---|---|---|
| **Discrete/combinatorial structure** | graphs, languages, games, proofs have structure that is not a density | transport *distributions over structures*; mean-field limits of random structures; accept combinatorial hardness |
| **Semantics and meaning** | Shannon information is not meaning; no balance law conserves sense | stay silent, or model meaning statistically (embeddings) while saying it is not conserved |
| **Purpose, norms, agency** | goals are not conserved quantities; "should" is not a drift term | use optimality/control structure for *rational* behaviour, and state that the objective is an assumption |
| **Non-measurable quantities** | no observable ⟹ no density | define the observable first; write the measurement model explicitly |
| **Emergence and information loss** | coarse-graining destroys information; memory and noise are the residue | Mori–Zwanzig-style corrections; never invert a reduced model and claim mechanism |
| **Non-identifiability** | many mechanisms, one transport law | design experiments that separate mechanisms; report a resolution analysis |
| **Mean-field breakdown** | fluctuations dominate in small/finite systems | agent-based or stochastic simulation; fluctuation-corrected closures |
| **Universality over-claiming** | power laws are not the only heavy tails: lognormal, stretched exponential and mixtures are common | fit tails properly; compare families; report model selection |
| **Formal limits** | no theory proves everything about itself; a universal *class of models* is not a *universal theory* | distinguish the toolbox (this atlas) from a theory of everything |
| **Ethics and intervention** | models of people change people; parameters are policy-dependent | give conditional predictions; be explicit about normativity; treat the Lucas critique as a modelling constraint |

## L3 · The four-question test

Before claiming that your problem "is a transport problem", answer these four:

1. **What is conserved** — or conserved up to stated sources and sinks? If nothing, stop.
2. **What is measured**, and how does the measured quantity relate to the modelled density?
3. **What is the geometry** — which metric makes the dynamics a descent, a flow, or a transport?
4. **Where does the continuum/mean-field assumption break**, and what is your fallback?

Answer all four and the machinery of this atlas applies: you may cite classification, well-posedness and numerical
results with confidence. Fail on (2) or (4) and you have a hypothesis, not a result — and the honest move is to
say so.

> [!warning] Trap
> Two seductive errors. **Over-extension**: "everything is diffusion", producing unfalsifiable papers.
> **Under-extension**: "it is only a metaphor", throwing away genuinely transferable theorems. The four-question
> test is the practical middle, and it costs five minutes.

## L4 · Working across fields without fooling yourself

* **Pre-register the mapping**: quantity, flux, driver, metric — written down *before* fitting.
* **State the identifiability plan**: which observation separates your mechanism from its rivals?
* **Test the mean-field condition empirically**: compare continuum predictions with agent or particle simulation
  at several sizes ([why everything flows](01-why-everything-flows.md)).
* **Report the mapping's failures**, not just its fits — failures are where the next model comes from.
* **Keep a falsification list**: what observation would make you abandon the transport description?
* **Separate the four claims in the write-up**: prediction, mechanism, meaning and policy have different evidence
  standards, and mixing them is the most common way good mathematics becomes bad science.

## Checks

1. Give a case where a transport model fits excellently but explains nothing. *(Any power-law tail: several
   mechanisms produce it, so the fit constrains the exponent, not the mechanism.)*
2. Why is "information is conserved" false? *(Information about a system is dissipated at a computable rate, and
   information is not meaning.)*
3. What is the difference between a universal *class of models* and a universal *theory*? *(A class can represent
   many systems while proving nothing about them; a theory makes falsifiable claims.)*
4. Which two questions most often expose over-claiming? *(What is measured? Where does the mean-field assumption
   break?)*

## See also

[Why everything flows](01-why-everything-flows.md) ·
[The decision tree & lookup](02-decision-tree-and-lookup.md) ·
[Inverse problems & data assimilation](../07-numerics/10-inverse-problems-and-data-assimilation.md) ·
[Measurement & experiments](../10-appendix/05-measurement-and-experiments.md) ·
[The Atlas](../00-atlas/index.md)

