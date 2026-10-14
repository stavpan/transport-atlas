---
title: The decision tree & lookup
blurb: Your object → its transport form. Sixty translations, with the equation you get and the note that explains it.
depth: 3
tags: [universality, lookup, translation, decision-tree, table]
---

# The decision tree & lookup

> **One-line picture.** Find your object on the left, read the transport form on the right, follow the link.
> If your object is not here, the [checklist](01-why-everything-flows.md) will get you there in eight steps.
>
> **Prerequisites.** [Why everything flows](01-why-everything-flows.md) ·
> **Leads to.** the domain notes of this part, and every note they link to

## Step 1 · The three-question decision tree

```
        Is there a countable quantity whose changes you can attribute
        to crossing a boundary + creation/destruction?
                          │
            ┌── no ───────┴─────── yes ──────────────────────────────┐
            │                                                       │
   Not (yet) a transport problem.                        What drives the movement?
   Try: enlarge the state,                          ┌──────────┬──────────┬─────────┐
   change the observable,                        gradient    random     optimal  symmetry
   or read the limits note.                          │          │          │        │
                                                     ▼          ▼          ▼        ▼
                                              constitutive  generator   HJB +    Noether
                                              law ⟹ PDE     ⟹ master / dual     ⟹ conserved
                                              (Fick,        FP /       density    quantities,
                                              Fourier,      kinetic    flow       constraints
                                              Darcy, …)                (MFG, OT)
                                                     │          │          │        │
                                                     └──────────┴──────────┴────────┘
                                                                  │
                            classify the operator (order, type, dimension),
                            non-dimensionalise, find the invariants/Lyapunov functional,
                            choose the numerics, and state the validity range.
```

## Step 2 · The lookup table

### Physics and engineering

| Your object | Transport form | Note |
|---|---|---|
| heat, solute, momentum in a continuum | advection–diffusion; Navier–Stokes | [diffusion](../01-foundations/01-balance-laws-and-flux.md) |
| a shock, a traffic jam, a flood wave | scalar conservation law + entropy condition | [shocks](../06-beyond/01-conservation-laws-and-shocks.md) |
| a flame, an epidemic front, an invader | reaction–diffusion front, speed $2\sqrt{Dk}$ | [fronts](../04-interaction/05-fronts-and-travelling-waves.md) |
| a phase boundary (melting, freezing) | Stefan free boundary | [phase change](../04-interaction/09-phase-change-and-stefan.md) |
| a rough growing interface | KPZ / stochastic growth | [SPDEs](../06-beyond/07-stochastic-pdes-and-random-media.md) |
| light or neutrons in a medium | radiative transfer (integro-differential) | [radiative transfer](../05-kinetic/04-radiative-transfer.md) |
| a rarefied gas, a micro-device | Boltzmann/kinetic; DSMC | [Boltzmann](../05-kinetic/01-boltzmann-equation.md) |
| a plasma, a fusion edge | Vlasov + Maxwell; gyrokinetics | [plasma kinetics](../05-kinetic/02-bgk-vlasov-and-plasma-kinetics.md) |
| a fibre-optic pulse, a rogue wave | nonlinear Schrödinger (integrable) | [solitons](../06-beyond/14-integrable-systems-and-solitons.md) |
| a suspension, a granular material | kinetic theory of granular gases; nonlocal rheology | [rheology](../02-bulk/09-non-newtonian-rheology.md) |
| spacetime itself | second-order constrained hyperbolic system | [MHD & relativity](../06-beyond/13-mhd-and-relativistic-transport.md) |
| quantum probability | continuity equation for $\lvert\psi\rvert^2$; Wigner transport | [quantum matter](../08-bridges/10-quantum-and-condensed-matter.md) |
| a quantum field | propagators (Green functions); RG flow of couplings | [mathematics itself](08-mathematics-itself.md) |
| turbulence | stochastic cascade + closure problem | [turbulence](../02-bulk/05-turbulence-and-eddy-diffusivity.md) |
| a climate model | advection–diffusion on a rotating sphere + radiation | [geoscience](../08-bridges/04-geoscience-and-climate.md) |
| ice sheets, glaciers | nonlinear (Glen) viscous flow, free surface | [nonlinear diffusion](../06-beyond/06-nonlinear-diffusion-and-porous-medium.md) |
| an electrochemical cell | porous-electrode Nernst–Planck + porous flow | [charged transport](../03-microscopic/07-charged-and-electrochemical-transport.md) |
| a composite material | homogenised tensor transport | [homogenisation](../06-beyond/08-homogenization-and-upscaling.md) |
| a crack, a damage zone | nonlocal (peridynamic) mechanics | [microcontinuum](../06-beyond/11-microcontinuum-and-generalized-continua.md) |

### Life, mind and behaviour

| Your object | Transport form | Note |
|---|---|---|
| a chemical reaction network | master equation / mass-action ODE | [kinetics](../04-interaction/01-reaction-kinetics-and-sinks.md) |
| a gene network with bursting | piecewise-deterministic Markov process (Liouville + reset) | [why everything flows](01-why-everything-flows.md) |
| transport inside a cell | crowding-limited anomalous diffusion | [anomalous diffusion](../03-microscopic/08-anomalous-diffusion.md) |
| embryonic patterning | reaction–diffusion / Turing | [Turing patterns](../04-interaction/04-reaction-diffusion-and-turing.md) |
| bacterial chemotaxis, immune recruitment | Keller–Segel; blow-up threshold $8\pi/\chi$ | [chemotaxis](../04-interaction/06-chemotaxis-and-keller-segel.md) |
| a neuron's membrane potential | cable equation; excitable medium; conduction delay | [delay](../06-beyond/16-delay-and-retarded-transport.md) |
| neural population activity | neural-field equations; mean-field density of spiking networks | [cognitive science](03-cognitive-science-and-mind.md) |
| perceptual decision making | drift–diffusion; first-passage time distributions | [cognitive science](03-cognitive-science-and-mind.md) |
| predictive coding, active inference | variational free-energy descent (KL gradient flow) | [cognitive science](03-cognitive-science-and-mind.md) |
| working memory, attractors | Hopfield energy descent (gradient flow on a spin glass) | [cognitive science](03-cognitive-science-and-mind.md) |
| forgetting curves | power-law relaxation / fractional diffusion | [cognitive science](03-cognitive-science-and-mind.md) |
| priming, spreading activation | diffusion on a semantic graph | [cognitive science](03-cognitive-science-and-mind.md) |
| synaptic plasticity, learning | stochastic gradient descent → Fokker–Planck | [computation](05-computation-and-algorithms.md) |
| an epidemic | SIR-type reaction–diffusion; network transport | [networks & traffic](../08-bridges/09-networks-society-and-traffic.md) |
| ecological invasion | Fisher–KPP front (pulled speed) | [fronts](../04-interaction/05-fronts-and-travelling-waves.md) |
| foraging and search | Lévy flights (superdiffusion) | [anomalous diffusion](../03-microscopic/08-anomalous-diffusion.md) |
| tumour growth and drug delivery | reaction–diffusion + poroelasticity + binding | [biology & medicine](../08-bridges/03-biology-and-medicine.md) |

### Society, economics and language

| Your object | Transport form | Note |
|---|---|---|
| opinion dynamics | nonlinear diffusion / bounded-confidence transport | [social science](04-social-behaviour-economics-language.md) |
| segregation | energy descent on a lattice (flip dynamics) | [social science](04-social-behaviour-economics-language.md) |
| innovation diffusion | logistic/Bass growth ⟹ reaction–diffusion in space | [social science](04-social-behaviour-economics-language.md) |
| wealth and income distributions | Fokker–Planck with multiplicative noise ⟹ power laws | [social science](04-social-behaviour-economics-language.md) |
| market prices | drift–diffusion (backward Kolmogorov) | [finance](../08-bridges/02-finance-and-economics.md) |
| strategic interaction of many agents | mean-field games (HJB + Fokker–Planck) | [finance](../08-bridges/02-finance-and-economics.md) |
| language change, dialect diffusion | advection–diffusion + Wright–Fisher noise | [social science](04-social-behaviour-economics-language.md) |
| word-frequency distributions | Yule–Simon preferential attachment ⟹ power law | [social science](04-social-behaviour-economics-language.md) |
| traffic | conservation law with concave flux | [networks & traffic](../08-bridges/09-networks-society-and-traffic.md) |
| crowd dynamics | nonlocal pedestrian transport; mean-field games | [social science](04-social-behaviour-economics-language.md) |
| information and rumours | reaction–diffusion on contact networks | [networks & traffic](../08-bridges/09-networks-society-and-traffic.md) |

### Computation, information and mathematics

| Your object | Transport form | Note |
|---|---|---|
| shortest paths, A\*, travel-time fields | eikonal / Hamilton–Jacobi; fast marching | [computation](05-computation-and-algorithms.md) |
| PageRank, influence, consensus | diffusion on a graph (graph Laplacian) | [computation](05-computation-and-algorithms.md) |
| gradient-descent training | gradient flow; with noise ⟹ Fokker–Planck | [computation](05-computation-and-algorithms.md) |
| Monte Carlo, HMC sampling | transport of measures in phase space | [computation](05-computation-and-algorithms.md) |
| diffusion models, flow matching | reverse-time SDE / continuity equation | [machine learning & data](../08-bridges/07-machine-learning-and-data.md) |
| Bayesian updating | transport of a measure (a change of measure) | [information & inference](07-information-statistics-and-inference.md) |
| estimators, Cramér–Rao bounds | gradient flow in Fisher–Rao geometry (natural gradient) | [information & inference](07-information-statistics-and-inference.md) |
| rare events, large deviations | WKB/Hamilton–Jacobi rate function (Sanov, Freidlin–Wentzell) | [information & inference](07-information-statistics-and-inference.md) |
| Ricci flow, mean-curvature flow | geometric diffusion of a metric or interface | [mathematics itself](08-mathematics-itself.md) |
| Markov kernels, probabilistic programming | Markov category: transport maps as morphisms | [mathematics itself](08-mathematics-itself.md) |
| eigenvalue statistics, random matrices | integrable hierarchies, determinantal processes | [solitons](../06-beyond/14-integrable-systems-and-solitons.md) |
| theta functions, modular forms | heat kernels on lattices and their symmetries | [mathematics itself](08-mathematics-itself.md) |

## Step 3 · What is *not* covered

The table is large, but it is not universal. Conspicuously absent: meaning, semantics, purpose,
measurement, and the discrete structure of language and games. Those are treated honestly in
[limits of the claim](09-limits-of-the-claim.md). The short version: transport theory is a theory of
**redistribution**, so it speaks only about quantities that can be counted and moved — and about the
consequences of the constraints that counting and moving impose.

> [!tip] How to use this page
> Do not read the table top to bottom. Find *your* object, note the equation family, then jump straight
> to that family's note and read only its L1 and L2 rungs. If the fit is wrong, go up one level to
> [the five structures](01-why-everything-flows.md) and re-derive the translation yourself — that is
> faster than browsing sixty rows.

## Checks

1. Which row covers "the number of users of an app"? *(Innovation diffusion: logistic growth, plus
   reaction–diffusion if geography matters.)*
2. Which row covers training a neural network with a noisy gradient? *(SGD as a Fokker–Planck/Langevin
   flow — the same family as Kramers escape and diffusion models.)*
3. Why does "shortest path" belong in the same table as heat conduction? *(Both are fields of the same
   transport structure — arrival times (eikonal/HJ) versus densities (diffusion); Dijkstra is a discrete
   Hamilton–Jacobi solver.)*
4. What would you do if your object is a *decision* rather than a quantity? *(Model the decision
   variable's distribution or its evidence accumulation; if the object has no distribution, you are outside
   the claim — see the limits note.)*

## See also

[Why everything flows](01-why-everything-flows.md) ·
[Cognitive science & mind](03-cognitive-science-and-mind.md) ·
[Computation & algorithms](05-computation-and-algorithms.md) ·
[Mathematics itself](08-mathematics-itself.md) ·
[Limits of the claim](09-limits-of-the-claim.md)


