---
title: Variational principles & Noether
blurb: From least action to conservation laws, symplectic flow as incompressible transport, and the variational structure of dissipative systems.
depth: 4
tags: [action, Euler-Lagrange, Noether, Hamiltonian, symplectic, GENERIC, Onsager]
---

# Variational principles & Noether

> **One-line picture.** If a system minimises something, its equations are the Euler–Lagrange equations,
> its symmetries become conservation laws, and its flow is an *incompressible transport* in phase space.
>
> **Prerequisites.** [Entropy & variational structure](../01-foundations/07-entropy-and-variational-structure.md) ·
> **Leads to.** [Integrable systems](14-integrable-systems-and-solitons.md),
> [Why everything flows](../11-universality/01-why-everything-flows.md)

## L1 · Everything from a functional

Two complementary ways to write physics, both of which are transport statements:

* **Dissipative (gradient flow):** $\partial_tu=-\mathcal{M}\,\delta F/\delta u$ — downhill on a
  functional in a chosen metric ([entropy & variational structure](../01-foundations/07-entropy-and-variational-structure.md)).
* **Conservative (action principle):** the path taken makes the action $S=\int L\,\mathrm{d}t$ stationary;
  the resulting Euler–Lagrange equations are the equations of motion. In field theory the action is a
  spacetime integral and the equations are PDEs: waves, elasticity, Maxwell, Einstein, Schrödinger,
  Yang–Mills.

The same PDE can be read either way, which is why variational thinking explains *why* particular terms
appear: a conservation law is a symmetry, and a constitutive law is a variational derivative.

## L2 · Noether and the structure theorems

**Noether's theorem.** Each continuous symmetry of the action gives a conservation law:

| Symmetry | Conserved quantity | Transport content |
|---|---|---|
| time translation | energy | flux balance for energy |
| space translation | momentum | momentum flux tensor |
| rotation | angular momentum | vorticity/circulation theorems |
| boost (Galilean, Lorentz) | centre-of-mass velocity, energy–momentum | relativistic transport constraints |
| phase (gauge, $U(1)$) | charge, probability | charge conservation = continuity equation |
| scaling | virial theorem | exponents of similarity solutions |
| internal (non-abelian gauge) | colour/weak isospin currents | **Noether's second theorem**: identities ⇒ constraints (e.g. Bianchi ⇒ $\nabla_\mu T^{\mu\nu}=0$) |

**Hamiltonian form and incompressible transport.** Writing the field as $(q,p)$ with a Hamiltonian $H$,
the flow is $\dot q=\partial H/\partial p$, $\dot p=-\partial H/\partial q$: a **symplectic**
(shear-like) velocity field in phase space. **Liouville's theorem** says the flow preserves phase-space
volume — literally *incompressible transport*, so the phase-space density satisfies
$\partial_tf+\{f,H\}=0$, the collisionless Boltzmann equation. Transport in phase space is thus not an
analogy: it is a continuity equation with a divergence-free velocity.

**The dissipative counterpart.** Onsager's principle of least dissipation, the principle of minimum
entropy production, and the **GENERIC** structure
$\dot z=L\,\delta E/\delta z+M\,\delta S/\delta z$ (a reversible co-symmetric part $L$ plus a
symmetric, positive-semidefinite dissipative part $M$) give a single framework in which the
Hamiltonian and the gradient-flow pictures coexist. That is also where Onsager's reciprocal relations
came from ([constitutive relations](../01-foundations/03-constitutive-relations.md)).

## L3 · What the mathematics guarantees

* **Symmetry ⟹ conservation, and broken symmetry ⟹ sources.** A conservation law holds *because* nothing
  breaks the symmetry; switch to a rotating frame and Coriolis "appears"; break spatial uniformity and a
  force appears. Every source term in this atlas can be read as a broken symmetry — which is a useful
  diagnostic when a term looks arbitrary in an equation.
* **Gauge invariance *is* a continuity equation.** The $U(1)$ symmetry of quantum mechanics gives
  $\partial_t|\psi|^2+\nabla\!\cdot\!\mathbf{j}=0$ exactly: quantum probability obeys a transport law with
  a conserved current. Magnetohydrodynamics, superconductivity and the Standard Model inherit the same
  structure — charge transport is not an analogy, it is Noether's theorem.
* **Constraints are Noether's second theorem.** Gauge/nonlocal symmetries produce *identities*
  (Bianchi identities) rather than conserved charges. That is why general relativity has its Hamiltonian
  and momentum constraints, why Maxwell has $\nabla\!\cdot\!\mathbf{B}=0$, and why pressure in
  incompressible flow is a Lagrange multiplier — all the same phenomenon
  ([incompressible flow](../02-bulk/03-incompressible-flow-vorticity-and-pressure.md)).
* **Stability is convexity.** The second variation of the action/functional decides stability; loss of
  positive-definiteness is a *unified* instability mechanism (Rayleigh–Bénard is loss of energy
  convexity; Turing is loss of stability of a uniform state; shearing instabilities are loss of
  definiteness of the energy in a moving frame).
* **Classical mechanics is the geometric-optics limit of wave mechanics.** The action satisfies a
  Hamilton–Jacobi equation, rays are its characteristics ([Hamilton–Jacobi](02-hamilton-jacobi-and-viscosity-solutions.md)),
  and the Feynman weight $\exp(iS/\hbar)$ is the transport of amplitudes — the WKB/vanishing-$\hbar$ limit
  turns wave transport into ray transport, caustics and all.

## L4 · Numerics

* **Symplectic/variational integrators conserve the structure, not just the solution.** Derived from a
  *discrete* action principle, they obey a **discrete Noether theorem** (exact momentum and angular
  momentum) and show *bounded* energy error instead of secular drift — the reason molecular dynamics,
  celestial mechanics and accelerator physics use them at all
  ([structure-preserving discretisations](../07-numerics/13-structure-preserving-discretizations.md)).
* **Casimir-preserving schemes** keep the invariants of the underlying Poisson bracket (e.g. vorticity
  integrals in 2-D Euler), which is what keeps long simulations of geophysical flows physical.
* **Hamiltonian Monte Carlo** is transport in phase space used as an algorithm: simulate the
  Hamiltonian flow with a symplectic integrator and accept/reject. Its efficiency in modern
  probabilistic machine learning *depends* on the symplectic structure
  ([machine learning & data](../08-bridges/07-machine-learning-and-data.md)).
* **Dissipative counterparts** should be discretely dissipative: entropy-stable schemes mirror GENERIC
  (reversible + dissipative split) and give unconditional nonlinear stability.
* **Benchmarks**: energy drift, symplectic versus non-symplectic, over $10^6$ steps (pendulum, Kepler,
  Fermi–Pasta–Ulam–Tsingou recurrence); discrete-Noether momentum checks; Casimir conservation;
  HMC acceptance rates versus step size.

## Checks

1. Why does Liouville's theorem make collisionless kinetic theory a transport equation?
   *($\{f,H\}=\nabla\!\cdot\!(f\,\mathbf{v})$ with $\nabla\!\cdot\!\mathbf{v}=0$ in phase space:
   incompressible flow.)*
2. What does Noether's *second* theorem produce? *(Identities — constraints like Bianchi,
   $\nabla\!\cdot\!\mathbf{B}=0$, incompressibility — rather than conserved charges.)*
3. What do variational integrators conserve exactly? *(Momentum and angular momentum (discrete Noether);
   energy is conserved to bounded oscillation rather than drifting.)*

## See also

[Entropy & variational structure](../01-foundations/07-entropy-and-variational-structure.md) ·
[Integrable systems & solitons](14-integrable-systems-and-solitons.md) ·
[Hamilton–Jacobi & viscosity solutions](02-hamilton-jacobi-and-viscosity-solutions.md) ·
[Structure-preserving discretisations](../07-numerics/13-structure-preserving-discretizations.md) ·
[Mathematics itself](../11-universality/08-mathematics-itself.md)

