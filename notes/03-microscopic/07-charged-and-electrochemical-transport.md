---
title: Charged & electrochemical transport
blurb: Nernst–Planck, Poisson–Nernst–Planck, electroneutrality, Debye layers — transport with electric fields, including semiconductor drift–diffusion.
depth: 3
tags: [Nernst-Planck, Poisson, electroneutrality, Debye, drift-diffusion, electrolytes]
---

# Charged & electrochemical transport

> **One-line picture.** Ions respond to two drives at once — concentration gradients (diffusion)
> and electric fields (migration) — and they *create* the fields they respond to.
>
> **Prerequisites.** [diffusion](01-diffusion.md),
> [cross-effects](06-cross-effects-and-multicomponent.md) · **Leads to.**
> [biology & medicine](../08-bridges/03-biology-and-medicine.md),
> [engineering devices](../08-bridges/06-engineering-devices.md)

## L1 · Two forces, one species

Salt in water and electrons in silicon obey the same transport equation. Each charged species
carries a flux with a diffusive part and a migration part:

$$\mathbf{J}_i=-D_i\nabla c_i-\frac{z_iF}{RT}D_i c_i\nabla\phi+\mathbf{u}c_i,\qquad
-\varepsilon\nabla^2\phi=F\sum_i z_ic_i .$$

The first line is the **Nernst–Planck** equation; the second is **Poisson's** equation. Together
they are the **Poisson–Nernst–Planck (PNP)** system. Note the built-in Einstein relation between
mobility and diffusivity ($D_i=u_iRT/F$) — the electrostatic face of the
[fluctuation–dissipation theorem](../01-foundations/08-random-walks-langevin-response.md).

## L2 · The approximations that make it tractable

| Approximation | Statement | When valid |
|---|---|---|
| electroneutrality | $\sum z_ic_i\approx0$ | away from interfaces, $L\gg\lambda_D$ |
| Debye layer | $\lambda_D=\sqrt{\varepsilon RT/(F^2\sum z_i^2c_i)}$ | sets the interfacial length scale (0.3–100 nm in water) |
| linearised PB | $zF\phi/RT\ll1$ | small potentials: Gouy–Chapman vs Debye–Hückel |
| single-ionic drift–diffusion | neglect $\nabla\phi$ from carriers | low-injection semiconductors |
| ambipolar diffusion | electrons and holes move together | photoconductors, plasmas |
| limiting current | one species exhausted at the electrode | electrodialysis, batteries at high rate |

In semiconductors the same equation is written
$\mathbf{J}_n=qD_n\nabla n+q\mu_nn\nabla\psi$ plus a recombination term; in plasmas, ambipolar
diffusion keeps quasineutrality by tying electron and ion fluxes together. **One equation, three
communities, three vocabularies** — see
[words that collide #3](../09-polysemy/03-diffusion-and-conduction.md).

## L3 · What the mathematics guarantees

* **Electroneutrality is an asymptotic limit.** As $\lambda_D/L\to0$, PNP converges (after matching
  boundary layers) to the electroneutral drift–diffusion system — the mathematical reason bulk
  electrolytes have no field, while interfaces always do.
* **Debye layers are boundary layers.** The potential decays exponentially over $\lambda_D$, giving
  a surface capacitance $\varepsilon/\lambda_D$ and a streaming potential when fluid flows past a
  charged wall. Overlapping Debye layers change the transport law entirely (nanochannels).
* **Nonlinearity and non-ideality.** Activity coefficients, ion pairing and steric (finite-size)
  effects matter at high concentration; then Nernst–Planck must be generalised (Maxwell–Stefan with
  electroneutrality constraints, or PNP with modified electrochemical potentials).
* **Charges create structure.** Space-charge regions, concentration polarisation and (in extreme
  cases) electroconvective instability are *consequences* of the coupling, not add-ons; they are the
  reason electrodialysis and battery charging hit limits.

## L4 · Numerics

* **Stiffness is severe** because $\varepsilon$ is tiny: Poisson couples over nm while devices are
  mm. Implicit or multiscale treatments, and asymptotic (electroneutral) formulations, are standard.
* **Current conservation** must be enforced exactly — non-conservative discretisations produce
  spurious charge accumulation and non-convergence. Use finite-volume or mixed FEM with consistent
  fluxes ([structure-preserving schemes](../07-numerics/13-structure-preserving-discretizations.md)).
* **Positivity** is mandatory: negative concentrations or densities break the Poisson coupling.
  Reconstruct in log-variables (Slotboom transform) when needed.
* **Benchmarks**: the Gouy–Chapman profile, limiting-current polarisation curves, the PNP system for
  a perm-selective membrane, and the standard SOC/diode curves for semiconductor solvers
  ([V&V](../07-numerics/12-verification-validation-and-benchmarks.md)).
* **Frontiers.** Ion transport in nanochannels and biological pores; electroconvection; coupled
  electro-chemo-mechanics in solid electrolytes (dendrites, fracture).

## Checks

1. Why does the bulk of an electrolyte show no electric field? *(Electroneutrality at leading
   order; fields live in Debye layers of thickness $\lambda_D$.)*
2. What is the transport analogue of the Einstein relation here? *(Mobility and diffusivity are
   proportional: $D=uRT/F$.)*
3. Why is PNP numerically stiff? *(The Poisson length scale $\lambda_D$ can be 5 orders of magnitude
   below the device scale.)*

## See also

[Cross-effects & multicomponent](06-cross-effects-and-multicomponent.md) ·
[Diffusion](01-diffusion.md) ·
[Biology & medicine](../08-bridges/03-biology-and-medicine.md) ·
[Engineering devices](../08-bridges/06-engineering-devices.md)
