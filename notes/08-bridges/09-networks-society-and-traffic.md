---
title: Transport in networks, society & traffic
blurb: Equations on graphs and roads — traffic as a conservation law, diffusion as a social process, and epidemics as reactive transport.
depth: 3
tags: [traffic, LWR, networks, graph diffusion, epidemics, PageRank]
---

# Transport in networks, society & traffic

> **One-line picture.** Put the transport equation on a graph and you get traffic jams, opinion spread,
> epidemics, queues and web ranking — the same conservation law with a new geometry.
>
> **Prerequisites.** [conservation laws & shocks](../06-beyond/01-conservation-laws-and-shocks.md),
> [diffusion](../03-microscopic/01-diffusion.md)

## L1 · Four transport problems with non-physical "stuff"

| System | Conserved quantity | Flux law | Character |
|---|---|---|---|
| road traffic | cars per metre | $f(\rho)=\rho v(\rho)$, typically concave | shocks: jams propagate *backwards* |
| epidemics | susceptible/infected counts | contact rate × mixing | reaction–diffusion, fronts |
| opinion / innovation | agents holding a view | imitation, switching | diffusion-like, with thresholds |
| queues and packets | jobs | service capacity, routing | conservation + discrete rules |
| PageRank / influence | probability mass | random walk with teleportation | heat kernel on a graph |

**Traffic** is the most beautiful case: the Lighthill–Whitham–Richards (LWR) model is a *scalar
conservation law* $\partial_t\rho+\partial_x f(\rho)=0$ with concave flux. Its shock speed is the chord
slope, which is *negative* when density is high — hence jams travel upstream while cars move downstream.
Adding a bottleneck or a red light produces rarefactions and shocks, and the
Godunov/Riemann machinery of [shock theory](../06-beyond/01-conservation-laws-and-shocks.md) becomes a
traffic simulator. Second-order models (Payne–Whitham) add momentum and can produce phantom jams and
instability — the traffic analogue of an ill-posed fluid model.

## L2 · Graphs as the geometry

On a network, the Laplacian $L=D-A$ replaces $\nabla^2$: heat conduction, random walks, consensus
dynamics and PageRank are all $\dot{\mathbf u}=-L\mathbf u$ plus external terms. Consequences:

* **Spectral gap = mixing time**: the second eigenvalue of the graph Laplacian controls how fast diffusion
  homogenises, exactly as in the continuum
  ([spectral view](../01-foundations/06-spectral-and-green-function-view.md)).
* **Communities are bottlenecks**: small cuts slow diffusion, which is the basis of spectral clustering.
* **Epidemics**: SIR on networks is reaction–diffusion with the contact graph as geometry; the epidemic
  threshold is a spectral radius condition, and spatial spread is a
  [front](../04-interaction/05-fronts-and-travelling-waves.md) in a network metric.
* **Optimal routing/evacuation** is a flow problem with capacity constraints — a
  [variational inequality](../06-beyond/12-variational-inequalities-and-hysteresis.md) (Wardrop
  equilibrium: no driver can improve by switching route).

## L3 · What the mathematics guarantees

* **Shocks in traffic are unavoidable** for concave flux: any deceleration region steepens into a jam; the
  entropy condition selects the jam solution rather than an "expansion jam".
* **Conservation on networks is subtle**: at junctions you must specify a *distribution* rule, and it
  must respect capacity and non-negativity; naive averaging loses cars.
* **Discrete versus continuum**: continuum models are limits of stochastic agent models, and the limit can
  produce different behaviour (finite-size noise drives jams) — a transport analogue of
  [fluctuation effects](../06-beyond/07-stochastic-pdes-and-random-media.md).
* **Ranking is diffusion**: PageRank is the stationary distribution of a random walk with restarts, i.e.
  the equilibrium of a transport process with a source term.

## L4 · Practice

* **Validate traffic models against fundamental-diagram data** ($\rho$ vs flux from loop detectors), not
  against single-vehicle anecdotes: the flux curve *is* the constitutive law.
* **Benchmarks**: Riemann problems for LWR with a bottleneck, ring-road instability thresholds, SIR front
  speeds, and PageRank convergence on standard graphs.
* **Beware of policy conclusions from an unvalidated flux function**: the shape of $f(\rho)$ determines
  whether jams form at all.
* **Frontiers.** Coupled traffic + emissions + routing; heterogeneous behaviour with human factors;
  mean-field games for selfish routing; epidemic control as an optimal-transport problem.

## Checks

1. Why do traffic jams travel backwards? *(Shock speed is negative when the chord slope of $f(\rho)$ on the
   dense side is negative — the wave moves upstream even though cars move downstream.)*
2. What sets the mixing time on a graph? *(The spectral gap of the graph Laplacian.)*

## See also

[Conservation laws & shocks](../06-beyond/01-conservation-laws-and-shocks.md) ·
[Fronts & travelling waves](../04-interaction/05-fronts-and-travelling-waves.md) ·
[Machine learning & data](07-machine-learning-and-data.md) ·
[Variational inequalities & hysteresis](../06-beyond/12-variational-inequalities-and-hysteresis.md)
