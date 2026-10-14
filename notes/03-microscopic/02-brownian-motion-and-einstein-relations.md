---
title: Brownian motion & Einstein relations
blurb: The 1905 argument that settled the existence of atoms, and the fluctuation–dissipation relations that every simulation still relies on.
depth: 2
tags: [Brownian, Einstein, Stokes-Einstein, Einstein relation, MSD]
---

# Brownian motion & Einstein relations

> **One-line picture.** Watch a pollen grain under a microscope and it jitters. The jitter is
> molecules; the smoothed-out law of the jitter is Fick's law; and the relation between them fixes
> the size of atoms.
>
> **Prerequisites.** [diffusion](01-diffusion.md),
> [random walks](../01-foundations/08-random-walks-langevin-response.md) · **Leads to.**
> [Fokker–Planck & Kramers](../05-kinetic/03-fokker-planck-and-kramers.md),
> [anomalous diffusion](08-anomalous-diffusion.md)

## L1 · The experiment and the argument

In 1827 Brown saw pollen grains jittering in water and could not explain it. In 1905 Einstein
proposed that the grains are being kicked by molecules too small to see, and turned that hypothesis
into a testable number:

$$\langle x^2\rangle=2Dt,\qquad D=\frac{k_BT}{6\pi\mu a}.$$

Measure the jitter of a sphere of known radius in water of known viscosity at known temperature and
you have measured $k_B$ — hence Avogadro's number, hence the size of molecules. This is one of the
arguments that made atoms unavoidable, and Perrin's experiments (1908) settled it.

## L2 · Three relations everyone uses

| Relation | Statement | Use |
|---|---|---|
| MSD law | $\langle r^2\rangle=6Dt$ (3-D) | extract $D$ from trajectories |
| Einstein (diffusion–mobility) | $D=\mu_{\rm mob}k_BT$ | link transport to response |
| Stokes–Einstein | $D=k_BT/(6\pi\mu a)$ | size from diffusion, diffusion from size |
| Stokes–Einstein–Debye (rotational) | $D_{\rm rot}=k_BT/(8\pi\mu a^3)$ | fluorescence anisotropy, NMR relaxation |
| Smoluchowski (suspensions) | collect $D$ and drift for settling | sedimentation equilibrium |

The Einstein relation is the simplest instance of the
[fluctuation–dissipation theorem](../01-foundations/08-random-walks-langevin-response.md): the same
molecular collisions that cause diffusion also cause drag. Consequently **you never fit both** — one
determines the other, and a simulation that violates this violates the second law.

Einstein's other gift to transport theory is the osmotic-pressure interpretation: a suspension
sedimenting under gravity settles until the sedimentation flux balances the diffusive flux, giving
the barometric profile $c(z)\propto e^{-mgz/k_BT}$. This is the equilibrium face of transport:
**flux balance *is* equilibrium.**

## L3 · What the mathematics guarantees

* **The microscopic scale sets the coefficient.** $D$ is a function of temperature, molecular size
  and solvent viscosity — not of the apparatus. That is why $D$ is a *material property* in the
  macroscopic equation.
* **Reynolds-number dependence.** Stokes–Einstein assumes $\mathrm{Re}\ll1$; larger particles or
  lower viscosity require corrections (Oseen, Faxén, or the full mobility tensor for anisotropic
  bodies), and near walls the mobility is reduced by hydrodynamic interactions.
* **Concentration dependence.** In concentrated suspensions, many-body hydrodynamic interactions
  reduce $D$ (and cause short-time/long-time discrepancies). Hard-sphere suspensions show
  $D\to0$ as jamming is approached — a transport coefficient controlled by geometry.
* **Finite particle size.** $D=k_BT/(6\pi\mu a)$ breaks down for solutes comparable to the solvent
  molecule (sub-nanometre), which is why measured diffusion of small ions is far below the
  hydrodynamic prediction (see [diffusion coefficients](04-diffusion-coefficients.md)).

## L4 · Measurement and simulation

* **Measurement.** Dynamic light scattering (DLS) measures $D$ from intensity autocorrelations;
  PFG-NMR measures displacement; single-particle tracking gives full distributions and detects
  anomalous behaviour ([measurement](../10-appendix/05-measurement-and-experiments.md)).
* **Simulation hierarchy.** Molecular dynamics (all-atom) → Brownian dynamics (Langevin with
  hydrodynamic interactions) → DPD/dissipative particle dynamics → continuum diffusion. Choosing
  the rung is an explicit trade between fidelity and time scale.
* **Trajectory analysis.** Always fit $\langle r^2\rangle$ with sub-sampling to avoid correlation
  bias; distinguish short-time and long-time diffusion coefficients in crowded systems.
* **Frontiers.** Anomalous diffusion in living cells (cytoskeletal obstacles, active motors);
  hydrodynamically interacting colloids near jamming; quantum limits of Brownian motion.

## Checks

1. Why does raising the temperature increase $D$ *and* decrease the viscosity, both raising $D$?
   *($D=k_BT/6\pi\mu a$: $T$ up, $\mu$ down, both increase $D$ — a double effect.)*
2. A protein of 5 nm radius in water at 300 K: what $D$? *($\approx4\times10^{-11}$ m²/s: a
   micron in ~10 s — the reason cells use motors.)*
3. What does sedimentation equilibrium tell you about the diffusion coefficient? *(Balancing
   sedimentation and diffusion fluxes gives a barometric profile whose decay length is set by
   $k_BT$.)*

## See also

[Diffusion](01-diffusion.md) ·
[Random walks, Langevin & response](../01-foundations/08-random-walks-langevin-response.md) ·
[Diffusion coefficients](04-diffusion-coefficients.md) ·
[Biology & medicine](../08-bridges/03-biology-and-medicine.md)
