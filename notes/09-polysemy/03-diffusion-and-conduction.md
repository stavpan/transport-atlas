---
title: Words that collide 3 — diffusion & conduction
blurb: Diffusion, conduction, migration, drift and relaxation all name the same mathematics — and each names something different in physics.
depth: 2
tags: [polysemy, diffusion, conduction, terminology]
---

# "Diffusion" and "conduction" are one equation with different carriers

> **Why this note exists.** The mathematics is identical (a gradient-driven flux), the physics is not,
> and the vocabulary splits into at least six words for one idea.
>
> **Prerequisites.** [diffusion](../03-microscopic/01-diffusion.md),
> [conduction](../03-microscopic/03-conduction.md)

## One equation, six names

| Word | Carriers | Driving gradient | Coefficient | Field |
|---|---|---|---|---|
| **diffusion** (Fick) | molecules, ions, vacancies | concentration | $D$ | chemistry, biology, materials |
| **conduction** (Fourier) | phonons, electrons | temperature | $k$, $\alpha$ | heat transfer |
| **viscous diffusion** | momentum through collisions | velocity | $\nu$ | fluid mechanics |
| **migration / drift** | charged species in a field | electric potential | mobility $u$ | electrochemistry |
| **relaxation** | any excess | — | relaxation time $\tau$ | kinetic theory, rheology |
| **pseudo-diffusion** | quantised carriers | chemical potential | $D$ from Kubo | condensed matter |

Where the difference is real:

* **The conservation law differs.** Heat diffusion conserves *energy* and includes a heat capacity
  ($\alpha=k/\rho c_p$); mass diffusion conserves *mass* with $D$ alone. Mixing the two formulas is the
  most common sign of a physicist writing biology or vice versa.
* **The temperature dependence is opposite.** $D_{\rm liquid}$ falls as viscosity rises with cooling;
  $k$ of a solid generally rises with electron/phonon transport but falls with phonon–phonon scattering.
* **Drift is not diffusion.** Migration in an electric field has a *linear* dependence on the field,
  not on its gradient; it is advection in potential space, and its coupling to diffusion is fixed by the
  Einstein relation ([charged transport](../03-microscopic/07-charged-and-electrochemical-transport.md)).
* **Anisotropy shows up differently.** Laminated rock has tensor diffusion; layered composites have
  tensor conduction; in both cases the effective coefficients along and across the layering differ.

## The trap

> Because the equations are identical, a solved problem in one field is a solved problem in the other
> — *provided* the boundary conditions map. Value conditions map to value conditions, flux conditions to
> flux conditions, but a convective (Robin) condition maps to a *different* physical situation than you
> intended. Always translate the boundary conditions explicitly.

## Two more confusions worth naming

* **"Diffusion" as a whole model**: first-order decay, dispersion, or any mixing process is often called
  diffusion colloquially. Only the second-order gradient law is diffusion proper.
* **"Conduction" in electronics**: Ohm's law, ballistic conduction and quantum conduction are different
  regimes of the same word ([quantum & condensed matter](../08-bridges/10-quantum-and-condensed-matter.md)).

## See also

[Diffusion](../03-microscopic/01-diffusion.md) ·
[Conduction](../03-microscopic/03-conduction.md) ·
[Charged & electrochemical transport](../03-microscopic/07-charged-and-electrochemical-transport.md) ·
[Words that collide 1 — dispersion](01-dispersion.md)
