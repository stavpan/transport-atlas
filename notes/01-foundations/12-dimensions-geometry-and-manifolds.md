---
title: Dimensions, geometry & manifolds
blurb: How the mathematics changes with dimension — Green functions, critical dimensions, anisotropic scaling, curved space, fractals, graphs.
depth: 3
tags: [dimension, Green function, manifolds, Laplace-Beltrami, spectral dimension, anisotropy]
---

# Dimensions, geometry & manifolds

> **One-line picture.** The *dimension* is not a detail: it changes recurrence, Green functions,
> critical exponents and which nonlinearities matter. And when space is curved, the Laplacian becomes the
> Laplace–Beltrami operator and transport follows the geometry.
>
> **Prerequisites.** [The spectral view](06-spectral-and-green-function-view.md),
> [General classification](10-general-pde-classification.md) ·
> **Leads to.** [Geoscience & climate](../08-bridges/04-geoscience-and-climate.md),
> [MHD & relativistic transport](../06-beyond/13-mhd-and-relativistic-transport.md)

## L1 · Dimension is physics, not bookkeeping

Three examples of dimension deciding the answer:

* **Random walks return home in 1-D and 2-D but not in 3-D** (Pólya). The drunkard finds his way back;
  the diffusing bird does not. Transport in low dimensions is *recurrent*: boundaries, boundaries layers
  and pollution matter qualitatively differently in a thin film, a 2-D membrane or a 3-D bulk.
* **Green functions change their shape**: the steady Laplacian's response to a point source is
  $G\sim r^{2-d}$, i.e. linear in 2-D (logarithmic, actually $\sim\ln r$) and $1/r$ in 3-D — which is why
  potential theory, electrostatics and groundwater drawdown look so different in different dimensions.
* **Critical dimensions exist.** Nonlinear PDEs have dimensions where the nonlinearity stops being
  relevant: the semilinear heat equation with $u^p$ has $p_c=1+2/d$; the focusing nonlinear Schrödinger
  equation has a mass-critical dimension; Keller–Segel blow-up depends on $d$; KPZ has an upper critical
  dimension 4. Above the critical dimension, mean-field/linear behaviour wins.

## L2 · The formulas that carry $d$

| Object | General dimension $d$ |
|---|---|
| heat kernel | $G=(4\pi Dt)^{-d/2}\exp(-|\mathbf{x}|^2/4Dt)$ |
| mean squared displacement | $\langle r^2\rangle=2dDt$ |
| steady Laplacian Green function | $G\propto r^{2-d}$ ($d\neq2$), $\ \propto\ln r$ ($d=2$) |
| longest relaxation time (domain $L$) | $\tau\sim L^2/(\pi^2 D)$ (independent of $d$) |
| turbulent cascade scale separation | $L/\eta\sim\mathrm{Re}^{3/4}$ (independent of $d$, but intermittency is not) |
| Péclet/Rayleigh/Damköhler | definitions unchanged, but the *operator's* behaviour changes with $d$ |
| finite-difference stability | advective $\Delta t\le\Delta x/(|u|\sqrt d)$, diffusive $\Delta t\le\Delta x^2/(2dD)$ |
| Green–Kubo $D$ (3-D) | $\frac13\int\langle\mathbf{v}\cdot\mathbf{v}\rangle\mathrm{d}t$ (the $\frac13$ is $1/d$) |

**Anisotropic scaling.** When time and space scale differently, write $t\sim x^z$ and call $z$ the
*dynamic exponent*: diffusion $z=2$, waves $z=1$, ballistic motion $z=1$, anomalous
$\langle x^2\rangle\sim t^\alpha$ gives $z=2/\alpha$, and higher-order operators give $z=m$
([higher order](11-higher-order-and-dispersive.md)). Systems with two competing scales can show
Lifshitz-type behaviour with *two* dynamic exponents; this is the language in which growth models,
turbulence and glasses are compared.

**Geometry.** On a curved surface or manifold, $\nabla\to\nabla_g$, $\nabla^2\to\Delta_g$ (the
Laplace–Beltrami operator), and the heat kernel knows the curvature:

$$G(t,\mathbf{x},\mathbf{y})\sim(4\pi t)^{-d/2}e^{-d_g^2/4t}\big(1+\tfrac16\mathrm{Ric}\,t+\cdots\big),$$

where $d_g$ is the geodesic distance and the correction involves the Ricci curvature. Consequences:
diffusion on a sphere is *not* diffusion in a box (no boundary, but two poles, and spherical harmonics
replace Fourier modes); coasts, ridges and curvature concentrate or dilute transport; on a sphere the
Laplacian's spectrum is $\ell(\ell+1)/R^2$, which sets climate modes and Rossby-wave scales.

| Setting | Geometry | What replaces Fourier |
|---|---|---|
| flat $d$-D box | Euclidean | sines/cosines |
| sphere / ocean / atmosphere | $\mathbb{S}^2$ | spherical harmonics |
| membrane, interface | surface with curvature | Laplace–Beltrami eigenfunctions |
| curved spacetime (relativity) | Lorentzian manifold | mode decomposition in a foliation |
| porous fractal medium | fractal, no smooth metric | spectral dimension |
| network | graph | graph Laplacian eigenmodes |

**Fractals and spectral dimension.** On a fractal, the *walk dimension* replaces the Euclidean one:
$P(t)\sim t^{-d_s/2}$ defines the **spectral dimension** $d_s$ (Sierpiński gasket $d_s\approx1.365$),
and transport is generically anomalous ($\alpha=d_s/d_w<1$). This is how a long-tailed
[CTRW](../03-microscopic/08-anomalous-diffusion.md) becomes geometry rather than randomness. Graphs work
the same way: the return probability of a random walk measures an effective dimension, and small-world
networks have $d_s\sim\infty$ in the short-time sense (fast mixing, slow saturation).

## L3 · What the mathematics guarantees

* **Recurrence and transience.** In $d\le2$ a random walker returns to its neighbourhood infinitely
  often; in $d\ge3$ it may never come back. Practical consequence: in 2-D, local release is felt
  *everywhere eventually* (logarithmic potential), while in 3-D it can be diluted away forever. The
  critical mass in [Keller–Segel](../04-interaction/06-chemotaxis-and-keller-segel.md), $8\pi/\chi$, is
  literally the coefficient of the 2-D log potential — a blow-up threshold written by the dimension.
* **Critical dimensions.** Semilinear diffusion $u_t=\Delta u+u^p$ has critical exponent $p_c=1+2/d$;
  NLS has mass- and energy-critical dimensions; KPZ has upper critical dimension 4; the Ising/$\phi^4$
  story has $d_c=4$. Above $d_c$ the nonlinearity is *irrelevant* in the renormalisation-group sense and
  mean-field behaviour returns — the cleanest way to see that "dimension" is a mathematical variable,
  not a physical accident.
* **Dimension enters the exponents explicitly.** The porous-medium Barenblatt profile has
  $\alpha=d/(d(m-1)+2)$; the diffusion-limited aggregation and coarsening exponents differ above and
  below their critical dimensions; biological scaling laws (metabolic rate $\propto M^{3/4}$, Kleiber)
  come from network *dimensions*, not from physics constants.
* **The heat kernel *is* the geometry.** The short-time expansion of $\int G$ recovers the area, the
  total curvature and (in 2-D) the Euler characteristic of a surface, and the long-time decay rate is the
  spectral gap, which is bounded by the Cheeger isoperimetric constant: **transport sees shape** — mixing
  time is geometry, and bottlenecks are curvature and topology.
* **Curvature focuses and defocuses.** Positive curvature concentrates heat (shorter return times);
  negative curvature spreads it (exponential volume growth → very slow return). This is the transport
  picture behind chaotic billiards, Anosov flows and the ergodicity of geodesic motion.

## L4 · Numerics

* **Spheres and manifolds need their own grids.** Cubed-sphere or icosahedral grids avoid the polar
  singularity; spherical harmonics are spectrally exact but awkward with sharp features; geodesic
  finite elements (cotangent Laplacian on triangulations) discretise $\Delta_g$ directly on real
  geometry.
* **Never forget the metric factors.** In curvilinear coordinates the divergence, gradient and volume
  element carry the Jacobian ($r$, $r^2\sin\theta$); discretising the operators without the metric
  produces a *spurious source* that violates conservation — the most common bug in spherical transport
  codes.
* **Dimension changes the stability constants** ($\Delta t\le\Delta x^2/(2dD)$, $\Delta t\le\Delta
  x/(|u|\sqrt d)$) and therefore the practicality of explicit schemes: what works in 1-D is hopeless in
  3-D.
* **Geodesic distance is a Hamilton–Jacobi problem**: use fast marching on meshes, not graph distances,
  when curvature matters ([Hamilton–Jacobi](../06-beyond/02-hamilton-jacobi-and-viscosity-solutions.md)).
* **Benchmarks**: heat-kernel decay versus the exact spectrum on spheres and tori; mixing time on graphs
  versus the spectral gap; the $d$-dimensional Barenblatt profile; return probabilities on fractals
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).

## Checks

1. Why does a drunkard get home in 2-D but a diffusing particle can be lost in 3-D? *(Recurrence holds
   only for $d\le2$: the Green function's decay still gives infinite expected visits.)*
2. Where does the famous $8\pi$ in the Keller–Segel blow-up threshold come from? *(The two-dimensional
   logarithmic Green function.)*
3. What does the spectral gap tell you about a shape? *(The slowest mixing mode — bounded above by the
   Cheeger constant, so bottlenecks and thin necks set the mixing time.)*

## See also

[The spectral view](06-spectral-and-green-function-view.md) ·
[General classification](10-general-pde-classification.md) ·
[Anomalous diffusion](../03-microscopic/08-anomalous-diffusion.md) ·
[Geoscience & climate](../08-bridges/04-geoscience-and-climate.md) ·
[MHD & relativistic transport](../06-beyond/13-mhd-and-relativistic-transport.md)

