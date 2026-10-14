---
title: Higher order & dispersive transport
blurb: Third, fourth and higher-order operators — dispersive waves, pattern-forming instabilities, thin films and the sign conditions that decide whether a high-order equation is physical.
depth: 3
tags: [higher-order, dispersive, KdV, Cahn-Hilliard, Kuramoto-Sivashinsky, biharmonic]
---

# Higher order & dispersive transport

> **One-line picture.** Add more derivatives and you get richer behaviour: *odd* orders make waves
> without damping; *even* orders smooth or sharpen depending on the sign. Above second order there is no
> classical trichotomy — there are signs, parities and instability bands.
>
> **Prerequisites.** [General PDE classification](10-general-pde-classification.md) ·
> **Leads to.** [Integrable systems & solitons](../06-beyond/14-integrable-systems-and-solitons.md),
> [Free boundaries & phase field](../06-beyond/09-free-boundaries-level-sets-and-phase-field.md)

## L1 · Where high-order operators come from

Second-order equations describe flux proportional to a gradient. Higher orders arise whenever the
*flux itself* wants to be smooth, or when the physics is curvature-driven or dispersive:

| Source of higher order | Mechanism | Prototype |
|---|---|---|
| surface energy of an interface | energy penalises curvature ⟹ $\int\kappa^2$ | Cahn–Hilliard (4th), Willmore flow |
| plates and shells | bending stiffness scales as $\partial^4$ | biharmonic plate, thin-film equations |
| surface diffusion | matter moves along a surface to reduce area | Mullins–Sekerka, evaporation fronts (4th) |
| dispersive waves | linear wave speed depends on $k$ | KdV (3rd), Boussinesq, Airy |
| two competing scales | inertial range + dissipation | Kuramoto–Sivashinsky (4th) |
| crystalline order | density waves with one preferred wavelength | phase-field crystal (6th) |
| numerical hyper-diffusion | stabilising a scheme | $-\varepsilon\Delta^2$ — a *model*, not physics |

The last row is a warning: higher-order terms are the easiest way to stabilise a code and the easiest way
to change the physics.

## L2 · Classification by parity and sign

For a constant-coefficient model $u_t=a_m\partial_x^m u$ the dispersion relation is
$\omega=a_m i^{m+1}k^m$, so the parity of $m$ decides the *character* of the operator:

| $m$ | $\omega(k)$ | Character | Well-posed when |
|---|---|---|---|
| 1 | $a_1k$ | advection / waves, nondispersive | any real $a_1$ |
| 2 | $-ia_2k^2$ | **dissipative** (diffusion) | $a_2>0$ |
| 3 | $a_3k^3$ | **dispersive** (no damping, no growth) | any real $a_3$ |
| 4 | $-ia_4k^4$ | **hyper-diffusive** | $a_4>0$ |
| 5 | $a_5k^5$ | dispersive, higher-order effects | any real $a_5$ |
| 6 | $-ia_6k^6$ | hyper-diffusive | $a_6>0$ |

General rule: **odd orders are dispersive (real $\omega$), even orders are dissipative (imaginary
$\omega$), and the sign of an even-order coefficient decides physically sensible vs explosive at short
wavelengths.** This is a special case of the **Lax–Mizohata condition**: a higher-order evolution
equation is well-posed iff its symbol's eigenvalues satisfy $\mathrm{Re}\,\lambda(\mathbf{k})\le C$ for
all real $\mathbf{k}$. Combine orders and you get the physics:

$$\underbrace{u_t+uu_x}_{\text{steepening}}\underbrace{+\,u_{xxx}}_{\text{dispersion}}=0
\ \text{(KdV)},\qquad
\underbrace{u_t+uu_x+u_{xx}}_{\text{unstable band}}+u_{xxxx}=0\ \text{(Kuramoto–Sivashinsky)} .$$

* **Balancing two powers of $k$ picks a length scale.** In Cahn–Hilliard,
  $\omega(k)=-Mk^2(\kappa k^2-f'')$ is positive only for $0<k<\sqrt{f''/\kappa}$: the **spinodal band**,
  whose width sets the pattern wavelength. In Kuramoto–Sivashinsky, growth $k^2$ competes with damping
  $k^4$: a band of unstable modes, hence spatiotemporal chaos. In thin-film flow the balance involves
  $h^3$ and produces a *finite-wavelength* dewetting instability.
* **Conserved higher-order flows** (Cahn–Hilliard, surface diffusion) are gradient flows in $H^{-1}$;
  their fourth-order structure preserves mass exactly and makes them stiff.
* **Dispersive hierarchies** (KdV, mKdV, fifth-order KdV) form infinite families with soliton solutions
  ([next note](../06-beyond/14-integrable-systems-and-solitons.md)).

## L3 · What the mathematics guarantees (and where it is delicate)

* **Higher-order diffusion still smooths, but the scaling changes.** Long waves relax with
  $\tau\sim k^{-4}$ (or $k^{-6}$) instead of $k^{-2}$: better damping of small scales, slower washing-out
  of large ones. Conserved fourth-order flows are *stiff* and their smoothing is slow at large scales —
  which is why coarsening takes so long.
* **The maximum principle is lost above second order.** Positivity of biharmonic problems holds only
  under special boundary conditions (the classical Boggio result for the clamped plate) and fails for
  others: no positivity, no comparison, no automatic bounds. Discrete schemes must enforce positivity
  and mass conservation *explicitly* ([entropy & variational structure](07-entropy-and-variational-structure.md)).
* **Instability is band-limited.** Linear analysis gives a most-unstable wavenumber $k_{\max}$; the
  nonlinear theory then selects a pattern and a coarsening law (Cahn–Hilliard: $L\sim t^{1/3}$;
  Kuramoto–Sivashinsky: spatiotemporal chaos with an attractor dimension growing with the domain size).
* **Lax–Mizohata is the general well-posedness test**: the symbol's eigenvalues must not grow. The
  failures are instructive — negative diffusion ($u_t=-Du_{xx}$), backward biharmonic
  ($u_t=-\Delta^2u$), and fourth-order dispersion with the wrong sign are all ill-posed at short
  wavelengths, and a numerical scheme that "fixes" them has silently solved a different problem.
* **Dispersive equations conserve more than energy.** KdV and its relatives have infinitely many
  conservation laws and (often) complete integrability; the linearised dynamics spreads any localised
  disturbance as $t^{-1/3}$ in $L^\infty$ (Airy-type decay), which is why dispersive numerical schemes
  must have very low dissipation to see the physics.

## L4 · Numerics

* **Stiffness scales as $\Delta x^m$.** An explicit scheme for a fourth-order operator needs
  $\Delta t\lesssim\Delta x^4/(\text{const})$: spectral, implicit or exponential integrators are the
  practical options; splitting the conservative part from the stiff part keeps mass exact.
* **Boundary conditions double.** Two conditions per edge, or a **mixed formulation**:
  Cahn–Hilliard as $u_t=\nabla\!\cdot\!(M\nabla\mu)$, $\mu=f'(u)-\kappa^2\Delta u$ with two second-order
  equations. But be careful — *splitting changes the admissible boundary data*, so it changes the
  physics unless the boundaries are periodic or natural.
* **Patterning needs resolution of the most-unstable scale**, and coarsening needs long-time accuracy:
  adaptive meshes plus energy-stable (convex-splitting) schemes are the standard pair
  ([structure-preserving schemes](../07-numerics/13-structure-preserving-discretizations.md)).
* **Hyperviscosity is a choice you must declare.** Replacing $-\nu\Delta$ by $-\nu_4\Delta^2$ stabilises
  high wavenumbers but flattens spectra and moves dissipation to the wrong scales; if you use it, report
  it and check the inert range.
* **Benchmarks**: Zabusky–Kruskal soliton collision and the KdV invariants; Cahn–Hilliard coarsening
  exponent; the Kuramoto–Sivashinsky attractor statistics; thin-film dewetting front speed
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).

## Checks

1. Which parity of leading order gives dispersion, and which gives dissipation? *(Odd ⟹ dispersive
   (real $\omega$, no growth); even ⟹ dissipative with the sign deciding smoothing versus blow-up.)*
2. Why does Cahn–Hilliard have a pattern wavelength? *(Balance of $k^2$ (destabilising, from $f''$) and
   $\kappa k^4$ (stabilising) defines a band $0<k<\sqrt{f''/\kappa}$.)*
3. Why can you not replace a biharmonic boundary condition by two Neumann ones? *(It is a different
   problem: the solutions, spectra and energy functionals all change.)*

## See also

[General PDE classification](10-general-pde-classification.md) ·
[Integrable systems & solitons](../06-beyond/14-integrable-systems-and-solitons.md) ·
[Free boundaries, level sets & phase field](../06-beyond/09-free-boundaries-level-sets-and-phase-field.md) ·
[Nonlinear diffusion & porous medium](../06-beyond/06-nonlinear-diffusion-and-porous-medium.md)

