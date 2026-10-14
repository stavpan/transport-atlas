---
title: Words that collide 1 — dispersion
blurb: One word, four sciences: porous-media spreading, Taylor shear dispersion, wave dispersion, and numerical phase error.
depth: 2
tags: [polysemy, dispersion, terminology]
---

# "Dispersion" means at least four different things

> **Why this note exists.** Almost every confusion between a hydrodynamicist, a hydrogeologist, a
> spectroscopist and a numerical analyst starts with this word.
>
> **Prerequisites.** [advection](../02-bulk/01-advection.md),
> [shear dispersion](../02-bulk/06-shear-dispersion-taylor-aris.md)

## The four meanings

| Meaning | Domain | What it is | Where it lives here |
|---|---|---|---|
| **mechanical / hydrodynamic dispersion** | porous media, groundwater | spreading caused by velocity variation in pores and flow paths; a tensor, $\alpha_L\gg\alpha_T$ | [Darcy flow](../02-bulk/08-porous-media-and-darcy.md) |
| **shear (Taylor–Aris) dispersion** | pipe and channel flow | spreading from a velocity profile coupled to cross-stream diffusion; $D_{\rm eff}=D+a^2U^2/48D$ | [Taylor–Aris](../02-bulk/06-shear-dispersion-taylor-aris.md) |
| **wave dispersion** | waves and optics | oscillation frequency depends on wavenumber, $\omega=\omega(k)$; different wavelengths travel at different speeds | [spectral view](../01-foundations/06-spectral-and-green-function-view.md) |
| **numerical dispersion** | computation | phase error of a discretisation: waves travel at the wrong speed, producing oscillations | [numerical errors](../07-numerics/03-numerical-diffusion-and-dispersion-error.md) |

Two more minor usages: **statistical dispersion** (variance/spread of any distribution) and **material
dispersion** (a medium supporting multiple wave modes, as in acoustics).

## How to keep them apart

* **Is the spreading caused by a velocity field?** If yes, it is mechanical/hydrodynamic or shear
  dispersion (transport spreading). If the *shape of a wave* changes speed with wavelength, it is wave
  dispersion.
* **Does it vanish when the flow stops?** Mechanical dispersion does; molecular diffusion does not; wave
  dispersion depends on the medium, not the flow.
* **Is it physical or numerical?** Numerical dispersion is an artifact of the scheme and disappears under
  refinement (with the right scheme); the others do not.
* **Is it a tensor or a scalar?** Hydrodynamic dispersion is anisotropic and aligned with the flow;
  numerical dispersion is aligned with the grid. Both look like diffusion; only one is real.

## The trap

> A plume that spreads ten times faster than molecular diffusion is not "diffusion" in the Fickian
> material-property sense — its coefficient depends on the velocity, the geometry and (in porous media)
> the observation scale. Reporting it as a material constant is the single most common error in
> subsurface transport.

## See also

[Shear dispersion (Taylor–Aris)](../02-bulk/06-shear-dispersion-taylor-aris.md) ·
[Porous media & Darcy](../02-bulk/08-porous-media-and-darcy.md) ·
[Numerical diffusion & dispersion](../07-numerics/03-numerical-diffusion-and-dispersion-error.md) ·
[The spectral view](../01-foundations/06-spectral-and-green-function-view.md)
