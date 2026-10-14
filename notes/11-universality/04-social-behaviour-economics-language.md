---
title: Social behaviour, economics & language
blurb: Opinion dynamics, wealth, innovation, segregation, language change and Zipf's law — collective behaviour as transport of distributions.
depth: 3
tags: [social-science, economics, linguistics, opinion, wealth, Zipf]
---

# Social behaviour, economics & language

> **One-line picture.** Societies are made of agents, but the quantities we measure — opinions, wealth,
> adoption rates, word frequencies — are *distributions*, and distributions move. The mathematics is the same:
> drift and diffusion for the shape of a distribution, reaction–diffusion for its spatial spread.
>
> **Prerequisites.** [Fokker–Planck & Kramers](../05-kinetic/03-fokker-planck-and-kramers.md),
> [Fronts & travelling waves](../04-interaction/05-fronts-and-travelling-waves.md) ·
> **Leads to.** [Cognitive science & mind](03-cognitive-science-and-mind.md),
> [Information, statistics & inference](07-information-statistics-and-inference.md)

## L1 · Why the social sciences are transport problems

Two levels exist, and it matters which one you are on:

* **Agent level** — discrete, heterogeneous, strategic, often only finitely many. Nothing here is a PDE until
  you aggregate.
* **Population level** — the distribution of agents over states (opinions, wealth, locations, vocabulary). This
  *is* a density, and it evolves by transport whenever agents move, copy, switch or are created/destroyed.
  Aggregation is a limit theorem (law of large numbers / mean-field), valid when agents are many and weakly
  correlated — the social-science **Knudsen condition**.

The payoff is not decoration: transport theory predicts *distribution shapes* (power laws, lognormal tails),
*spreading speeds* (adoption fronts), and *stability* (consensus, polarisation, cycles) — quantities that
agent-level intuition gets wrong.

## L2 · The canonical models

**Opinion dynamics.** Continuous-opinion models give nonlinear diffusion,
$\partial_t\rho=\partial_x^2\!\big(D(\rho)\rho\big)$, where the diffusivity depends on how far opinions can
influence each other. Bounded confidence produces *compact support* and clustering — the mathematics of
[porous-medium-type degeneracy](../06-beyond/06-nonlinear-diffusion-and-porous-medium.md) with a moving front,
which is why consensus, polarisation and fragmentation are *transport* outcomes rather than voting outcomes.

**Wealth and income.** A multiplicative random growth process, $\dot w=\mu w+\sigma w\,\xi$, has a
Fokker–Planck equation for the wealth density,

$$\partial_t\rho=-\partial_w(\mu w\rho)+\tfrac{\sigma^2}{2}\partial_w^2(w^2\rho),$$

whose stationary state is a power law (Pareto). This is the cleanest case in the social sciences where the
*observed distribution shape* is predicted by a transport coefficient: multiplicative noise ⟹ heavy tails,
additive noise ⟹ Gaussian. Kinetic exchange models reproduce the same families and explain why redistribution
changes the exponent rather than the mechanism.

**Innovation and behaviour diffusion.** Adoption among a population with imitation gives logistic (Bass)
growth; combined with spatial movement it gives
$\partial_tp=D\nabla^2p+kp(1-p)$ — Fisher–KPP, with front speed $2\sqrt{Dk}$
([fronts](../04-interaction/05-fronts-and-travelling-waves.md)). Consequences that matter: adoption waves have a
*measurable* speed, heterogeneous resistance slows the front (pulled-front sensitivity), and spatial structure
determines whether an innovation stalls.

**Segregation.** Schelling's model — mild individual preferences plus local moves — is an energy-descent
process on a lattice: agents flip to reduce local "unhappiness", so the aggregate dynamics is a
[gradient flow](../01-foundations/07-entropy-and-variational-structure.md) with a strong hysteresis loop.
The famous result (mild preferences ⟹ severe segregation) is a statement about a *non-convex* energy landscape
with metastable states and path dependence, not about individual prejudice.

**Language change and contact.** A variant spreading in a population obeys a reaction–diffusion equation with
**Wright–Fisher noise**: logistic selection plus spatial diffusion plus genetic drift gives dialect boundaries —
clines, isoglosses and wave-like propagation, with the noise term mattering precisely because speaker
populations are finite ([stochastic PDEs](../06-beyond/07-stochastic-pdes-and-random-media.md)). Counting
vocabulary gives **Zipf's law**: preferential attachment (Yule–Simon) is multiplicative growth in frequency
space, whose stationary distribution is a power law with exponent near 1 — the same mechanism as wealth above,
applied to words.

**Networks and crowds.** Epidemics, rumours and crowd flow live on graphs and in space: SIR-type reaction
diffusion on contact networks, nonlocal pedestrian transport (a flux depending on a *neighbourhood* density —
[nonlocal operators](../06-beyond/03-nonlocal-and-fractional-operators.md)), and mean-field games for
strategic routing.

| Social object | Transport structure | Shape it predicts |
|---|---|---|
| opinions | nonlinear diffusion / degenerate | clustering, polarisation, consensus time |
| wealth, word frequencies | multiplicative-noise Fokker–Planck / Yule–Simon | power laws, lognormal cores |
| adoption, rumours | logistic + diffusion (Fisher–KPP) | fronts with speed $2\sqrt{Dk}$ |
| segregation | energy descent with hysteresis | sharp separating interfaces |
| dialects | reaction–diffusion + Wright–Fisher noise | clines, isoglosses, drift |
| cities and flows | gravity models, optimal transport | spatial interaction laws |

## L3 · What the mathematics guarantees — and what it warns you about

* **Aggregation is a theorem with hypotheses.** Going from agents to a density needs many weakly correlated
  agents. Fault that condition and the fluid description fails *qualitatively*: finite populations add
  demographic noise (Wright–Fisher), small groups can lock into states the mean-field theory says are
  impossible, and a single influential actor can change a front (pulled fronts are driven by their leading
  edge — [fronts](../04-interaction/05-fronts-and-travelling-waves.md)).
* **Stationary shapes are diagnostic, not explanatory.** Pareto tails, Zipf exponents and lognormal cores each
  arise from several different mechanisms; the transport equation tells you *which families* are possible
  (multiplicative noise ⟹ heavy tails; additive ⟹ Gaussian) and what else must be true if that family holds
  (e.g. two-regime transport: lognormal body, power-law tail). It does not identify the mechanism from the shape
  alone — the social version of the non-identifiability warning
  ([inverse problems](../07-numerics/10-inverse-problems-and-data-assimilation.md)).
* **Hysteresis and tipping points are structural.** Non-convex energies mean the same parameters support
  several stable states; policy changes may be reversible in the model but not in the trajectory. Where the
  transport equation has a saddle-node bifurcation, the system has a **tipping point**, and near it the
  linearised drift loses its restoring rate: *critical slowing down*. That yields testable early-warning
  statistics — rising variance, rising autocorrelation, longer recovery times — because the spectral gap is
  closing ([spectral view](../01-foundations/06-spectral-and-green-function-view.md)).
* **Optimality and equilibrium are different theories.** Mean-field games pair an agent-level optimality
  principle (HJB) with a population-level transport equation (Fokker–Planck): the equilibrium is a *fixed point
  of the coupling*. Classic equilibria (Nash, competitive, Walrasian) are the static limits; the transport view
  adds the approach dynamics, its stability, and the possibility of cycles where the static theory sees none
  ([finance & economics](../08-bridges/02-finance-and-economics.md)).
* **Parameters are behavioural, so they move.** Unlike viscosity, an adoption rate or a dispersion coefficient
  responds to the policy applied to it — the transport coefficients are not constants of nature. Fit them on
  one regime and use them in another at your peril; this is the mathematical content of the Lucas critique.

## L4 · Practice

* **Estimate exponents honestly.** Log–log least squares is biased: use maximum likelihood with a
  Kolmogorov–Smirnov or Hill estimator, fit the *tail separately* from the body, and report confidence intervals
  by bootstrap. Distinguish "the data are heavy-tailed" from "the model is a power law".
* **Simulate agents and the continuum together.** Validate every mean-field reduction against agent-based
  simulation at several population sizes, and use the discrepancy to estimate the size of the fluctuation
  correction. Where they disagree, believe the agents.
* **Do not confuse expansion with relocation.** A spreading front and a hierarchical jump-diffusion can produce
  the same spatial adoption pattern: identifiability requires time-resolved data (which individuals adopted
  where), not just a final map — the geography version of the same warning as above.
* **Networks change the thresholds.** Epidemic and cascade thresholds depend on the graph's spectral radius,
  not on mean degree; use configuration models and real topologies, and check network version versus mean-field
  prediction ([networks & traffic](../08-bridges/09-networks-society-and-traffic.md)).
* **Early-warning indicators need discipline**: detrend, use rolling windows, correct for multiple comparisons,
  and report false-positive rates — slowing down is a genuine fingerprint, but not a prophecy.
* **Benchmarks**: Bass-model adoption curves and their spatial fronts; Zipf's law under a stated tokenization;
  Lorenz/Gini recomputed from fitted distributions; Schelling segregation curves; epidemic thresholds against
  network spectra.

## Checks

1. Why do multiplicative (not additive) fluctuations in wealth produce power-law tails? *(The Langevin equation $\dot w=\mu w+\sigma w\xi$ has a stationary Fokker–Planck solution $\rho\propto w^{-(1+2\mu/\sigma^2)}$ — a Pareto law determined by the drift-to-noise ratio.)*
2. What does a tipping point look like in the transport equation, and what is the observable warning?
   *(A saddle-node bifurcation of the drift; near it the linearised restoring rate vanishes — critical slowing
   down, with rising variance and autocorrelation.)*
3. What is the social analogue of the Knudsen number, and what happens when it is small? *(Population size
   relative to interaction correlation length; small populations add demographic noise, so the fluid/mean-field
   description fails and stochastic agent models are required.)*
4. Why can the same final map of adoption be produced by two different transport mechanisms? *(Contagious
   expansion (front) and hierarchical jump-diffusion are non-identifiable from end states alone.)*

## See also

[Cognitive science & mind](03-cognitive-science-and-mind.md) ·
[Fronts & travelling waves](../04-interaction/05-fronts-and-travelling-waves.md) ·
[Networks, society & traffic](../08-bridges/09-networks-society-and-traffic.md) ·
[Finance & economics](../08-bridges/02-finance-and-economics.md) ·
[Limits of the claim](09-limits-of-the-claim.md)

