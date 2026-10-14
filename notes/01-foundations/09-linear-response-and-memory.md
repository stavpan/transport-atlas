---
title: Linear response & memory
blurb: What to do when the past matters — Green–Kubo relations, memory kernels, Mori–Zwanzig projection, and why every effective transport coefficient is a correlation function.
depth: 3
tags: [Green-Kubo, memory kernel, Mori-Zwanzig, model reduction, FDT]
---

# Linear response & memory

> **One-line picture.** Kick a material gently and it responds linearly — but not instantly.
> The response is remembered, and the memory is a correlation function of the microscopic
> fluctuations you chose to ignore.
>
> **Prerequisites.** [random walks & Langevin](08-random-walks-langevin-response.md) ·
> **Leads to.** [viscoelastic transport](../06-beyond/04-memory-viscoelastic-and-hereditary.md),
> [homogenisation](../06-beyond/08-homogenization-and-upscaling.md)

## L1 · Materials remember

Push honey and let go: it keeps moving. Cool a polymer melt locally: it over-relaxes before
settling. In both cases the flux is not set by the gradient *now*, but by an integral over the
gradients that came before:

$$\mathbf{J}(t)=\int_{-\infty}^{t}M(t-t')\,\mathbf{X}(t')\,\mathrm{d}t' .$$

$M$ is a **memory kernel**. Fick's law, Fourier's law and Newton's law of viscosity are the
special case $M\propto\delta(t-t')$ — an *instantaneous* response. That is a modelling choice,
not a law of nature.

## L2 · Green–Kubo: transport coefficients are correlation functions

The coefficients you measure macroscopically can be computed from equilibrium fluctuations:

| Coefficient | Green–Kubo formula |
|---|---|
| self-diffusion | $D=\frac13\int_0^\infty\langle\mathbf{v}(0)\!\cdot\!\mathbf{v}(t)\rangle\,\mathrm{d}t$ |
| shear viscosity | $\eta=\frac{V}{k_BT}\int_0^\infty\langle\sigma_{xy}(0)\sigma_{xy}(t)\rangle\,\mathrm{d}t$ |
| thermal conductivity | $k=\frac{V}{3k_BT^2}\int_0^\infty\langle\mathbf{q}(0)\!\cdot\!\mathbf{q}(t)\rangle\,\mathrm{d}t$ |
| electrical conductivity | $\sigma=\frac{V}{3k_BT}\int_0^\infty\langle\mathbf{j}(0)\!\cdot\!\mathbf{j}(t)\rangle\,\mathrm{d}t$ |

Three consequences: **transport *is* fluctuation** (no fluctuations, no transport); **equilibrium
simulations predict nonequilibrium behaviour** (no gradients required); **correlation functions
are the universal currency**, which is why molecular dynamics measures $D$, $\eta$, $k$ by
integrating autocorrelations. Fourier transforming $M$ gives frequency-dependent coefficients
$D(\omega)$, $\eta(\omega)$ — real part is dissipation, imaginary part reactive response, and
causality ties them together through Kramers–Kronig.

## L3 · Mori–Zwanzig: where effective equations come from

Project the full $10^{23}$-dimensional dynamics onto a few slow variables and you get, *exactly*,

$$\partial_t(\text{slow})=\underbrace{\text{Markovian drift}}_{\text{expected}}
+\underbrace{\int_0^tK(t-s)\,(\text{slow})(s)\,\mathrm{d}s}_{\text{memory}}
+\underbrace{\mathcal{F}(t)}_{\text{noise}},\qquad \text{memory}\leftrightarrow\text{noise by FDT}.$$

So: **you never obtain a closed Markovian equation for the slow variables without either
losing information, or accepting a memory kernel plus noise.** Every subgrid model, eddy
viscosity, effective diffusivity and coarse-grained parameter is an approximation to $K$ and
$\mathcal{F}$. The FDT says which approximations are legal — and why
[homogenised and stochastic models](../06-beyond/08-homogenization-and-upscaling.md) contain
noise even when the original problem had none.

## L4 · Numerics, limits, frontiers

* **Estimating kernels from data.** Integrate equilibrium time-correlation functions over long
  molecular-dynamics runs; the *tail* dominates the error, so use windowing or
  Einstein–Helfand estimators rather than naive trapezoid integration.
* **Power-law memory $=$ fractional derivatives.** $M(t)\sim t^{-\alpha}$ turns the convolution
  into a [fractional operator](../06-beyond/03-nonlocal-and-fractional-operators.md): the origin
  of fractional viscoelasticity, fractional diffusion and
  [history-dependent rheology](../06-beyond/04-memory-viscoelastic-and-hereditary.md).
* **Cost of memory.** A convolution in time is $O(N^2)$; sum-of-exponentials, fast-convolution
  and FFT schemes reduce it to $O(N\log N)$ — standard in fractional solvers.
* **Markovianisation.** A memory kernel that is a sum of exponentials can be replaced exactly by
  a few auxiliary variables (generalised Maxwell, Prony series, hidden Markov), making the
  problem local in time again. This is the workhorse of practical viscoelastic simulation.
* **Frontiers.** Learning memory kernels and transfer operators from data (Koopman theory);
  non-Markovian turbulence and climate closures; FDT-respecting learned closure operators
  ([ML for transport](../07-numerics/11-machine-learning-and-operator-learning.md)).

## Checks

1. Why must the Green–Kubo formula use *equilibrium* fluctuations? *(Linear response relates
   nonequilibrium transport to equilibrium correlations; that is the content of the FDT.)*
2. When is a plain diffusion equation legitimate for a viscoelastic solvent? *(When the kernel
   decays much faster than any observation time, so $M\approx$ const.)*
3. What extra objects appear when you eliminate a fast variable? *(A memory integral and a noise
   term, tied together by an FDT.)*

## See also

[Random walks & Langevin](08-random-walks-langevin-response.md) ·
[Memory & viscoelastic transport](../06-beyond/04-memory-viscoelastic-and-hereditary.md) ·
[Homogenisation & upscaling](../06-beyond/08-homogenization-and-upscaling.md) ·
[Nonlocal & fractional operators](../06-beyond/03-nonlocal-and-fractional-operators.md)
