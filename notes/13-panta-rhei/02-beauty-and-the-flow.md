---
title: Beauty and the flow
blurb: Why these patterns please the eye — chaotic advection, Turing patterns, fractals, the processing-fluency account of pleasure, the mathematics inside ornament, and how to make a figure worth looking at.
depth: 4
tags: [panta rhei, beauty, art, generative, turing patterns, fractals, aesthetics, marbling]
---

# Beauty and the flow

> **One-line picture.** The pictures in this atlas are not decoration: they are the *only* way most of
> these mechanisms are ever recognised. Flow makes beauty with a small repertoire of tricks — folding,
> symmetry breaking, hierarchy, edge-of-chaos — and human eyes are tuned to read exactly those tricks.
> This note takes the aesthetics seriously, because design is how science is transmitted.
>
> **Prerequisites.** [Mixing & chaotic advection](../02-bulk/07-mixing-and-chaotic-advection.md),
> [Reaction–diffusion & Turing](../04-interaction/04-reaction-diffusion-and-turing.md) ·
> **Leads to.** [The river as a model](06-the-river-as-a-model.md),
> [scaling & self-similarity](../12-recurring-mechanisms/07-scaling-and-self-similarity.md)

## L1 · Four ways a flow makes something beautiful

1. **Folding and stretching (marbling).** Chocolate, Turkish paper, cream in coffee, Jupiter's clouds:
   all result from a flow that repeatedly stretches and folds a boundary. The result is an *infinite*
   layered structure with a finite number of material regions — beauty from pure kinematics, no forces
   required.
2. **Symmetry breaking (patterns).** A uniform mixture that *chooses* a wavelength produces spots,
   stripes, hexagons, spirals. The selection is not arbitrary: a growth-rate curve picks a band, and
   nonlinear competition picks the survivor
   ([Turing patterns](../04-interaction/04-reaction-diffusion-and-turing.md)).
3. **Self-similarity (fractals).** Coastlines, ferns, viscous fingering, turbulence, and the branching of
   rivers share the property that the *shape* survives a change of scale
   ([scaling](../12-recurring-mechanisms/07-scaling-and-self-similarity.md)). A fractal is an image with
   no natural zoom level, which is why it holds attention.
4. **Edge of chaos (critical avalanches).** Systems poised at a critical point produce event
   distributions with heavy tails: the eye is drawn to the occasional large event against a background of
   many small ones ([criticality](../12-recurring-mechanisms/06-phase-transitions-and-criticality.md)).

![**Figure P1.** Marbling, computed rather than photographed. Two point vortices blink on and off in turn
in an incompressible flow, and tracer particles — coloured by where they started — are stirred for a few
thousand timesteps. Nothing here is random: the filaments are the *deterministic* consequence of repeated
stretch-and-fold. This is Aref's blinking vortex, and it is the same mechanism that swirls cream into
coffee and then, given time, mixes it away.](../../figures/generative-flow-art.svg)

![**Animation A1.** Marbling, in motion: the same two blinking vortices as the figure
above, run for a few thousand timesteps. Watch the boundary being stretched into filaments —
this is how a stirred cup mixes *without* any turbulence at all.](../../figures/anim-flow-marbling.webp)

![**Figure P2.** The other kind of beauty: a Turing pattern grown from two chemicals with a simple
autocatalytic rule (left) and the reason it looks like this (right) — only a band of wavelengths can grow,
so the system selects a size. This is the standard Gray–Scott system, and it is the ancestor of half the
"natural" texture in computer graphics.](../../figures/reaction-diffusion-art.svg)

![**Animation A2.** The same pattern growing: seeds are placed, spread, collide and
settle. The wavelength is chosen by the dynamics, not by the seeds — and every spot stops
itself by eating the fuel around it.](../../figures/anim-turing-growth.webp)

## L2 · Why they please: the psychology, briefly and without hand-waving

The most useful account in experimental aesthetics is **processing fluency**: the ease with which a
stimulus is processed is itself *hedonically marked* — fluent processing feels good, and people read that
feeling as information about the object ("this is good, this is true"). Fluency is raised by *good form,
symmetry, figure–ground contrast and prototypicality*, and by the viewer's own experience (repeated
exposure, familiarity).

Two consequences matter here, because both are visible in the figures above:

* **The inverted U.** Complexity hurts twice: too complex and processing is disfluent (hard work, no
  pleasure); too simple and the ease is discounted as uninformative ("of course it's easy, it's plain").
  Beauty peaks between — precisely where a *pattern with structure* lives. Flow systems sit exactly
  there: a marbled image is locally intricate but globally organised, so it is fluent *and* surprising.
* **Fluency is about structure, not about symmetry alone.** A Turing pattern is not symmetric in the
  wallpaper sense; it is *comprehensible* — you can see the rule after a moment. That comprehension
  is the aesthetic pay-off, which is also why the *explanation* panels in this atlas are as attractive
  as the pretty ones.

Add two more ingredients that the fluency account does not fully capture, but that describe what is
happening: **scale-hierarchy** (detail at every zoom level, so exploration never ends — the fractal
appeal) and **motion/flow reading** (humans are extremely good at reading implied motion, which is why a
frozen filament pattern still looks like something pouring).

## L3 · Mathematics inside art, and art inside mathematics

* **Composition by geometry.** Linear perspective (Alberti, Piero della Francesca), proportion systems
  (Polykleitos' *Canon*, Pacioli's *De divina proportione* with Leonardo's illustrations), and the use of
  polyhedra and the camera obscura are mathematics *applied* to art.
* **Symmetry as ornament.** The classification of planar patterns (the 17 wallpaper groups) and of
  frieze patterns is, in practice, a *complete taxonomy of decorative design* — from Moroccan zellige to
  Alhambra tilings to Escher's tessellations. Group theory does not merely describe ornament; it exhausts
  it. Escher's later work goes further, into hyperbolic geometry, after his correspondence with Coxeter.
* **The golden ratio: handle with care.** The claim that ancient art and architecture were *designed*
  around $\varphi$ is repeated far more often than it is evidenced; the standard critiques (notably
  Markowsky) show that many measurements are selective, and that the ratio can be "found" in almost any
  rectangle with sufficient imagination. The defensible statement is that $\varphi$ appears in art that
  *deliberately* uses it (some Renaissance and modernist work), and in mathematics constantly.
* **Fractals and computer art.** Mandelbrot's geometry supplied both a scientific language for natural
  roughness and an aesthetic object (the Mandelbrot and Julia sets). The generative-art tradition —
  L-systems, cellular automata, reaction–diffusion textures, flow-field marbling, and now diffusion
  models — runs entirely on the observation that a simple rule plus iteration produces inexhaustible
  structure. Everything in [this atlas's figure set](../../figures/reaction-diffusion-art.svg) is a
  member of that tradition.
* **Mathematics *as* art.** Symmetry, minimality, unexpected necessity ("it *had* to be that"): the
  aesthetic of proof is real, and some of it is the same inverted-U fluency story with a longer training
  period.
* **Quantitative claims about famous paintings.** The best-known example is the analysis of *multiscale
  luminance statistics* in late Van Gogh — swirl patterns whose spatial statistics resemble turbulent
  flow. It is a genuinely interesting observation, and it is routinely over-stated. The honest reading:
  the paintings show *scale-free, directionally coherent structure* consistent with turbulent
  phenomenology; that does not establish that the painter was simulating Navier–Stokes, and it does not
  need to. See the [bibliography](../12-recurring-mechanisms/11-bibliography.md) for the reference and its
  caveats.

## L4 · Making a figure that carries an idea

Practical rules, learned from the figure factory behind this atlas (the scripts are in `scripts/figlib.py`
and `scripts/figpart*.py`, and they are worth reading as an argument about clarity):

1. **One idea per figure, stated in the title.** If the title needs a conjunction, split the figure.
2. **Colour as a *scale*, not as decoration.** Sequential palettes for magnitudes, diverging palettes for
   signed fields, hue only when the quantity is genuinely cyclic (phase, angle). Never encode two
   quantities with two unrelated colour channels unless you provide a legend that explains the mapping.
3. **Contrast beats resolution.** Vector output, thin grid lines, ink-dark axes, one bright accent for
   the quantity that matters. A figure with five bold colours carries nothing.
4. **Annotate the mechanism, not the data.** The arrows and the one-line caption are what convert a plot
   into an explanation; put them where the eye already is.
5. **Show the generative rule when you show a pattern.** The dispersion curve beside the Turing pattern,
   the phase portrait beside the time series: the second panel is the *reason*, and it is what someone
   remembers.
6. **Respect the medium.** SVG for the web, PDF for print, a raster fallback for viewers that cannot
   render either — and check the file sizes, because a beautiful figure that takes four seconds to load
   is a worse figure.