---
title: Linearisation and stability
blurb: Does a small nudge grow or die? The Jacobian, the four linear portraits, energy methods, non-normal growth, and how a growth-rate curve selects the pattern you see.
depth: 4
tags: [mechanisms, stability, eigenvalues, linearisation, dispersion relation, non-normal]
---

# Linearisation and stability

> **One-line picture.** Push a system a little and watch: if the push decays, the state is stable and
> you will see it; if it grows, the state is a mathematical ghost. Linearisation is the calculus of
> that one question — and it reaches astonishingly far, because "will the nudge grow?" is also "which
> wavelength will appear?".
>
> **Prerequisites.** [Equilibria & critical points](01-equilibria-and-critical-points.md),
> [Spectral & Green-function view](../01-foundations/06-spectral-and-green-function-view.md) ·
> **Leads to.** [Bifurcation theory](03-bifurcation-theory.md),
> [Phase transitions & criticality](06-phase-transitions-and-criticality.md)

## L1 · The everyday version

A tall stack of coins either stands or it does not; the difference is not the height but whether a
wobble shrinks or amplifies. Everything in this note answers that question in advance:

* **stability** — wobbles die: the state is what you observe;
* **instability** — wobbles grow until something else takes over (the
  [bifurcation](03-bifurcation-theory.md) story, next note);
* **marginal** — wobbles persist: neutral, and the interesting case, because here the system might do
  either.

In an extended system the wobble is not a single number but a *shape*: a ripple with a wavelength. The
question becomes **which wavelengths grow**, which is why one stability calculation predicts stripes on
a fish, rolls in a heated pan, and jets in the atmosphere.

## L2 · The Jacobian, and the four portraits

Perturb $x\to x^{\ast}+\delta$ in $\dot{x}=f(x)$. Truncating the Taylor series gives the *linearisation*
$\dot\delta=J\delta$ with $J=\partial f/\partial x$ at $x^{\ast}$, whose solution is a sum of exponentials
$e^{\lambda_i t}$ over the eigenvalues of $J$:

* $\mathrm{Re}\,\lambda<0$ for all $i$ → stable (the perturbation dies);
* some $\mathrm{Re}\,\lambda>0$ → unstable (it grows);
* $\mathrm{Re}\,\lambda=0$ → marginal, and linear theory cannot decide: nonlinearity does.

![**Figure R2.** All of stability theory, locally, in four pictures. The pair of eigenvalues decides the
portrait: two real negatives (node), a complex pair with negative real part (spiral), a sign change
(saddle — the decisive case for escape), and a purely imaginary pair (centre — where a nudge neither
dies nor grows).](../../figures/linear-stability-zoo.svg)

| Portrait | Eigenvalues | Physical reading |
|---|---|---|
| **Node** | both real, negative | monotone return; relaxation to a steady state |
| **Spiral** | complex, negative real part | damped oscillation; a ringing that fades |
| **Saddle** | real, opposite signs | a watershed; escape over a barrier ([Kramers](09-noise-induced-phenomena.md)) |
| **Centre / marginal** | purely imaginary | a persistent mode — the seed of oscillation and of critical slowing |

For PDEs the same four cases are applied *mode by mode*. Substituting $u=\hat u\,e^{ikx+\lambda t}$
into $\partial_t u=\mathcal L u$ turns an operator into a function of $k$: the **dispersion relation**
$\lambda(k)$. Stability then becomes a picture rather than a number: stable if
$\mathrm{Re}\,\lambda(k)<0$ for every $k$, and the *most unstable* $k$ is the one you will see. Two
canonical shapes keep appearing:

* $\lambda(k)=-Dk^2$ (diffusion): monotonically worse for large $k$ — fine scales are always damped;
* a hump: stable at $k=0$, unstable over a band $k_1<k<k_2$. This is diffusion-driven
  ([Turing](../04-interaction/04-reaction-diffusion-and-turing.md)) instability, and it is how a
  perfectly uniform state decides on a wavelength — see the right-hand panel of
  [the pattern figure](../13-panta-rhei/02-beauty-and-the-flow.md).

## L3 · Beyond eigenvalues: five refinements that matter

1. **Energy (Lyapunov) methods.** Find a functional $E\ge0$ with $\dot E\le0$ and you have proved
   stability *without* linearising, hence beyond the small-perturbation regime. In fluids this is how
   nonlinear stability of shear flows is established; it usually gives a threshold *below* the spectral
   one — conservative, but rigorous.
2. **Non-normality and transient growth.** When the eigenvectors of $J$ are nearly parallel (shear
   flows, reaction networks), perturbations can grow enormously *before* eventually decaying: a
   transient amplification that awakens nonlinearity and bypasses the eigenvalue story entirely. It is
   why a pipe flow is linearly stable yet experimentally turbulent. Diagnose with pseudospectra, not
   eigenvalues alone.
3. **Absolute versus convective instability.** A flow can be stable to a disturbance that grows, but
   only while it is *advected away* — spatially amplifying noise. The distinction decides whether a jet
   radiates or amplifies, and is invisible if you only Fourier-transform in space.
4. **Centre manifolds and amplitude equations.** At marginality, project onto the slow modes: you get a
   small system — the normal form — whose coefficients decide the outcome. This is the bridge from
   linear theory to [bifurcation](03-bifurcation-theory.md) theory.
5. **Conditioning of the answer.** Eigenvalues of a non-normal matrix can be hypersensitive to
   parameters. "The growth rate is 0.01" may be a statement about your matrix, not about the physics.

## L4 · Computing stability without fooling yourself

* **Discretise, then ask.** Assemble the *discretised* Jacobian and compute its rightmost eigenvalues by
  shift-invert [Arnoldi/Krylov](../07-numerics/06-linear-solvers-and-preconditioning.md). Do not compute
  the whole spectrum: you want the edge of the right half-plane, so shift the problem there.
* **Beware spurious modes.** Boundary conditions live *inside* the discretisation; unstable eigenmodes
  that sit on two grid cells or hug the boundary are usually the grid apologising, not the physics.
  Refine and re-check.
* **Delay makes it transcendental** ($\lambda=ae^{-\lambda\tau}$): infinitely many eigenvalues, so the
  stability boundary must come from the characteristic equation or a Krylov approximation of the delay
  operator — see [delay & retarded transport](../06-beyond/16-delay-and-retarded-transport.md).
* **Nonlinear confirmation is mandatory.** An eigenvalue says the state *will* leave; a nonlinear run
  says *where to*. Report both, or you have told half the story.