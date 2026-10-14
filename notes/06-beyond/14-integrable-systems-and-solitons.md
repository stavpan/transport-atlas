---
title: Integrable systems & solitons
blurb: Waves that survive collisions — Lax pairs, inverse scattering as a nonlinear Fourier transform, and the transport of spectral data.
depth: 4
tags: [integrable, soliton, KdV, NLS, inverse scattering, Lax pair]
---

# Integrable systems & solitons

> **One-line picture.** Some nonlinear dispersive equations are secretly linear: change variables to
> *scattering data* and the nonlinear flow becomes a rigid translation. The transport is real — it just
> happens in spectral space.
>
> **Prerequisites.** [Higher order & dispersive](../01-foundations/11-higher-order-and-dispersive.md) ·
> **Leads to.** [Variational principles & Noether](15-variational-principles-and-noether.md),
> [Why everything flows](../11-universality/01-why-everything-flows.md)

## L1 · The observation that started it (1834, and again in 1965)

Scott Russell watched a solitary wave travel a canal for miles without changing shape. A century later
Zabusky and Kruskal simulated the Korteweg–de Vries equation, saw two such humps pass *through* each
other and emerge unchanged (apart from a small phase shift), and called them **solitons**. Since then the
same objects have been found in optical fibres, plasmas, Bose–Einstein condensates, lattices, Josephson
junctions and DNA models — and the mathematics behind them turned out to be one of the deepest in the
subject.

The engine is a *balance*: nonlinearity steepens a wave, dispersion spreads it, and the two can hold
each other in equilibrium — a soliton is a nonlinear wave whose steepening exactly cancels its spreading.

## L2 · Integrability: what it means, and how it works

**Lax pair.** A nonlinear equation $u_t=K[u]$ is integrable if it is the compatibility condition of two
*linear* problems, $L\psi=\lambda\psi$ and $\psi_t=A\psi$, i.e.

$$L_t=[A,L].$$

Because the evolution is a similarity transformation, **the spectrum of $L$ is time-independent** — the
eigenvalues are integrals of the motion. For KdV, $L=-\partial_x^2+u$ is a Schrödinger operator, so the
"quantum mechanics of a potential" governs water waves.

**Inverse scattering transform (IST)** — a nonlinear Fourier transform in three steps:

1. **Direct scattering**: send a wave packet through the potential $u(x,0)$, record the *scattering
   data*: reflection coefficient $R(k)$ and bound-state eigenvalues/norming constants.
2. **Evolve**: the scattering data obey *linear, constant-velocity* equations —
   $R(k,t)=R(k,0)e^{8ik^3t}$, eigenvalues fixed. This is **transport in spectral space**, and it is the
   entire nonlinear dynamics in disguise.
3. **Inverse scattering**: reconstruct $u(x,t)$ from the evolved data by solving a linear
   Riemann–Hilbert/Gel'fand–Levitan problem.

| Equation | Physical setting | Soliton content |
|---|---|---|
| KdV $u_t+6uu_x+u_{xxx}=0$ | shallow water, ion-acoustic plasma, lattices | $N$-solitons, elastic collisions with phase shifts |
| NLS $i\psi_t+\psi_{xx}+\|\psi\|^2\psi=0$ | fibre optics, BEC, deep water | bright/dark solitons, breathers, rogue waves |
| sine-Gordon $u_{tt}-u_{xx}+\sin u=0$ | Josephson junctions, crystal dislocations | kinks, antikinks, breathers |
| Toda lattice | nonlinear springs | discrete solitons |
| KP / Davey–Stewartson | 2-D water waves | line solitons, lumps, higher-dimensional structure |

**Why "infinite conservation laws" follows**: the spectrum is fixed, so every functional of the
scattering data is conserved; expanding in $k$ generates an infinite hierarchy (mass, momentum, energy,
and infinitely many more). This is also why integrable equations are so valuable numerically: they come
with an unlimited supply of exact checks.

**Beyond the first example.** The same circle of ideas gives Riemann–Hilbert problems, the
KP/Toda hierarchies, finite-gap (algebro-geometric) solutions on Riemann surfaces, $\tau$-functions, and
the asymptotic theory of universality classes in random matrix theory — the same equations resurface in
the statistics of growth interfaces and of eigenvalue fluctuations.

## L3 · What integrability guarantees

* **Solitons are *stable*, and variationally so.** For NLS, a soliton is the minimiser of the energy at
  fixed mass — orbital stability follows from that convexity, not from luck. This is the same mechanism
  that stabilises vortices, skyrmions and coherent structures generally.
* **Collisions are elastic with computable phase shifts.** Integrable systems exchange momentum but not
  "identity"; generic systems interact inelastically and chaotically. Two solitons emerging unchanged is
  therefore a *diagnostic* of integrability.
* **Soliton resolution**: for generic initial data, the solution decomposes as $t\to\infty$ into a finite
  number of solitons plus a decaying dispersive tail. This is the nonlinear analogue of a spectral
  decomposition or of the central limit theorem — a complete classification of long-time behaviour, and
  it is *proved* for KdV, NLS and many relatives.
* **Chaos is absent.** Integrable flows live on tori, have zero Lyapunov exponents, and have as many
  conserved quantities as degrees of freedom (Liouville). Perturb them and KAM theory keeps most tori —
  but allows exponentially slow *Arnold diffusion* between them: transport in action space, with an
  astronomical but finite rate.
* **Integrability is fragile but not isolated.** A generic perturbation destroys it, yet the nearby
  structure (tori, slow diffusion, coherent structures) persists — which is why solitons are observed in
  real water, real fibres and real plasmas rather than only in exactly solvable models.

## L4 · Numerics

* **Dissipation destroys the physics.** A first- or second-order upwind scheme turns a soliton into a
  spreading blob within a few widths. Integrable and dispersive problems demand spectral or high-order
  compact schemes with almost no numerical damping
  ([numerical diffusion & dispersion](../07-numerics/03-numerical-diffusion-and-dispersion-error.md)).
* **Splitting is exact where it can be.** For KdV/NLS, integrate the linear dispersive part exactly in
  Fourier space and the nonlinear part exactly in physical space, composed by Strang splitting: second
  order, cheap, and it preserves the invariants to high accuracy
  ([splitting & coupling](../07-numerics/05-operator-splitting-and-multiphysics-coupling.md)).
* **Conservation is your error metric.** Mass, momentum, energy and (for integrable cases) higher
  invariants are known exactly: monitor them instead of guessing. Soliton *positions* after many
  collisions are the sensitive test.
* **Long-time phase accuracy** matters more than local accuracy: soliton speeds are the physical
  observables, so a scheme with a small phase error will pass short tests and fail long ones.
* **Benchmarks**: the Zabusky–Kruskal recurrence experiment; the two-soliton collision phase shift; NLS
  bright solitons, breathers and Peregrine rogue waves; focusing blow-up at critical mass
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).

## Checks

1. What does $L_t=[A,L]$ buy you? *(Time-independence of the spectrum of $L$ — infinitely many conserved
   quantities, and linear evolution of the scattering data.)*
2. Why is "a soliton emerges unchanged from a collision" a signature of integrability? *(Elastic
   collisions with only phase shifts do not occur in generic nonlinear systems.)*
3. What is soliton resolution? *(The rigorous statement that generic solutions separate into solitons plus
   a decaying tail — a complete long-time classification.)*

## See also

[Higher order & dispersive](../01-foundations/11-higher-order-and-dispersive.md) ·
[Variational principles & Noether](15-variational-principles-and-noether.md) ·
[Conservation laws & shocks](01-conservation-laws-and-shocks.md) ·
[Optimal transport & gradient flows](10-optimal-transport-and-gradient-flows.md)

