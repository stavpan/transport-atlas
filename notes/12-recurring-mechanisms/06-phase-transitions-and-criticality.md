---
title: Phase transitions and criticality
blurb: Where order appears and how sharply — order parameters, broken symmetry, diverging susceptibility, hysteresis, and what it takes to claim criticality honestly.
depth: 4
tags: [mechanisms, criticality, phase transition, universality, avalanches, SOC, scaling]
---

# Phase transitions and criticality

> **One-line picture.** Sometimes order appears *suddenly* and *collectively*: one number crosses a
> threshold and a whole population of degrees of freedom decides, at once, on a common state. At the
> critical point itself the system has no preferred scale — correlations stretch across the entire
> system, and everything you can measure behaves as a power of the distance from the threshold.
>
> **Prerequisites.** [Linearisation & stability](02-linearization-and-stability.md),
> [Entropy & variational structure](../01-foundations/07-entropy-and-variational-structure.md) ·
> **Leads to.** [Scaling & self-similarity](07-scaling-and-self-similarity.md),
> [Collective behaviour & synchrony](../13-panta-rhei/03-collective-behaviour-and-synchrony.md)

## L1 · The everyday version

Heat ice and, at 0 °C, the *whole block* changes character — not gradually, but on one number. Cool a
magnet past its Curie point and suddenly it remembers a direction. Pack more and more cars on a road and
at some density a jam appears, not as a bigger jam but as a *new phase* of traffic
([networks, society & traffic](../08-bridges/09-networks-society-and-traffic.md)).

The common structure: there is a **control parameter** (temperature, density, coupling), an **order
parameter** that is zero in one phase and non-zero in the other, and a **transition** that can be sharp
(second order — continuous order parameter) or abrupt (first order — a jump, with latent heat or
hysteresis). And the most interesting place is not either phase but the **critical point** between
them, where the system looks the same at every magnification.

## L2 · The three signatures to look for

![**Figure R7.** The anatomy of a continuous transition. *Left*: the order parameter vanishes at $T_c$
with a power law, $m\sim(T_c-T)^\beta$. *Centre*: the susceptibility — the response to a small nudge —
diverges, so the system becomes infinitely soft exactly at the threshold. *Right*: below $T_c$ there are
two stable states, and sweeping a field up and down traces a hysteresis loop: the system's state is a
record of its history.](../../figures/phase-transition-order-parameter.svg)

1. **Diverging correlation length.** Fluctuations are correlated over a length $\xi$ that grows without
   bound as the control parameter approaches its critical value: $\xi\sim|T-T_c|^{-\nu}$. This single
   fact is why criticality matters in transport — near $T_c$ the system *cannot* be described by local
   laws, because every point is in communication with every other.
2. **Diverging susceptibility.** A small external field produces an enormous, often nonlinear response:
   $\chi\sim|T-T_c|^{-\gamma}$. Practically: the system is hypersensitive to perturbations whose
   wavelength matches the growing correlation dome.
3. **Hysteresis and multi-stability.** In a first-order transition (or a subcritical second-order one),
   two states coexist and the path you took determines the state you see. This is memory of a very
   specific kind — not storage, but branch selection.

Order parameters in transport-flavoured settings (the same mathematics, different nouns):

| System | Control parameter | Order parameter | Sharpness |
|---|---|---|---|
| Ferromagnet | temperature | magnetisation | 2nd order (mean field), fluctuation-changed |
| [Rayleigh–Bénard cell](../02-bulk/02-convection-and-buoyancy.md) | Rayleigh number $Ra$ | magnitude of the flow | 1st order if subcritical; else 2nd |
| Percolation in a porous medium | porosity / occupancy | connected-cluster fraction, conductivity | 2nd order |
| Traffic | density | fraction of cars that are jammed | jamming, with non-eq. hysteresis |
| [Coupled oscillators](../13-panta-rhei/03-collective-behaviour-and-synchrony.md) | coupling | synchrony order parameter | 2nd order at $K_c$ |
| Opinion consensus | imitation rate | consensus fraction | 1st order (with zealots, often abrupt) |

## L3 · Landau, fluctuations, and the renormalisation group

* **Landau theory** writes the free energy as a series in the order parameter,
  $F=\frac{a}{2}m^2+\frac{b}{4}m^4-hm$ with $a\propto(T-T_c)$. Minimising gives the mean-field
  exponents $\beta=\frac12$, $\gamma=1$, $\nu=\frac12$ and the classic square-root onset. It is the
  *first* answer, correct above the upper critical dimension and qualitatively right almost everywhere —
  which is why it is the most-used sentence in the subject.
* **Fluctuations break it.** Mean field ignores that the order parameter is not uniform. The Ginzburg
  criterion compares the fluctuation energy inside a correlation volume with the energy scale of the
  transition; when fluctuations win (low dimension, short-range interactions), the exponents change —
  Ising in 2-D is the canonical case, and the exponents become irrational, not the mean-field halves.
* **Scaling relations and universality.** Exponents are not independent: $\alpha+2\beta+\gamma=2$,
  $\nu d=2-\alpha$, and so on. Universality means that the exponents depend only on dimension, symmetry
  and interaction range — a *classification theorem for whole phenomena*, arrived at through the
  renormalisation group.
* **Finite-size scaling.** In a simulation there is no true divergence: $\xi$ is capped by the box $L$,
  so observables obey $O(L,T)=L^{\,\omega/\nu}f\big(L^{1/\nu}(T-T_c)\big)$ — a *data collapse* that lets
  you extract exponents from small systems ([scaling](07-scaling-and-self-similarity.md)).

## L4 · Criticality without self-deception

**Self-organised criticality (SOC).** Bak, Tang and Wiesenfeld's 1987 sandpile proposal claimed that a
system with slow driving and fast threshold relaxation drives *itself* to a critical state, so power-law
statistics appear with no tuning. It is one of the most seductive ideas in the field — and one of the
most over-claimed:

* **What is solid.** Dissipative threshold dynamics under slow drive really does fluctuate about a
  marginally stable state with scale-free avalanche statistics; the exponents are reproducible for that
  model, and the mechanism (separation of driving and relaxation timescales) is a *real* requirement, not
  an absence of one. The class of models has been applied with genuine success to earthquakes
  (Gutenberg–Richter), forest fires, solar flares, crackling magnets and neuronal avalanches.
* **What is not.** "Power law" does not imply criticality: myriad non-critical mechanisms produce
  power-law-looking histograms — log-normals, mixtures, superpositions of exponentials. "Self-organised"
  is not automatic: the timescale separation is a hidden tuning, and moderate departures from it give
  *different* exponents. And estimates are estimator-dependent: log-binning, finite-size cutoffs and
  subsampling (crucial for neuronal data) can shift exponents enough to change the conclusion. The
  literature's own critical literature — see the [bibliography](11-bibliography.md) — makes this point
  repeatedly and it has not been superseded.
* **The honest protocol.** (i) state the timescale separation you rely on; (ii) show the histogram across
  system sizes and fit with finite-size scaling, not a single log-log line; (iii) show the collapse under
  rescaling; (iv) test at least one non-critical alternative model that reproduces the same statistic;
  (v) report the exponent as a value with an interval and the method that produced it.

![**Figure R8.** SOC in a real simulation: avalanche sizes from a slowly driven 2-D sandpile (left, with
the fitted slope — the tail is cut off by the box size, not by any physical scale) and the pile itself
(right), hovering at the critical slope where one more grain may do nothing at all or rearrange the whole
pile. The finite-size *collapse* of such distributions is the real evidence for scaling, and it is shown
in the [scaling note](07-scaling-and-self-similarity.md).](../../figures/soc-avalanche-statistics.svg)