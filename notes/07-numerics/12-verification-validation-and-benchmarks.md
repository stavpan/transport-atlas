---
title: Verification, validation & benchmarks
blurb: How to know your transport code is right — manufactured solutions, convergence studies, and the benchmarks that everybody uses.
depth: 3
tags: [verification, validation, MMS, convergence, benchmark, GCI]
---

# Verification, validation & benchmarks

> **One-line picture.** Verification asks "am I solving the equations right?"; validation asks "am I
> solving the right equations?". They are different questions with different tools, and confusing them
> wastes years.
>
> **Prerequisites.** [discretisation & stability](01-discretization-consistency-stability-convergence.md) ·
> **Leads to.** [measurement & experiments](../10-appendix/05-measurement-and-experiments.md)

## L1 · The two questions

* **Code verification**: does the implementation solve the discrete equations it claims to solve? Tools:
  unit tests of operators, **method of manufactured solutions (MMS)** — pick an analytic solution,
  substitute it into the PDE to obtain a source term, and check the *observed order of accuracy* under
  refinement.
* **Solution verification**: how large is the numerical error in this particular run? Tools: grid
  convergence index (GCI, Roache), Richardson extrapolation, and a posteriori error estimators. Report
  the uncertainty, not just the answer.
* **Validation**: do the equations (with their empirical parameters) reproduce measured reality, within
  stated uncertainties? Tools: comparison with experiments, calibration, and acceptance criteria defined
  *before* running.
* **Calibration vs validation**: fitting parameters to data and then "validating" on the same data proves
  nothing. Hold out data.

## L2 · Benchmarks you can rely on

| Physics | Benchmark | What it tests |
|---|---|---|
| advection | Gaussian advection, Zalesak disk | dissipation, dispersion, symmetry |
| shocks | Sod, Lax, double Mach reflection | conservation, entropy, limiters |
| convection | Rayleigh–Bénard onset and $\mathrm{Nu}(\mathrm{Ra})$ | coupling, buoyancy, resolution |
| porous flow | Henry, McWhorter–Sunada, SPE10 | density coupling, heterogeneity, upscaling |
| poroelasticity | Mandel, Terzaghi, Barry–Mercer | coupling stability, consolidation |
| phase change | Stefan similarity, gallium melting | free-boundary accuracy, latent heat |
| turbulence | channel at $\mathrm{Re}_\tau\approx180$, decaying isotropic | spectra, wall laws |
| kinetic | Couette/DSMC across $\mathrm{Kn}$, shock structure | kinetic limits, slip |
| radiation | Marshak wave, plane-parallel albedo | asymptotic preservation |
| reactive transport | column breakthrough with retardation | sorption, dispersion, kinetics |

The rule for using a benchmark: state the metric, the tolerance and the acceptance criterion *first*;
otherwise "looks fine" replaces verification.

## L3 · What the mathematics guarantees

* **Observed order of accuracy** in $h$ (or better, GCI) is the single most informative diagnostic: it
  detects bugs, boundary-closure errors, and order reduction from nonlinearity or limiters.
* **Conservation audits** are cheap and decisive: integrate fluxes over the boundary and compare with the
  stored mass change to machine precision (up to boundary-condition error).
* **Symmetry and invariance tests** (translation, rotation, Galilean invariance) detect subtle indexing
  and discretisation errors that convergence studies can miss.
* **Sensitivity to parameters must be reported**: a validation claim without parameter uncertainties is
  not a validation.

## L4 · Practicalities

* **Automate**: a test suite that runs quick MMS and conservation checks on every commit catches the
  majority of real bugs.
* **Keep the "digital twin" honest**: log solver tolerances, CFL numbers, iteration counts and error
  indicators with every result so that anomalies can be diagnosed later.
* **Distinguish code, solution and model error** explicitly in reports; reviewers will ask.
* **Cross-code comparison** (different codes, same benchmark) is the strongest verification available
  when no analytic solution exists.
* **Frontiers.** Automated verification and formal methods; uncertainty-aware validation criteria (model
  form error); benchmarks for learned surrogates and closures.

## Checks

1. What is the difference between verification and validation? *(Solving the equations right versus
   solving the right equations.)*
2. Why is MMS the gold standard for code verification? *(It provides an exact solution for arbitrary
   operators, so the observed order can be measured for every term.)*

## See also

[Discretisation & stability](01-discretization-consistency-stability-convergence.md) ·
[Measurement & experiments](../10-appendix/05-measurement-and-experiments.md) ·
[Benchmarks across the atlas](../10-appendix/04-key-derivations.md)
