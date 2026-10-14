---
title: Chemotaxis & Keller–Segel
blurb: Cells that swim up a chemical gradient — and the aggregation instability that can concentrate them into a singularity.
depth: 3
tags: [chemotaxis, Keller-Segel, aggregation, blow-up, Patlak]
---

# Chemotaxis & Keller–Segel

> **One-line picture.** Bacteria do not diffuse; they *run and tumble* up a gradient. The resulting
> flux is directed transport, and it can destabilise an initially uniform suspension into clumps.
>
> **Prerequisites.** [diffusion](../03-microscopic/01-diffusion.md),
> [reaction–diffusion](04-reaction-diffusion-and-turing.md) · **Leads to.**
> [biology & medicine](../08-bridges/03-biology-and-medicine.md),
> [nonlinear diffusion](../06-beyond/06-nonlinear-diffusion-and-porous-medium.md)

## L1 · Active transport instead of random walks

A swimming cell samples its environment and biases its motion toward higher concentrations of an
attractant. Macroscopically that is a flux $-\chi c\nabla S$ with a *chemotactic sensitivity* $\chi$
(m²/s per unit gradient), added to diffusion. The classical model (Keller–Segel, 1970; Patlak 1953)
reads

$$\partial_tc=\nabla\!\cdot\!\big(D\nabla c-\chi c\nabla S\big),\qquad
\underbrace{\partial_tS=D_S\nabla^2S+kc-\lambda S}_{\text{signal produced by the cells}} .$$

Cells both *sense* and *produce* the signal, which closes a positive feedback: more cells → more
attractant → more cells arrive. The competition between diffusion (spreading) and chemotaxis
(aggregation) is controlled by $\chi c_0/D$, the chemotactic Péclet number.

## L2 · Aggregation, blow-up, and what limits it

| Behaviour | Condition | Meaning |
|---|---|---|
| uniform decay | weak chemotaxis, strong diffusion | no pattern |
| aggregation into a peak | above threshold | clumping (biofilms, slime moulds) |
| finite-time blow-up (2-D) | mass above $8\pi D/\chi$ | mathematical singularity: infinite density |
| pattern/band formation | signal dynamics + growth | travelling chemotactic bands |
| travelling pulses | excitable signal dynamics | bacterial waves (E. coli rings) |

In 3-D and in 2-D with sufficient diffusion, global solutions exist; in 2-D below the critical
diffusion, solutions can concentrate in finite time — a rare, concrete instance of a PDE blow-up that
is biologically meaningful, because real systems are saved by saturation, volume exclusion or
signal degradation (patched models).

## L3 · What the mathematics guarantees

* **Free energy and critical mass.** Keller–Segel systems possess a Lyapunov functional (a
  chemotactic free energy); its structure gives the critical-mass threshold for blow-up and the
  "chemotactic collapse" analysis. Saturation terms or nonlinear diffusion remove the singularity.
* **Cross-diffusion structure.** The system is a cross-diffusion problem: the flux of one species
  depends on the gradient of another, and the matrix of diffusivities is *not* positive definite —
  hence standard maximum principles fail, and entropy methods become essential.
* **Patterns and bands.** Adding growth or signal kinetics produces travelling bands and
  periodic patterns; these are the mechanism behind bacterial ring patterns and macrophage
  recruitment in wounds.
* **Biological realism limits the model.** Cells have finite speed, finite sensing length and finite
  size; run-and-tumble models, kinetic equations and stochastic simulations replace the macroscopic
  flux when gradients are steep relative to the cell's motion
  ([kinetic theory](../05-kinetic/02-bgk-vlasov-and-plasma-kinetics.md)).

## L4 · Numerics

* **Positivity and mass conservation** are essential and hard: use finite-volume discretisations
  with upwind (Patlak) fluxes, which are positivity-preserving.
* **Blow-up needs handling**: adaptive refinement, regularisation (saturation or volume filling), or
  rescaling near the singularity; plain uniform grids cannot resolve collapse.
* **Stiffness from the signal equation** (fast production/degradation) calls for implicit treatment
  ([time integration](../07-numerics/02-cfl-stiffness-and-time-integration.md)).
* **Benchmarks**: the critical-mass blow-up computation, travelling chemotactic bands, and
  single-peak aggregation profiles
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Chemotaxis in tumours and immune response; coupling with fluid flow (swimming in
  mucus); active matter and phase separation driven by activity
  ([quantum & condensed matter](../08-bridges/10-quantum-and-condensed-matter.md)).

## Checks

1. Why can aggregation occur when the chemical signal is produced by the same cells that respond to
   it? *(Positive feedback: arrival begets attractant.)*
2. What stops blow-up in reality? *(Saturation of the chemotactic response, volume exclusion, signal
   degradation — mathematically, extra terms that restore coercivity.)*
3. Why do standard maximum principles fail? *(The diffusivity matrix is not positive definite:
   cross-diffusion is anti-diffusive.)*

## See also

[Diffusion](../03-microscopic/01-diffusion.md) ·
[Reaction–diffusion & Turing](04-reaction-diffusion-and-turing.md) ·
[Biology & medicine](../08-bridges/03-biology-and-medicine.md) ·
[Nonlinear diffusion](../06-beyond/06-nonlinear-diffusion-and-porous-medium.md)
