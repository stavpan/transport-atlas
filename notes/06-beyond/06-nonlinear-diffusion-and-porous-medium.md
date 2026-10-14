---
title: Nonlinear diffusion & the porous medium equation
blurb: When diffusivity depends on the density — finite-speed fronts, Barenblatt profiles, and why "diffusion" can behave like a wave.
depth: 3
tags: [porous medium, Barenblatt, p-Laplacian, nonlinear diffusion, free boundary]
---

# Nonlinear diffusion & the porous medium equation

> **One-line picture.** Make the diffusivity depend on the concentration and diffusion stops being
> infinitely fast: it acquires a sharp edge and behaves partly like a wave.
>
> **Prerequisites.** [diffusion](../03-microscopic/01-diffusion.md) ·
> **Leads to.** [free boundaries & phase field](09-free-boundaries-level-sets-and-phase-field.md),
> [optimal transport & gradient flows](10-optimal-transport-and-gradient-flows.md)

## L1 · Three ways for diffusion to be nonlinear

$$\partial_tc=\nabla\cdot\big(D(c)\nabla c\big)\quad\Longleftrightarrow\quad
\partial_tc=\nabla\cdot\big(mc^{m-1}\nabla c\big)=\nabla^2(c^m).$$

* **Degenerate diffusion** — $D(c)\to0$ as $c\to0$: this is the **porous medium equation**
  ($\partial_tc=\Delta c^m$, $m>1$). Gas flowing in soil, groundwater in an unconfined aquifer, heat
  radiation in a plasma, population dispersal with crowding.
* **Fast diffusion** — $D(c)\to\infty$ as $c\to0$ ($m<1$): solutions can vanish in finite time;
  used in plasma physics and for thin films.
* **$p$-Laplacian / non-Newtonian filtration** — $D\propto|\nabla c|^{p-2}$: shear-thinning flow in
  porous media, image processing (total-variation denoising), glaciology.

The headline difference from linear diffusion: **finite speed of propagation**. A compactly supported
initial blob stays compactly supported, with a genuinely moving boundary — an interface you can
specify and track ([free boundaries](09-free-boundaries-level-sets-and-phase-field.md)).

## L2 · The similarity solution and its consequences

The porous-medium equation has the Barenblatt–Pattle solution
$c(\mathbf x,t)=t^{-\alpha}\big[1-\big(r/t^{\beta}\big)^2\big]_+^{\,1/(m-1)}$ with
$\alpha=d/(d(m-1)+2)$ and $\beta=\alpha/d$. The consequences are all visible in that formula:

| Feature | Linear diffusion | Porous medium ($m>1$) |
|---|---|---|
| support | infinite for $t>0$ | compact, moving front |
| front speed | infinite | finite, $\propto t^{\beta}$ |
| central value | $\propto t^{-d/2}$ | $\propto t^{-\alpha}$ (slower decay for $m>1$) |
| long-time state | Gaussian | Barenblatt profile |
| comparison principle | yes | yes (with a modulus) |

Barenblatt profiles also appear as the long-time attractor for *any* compactly supported data — the
nonlinear analogue of the central limit theorem for these flows, and the reason they are the natural
test cases for nonlinear diffusion codes.

## L3 · What the mathematics guarantees

* **Well-posedness by parabolic regularisation.** The equation is degenerate, so solutions are only
  Hölder continuous; existence follows from "regularised" equations ($D\geq\varepsilon$) plus compactness
  arguments (Aronson, Caffarelli–Vázquez).
* **Speed of propagation is finite and computable.** The support expands like $t^{1/(d(m-1)+2)}$ —
  derived from the similarity solution and confirmed by the theory of the free boundary.
* **Entropy and gradient-flow structure.** PME is the Wasserstein gradient flow of the internal energy
  $\frac{1}{m-1}\int c^m$; displacement convexity gives contraction and uniqueness — the cleanest
  demonstration that the "right" geometry depends on the physics
  ([optimal transport](10-optimal-transport-and-gradient-flows.md)).
* **Nonlinearity can destroy uniqueness.** For certain $p$-Laplacian-type problems with measure data,
  non-uniqueness is genuine: the maximum principle and comparison arguments do not simply carry over.
* **Interfaces can be non-smooth.** Solutions of the PME have interfaces whose derivatives may blow up
  at the edge; a genuine contact-line analysis is required (relevant to wetting and to
  Hele-Shaw flow).

## L4 · Numerics

* **Track the front or resolve it.** Uniform grids waste effort on the empty region around the support;
  moving meshes, level sets or front-tracking give far better accuracy per grid point
  ([moving meshes](../07-numerics/08-mesh-adaptivity-moving-domains-and-parallel.md)).
* **Preserve positivity and the support.** Schemes that create small positive values outside the support
  destroy the finite-speed property; use positivity-preserving, entropy-stable discretisations.
* **Nonlinear iterations.** Newton may struggle at the front; use damped Newton, Picard, or
  JKO/backward-Euler minimisation, which is monotone
  ([nonlinear solvers](../07-numerics/07-nonlinear-solvers-and-continuation.md)).
* **Benchmarks**: Barenblatt profile convergence, the "waiting time" problem for a blob on a slope,
  and the Hele–Shaw analogue ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Nonlinear diffusion on manifolds and networks; degenerate diffusion with reactions
  (combustion, tumour growth); nonlocal PME; rigorous long-time asymptotics.

## Checks

1. Why does the porous-medium equation propagate at finite speed? *($D\to0$ at the edge, so the edge
   cannot move until material arrives — mathematically, degeneracy at $c=0$.)*
2. What is the long-time attractor for compact data? *(The Barenblatt–Pattle profile.)*
3. Which functional makes PME a gradient flow, and in which metric? *(Internal energy
   $\frac{1}{m-1}\int c^m$, in the Wasserstein $W_2$ metric.)*

## See also

[Diffusion](../03-microscopic/01-diffusion.md) ·
[Free boundaries, level sets & phase field](09-free-boundaries-level-sets-and-phase-field.md) ·
[Optimal transport & gradient flows](10-optimal-transport-and-gradient-flows.md) ·
[Images & signals](../08-bridges/08-images-and-signals.md)
