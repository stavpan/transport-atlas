---
title: Non-Newtonian rheology
blurb: When the constitutive law becomes a model of history — shear thinning, yield stress, viscoelasticity and elastic turbulence.
depth: 3
tags: [rheology, yield stress, viscoelastic, Weissenberg, Bingham]
---

# Non-Newtonian rheology

> **One-line picture.** Water's viscosity is a number; paint's viscosity is a *story* about how it
> has been stirred. The constitutive law becomes a model of history and the mathematics of
> transport changes with it.
>
> **Prerequisites.** [constitutive relations](../01-foundations/03-constitutive-relations.md) ·
> **Leads to.** [memory & viscoelastic transport](../06-beyond/04-memory-viscoelastic-and-hereditary.md),
> [variational inequalities](../06-beyond/12-variational-inequalities-and-hysteresis.md)

## L1 · What changes, and why it matters

* **Shear thinning** (ketchup, blood, polymer solutions): apparent viscosity falls with shear rate.
  Its opposite, **shear thickening** (cornflour suspensions), stiffens under impact.
* **Yield stress** (toothpaste, concrete, mud): below a threshold the material does not flow at
  all. Plug flow appears in pipes, and unsheared regions can be stranded mid-channel.
* **Viscoelasticity** (polymer melts, mucus, dough): stress depends on deformation *history* with a
  memory time $\lambda$. Materials recover shape, climb rotating rods, swell at dies and recoil.

Non-Newtonian transport is therefore not a footnote: it is where
[memory](../01-foundations/09-linear-response-and-memory.md) enters fluid mechanics.

## L2 · Models

| Model | Form | Captures |
|---|---|---|
| power law | $\mu_{\rm app}=m\dot\gamma^{\,n-1}$ | shear thinning ($n<1$) / thickening ($n>1$) |
| Carreau–Yasuda | smooth transition with plateaux | realistic viscosity curves |
| Bingham / Herschel–Bulkley | flow only if $\tau>\tau_y$ | yield stress, plug flow |
| Maxwell (upper convected) | $\lambda\overset{\triangledown}{\boldsymbol\tau}+\boldsymbol\tau=2\mu\mathbf{D}$ | stress relaxation, normal stresses |
| Oldroyd-B | Maxwell + solvent viscosity | Boger fluids, elastic instabilities |
| Giesekus / PTT | nonlinear stress terms | shear thinning, finite extensibility |
| fractional Maxwell | $\lambda^{\alpha}D_t^{\alpha}\boldsymbol\tau+\boldsymbol\tau=\cdots$ | broad relaxation spectra |

Two numbers do the work: $\mathrm{Wi}=\lambda\dot\gamma$ (memory time vs deformation time) and
$\mathrm{De}=\lambda/t_{\rm obs}$. Above $\mathrm{Wi}\sim1$ elasticity dominates, with asymmetric
velocity profiles, secondary flows in straight channels, and purely elastic turbulence at
$\mathrm{Re}\ll1$.

## L3 · What the mathematics guarantees

* **The type changes.** Viscoelastic models are *hyperbolic* in the stress (stress propagates at
  finite speed) and parabolic in velocity; the mixed type, plus loss of positive definiteness in
  some regimes, is why high-Weissenberg simulations fail. The high-$\mathrm{Wi}$ problem remains
  open.
* **Objective derivatives are mandatory.** Stress must be advected frame-invariantly (Jaumann,
  upper/lower convected): the corotational terms come from
  [objectivity](../01-foundations/02-material-derivative.md) and are physics, not algebra.
* **Yield stress is a variational inequality.** The yielded/unyielded interface is unknown and must
  be found as part of the solution; hysteresis means answers depend on history
  ([variational inequalities & hysteresis](../06-beyond/12-variational-inequalities-and-hysteresis.md)).
* **Non-monotone laws destroy well-posedness.** A $\tau(\dot\gamma)$ curve with a decreasing branch
  makes the steady problem ill-posed (shear banding) unless regularised by gradient terms or
  stress diffusion.

## L4 · Numerics

* **Mixed formulations** need LBB-stable elements or stabilisation; naive pairs lock or oscillate.
* **Separate physical from numerical instability** in the high-$\mathrm{Wi}$ regime: mesh
  refinement studies plus DEVSS/SUPG-type schemes are the usual defences.
* **Yield-stress solvers** use augmented Lagrangian or regularised bi-viscosity models; the
  regularisation parameter controls the resolvable sharpness of the plug boundary.
* **Benchmarks**: 4:1 contraction, viscoelastic flow past a sphere (drag reduction, negative wake),
  lid-driven cavity at matched $\mathrm{Wi}$ ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Thixotropic and ageing materials; elastic turbulence as a mixing mechanism;
  nonlocal rheology in dense suspensions.

## Checks

1. What distinguishes shear thinning from viscoelasticity? *(The first depends only on the current
   shear rate; the second on history.)*
2. Why is rod-climbing impossible in a Newtonian fluid? *(It requires normal-stress differences,
   hence elasticity.)*
3. Why do yield-stress problems need free-boundary methods? *(The plug boundary is an output.)*

## See also

[Memory & viscoelastic transport](../06-beyond/04-memory-viscoelastic-and-hereditary.md) ·
[Variational inequalities & hysteresis](../06-beyond/12-variational-inequalities-and-hysteresis.md) ·
[Constitutive relations](../01-foundations/03-constitutive-relations.md)
