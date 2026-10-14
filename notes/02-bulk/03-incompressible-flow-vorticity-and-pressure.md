---
title: Incompressible flow, vorticity & pressure
blurb: Why pressure is a Lagrange multiplier, why vorticity is the right variable, and how projection methods actually work.
depth: 3
tags: [incompressibility, vorticity, Helmholtz, projection, pressure Poisson]
---

# Incompressible flow, vorticity & pressure

> **One-line picture.** Incompressibility is not an equation for pressure — it is a *constraint*.
> Pressure is the enforcer: it takes whatever value is needed to keep the velocity field
> divergence-free, instantly and globally.
>
> **Prerequisites.** [material derivative](../01-foundations/02-material-derivative.md) ·
> **Leads to.** [boundary layers](04-boundary-layers.md),
> [turbulence](05-turbulence-and-eddy-diffusivity.md), [MHD](../06-beyond/13-mhd-and-relativistic-transport.md)

## L1 · Two ideas in words

**Pressure is a Lagrange multiplier.** In a gas, pressure is thermodynamic: compute it from
density and temperature. In water you can raise the pressure without changing the density at all,
so the momentum equation cannot *find* it. Instead impose "every parcel keeps its volume", and
pressure becomes the field that makes that true — non-local, instantaneous, and fixed by the
boundary conditions. Physically, sound carries the message at $c_s\sim1500$ m/s; since that is
much faster than anything else in the flow, the approximation works.

**Vorticity is the fluid's memory of rotation.** $\boldsymbol\omega=\nabla\times\mathbf{u}$
measures local spin, and in an inviscid fluid it is *carried and stretched*, not created.
Turbulence, mixing, lift and most structure lives in $\boldsymbol\omega$, not in $\mathbf{u}$.

## L2 · The equations

$$\nabla\cdot\mathbf{u}=0,\qquad
\rho(\partial_t\mathbf{u}+\mathbf{u}\cdot\nabla\mathbf{u})=-\nabla p+\mu\nabla^2\mathbf{u}+\mathbf{f}.$$

Taking the divergence (and using the constraint) gives the **pressure Poisson equation**

$$\nabla^2p=-\rho\,\nabla\cdot(\mathbf{u}\cdot\nabla\mathbf{u})+\nabla\cdot\mathbf{f},$$

*elliptic*, with no time derivative: pressure adjusts globally, instantly. Taking the curl gives
the **vorticity equation**

$$\partial_t\boldsymbol\omega+\mathbf{u}\cdot\nabla\boldsymbol\omega
=\boldsymbol\omega\cdot\nabla\mathbf{u}+\nu\nabla^2\boldsymbol\omega
+\frac{1}{\rho^2}\nabla\rho\times\nabla p,$$

read as: carried (advection) $+$ **stretched** (amplified: the engine of turbulence) $+$ smoothed
by viscosity $+$ created baroclinically where $\nabla\rho$ and $\nabla p$ misalign (sea breezes,
and any non-barotropic fluid).

**Helmholtz decomposition** $\mathbf{u}=\nabla\times\boldsymbol\psi+\nabla\phi$ separates the
solenoidal and gradient parts; in 2-D it collapses to a streamfunction
$\mathbf{u}=\nabla^\perp\psi$ whose level curves are streamlines. This is the algebra behind
projection methods.

## L3 · What the mathematics guarantees

* **Non-locality is real.** The pressure problem is elliptic: a change anywhere is felt
  everywhere. Well-posedness forbids prescribing both $p$ and $\partial_np$ on the same piece of
  boundary.
* **Compatibility condition.** With pure Neumann pressure data, a solution exists only if
  $\oint\partial_np=0$. In codes this appears as a constant null space of the pressure operator;
  forgetting it gives a solver that never converges.
* **Vorticity theorems.** Kelvin (circulation conserved on material loops), Helmholtz (vortex lines
  move with the fluid), Bjerknes (baroclinic generation). Together: no vorticity can be made in
  the interior of a barotropic inviscid flow — all of it comes from boundaries, initial data, or
  non-barotropic effects.
* **2-D and 3-D are qualitatively different.** In 2-D, stretching vanishes identically, enstrophy
  is bounded, and the energy cascade runs *up* scale. In 3-D, stretching amplifies vorticity and
  the finite-time blow-up question is a Millennium Prize problem.
* **Energy balance.** $\frac{\mathrm{d}}{\mathrm{d}t}\frac{\rho}{2}\int|\mathbf{u}|^2
  =-\mu\int|\boldsymbol\omega|^2+\text{boundary work}$: vorticity *is* the dissipation.

## L4 · Numerics

* **Projection / fractional step.** Advance momentum without pressure, then project onto
  divergence-free fields by solving for a pseudo-pressure. Splitting error is $O(\Delta t)$ near
  boundaries unless higher-order rotational forms are used.
* **Staggered grids** (MAC) put velocity components on faces, pressure at cell centres: the
  discrete gradient is then the exact adjoint of the discrete divergence, so the pressure matrix
  is symmetric and has the correct null space.
* **Pressure is the expensive part.** Every step needs an elliptic solve — FFT if periodic,
  [multigrid or preconditioned Krylov otherwise](../07-numerics/06-linear-solvers-and-preconditioning.md).
* **Vorticity formulations** (vortex methods, vortex-in-cell) avoid pressure entirely: superb for
  wakes and external flows, awkward with boundaries and viscous diffusion.
* **Frontiers.** Wall models that respect vorticity generation; pressure solvers at $10^{12}$
  unknowns; regularity of 3-D Navier–Stokes.

## Checks

1. Why is there no equation of state for $p$ here? *(Density is constant by assumption, so
   thermodynamics cannot determine pressure; the constraint does.)*
2. Where does a smoke ring's vorticity come from? *(Generated at the nozzle boundary; then purely
   advected and stretched.)*
3. Why does 2-D turbulence look so different? *($\boldsymbol\omega\cdot\nabla\mathbf{u}\equiv0$: no
   stretching, no forward enstrophy cascade.)*

## See also

[Boundary layers](04-boundary-layers.md) ·
[Turbulence & eddy diffusivity](05-turbulence-and-eddy-diffusivity.md) ·
[Advection](01-advection.md) ·
[MHD & relativistic transport](../06-beyond/13-mhd-and-relativistic-transport.md)
