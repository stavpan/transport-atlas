---
title: Scaling and self-similarity
blurb: When shape stops depending on size — dimensional analysis, power laws, self-similar solutions, fractals, and the collapse test that separates real scaling from a straight line on a log plot.
depth: 4
tags: [mechanisms, scaling, self-similarity, power law, fractals, collapse, dimensional analysis]
---

# Scaling and self-similarity

> **One-line picture.** A self-similar process looks the same at every magnification, so its *shape* is
> independent of its *size*. That single property is what makes a blast wave, a spreading drop, a
> coastline, an avalanche distribution and a turbulent cascade describable with **one exponent instead of
> a function** — and it is what makes dimensional analysis so unreasonably effective.
>
> **Prerequisites.** [Dimensionless numbers](../01-foundations/05-dimensionless-numbers.md),
> [Phase transitions & criticality](06-phase-transitions-and-criticality.md) ·
> **Leads to.** [Duality & transforms](08-duality-and-transforms.md),
> [the river as a model](../13-panta-rhei/06-the-river-as-a-model.md)

## L1 · The everyday version

Photograph a bomb blast at $1$ ms and at $10$ ms: apart from scale, the pictures are the same. Look at a
map of a coastline, then zoom in on a bay: same kind of raggedness. Shake a flour-and-water mixture and
the marbling repeats at every size you look. This "same picture, different ruler" property is
**self-similarity**, and it converts a hard function-of-many-variables problem into a one-exponent
problem.

Why it matters in transport: much of what we solve has *no characteristic scale* at some stage of its
life — the blast is past its initial radius but not yet reached its boundary; the avalanche is bigger
than a grain but smaller than the box; turbulence is between the outer and the viscous scales. In that
window, only ratios matter, and ratios of powers are powers.

## L2 · How to find the shape: $\pi$-groups, power laws, similarity

* **Buckingham $\pi$.** Reduce $n$ variables and $m$ dimensions to $n-m$ dimensionless groups. Those
  groups are the *only* arguments the answer can depend on, so the answer as a function of them is a
  theorem with unknown content. With fewer than three groups, you can often guess the function.
* **Scaling ansatz.** Assume the solution depends on $x$ and $t$ only through a combined variable
  $\xi=x/t^{\alpha}$. Substituting into the PDE turns it into an *ordinary* differential equation for
  the profile — the same trick that makes the diffusion kernel, the boundary-layer profile, the Blasius
  solution and the Taylor–Sedov blast all "one-line" results.
* **Power laws.** If a distribution has no scale, the only scale-free density is $P(s)\sim s^{-\tau}$
  (and then the moment exponents obey the scaling relations of note
  [6](06-phase-transitions-and-criticality.md)). The signature is a straight line on log–log axes, with
  a *cutoff* wherever the finite size of the system intervenes.
* **Fractals.** Self-similar sets have non-integer dimension, defined by how the number of boxes scales,
  $N(\epsilon)\sim\epsilon^{-d_f}$ — the geometric cousin of a scaling exponent.

## L3 · Intermediate asymptotics, and the collapse test

Barenblatt's framing is the cleanest one available: a self-similar solution is an **intermediate
asymptotic** — the state of a system after it has forgotten its initial conditions but before it has
felt its boundaries. Two kinds exist: *first kind*, where the exponents follow from dimensional analysis
alone (the diffusion kernel; Taylor–Sedov), and *second kind*, where the exponent is fixed by an
eigenvalue condition of the similarity ODE and cannot be obtained by $\pi$-groups (some fingering,
coalescence and wetting problems).

The operational test is the **data collapse**: suppose observables from systems of different size $L$
obey $P(s,L)=L^{-\theta}f\big(s/L^{D}\big)$. Plot $L^{\theta}P$ against $s/L^{D}$ for every $L$: if the
curves fall on one master curve, you have scaling with exponents $(D,\theta)$, valid across the whole
family — a far stronger claim than one fitted line.

![**Figure R9.** The collapse test. Left: distributions from four different system sizes, each with its own
cutoff. Right: the same data after dividing sizes by $L^{D}$ and rescaling the density — one curve. This is
what "universality" looks like as a figure, and it is the check to run before believing any power-law
exponent.](../../figures/scaling-collapse.svg)

![**Animation A7.** Coarsening, with the structure factor beside it: domains merge, and the
peak of $S(k)$ walks steadily to smaller $k$ while the curve keeps its shape — self-similarity
in time, which is the same collapse as in the figure above.](../../figures/anim-coarsening.webp)

## L4 · Doing scaling work that survives scrutiny

1. **Choose scales from physics, not from the data.** Fix $D$ and $\theta$ by an argument (or by theory),
   then collapse; fitting both expanders and exponents to a single dataset is circular.
2. **Report the residuals of the collapse**, not just the picture. A collapse that requires different
   scalings in different decades is not a collapse.
3. **Suspect the alternatives.** Log-normal, stretched-exponential and *mixtures* of simple distributions
   all look straight over two decades. Report at least one competing functional form and compare by
   likelihood or by the collapse quality — this is the standing criticism of the power-law literature.
4. **Watch the cutoff.** Physical cutoffs (box size, correlation length, measurement resolution) are
   often the most informative part of the data: their scaling with $L$ *is* the exponent $D$.
5. **Beware selection effects.** "Scaling" in city sizes, wealth, firm sizes and citation counts is often
   produced by the definition of the unit (how you count) rather than by the dynamics — a caveat that
   applies to transport-adjacent economics as much as to physics.