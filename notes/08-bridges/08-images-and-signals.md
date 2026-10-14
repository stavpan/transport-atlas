---
title: Transport in images & signals
blurb: Blurring is the heat equation, edge-preserving smoothing is nonlinear diffusion, inpainting is a free boundary, and shock filters are Hamilton–Jacobi.
depth: 3
tags: [image processing, Perona-Malik, total variation, shock filter, level set]
---

# Transport in images & signals

> **One-line picture.** Every classic image-processing operation is a PDE in disguise: smoothing is heat
> flow, edge preservation is nonlinear diffusion, and segmentation is a moving front.
>
> **Prerequisites.** [diffusion](../03-microscopic/01-diffusion.md),
> [nonlinear diffusion](../06-beyond/06-nonlinear-diffusion-and-porous-medium.md)

## L1 · The dictionary

| Image operation | PDE | Notes |
|---|---|---|
| Gaussian blur | heat equation $\partial_tu=\Delta u$ | scale $t$ is the blur radius squared |
| anisotropic diffusion (Perona–Malik) | $\partial_tu=\nabla\!\cdot\!\big(g(\|\nabla u\|)\nabla u\big)$ | diffusivity falls where gradients are large |
| denoising by total variation | $\partial_tu=\nabla\!\cdot\!\big(\nabla u/\|\nabla u\|\big)$ | $L^1$ of gradients; keeps edges, makes staircases |
| shock filter | $\partial_tu=-\|\nabla u\|\,F(D^2u)$ | Hamilton–Jacobi: sharpens edges |
| inpainting | diffusion with a constraint on the known region | obstacle/complementarity structure |
| segmentation / active contours | level-set front motion | curve evolution, topology change free |
| optical flow | advection–diffusion for the flow field | brightness constancy is an advection constraint |
| scale space / structure tensor | anisotropic heat kernel on the image | multiscale analysis by diffusion time |
| diffusion maps / manifold learning | heat kernel on a data graph | eigenfunctions of the graph Laplacian |

Two bridges are deeper than they look: **the heat equation's semigroup is the multiscale representation of
an image** (Gaussian pyramids are diffusion in time), and **the graph Laplacian of a data cloud converges
to the Laplace–Beltrami operator of the underlying manifold** — which is why diffusion-based methods are
legitimate geometry, not heuristics.

## L2 · Why nonlinearity is essential

Linear diffusion smooths edges as fast as noise — unacceptable for images. Perona–Malik's insight was to
make the diffusivity depend on the local gradient: strongly diffusive in flat regions, nearly zero across
edges. The result behaves like anisotropic diffusion along level lines, and it is a
[nonlinear diffusion](../06-beyond/06-nonlinear-diffusion-and-porous-medium.md) equation with all the
attendant theory: well-posedness requires regularisation (the equation as originally proposed can be
backward-diffusive for steep gradients), and total-variation flow is the degenerate limit that keeps edges
while removing oscillation.

## L3 · What the mathematics guarantees

* **Maximum principle and scale-space axioms** justify Gaussian blur as *the* linear smoothing (Koenderink:
  causality, isotropy and linearity force the heat equation).
* **TV flow is a gradient flow** of total variation and has a well-developed theory (with staircasing as a
  known artifact) — a rare case where an image-processing heuristic has complete analysis.
* **Shock filters and level-set segmentation are viscosity solutions** of Hamilton–Jacobi equations, so
  monotone numerics are required for stability
  ([Hamilton–Jacobi](../06-beyond/02-hamilton-jacobi-and-viscosity-solutions.md)).
* **Inpainting is a free-boundary/complementarity problem**: the solution must satisfy the PDE where data
  is missing and match the data where it exists ([variational inequalities](../06-beyond/12-variational-inequalities-and-hysteresis.md)).

## L4 · Practice

* **Choose the scheme by the structure you want**: explicit with small steps for accuracy, operator
  splitting for speed (splitting diffusion from fidelity), and AOS/implicit schemes for unconditional
  stability ([splitting](../07-numerics/05-operator-splitting-and-multiphysics-coupling.md)).
* **Do not over-smooth**: every diffusion-based method trades noise against detail in a way that is exactly
  quantified by its diffusion coefficient — measure it.
* **For PDE-based vision, verify with synthetic ground truth**: Gaussian blur with a known $\sigma$, TV
  denoising of piecewise constants, and level-set motion of a circle.

## Checks

1. Why is Gaussian blur the "right" linear smoother? *(Scale-space axioms force the heat equation.)*
2. What goes wrong with unregularised Perona–Malik? *(It can be backward-diffusive for large gradients:
   ill-posed, noise-amplifying.)*

## See also

[Nonlinear diffusion & porous medium](../06-beyond/06-nonlinear-diffusion-and-porous-medium.md) ·
[Hamilton–Jacobi & viscosity solutions](../06-beyond/02-hamilton-jacobi-and-viscosity-solutions.md) ·
[The spectral view](../01-foundations/06-spectral-and-green-function-view.md) ·
[Machine learning & data](07-machine-learning-and-data.md)
