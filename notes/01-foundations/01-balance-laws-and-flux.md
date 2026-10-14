---
title: Balance laws & flux
blurb: Why every transport equation is a divergence plus a source, why the conservative form is non-negotiable, and where jump conditions come from.
depth: 1
tags: [conservation, flux, divergence theorem, weak solutions]
---

# Balance laws & flux

> **One-line picture.** Draw any closed surface in the world. Whatever changes inside it must
> be accounted for by what crosses the surface and by what is created or destroyed within it.
>
> **Prerequisites.** None. This is the first note. · **Leads to.**
> [material derivative](02-material-derivative.md), [constitutive relations](03-constitutive-relations.md).

![**Figure 3.** The bookkeeping. A flux $\mathbf{J}$ crossing the boundary $\partial V$ of a control volume $V$, together with volumetric sources and sinks $f$. The integral statement and its local form say exactly the same thing whenever the fields are smooth.](../../figures/balance-control-volume.svg)

## L1 · What it is, in words

Imagine a bathtub with a tap and a drain. The amount of water in the tub changes because of
two things only: what comes in and out through the pipes, and what appears or disappears
inside (a leak, say). Nothing else is possible. If you could suddenly have more water than
the pipes deliver, you would have found a new law of physics.

That is the whole idea. Pick *any* quantity — heat, salt, momentum, electric charge,
probability, cars on a road, money in accounts — and the same sentence applies: **the rate of
change inside a region equals the net flow across its boundary plus the net production
inside**. That sentence, written with calculus, is called a *balance law* or *conservation
equation*, and every equation in this atlas is a special case of it.

## L2 · Why the term looks the way it does

Let $c(\mathbf{x},t)$ be the density of "stuff" per unit volume, and $\mathbf{J}$ the flux
vector: the amount crossing unit area per unit time, in a specified direction. For an
arbitrary region $V$ with outward normal $\mathbf{n}$,

$$\frac{\mathrm{d}}{\mathrm{d}t}\int_V c\,\mathrm{d}V
= -\oint_{\partial V}\mathbf{J}\cdot\mathbf{n}\,\mathrm{d}A+\int_V f\,\mathrm{d}V .$$

* The minus sign is a convention with content: $\mathbf{n}$ points *out*, so
  $\mathbf{J}\cdot\mathbf{n}>0$ means leaking, not gaining.
* $f$ collects everything that is not transport: chemical production, radioactive decay,
  gravity, pressure work, buoyancy — anything that changes the amount without moving it
  across the boundary.

Now apply the divergence theorem $\oint_{\partial V}\mathbf{J}\cdot\mathbf{n}\,\mathrm{d}A
=\int_V \nabla\cdot\mathbf{J}\,\mathrm{d}V$. Since $V$ was arbitrary, the integrands must match
pointwise:

$$\boxed{\;\partial_t c+\nabla\cdot\mathbf{J}=f\;}$$

This is the *differential* (local) form. Everything else is a choice of $c$, a choice of
$\mathbf{J}$, and a choice of $f$:

| Quantity $c$ | Flux $\mathbf{J}$ | Source $f$ | Constitutive law |
|---|---|---|---|
| mass concentration | $\mathbf{u}c-D\nabla c$ | reactions | Fick |
| energy (heat) | $\mathbf{u}(\rho c_p T)-k\nabla T$ | $\dot q$, viscous $\Phi$, radiation | Fourier |
| momentum | $\rho\mathbf{u}\mathbf{u}-\boldsymbol{\tau}$ | $-\nabla p+\rho\mathbf{g}$ | Newtonian (Newton) |
| electric charge | $\mathbf{J}_{\rm cond}+\rho_e\mathbf{u}$ | — | Ohm |
| probability density | drift $\times\rho$ | — | Fokker–Planck |
| cars per metre | $f(c)=c(1-c)$ | on/off ramps | LWR traffic model |

Notice that the *structure* is identical while the physics differs entirely. That is the
reason this atlas can put batteries, black holes and traffic jams in the same document.

> **Deeper (L3).** Note that the derivation assumed $c$ and $\mathbf{J}$ are differentiable.
> When they are not — at a shock, a phase boundary, a fracture — the *integral* form survives
> and gives a **jump condition** instead (see below). Physicists and engineers therefore
> prefer to start from the integral statement, because it is the one that keeps holding when
> the mathematics of the local form has already broken down.
