---
title: Shear dispersion (Taylor–Aris)
blurb: How a velocity gradient turns into an effective diffusion tensor — the mechanism behind every tracer test, and a model of how upscaling works.
depth: 3
tags: [Taylor-Aris, macrodispersion, moments, upscaling]
---

# Shear dispersion (Taylor–Aris)

> **One-line picture.** When the fluid moves faster in some places than others, a blob of tracer
> gets *sheared* into a long stripe, and only the cross-stream diffusion that folds it back makes
> the spread look like (much larger) diffusion.
>
> **Prerequisites.** [advection](01-advection.md), [diffusion](../03-microscopic/01-diffusion.md) ·
> **Leads to.** [porous media & Darcy](08-porous-media-and-darcy.md),
> [words that collide #1](../09-polysemy/01-dispersion.md)

![**Figure 13.** The mechanism (Taylor, 1953): a parabolic Poiseuille profile stretches a blob along the channel while cross-stream diffusion continually re-injects material into different streamlines. After a while the blob is Gaussian again — with a diffusion coefficient far larger than the molecular one.](../../figures/taylor-aris.svg)

## L1 · The observation that started it

Inject dye into a pipe. You expect it to travel at the mean velocity and spread by molecular
diffusion, $D\sim10^{-9}$ m²/s — i.e. barely at all over a metre. What you actually observe is a
blob that spreads by centimetres over that distance: an *effective* diffusivity $10^{5}$ times
larger. Taylor's 1953 explanation: the parabolic velocity profile smears the blob into a thin
parabola (fast centre, slow walls), while molecular diffusion shuffles material across
streamlines. The two together are equivalent to a single Fickian diffusion with

$$D_{\rm eff}=D+\frac{a^2U^2}{48D}\qquad\text{(tube radius }a,\ \text{mean }U),$$

valid once the tracer has had time to sample all streamlines, $t\gg a^2/D$.

## L2 · Why the $U^2/D$ is not a mistake

The counter-intuitive form — diffusion in the *denominator* — is the heart of the mechanism:

| Regime | Time scale | Behaviour |
|---|---|---|
| $t\ll a^2/D$ | shear dominates | the blob is a parabola, spread grows as $Ut$ |
| $t\gg a^2/D$ | cross-stream mixing complete | Gaussian, spread grows as $\sqrt{D_{\rm eff}t}$ |
| $D\to0$ | no cross-stream mixing | no Fickian limit at all: a frozen striped pattern |

Small molecular diffusivity makes the *early* spread violent (the stripe is longer) but delays the
onset of the Fickian regime. In porous media, the same mechanism with many flow paths is called
**mechanical (hydrodynamic) dispersion**, described by a tensor with longitudinal and transverse
components aligned with the flow:

$$D_L=\alpha_L|\mathbf{v}|+D_m,\qquad D_T=\alpha_T|\mathbf{v}|+D_m,\qquad \alpha_L\approx(10{-}100)\alpha_T .$$

## L3 · What the mathematics guarantees

* **Moment analysis.** Track $\int c\,\mathrm{d}x$, $\int xc\,\mathrm{d}x$, $\int x^2c\,\mathrm{d}x$:
  the centre of mass moves at the *flux-averaged* velocity, and the variance grows linearly for
  large $t$ with slope $2D_{\rm eff}$. Dispersion coefficients are defined by long-time *moments*,
  not by local fluxes.
* **It is homogenisation in miniature.** The solvability condition of a cell problem produces
  exactly $a^2U^2/48D$; see [upscaling](../06-beyond/08-homogenization-and-upscaling.md).
* **Skewness and preasymptotics.** At intermediate times the distribution is skewed (a long tail
  of slow material near the walls). Breakthrough curves that "have a tail" are usually in this
  preasymptotic regime — very common in groundwater, where $t\gg a^2/D$ may take years.
* **Validity conditions matter.** Taylor–Aris assumes steady laminar flow, uniform tube, and
  $\mathrm{Pe}\,a/L$ small enough that the tracer samples the profile. Reactive transport,
  turbulence and dead-end pores all modify the result, sometimes decisively
  ([sorption](../04-interaction/07-sorption-and-retardation.md)).

## L4 · Numerics

* **Resolution requirement:** the cross-stream profile must be resolved or the effective
  dispersion is *numerical*, not physical. Codes that use coarse transverse grids invent their own
  $\alpha_T$.
* **Grid orientation artifacts:** in isotropic media $\alpha_L/\alpha_T$ ratios of 100 mean a
  rotated flow direction has enormous effective dispersion; tensor rotation is a standard source
  of bugs.
* **Benchmarks:** the classic two-region (mobile–immobile) tests and column experiments; use
  breakthrough curves, not snapshots, to fit dispersion
  ([measurement](../10-appendix/05-measurement-and-experiments.md)).
* **Frontiers.** Non-Fickian dispersion in heterogeneous media with broad residence-time
  distributions — the crossover to [anomalous transport](../03-microscopic/08-anomalous-diffusion.md).

## Checks

1. Why does a *smaller* molecular diffusivity give a larger effective dispersion? *(The sheared
   stripe is longer; cross-stream mixing is slower, so the Fickian limit is delayed — but the
   asymptotic coefficient grows as $1/D$.)*
2. At what time is the Taylor–Aris formula valid? *($t\gg a^2/D$.)*
3. Why do transverse and longitudinal dispersivities differ by orders of magnitude? *(Flow paths
   differ mostly along the flow direction; crossing streamlines requires molecular or turbulent
   motion.)*

## See also

[Porous media & Darcy](08-porous-media-and-darcy.md) ·
[Turbulence & eddy diffusivity](05-turbulence-and-eddy-diffusivity.md) ·
[Words that collide: dispersion](../09-polysemy/01-dispersion.md) ·
[Homogenisation & upscaling](../06-beyond/08-homogenization-and-upscaling.md)
