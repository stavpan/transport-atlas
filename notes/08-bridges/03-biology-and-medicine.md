---
title: Transport in biology & medicine
blurb: Diffusion limits cells, reaction–diffusion builds bodies, and transport physics explains tumours, drug delivery, kidneys and nerve impulses.
depth: 2
tags: [biology, medicine, morphogen, tumour, drug delivery, cable equation]
---

# Transport in biology & medicine

> **One-line picture.** Life is a fight against diffusion: too slow to feed a cell body, exactly right
> for signalling, and fatal when it fails.
>
> **Prerequisites.** [diffusion](../03-microscopic/01-diffusion.md),
> [reaction–diffusion & Turing](../04-interaction/04-reaction-diffusion-and-turing.md)

## L1 · Diffusion limits the size of life

Oxygen must reach a cell interior by diffusion when no vessels are present. With
$D\approx2\times10^{-9}$ m²/s and a need for ~1 s of supply, the accessible radius is roughly
$r\sim\sqrt{Dt}\approx50$–$200$ µm. That is the scale of a capillary spacing, of an avascular tumour's
necrotic core, and of the reason insects can breathe by tubes (tracheae) but not grow large like
vertebrates. **Diffusion sets the plumbing.**

The same scaling appears in drug delivery (diffusion of a drug out of a polymer implant, or into a
biofilm), in tissue engineering (how thick a scaffold can be), and in pharmacokinetics (compartmental
models are just lumped resistance–capacitance networks —
[circuit models](01-analogy-and-circuit-models.md)).

## L2 · Four biological transport mechanisms worth knowing

| Mechanism | Equations | Role |
|---|---|---|
| signalling by morphogens | reaction–diffusion, Turing patterns | patterning of digits, hair, stripes; robustness requires gradients of ligands/receptors |
| chemotaxis | Keller–Segel | immune recruitment, bacterial foraging, slime-mould aggregation |
| nerve conduction | cable equation (telegrapher-like) | action potentials as travelling waves in excitable media |
| electrochemical transport | Nernst–Planck + Poisson | membrane potentials, ion channels, kidneys, nerve, salt balance |
| tissue mechanics coupling | poroelasticity + transport | cartilage, bone remodelling, interstitial flow, oedema |
| blood–tissue exchange | convection–reaction in vessels + diffusion | oxygen/glucose delivery, drug distribution |

**Travelling waves in excitable media** are the reason cardiac tissue has a refractory period: fronts
become spiral waves, and spiral breakup is fibrillation. The mathematics is identical to the
[reaction–diffusion fronts](../04-interaction/05-fronts-and-travelling-waves.md) of combustion.

## L3 · Transport reasoning that changes decisions

* **Diffusion limitation predicts hypoxic cores** in tumours and hence which therapies (or which sizes of
  spheroid) are realistic.
* **Microscale Péclet numbers govern drug penetration**: in tumour interstitium, slow interstitial flow
  plus binding gives non-Fickian, retarded transport —
  [sorption & retardation](../04-interaction/07-sorption-and-retardation.md).
* **Reaction–diffusion models without parameters are useless**: the same equations with different
  rate constants give spots, stripes or travelling waves — the parameters must be estimated
  ([inverse problems](../07-numerics/10-inverse-problems-and-data-assimilation.md)).
* **Anomalous diffusion is the norm inside cells** (crowding, cytoskeleton, molecular motors): measured
  exponents $\alpha<1$, ergodicity breaking, and subtle dependence on probe size
  ([anomalous diffusion](../03-microscopic/08-anomalous-diffusion.md)).

## L4 · Practice

* **Do not measure a biological coefficient with a Fickian model if the transport is anomalous** — you
  will get a length- and time-dependent number.
* **Couple the mechanics**: growth, swelling and transport are coupled through poroelasticity; ignoring
  it produces wrong drug release and wrong tumour-induced stress predictions.
* **Use dimensionless groups for scale-up**: oxygen penetration depth, Thiele modulus (reaction vs
  diffusion in a biofilm), and Péclet numbers in vessels decide the regime.
* **Frontiers.** Single-molecule and single-cell transport in living tissue; multiscale models from
  channels to organs; mechano-transport coupling in disease; learned constitutive laws for tissue.

## Checks

1. Why can a cell not be 1 cm across without a vascular supply? *(Oxygen diffusion over 1 cm would take
   hours-to-days.)*
2. Why is the cable equation "telegrapher-like"? *(It carries a diffusive current along the axon plus a
   membrane capacitance, giving wave propagation with damping.)*

## See also

[Reaction–diffusion & Turing](../04-interaction/04-reaction-diffusion-and-turing.md) ·
[Chemotaxis & Keller–Segel](../04-interaction/06-chemotaxis-and-keller-segel.md) ·
[Charged & electrochemical transport](../03-microscopic/07-charged-and-electrochemical-transport.md) ·
[Anomalous diffusion](../03-microscopic/08-anomalous-diffusion.md)
