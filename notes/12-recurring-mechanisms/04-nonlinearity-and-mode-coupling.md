---
title: Nonlinearity and mode coupling
blurb: What happens when superposition fails — harmonics, cascades, shocks, solitons and pattern selection, and why nonlinearity is best understood as a *mixer* between scales.
depth: 4
tags: [mechanisms, nonlinearity, mode coupling, cascade, shocks, solitons, weakly nonlinear]
---

# Nonlinearity and mode coupling

> **One-line picture.** Linear systems add; nonlinear systems **talk**. When two motions interact, they
> create new motions at new scales — and that single fact generates harmonics, turbulence, shocks,
> solitons, patterns and chaos. Nonlinearity is not a difficulty; it is a *mechanism for transfer*.
>
> **Prerequisites.** [Constitutive relations](../01-foundations/03-constitutive-relations.md),
> [Higher order & dispersive](../01-foundations/11-higher-order-and-dispersive.md) ·
> **Leads to.** [Chaos & predictability](05-chaos-and-predictability.md),
> [Scaling & self-similarity](07-scaling-and-self-similarity.md)

## L1 · The everyday version

Play two notes on a violin: you hear two notes, plus a faint extra tone that neither string produced.
Push two storm waves into each other and they do not pass through unchanged — one may break. Ask a
loudspeaker for more volume and it distorts: new frequencies appear. Add a second chemical that
reacts with the first and the smooth pattern that was forming becomes spots.

In linear systems effects add and pass through each other. In nonlinear systems they **interact**, and
the interaction has three everyday signatures:

1. **New components appear** — harmonics (2×, 3×), subharmonics, combination tones.
2. **Everything saturates or dies** — growth is capped, thresholds appear, runaway ends in a new state.
3. **Energy travels between scales** — a smooth, large-scale motion can feed small-scale roughness
   (the [turbulent cascade](../02-bulk/05-turbulence-and-eddy-diffusivity.md)), and a small-scale
   irregularity can organise the large scale (pattern formation).

## L2 · Where nonlinearity comes from, and what it does

| Source | Example | Immediate consequence |
|---|---|---|
| State-dependent transport coefficient | $k(T)$, $\mu(\dot\gamma)$, $D(c)$ | a linear PDE becomes a nonlinear one: [porous-medium flow](../06-beyond/06-nonlinear-diffusion-and-porous-medium.md) |
| Bilinear reaction | $u\,v$, $u\,v^2$ | excitability, [oscillation](../04-interaction/03-autocatalysis-and-oscillations.md), Turing patterns |
| Inertial advection | $\mathbf v\!\cdot\!\nabla\mathbf v$ | steepening → [shocks](../06-beyond/01-conservation-laws-and-shocks.md); turbulence |
| Feedback and saturation | growth $\dot x=rx(1-x/K)$ | finite carrying capacity; Hopf and limit cycles |
| Thresholds and switches | relay, valve, ignition | multi-stability, [hysteresis](../06-beyond/12-variational-inequalities-and-hysteresis.md) |
| Geometric nonlinearity | large deformations, moving boundaries | [free boundaries](../06-beyond/09-free-boundaries-level-sets-and-phase-field.md) behave nonlinearly even for linear physics |

Modes couple when three of them satisfy a **resonance condition**: $k_1\pm k_2=k_3$ *and*
$\omega_1\pm\omega_2=\omega_3$. Everything familiar then follows:

* **Harmonic generation** — one mode feeds its multiples; the spectrum widens.
* **The cascade** — a range of resonances passes energy from large to small scales, producing the
  power-law spectra of turbulence and wave turbulence.
* **Shock formation** — the "fast parts" of a wave catch up the slow parts, so a smooth ramp steepens
  into a jump; only diffusion can round it off, and the whole problem needs a weak-solution framework
  with an entropy condition.
* **Solitons** — when steepening is balanced by *dispersion* instead of dissipation, the hump neither
  breaks nor spreads: a stable, particle-like wave
  ([integrable systems](../06-beyond/14-integrable-systems-and-solitons.md)).
* **Pattern selection** — a band of wavelengths is unstable but only one or a few survive competition;
  which one depends on nonlinear saturation, not on the linear growth rate alone.

![**Figure R4.** Mode coupling made visible. The left panel is a real solution of a two-species
reaction–diffusion system: an initially smooth, seeded field grows into spots and stripes of a
preferred size. The right panel is the reason: only a *band* of wavenumbers grows, and the growth-rate
curve has a maximum. Nonlinearity sets the final amplitude and arbitrates the competition between the
surviving modes.](../../figures/reaction-diffusion-art.svg)

![**Animation A4.** A smooth wave steepening into a shock. Nothing is added and nothing
removed: the fast part of the wave catches up the slow part, and at $t=1$ the solution stops
being differentiable. This is nonlinearity with no escape clause.](../../figures/anim-shock-formation.webp)

## L3 · The weakly nonlinear toolkit

When the failure of superposition is *small*, perturbation theory turns a hard PDE into a small set of
equations for the amplitudes:

1. **Rescale** with the small amplitude $\varepsilon$: $u=\varepsilon u_1+\varepsilon^2u_2+\cdots$.
2. **Solve order by order.** At first order you recover the linear problem; at second order the
   nonlinearity acts as a *source* at exactly the resonance conditions.
3. **Impose solvability** (Fredholm alternative: the source must be orthogonal to the adjoint
   homogeneous mode) and out pop **amplitude equations**:
   * pattern amplitude $A$: $\dot A=\mu A-g|A|^2A$ — the Landau equation; $g>0$ gives a gentle
     (supercritical) onset, $g<0$ a jump (subcritical);
   * three-wave interactions in wave turbulence, and the Zakharov equations for strong wave coupling;
   * the nonlinear Schrödinger and Korteweg–de Vries equations as *universal* envelopes, integrable by
     inverse scattering, with solitons as the elementary excitations.

Two structural facts worth carrying around:

* **Dimension decides whether resonance is generic.** In one dimension three-wave resonance conditions
  are usually impossible except for special dispersion relations — hence the integrable, soliton-rich
  special cases. In two and three dimensions resonances are plentiful, so energy transfer is generic
  and turbulence (not solitons) is the default.
* **Nonlinearity can create the very conditions for its own breakdown.** Shocks form in finite time
  ($t_s=-1/\min_x\partial_x u$ for inviscid Burgers), which is why "the model stopped working" is often a
  *correct* prediction rather than a numerical failure.

## L4 · Computing with nonlinearity

* **Wider spectra.** Each nonlinear interaction doubles the bandwidth. A grid that resolves the initial
  condition may fail after a few eddy turn-over times; resolve the *developed* spectrum, not the input.
* **Aliasing.** Products of unresolved modes fold back as spurious large-scale structure. Use
  de-aliasing (the 2/3 rule for Fourier methods, or over-integration for collocation) unless you want
  numerical pseudo-phenomena.
* **Shocks need limiters or filters**, and the scheme must be *entropy stable*: honouring the discrete
  analogue of the entropy condition is a stronger requirement than linear stability
  ([limiters & WENO](../07-numerics/04-limiters-tvd-and-weno.md)).
* **Distinguish physical from numerical transfer.** Plot spectra, the spectral flux across scales, and
  the resolved-scale budget; refine and check that the *statistics* are grid-independent. Slope
  agreement between two grids with different resolution can both be wrong in the same way — use
  convergence, not resemblance.
* **Test on known nonlinear solutions.** Solitons, self-similar blast waves
  ([scaling](07-scaling-and-self-similarity.md)), and travelling fronts have exact or near-exact
  forms; they catch nonlinear bugs that linear test problems cannot.