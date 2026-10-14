---
title: History, etymology & open problems
blurb: Who discovered what, where the words came from, and what is still unsolved.
depth: 2
tags: [history, etymology, open problems, timeline]
---

# History, etymology & open problems

> Knowing the *sequence* makes ideas memorable, the *etymology* makes them intuitive, and the *open
> problems* keep you honest about what is settled.

## A transport timeline

| Year | Person | Contribution |
|---|---|---|
| 1822 | Fourier | *Théorie analytique de la chaleur*: Fourier series + the heat equation |
| 1827 | Brown | pollen jitter, unexplained for 78 years |
| 1828/1845 | Navier / Stokes | momentum transport with viscous stress |
| 1855 | Fick | diffusion equation, by analogy with Fourier |
| 1856 | Darcy | linear flow law for water through sand |
| 1857 | Clausius | mean free path: kinetic theory begins |
| 1872 | Boltzmann | kinetic equation and the H-theorem |
| 1904 | Prandtl | boundary-layer theory |
| 1905 | Einstein / Smoluchowski | Brownian motion; Stokes–Einstein relation |
| 1931 | Onsager | reciprocal relations for coupled transport |
| 1934 | Zeldovich, Frank-Kamenetskii, Semenov | combustion fronts, thermal explosion |
| 1937 | Fisher; KPP | reaction–diffusion fronts and their speed |
| 1941 | Kolmogorov | turbulence cascade and the $-5/3$ spectrum |
| 1948 | Cattaneo, Vernotte | finite-speed heat conduction |
| 1951/1957 | Green / Kubo | transport coefficients from equilibrium correlations |
| 1952 | Turing | diffusion-driven pattern formation |
| 1953–56 | Taylor, Aris | shear dispersion in tubes |
| 1955–56 | Lighthill, Whitham, Richards | traffic flow as a conservation law |
| 1958 | Cahn–Hilliard | spinodal decomposition |
| 1960/1965 | Mori / Zwanzig | memory kernels and projection operators |
| 1967 | Strang | second-order operator splitting |
| 1970 | Keller–Segel | chemotaxis |
| 1974/1998 | Benamou–Brenier / JKO | optimal transport and gradient flows |
| 1986–88 | Harten–Osher–Engquist / Shu–Osher | ENO and WENO schemes |
| 1990s | (many) | lattice-Boltzmann, DSMC and kinetic solvers mainstream |
| 2019+ | machine learning | neural operators, PINNs, learned closures |

## Etymology: the words carry the pictures

| Word | Origin | Literal image |
|---|---|---|
| advection | *advehere* "carry to" | a cart carrying goods |
| convection | *convehere* "carry together" | a crowd moving as one body |
| diffusion | *diffundere* "pour apart" | wine spreading on a table |
| conduction | *conducere* "lead together" | a bucket brigade of energy |
| dispersion | *dispergere* "scatter" | seed thrown by a sower |
| dissipation | *dissipare* "squander" | money scattered to the winds |
| radiation | *radius* "spoke, ray" | rays leaving a source |
| efflux / influx | *fluere* "flow" | flowing out / flowing in |
| adsorption | *ad-* + *sorbere* "suck to" | a sponge grabbing molecules |
| absorption | *ab-* + *sorbere* "suck away" | swallowed into the bulk |
| accretion | *accrescere* "grow to" | a snowball rolling downhill |
| subsidence | *subsidere* "sit below" | the ground taking a seat |
| viscoelastic | *viscus* "mistletoe glue" | a material that remembers |

The Latin prefixes do the physical work — *ad-* to, *con-* together, *dis-* apart, *sub-* below,
*ab-* away — which is why four roots (*vehere*, *fundere*, *sorbere*, *fluere*) generate the entire
vocabulary.

## Open problems (a working list)

1. **3-D Navier–Stokes regularity** (Millennium Prize): does smooth data stay smooth forever?
2. **Turbulence closures with guarantees**: accurate *and* provably realisable and conservative.
3. **Anomalous transport as a predictive theory**: parameters from medium statistics, not fits.
4. **High-Weissenberg viscoelastic simulation**: separating physical from numerical instability.
5. **Reactive turbulent transport at scale**: combustion and subsurface reactive mixing remain hard.
6. **Long-time statistics of gradient flows**: coarsening, metastability and ageing need new methods.
7. **Structure-preserving learned models**: closures that respect entropy, positivity and conservation.
8. **UQ for multiphysics**: coupling error and model-form error propagating through long integrations.
9. **Nonlocal-to-local limits**: asymptotically compatible discretisations for general kernels.
10. **Rare events and extremes**: escape, nucleation, fracture and failure beyond heuristics.

## See also

[Measurement & experiments](05-measurement-and-experiments.md) ·
[Key derivations](04-key-derivations.md) ·
[One mathematics of transport](../08-bridges/11-unifying-mathematics-of-transport.md) ·
[The Atlas](../00-atlas/index.md)
