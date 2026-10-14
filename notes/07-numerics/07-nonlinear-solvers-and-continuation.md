---
title: Nonlinear solvers & continuation
blurb: Newton and its variants, why nonlinear transport problems fail to converge, and how continuation turns failure into a path.
depth: 3
tags: [Newton, JFNK, line search, continuation, Picard, homotopy]
---

# Nonlinear solvers & continuation

> **One-line picture.** Nonlinear transport problems are solved by repeatedly solving linear ones — and
> the difference between a working code and a failing one is usually the *globalisation*, not the speed.
>
> **Prerequisites.** [linear solvers](06-linear-solvers-and-preconditioning.md) ·
> **Leads to.** [variational inequalities & hysteresis](../06-beyond/12-variational-inequalities-and-hysteresis.md),
> [inverse problems](10-inverse-problems-and-data-assimilation.md)

## L1 · Newton and its family

For $\mathbf F(\mathbf u)=0$, Newton solves $\mathbf J(\mathbf u^k)\,\delta=-\mathbf F(\mathbf u^k)$ and
updates $\mathbf u^{k+1}=\mathbf u^k+\delta$: quadratic convergence near a solution, fragile far from one.

| Variant | Idea | When to use |
|---|---|---|
| Newton | full Jacobian | fast, smooth problems, good initial guess |
| Newton–Krylov (JFNK) | Jacobian-free matrix–vector products | Jacobian impractical to form |
| damped Newton / line search | shrink the step if the residual does not drop | near-singular or strongly nonlinear |
| trust region | bound the step, adapt the model | ill-conditioned, unreliable Jacobians |
| Picard / fixed-point | iterate on the linearised operator | mildly nonlinear, cheap, linear convergence |
| pseudo-transient continuation | add a time term to drive to steady state | steady solves with bad initial guesses |
| Gauss–Newton / Levenberg | nonlinear least squares | inverse problems, data fitting |

## L2 · Continuation: make the problem easy first

Instead of solving the hard problem directly, solve a sequence of easier ones:

$$\mathbf F(\mathbf u,\lambda)=0\quad\text{with }\lambda:0\to1\ \text{in steps}
\qquad(\text{parameter or homotopy continuation}).$$

Applications: ramping the Rayleigh number in convection, ramping reaction rates from zero, ramping
nonlinear diffusion from the linear case, or a "natural continuation" in a pseudo-time variable. If the
solution branch folds (saddle-node bifurcation), pseudospectral arc-length continuation follows the
branch around the fold — essential for ignition/extinction problems
([kinetics](../04-interaction/01-reaction-kinetics-and-sinks.md)).

## L3 · What the mathematics guarantees

* **Local quadratic convergence** for smooth $\mathbf F$ and nonsingular $\mathbf J$; superlinear for
  quasi-Newton. Convergence *radius* is problem-specific and shrinks with nonlinearity.
* **Inexact Newton** retains superlinear convergence if the linear tolerance is tightened with the
  residual norm (Eisenstat–Walker) — the practical basis of JFNK.
* **Continuation exists when the solution manifold does not fold**; at folds, the Jacobian is singular and
  you need arc-length parameterisation. Distinguishing a fold from a *failure to converge* is a key skill.
* **Discrete schemes can break Newton.** Limiters, phase changes and complementarity constraints make
  $\mathbf F$ non-differentiable; use semismooth Newton, active-set strategies, or smooth regularisation.

## L4 · Practicalities

* **Non-dimensionalise and scale unknowns** before assembling residuals: badly scaled variables destroy
  line searches.
* **Always monitor the residual norm, its reduction per iteration and the Jacobian conditioning**.
  Divergence with a decreasing residual usually means a bad linear tolerance; oscillation means a bad
  Jacobian or a genuinely non-differentiable scheme.
* **Warm-start** from the previous time step; for steady problems use pseudo-transient continuation with
  CFL-type ramping (a trick imported from aerodynamics).
* **Benchmarks**: Bratu problem, lid-driven cavity at increasing Reynolds number, and reactive
  steady-state ignition curves ([V&V](12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Automatic differentiation for exact Jacobians; learned preconditioners; robust solvers
  for non-smooth multiphysics.

## Checks

1. Why is JFNK attractive for multiphysics? *(No analytic Jacobian needed: matrix–vector products suffice,
   and preconditioners can be physics-based approximations.)*
2. What does a fold mean for continuation? *(The Jacobian is singular; you must parameterise by
   arc-length to track the branch.)*

## See also

[Linear solvers & preconditioning](06-linear-solvers-and-preconditioning.md) ·
[Variational inequalities & hysteresis](../06-beyond/12-variational-inequalities-and-hysteresis.md) ·
[Inverse problems & data assimilation](10-inverse-problems-and-data-assimilation.md)
