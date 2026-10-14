---
title: Anomalous diffusion
blurb: When the mean squared displacement is not linear — subdiffusion, superdiffusion, CTRW, Lévy flights, and why cells and disordered media never obey Fick.
depth: 3
tags: [anomalous, CTRW, Levy, subdiffusion, ergodicity, fractional]
---

# Anomalous diffusion

> **One-line picture.** Fick's law assumes a walker with finite step variance and finite mean
> waiting time. Break either assumption and diffusion stops being Fickian — but it remains
> *transport*, with laws of its own.
>
> **Prerequisites.** [diffusion](01-diffusion.md),
> [random walks](../01-foundations/08-random-walks-langevin-response.md) · **Leads to.**
> [nonlocal & fractional operators](../06-beyond/03-nonlocal-and-fractional-operators.md),
> [stochastic PDEs & random media](../06-beyond/07-stochastic-pdes-and-random-media.md)

![**Figure 16.** Mean squared displacement for the four transport classes. All are called diffusion; only $\alpha=1$ is Fickian, and the exponent identifies the mechanism.](../../figures/diffusion-suite.svg)

## L1 · The generalisation, and where it comes from

Define $\langle x^2\rangle\sim t^{\alpha}$. Normal diffusion is $\alpha=1$; **subdiffusion** $\alpha<1$
comes from trapping, crowding and viscoelastic drag; **superdiffusion** $\alpha>1$ comes from long
jumps, active motion and turbulence; $\alpha=2$ is ballistic.

| Mechanism | Exponent | Setting |
|---|---|---|
| waiting times $\psi(\tau)\sim\tau^{-1-\gamma}$ | $\alpha=\gamma$ | traps, sticking, glassy dynamics |
| Lévy flights, jumps $\sim|x|^{-1-\beta}$ | $t^{1/\beta}$ scaling, infinite variance | plasma transport, animal search |
| viscoelastic drag / memory kernel | $\alpha<1$, fractional | polymer solutions, cytoskeleton |
| correlated velocities (persistent walk) | $\alpha\approx2$, crossing to 1 | active matter, swimmers |
| broad velocity distribution in a heterogeneous medium | $\alpha\approx1$ with heavy tails | fractured rock, groundwater |
| continuous-time random walk (CTRW) | framework for all of the above | the standard model |

Keeping waiting times random makes the walk subdiffusive; keeping jump lengths heavy-tailed makes
it superdiffusive. In the continuum limit both become **fractional** equations
([fractional operators](../06-beyond/03-nonlocal-and-fractional-operators.md)):

$$\partial_t^{\alpha}c=D_{\alpha}\,\partial_{|x|}^{\beta}c .$$

## L2 · How to tell them apart in data

* **Log–log MSD slope** is the first diagnostic — and the one most often misreported because the fit
  window decides the answer.
* **Distribution shape:** subdiffusion keeps a Gaussian core with long tails; Lévy flights have
  heavy tails in the displacement distribution itself.
* **Ergodicity breaking:** for subdiffusive CTRW, time averages and ensemble averages disagree, so
  single-particle tracking and bulk measurements return different "diffusion coefficients". A real
  effect, not an error bar.
* **Ageing:** transport depends on how long the system has been running, violating the assumptions
  of standard inverse methods.

## L3 · What the mathematics guarantees

* **The Laplacian is special.** The fractional Laplacian $(-\Delta)^{\beta/2}$ generates a Lévy
  process: nonlocal, scale-invariant, and requiring *global* boundary conditions — locality of
  physics is lost.
* **Relaxation stops being exponential.** Time-fractional equations decay as Mittag-Leffler /
  power laws and never fully forget initial data, which is why memory effects persist in glasses and
  cells for experimental ages.
* **Variance may not exist.** For superdiffusive Lévy transport $\langle x^2\rangle=\infty$: second
  moments are the wrong descriptor, so use scaling functions or fractional moments instead.
* **Anomaly can be transient or asymptotic.** Finite traps eventually exhaust (crossover to
  normal); fractal trap distributions sustain anomaly forever. The crossover time is often the
  number that matters in practice.

## L4 · Numerics

* **Fractional solvers**: convolution quadrature, FFT for periodic problems, Toeplitz and
  sum-of-exponentials schemes for long history
  ([fractional operators](../06-beyond/03-nonlocal-and-fractional-operators.md)).
* **Monte Carlo is easiest**: simulate CTRW or Lévy walkers directly instead of assembling dense
  nonlocal matrices ([particle methods](../07-numerics/09-particle-and-monte-carlo-methods.md)).
* **Do not fit Fickian models to anomalous data**: the fit returns a length- and time-dependent $D$,
  which is a symptom of model error, not a coefficient.
* **Benchmarks**: CTRW exponent recovery, subdiffusive Barenblatt-type profiles, Lévy tail
  distributions ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Anomalous transport in cells and tissues; non-ergodic groundwater transport;
  anomalous heat conduction at the nanoscale.

## Checks

1. Which two random-walk assumptions does Fick's law require? *(Finite jump variance and finite mean
   waiting time.)*
2. Why do time-averaged and ensemble measurements disagree in subdiffusive CTRW? *(Ergodicity is
   broken.)*
3. Which operator replaces $\nabla^2$ for Lévy flights? *(The fractional Laplacian
   $(-\Delta)^{\beta/2}$, $\beta<2$.)*

## See also

[Diffusion](01-diffusion.md) ·
[Nonlocal & fractional operators](../06-beyond/03-nonlocal-and-fractional-operators.md) ·
[Stochastic PDEs & random media](../06-beyond/07-stochastic-pdes-and-random-media.md) ·
[Shear dispersion](../02-bulk/06-shear-dispersion-taylor-aris.md)
