---
title: Collective behaviour and synchrony
blurb: Fireflies, flocks and power grids — coupled oscillators as a transport problem for phase, the Kuramoto threshold, chimeras, and how to talk about synchrony without over-claiming.
depth: 4
tags: [panta rhei, synchrony, Kuramoto, collective behaviour, networks, phase transition]
---

# Collective behaviour and synchrony

> **One-line picture.** Thousands of independent units with their own rhythms can agree on a common
> rhythm — abruptly, at a critical coupling, and with the same mathematics whether the units are
> fireflies, neurons, generators on a grid, or people clapping. The trick is to stop tracking each unit
> and start tracking the **density of phases**, which is a transport problem.
>
> **Prerequisites.** [Phase transitions & criticality](../12-recurring-mechanisms/06-phase-transitions-and-criticality.md),
> [Networks, society & traffic](../08-bridges/09-networks-society-and-traffic.md) ·
> **Leads to.** [Crossings & cross-fertilisation](05-crossings-and-cross-fertilisation.md),
> [the river as a model](06-the-river-as-a-model.md)

## L1 · The phenomena

* **Fireflies** in a mangrove forest flash in loose unison, and then in tight unison, without a leader.
* **Pacemaker cells** in the heart fire together; if they fail to synchronise, the heart does not pump.
* **A power grid** holds a common frequency (50 or 60 Hz) across a continent; when synchronism is lost,
  the grid *is* the failure, and the 2003 and 2009 blackouts are studies in desynchronisation.
* **Flocks and schools** align their headings; **crowds** lock their footsteps (the Millennium Bridge
  wobble); **audiences** converge on synchronised applause and then abandon it.
* **Neurons** show oscillations that lock to stimuli and to each other, which is how the brain is
  believed to bind features across regions.

What unites them: many *self-sustained oscillators*, weak *coupling*, and (usually) *heterogeneity* —
no two fireflies or generators have exactly the same natural frequency. Synchrony is not the absence of
disagreement; it is a *collective decision* taken in the presence of it.

## L2 · The Kuramoto model: order from frequency disorder

Set aside the physics of each unit and describe only its **phase** $\theta_i$ (where it is in its cycle),
with a natural frequency $\omega_i$ drawn from a distribution $g(\omega)$, and a sinusoidal coupling to
the mean field:

$$\dot\theta_i=\omega_i+\frac{K}{N}\sum_j\sin(\theta_j-\theta_i).$$

Define the **order parameter** $r$ as the magnitude of the mean of $e^{i\theta}$: $r=0$ means the phases
are scattered, $r\approx1$ means they are locked. The exact result (for an infinite population) is a
sharp threshold:

$$K_c=\frac{2}{\pi\,g(0)},\qquad r\simeq\sqrt{1-K_c/K}\ \ \text{for }K>K_c,$$

so the transition is continuous with the *mean-field critical exponent* $1/2$ — the same square root as
in the [phase-transition note](../12-recurring-mechanisms/06-phase-transitions-and-criticality.md).
Note what $K_c$ depends on: not the mean frequency (a common rotation is unobservable in a phase
comparison) but the **density of oscillators at the mean**, $g(0)$. Rarer agreement at the centre means
harder lock-in.

![**Figure P3.** Kuramoto synchronisation from a real simulation ($N=400$, Lorentzian frequencies, threshold
$K_c=2\gamma$ here $=1$). Left: the order parameter rises from zero at the predicted threshold, following
the theoretical square-root law until finite-size fluctuations blur it. Right: phase snapshots below and
above threshold, coloured by natural frequency — below, a smeared circle; above, a locked cluster with a
tail of still-drifting outliers. That tail is *not* a defect: it is the mathematically necessary
consequence of having frequencies far from the mean.](../../figures/kuramoto-synchronisation.svg)

Where the same structure appears (a partial list, because the model is deliberately indifferent to the
substrate):

| System | The oscillators | The coupling | What $r$ would mean |
|---|---|---|---|
| Fireflies | flashing cycles | visual reset by neighbours | fraction of the population in phase |
| Heart / circadian | pacemaker cells, SCN neurons | gap junctions, neurotransmitters | coherent tissue rhythm |
| Power grid | generators (rotor angles) | transmission lines (power flow) | continental frequency lock |
| Neurons | membrane potentials | synaptic currents | a travelling oscillation |
| Crowds | walking gaits | mechanical coupling through the bridge | synchronised footfalls |
| Lasers | cavity modes | light field | phase locking of a laser array |

## L3 · Why this belongs in a transport atlas

Because the thing that actually evolves is a *density*: the distribution of phases, $\rho(\theta,t)$,
obeys an exact **continuity equation** on the circle,

$$\frac{\partial\rho}{\partial t}+\frac{\partial}{\partial\theta}\big[(\omega+K\,r\sin(\psi-\theta))\rho\big]=0,$$

where $(r,\psi)$ is the mean field computed from $\rho$ itself. Synchronisation is therefore a
*self-consistent transport problem*: the flux of phases depends on the distribution, which depends on the
flux. Three consequences follow directly from material already in this atlas:

* **It is a critical phenomenon.** At $K_c$ the phase distribution loses stability of the incoherent
  state in a way that is analysed exactly as in note
  [6 of part 12](../12-recurring-mechanisms/06-phase-transitions-and-criticality.md) — a linear stability
  problem around a uniform state, with $r$ as the order parameter.
* **It has a low-dimensional description.** For Lorentzian frequencies the infinite-$N$ dynamics reduces
  *exactly* to a two-dimensional equation for the mean field (the Ott–Antonsen reduction). This is a
  textbook example of the atlas's central claim: track the density, and a
  $10^{23}$-dimensional problem becomes two equations.
* **Geometry enters through the coupling operator.** Replace the all-to-all sum by a network or a
  nonlocal kernel and the threshold becomes a spectral property of that operator. Degree heterogeneity
  can *lower* the threshold sharply (and, in some degree-correlated networks, produce an explosive,
  first-order transition), while sparse expander-like graphs can synchronise with an asymptotically
  vanishing coupling. The structure of the coupling is therefore a first-class part of the physics, not a
  technical detail.

Two further collective phenomena worth knowing by name:

* **Chimera states.** With nonlocal coupling, one system can split into coexisting coherent and incoherent
  domains: half your fireflies blink together while the other half flash erratically. Discovered as a
  theoretical curiosity, now seen in mechanical, optical and electrochemical systems.
* **Metastability.** Partially locked clusters can form, dissolve and re-form on long timescales, so the
  order parameter fluctuates between several values rather than choosing one. In networks this is the
  bridge to memory and computation: metastable states are what a network can *hold*.

## L4 · Measuring and claiming synchrony honestly

1. **Separate three different things:** *co-occurrence* (events happen near each other), *correlation*
   (signals covary), and *phase locking* (the phase difference is bounded). Only the third is synchrony
   in the technical sense, and a common input — a shared stimulus, a shared driver, a shared noise — can
   produce the first two with no coupling at all.
2. **Estimate phases deliberately.** Hilbert transform, wavelet phase, or an event-based phase from the
   timing of spikes or flashes; each has artefacts for broadband signals. Report the method.
3. **Test significance against surrogates.** Phase-randomised surrogates destroy coupling while preserving
   spectra; if your synchrony index is not significantly above the surrogate band, you have measured
   your own window length. Below $K_c$ the order parameter *fluctuates* like $1/\sqrt{N}$ — finite-size
   noise looks a lot like weak synchrony.
4. **Distinguish a smooth transition from a sudden one.** Where the transition is first-order (explosive),
   early-warning logic from [bifurcation theory](../12-recurring-mechanisms/03-bifurcation-theory.md)
   applies to the *synchronised* branch, not the incoherent one, and hysteresis means the response
   depends on history.
5. **Be sceptical of famous anecdotes.** The synchrony literature contains celebrated effects that failed
   replication (human menstrual synchrony is the standard cautionary case), and effects that are real but
   explained by a shared external driver (the Millennium Bridge wobble is genuinely driven by footfall
   coupling, but the 50 Hz grid frequency is *imposed* by control loops as much as it emerges). Name the
   coupling mechanism or say plainly that you have not identified one.
6. **Remember the engineering reading.** In a power grid, synchrony is not a curiosity but a service:
   loss of phase locking *is* the blackout, and the useful question is how far from the threshold you are
   operating and how the threshold moves under load and network changes.