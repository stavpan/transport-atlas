---
title: Transport in quantum & condensed matter
blurb: Heat carried by phonons, charge by electrons, spin by magnons — and where quantum transport stops looking like diffusion at all.
depth: 4
tags: [phonon, electron, spin, Wigner, superconductivity, second sound]
---

# Transport in quantum & condensed matter

> **One-line picture.** The same transport equations, with quantum carriers: what changes is that the
> carriers can be ballistic, coherent, and honest about their statistics.
>
> **Prerequisites.** [conduction](../03-microscopic/03-conduction.md),
> [the Boltzmann equation](../05-kinetic/01-boltzmann-equation.md)

## L1 · Five carriers, five transport stories

| Carrier | Transport quantity | Equation | Regime notes |
|---|---|---|---|
| phonon | heat | Boltzmann transport equation (BTE) | ballistic when $\ell\gg L$: Fourier's law fails |
| electron | charge and heat | drift–diffusion; BTE; Wiedemann–Franz | quantum coherence in mesoscopic devices |
| magnon | spin/heat | spin diffusion; magnon BTE | spin caloritronics |
| exciton / polariton | energy | diffusion + recombination | organic photovoltaics |
| superfluid/condensate | mass, heat | two-fluid model | second sound: heat as a wave |

Condensed matter is where the *limits* of classical transport are visible and controllable:

* **Ballistic transport** (nanowires, graphene, point contacts): resistance is set by geometry and
  quantum reflection, not by a bulk coefficient. Fourier's law is replaced by the Landauer picture.
* **Second sound**: in pure crystals at low temperature, heat propagates as a wave — the long-predicted
  [Maxwell–Cattaneo](../06-beyond/04-memory-viscoelastic-and-hereditary.md) regime, now routinely measured.
* **Hydrodynamic electron flow**: in very clean conductors, electrons behave as a viscous fluid, with
  viscous dissipation and Poiseuille-like profiles — quantum transport becoming
  [Navier–Stokes](../02-bulk/03-incompressible-flow-vorticity-and-pressure.md).
* **Quantum walks and Wigner transport**: the Wigner function obeys a kinetic equation whose diffusion
  limit is classical, but whose coherence terms have no classical analogue.

## L2 · The general structure

The transport coefficients of a quantum system are **Kubo formulas**: equilibrium correlation functions
of current operators, exactly the [Green–Kubo relations](../01-foundations/09-linear-response-and-memory.md)
with quantum correlators. This single structure explains:

* why thermal and electrical conductivity are linked (Wiedemann–Franz), and where that link fails;
* why transport is *dissipative from a unitary theory* only after coarse-graining — the quantum version of
  the H-theorem's fine print;
* why low-dimensional systems can have anomalously conducting or insulating behaviours (integrable
  systems, many-body localisation) that no classical diffusion equation reproduces.

## L3 · What is genuinely different

* **Quantisation of transport**: conductance can be quantised ($2e^2/h$ per channel), so "coefficient" is
  no longer a continuous material property.
* **Coherence**: interference between paths (Aharonov–Bohm, weak localisation) is transport behaviour with
  no classical counterpart.
* **Statistics matter**: fermions and bosons obey different distribution functions; the classical Fick law
  is the degenerate limit.
* **Long memory and non-Markovian dynamics** are the norm at short times: the memory kernel language of
  [Mori–Zwanzig](../01-foundations/09-linear-response-and-memory.md) is native to this field.

## L4 · Practice

* **Check the mean free path against the device** before using any bulk coefficient
  ([Knudsen-style reasoning](../03-microscopic/05-knudsen-and-rarefied-transport.md)).
* **Benchmarks**: Debye-model thermal conductivity, Landauer conductance of a point contact, second-sound
  pulse speeds, and Kubo-formula consistency with the fluctuation–dissipation theorem.
* **Frontiers.** Hydrodynamic electron flow in graphene and Weyl metals; phonon hydrodynamics; spin
  caloritronics; quantum thermal machines; transport in strongly correlated systems where quasiparticles
  fail.

## Checks

1. Why does Fourier's law fail in a nanowire? *(The phonon mean free path exceeds the wire length: transport
   is ballistic.)*
2. What is the quantum analogue of Green–Kubo? *(Kubo formulas: equilibrium current correlation functions,
   with quantum statistics.)*

## See also

[Conduction](../03-microscopic/03-conduction.md) ·
[The Boltzmann equation](../05-kinetic/01-boltzmann-equation.md) ·
[Linear response & memory](../01-foundations/09-linear-response-and-memory.md) ·
[Memory, viscoelasticity & Cattaneo](../06-beyond/04-memory-viscoelastic-and-hereditary.md)
