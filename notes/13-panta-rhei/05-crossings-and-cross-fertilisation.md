---
title: Crossings and cross-fertilisation
blurb: Where one field's mechanism solves another field's problem — the honest rules of transfer, the famous successes, the well-documented failures, and a worked mini-example.
depth: 4
tags: [panta rhei, cross-fertilisation, analogy, transfer, modelling, failures]
---

# Crossings and cross-fertilisation

> **One-line picture.** The same equation in a different subject is not a coincidence — it is a *free
> research programme*. But the transfer only works when the objects being transported, the conserved
> quantities and the relevant dimensionless numbers actually correspond. This note is about doing it
> consciously: the successes, the conditions, and the failures that are now textbook.
>
> **Prerequisites.** [The intersections map](../12-recurring-mechanisms/10-intersections-map.md),
> [Why everything flows](../11-universality/01-why-everything-flows.md) ·
> **Leads to.** [Limits of the claim](../11-universality/09-limits-of-the-claim.md),
> [the river as a model](06-the-river-as-a-model.md)

## L1 · Ideas migrate

The history of transport theory is largely a history of *imports*:

* **Fourier's heat equation** (1822) became diffusion in chemistry, Brownian motion in physics, thermal
  noise in electronics, and — via the Black–Scholes equation — option pricing in finance.
* **The Ising model** (1925, magnets) became opinion dynamics, segregation models, neural networks and
  the mathematics of phase transitions in general.
* **Sandpile criticality** (1987, toy physics) became earthquake statistics, forest-fire models, solar
  flares, neuronal avalanches and (much more speculatively) financial crashes.
* **The SIR epidemic model** (1927) became the mathematics of rumours, computer malware, innovation
  diffusion and social contagion.
* **The Fokker–Planck equation** became the theory of learning and sampling in machine learning, of
  molecular motors, and of population genetics.
* **Optimal transport** (1781, moving earth) became a theory of gradient flows, of image registration,
  and of generative models in machine learning.

Why it works: the objects of a transport model are *generic* — a conserved quantity, a flux, a
constitutive law, a boundary condition. If your new field has those four things, it inherits the whole
mathematical apparatus, including its theorems *and its known failure modes*.

## L2 · Three kinds of crossing (and their different warranties)

| Kind | What is transferred | Warranty | Example |
|---|---|---|---|
| **Isomorphism** | the exact equations | full: the theorems transfer verbatim | heat ↔ diffusion ↔ Black–Scholes (for log-prices, without jumps) |
| **Analogy** | the structure, not the equations | partial: predictions must be re-derived | fluid turbulence ↔ financial volatility cascades |
| **Technique** | a method (asymptotics, scaling, a numerical scheme) | only as good as the mapping it is applied to | dimensional analysis imported from fluid mechanics into biology |

The most common error is mistaking an **analogy** for an **isomorphism**. An isomorphism lets you import
*results*; an analogy lets you import *questions*. Both are useful, but only one lets you skip the work.

## L3 · When the crossing holds, and when it famously does not

**The five conditions for a successful transfer.** Check them *before* writing the paper:

1. **A conserved (or at least balanced) quantity** exists in the target field. If you cannot name it, you
   do not have a transport model — you have a metaphor.
2. **The same symmetry or constraint** holds (a maximum principle, positivity, reciprocity, a divergence
   condition). Laws that depend on a symmetry are only as valid as that symmetry in the new context.
3. **The dimensionless number exists** and has the same meaning. If the Reynolds number of a market
   cannot be defined operationally, the imported phenomenology has no anchor.
4. **The variables are measurable** in the target field, at the relevant scale. Quantities that only exist
   in the model (a "market pressure potential") are where the trouble starts.
5. **The boundary conditions are legitimate.** Equations are imported easily; *boundary conditions* are
   where most transfers fail — an open market, a free surface, and a magnet's edge are not the same
   object, and the solution depends on which one you chose.

**Documented failures and disputes**, included because a part about crossings that only listed successes
would be advertising:

* **Economics and physics-envy.** Borrowing equilibrium thermodynamics or sandpile criticality for
  financial markets produced elegant models and famously weak predictions; the 2008 crisis is the
  standard example of the cost. The mathematics transferred; the *identification of the conserved
  quantity* did not.
* **Criticality claims in neuroscience and ecology.** Power-law-like statistics have been reported
  everywhere, and alternatives (non-critical mechanisms, subsampling artefacts, estimator bias) explain
  many of the same numbers. The dispute is not whether the mathematics is right but whether the mapping
  is.
* **"Quantum" social science and consciousness.** Importing the vocabulary of quantum mechanics into
  psychology and decision theory has produced mostly unfalsifiable models, and it is the classic
  example of transferring the *words* rather than the *structure*.
* **Scale-free networks as a universal explanation.** The discovery was real and important; the
  subsequent habit of finding power laws in every network (often from biased sampling) is the reason the
  statistical caveats of [note 7 of part 12](../12-recurring-mechanisms/07-scaling-and-self-similarity.md)
  exist.

## L4 · A worked mini-example, and a reporting checklist

**Does traffic jam like a fluid or like a sandpile?** Both crossings have been made, and comparing them is
instructive:

* *Fluid crossing.* Treat cars as a compressible continuum with density $\rho$ and flux $q(\rho)$; the
  balance law gives a kinematic-wave (Lighthill–Whitham–Richards) model. Successes: the *upstream
  propagation* of traffic jams at a predictable speed, and shock formation as the mechanism of a jam's
  leading edge — both follow from the [conservation-law theory](../06-beyond/01-conservation-laws-and-shocks.md)
  with no new physics. Failures: the model's velocity is a function of density alone, so it cannot
  produce *spontaneous* jams out of smooth flow, because the underlying instability is missing.
* *Sandpile crossing.* Treat stop-and-go traffic as threshold relaxation with slow drive — a
  [self-organised-criticality](../12-recurring-mechanisms/06-phase-transitions-and-criticality.md)
  structure. Successes: the *power-law-like* distributions of jam sizes and the existence of a critical
  density, observed experimentally in the "jam without a bottleneck" experiments. Failures: exponents are
  not universal, and the "self-organised" part is fragile — the timescale separation is imposed by
  drivers, not guaranteed by the dynamics.
* *The lesson.* Each crossing captured something the other missed, and the decisive test was an
  **intervention**: change the driver behaviour (the coupling) and see whether the predicted scaling
  survives. That is the protocol.

**Reporting checklist for any imported mechanism.** (i) State the mapping explicitly, quantity by
quantity. (ii) State which parts of the mapping are *assumed* rather than derived. (iii) Give the
dimensionless number and its measured range. (iv) Name a prediction that would fail if the crossing is
wrong, and test it out of sample. (v) Report one competing mechanism that explains your data. Do these
five things and cross-fertilisation stops being a gamble and becomes a method.