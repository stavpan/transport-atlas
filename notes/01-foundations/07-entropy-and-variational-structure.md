---
title: Entropy & variational structure
blurb: Why transport equations do not explode — Lyapunov functionals, maximum principles, gradient-flow structure, and the two metrics that explain diffusion.
depth: 2
tags: [entropy, gradient flow, Lyapunov, maximum principle, Wasserstein]
---

# Entropy & variational structure

> **One-line picture.** Every well-posed transport equation carries a quantity that can only
> go downhill. Find it and you know the long-time behaviour, the stability — and often the
> right numerical scheme.
>
> **Prerequisites.** [constitutive relations](03-constitutive-relations.md) · **Leads to.**
> [optimal transport & gradient flows](../06-beyond/10-optimal-transport-and-gradient-flows.md)

## L1 · A ball in a bowl

A ball never climbs up the bowl by itself. Transport equations behave the same way: they
carry a hilltop function — an energy, an entropy, a free energy — that decreases as time runs
forward, and the state ends up parked at its minimum. This explains why a rod relaxes to a
uniform temperature, why mixtures mix or unmix, and why schemes that violate the trend blow up.
It also explains the arrow of time: the film of a diffusion experiment cannot be run backwards
because $\int c\ln c$ refuses to increase.

## L2 · The standard functionals

| Equation | Monotone functional | Identity |
|---|---|---|
| $\partial_tc=D\nabla^2c$ | energy $\tfrac12\int c^2$ | $\tfrac12\frac{\mathrm{d}}{\mathrm{d}t}\int c^2=-D\int\|\nabla c\|^2$ |
| $\partial_tc=D\nabla^2c$ | entropy $\int c\ln c$ | $\frac{\mathrm{d}}{\mathrm{d}t}\int c\ln c=-\int D\|\nabla c\|^2/c$ |
| reaction–diffusion | $\int V(c)$, logistic potential | $V'=-R(c)$ |
| Cahn–Hilliard | free energy $\int(\tfrac{\kappa}{2}\|\nabla c\|^2+f(c))$ | decreasing in $H^{-1}$ |
| Fokker–Planck | relative entropy $\int p\ln(p/p_{\rm eq})$ | H-theorem |
| porous medium | $\frac{1}{m-1}\int c^m$ | decays in $W_2$ |

**Maximum principle.** Without sources, $\min c\le c(\mathbf{x},t)\le\max c$ for all time, and a
steady elliptic solution attains its extremes on the boundary. Practical use: if your
simulation ever produces concentrations outside the range of the data and boundary values, it
is wrong — no convergence study needed.

## L3 · Gradient flows: the deep structure, and the metric *is* the physics

$$\partial_tc=-\mathcal{M}\frac{\delta F}{\delta c},\qquad\text{but which metric?}$$

| Equation | $F$ | Metric | Consequence |
|---|---|---|---|
| heat / Fokker–Planck | entropy | Wasserstein $W_2$ | diffusion is downhill transport of entropy |
| Allen–Cahn | free energy | $L^2$ | curvature-driven interface motion |
| Cahn–Hilliard | free energy + gradient penalty | $H^{-1}$ | conserved, coarsening patterns |
| porous medium | internal energy | $W_2$ | finite-speed fronts, Barenblatt profiles |

For $W_2$ the theory (Jordan–Kinderlehrer–Otto, 1998) proves **displacement convexity** of the
entropy along geodesics, which yields contraction estimates, uniqueness and convergence of the
JKO minimisation scheme. It is the strongest available tool for nonlinear diffusion and the
bridge to geometry, optimal transport and — unexpectedly — generative machine learning.

> **Trap.** Not everything is dissipative. Oscillatory (Brusselator), excitable and Hamiltonian
> systems have *no* Lyapunov functional; their attractors are limit cycles, and long-time error
> appears as phase drift. Never impose a gradient-flow scheme on a system that lacks one.

## L4 · Numerics and frontiers

* **Entropy stability.** Designing a scheme so a *discrete* entropy inequality holds buys
  nonlinear stability for free — the principle behind entropy-conservative fluxes and
  summation-by-parts methods ([structure-preserving](../07-numerics/13-structure-preserving-discretizations.md)).
* **Discrete maximum principles and positivity** follow from monotone stencils and consistent
  conservative fluxes; violating them gives negative concentrations and reactive blow-up.
* **Implicit steps are minimisations.** Backward Euler on a gradient flow *is* a JKO step;
  convex splitting exploits this for unconditional stability and monotone energy decay.
* **Where it is hard.** Non-convex free energies give exponentially long metastable plateaux in
  coarsening and phase separation: you need rare-event and coarse-graining methods, not finer
  grids. Long-time *statistics* are the frontier, not short-time accuracy.
* **Frontiers.** Variational structure for coupled multiphysics; learned energy functionals
  that preserve known dissipation; entropy-stable kinetic discretisations.

## Words that collide

> **Entropy** means thermodynamic entropy to a physicist, information entropy to a
> probabilist, and any monotone Lyapunov functional to an analyst — the last is the most
> general. **Free energy** may be Helmholtz or Gibbs depending on what is held fixed.

## Checks

1. Why does the maximum principle fail when you add a source? *(Production can push values
   beyond the boundary data; use a comparison principle against the source instead.)*
2. Which metric makes heat flow the steepest descent of entropy? *(Wasserstein $W_2$.)*
3. Name a transport system with no Lyapunov functional. *(Belousov–Zhabotinsky reaction;
   Hamiltonian dynamics.)*

## See also

[Optimal transport & gradient flows](../06-beyond/10-optimal-transport-and-gradient-flows.md) ·
[Structure-preserving discretisations](../07-numerics/13-structure-preserving-discretizations.md) ·
[Reaction–diffusion & Turing](../04-interaction/04-reaction-diffusion-and-turing.md) ·
[Nonlinear diffusion](../06-beyond/06-nonlinear-diffusion-and-porous-medium.md)
