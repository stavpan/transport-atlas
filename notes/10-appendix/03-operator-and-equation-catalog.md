---
title: Operator & equation catalogue
blurb: One table for every operator form in the atlas — order, type, locality, and the notes that explain each.
depth: 2
tags: [catalogue, operators, equations, reference]
---

# Operator & equation catalogue

> Every equation in this atlas is a balance law plus one of these operators. Find your operator, get the
> type, the numerics and the physics.

| Operator / equation | Order & type | Local? | Notes, numerics | Explained in |
|---|---|---|---|---|
| advection $\mathbf u\cdot\nabla c$ | 1st, hyperbolic | yes | upwind/limiter, CFL, numerical diffusion | [Advection](../02-bulk/01-advection.md) |
| conservative transport $\nabla\cdot(\mathbf u c)$ | 1st, hyperbolic | yes | finite-volume flux form | [Balance laws](../01-foundations/01-balance-laws-and-flux.md) |
| diffusion $\nabla\cdot(D\nabla c)$ | 2nd, parabolic | yes | $\Delta t\le\Delta x^2/2D$ explicit; implicit preferred | [Diffusion](../03-microscopic/01-diffusion.md) |
| conduction $\nabla\cdot(k\nabla T)$ | 2nd, parabolic | yes | interface flux continuity | [Conduction](../03-microscopic/03-conduction.md) |
| Darcy flux $-(K/\mu)\nabla p$ | flux law | yes | conservative, high-contrast solvers | [Porous media](../02-bulk/08-porous-media-and-darcy.md) |
| incompressibility $\nabla\cdot\mathbf u=0$ | constraint + Poisson | no (elliptic) | projection, staggered grids | [Vorticity & pressure](../02-bulk/03-incompressible-flow-vorticity-and-pressure.md) |
| reaction $R(c)$ | 0th (algebraic) | yes | stiff; implicit; positivity | [Kinetics](../04-interaction/01-reaction-kinetics-and-sinks.md) |
| nonlinear conservation law $\partial_tc+\partial_xf(c)=0$ | 1st, hyperbolic | yes | shocks, entropy condition, TVD/WENO | [Shocks](../06-beyond/01-conservation-laws-and-shocks.md) |
| Hamilton–Jacobi $\partial_tu+H(\nabla u)=0$ | 1st, nonlinear | yes | monotone schemes, fast marching | [Hamilton–Jacobi](../06-beyond/02-hamilton-jacobi-and-viscosity-solutions.md) |
| nonlinear diffusion $\nabla\cdot(mc^{m-1}\nabla c)$ | 2nd, degenerate parabolic | yes | finite speed, Barenblatt, free boundary | [Nonlinear diffusion](../06-beyond/06-nonlinear-diffusion-and-porous-medium.md) |
| $p$-Laplacian $\nabla\cdot(\|\nabla c\|^{p-2}\nabla c)$ | 2nd, quasilinear | yes | TV denoising, non-Newtonian flow | [Images & signals](../08-bridges/08-images-and-signals.md) |
| Cahn–Hilliard $\nabla\cdot(M\nabla(f'-\kappa^2\nabla^2c))$ | 4th, parabolic | yes | needs $C^1$ or mixed methods | [Free boundaries](../06-beyond/09-free-boundaries-level-sets-and-phase-field.md) |
| telegraph / Cattaneo $\tau c_{tt}+c_t=Dc_{xx}$ | 2nd, hyperbolic-damped | yes | finite speed, stiff relaxation | [Memory & viscoelasticity](../06-beyond/04-memory-viscoelastic-and-hereditary.md) |
| fractional time $D_t^{\alpha}c=D\nabla^2c$ | non-integer | no (memory) | convolution quadrature, sum-of-exponentials | [Nonlocal & fractional](../06-beyond/03-nonlocal-and-fractional-operators.md) |
| fractional space $(-\Delta)^{\beta/2}c$ | non-integer | **no** | dense/Toeplitz/FFT; needs volume BCs | same note |
| nonlocal diffusion $\int K(x,y)[c(y)-c(x)]\mathrm dy$ | integral | **no** | asymptotically compatible schemes | same note |
| memory $\int M(t-s)\mathbf X(s)\mathrm ds$ | Volterra | no (time) | Prony/sum-of-exponentials | [Linear response](../01-foundations/09-linear-response-and-memory.md) |
| Fokker–Planck | 2nd, parabolic | yes | conservative form, positivity | [Fokker–Planck](../05-kinetic/03-fokker-planck-and-kramers.md) |
| Boltzmann | kinetic, $2d$-dim phase space | collision nonlocal in $\mathbf v$ | DSMC, discrete velocity | [Boltzmann](../05-kinetic/01-boltzmann-equation.md) |
| Vlasov | kinetic, self-consistent field | field non-local | PIC, semi-Lagrangian | [BGK & Vlasov](../05-kinetic/02-bgk-vlasov-and-plasma-kinetics.md) |
| radiative transfer $\Omega\cdot\nabla I=-\kappa I+j$ | 1st in space, integral in angle | **no (angle)** | $S_N$, Monte Carlo, asymptotic-preserving | [Radiative transfer](../05-kinetic/04-radiative-transfer.md) |
| stochastic PDE | stochastic | — | strong vs weak convergence | [Stochastic PDEs](../06-beyond/07-stochastic-pdes-and-random-media.md) |
| variational inequality | constraint | yes | semismooth Newton, active sets | [Variational inequalities](../06-beyond/12-variational-inequalities-and-hysteresis.md) |
| gradient flow $\partial_t\rho=-\mathcal M\,\delta F/\delta\rho$ | depends on metric | yes | energy-stable schemes, JKO | [Optimal transport](../06-beyond/10-optimal-transport-and-gradient-flows.md) |
| MHD induction | mixed hyperbolic/parabolic | yes | constrained transport, HLLD | [MHD](../06-beyond/13-mhd-and-relativistic-transport.md) |

## Quick classification guide

* **Order** fixes the number of boundary conditions and the stencil width.
* **Type** (elliptic/parabolic/hyperbolic) fixes the boundary-data requirements and the numerical family.
* **Locality** decides sparse versus dense/hierarchical algebra.
* **Constraints** ($\nabla\cdot\mathbf u=0$, $\nabla\cdot\mathbf B=0$, inequalities) need separate
  enforcement and produce saddle-point structure.
* **Linearity** decides whether you solve once or iterate.

## Higher order, systems and non-PDE forms

The table above is the classical catalogue; these are the entries that make it general
([general classification](../01-foundations/10-general-pde-classification.md),
[higher order](../01-foundations/11-higher-order-and-dispersive.md)).

| Operator / equation | Order & type | Local? | Notes, numerics | Explained in |
|---|---|---|---|---|
| principal symbol $\sigma_L(\mathbf x,\mathbf k)$ | *any* order, any $d$ | — | classification = roots of the symbol; test your *discrete* symbol against it | [general classification](../01-foundations/10-general-pde-classification.md) |
| first-order symmetric system $u_t+\sum_jA_ju_{x_j}=Bu$ | 1st system, symmetric hyperbolic | yes | energy estimates; finite speed; goundation of GR/MHD/elasticity codes | same note |
| constrained hyperbolic system | 1st/2nd system + constraints | yes | projection/constrained transport/constraint damping | [variational principles & Noether](../06-beyond/15-variational-principles-and-noether.md) |
| dispersive $u_t+u_{xxx}=0$ (Airy/KdV) | 3rd, dispersive | yes | spectral or high-order; low-order dissipation destroys solitons | [integrating solitons](../06-beyond/14-integrable-systems-and-solitons.md) |
| hyper-diffusive $u_t=-a_4\partial_x^4u$, $a_4>0$ | 4th, parabolic | yes | stabilising; $\Delta t\sim\Delta x^4$; hyperviscosity must be reported | [higher order](../01-foundations/11-higher-order-and-dispersive.md) |
| Kuramoto–Sivashinsky | 4th, unstable band | yes | spatiotemporal chaos; attractor dimension grows with size | same note |
| thin-film / lubrication | 4th (often degenerate) | yes | free surface, finite-wavelength dewetting | [free boundaries](../06-beyond/09-free-boundaries-level-sets-and-phase-field.md) |
| phase-field crystal | 6th, pattern-forming | yes | crystalline order; narrow unstable band | [higher order](../01-foundations/11-higher-order-and-dispersive.md) |
| strain-gradient / micropolar | 4th, elliptic (mixed form) | yes | two BCs per edge; mesh-objective localisation | [microcontinuum](../06-beyond/11-microcontinuum-and-generalized-continua.md) |
| delay PDE / retarded functional equation | hyperbolic + history | yes | store & interpolate history; characteristic-aware schemes | [delay & retarded transport](../06-beyond/16-delay-and-retarded-transport.md) |
| Volterra / hereditary integral | time-nonlocal | no (time) | sum-of-exponentials, convolution quadrature | [memory & viscoelasticity](../06-beyond/04-memory-viscoelastic-and-hereditary.md) |
| master equation on a graph/lattice | discrete state space | edges | sparse exponentials, kinetic Monte Carlo, Gillespie | [why everything flows](../11-universality/01-why-everything-flows.md) |
| Hamilton–Jacobi–Bellman (control) | 1st, nonlinear, viscosity | yes | monotone schemes; value iteration = discrete HJ | [algorithms](../11-universality/05-computation-and-algorithms.md) |
| mean-field game system | HJB $+$ Fokker–Planck coupled | yes (both) | fixed-point iteration; monotonicity for uniqueness | [finance & economics](../08-bridges/02-finance-and-economics.md) |
| Ricci / mean-curvature / harmonic-map flow | 2nd, parabolic in geometry | yes (geo) | Lyapunov monotonicity as a numerical diagnostic | [mathematics itself](../11-universality/08-mathematics-itself.md) |
| minimum-cost flow, assignment, EMD | discrete optimal transport | graph | network simplex; the exact sibling of Sinkhorn | same note |
| Markov category / probabilistic program | compositional (no derivatives) | — | semantics, not numerics | [information & inference](../11-universality/07-information-statistics-and-inference.md) |

## See also

[PDE taxonomy & boundary conditions](../01-foundations/04-pde-taxonomy-and-boundary-conditions.md) ·
[Discretisation & stability](../07-numerics/01-discretization-consistency-stability-convergence.md) ·
[Symbol glossary](01-symbol-glossary.md) ·
[One mathematics of transport](../08-bridges/11-unifying-mathematics-of-transport.md)
