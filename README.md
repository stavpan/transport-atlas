# Panta Rhei — the Transport Atlas

*πάντα ῥεῖ — "all things flow": a layered, self-contained reference for transport phenomena, from
"what is a flux?" to fractional operators, kinetic theory, criticality, synchrony and operator learning.*

**Live site:** <https://stavpan.github.io/transport-atlas/> ·
**Source:** <https://github.com/stavpan/transport-atlas> ·
**Offline edition:** [`dist/atlas-standalone.html`](dist/atlas-standalone.html) (~10 MB, one file, no server)
— every push to `main` rebuilds and redeploys the site through `.github/workflows/pages.yml`.

This is a complete rebuild of the "comprehensive dictionary of transport phenomena"
idea, restructured as a **layered atlas of notes** rather than a flat dictionary.

---

## What makes this different

| Flat dictionary (the earlier attempt) | The Transport Atlas (this) |
|---|---|
| One big file, one difficulty level | **122 notes + 14 category indexes**, each note a 4-rung ladder from plain language to research depth (~106 000 words) |
| 17 terms in 4 hand-made buckets | **14 categories**: *beyond-PDEs*, a **Universality** part that argues the strongest version of the claim (and states its limits), a **Recurring mechanisms** part (equilibria → stability → bifurcation → chaos → criticality → scaling → duality → noise, plus an intersections map and a source-marked bibliography), and **Panta Rhei** — the theme taken seriously |
| Equations appear with no derivation | Every equation is **earned**: mechanism → dimensionless form → operator → analysis → numerics |
| Numerical behaviour described in prose | Regime maps, stability regions, error portraits, amplification factors — **generated vector figures** |
| Figure-free | **35 vector figures** + **7 animated figures** (matplotlib) + a **114-node / 335-edge concept map** (graphviz), as SVG for the web, PDF for print, animated WebP/GIF for motion, and PNG as a fallback |
| No path for a beginner | **Reading paths by level** (L1 newcomer → L4 specialist), a browsable site, an interactive **connection graph**, and client-side search |
| No cross-domain intuition | A **Bridges** category: transport in engineering, geology, biology, finance, plasmas, images, networks, quantum matter and machine learning |
| Stops at ordinary PDEs | **Beyond-PDEs**: shocks, Hamilton–Jacobi, fractional/nonlocal, memory, Cattaneo, porous medium, SPDEs, homogenisation, level sets, optimal transport & gradient flows, microcontinuum, variational inequalities, MHD/relativistic, **integrable systems, variational principles, delay** |
| Only second-order, two-variable rules | **General classification**: principal symbols, arbitrary order, arbitrary dimension, systems (symmetric hyperbolic, Petrovsky, constrained) — plus patterns from minds to markets to mathematics |
| Theory with no picture of *why it keeps happening* | **Recurring mechanisms**: the nine behaviours that ride on any transport law (equilibria, stability, bifurcation, mode coupling, chaos, criticality, scaling, duality, noise), each with its own generated figure, its failure modes, and exits marked in a cross-referenced bibliography |
| A subject, not a culture | **Panta Rhei**: Heraclitus read as a question about identity under replacement, beauty and generative pattern (chaotic-advection marbling, Turing patterns), synchrony as transport of phase density, the arrow of time, and honest case studies of cross-fertilisation that failed |

## What is actually in the box

```
122 notes across 14 categories         35 vector figures + 114-node concept map
  3 new foundations (general classification for ANY order & dimension,
                     higher order & dispersive, dimensions, geometry & manifolds)
  9 foundations    (balance law … random walks, memory)
 10 bulk fluid      (advection … turbulence, Darcy, rheology)
  8 microscopic     (Fick … anisotropic, anomalous, ionic)
 13 interaction     (kinetics … Turing, Stefan, wells, dissipation)
  6 kinetic         (Boltzmann … lattice-Boltzmann)
 16 beyond-PDEs     (shocks … MHD, integrable systems, variational
                     principles & Noether, delay & retarded transport)
 13 numerics        (discretisation … limiters, solvers, V&V, ML)
 11 bridges         (engineering … finance, biology, ML, quantum)
  9 universality    (five structures, translation lookup, cognitive science,
                     society/economics/language, algorithms, physics & QFT,
                     information & inference, mathematics itself, limits)
 11 mechanisms      (equilibria, stability, bifurcation, mode coupling, chaos,
                     criticality, scaling, duality, noise, the intersections
                     map, bibliography)
  6 panta rhei       (Heraclitus, beauty & the flow, synchrony, the arrow of
                     time, crossings, the river as a model)
  4 polysemy notes  (dispersion, convection, diffusion, absorption lingo)
  6 appendix notes  (symbols, dimensionless cards, operator catalogue,
                     key derivations, measurement, history & open problems)
```

## Build outputs

| Output | What it is |
|---|---|
| `dist/index.html` | the master note: one balance law, reading paths, the concept map and a **generated catalogue of every note** |
| `dist/notes/**/*.html` | one page per note, with sidebar navigation, on-page TOC, and prev/next |
| `dist/graph.html` | **interactive connection graph** built from the real 1100+ note-to-note links (drag, hover to isolate, click to open) |
| `dist/atlas-standalone.html` | **one self-contained file (~18 MB)**: all notes, all figures *including the seven animations*, search, MathML — the shareable edition |
| `dist/L1`, `dist/L2`, `dist/L3` | the same site with the deeper ladder rungs trimmed away (the same URLs, shallower content) |
| `dist/all-in-one.html` | every note concatenated, for reading or printing in one scroll |
| `dist/atlas.pdf` | printable build (~3.4 MB, ~320 pages) with vector figures |
| `dist/search-index.json` | drives the search box (press `/`) |


## The four levels

Every note is written as a ladder. Any note can be rendered at any depth:

| Level | Question it answers | Audience |
|---|---|---|
| **L1** | *What is it, in everyday words?* No math. | Curious beginner |
| **L2** | *Why does it happen, and what is the mathematical object?* Mechanism + the PDE term, dimensionless numbers. | Undergrad STEM |
| **L3** | *What does the mathematics guarantee?* Well-posedness, limits, spectra, asymptotic regimes, invariants. | Grad / researcher-in-training |
| **L4** | *What breaks, what is unsolved, how do you actually compute it?* Numerics, stability, open problems, cross-domain structure. | Specialist / practitioner |

The head of every note carries a **one-line picture** and a **prerequisite line** so you can
enter anywhere and walk down.

## Layout

```
transport-atlas/
├── README.md              ← you are here
├── build.py               ← pandoc-based builder (site, level mirrors, PDF, link check)
├── assets/                ← stylesheet, page template, search JS
├── notes/
│   ├── 00-atlas/          ← THE master note: brief, collects everything, auto-catalog
│   ├── 01-foundations/    ← flux, balance laws, PDE taxonomy, dimensionless numbers, entropy,
│   │                        spectral/Green function view, random walks, Langevin & response
│   ├── 02-bulk/           ← advection, convection, vorticity & pressure, boundary layers,
│   │                        turbulence, Taylor–Aris shear dispersion, mixing, jets, Darcy,
│   │                        non-Newtonian rheology
│   ├── 03-microscopic/    ← Fick, Brownian/Einstein, Fourier conduction, mass-diffusion
│   │                        coefficients, Knudsen/rarefied, Soret–Dufour–Maxwell–Stefan,
│   │                        Nernst–Planck, anomalous diffusion (CTRW)
│   ├── 04-interaction/    ← kinetics, saturation, autocatalysis, Turing, fronts, chemotaxis,
│   │                        sorption, absorption, Stefan, sedimentation, accretion, wells,
│   │                        subsidence/poroelasticity, viscous dissipation
│   ├── 05-kinetic/        ← Boltzmann, BGK/Vlasov, Fokker–Planck & Kramers, radiative
│   │                        transfer, neutron transport, lattice-Boltzmann
│   ├── 06-beyond/         ← conservation laws & shocks, Hamilton–Jacobi & viscosity
│   │                        solutions, nonlocal/fractional operators, memory & viscoelasticity,
│   │                        Cattaneo & telegraph, porous-medium & nonlinear diffusion,
│   │                        SPDEs & random media, homogenisation, free boundaries/phase fields,
│   │                        optimal transport & gradient flows, microcontinuum continua,
│   │                        variational inequalities & hysteresis, MHD & relativistic transport
│   ├── 07-numerics/       ← consistency/stability/convergence, CFL & stiffness, numerical
│   │                        diffusion, limiters/TVD/WENO, splitting & coupling, linear and
│   │                        nonlinear solvers, adaptivity & parallel decomposition, particle
│   │                        methods, inversion & data assimilation, ML/operator learning, V&V,
│   │                        structure-preserving discretisations
│   ├── 08-bridges/        ← heat–mass–momentum analogy & circuit models, finance, biology,
│   │                        geoscience & climate, plasma & astrophysics, engineering devices,
│   │                        machine learning, images & signals, society & networks,
│   │                        quantum/condensed matter, unifying mathematics
│   ├── 09-polysemy/       ← words that collide: dispersion, convection, diffusion, conduction,
│   │                        absorption vs adsorption, flux/source/sink/BC lingo
│   ├── 10-appendix/       ← symbol glossary, dimensionless-number cards, operator catalogue,
│   │                        key derivations, measurement, history & etymology, open problems
│   ├── 11-universality/   ← the five universal structures, the object→transport lookup, mind,
│   │                        society/economics/language, algorithms, physics & QFT, inference,
│   │                        mathematics itself, and the limits of the claim
│   ├── 12-recurring-mechanisms/  ← equilibria & critical points, linearisation & stability,
│   │                        bifurcation, nonlinearity & mode coupling, chaos & predictability,
│   │                        phase transitions & criticality, scaling & self-similarity,
│   │                        duality & transforms, noise-induced phenomena, the intersections
│   │                        map, and a bibliography marked primary/review/sceptical
│   └── 13-panta-rhei/     ← Heraclitus & the river, beauty & the flow, collective behaviour
│                            & synchrony, irreversibility & the arrow of time, crossings &
│                            cross-fertilisation, the river as a model
├── scripts/               ← figure generators (matplotlib + graphviz)
├── figures/               ← generated SVG / PDF / PNG
└── dist/                  ← generated site
```

## Figures and animations

Every figure is generated from a script — there are no screenshots and no hand-drawn diagrams.

```
scripts/figlib.py       the style: palette, grids, helpers (arrow/box/plain/tidy), and the
                        writers  save()  (SVG + PDF + PNG)  and  save_anim()  (WebP + GIF)
scripts/figpart1–13.py  the static figures, one module per group, each registering itself
scripts/figanim.py      the animated figures (A1–A7) plus a static *filmstrip* poster each
scripts/make_figures.py the CLI: every figure, or names, or --gifs / --list
scripts/audit_figures.py  the legibility gate (see below)
scripts/make_concept_map.py  the graphviz concept map
```

**Three formats, three jobs.** Vector `SVG` for the web, vector `PDF` for print, raster `PNG`
as a fallback — plus, for the seven animated figures, an animated `WebP` (what the site and the
vault embed; 10–30× smaller than the equivalent GIF) and a downscaled `GIF` fallback. Animations
are the phenomena that *are* motion: marbling, pattern growth, locking, shock formation, chaotic
divergence, avalanching and coarsening. In the print build each animation becomes its filmstrip,
in the single-file edition it is inlined as a data URI, and in the Obsidian vault it plays.

**The legibility gate.** `scripts/audit_figures.py` re-runs every figure, intercepts `save()`
so nothing is written, and inspects the live artists: it flags text below 8 pt, text that
matplotlib clips away, text thrown far outside the canvas, and — the defect that code review
never catches — two hand-placed labels sitting on top of each other. Findings that involve only
axis furniture (a label grazing a tick number) are printed as advisory notes and are not counted.
It exits non-zero when there is something to fix, so it can gate CI (the workflow runs it as an
advisory step, since font metrics vary between matplotlib versions):

```bash
/home/stav/.pixi/envs/sage/bin/python scripts/audit_figures.py        # quiet unless something is wrong
/home/stav/.pixi/envs/sage/bin/python scripts/audit_figures.py --verbose
```

The current state of the figure set: **0 sub-8pt labels, 0 clipped annotations, 0 collisions
between hand-placed labels**. Two classes of defect were found and fixed by this gate while it was
being written: a legend whose five swatches were all drawn at the same coordinates, and annotations
that `ax.annotate` was silently clipping at the axes edge (figlib now un-clips every annotation
before a figure is written).

**Conventions the figures follow.** One idea per figure, stated in the title; colour as a scale
rather than decoration (sequential for magnitudes, diverging for signed fields, hue only when the
quantity is genuinely cyclic); annotations that name the *mechanism* rather than the data; and a
second panel whenever a rule produces a pattern, because the rule is what people remember.

## Building

Requirements (all already present in this workspace):

* `pandoc` ≥ 3 — `/home/stav/.pixi/bin/pandoc`
* Python 3 with `matplotlib`/`numpy` for the figures, `pillow` for the animations —
  `/home/stav/.pixi/envs/sage/bin/python`
* `graphviz` (`dot`) for the concept map, `xelatex` for the PDF build

```bash
cd transport-atlas

# 1. figures (once, or after editing scripts/)
/home/stav/.pixi/envs/sage/bin/python scripts/make_figures.py
python3 scripts/make_concept_map.py

# 2. the site  →  dist/index.html
python3 build.py

# 3. also the L1/L2/L3 pedagogical mirrors
python3 build.py --levels

# 4. also the printable PDF (needs xelatex)
python3 build.py --pdf

# 5. sanity check: broken links, missing figures
python3 build.py --check

# 6. a fully offline site (math rendered as MathML, no CDN, no internet needed)
python3 build.py --levels --offline
```

## The Obsidian vault is the primary output

The same `notes/**/*.md` sources are also converted into **structured Obsidian notes** in the vault at
`~/Notes` (see `scripts/to_obsidian.py`):

```bash
cd transport-atlas
python3 scripts/to_obsidian.py --dry-run     # show the plan, write nothing
python3 scripts/to_obsidian.py               # write into ~/Notes/Transport Atlas/
python3 scripts/to_obsidian.py --vault /some/other/vault --folder "Transport Atlas"
```

It produces

```
~/Notes/Transport Atlas/
├── Transport Atlas.md              master note (MOC): the one balance law, four reading
│                                   paths, the concept map, live Dataview index, usage callout
├── Transport Atlas - Cheat Sheet.md   the whole atlas on one screen
├── Where to read more.md           the standard texts, mapped onto the parts
├── Transport Atlas.canvas          Obsidian canvas: one card per part
├── <Part> (MOC).md                 one MOC per part (12 of them)
└── <Part>/…                        the 105 notes, in part folders
~/Notes/Assets/transport/*.svg      22 vector figures, embedded with ![[name.svg]]
```

and rewrites the notes into house style: `[[wikilinks]]` with aliases, `![[figure.svg]]` embeds with
italic captions, Obsidian **callouts** (`> [!abstract] In one line`, `> [!info] Where this note sits`,
`> [!warning] Trap`, `> [!question]- Check yourself`), **🔬 L3/L4** headings for the rigorous rungs,
front-matter properties (`tags`, `type`, `up`, `part`, `level`, `summary`, `aliases`) and a
Dataview-driven index. Running it again after editing the sources regenerates everything in place.


Then open `dist/index.html` in a browser.

## Sharing and hosting (free, in order of effort)

Four ways, from "send a file" to "a live URL that updates itself".

**1 · One file, no server (works right now).** `dist/atlas-standalone.html` (≈6 MB) contains every
note, every figure and the search box, with maths rendered as MathML and no CDN. Email it, put it on a
USB stick, drop it in Drive — it opens offline in any browser. Attach the figures folder instead if you
prefer the full site: `dist/` is a completely static folder, so `python3 -m http.server -d dist` (or
`npx serve dist`) is all a local server needs.

**2 · Share on your local network** (same Wi-Fi, instantly):

```bash
python3 -m http.server -d dist 8000      # then open http://<your-ip>:8000/
hostname -I                              # to print your IP
```

**3 · Drag-and-drop static hosts** (free tier, no CLI): upload the whole of `dist/` to
[Netlify Drop](https://app.netlify.com/drop), [Cloudflare Pages](https://pages.cloudflare.com/) or
[Vercel](https://vercel.com/new) — you get a public link in seconds. No build step is needed because
`dist/` is already static; if you *do* let them build, the commands are
`python build.py --levels --standalone` (a `netlify.toml`/`vercel.json` is unnecessary).

Instant link without any account, straight from the shell (the file becomes publicly downloadable —
it contains only your own notes):

```bash
curl -F "file=@dist/atlas-standalone.html" https://0x0.st     # prints a public URL
```

**4 · GitHub Pages, live and self-updating** (needs one login):

```bash
gh auth login                 # once, if the token in ~/.config/gh is stale
./scripts/publish.sh          # builds, creates the repo, pushes, enables Pages
# → https://<your-user>.github.io/transport-atlas/
```

`scripts/publish.sh` builds the site, initialises a repository if needed, pushes it, and switches
GitHub Pages to the *GitHub Actions* source. The workflow in `.github/workflows/pages.yml` then rebuilds
the figures, the concept map, the graph page and the standalone file on every push — so the URL is always
the current version of the notes. To publish somewhere else instead:

```bash
REPO=youruser/your-repo ./scripts/publish.sh
```

> [!note] Why the site is static
> Everything is generated by `build.py` from the same `notes/**/*.md` that feed the Obsidian vault, so
> there is no server-side anything to maintain: git, a folder, or a single HTML file are all the
> infrastructure the atlas needs.

## Authoring conventions

* One note = one `.md` file under `notes/<category>/`, named `NN-slug.md` (`NN` sets order).
* YAML front matter: `title`, `blurb` (one sentence — feeds the catalog *and* the search box),
  `category`, `depth` (1–4: the level from which the note starts being useful), `tags`.
* Ladder sections **must** be headed `## L1 · …`, `## L2 · …`, `## L3 · …`, `## L4 · …` so the
  builder can trim them. Non-ladder sections (`## Words that collide`, `## See also`, …) are
  always kept.
* Figures: `![**Figure N.** caption](../figures/name.svg)` — the builder switches `.svg` → `.pdf`
  for the print build automatically.
* Callouts are blockquotes with a bold label — `> **Trap.** …` — because those survive both
  HTML and LaTeX.
* Cross-link freely with relative `.md` links; the builder rewrites them to `.html`.
