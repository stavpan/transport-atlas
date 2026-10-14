---
title: Hamilton–Jacobi & viscosity solutions
blurb: Transport of fronts and travel times — first-order nonlinear PDEs, why classical solutions fail at corners, and how viscosity solutions save the day.
depth: 4
tags: [Hamilton-Jacobi, viscosity solution, eikonal, level set, optimal control]
---

# Hamilton–Jacobi & viscosity solutions

> **One-line picture.** Describe a moving front by its arrival time and you get a first-order
> nonlinear equation whose solutions develop corners. Those corners are physical, and the theory of
> *viscosity solutions* is what makes them legal.
>
> **Prerequisites.** [conservation laws & shocks](01-conservation-laws-and-shocks.md) ·
> **Leads to.** [free boundaries & phase field](09-free-boundaries-level-sets-and-phase-field.md),
> [images & signals](../08-bridges/08-images-and-signals.md)

## L1 · Fronts, arrival times, and the eikonal equation

Track a front moving with speed $F$ along its normal (a flame, a wave, an etching front, a
crystallisation front). Its arrival time $T(\mathbf{x})$ obeys the **eikonal equation**

$$F|\nabla T|=1,\qquad T=0\ \text{on the initial front},$$

a first-order nonlinear PDE. For a seismic wave, $|\nabla T|=1/c(\mathbf{x})$ gives first-arrival
travel times; for a robot, the same equation gives the distance-to-goal function — the reason
Hamilton–Jacobi equations are the language of optimal control and path planning.

Solutions develop discontinuities in the gradient (corners) whenever characteristics cross — behind a
concave corner, or where fronts from different sources collide. Classical differentiability fails, and
so does naive differentiation.

## L2 · The general form, and the viscosity-solution idea

The general first-order equation is $H(\mathbf{x},\nabla u)=0$; evolution versions are
$\partial_tu+H(\mathbf{x},\nabla u)=0$. Two complementary constructions resolve the corners:

* **Vanishing viscosity:** solve $u_t+H(\nabla u)=\varepsilon\nabla^2u$ and let $\varepsilon\to0$. The
  limit is the physically correct (and unique) solution — the same mechanism that selects entropy
  solutions of conservation laws.
* **Lax–Oleinik / Hopf–Lax formulas:** the solution is given by an infimum (shortest path, cheapest
  control) over trajectories — a variational representation, which is why HJ = dynamic programming.

The definition of a **viscosity solution** is beautifully minimal: a continuous $u$ is a viscosity
subsolution if every smooth test function touching it from above satisfies $H(\mathbf{x},\nabla\phi)\le0$,
and the reverse for supersolutions. Corners become testable objects, and the comparison principle
(uniqueness) follows. Caution: "viscosity solution" is a *definition*, not a numerical scheme — adding
a small $\varepsilon$ in a code does not automatically give the right answer unless it is consistent
with the limit.

## L3 · What the mathematics guarantees

* **Existence and uniqueness via comparison.** Under coercivity and convexity in $\nabla u$, viscosity
  solutions exist, are unique, and are *Lipschitz* — the corners are controlled.
* **Crandall–Lions theory** connects HJ equations to monotone (max-plus) semigroups, giving exact
  nonlinear superposition: solutions are obtained by infimal convolution, the nonlinear analogue of the
  Green's function convolution in [the spectral view](../01-foundations/06-spectral-and-green-function-view.md).
* **Level-set connection.** The level sets of a viscosity solution solve a *geometric* equation of
  motion: the interface moves with normal velocity $F$. This is why level-set methods for
  [moving boundaries](09-free-boundaries-level-sets-and-phase-field.md) work at all, including
  topological changes.
* **Optimal control duality.** The same object is the value function of a deterministic control problem
  (via Pontryagin/HJB), which is why the equation appears in robotics, economics and
  [mean-field games](../08-bridges/02-finance-and-economics.md).

## L4 · Numerics

* **Monotone schemes are mandatory.** Godunov-type or upwind discretisations of HJ equations converge to
  the viscosity solution; higher-order accurate non-monotone schemes converge to something else. This
  is the direct analogue of Godunov's theorem for conservation laws.
* **Fast marching (first-order, Dijkstra-like) and fast sweeping** solve the eikonal equation in
  $O(N\log N)$; they are the workhorses of seismology, computer graphics and medical imaging.
* **Level-set methods** discretise the geometry in higher dimension and handle merging/splitting
  fronts that are hopeless in arrival-time form (where a single $T$ cannot represent two fronts).
* **Benchmarks**: the eikonal on analytic media (constant and linear velocity), the Zeldovich–Frank-
  Kamenetskii flame front, and shape-from-shading in image processing
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** HJ on graphs and networks ([networks & traffic](../08-bridges/09-networks-society-and-traffic.md));
  mean-field games; second-order HJ from diffusions (Wasserstein gradient flows); machine-learned
  value functions with monotonicity constraints.

## Checks

1. Why do corners appear in arrival-time solutions? *(Characteristics cross where fronts from different
   directions meet; the gradient jumps.)*
2. What selects the correct solution among many? *(Vanishing viscosity, equivalently comparison: the
   viscosity solution.)*
3. Why must discretisations be monotone? *(Non-monotone schemes converge to non-solutions — the HJ
   analogue of Godunov's theorem.)*

## See also

[Conservation laws & shocks](01-conservation-laws-and-shocks.md) ·
[Free boundaries, level sets & phase field](09-free-boundaries-level-sets-and-phase-field.md) ·
[Images & signals](../08-bridges/08-images-and-signals.md) ·
[Networks, society & traffic](../08-bridges/09-networks-society-and-traffic.md)
