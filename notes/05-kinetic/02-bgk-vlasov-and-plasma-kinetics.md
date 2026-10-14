---
title: BGK, Vlasov & plasma kinetics
blurb: Collision models that are cheap, collisionless dynamics that are rich — relaxation, Landau damping, and mean-field transport in plasmas.
depth: 4
tags: [BGK, Vlasov, Landau damping, plasma, mean field]
---

# BGK, Vlasov & plasma kinetics

> **One-line picture.** Replace the collision integral by "relax toward equilibrium" and the kinetic
> equation becomes usable; drop collisions entirely and long-range forces take over — that is plasma
> physics.
>
> **Prerequisites.** [Boltzmann equation](01-boltzmann-equation.md) ·
> **Leads to.** [MHD & relativistic transport](../06-beyond/13-mhd-and-relativistic-transport.md),
> [plasma & astrophysics](../08-bridges/05-plasma-and-astrophysics.md)

## L1 · Two idealisations

* **BGK (Bhatnagar–Gross–Krook):** $\mathcal C[f]\approx-(f-f_{\rm eq})/\tau$. One parameter, exact
  conservation, correct H-theorem, and a *relaxation-time* interpretation of viscosity and diffusion
  ($\mu\approx p\tau$). Its simplicity is why it underlies lattice-Boltzmann and much of DSMC practice.
* **Vlasov:** collisions are negligible relative to the *mean field* (Coulomb forces in plasmas,
  gravity in galaxies), so $\mathcal C=0$ and the force term contains the self-consistent field
  $\mathbf F=-q\nabla\phi$, $\nabla^2\phi=-\rho_q/\varepsilon$ (Poisson). The result is a
  **collisionless** kinetic equation whose dynamics are surprisingly rich.

## L2 · What the two models predict

| Model | Key phenomenon | Why it matters |
|---|---|---|
| BGK | relaxation to local Maxwellian; slip/jump boundary layers | cheap kinetic solver for $\mathrm{Kn}\sim0.1{-}10$ |
| BGK | finite propagation of viscous/conduction response | origin of [Cattaneo-type hyperbolic heat](../06-beyond/04-memory-viscoelastic-and-hereditary.md) |
| Vlasov–Poisson | **Landau damping**: waves decay with no dissipation | energy goes to the *distribution*, not to heat — experimentally confirmed |
| Vlasov–Poisson | kinetic instabilities (two-stream, beam-plasma) | drives turbulence and heating in fusion devices |
| Vlasov–Poisson | plasma sheaths, quasineutrality breakdown | the boundary layers of plasma transport |
| Vlasov + gravity | Jeans instability, collisionless relaxation (violent relaxation) | structure formation in astrophysics |

The essential message of plasma kinetics is that **dissipation does not require collisions**.
Landau damping is phase mixing: particles with velocities near the wave phase speed exchange energy
with the wave, and the information is transferred to ever-finer structure in velocity space —
reversible in principle, irreversible in practice. This is a transport phenomenon in the *kinetic*
sense: it moves energy in phase space rather than in physical space.

## L3 · What the mathematics guarantees

* **BGK preserves exact conservation and an H-theorem**, so it inherits the positivity of transport
  coefficients — a rare case where a simplification is provably safe.
* **Landau damping is a theorem for analytic data (Villani–Mouhot 2010)** but is *not* damping for
  rough data: the electric field decays while the distribution develops fine structure. Decay is a
  statement about smoothness, not about energy loss.
* **Quasineutrality is a limit.** Debye-scale boundary layers (sheaths) persist even when
  $\lambda_D/L\to0$; neglecting them gives wrong wall fluxes — the plasma analogue of
  [electroneutrality and Debye layers](../03-microscopic/07-charged-and-electrochemical-transport.md).
* **The fluid limit needs care.** Chapman–Enskog for magnetised plasmas produces anisotropic
  transport (Braginskii): $\kappa_\parallel\gg\kappa_\perp$, with heat flowing along field lines — the
  reason a tokamak's transport is dominated by field-line geometry.

## L4 · Numerics

* **Particle-in-cell (PIC)** is the workhorse: sample the distribution with macroparticles, deposit
  charge to a grid, solve the field, push the particles. Noise scales as $1/\sqrt{N}$; energy
  conservation must be monitored.
* **Velocity-space discretisation** (finite volume/semi-Lagrangian on a $(\mathbf{x},\mathbf{v})$ grid)
  avoids noise but suffers from filamentation, which must be controlled by conservative,
  positivity-preserving schemes.
* **Asymptotic-preserving schemes** are essential: they must behave sensibly as
  $\lambda_D/L\to0$ and as collision time $\to0$, without resolving either scale.
* **Benchmarks**: Landau damping rates, two-stream instability growth rates, the Braginskii transport
  coefficients, and sheath profiles
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Gyrokinetic turbulence for fusion; cosmic-ray transport in magnetised turbulence;
  reconnection and collisionless shocks.

## Checks

1. What does BGK replace, and what does it preserve? *(The collision integral; conservation laws, H
   and positivity.)*
2. How can a wave damp with no collisions? *(Phase mixing: energy moves to fine velocity-space
   structure.)*
3. Why is plasma thermal conduction anisotropic? *(Charged particles move freely along field lines but
   are confined across them.)*

## See also

[The Boltzmann equation](01-boltzmann-equation.md) ·
[Charged & electrochemical transport](../03-microscopic/07-charged-and-electrochemical-transport.md) ·
[MHD & relativistic transport](../06-beyond/13-mhd-and-relativistic-transport.md) ·
[Plasma & astrophysics](../08-bridges/05-plasma-and-astrophysics.md)
