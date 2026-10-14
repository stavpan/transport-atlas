---
title: Measurement & experiments
blurb: How every transport coefficient is actually measured — tracer tests, PFG-NMR, thermoreflectance, PIV, and the inversion that always follows.
depth: 3
tags: [measurement, tracer, NMR, PIV, thermoreflectance, experiment]
---

# Measurement & experiments

> **One-line picture.** Nature never reports a coefficient; it reports a signal. Every measurement is an
> inverse problem in disguise.
>
> **Prerequisites.** [inverse problems & data assimilation](../07-numerics/10-inverse-problems-and-data-assimilation.md)

## L1 · The catalogue

| Quantity | Method | What is measured | Notes |
|---|---|---|---|
| diffusion coefficient $D$ (liquid) | Taylor dispersion in a capillary, diaphragm cell | axial spreading | extremely precise; needs a well-characterised profile |
| $D$ (polymer, colloid) | dynamic light scattering, PFG-NMR, single-particle tracking | fluctuation correlation / displacement | DLS gives $D$ and size; SPT reveals anomalies |
| $D$ in porous media | column tracer tests, push–pull tests | breakthrough curves | inversion for $D$, $v$, retardation, kinetics |
| thermal conductivity $k$ | steady-state guard method, laser flash (LFA), 3$\omega$, thermoreflectance | temperature response | thin films need thermoreflectance; interface conductance separately |
| viscosity $\mu$ | capillary, rotational, falling ball | stress–strain-rate relation | non-Newtonian fluids need a full flow curve |
| permeability $K$ | core flooding, well tests (Theis analysis) | flow rate / drawdown | scale-dependent: core vs field values differ |
| reaction rate constants | batch reactors, plug-flow reactors, TGA/DSC | concentration vs time | Arrhenius fits require several temperatures |
| dispersion/dispersivity | column and field tracer tests | plume moments / breakthrough shape | often scale-dependent: report the length |
| velocity fields | PIV/PTV, LDV, ultrasonic | instantaneous velocity | PIV resolves structures; LDV gives point accuracy |
| concentration fields | PLIF, absorption spectroscopy, Raman | planar/point concentration | PLIF needs calibration for laser sheet non-uniformity |
| phase change | DSC/TGA, neutron/X-ray imaging, thermocouples | latent heat, front position | front tracking needs imaging |
| surface phenomena | tensiometry, ellipsometry, QCM | surface tension, film thickness, adsorption | contact-angle hysteresis is common |

## L2 · The four rules of transport measurement

1. **A measurement is a convolution.** You measure the response of your apparatus, not the material:
   finite injection widths, sensor dynamics and boundary effects all smear the signal. Deconvolve, or
   design the experiment so the instrument's response is much shorter than the physics.
2. **Fit the model you actually have.** Extracting $D$ from a plume assumes Fickian behaviour; if the
   transport is anomalous, the fitted $D$ drifts with scale. Report the fitting window and test for scale
   dependence.
3. **Report uncertainty and sensitivity together.** Transport coefficients often enter exponentially
   (Arrhenius, Kramers), so a 10% coefficient error can be a factor-of-two rate error.
4. **Design to break degeneracy.** Velocity, dispersion, retardation and kinetic sorption all shift or
   spread a breakthrough curve; use multiple observation points, multiple flow rates, and non-sorbing
   tracers to separate them
   ([sorption & retardation](../04-interaction/07-sorption-and-retardation.md)).

## L3 · What the mathematics guarantees

* **Identifiability is a property of the experiment, not the data volume.** More samples do not fix a
  structurally degenerate design; the resolution matrix must be studied before the campaign
  ([inverse problems](../07-numerics/10-inverse-problems-and-data-assimilation.md)).
* **Moment analysis is robust and assumption-light**: the first two moments of a breakthrough curve give
  velocity and dispersion without fitting any functional form — the recommended first pass.
* **Frequency-domain measurements trade time for resolution**: periodic forcing (modulated
  thermoreflectance, oscillatory shear) measures the *frequency-dependent* coefficient $D(\omega)$,
  $\eta(\omega)$ directly, exposing memory that a single steady number hides
  ([linear response & memory](../01-foundations/09-linear-response-and-memory.md)).
* **Well-designed experiments measure ratios**, not absolutes: the ratio of dispersion to diffusion, of
  $\mathrm{Sh}$ to $\mathrm{Nu}$, or of two thermal conductivities cancels apparatus errors.

## L4 · Practice

* **Calibrate the apparatus with a known sample** before measuring an unknown one, and report the
  calibration uncertainty separately from the measurement spread.
* **Check the dimensionless groups of the apparatus** (Péclet of the test section, Biot number of the
  sample, $\mathrm{Kn}$ of the gas) so the experiment sits in the intended regime.
* **Cross-validate with an independent method** — thermoreflectance against laser flash, PFG-NMR against
  DLS — because systematic errors are method-specific.
* **Publish the raw signal and the fit window**, not only the coefficient: reproducibility depends on the
  former.

## Checks

1. Why is a tracer test an inverse problem? *(You measure concentration histories, not coefficients; the
   parameters come from fitting or moment analysis.)*
2. Why is a frequency-domain measurement more informative than a steady one? *(It resolves the memory
   kernel/frequency dependence, not just a single lumped value.)*

## See also

[Inverse problems & data assimilation](../07-numerics/10-inverse-problems-and-data-assimilation.md) ·
[Verification, validation & benchmarks](../07-numerics/12-verification-validation-and-benchmarks.md) ·
[Diffusion coefficients](../03-microscopic/04-diffusion-coefficients.md) ·
[History, etymology & open problems](06-history-etymology-and-open-problems.md)
