---
title: Duality and transforms
blurb: The same problem in two costumes — Fourier, Laplace, Legendre, Cole–Hopf, special dualities — and a practical dictionary for choosing the right change of clothes.
depth: 4
tags: [mechanisms, duality, transform, Fourier, Cole-Hopf, Kramers-Wannier, dictionary]
---

# Duality and transforms

> **One-line picture.** Duality is a *dictionary*: a change of variables, a transform, or an exact map
> between two theories, under which a hard problem becomes an easy one. When you meet a new equation, the
> first professional move is not to discretise it — it is to ask **which bookkeeping makes it simple**.
>
> **Prerequisites.** [Spectral & Green-function view](../01-foundations/06-spectral-and-green-function-view.md),
> [Scaling & self-similarity](07-scaling-and-self-similarity.md) ·
> **Leads to.** [the intersections map](10-intersections-map.md),
> [information, statistics & inference](../11-universality/07-information-statistics-and-inference.md)

## L1 · The everyday version

Two descriptions of one thing. Celsius or Fahrenheit: the physics is identical, the arithmetic is not.
A wobbly signal or its list of frequencies: which is "simpler" depends on the question. A queue of cars or
the density of cars: the same traffic, one easy to count, the other easy to differentiate.

Some dualities are mere conveniences. Others are *deep*: two theories that look completely different can
turn out to be the same theory, with strong coupling in one becoming weak coupling in the other — which is
how problems get solved that nobody could solve directly.

## L2 · The everyday duality: a change of variables

| Transform / substitution | Turns this into | Classic use |
|---|---|---|
| Fourier / Laplace | derivatives into multiplication; convolution into product | constant-coefficient linear PDEs, [spectral view](../01-foundations/06-spectral-and-green-function-view.md) |
| Similarity variable $\xi=x/t^{\alpha}$ | PDE into ODE | diffusion kernel, Blasius, Taylor–Sedov |
| Legendre | conjugate pairs; convex functions into dual variables | thermodynamics, [optimal transport](../06-beyond/10-optimal-transport-and-gradient-flows.md) |
| Cole–Hopf $u=-2\nu\,\partial_x\ln\phi$ | viscous Burgers into the heat equation | a genuinely nonlinear equation, linearised exactly |
| Kirchhoff / Madelung | nonlinear diffusion, or a wave, into a hydrodynamic form | porous-medium, quantum hydrodynamics |
| Change of measure (Girsanov, exponential tilting) | a drift into a weight | Feynman–Kac, rare events, [large deviations](../11-universality/07-information-statistics-and-inference.md) |

The pattern to notice: **nonlinearity is often an artefact of the variables.** Burgers' equation is
nonlinear — until you exponentiate. A path-dependent option price is complicated — until you change
probability measure. Choosing variables is a *theorem-producing* activity, not cosmetic tidying.

## L3 · Exact dualities between theories

* **Kramers–Wannier (1941).** The 2-D Ising model at low temperature maps onto *itself* at high
  temperature with $T\leftrightarrow T_c^2/T$: the coupling strength and its dual exchange roles. Because
  the model is self-dual at exactly $T_c$, this pins the critical temperature without solving anything —
  and the same duality later explained why the model can be solved by free fermions.
* **Waves and particles.** Wave–particle duality, the Fourier pairing of position and momentum, and the
  path integral: three costumes of one mathematical structure (a symplectic Fourier transform). Modern
  versions are the workhorses of quantum transport.
* **Holography (AdS/CFT).** A gravitational theory in the bulk is dual to a quantum field theory on its
  boundary: strong coupling on one side is weak and calculable on the other. It is the most ambitious
  duality currently in physics; it is also a genuine computational tool for strongly coupled transport
  (viscosity-to-entropy ratios, quark–gluon plasma).
* **Particle–vortex duality** in 2-D, and the dualities of statistical mechanics generally: an exact
  bijection between configurations, with the dual variables being topological defects (vortices, domain
  walls) of the original.
* **The general moral.** When a problem has a conserved quantity, a symmetry, or a graphical structure,
  there is usually a dual description in which the conserved thing becomes a defect, the symmetry becomes a
  constraint, and the difficulty moves somewhere you can handle.

## L4 · Using transforms without being used by them

* **Boundary conditions travel badly.** Fourier is natural for infinite domains and periodic boundaries;
  on a finite interval with mixed boundary conditions it produces series whose convergence *is* the
  problem. Verify that the transform respects the physics you imposed at the edges.
* **Transforms fail exactly where you need them most.** Cole–Hopf solves viscous Burgers for
  *special* initial data and cannot handle a general flux function; Fourier needs constant coefficients;
  the $J$-integral analogy only holds for a linear material. Know the hypothesis list by heart.
* **Numerically, the transform is a discretisation choice.** Spectral methods *are* the Fourier duality
  implemented on a grid; pseudospectral methods pay for their accuracy with aliasing (see
  [mode coupling](04-nonlinearity-and-mode-coupling.md)). Simulating in the dual variables can be the
  difference between spectral accuracy and no accuracy at all — or between a stable and an unstable scheme.
* **Dual descriptions must agree on observables.** If two descriptions are exact duals, they must predict
  the same measurable quantities. Use this as a test: transport coefficients, correlation functions and
  conservation laws computed in both worlds should match to numerical error. When they do not, you have
  found either a bug or a broken duality — and both are interesting.