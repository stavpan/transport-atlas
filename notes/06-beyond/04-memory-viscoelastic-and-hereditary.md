---
title: Memory, viscoelasticity & Cattaneo
blurb: When the flux lags the force — hereditary integrals, Maxwell and fractional models, and the finite speed of heat.
depth: 4
tags: [viscoelastic, memory kernel, Maxwell, Cattaneo, telegraph, second sound]
---

# Memory, viscoelasticity & Cattaneo

> **One-line picture.** Instantaneous constitutive laws are an approximation. Give the flux a
> *relaxation time* and it lags the force — which restores finite propagation speed, produces
> viscoelastic memory, and changes the type of the equation.
>
> **Prerequisites.** [linear response & memory](../01-foundations/09-linear-response-and-memory.md),
> [non-Newtonian rheology](../02-bulk/09-non-newtonian-rheology.md) · **Leads to.**
> [nonlocal operators](03-nonlocal-and-fractional-operators.md),
> [free boundaries & phase field](09-free-boundaries-level-sets-and-phase-field.md)

## L1 · The lag, and why it matters

Fourier's and Fick's laws assume the flux responds to the gradient *instantaneously*. Physically that
cannot be exactly true: it would imply infinite propagation speed. The minimal fix is a relaxation
time $\tau$ — the **Maxwell–Cattaneo** law

$$\tau\,\partial_t\mathbf J+\mathbf J=-D\nabla c .$$

Eliminating the flux between this and the balance law gives the **telegrapher's equation**

$$\tau\,\partial_t^2c+\partial_tc=D\nabla^2c,$$

which is *hyperbolic* for short times (waves at speed $c_0=\sqrt{D/\tau}$) and *parabolic* for long
times (ordinary diffusion). The same equation describes voltage on a lossy transmission line, random
walks with persistence, and phonon heat transport ("second sound" observed in solids at low
temperature).

For materials, the same idea becomes a **hereditary constitutive law**:
$\boldsymbol\tau(t)=\int_{-\infty}^{t}G(t-t')\dot{\boldsymbol\gamma}(t')\,\mathrm{d}t'$, with $G$ the
relaxation modulus. Viscoelasticity is transport with memory.

## L2 · Models and their signatures

| Model | Law | Signature |
|---|---|---|
| Maxwell | $\lambda\dot{\boldsymbol\tau}+\boldsymbol\tau=2\mu\mathbf D$ | stress relaxes exponentially; normal stresses |
| Kelvin–Voigt | $\boldsymbol\tau=2\mu\mathbf D+2G\boldsymbol\varepsilon$ | creep, no stress relaxation |
| Jeffreys / Oldroyd-B | solvent + polymer + relaxation | realistic polymer melts; die swell |
| generalised Maxwell (Prony) | sum of exponentials | any measured $G(t)$ to engineering accuracy |
| fractional Maxwell | $\lambda^{\alpha}D_t^{\alpha}\boldsymbol\tau+\boldsymbol\tau=\cdots$ | broad spectrum (power law) |
| Maxwell–Cattaneo | $\tau\partial_t\mathbf J+\mathbf J=-D\nabla c$ | finite-speed diffusion, damped waves |

Test vocabulary you will meet: **creep** (strain under constant stress), **stress relaxation**
(stress under constant strain), and **dynamic moduli** $G'(\omega)$ (storage) and $G''(\omega)$ (loss),
coupled by Kramers–Kronig because of causality.

## L3 · What the mathematics guarantees

* **Type change and its consequences.** The telegraph equation is hyperbolic with damping; the
  solution has a *sharp front* at $x=c_0t$ and smooths only behind it. As $\tau\to0$ (stiff relaxation
  limit) the solution converges to the diffusion solution — but *not uniformly* near $t=0$, which is
  exactly where the hyperbolic correction matters (ultrafast laser heating, ballistic phonons).
* **Well-posedness needs care.** Naive hyperbolic heat conduction can produce negative temperatures
  (it lacks a maximum principle); extended thermodynamics adds second-order terms to restore
  positivity — the classical example of a higher-order closure that is *worse*, not better.
* **Memory implies nonlocal equations in time.** Power-law kernels turn into fractional derivatives,
  giving Mittag-Leffler relaxation, ageing, and non-exponential creep. In the frequency domain, memory
  is just frequency-dependent moduli, and causality ties real and imaginary parts together.
* **Objectivity again.** For flowing materials, the stress must be advected with an objective
  derivative ([material derivative](../01-foundations/02-material-derivative.md)); the corotational
  terms are not decoration.

## L4 · Numerics

* **Convolution costs.** Hereditary integrals are $O(N^2)$ in time; use sum-of-exponentials
  (Prony) approximations to convert them into auxiliary ODEs — this makes memory *local in time* again
  and is the standard industrial trick.
* **Hyperbolic diffusion schemes** need upwinding and limiters (they are hyperbolic!) and stiff
  relaxation handling when $\tau$ is small; asymptotic-preserving schemes transition smoothly to the
  parabolic limit.
* **Consistency with equilibrium.** Any hyperbolic model must reproduce Fourier's law in the limit of
  slow variation; check by comparing against the classical solution on long time and length scales.
* **Benchmarks**: Cattaneo heat pulse (front speed and amplitude), stress relaxation ($G(t)$) fits,
  Prony series accuracy, and Maxwell-model oscillatory shear
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Ultrafast and nanoscale heat transport (phonon hydrodynamics, Guyer–Krumhansl);
  biological tissue poroviscoelasticity; memory kernels learned from rheological data.

## Checks

1. What does the relaxation time $\tau$ do to the equation's type? *(Makes it hyperbolic at short times;
   a wave speed $\sqrt{D/\tau}$ appears.)*
2. Why does the hyperbolic model converge to diffusion only non-uniformly? *(A boundary layer in time
   near $t=0$: the wave front.)*
3. How can a power-law memory kernel be simulated efficiently? *(Sum-of-exponentials approximation
   converts it into a few auxiliary differential equations.)*

## See also

[Linear response & memory](../01-foundations/09-linear-response-and-memory.md) ·
[Nonlocal & fractional operators](03-nonlocal-and-fractional-operators.md) ·
[Non-Newtonian rheology](../02-bulk/09-non-newtonian-rheology.md) ·
[Nonlinear diffusion & porous medium](06-nonlinear-diffusion-and-porous-medium.md)
