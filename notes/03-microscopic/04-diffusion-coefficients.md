---
title: Diffusion coefficients
blurb: Where D comes from microscopically — kinetic theory estimates, temperature and pressure scaling, and why measured values disagree with naive formulas.
depth: 3
tags: [Chapman-Enskog, kinetic theory, Arrhenius, tortuosity]
---

# Diffusion coefficients

> **One-line picture.** Fick's law is easy; the number in it is not. $D$ is a hydrodynamic
> statement about molecules that you can estimate in three ways, none of which is exact.
>
> **Prerequisites.** [diffusion](01-diffusion.md) · **Leads to.**
> [Knudsen & rarefied transport](05-knudsen-and-rarefied-transport.md),
> [Boltzmann equation](../05-kinetic/01-boltzmann-equation.md)

## L1 · Three routes to one number

1. **Empirical correlations** — Stokes–Einstein for large solutes, Wilke–Chang for liquids,
   Fuller for gases. Fast, broadly accurate, silent about limits.
2. **Kinetic theory** — mean free path over thermal speed, refined by Chapman–Enskog; excellent for
   dilute gases and for gases with known intermolecular potentials.
3. **Simulation** — molecular dynamics with Green–Kubo integrals
   ([linear response](../01-foundations/09-linear-response-and-memory.md)); the only route when the
   medium is complex (electrolytes, polymers, confining pores).

## L2 · The estimates

| Case | Formula | Notes |
|---|---|---|
| dilute gas (hard spheres) | $D\approx\frac13\bar v\lambda$, $\lambda\propto1/(n\sigma)$ | $D\propto T^{3/2}/p$: **independent of pressure at fixed composition** in mole fraction terms, decreasing with $p$ |
| dilute gas (real potential) | Chapman–Enskog: $D\propto T^{1.5{-}1.8}/(p\sigma^2\Omega)$ | collision integral $\Omega$ from the potential |
| large sphere in liquid | $D=k_BT/(6\pi\mu a)$ | Stokes–Einstein (valid for $a\gg$ solvent size) |
| liquid self-diffusion | $D\sim k_BT/(\zeta)$ with $\zeta$ from viscosity | free-volume and Arrhenius forms; strong $T$ dependence |
| electrolyte at infinite dilution | Nernst–Einstein: $D_i=RT\lambda_i/(z_i^2F^2)$ | links $D$ to molar conductivity |
| porous medium | $D_{\rm eff}=D\theta/\tau$ | tortuosity $\tau>1$; measured, never guessed |
| in a membrane/tissue | $D_{\rm eff}$ plus obstructions | crowding makes it anomalous at short times |

**Two scaling laws worth memorising:** in gases, $D$ rises steeply with temperature
(roughly $T^{1.8}$) and falls as $1/p$; in liquids, $D$ follows an Arrhenius or free-volume law and
is fairly insensitive to pressure but very sensitive to viscosity and structure.

## L3 · Where the clean formulas fail

* **Small solutes.** Stokes–Einstein overestimates $D$ for molecules comparable to the solvent;
  the effective hydrodynamic radius is not the molecular radius.
* **Concentration.** In non-ideal mixtures, the driving force is the *gradient of chemical
  potential*, not of concentration, so Fick's $D$ becomes activity-corrected,
  $D=D_{\rm MS}(1+\partial\ln\gamma/\partial\ln c)$ ([Maxwell–Stefan](06-cross-effects-and-multicomponent.md)).
* **Non-ideal and multicomponent systems** require a diffusivity *matrix*, and ternary systems can
  show uphill diffusion (a component moving up its own gradient) — impossible for a scalar $D$.
* **Crowding and confinement.** Diffusion slows and often becomes anomalous in the presence of
  obstacles, binding sites and attractive walls; the long-time $D$ can be orders of magnitude below
  the short-time value ([anomalous diffusion](08-anomalous-diffusion.md)).
* **Cross-effects.** A temperature gradient adds a Soret flux, an electric field an ionic one —
  measured $D$ then depends on the experiment
  ([cross-effects](06-cross-effects-and-multicomponent.md)).

## L4 · Measurement and numerics

* **Standard methods**: diaphragm cell (classic, slow), Taylor dispersion in a capillary (precise),
  PFG-NMR, DLS, and electrochemical techniques for ions
  ([measurement](../10-appendix/05-measurement-and-experiments.md)).
* **Molecular dynamics pitfalls**: finite-size corrections ($D$ depends on box size), thermostat
  artifacts, and correlation-function tails; report the estimator and the fit window.
* **Inverse use**: fit $D(\mathbf{x},c)$ from column or field data — usually
  [ill-posed and regularised](../07-numerics/10-inverse-problems-and-data-assimilation.md).
* **Frontiers.** Machine-learned diffusion coefficients that respect thermodynamic consistency;
  concentration-dependent diffusivity in battery electrolytes; nanoconfined transport.

## Checks

1. Why does gas-phase $D$ fall as pressure rises but rise faster than linearly with temperature?
   *($D\propto T^{1.5}/p$: the mean free path sets both.)*
2. Why can Stokes–Einstein fail for a 0.2 nm ion? *(The hydrodynamic radius concept breaks down at
   molecular scales; hydration shells dominate.)*
3. What does tortuosity do to $D_{\rm eff}$? *(Reduces it, roughly as $\theta/\tau$ with
   $\tau$ typically 1.5–5.)*

## See also

[Diffusion](01-diffusion.md) ·
[Knudsen & rarefied transport](05-knudsen-and-rarefied-transport.md) ·
[Cross-effects & multicomponent](06-cross-effects-and-multicomponent.md) ·
[Boltzmann equation](../05-kinetic/01-boltzmann-equation.md)
