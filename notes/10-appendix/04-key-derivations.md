---
title: Key derivations
blurb: The ten derivations worth doing once by hand — each one carried from first principles to the result you will use.
depth: 3
tags: [derivations, reference, Green function, Taylor-Aris, Barenblatt]
---

# Key derivations

Each section states the starting point, the one decisive step, and the result. If you can reproduce these
ten, you can follow every note in the atlas.

## 1 · Fick's law from a random walk
Start from the master equation $p_{n+1}(x)=\frac12p_n(x-a)+\frac12p_n(x+a)$. Taylor expand both sides to
second order: $\partial_tp=\frac{a^2}{2\tau}\partial_x^2p$, so $D=a^2/2\tau$ and
$\langle x^2\rangle=2Dt$. **Decisive step:** the flux is the *difference* of the two hopping fluxes,
$-D\partial_xp$. → [Diffusion](../03-microscopic/01-diffusion.md)

## 2 · The diffusion Green function
Solve $\partial_tc=D\partial_x^2c$, $c(x,0)=M\delta(x)$ by Fourier transform:
$\hat c(k,t)=Me^{-Dk^2t}$, invert to get the Gaussian with variance $2Dt$. **Decisive step:** in Fourier
space diffusion is multiplication by $e^{-Dk^2t}$.
→ [Spectral view](../01-foundations/06-spectral-and-green-function-view.md)

## 3 · The divergence theorem step of every balance law
Volume balance → divergence theorem → integrands equal (arbitrary volume) → local PDE. **Decisive step:**
the domain is arbitrary, so the integrand must vanish pointwise. This is where jump conditions come from
when smoothness fails. → [Balance laws](../01-foundations/01-balance-laws-and-flux.md)

## 4 · Reynolds transport theorem
Differentiate a moving-volume integral, use $\dot{\mathbf x}=\mathbf u$ and the divergence theorem:
$\frac{\mathrm d}{\mathrm dt}\int_Vc\,\mathrm dV=\int_V[\partial_tc+\nabla\cdot(c\mathbf u)]\mathrm dV$.
**Decisive step:** the boundary moves with the material, so a surface term appears.
→ [Material derivative](../01-foundations/02-material-derivative.md)

## 5 · Einstein's 1905 argument
Balance the diffusive flux $-D\nabla c$ against the drift flux $c\,\mu_{\rm mob}\mathbf F$ at equilibrium,
where $c\propto e^{-V/k_BT}$; matching gives $D=\mu_{\rm mob}k_BT$. With Stokes drag
$\mu_{\rm mob}=1/(6\pi\mu a)$, $D=k_BT/(6\pi\mu a)$.
→ [Brownian motion](../03-microscopic/02-brownian-motion-and-einstein-relations.md)

## 6 · Taylor–Aris dispersion
Decompose the velocity as mean + fluctuation, and the concentration into a cross-sectional mean plus a
deviation. Solve the deviation to leading order in the radial diffusion time, then average: the mean
satisfies a 1-D advection–diffusion equation with
$D_{\rm eff}=D+a^2U^2/48D$. **Decisive step:** the *solvability condition* of the cell problem (the mean
of the deviation equation must vanish). Removes the ambiguity and identifies the effective diffusivity.
→ [Shear dispersion](../02-bulk/06-shear-dispersion-taylor-aris.md)

## 7 · Rayleigh–Bénard onset
Linearise the Boussinesq equations about the conduction state, eliminate pressure and velocity to get a
single equation for the temperature perturbation, and impose stress-free or no-slip boundaries. The
smallest eigenvalue over allowed wavenumbers gives $\mathrm{Ra}_c=1708$ with $k_c\approx3.12$ (rigid).
**Decisive step:** the eigenvalue problem is *linear*, so the onset is sharp.
→ [Convection](../02-bulk/02-convection-and-buoyancy.md)

## 8 · Stefan similarity solution
Seek $T=f(\eta)$ with $\eta=x/\sqrt{\alpha t}$ and an interface at $s=2\lambda\sqrt{\alpha t}$. The heat
equation becomes an ODE; the Stefan condition at the interface becomes the transcendental equation for
$\lambda$. **Decisive step:** the similarity ansatz simultaneously satisfies the PDE and the free-boundary
condition only for this scaling. → [Phase change](../04-interaction/09-phase-change-and-stefan.md)

## 9 · Barenblatt–Pattle profile for the porous medium equation
For $\partial_tc=\Delta c^m$ seek a self-similar compactly supported solution
$c=t^{-\alpha}f(r t^{-\beta})$ with $\alpha=d/(d(m-1)+2)$; the ODE for $f$ is solvable and yields the
profile that attracts all compact data. **Decisive step:** mass conservation fixes the exponents, and
degeneracy at $c=0$ produces the moving edge.
→ [Nonlinear diffusion](../06-beyond/06-nonlinear-diffusion-and-porous-medium.md)

## 10 · JKO: heat flow as steepest descent of entropy
Show that $\frac{\mathrm d}{\mathrm dt}\int\rho\ln\rho=-\int\|\nabla\ln\rho\|^2\rho$, and that minimising
$F+\frac{1}{2\tau}W_2^2$ over $\rho$ with $F=\int\rho\ln\rho$ recovers one implicit heat step. **Decisive
step:** expanding $W_2^2$ for small displacements turns the Wasserstein gradient into $\nabla\cdot(\rho\nabla
\delta F/\delta\rho)$. → [Optimal transport](../06-beyond/10-optimal-transport-and-gradient-flows.md)

## Five more derivations (higher order, geometry, stochastic, collective)

These extend the list to the material added in the extended atlas — the general classification, higher orders,
dimensions, collective phenomena and inference.

## 11 · Classification from the principal symbol
Given an operator of order $m$, keep only the highest derivatives, substitute $\partial\to i\mathbf k$ and study
the polynomial $\sigma_L(\mathbf x,\mathbf k)$. **Decisive step:** type is a property of the *symbol*, not of the
equation's lower-order terms — which is why the same classification covers any order, any dimension and any
system. → [general classification](../01-foundations/10-general-pde-classification.md)

## 12 · Parity and sign rules for higher-order operators
For $u_t=a_m\partial_x^mu$, the dispersion relation is $\omega=a_mi^{m+1}k^m$. **Decisive step:** read off the
parity — odd $m$ gives real $\omega$ (dispersion, no growth), even $m$ gives imaginary $\omega$ (dissipation),
and the *sign* of an even-order coefficient decides smoothing versus short-wave blow-up (the Lax–Mizohata
condition). → [higher order & dispersive](../01-foundations/11-higher-order-and-dispersive.md)

## 13 · Green function and first-passage distribution for drift–diffusion
Solve $\partial_tp=-\mu\partial_xp+\frac{\sigma^2}{2}\partial_x^2p$ on $(-\theta,\theta)$ with absorbing
boundaries; the first-passage density follows from the flux at the boundary. **Decisive step:** reaction times
are *boundary fluxes* of a diffusion — the same calculation for chemical reactions (Kramers), decision making
(DDM) and psychophysics. → [cognitive science & mind](../11-universality/03-cognitive-science-and-mind.md)

## 14 · Fisher metric from invariance (statement and use)
Require a Riemannian metric on the space of distributions that is invariant under sufficient statistics; the
unique answer (up to scale) is $g_{ij}=\mathbb E[\partial_i\ln p\,\partial_j\ln p]$. **Decisive step:** the
geometry is *forced*, so natural gradient is not a heuristic but the invariant steepest-descent direction.
→ [information, statistics & inference](../11-universality/07-information-statistics-and-inference.md)

## 15 · Small-noise limit of Fokker–Planck gives Hamilton–Jacobi
Insert $p\sim e^{-S/\varepsilon}$ into $\partial_tp=-\partial_x(bp)+\frac\varepsilon2\partial_x^2p$ and keep the
leading order in $\varepsilon$: you get $\partial_tS+H(\partial_xS)=0$ with $H=b\,p$. **Decisive step:** the
classical action is the rate function of a rare event — which is why WKB, large deviations (Sanov,
Freidlin–Wentzell) and optimal control share formulas.
→ [information, statistics & inference](../11-universality/07-information-statistics-and-inference.md)

## The habits these ten derivations teach

1. **Always find the solvability condition** — it is usually where the physics enters (items 6, 9).
2. **Non-dimensionalise early** — the dimensionless numbers fall out of the algebra, not from memory
   (items 7, 8).
3. **Get the equilibrium right first** — a diffusive flux must be expressible as a drift of a Boltzmann
   factor (item 5), otherwise your constitutive law violates the second law.
4. **Check conservation at every step** — the local form is a derived convenience; the integral statement
   is the physics (item 3).

## See also

[Operator & equation catalogue](03-operator-and-equation-catalog.md) ·
[Measurement & experiments](05-measurement-and-experiments.md) ·
[History, etymology & open problems](06-history-etymology-and-open-problems.md)
