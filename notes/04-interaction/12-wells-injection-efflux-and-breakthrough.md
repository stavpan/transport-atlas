---
title: Wells, injection, efflux & breakthrough
blurb: Sources and sinks you can point at — Theis drawdown, capture zones, plume arrival, and the inversion of tracer tests.
depth: 2
tags: [wells, injection, Theis, breakthrough, capture zone, tracer]
---

# Wells, injection, efflux & breakthrough

> **One-line picture.** A well is a point source or sink. Its mathematics is a Green function, and
> the curve it produces downstream is the most informative measurement in subsurface transport.
>
> **Prerequisites.** [porous media & Darcy](../02-bulk/08-porous-media-and-darcy.md) ·
> **Leads to.** [subsidence & poroelasticity](13-subsidence-and-poroelasticity.md),
> [inverse problems](../07-numerics/10-inverse-problems-and-data-assimilation.md)

## L1 · Point sources and point sinks

Injecting or extracting at rate $Q$ gives a source term $Q\delta(\mathbf{x}-\mathbf{x}_0)$. Because the
pressure equation is linear and elliptic, solutions superpose — the whole theory of wells is built
from one solution: the **Theis** solution for a pumping well in a confined aquifer,

$$s(r,t)=\frac{Q}{4\pi T}\,W\!\left(\frac{r^2S}{4Tt}\right),\qquad
W(u)=\int_u^\infty\frac{e^{-z}}{z}\,\mathrm{d}z .$$

The logarithm-like well function is the exponential-integral sibling of a diffusion Green function:
pressure transients obey a diffusion equation with hydraulic diffusivity $T/S$. Practical
consequences include the straight-line $s$ vs $\log t$ analysis of pumping tests and the
"radius of influence" (a fiction, but a useful one: it is where drawdown becomes immeasurable).

## L2 · The vocabulary, and what each term means physically

| Term | Meaning | Mathematics |
|---|---|---|
| **injection / influx** | forcing mass *in* | source $S(\mathbf{x},t)$ or inflow boundary |
| **extraction / effluent** | removing mass | negative source (sink) |
| **efflux / outflow** | mass leaving a boundary | boundary flux, or zero-gradient (Danckwerts) condition |
| **jetting** | directed high-velocity efflux | prescribed velocity profile at an orifice |
| **capture zone** | region that eventually reaches the well | particle-tracking streamlines; dividing surface |
| **breakthrough curve** | concentration history at a downstream probe | the fingerprint of transport processes |
| **tracer test** | inject a pulse, measure the response | inverse problem for $v$, $D$, $R$, $k$ |
| **recycled coupling** | injection and extraction interact | superposition, plus flow-field change if rates are large |

The **breakthrough curve** is the workhorse: its first moment gives the mean velocity, its second
moment the dispersion, its shift the retardation factor, its tail the kinetic sorption, its shape at
early time the short-circuiting through fractures. Fitting all of these simultaneously is
[an inverse problem](../07-numerics/10-inverse-problems-and-data-assimilation.md) — and it is usually
ill-posed, so regularisation and multiple observation points are essential.

## L3 · What the mathematics guarantees

* **Linearity and superposition** for pressure (Darcy flow) and for dilute solute transport. Drawdown
  from many wells is a sum of Theis solutions; this is why well-field design is combinatorial rather
  than computational.
* **Capture zones are exact objects.** In a steady divergence-free flow, the capture zone boundary is
  a streamline; for a uniform flow plus a well it is the well-known paraboloid (Strack's solution),
  and its width far upstream is exactly $Q/(Ub)$ — the pumping rate divided by the aquifer
  transmissivity per unit thickness.
* **Green-function reciprocity.** The response at A due to a source at B equals the response at B due
  to a source at A: a theorem with concrete consequences for monitoring network design
  ([spectral view](../01-foundations/06-spectral-and-green-function-view.md)).
* **Nonlinear complications.** Density-driven flow (saltwater intrusion), unsaturated flow,
  non-Darcy near-well effects, and multiphase flow break superposition; then you need the full
  coupled system ([variational inequalities](../06-beyond/12-variational-inequalities-and-hysteresis.md)).

## L4 · Numerics and measurement

* **Point sources need special treatment**: a delta function cannot live on a grid. Distribute the
  source over a few cells (or use a well index / Peaceman correction) so that the pressure response
  matches the analytic solution for the same grid.
* **Injection/production wells are the stiffest part** of reservoir simulators: cross-flow between
  layers, wellbore storage, and changing rates all need implicit treatment.
* **Outflow boundaries** must be non-reflecting (Danckwerts) or the plume will bounce; and an inflow
  boundary needs a specified *state*, not just a flux.
* **Benchmarks**: Theis drawdown, Strack capture-zone geometry, and 1-D column breakthrough with
  retardation ([measurement](../10-appendix/05-measurement-and-experiments.md)).
* **Frontiers.** Coupling well operations with geomechanics (subsidence, induced seismicity);
  geothermal doublets; CO₂ injection with dissolution and trapping;
  [data assimilation](../07-numerics/10-inverse-problems-and-data-assimilation.md) of field
  breakthrough curves.

## Checks

1. Why can you superpose well solutions? *(Pressure obeys a linear elliptic equation; the constraint
   and boundary conditions are linear.)*
2. What sets the far-field width of a well's capture zone? *($Q/(Ub)$: the pumping rate divided by the
   ambient flow per unit thickness.)*
3. Why is a tracer breakthrough curve so informative? *(Its moments encode velocity, dispersion,
   retardation, kinetic sorption and fracture short-circuiting simultaneously.)*

## See also

[Porous media & Darcy](../02-bulk/08-porous-media-and-darcy.md) ·
[Subsidence & poroelasticity](13-subsidence-and-poroelasticity.md) ·
[Sorption & retardation](07-sorption-and-retardation.md) ·
[Inverse problems & data assimilation](../07-numerics/10-inverse-problems-and-data-assimilation.md)
