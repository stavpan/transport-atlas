---
title: Fronts & travelling waves
blurb: Invasion, combustion and nerve impulses as one object — speed selection, pulled fronts, and why the leading edge controls everything.
depth: 3
tags: [Fisher-KPP, travelling wave, front speed, reaction-diffusion, excitable]
---

# Fronts & travelling waves

> **One-line picture.** A reaction that turns "off" into "on" produces a self-sustaining front whose
> speed is dictated by the *leading edge*, where the chemical is barely present.
>
> **Prerequisites.** [reaction kinetics](01-reaction-kinetics-and-sinks.md),
> [autocatalysis](03-autocatalysis-and-oscillations.md) · **Leads to.**
  [phase change & Stefan](09-phase-change-and-stefan.md),
> [biology & medicine](../08-bridges/03-biology-and-medicine.md)

![**Figure 18.** A Fisher–KPP front at four times: the profile translates without changing shape, and the speed is set by the edge of the wave where the nonlinearity is still linear. Right: the Stefan free boundary, where latent heat slows the interface to $\sqrt{t}$.](../../figures/fronts-and-stefan.svg)

## L1 · Three applications, one object

A flame front, an epidemic wave, a spreading population, a nerve impulse, an invading tumour, a
curing resin — all are fronts where a state invades a rest state. They share three questions:
*Does a front exist? How fast does it move? Is it the only one?*

## L2 · The mathematics

For the Fisher–KPP equation, $\partial_tc=D\partial_x^2c+kc(1-c)$, look for travelling waves
$c(x,t)=f(x-ct)$. Substituting reduces the PDE to an ODE whose phase-plane analysis gives:

* fronts exist **only** for $c\ge c_{\min}=2\sqrt{Dk}$;
* the realised speed is exactly the minimum, $c=2\sqrt{Dk}$, selected by the leading edge where
  $c\ll1$ and the equation is linear;
* the profile decays exponentially ahead of the front, $c\sim e^{-cx/D}$.

| Front type | Selection rule | Speed | Examples |
|---|---|---|---|
| **pulled** (KPP) | the leading edge sets it | $c_{\min}=2\sqrt{Dk}$ | epidemics, invasive species |
| **pushed** | the bulk sets it | larger than $c_{\min}$ | some bistable systems |
| bistable | Maxwell/equal-area rule | unique, parameter-independent | phase boundaries, nerve pulses |
| excitable pulses | dispersion relation | a function of refractory time | cardiac, neural, chemical waves |

The distinction between pulled and pushed fronts is not academic: for pulled fronts the front speed
is sensitive to the *tail* of the initial condition and to any change in the reaction at low
concentrations, while for pushed fronts it is robust.

## L3 · What the mathematics guarantees

* **Speed selection is a theorem**, not a fit. The KPP result (Kolmogorov–Petrovskii–Piskunov 1937;
  Fisher 1937) is one of the cleanest in nonlinear PDEs.
* **Approach to the asymptotic speed is slow.** Bramson's correction: the front position converges
  to $2\sqrt{Dk}\,t$ only up to a logarithmic term, $\sim-\frac{3}{2c}\ln t$ — a famous trap when
  fitting front positions from experiments or simulations.
* **Sharp fronts require nonlinearity of a different kind.** Degenerate diffusion (e.g., the
  porous-medium equation) produces *compact-support* fronts with well-defined interfaces and finite
  propagation speed ([porous medium](../06-beyond/06-nonlinear-diffusion-and-porous-medium.md)),
  which demands free-boundary or [level-set](../06-beyond/09-free-boundaries-level-sets-and-phase-field.md)
  methods rather than fine grids over a tail.
* **Stability.** KPP fronts are stable to perturbations; non-minimal speeds are unstable. Bistable
  fronts can be unstable to curvature (leading to interface instability: Mullins–Sekerka,
  Saffman–Taylor).
* **Curvature and quenching.** In 2-D and 3-D, curved fronts move faster (or slower for concave
  fronts); the eikonal relation $v_n=c-\kappa D_{\rm eff}$ links front dynamics to
  [Hamilton–Jacobi equations](../06-beyond/02-hamilton-jacobi-and-viscosity-solutions.md), and
  heat losses (quenching) can extinguish thin flames.

## L4 · Numerics

* **Resolving a tail that spans many orders of magnitude** is expensive. Adaptive meshes or
  transformation of variables (log-form) are often required to capture both the tail and the bulk.
* **Front position must be defined carefully** (a threshold, or a first moment), and reported with
  the Bramson correction in mind for pulled fronts.
* **Level-set and front-tracking methods** are superior when the front is genuinely a moving
  interface with its own internal structure; phase-field methods are robust for topology changes
  ([free boundaries](../06-beyond/09-free-boundaries-level-sets-and-phase-field.md)).
* **Benchmarks**: KPP speed convergence (including the log correction), bistable front speed, and
  spiral-wave frequency in excitable media
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Fronts in heterogeneous and random media (speed depends on the environment);
  reactive fronts in porous media and fractures; conservation laws with source terms and the
  transition to detonations.

## Checks

1. Why is the KPP speed the *minimum* possible speed? *(Faster speeds are also solutions, but only
   the minimum is stable/selected.)*
2. What is the Bramson correction and why does it matter? *(A $-\frac{3}{2c}\ln t$ term in front
   position: naive fits to $ct$ give biased speeds.)*
3. When is front tracking better than a fine grid? *(When the interface has internal structure
   spanning scales far below the domain, or when topology changes must be handled.)*

## See also

[Autocatalysis & oscillations](03-autocatalysis-and-oscillations.md) ·
[Phase change & Stefan](09-phase-change-and-stefan.md) ·
[Hamilton–Jacobi & viscosity solutions](../06-beyond/02-hamilton-jacobi-and-viscosity-solutions.md) ·
[Biology & medicine](../08-bridges/03-biology-and-medicine.md)
