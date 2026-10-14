---
title: Reaction–diffusion & Turing patterns
blurb: How diffusion — the great smoother — can create pattern, and what that says about morphogenesis, ecology and every spotted animal.
depth: 3
tags: [Turing, pattern formation, morphogenesis, dispersion relation, activator-inhibitor]
---

# Reaction–diffusion & Turing patterns

> **One-line picture.** Diffusion normally erases structure. Add a fast inhibitor to a slow
> activator and diffusion *creates* it — with a wavelength set by the chemistry, not the domain.
>
> **Prerequisites.** [reaction kinetics](01-reaction-kinetics-and-sinks.md),
> [spectral view](../01-foundations/06-spectral-and-green-function-view.md) · **Leads to.**
> [chemotaxis](06-chemotaxis-and-keller-segel.md),
> [free boundaries & phase field](../06-beyond/09-free-boundaries-level-sets-and-phase-field.md)

![**Figure 17.** Left: the dispersion relation of a Turing instability. Only a band of wavenumbers has positive growth rate, so the pattern has an intrinsic wavelength. Right: a Gray–Scott simulation, in which spots organise themselves with no template and no boundary data.](../../figures/turing-patterns.svg)

## L1 · The counter-intuitive idea

In 1952 Turing asked how a uniform ball of cells develops spots, stripes and branches without a
blueprint. His answer: a chemical system that is *stable without diffusion* can be destabilised by
diffusion if one species diffuses much faster than the other.

The intuition is **local activation with long-range inhibition**: a spot of activator grows, produces
an inhibitor, the inhibitor spreads far and fast, and suppresses neighbouring spots, leaving a
periodic pattern whose spacing is set by the ratio of diffusion coefficients.

## L2 · The mathematics of the instability

Linearise about the uniform state, $\mathbf{u}=\mathbf{u}_0+\delta\mathbf{u}e^{\sigma t+i\mathbf{k}\cdot\mathbf{x}}$;
the growth rate solves

$$\det\!\big[\sigma\mathbf{I}+\mathbf{J}+\mathbf{D}k^2\big]=0,$$

with $\mathbf{J}$ the reaction Jacobian and $\mathbf{D}=\mathrm{diag}(D_u,D_v)$. Turing's conditions:
$\mathrm{tr}\,\mathbf{J}<0$ and $\det\mathbf{J}>0$ (locally stable) yet $\mathrm{Re}\,\sigma>0$ for some
$k>0$ — impossible unless the diffusivities differ substantially. The result is a *band* of unstable
wavenumbers, hence a preferred wavelength.

| Pattern class | Mechanism | Example |
|---|---|---|
| Turing (stationary) | activator–inhibitor, unequal $D$ | spots/stripes on fish, digits |
| Turing–Hopf | oscillatory instability at $k\neq0$ | chemotactic banding, travelling patterns |
| spinodal / Cahn–Hilliard | free-energy descent, no reaction | phase separation, polymer blends |
| Gray–Scott families | activator with depletion | self-replicating spots, coral growth |
| Swift–Hohenberg | model near convection onset | Rayleigh–Bénard rolls |

## L3 · What the mathematics guarantees

* **Wavelength selection, not uniqueness.** The most unstable $k$ sets the scale, but the domain size
  then determines how many spots fit, producing multistability (hexagons, stripes, mixed states).
* **Weakly nonlinear reduction.** Near onset, amplitude equations (Swift–Hohenberg type) describe
  pattern selection and stability using a handful of ODEs — this is how hexagon-versus-stripe
  competition is decided analytically.
* **Patterns may never settle.** Coarsening, spot splitting and defect motion can continue
  indefinitely; the asymptotic state is sometimes a sponge, not a crystal.
* **Mobility contrast is required.** Biologically this is achieved by making the inhibitor a small,
  fast-diffusing molecule and the activator membrane-bound — or by replacing diffusion with active
  transport ([chemotaxis](06-chemotaxis-and-keller-segel.md)).

## L4 · Numerics

* **Resolution.** The grid must resolve the intrinsic wavelength by roughly ten points, and the
  unstable band must lie inside the resolved wavenumber range; a coarse grid can *hide* a genuine
  instability.
* **Boundary conditions.** Neumann boundaries pin nodes at the edges; use periodic boundaries or
  large domains to see intrinsic patterns.
* **Stiffness.** Reaction rates often exceed diffusion rates by orders of magnitude: implicit or IMEX
  splitting is standard ([splitting & coupling](../07-numerics/05-operator-splitting-and-multiphysics-coupling.md)).
* **Benchmarks**: Gray–Scott pattern families, Brusselator wavelength predictions, Turing–Hopf
  travelling bands ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Turing patterns in tissue (pigment, digits, hair); stochastic patterns at low copy
  numbers; patterns on growing domains; learned networks reproducing observed morphology.

## Checks

1. Why does diffusion destabilise here when it stabilises single-species systems? *(The inhibitor
   diffuses far faster, so inhibition is non-local while activation stays local.)*
2. Which species is fast? *(The inhibitor.)*
3. Why is the wavelength independent of the domain? *(It is set by the instability band in $k$.)*

## See also

[Reaction kinetics](01-reaction-kinetics-and-sinks.md) ·
[Autocatalysis & oscillations](03-autocatalysis-and-oscillations.md) ·
[Chemotaxis & Keller–Segel](06-chemotaxis-and-keller-segel.md) ·
[Entropy & variational structure](../01-foundations/07-entropy-and-variational-structure.md)
