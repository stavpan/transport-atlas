---
title: Equilibria and critical points
blurb: Where a system stops moving — the difference between thermodynamic equilibrium and a living steady state, and how to find the stationary points of an equation that cannot be solved by hand.
depth: 4
tags: [mechanisms, equilibrium, steady state, stationary, variational, Morse theory]
---

# Equilibria and critical points

> **One-line picture.** A system stops when everything that pushes it balances — and *how* it stops
> tells you what kind of system it is. A bathtub stops because nothing is coming in; a river never
> stops but its shape does; a laser stops pulsing but keeps pumping. Same word, three different
> mathematics.
>
> **Prerequisites.** [Balance laws & flux](../01-foundations/01-balance-laws-and-flux.md),
> [Entropy & variational structure](../01-foundations/07-entropy-and-variational-structure.md) ·
> **Leads to.** [Linearisation & stability](02-linearization-and-stability.md),
> [Bifurcation theory](03-bifurcation-theory.md)

## L1 · The everyday version

Put a marble in a bowl. It rattles, then sits still at the bottom. Put it on a dome: it sits, but the
smallest breath sends it away. Both are equilibria — the marble is not moving — but only one is
*stable*, and the difference is the whole subject.

Three things called "equilibrium" must be kept apart, because collapsing them causes real confusion:

1. **Thermodynamic equilibrium** — nothing flows, anywhere. The system is maximally disordered: heat
   conduction stops when $T$ is uniform; diffusion stops when $c$ is uniform.
2. **A steady state / non-equilibrium steady state (NESS)** — the *state variables* stop changing, but
   fluxes continue. A river's depth profile is steady while water rushes past; a heated rod's profile
   is steady while heat flows through it; your body is steady while matter and energy stream through it.
3. **A balance of forces** — a mechanical equilibrium that may be neutral (oars, planets) rather than
   attractive.

The first is *static*, the second *dynamic* and alive, the third *neutrally* free. Most interesting
transport is of the second kind, which is why "equilibrium" is a poor name for it: the state is
stationary, not the substance. *Nothing about the fluid element persists; the pattern does.*

## L2 · What the equations say

Steady means the time derivative vanishes — and, just as importantly, so does the net of whatever else
changes the state.

| Setting | Stationary condition | What it looks like |
|---|---|---|
| ODE $\dot{x}=f(x)$ | $f(x)=0$ | a point; the marble's resting places |
| PDE $\partial_t u=\mathcal L u+\mathcal N(u)$ | $\mathcal L u+\mathcal N(u)=0$ | a *profile*: $\mathrm{d}P/\mathrm{d}x=0$ in flow, $\nabla^2T=0$ in conduction |
| Balance with sources | $\nabla\!\cdot\!\mathbf J=\sigma$ | a NESS with $\mathbf J\neq 0$: flux in, flux out, no accumulation |
| Variational | $F'(u)=0$ | a critical point of an energy or entropy functional |
| Discrete/network | mass-balance residual zero | a flow pattern on a graph (Kirchhoff, resistor networks, PageRank) |

Three consequences carry most of the practical weight:

* **A profile is a balance of two mechanisms.** In advection–diffusion the steady state is where
  transport *by* the flow is exactly undone by spreading: $\mathbf v\!\cdot\!\nabla c=D\nabla^2c$,
  giving exponential boundary layers of thickness $D/v$. In a boundary layer it is inertia against
  viscosity; in a Stefan problem, latent heat against conduction. Name the two competing terms and
  dimensional analysis guesses the profile.
* **Stability is a separate question from existence.** A stationary state exists whenever a balance
  can be struck; whether it is *observable* is decided by note
  [2](02-linearization-and-stability.md).
* **Steady state ≠ minimum energy.** A NESS is generally *not* an energy minimum: it minimises
  something else (entropy production, in the near-equilibrium regimes of Onsager; free energy in a
  moving frame for some flows), or nothing at all.

![**Figure R1.** The same stationary point seen two ways. Left: as a critical point of an energy
landscape $V(x)$ — the marble picture, where stability is curvature. Right: as the zero of the flow
field — where "arrows point in" is stability and "arrows point out" is instability. When a system has a
gradient structure, the two pictures are the same theorem.](../../figures/energy-landscape-stability.svg)

## L3 · Existence, multiplicity, and counting solutions

For a nonlinear problem "find the steady states" is a global question, and the tools are topological.

* **Variational existence.** If a functional is coercive and weakly lower semicontinuous, minimisers
  exist — that is how one proves existence of equilibrium profiles without solving anything. Convexity
  gives *uniqueness*; loss of convexity is where multiplicity begins.
* **Index and degree theory.** The Poincaré–Hopf theorem says the indices of the zeros of a vector
  field on a closed surface sum to its Euler characteristic, so zeros cannot simply vanish: they move,
  merge, or exit through the boundary. This is a *forecast*: it predicts the
  [bifurcations](03-bifurcation-theory.md) that must exist.
* **Morse theory.** The number of critical points of a smooth function is bounded below by the topology
  of the space it lives on. Multiple steady states are, in this sense, topological rather than
  accidental.
* **Spectral bridging.** Stationary states of $\partial_t u=\mathcal L u+\mathcal N(u)=0$ are fixed
  points of $\mathcal L^{-1}\mathcal N$: an equation on the spectrum, which is why the
  [spectral view](../01-foundations/06-spectral-and-green-function-view.md) is the natural language.
* **Detailed balance.** When true equilibrium exists (no net flux), a stationary Markov distribution
  obeys $\pi_i w_{ij}=\pi_j w_{ji}$. Every departure from this — cyclic fluxes — is the signature of a
  NESS, and a precondition for life-like behaviour: a motor, a pump, a cell.

## L4 · Finding them in practice

1. **Newton–Krylov.** For discretised PDEs the Jacobian is sparse; matrix-free Krylov solves of
   $J\delta=-R$ plus continuation in the parameter is the workhorse. Near a bifurcation the Jacobian is
   singular *by design*, and you must switch to
   [arc-length continuation](../07-numerics/07-nonlinear-solvers-and-continuation.md).
2. **Time marching to a steady state.** Cheapest when a stable state is to be reached, useless when
   the state is unstable, and dangerous when the state is *metastable*: the run looks converged for a
   long time and then leaves.
3. **Spurious discretisation equilibria.** A coarse grid, a limiter or a large time step can create
   fixed points the continuum problem does not have, and destroy real ones. Refine one level and check
   that the state moves by less than an error bar.
4. **Diagnose the converged state.** Report residuals *and* fluxes: a residual of $10^{-9}$ around a
   vanishing flux balance can still be physically wrong.

Traps observed in practice: multiple steady states in the same geometry (high-Reynolds-number
lid-driven cavity flows settle into *different* patterns depending on how they were started);
hysteresis of convection onset; grid-dependent locking of a front; and "converged" profiles that are
converged only in a norm nobody printed.
