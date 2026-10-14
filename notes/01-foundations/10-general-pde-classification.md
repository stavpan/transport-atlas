---
title: General PDE classification
blurb: Order, dimension, systems and nonlinearity — how to classify any evolution equation, not just second-order ones in two variables.
depth: 3
tags: [classification, principal symbol, characteristics, systems, well-posedness]
---

# General classification: any order, any dimension

> **One-line picture.** Forget the discriminant formula for two variables: the general classification is
> *spectral*. Take the highest-derivative part of the operator, replace derivatives by a wavevector, and
> ask what that polynomial does.
>
> **Prerequisites.** [PDE taxonomy & boundary conditions](04-pde-taxonomy-and-boundary-conditions.md) ·
> **Leads to.** [Higher order & dispersive](11-higher-order-and-dispersive.md),
> [Dimensions & geometry](12-dimensions-geometry-and-manifolds.md),
> [Integrable systems](../06-beyond/14-integrable-systems-and-solitons.md)

## L1 · Why the two-variable rule is not enough

The familiar rule — elliptic if $B^2-AC<0$, parabolic if $=0$, hyperbolic if $>0$ — applies to
**second-order, linear, two-variable, constant-coefficient** equations. Real problems are routinely none
of those: elasticity and Maxwell are second-order *systems* in three dimensions; Navier–Stokes is
nonlinear; the plate equation is fourth order; Korteweg–de Vries is third order; Cahn–Hilliard is fourth
order; Einstein's field equations are a *constrained* system; the Schrödinger equation is first order in
time with complex coefficients. Classification must survive all of that.

The recipe has three steps and uses only the **highest-order (principal) part** — lower-order terms never
change the type, only the behaviour.

## L2 · The general recipe

Write a linear operator of order $m$ as $L=\sum_{|\alpha|\le m}a_\alpha(\mathbf{x})\partial^\alpha$ and
define the **principal symbol**

$$\sigma_L(\mathbf{x},\mathbf{k})=\sum_{|\alpha|=m}a_\alpha(\mathbf{x})(i\mathbf{k})^\alpha ,$$

a homogeneous polynomial of degree $m$ in the wavevector. Everything follows from this one object:

| Property of $\sigma_L$ | Type | Consequence |
|---|---|---|
| $\sigma_L\neq0$ for all real $\mathbf{k}\neq0$ | **elliptic** | interior smoothness; boundary-value problems; infinite signal speed |
| real distinct roots in $\tau$ for all $\mathbf{k}$ | **strictly hyperbolic** | real characteristics; well-posed Cauchy problem; finite speed; shocks |
| real roots, possibly repeated | **weakly hyperbolic** | well-posedness needs the lower-order terms to cooperate |
| complex roots all with $\mathrm{Im}\le0$ | **parabolic** (Petrovsky sense) | instantaneous smoothing in some directions |
| roots crossing into the lower half-plane | **ill-posed** (Hadamard) | tiny data blow up — a sign error, usually |
| $\sigma_L$ real in some cone, complex outside | **mixed / variable type** | transonic flow, Tricomi equation, degenerate edges |

**Characteristics** are the surfaces $\varphi=0$ with $\sigma_L(\mathbf{x},\nabla\varphi)=0$: data may be
prescribed on non-characteristic surfaces, and singularities propagate along characteristics. In $d$
dimensions a characteristic set is a *hypersurface*, and its geometry — not merely its existence —
controls the solution.

**Order matters in ways the classical labels hide:**

| Order | Prototype | What is genuinely new |
|---|---|---|
| 1 | advection, Liouville, Schrödinger (complex) | characteristics are trajectories; systems already interesting |
| 2 | diffusion, wave, elasticity | the classical table |
| 3 | KdV, Airy, Boussinesq | **dispersive**: wave speed depends on $k$ |
| 4 | biharmonic, Cahn–Hilliard, Kuramoto–Sivashinsky | two boundary conditions per edge; stiff; unstable bands |
| 5–6 | KdV hierarchy, thin-film and phase-field-crystal models | delicate well-posedness; isolated unstable wavenumber bands |
| non-integer | fractional diffusion | nonlocal: no local characteristics at all |
| integro-differential | Boltzmann, radiative transfer | classified by symbol *and* kernel |

**Systems.** For $u_t+\sum_jA_j(\mathbf{x})u_{x_j}=B$, look at
$\det(\tau I+\sum_jA_jk_j)=0$:

* **Symmetric hyperbolic** (Friedrichs): all $A_j$ symmetric ⇒ energy estimates, well-posed Cauchy
  problem, finite propagation speed. Most of physics fits: Maxwell, elasticity, Euler, MHD, and
  Einstein's equations in a suitable gauge.
* **Strictly hyperbolic** (Leray–Ohya): real distinct eigenvalues ⇒ well-posed with variable
  coefficients, no derivative loss.
* **Petrovsky parabolic**: diffusion–reaction systems, Navier–Stokes in the right variables.
* **Constrained symmetric hyperbolic**: $\nabla\!\cdot\!\mathbf B=0$, the Einstein constraints,
  incompressibility. Constraints propagate if they hold initially — hence projection, constrained
  transport and constraint-damping in codes.
* **Nonlinear** equations are classified by *linearising about a solution*; the type may change where
  coefficients degenerate, and that is exactly where the interesting mathematics lives (shock
  formation, sonic lines, turning points).

## L3 · What each type buys you (the well-posedness hierarchy)

* **Elliptic** — interior regularity as good as the data; maximum principles; Fredholm alternative;
  unique solvability with boundary data; no real characteristics carrying information.
* **Hyperbolic** — finite propagation speed; energy conservation; local well-posedness in Sobolev
  spaces; smooth solutions may break in finite time (shocks), after which only weak, entropy-selected
  solutions exist ([shocks](../06-beyond/01-conservation-laws-and-shocks.md)).
* **Parabolic** — instantaneous smoothing, interior analyticity for $t>0$, maximum principles,
  semigroup well-posedness; the *backward* problem is ill-posed.
* **Dispersive** (odd-order skew-adjoint part: KdV, Schrödinger) — no smoothing and no shocks:
  oscillations spread to infinity. Strichartz estimates, infinitely many conservation laws, often
  complete integrability ([solitons](../06-beyond/14-integrable-systems-and-solitons.md)).
* **Weakly hyperbolic and degenerate** — the hardest and most physical case: transonic flow, shallow
  water at the shoreline, relativistic fluids at critical speed. Well-posedness becomes a research
  question, and numerics need extra dissipation and entropy fixes.
* **Cauchy–Kowalevski** — analytic data on a non-characteristic surface give a unique analytic
  solution *whatever the type*. Classification is thus about **information flow and stability**, not
  about mere existence.

## L4 · Numerics: the type dictates the algorithm

| Type | Discretisation |
|---|---|
| elliptic | sparse solve; multigrid; exploit symmetry |
| parabolic | implicit or fractional-step time integration; positivity by construction |
| strictly hyperbolic | conservative flux form, characteristic upwinding, limiters |
| weakly hyperbolic / mixed | added numerical dissipation, entropy fixes, careful boundaries |
| constrained systems | projection, constrained transport, staggered/compatible grids |
| higher order | compact/WENO stencils, $C^1$ or mixed elements, split off the stiff part |
| dispersive | high-order or spectral; low-order dissipation destroys the physics |
| nonlocal / fractional | FFT/Toeplitz hierarchical methods; Monte Carlo |

Two habits that save projects: **(1) classify before you discretise** — a mixed-type problem solved
with a parabolic scheme yields nothing but artefacts; **(2) test the symbol** — insert a plane wave into
the *discrete* operator and compare with $\sigma_L$; the difference is your error, and its sign tells you
whether you accidentally added diffusion or dispersion
([spectral view](06-spectral-and-green-function-view.md)).

## Checks

1. What type is KdV, $u_t+u_{xxx}=0$, by the elliptic/parabolic/hyperbolic trichotomy — and what is the
   honest answer? *(Its symbol is purely imaginary: it is none of them; it is dispersive, and the
   classical trichotomy simply does not cover it.)*
2. Why does the discriminant test fail for Navier–Stokes? *(Nonlinear, a system, in three dimensions —
   and classification is a local, linear notion anyway.)*
3. Give an equation whose type changes inside the domain. *(The Tricomi equation $y\,u_{xx}+u_{yy}=0$;
   transonic flow past a wing.)*
4. What does "symmetric hyperbolic" buy you that "strictly hyperbolic" does not? *(Energy estimates for
   *nonlinear* problems and variable coefficients — the reason Friedrichs systems are the workhorse of
   mathematical relativity, MHD and elasticity.)*

## See also

[PDE taxonomy & boundary conditions](04-pde-taxonomy-and-boundary-conditions.md) ·
[Higher order & dispersive](11-higher-order-and-dispersive.md) ·
[Dimensions & geometry](12-dimensions-geometry-and-manifolds.md) ·
[Variational principles & Noether](../06-beyond/15-variational-principles-and-noether.md) ·
[Operator & equation catalogue](../10-appendix/03-operator-and-equation-catalog.md)

