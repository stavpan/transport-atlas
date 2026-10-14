---
title: Sorption, partitioning & retardation
blurb: Why pollutants arrive late — isotherms, retardation factors, kinetic sorption, hysteresis, and chromatography as the laboratory version.
depth: 3
tags: [adsorption, isotherm, retardation, Langmuir, chromatography]
---

# Sorption, partitioning & retardation

> **One-line picture.** Some of the solute spends its time stuck to the solid. It still travels, but
> only for the fraction of the time it is dissolved — so it arrives later, and its tail is longer.
>
> **Prerequisites.** [advection](../02-bulk/01-advection.md), [diffusion](../03-microscopic/01-diffusion.md) ·
> **Leads to.** [porous media](../02-bulk/08-porous-media-and-darcy.md),
> [wells & breakthrough](12-wells-injection-efflux-and-breakthrough.md)

## L1 · Adsorption versus absorption

* **Adsorption** — attachment to a *surface* (activated carbon, clay, biofilm, catalyst).
  The metaphor is a sponge: molecules are sucked onto the interface.
* **Absorption** — uptake into the *bulk* of another phase (CO₂ into water, water into a polymer).
  The metaphor is dissolution.

Both reduce the dissolved concentration and hence **retard** transport. They differ in mechanism, in
saturation behaviour and usually in time scale — adsorption is often fast and reversible, absorption
is often slow and limited by interfacial resistance
([absorption & interfacial transfer](08-absorption-dissolution-and-interfacial-transfer.md)).

## L2 · Isotherms and the retardation factor

Write the mass balance for a two-phase system (dissolved concentration $c$, sorbed mass per solid
mass $F$):

$$\partial_t(\theta c+\rho_bF)+\nabla\cdot(\mathbf{u}c-\mathbf{D}\cdot\nabla c)=R(c).$$

For a **linear isotherm** $F=K_dc$ this collapses to the same advection–dispersion equation with a
retarded velocity:

$$R=1+\frac{\rho_bK_d}{\theta},\qquad v_{\rm eff}=\frac{v}{R},\qquad D_{\rm eff}=\frac{D}{R}.$$

| Isotherm | Form | Signature on the breakthrough curve |
|---|---|---|
| linear | $F=K_dc$ | shifted curve, no shape change |
| Langmuir | $F=F_{\max}K_Lc/(1+K_Lc)$ | sharpening front, tail at low $c$ |
| Freundlich | $F=K_Fc^{n}$, $n<1$ | self-sharpening at low $c$, spreading at high $c$ |
| BET | multilayer | high-concentration curvature |
| kinetic (two-site) | $\partial_tF=k_ac-k_dF$ | early breakthrough plus long tail (non-equilibrium) |

**Chromatography** is exactly this problem with a packed column and an injected pulse: retention time
*is* retardation, and peak asymmetry *is* kinetic sorption — which is why transport theory and
separation science share their equations.

## L3 · What the mathematics guarantees

* **Nonlinear isotherms change wave structure.** Convex isotherms (Langmuir) produce *shock-like*
  sharp fronts; concave ones (Freundlich) produce rarefaction-like spreading. The names come from
  [conservation-law theory](../06-beyond/01-conservation-laws-and-shocks.md), and the front speed is
  given by a Rankine–Hugoniot relation with the sorbed mass included — the reason column
  experiments can be used to *measure* isotherms.
* **Retardation is not a delay.** It changes both velocity and dispersion ($v/R$, $D/R$), so the
  *shape* of a breakthrough curve, not just its position, distinguishes sorption from a
  velocity change.
* **Hysteresis is common.** Desorption often follows a different isotherm from adsorption (slow
  release, irreversible binding), so the answer depends on history —
  [variational inequalities & hysteresis](../06-beyond/12-variational-inequalities-and-hysteresis.md).
* **Kinetic sorption breaks the Fickian assumption.** Two-site models and mass-transfer-limited
  sorption generate long tails and early breakthrough simultaneously, and are the standard
  explanation of non-Fickian field plumes
  ([words that collide #1](../09-polysemy/01-dispersion.md)).

## L4 · Numerics

* **Couple the sorbed phase as an ODE per control volume** (implicit, for stiffness) rather than
  adding an artificial diffusion. Two-site models are stiff: the fast site requires implicit
  treatment.
* **Nonlinear isotherms** need Newton iteration inside each time step; ensure the isotherm's
  derivative stays positive to preserve monotonicity.
* **Hysteresis** requires state variables (loading history) — a naive steady isotherm cannot
  reproduce it.
* **Benchmarks**: linear-retardation step response, Langmuir shock speeds, and the two-site
  breakthrough with a known analytic solution
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Competitive multicomponent sorption for remediation; sorption in nanoporous media
  with confinement effects; reactive surfaces with coupled redox chemistry.

## Checks

1. Why does a linear isotherm shift but not distort a breakthrough curve? *(It is a constant scaling
   of velocity and dispersion: $R$ is concentration-independent.)*
2. Why does Langmuir sorption sharpen fronts? *(Convex isotherm: high concentrations travel faster
   through the isotherm than low ones, so the front steepens.)*
3. How does kinetic sorption produce both early breakthrough and a long tail? *(Fast sites saturate
   immediately, slow sites release slowly.)*

## See also

[Absorption & interfacial transfer](08-absorption-dissolution-and-interfacial-transfer.md) ·
[Conservation laws & shocks](../06-beyond/01-conservation-laws-and-shocks.md) ·
[Wells & breakthrough](12-wells-injection-efflux-and-breakthrough.md) ·
[Chromatography in engineering devices](../08-bridges/06-engineering-devices.md)
