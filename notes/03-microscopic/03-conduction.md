---
title: Conduction (Fourier)
blurb: Heat transport by contact — Fourier's law, phonons and electrons, contact resistance, and why the same equation describes so many different things.
depth: 2
tags: [Fourier, phonon, thermal conductivity, Wiedemann-Franz, contact resistance]
---

# Conduction (Fourier)

> **One-line picture.** Heat is the jitter of atoms. Conduction is that jitter being passed along
> from neighbour to neighbour without the material moving — one bucket brigade, no crowd.
>
> **Prerequisites.** [diffusion](01-diffusion.md),
> [constitutive relations](../01-foundations/03-constitutive-relations.md) · **Leads to.**
> [phase change & Stefan](../04-interaction/09-phase-change-and-stefan.md),
> [engineering devices](../08-bridges/06-engineering-devices.md)

## L1 · What it is

Touch a metal spoon to a flame. The handle warms long before the flame reaches it. No material has
travelled: the energy passes down the rod as atomic vibrations (phonons) and, in metals, as mobile
electrons. It is a *contact* mechanism — it needs a medium, and it stops dead at a vacuum (which is
why vacuum flasks exist).

The same mathematics describes charge conduction in wires, thermal conduction in windows and
diffusion in a beaker; only the coefficient and the carrier changes. This is the first place where
the [heat–mass–momentum analogy](../08-bridges/01-analogy-and-circuit-models.md) pays off.

## L2 · Fourier's law and the heat equation

$$\mathbf{q}=-k\nabla T,\qquad \rho c_p\,\partial_tT=\nabla\cdot(k\nabla T)+\dot q_{\rm gen},$$

with thermal diffusivity $\alpha=k/(\rho c_p)$. Typical values tell you most of what you need:

| Material | $k$ (W/m·K) | $\alpha$ (m²/s) | Remark |
|---|---|---|---|
| copper | 400 | $1.1\times10^{-4}$ | electrons dominate |
| water | 0.6 | $1.4\times10^{-7}$ | convection usually beats conduction |
| air | 0.026 | $2\times10^{-5}$ | insulators trap air |
| silica aerogel | 0.015 | — | nanostructure below gas mean free path |
| diamond | 2000 | — | phonon transport at its best |
| human tissue | 0.2–0.6 | — | drives thermal therapies |

For steady 1-D conduction, this collapses to the **thermal resistance** network
$R=L/(kA)$, in series and parallel exactly like resistors — the reason thermal engineers draw
circuits, not PDEs.

## L3 · What the mathematics guarantees

* **Maximum principle and smoothness.** Temperature never overshoots the data, and interior
  gradients relax; the steady problem has no interior extrema.
* **Interfaces and jump conditions.** The flux is continuous while $k$ jumps, so the *gradient* has
  a kink: $\llbracket k\partial_nT\rrbracket=0$. Getting this wrong is the classic source of a
  spurious interface source in codes. In practice a thin layer of imperfect contact adds a
  **contact resistance** $R_{\rm c}=1/h_{\rm c}$ — often dominant in electronics.
* **Ballistic limits.** Fourier's law assumes carriers scatter many times across the device. As
  the mean free path approaches the feature size, conduction becomes *ballistic* and the law fails:
  nanowires, thin films and graphene show size-dependent $k$, and heat can travel as waves
  (second sound) — see [Cattaneo & hyperbolic heat](../06-beyond/04-memory-viscoelastic-and-hereditary.md).
* **Carrier physics gives the coefficient.** Kinetic theory gives $k\approx\frac13 C v\ell$ with
  $C$ the heat capacity, $v$ the carrier speed, $\ell$ the mean free path. In metals, the
  Wiedemann–Franz law ties $k$ to electrical conductivity, $k/(\sigma T)\approx L_0$ — a reminder
  that transport coefficients are linked by their microscopic carriers.

## L4 · Numerics

* **Multi-material solvers** must conserve flux at interfaces; use harmonic averaging of $k$ on
  faces ([structure-preserving](../07-numerics/13-structure-preserving-discretizations.md)).
* **Nonlinear materials** ($k(T)$, phase change with latent heat) make the problem nonlinear:
  effective-heat-capacity or enthalpy methods are standard, with the sharp latent-heat release
  handled implicitly or by [front tracking](../04-interaction/09-phase-change-and-stefan.md).
* **Radiation couples in at high temperature** (furnaces, re-entry, combustion) and is non-local —
  you need [radiative transfer](../05-kinetic/04-radiative-transfer.md), not a bigger $k$, though
  the Rosseland diffusion approximation is often a good first step.
* **Benchmarks**: 1-D composite wall, the Stefan problem, and pulsed laser heating (thermoreflectance)
  for extracting $k$ and interface conductance
  ([measurement](../10-appendix/05-measurement-and-experiments.md)).

## Checks

1. Why does a metal feel colder than wood at the same temperature? *(Much larger $k$ and $\alpha$:
   it draws heat from your finger faster.)*
2. Why must the gradient kink at a material interface? *(Flux continuity with different $k$.)*
3. When does Fourier's law fail? *(When the carrier mean free path is comparable to the device —
   nanoscale and ultrafast regimes.)*

## See also

[Diffusion](01-diffusion.md) ·
[Phase change & Stefan](../04-interaction/09-phase-change-and-stefan.md) ·
[Radiation & neutron transport](../05-kinetic/04-radiative-transfer.md) ·
[Heat–mass–momentum analogy](../08-bridges/01-analogy-and-circuit-models.md)
