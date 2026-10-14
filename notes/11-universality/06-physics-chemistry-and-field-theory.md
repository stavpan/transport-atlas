---
title: Physics, chemistry & field theory
blurb: Where transport is literal — hyperbolic field equations, quantum probability currents, phase-space hierarchies, chemical master equations and the renormalisation group as coarse-graining.
depth: 4
tags: [physics, quantum, field-theory, quantum-mechanics, renormalisation, chemistry]
---

# Physics, chemistry & field theory

> **One-line picture.** In physics the transport view is not an analogy: fields *are* transported, quantum
> probability *does* obey a continuity equation, statistical mechanics *is* transport in phase space, and
> the renormalisation group is coarse-graining in the sense of Mori–Zwanzig — flow in the space of
> parameters.
>
> **Prerequisites.** [Variational principles & Noether](../06-beyond/15-variational-principles-and-noether.md),
> [The Boltzmann equation](../05-kinetic/01-boltzmann-equation.md) ·
> **Leads to.** [Mathematics itself](08-mathematics-itself.md),
> [Plasma & astrophysics](../08-bridges/05-plasma-and-astrophysics.md)

## L1 · Four branches, one structure

* **Classical fields.** Elasticity, electromagnetism, gas dynamics and MHD are first- or second-order
  *systems*, symmetric-hyperbolic once you set them up properly; their well-posedness theory is the
  theory of constrained hyperbolic transport.
* **Quantum mechanics.** The Schrödinger equation gives an *exact* continuity equation for probability —
  $\partial_t|\psi|^2+\nabla\!\cdot\!\mathbf j=0$ — so quantum evolution is transport of a conserved density by a
  unitary generator. Decoherence and dissipation are then kinetics in phase space.
* **Statistical mechanics.** Liouville's theorem is incompressible transport; the BBGKY hierarchy is the closure
  problem; the Boltzmann equation is kinetic transport; hydrodynamics is its Chapman–Enskog limit.
* **Quantum field theory.** Fields propagate by Green functions ("propagators"), scattering is an inverse problem,
  and the renormalisation group is coarse-graining: **transport in coupling space**, with fixed points that define
  universality classes.

## L2 · The structures, itemised

| System | Transport structure | Key statement |
|---|---|---|
| wave, elastic, Maxwell | symmetric hyperbolic (Friedrichs) | finite speed; constraints propagate (Bianchi/divergence) |
| Euler, MHD | hyperbolic conservation laws | shocks, entropy conditions, Rankine–Hugoniot |
| Einstein's equations | constrained hyperbolic (ADM/BSSN) | **well-posedness proved this way** — why numerical relativity works |
| Schrödinger | unitary generator; continuity equation | probability conserved exactly; current $\mathbf j=(\hbar/m)\mathrm{Im}(\psi^*\nabla\psi)$ |
| Gross–Pitaevskii (BEC) | nonlinear Schrödinger | solitons, vortices, quantum turbulence |
| Wigner equation | kinetic transport in phase space | quantum analogue of Boltzmann; contains coherence + classical drift |
| open quantum system | Lindblad master equation; CPTP maps | positivity and trace preserved — a "maximum principle" for operators |
| Dirac, Klein–Gordon | first/second-order hyperbolic | propagators = Green functions; spin transport |
| Liouville, BBGKY | incompressible phase-space transport + hierarchy | closure problem (the same as turbulence) |
| Boltzmann, Fokker–Planck | kinetic transport | H-theorem; hydrodynamic limits |
| chemical master equation | master equation on the *composition lattice* | stochastic chemistry as transport of probability over molecule numbers |
| mass-action kinetics | reaction–diffusion | patterns, oscillations, bistability |
| QFT propagators | Green functions of field operators | scattering amplitudes from a wave equation |
| renormalisation group | coarse-graining flow in coupling space | fixed points ⟹ universality classes, critical exponents |
| lattice field theory | structure-preserving discretisation | continuum limit is a *measured* limit, like any PDE code |
| quantum walks | discrete transport on a graph | quantum speedups for mixing/transport problems |

## L3 · What this buys, and what it costs

* **Numerical relativity exists because of classification.** The ADM formulation is only weakly hyperbolic;
  strongly hyperbolic reformulations (BSSN and relatives) with constraint damping made long-time black-hole
  evolutions possible. This is the clearest example in physics where *choosing the right hyperbolic form* was
  the difference between a well-posed and an unusable problem — and where gauge choice (a foliation) changes the
  operator's type and stability.
* **Constraints are Noether identities, and they propagate.** Bianchi identities guarantee that if
  $\nabla_\mu T^{\mu\nu}=0$ and the constraints hold on one slice, they hold on later slices. Codes exploit this
  with projection or damping rather than re-solving them
  ([variational principles & Noether](../06-beyond/15-variational-principles-and-noether.md)).
* **Quantum conservation is exact.** Unitarity gives $\partial_t|\psi|^2+\nabla\!\cdot\!\mathbf j=0$; open systems
  replace it with completely positive trace-preserving maps, which are the operator-level analogue of a maximum
  principle: positivity and total probability are preserved by construction. Decoherence appears as *diffusion in
  phase space*, and the classical limit $\hbar\to0$ is a singular limit with boundary layers and caustics
  ([Hamilton–Jacobi](../06-beyond/02-hamilton-jacobi-and-viscosity-solutions.md)).
* **The renormalisation group is coarse-graining, and couplings transport.** The beta function is a velocity
  field in the space of parameters; fixed points are stationary points; relevant directions are unstable
  eigendirections. Hence: effective transport coefficients *run with scale* — the same phenomenon as
  homogenisation's effective tensors ([homogenisation](../06-beyond/08-homogenization-and-upscaling.md)) and the
  same reason mean-field theory works above the upper critical dimension
  ([why everything flows](01-why-everything-flows.md)). Honest caveat: the RG is a framework; rigorous versions
  exist for specific lattice models and low-dimensional constructive field theory, while many applications are
  perturbative approximations with uncontrolled errors.
* **Chemical discreteness is a transport statement.** The chemical master equation is transport of probability on
  a *lattice of compositions* with jumps of $\pm1$ molecule; the system-size expansion turns it into a
  Fokker–Planck equation with $1/V$ noise (the chemical Langevin equation). So "concentrations obey
  reaction–diffusion" is a *limit*, with a computable correction — the chemistry version of the Knudsen number.

## L4 · Practice

* **Numerical relativity**: hyperbolic formulations with constraint damping, gauge drivers, apparent-horizon
  finders; verify with convergence tests and known spacetimes (Schwarzschild perturbations, binary black-hole
  waveform catalogues). Treat constraints as *conservation audits*, not as equations to re-solve every step.
* **Lattice field theory**: the continuum limit is measured by scaling the lattice spacing exactly as in a fluid
  code; discretisation artifacts (doubling, chiral symmetry breaking) require structure-preserving fermion
  discretisations. The **sign problem** at finite density remains the central obstacle — honest candidates
  include reweighting, complex Langevin, tensor networks and quantum simulation, none of them a general solution.
* **Quantum simulation of transport**: analogue and gate-based devices can implement Lindblad dynamics, quantum
  walks and spin transport; the interesting question is where they beat classical transport solvers, and that is
  an open, actively studied question rather than a guarantee.
* **Stochastic chemistry**: Gillespie's algorithm is an exact kinetic Monte Carlo for the master equation;
  $\tau$-leaping is a controlled approximation to the corresponding Fokker–Planck equation; stiff deterministic
  kinetics stay implicit ([time integration](../07-numerics/02-cfl-stiffness-and-time-integration.md)).
* **Benchmarks**: H-theorem monitoring in kinetic codes; Maxwell and elastic wave convergence; constraint
  convergence in GR; Gillespie versus exact master-equation solutions; RG predictions versus Monte Carlo critical
  exponents; lattice-spacing scaling studies.

## Checks

1. Why did numerical relativity require reformulating Einstein's equations? *(ADM is only weakly hyperbolic;
   strongly hyperbolic forms with constraint damping are well-posed and stable — classification decided
   feasibility.)*
2. What is the quantum-mechanical continuity equation, and what does it conserve? *($\partial_t|\psi|^2+\nabla\!\cdot\!\mathbf j=0$:
   total probability, exactly — the $U(1)$ Noether current.)*
3. What is the renormalisation group in transport language? *(Coarse-graining flow — a velocity field (beta
   function) in parameter space; fixed points are universality classes and couplings "run" with scale.)*
4. In what sense is a chemical reaction network a transport problem? *(Its master equation transports probability
   over the composition lattice by $\pm1$ jumps; the large-volume limit is a Fokker–Planck/Langevin
   approximation with $1/V$ noise.)*

## See also

[Variational principles & Noether](../06-beyond/15-variational-principles-and-noether.md) ·
[The Boltzmann equation](../05-kinetic/01-boltzmann-equation.md) ·
[Mathematics itself](08-mathematics-itself.md) ·
[Plasma & astrophysics](../08-bridges/05-plasma-and-astrophysics.md) ·
[Limits of the claim](09-limits-of-the-claim.md)

