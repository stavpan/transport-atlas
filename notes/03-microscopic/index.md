---
title: Microscopic transport
blurb: The molecular layer — Fick, Brownian motion, Fourier conduction, kinetic-theory coefficients, rarefaction, cross-effects, ions and anomalous transport.
depth: 2
tags: [index, microscopic transport]
---

# Microscopic transport

This category explains **where the coefficients come from**. Everything here answers one of two
questions: *what is the microscopic mechanism?* and *when does the macroscopic law stop being valid?*

| # | Note | The one thing it gives you |
|---|---|---|
| 1 | [Diffusion (Fick)](01-diffusion.md) | the archetype: Green function, $\sqrt{Dt}$, maximum principle, in one place |
| 2 | [Brownian motion & Einstein relations](02-brownian-motion-and-einstein-relations.md) | the 1905 argument and the relations every simulation uses |
| 3 | [Conduction (Fourier)](03-conduction.md) | heat by contact, phonons and electrons, contact resistance |
| 4 | [Diffusion coefficients](04-diffusion-coefficients.md) | three routes to $D$, and where each route fails |
| 5 | [Knudsen & rarefied transport](05-knudsen-and-rarefied-transport.md) | the continuum's expiry date: slip, jump, ballistic transport |
| 6 | [Cross-effects & multicomponent diffusion](06-cross-effects-and-multicomponent.md) | Soret, Dufour, Maxwell–Stefan: coupling as a rule, not an exception |
| 7 | [Charged & electrochemical transport](07-charged-and-electrochemical-transport.md) | Nernst–Planck, PNP, Debye layers, drift–diffusion |
| 8 | [Anomalous diffusion](08-anomalous-diffusion.md) | when $\langle x^2\rangle$ is not linear: CTRW, Lévy, non-ergodicity |

![**Figure B.** One random walk seen three ways — Green function, trajectories and mean squared displacement. Almost every note in this category is a variation on these three pictures.](../../figures/diffusion-suite.svg)

## The through-line

Molecular transport is **slow and patient**: $t\sim L^2/D$. That single scaling explains the sizes that
biology adopts, why groundwater plumes take decades to move, and why engineering almost always replaces
molecular transport with advection or convection. Read [diffusion](01-diffusion.md) first, then follow the
question you actually have: *where does $D$ come from?* ([coefficients](04-diffusion-coefficients.md)) ·
*when does the law fail?* ([Knudsen](05-knudsen-and-rarefied-transport.md)) ·
*what if there is another gradient?* ([cross-effects](06-cross-effects-and-multicomponent.md)) ·
*what if the walk is not simple?* ([anomalous](08-anomalous-diffusion.md)).
