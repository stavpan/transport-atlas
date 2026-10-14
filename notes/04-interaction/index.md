---
title: Interaction, source & sink
blurb: Everything that creates, destroys or transforms while transport is happening — reactions, sorption, phase change, wells, and dissipation.
depth: 2
tags: [index, source, sink, reactions]
---

# Interaction, source & sink

Everything so far in the atlas *moves* things. This category changes them: reactions transform, surfaces
capture, phases change, wells inject, and dissipation converts motion into heat. Formally, these are the
right-hand-side terms — but physically they are where the interesting behaviour (nonlinearity, patterns,
shocks, thresholds) comes from.

| # | Note | The one thing it gives you |
|---|---|---|
| 1 | [Reaction kinetics & chemical sinks](01-reaction-kinetics-and-sinks.md) | orders, Arrhenius, saturation, scavenging — the source term that makes equations nonlinear |
| 3 | [Autocatalysis & oscillations](03-autocatalysis-and-oscillations.md) | clocks, excitability and what happens when a Lyapunov function disappears |
| 4 | [Reaction–diffusion & Turing](04-reaction-diffusion-and-turing.md) | diffusion creating pattern; wavelength selection |
| 5 | [Fronts & travelling waves](05-fronts-and-travelling-waves.md) | invasion, flames and nerve impulses as one object; speed selection |
| 6 | [Chemotaxis & Keller–Segel](06-chemotaxis-and-keller-segel.md) | directed cell motion, aggregation and blow-up |
| 7 | [Sorption & retardation](07-sorption-and-retardation.md) | why pollutants arrive late: isotherms, retardation, chromatography |
| 8 | [Absorption, dissolution & interfacial transfer](08-absorption-dissolution-and-interfacial-transfer.md) | the mass-transfer coefficient, two-film theory, reaction enhancement |
| 9 | [Phase change & the Stefan problem](09-phase-change-and-stefan.md) | moving boundaries paid for in latent heat |
| 10 | [Sedimentation, deposition & filtration](10-sedimentation-deposition-and-filtration.md) | particles that fall and stick; cake resistance |
| 11 | [Accretion, ablation & surface growth](11-accretion-ablation-and-surface-growth.md) | domains that grow and shrink; residual stress |
| 12 | [Wells, injection, efflux & breakthrough](12-wells-injection-efflux-and-breakthrough.md) | point sources and the measurement that characterises a site |
| 13 | [Subsidence & poroelasticity](13-subsidence-and-poroelasticity.md) | transport that changes the solid — permanently |
| 14 | [Viscous dissipation & heating](14-viscous-dissipation-and-heating.md) | the one-way conversion of motion into heat |

![**Figure C.** The shapes source and sink terms create: an advected and diffusing pulse, with a
breakthrough curve that carries the fingerprint of every interaction the solute experienced.](../../figures/advection-vs-diffusion.svg)

## Three ideas that organise this category

1. **Zero-order terms change amplitude; nonlinear terms change structure.** Exponential decay, logistic
   growth, shock-forming isotherms and Turing patterns all come from the same algebraic term $R(c)$.
2. **Interfaces are where the rate law lives.** Sorption, absorption, phase change, filtration and growth
   are all *boundary* phenomena: get the interface condition wrong and no amount of interior accuracy
   helps.
3. **Feedback makes transport stiff and history-dependent.** Temperature-dependent viscosity, Arrhenius
   kinetics, plasticity and hysteresis all mean the transport coefficients depend on the answer —
   which is where coupled, implicit solvers become unavoidable.
