---
title: Porous media & Darcy's law
blurb: Flow and transport through rock, soil and tissue — Darcy, permeability, dispersion, and how microscale geometry becomes an effective law.
depth: 2
tags: [Darcy, permeability, Forchheimer, Brinkman, dispersion]
---

# Porous media & Darcy's law

> **One-line picture.** You cannot solve Navier–Stokes in every pore, so you average: the net
> effect of ten million tortuous passages is a linear law with one material constant.
>
> **Prerequisites.** [constitutive relations](../01-foundations/03-constitutive-relations.md) ·
> **Leads to.** [subsidence](../04-interaction/13-subsidence-and-poroelasticity.md),
> [wells & breakthrough](../04-interaction/12-wells-injection-efflux-and-breakthrough.md),
> [homogenisation](../06-beyond/08-homogenization-and-upscaling.md)

## L1 · Why a single constant works

Push water through sand slowly and the flow rate is proportional to the pressure gradient. That is
all Darcy's law says. It is astonishing that it works, because the pore-scale flow is a mess of
separating and reattaching streams. The reason is averaging: at low Reynolds number the viscous
resistance of a statistically homogeneous medium is linear in the driving force, so an effective
coefficient exists.

The law has a validity range, and knowing its edges is the whole art:

| Regime | Law | Condition |
|---|---|---|
| creeping, low $\mathrm{Re}$ | $\mathbf{q}=-(K/\mu)(\nabla p-\rho\mathbf{g})$ | $\mathrm{Re}_{\rm pore}\lesssim1$ |
| inertial corrections | Forchheimer: add $-\beta\rho|\mathbf{q}|\mathbf{q}$ | $\mathrm{Re}_{\rm pore}\gtrsim1{-}10$ |
| near a free surface or fracture | Brinkman: add $\mu_{\rm eff}\nabla^2\mathbf{q}$ | boundary-layer-like transitions |
| very tight pores | Klinkenberg slippage | gas mean free path $\sim$ pore size |
| consolidation/compaction | poroelastic (Biot) | when the matrix deforms |

## L2 · From pores to a tensor

With porosity $\theta$ (void fraction) and Darcy (seepage) velocity $\mathbf{q}$, the actual pore
velocity is $\mathbf{v}=\mathbf{q}/\theta$, and mass balance gives the **advection–dispersion
equation**

$$\partial_t(\theta c)+\nabla\cdot(\mathbf{q}c-\theta\mathbf{D}\cdot\nabla c)=R(c),\qquad
K=\frac{\theta d^2}{180(1-\theta)^2}\ (\text{Kozeny–Carman}, d=\text{grain size}).$$

* **Permeability is a tensor** in layered or fractured rock; flow anisotropy of $10^3$ is common,
  which is why horizontal wells exist.
* **Dispersion is a tensor too**, aligned with the flow, with
  $\alpha_L\gg\alpha_T$ ([shear dispersion](06-shear-dispersion-taylor-aris.md)).
* **Capillarity matters** at infiltration fronts and in the vadose zone: $K$ and $p$ become
  functions of saturation (Richards' equation), turning the problem *nonlinear* and often
  hysteretic ([variational inequalities](../06-beyond/12-variational-inequalities-and-hysteresis.md)).

## L3 · What the mathematics guarantees

* **Upscaling is exact in the limit.** Volume averaging or two-scale asymptotics produce Darcy's
  law with $K$ computed from a *cell problem* on the pore geometry — a genuine theorem, not a
  fudge ([homogenisation](../06-beyond/08-homogenization-and-upscaling.md)).
* **Elliptic steady problems, parabolic transients.** The steady flow (and pressure) solves an
  elliptic problem; pressure transients obey a diffusion equation with hydraulic diffusivity
  $T/S$ — identical mathematics to heat conduction, which is why well-test analysis was built from
  heat-conduction solutions.
* **Reciprocity and symmetry.** $K$ is symmetric positive definite; a consequence is that
  streamlines and potential gradients are orthogonal only in isotropic media, and that well
  patterns have reciprocal responses.
* **Dispersion coefficients are asymptotic.** Valid only for lengths much larger than a
  heterogeneity correlation length; practical aquifers often violate this, producing non-Fickian
  plumes ([anomalous transport](../03-microscopic/08-anomalous-diffusion.md)).

## L4 · Numerics

* **Grid orientation artifacts** appear with anisotropic dispersion tensors; keep the tensor
  symmetric and check rotation invariance with a diagonal-flow test.
* **Reservoir simulators live here**: IMPES (implicit pressure, explicit saturation) versus fully
  implicit, upwinding for saturations, and [limiters](../07-numerics/04-limiters-tvd-and-weno.md)
  to control front smearing. Mass conservation is non-negotiable and is why finite-volume
  discretisations dominate.
* **Heterogeneity modelling** (geostatistical realisations, upscaling of correlated random fields)
  is the main computational cost — a study may require hundreds of realisations for uncertainty
  quantification ([UQ and inversion](../07-numerics/10-inverse-problems-and-data-assimilation.md)).
* **Benchmarks**: the Henry problem (density-driven flow), the McWhorter–Sunada problem, and
  analytical well-test solutions (Theis, Cooper–Jacob)
  ([measurement](../10-appendix/05-measurement-and-experiments.md)).

## Checks

1. Why is Darcy's law linear while the pore-scale flow is not? *(Averaging at low
   $\mathrm{Re}_{\rm pore}$: inertia is negligible, so resistance is linear.)*
2. What happens when $\mathrm{Re}_{\rm pore}$ grows? *(Forchheimer's quadratic correction — the
   flow is no longer proportional to the gradient.)*
3. Why is permeability not a property of the solid alone? *(It depends on pore geometry; and in
   the slip regime on the gas mean free path as well.)*

## See also

[Shear dispersion](06-shear-dispersion-taylor-aris.md) ·
[Homogenisation & upscaling](../06-beyond/08-homogenization-and-upscaling.md) ·
[Subsidence & poroelasticity](../04-interaction/13-subsidence-and-poroelasticity.md) ·
[Geoscience & climate](../08-bridges/04-geoscience-and-climate.md)
