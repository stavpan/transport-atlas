---
title: Microcontinuum & generalized continua
blurb: When a material point needs internal structure — micropolar, couple-stress, strain-gradient and nonlocal mechanics.
depth: 4
tags: [micropolar, couple stress, strain gradient, Eringen, size effects]
---

# Microcontinuum & generalized continua

> **One-line picture.** Classical continua assume a point has no size. When the microstructure is
> comparable to the gradients, give the point internal degrees of freedom — or accept that your model
> has no length scale and cannot reproduce size effects.
>
> **Prerequisites.** [nonlocal & fractional operators](03-nonlocal-and-fractional-operators.md) ·
> **Leads to.** [variational inequalities & hysteresis](12-variational-inequalities-and-hysteresis.md),
> [structure-preserving discretisations](../07-numerics/13-structure-preserving-discretizations.md)

## L1 · Why classical continua run out of information

A classical elastic solid has **no intrinsic length scale**: a 1 mm beam and a 1 m beam of the same
material behave identically up to scaling. Experiments disagree at small scales — thin wires are
relatively stiffer in torsion, waves become dispersive near the micro-wavelength, shear bands have a
finite width. Classical averaging erased the scale information. Three ways to put it back:

* **Internal degrees of freedom** — each point carries an independent rotation (micropolar/Cosserat) or
  micro-deformation, giving couple stresses and a length $\ell$.
* **Gradient enrichment** — the energy depends on strain *gradients*, introducing higher-order terms
  (strain-gradient elasticity, gradient plasticity).
* **Nonlocal averaging** — stress depends on the neighbourhood's strain (Eringen, peridynamics): the
  solid-mechanics version of [nonlocal diffusion](03-nonlocal-and-fractional-operators.md).

## L2 · Observable signatures

| Effect | Classical | Generalized continuum |
|---|---|---|
| torsion of thin wires | size-independent | stiffer as the diameter shrinks |
| bending stiffness | fixed $EI$ | raised by the length $\ell$ |
| wave propagation | non-dispersive | dispersive near micro-wavelengths |
| shear band width | zero (ill-posed) | finite, set by $\ell$ |
| crack-tip stress | singular | regularised and finite |
| strain localisation | mesh-dependent | mesh-objective |

The last two rows are the practical payoff: a length scale converts an ill-posed localisation problem
into a well-posed one, which is why gradient and nonlocal models dominate damage, plasticity and
fracture modelling.

## L3 · What the mathematics guarantees

* **Higher order $\Rightarrow$ more boundary conditions.** Gradient and couple-stress models are fourth
  order, needing e.g. prescribed micro-rotation or normal strain gradient. Their boundary layers are
  *physical*.
* **The length scale is what restores ellipticity.** Without it the acoustic tensor loses positivity,
  localisation solutions become non-unique, and results depend on the mesh.
* **Variational origin.** Gradient models are derived from an energy functional, so they inherit
  hyperelastic consistency and can be discretised in a structure-preserving way.
* **Nonlocal elasticity is not "smoother elasticity"**: reciprocity and Saint-Venant principles change,
  and the nonlocal length must be calibrated from dispersion or size-effect data.

## L4 · Numerics

* **$C^1$ elements** (Hermite, Argyris) or **mixed formulations** with the gradient as an independent
  variable; the mixed route is usually more robust.
* **Mesh-objectivity tests** are the verification standard: refine and confirm that localisation width
  converges to the physical $\ell$ rather than to zero.
* **Coupling with transport** appears in microstructured poroelasticity, thermal gradients in
  composites, and damage–diffusion coupling in electrodes
  ([poroelasticity](../04-interaction/13-subsidence-and-poroelasticity.md)).
* **Benchmarks**: torsion/bending size effects, dispersion curves for microstructured beams, localisation
  width convergence ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Engineering-scale peridynamic fatigue; gradient models calibrated by molecular dynamics;
  learned micromorphic constitutive laws.

## Checks

1. Why can a classical continuum not predict size effects? *(It is scale-invariant — no length scale.)*
2. What does a length parameter do to localisation? *(Restores ellipticity: unique, mesh-objective
   solutions.)*
3. Why extra boundary conditions? *(Fourth-order operators need two conditions per boundary.)*

## See also

[Nonlocal & fractional operators](03-nonlocal-and-fractional-operators.md) ·
[Subsidence & poroelasticity](../04-interaction/13-subsidence-and-poroelasticity.md) ·
[Structure-preserving discretisations](../07-numerics/13-structure-preserving-discretizations.md) ·
[Engineering devices](../08-bridges/06-engineering-devices.md)
