---
title: Bridges to other fields
blurb: The same equations in other costumes — engineering, geology, biology, finance, plasmas, images, networks, quantum matter, machine learning.
depth: 2
tags: [index, bridges, applications]
---

# Bridges to other fields

This is why the atlas exists: transport theory is not one field's tool, it is a common language. Each note
here follows the same recipe — *name the conserved quantity and the flux law, then say what the field
calls them and what goes wrong there*.

| # | Note | Where it lands |
|---|---|---|
| 1 | [Heat–mass–momentum analogy & circuit models](01-analogy-and-circuit-models.md) | engineering practice; resistance networks; Chilton–Colburn |
| 2 | [Finance & economics](02-finance-and-economics.md) | Black–Scholes as backward diffusion; mean-field games |
| 3 | [Biology & medicine](03-biology-and-medicine.md) | oxygen limits, morphogens, tumours, drug delivery, nerves |
| 4 | [Geoscience & climate](04-geoscience-and-climate.md) | mantle convection, aquifers, sea ice, radiative–convective balance |
| 5 | [Plasma & astrophysics](05-plasma-and-astrophysics.md) | kinetic and MHD transport; accretion; cosmic rays |
| 6 | [Engineering devices](06-engineering-devices.md) | batteries, reactors, heat exchangers, chips, additive manufacturing |
| 7 | [Machine learning & data](07-machine-learning-and-data.md) | diffusion models, graph diffusion, optimal transport in ML |
| 8 | [Images & signals](08-images-and-signals.md) | blurring as heat flow, anisotropic diffusion, level-set segmentation |
| 9 | [Networks, society & traffic](09-networks-society-and-traffic.md) | traffic jams, epidemics, opinion spread, PageRank |
| 10 | [Quantum & condensed matter](10-quantum-and-condensed-matter.md) | ballistic phonons, hydrodynamic electrons, second sound |
| 11 | [One mathematics of transport](11-unifying-mathematics-of-transport.md) | the closing argument: it is all one subject |

![**Figure G.** The concept map of the whole atlas. Follow the colours to see which level a topic first
becomes useful, and follow the arrows to see which ideas are prerequisites for which.](../../figures/concept-map.svg)

## What transfers, and what does not

**Transfers beautifully:**
* The balance law and the divergence theorem — universal.
* Dimensionless analysis and similarity solutions — universal.
* The structure of the equations (elliptic/parabolic/hyperbolic, local/nonlocal) — universal.
* Numerical methods, stability theory and inversion — universal.
* Entropy/energy arguments — universal *provided* you identify the right functional and metric.

**Does not transfer automatically:**
* Constitutive laws (a "diffusion coefficient" in finance is not measured by a diaphragm cell).
* Boundary conditions (a Dirichlet condition is a modelling claim about a real interface).
* Conservation (in social and financial systems, quantities are only conserved by construction).
* Values of parameters: the dimensionless numbers may be astronomically different.

> **A useful test before using an analogy:** can you write down what is conserved, what drives it, and
> what the boundary does — in the new field's own terms? If not, the analogy is decorative.
