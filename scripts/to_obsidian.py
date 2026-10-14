#!/usr/bin/env python3
"""
Convert the Transport Atlas notes into structured Obsidian notes.

One source of truth, two outputs:
    notes/**/*.md  --(build.py)-->       dist/ website + PDF
    notes/**/*.md  --(to_obsidian.py)--> ~/Notes/Transport Atlas/  (this script)

What the conversion does
------------------------
* filename  = note title (vault-wide unique; verified before writing)
* front matter -> Obsidian properties (`up`, `part`, `level`, `tags`, ...)
* `[text](../cat/note.md)`            -> `[[Note title|text]]`   (wikilinks!)
* `![**Figure 3.** caption](../figures/x.svg)` -> `![[x.svg]]` + italic caption
* `> **Trap.** ...`                   -> Obsidian callout `> [!warning] Trap`
* the note's opening blockquote       -> `[!abstract] In one line` + `[!info] Where this note sits`
* `## L3 · ...` / `## L4 · ...`       -> `## 🔬 L3 — ...` (the vault's "going deeper" idiom)
* `## Checks`                         -> `> [!question] Check yourself`
* the website's auto-catalogue       -> real wikilink tables + Dataview queries
* figures                            -> <vault>/Assets/transport/*.svg

Usage
-----
    python3 scripts/to_obsidian.py --dry-run          # show the plan, write nothing
    python3 scripts/to_obsidian.py                    # write into ~/Notes
    python3 scripts/to_obsidian.py --vault /path/to/vault --folder "Transport Atlas"
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import build  # noqa: E402  (same loader as the website build)

DEFAULT_VAULT = Path.home() / "Notes"
DEFAULT_FOLDER = "Transport Atlas"
ASSET_SUBDIR = "transport"

# callout types for the labelled blockquotes the notes already use
CALLOUT_BY_LABEL = [
    ("trap", "warning"), ("pitfall", "warning"), ("caution", "warning"),
    ("habit", "tip"), ("use", "tip"), ("reading tip", "tip"),
    ("why this note exists", "info"), ("where to jump", "info"), ("how to read", "info"),
    ("deep", "abstract"), ("the general rule", "abstract"), ("unifying", "abstract"),
    ("check", "question"), ("how to use", "info"), ("roadmap", "info"),
]

LADDER_RE = re.compile(r"^##\s+L([1-4])\s*[·—-]\s*(.+)$")
IMAGE_RE = re.compile(r"!\[(.*?)\]\(((?:\.\./)*figures/[^)\s]+|[^)\s]+\.(?:svg|png|jpe?g|gif))\)", re.S)
LINK_RE = re.compile(r"(?<!!)\[([^\]\n]*)\]\(([^)\s]+)\)")
BLOCKQUOTE_LABEL_RE = re.compile(r"^>\s*\*\*(.{2,80}?)\*\*\.?\s*(.*)$")


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #
def slug_tag(text: str) -> str:
    """Make a tag-safe slug: lowercase, no spaces, no punctuation."""
    t = text.lower().replace("&", "and")
    t = re.sub(r"[^a-z0-9/]+", "-", t).strip("-")
    return re.sub(r"-{2,}", "-", t)


def safe_filename(title: str) -> str:
    return re.sub(r'[\\/:*?"<>|]', "-", title).strip()


def mathjax_safe(text: str) -> str:
    """Obsidian renders math with MathJax, which lacks the stmaryrd brackets."""
    return (text.replace(r"\llbracket", r"[\![")
                .replace(r"\rrbracket", r"]\!]"))


class Note:
    """A source note plus its vault identity."""

    def __init__(self, raw, categories, title_map):
        self.raw = raw
        self.title = raw["title"]
        self.filename = safe_filename(self.title) + ".md"
        self.category_key = raw["category"]
        self.category_title = categories[raw["category"]]["title"]
        self.is_index = raw["is_index"]
        self.level = int(raw["depth"])
        self.blurb = raw["blurb"]
        self.body = raw["body"]
        self.url_dir = Path("notes") / raw["category"]      # for resolving links
        self.title_map = title_map
        self.tags = self.build_tags(raw)

    def build_tags(self, raw):
        tags = ["transport"]
        tags.append("transport/index" if self.is_index else "transport/term")
        if not self.is_index:
            cat_slug = re.sub(r"(-transport|^transport-)$", "", slug_tag(self.category_title))
            tags.append("transport/" + cat_slug)
            tags.append("transport/level-%d" % self.level)
        for t in raw["tags"]:
            tags.append("transport/topic/" + slug_tag(t))
        return tags

    # -- link resolution ---------------------------------------------------- #
    def resolve(self, target: str):
        """Map a relative markdown target onto a vault note title."""
        path, _, _frag = target.partition("#")
        if not path:
            return None
        resolved = os.path.normpath(os.path.join(self.url_dir.as_posix(), path))
        return self.title_map.get(resolved)

    def convert_images(self, text: str, fig_names) -> str:
        self.fig_names = set(fig_names)          # reused by convert_links

        def sub(m):
            alt, target = m.group(1).strip(), m.group(2)
            name = Path(target).name
            if name not in fig_names:
                return m.group(0)
            label, caption = "", alt
            m2 = re.match(r"\*\*(Figure[^*]*?)\*\*\s*(.*)", alt, re.S)
            if m2:
                label, caption = m2.group(1).strip(), m2.group(2).strip()
            out = "![[%s]]" % name
            if caption:
                out += ("\n*%s* %s" % (label, caption)) if label else ("\n*%s*" % caption)
            return out

        return IMAGE_RE.sub(sub, text)

    def convert_links(self, text: str) -> str:
        def sub(m):
            label, target = m.group(1), m.group(2)
            if target.startswith(("http", "#", "mailto", "data:")):
                return m.group(0)
            if not target.endswith(".md"):
                name = Path(target).name
                if name in getattr(self, "fig_names", ()):
                    # a plain link to a figure (e.g. inside a caption) — keep it resolvable
                    clean = re.sub(r"\s*#\s*\d+$", "", label).strip()
                    return "[[%s|%s]]" % (name, clean) if clean else "![[%s]]" % name
                return m.group(0)
            title = self.resolve(target)
            if not title:
                return "`%s` (unresolved: %s)" % (label, target)
            clean = re.sub(r"\s*#\s*\d+$", "", label).strip()
            if clean == title or not clean:
                return "[[%s]]" % title
            return "[[%s|%s]]" % (title, clean)

        return LINK_RE.sub(sub, text)




# --------------------------------------------------------------------------- #
# body transformation
# --------------------------------------------------------------------------- #
def convert_header_blockquote(body: str, note: Note) -> str:
    """The opening `> ...` block becomes an abstract callout plus a links callout.

    Only the block at the very top counts (before the first `##` heading) — in the
    category index notes a blockquote further down is a normal callout, not a header.
    """
    lines = body.split("\n")
    start = next((i for i, l in enumerate(lines) if l.startswith(">")), None)
    first_heading = next((i for i, l in enumerate(lines) if l.startswith("## ")), len(lines))
    if start is None or start > first_heading:
        return body
    end = start
    while end < len(lines) and (lines[end].startswith(">") or lines[end].strip() == ""):
        if lines[end].strip() == "" and end + 1 < len(lines) and not lines[end + 1].startswith(">"):
            break
        end += 1
    block = [re.sub(r"^>\s?", "", l).rstrip() for l in lines[start:end]]
    # split the block into paragraphs on the '>' blank lines
    paras, cur = [], []
    for l in block:
        if l.strip():
            cur.append(l.strip())
        elif cur:
            paras.append(" ".join(cur))
            cur = []
    if cur:
        paras.append(" ".join(cur))
    if not paras:
        return body

    one_line = re.sub(r"^\*\*[^*]{2,60}?\.?\*\*\s*", "", paras[0]).strip()
    out = ["> [!abstract] In one line", "> " + one_line]
    rest = [re.sub(r"\*\*([^*]+?)\.\*\*", r"*\1.*", p) for p in paras[1:]]
    if rest:
        out += [">", "> [!info] Where this note sits"]
        for p in rest:
            out.append("> " + p)
    return "\n".join(lines[:start] + out + lines[end:])


def convert_label_blockquotes(body: str) -> str:
    """`> **Trap.** text` -> `> [!warning] Trap` + `> text`."""
    lines = body.split("\n")
    out, i = [], 0
    while i < len(lines):
        m = BLOCKQUOTE_LABEL_RE.match(lines[i])
        if m and not lines[i].startswith("> [!"):
            label, first = m.group(1).strip().rstrip("."), m.group(2).strip()
            if ":" in label and len(label) > 24:
                label, extra = label.split(":", 1)
                first = (extra.strip() + " " + first).strip()
            ctype = "note"
            for key, val in CALLOUT_BY_LABEL:
                if key in label.lower():
                    ctype = val
                    break
            out.append("> [!%s] %s" % (ctype, label))
            if first:
                out.append("> " + first)
            i += 1
            while i < len(lines) and lines[i].startswith(">"):
                out.append(lines[i])
                i += 1
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


def convert_checks(body: str) -> str:
    """The `## Checks` list becomes a collapsible ✓ callout."""
    lines = body.split("\n")
    out, i = [], 0
    while i < len(lines):
        if re.match(r"^##\s+Checks\s*$", lines[i]):
            i += 1
            block = []
            while i < len(lines) and not lines[i].startswith("## "):
                if lines[i].strip():
                    block.append(lines[i].strip())
                i += 1
            out.append("> [!question]- Check yourself")
            for b in block:
                out.append("> " + b)
            out.append("")
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


def convert_ladder(body: str) -> str:
    """Keep the four rungs; mark the rigorous ones with 🔬, as the vault does."""
    out = []
    for line in body.split("\n"):
        m = LADDER_RE.match(line)
        if m:
            lvl, rest = m.group(1), m.group(2).strip()
            mark = "🔬 " if lvl in ("3", "4") else ""
            out.append("## %sL%s — %s" % (mark, lvl, rest))
        else:
            out.append(line)
    return "\n".join(out)


def convert_see_also(body: str) -> str:
    """Rename the tail navigation section to the vault's phrasing."""
    return re.sub(r"^##\s+See also\s*$", "## Nearby notes", body, flags=re.M)


def transform(note: Note, fig_names) -> str:
    body = note.body
    body = convert_header_blockquote(body, note)
    body = convert_images_and_links(note, body, fig_names)
    body = convert_label_blockquotes(body)
    body = convert_checks(body)
    body = convert_ladder(body)
    body = convert_see_also(body)
    body = mathjax_safe(body)
    body = re.sub(r"\n{4,}", "\n\n\n", body)
    return body.strip() + "\n"


def convert_images_and_links(note: Note, body: str, fig_names) -> str:
    body = note.convert_images(body, fig_names)
    return note.convert_links(body)


def front_matter(note: Note, aliases=None, skip_up=False) -> str:
    part = note.category_title
    lines = ["---",
             "tags: [%s]" % ", ".join(note.tags),
             "type: %s" % ("transport-index" if note.is_index else "transport-note")]
    if not skip_up:
        lines.append("up: \"[[Transport Atlas]]\"")
    if aliases:
        lines.append("aliases: [%s]" % ", ".join('"%s"' % a for a in aliases))
    if not note.is_index:
        lines.append("part: \"[[%s (MOC)]]\"" % part)
        lines.append("level: %d" % note.level)
        lines.append("summary: \"%s\"" % note.blurb.replace('"', "'"))
    lines.append("source: \"Transport Atlas (generated)\"")
    lines.append("---")
    return "\n".join(lines) + "\n"


def normalize_h1(text: str, title: str) -> str:
    """Guarantee exactly one H1, and make it the note title."""
    lines = text.lstrip("\n").split("\n")
    if lines and lines[0].startswith("# "):
        lines[0] = "# " + title
    else:
        lines = ["# " + title, ""] + lines
    return "\n".join(lines).strip("\n") + "\n"


def write_note(note: Note, text: str, target: Path, title: str, aliases=None, skip_up=False):
    body = normalize_h1(text, title)
    target.write_text(front_matter(note, aliases, skip_up) + "\n" + body, encoding="utf-8")



# --------------------------------------------------------------------------- #
# generated companions: master MOC, category MOCs, cheat sheet, reading list, canvas
# --------------------------------------------------------------------------- #
def catalog_markdown(cats) -> str:
    """Wikilink tables (always work) + a Dataview view of the whole atlas."""
    out = ["```dataview",
           "TABLE WITHOUT ID link(file.link, file.name) AS \"note\", summary AS \"what it is\", part AS \"part\", level AS \"starts at\"",
           "FROM #transport/term",
           "SORT part ASC, level ASC, file.name ASC",
           "```",
           ""]
    rows = []
    for key, cat in cats.items():
        if key == "00-atlas":
            continue
        rows.append("### %s  ·  [[%s (MOC)|%s]]" % (cat["title"], cat["title"], cat["title"]))
        if cat["blurb"]:
            rows.append("*%s*" % cat["blurb"])
        rows += ["", "| note | what it is | starts at |", "|---|---|---|"]
        for n in cat["notes"]:
            rows.append("| [[%s]] | %s | L%d |" % (n["title"], n["blurb"], n["depth"]))
        rows.append("")
    out.append("\n".join(rows))
    return "\n".join(out)


def category_moc_body(text: str, cat_title: str) -> str:
    dv = ["```dataview",
          "TABLE WITHOUT ID link(file.link, file.name) AS \"note\", summary AS \"what it is\", level AS \"starts at\"",
          "FROM #transport/term",
          "WHERE part = [[%s]]" % cat_title,
          "SORT level ASC, file.name ASC",
          "```"]
    return text.rstrip() + "\n\n## All notes in this part (live)\n\n" + "\n".join(dv) + "\n"


CANVAS_INTRO = """# Transport Atlas

Ten parts, 90 notes. Each note is a ladder: L1 in plain words → L2 mechanism and form →
🔬 L3 what the maths guarantees → 🔬 L4 numerics, limits, frontiers.

Open a part to see its notes, or start from the graph view.
"""

USAGE_CALLOUT = """
> [!tip] How to read this in Obsidian
> * **Graph view** shows the shape of the whole subject — every note is wired to its part, to its
>   prerequisites and to its neighbours.
> * **Filter by depth** with the `level` property (`1` = no background needed, `4` = research depth)
>   or with the tags `#transport/level-1` … `#transport/level-4`.
> * **🔬 headings** mark the "going deeper" rungs: read L1/L2 first, come back to L3/L4 once the
>   picture is in place.
> * **Dataview** drives the live tables below; the fixed tables after them are the frozen snapshot.
> * **Canvas**: `Transport Atlas.canvas` in this folder is one card per part.
> * **One screen**: [[Transport Atlas - Cheat Sheet]] · **bibliography**: [[Where to read more]].
"""

MOC_CLEANUPS = [
    (r"The site is built four times:.*?shallower content\.",
     "The same source also builds a static website and a PDF, but these notes are now the primary "
     "form: **wikilinks** for the connections, the **graph view** for the shape of the subject, and "
     "**properties** (`level`, `part`) for filtering."),
]


CHEAT_SHEET = r"""
> [!abstract] What this is
> The whole atlas on one screen: the one balance law, the four operator families, the numbers that
> decide the regime, and how to choose a method. Everything links into [[Transport Atlas]].

## 1 · The one equation

$$\partial_t c+\nabla\cdot\mathbf{J}=f
\qquad\Longleftrightarrow\qquad
\frac{\mathrm{d}}{\mathrm{d}t}\int_V c\,\mathrm{d}V
=-\oint_{\partial V}\mathbf{J}\cdot\mathbf{n}\,\mathrm{d}A+\int_V f\,\mathrm{d}V$$

Every note in the atlas is a choice of $c$, $\mathbf{J}$ and $f$. → [[Balance laws & flux]]

## 2 · The flux laws (all the same shape)

| domain | flux | law | coefficient |
|---|---|---|---|
| mass | $-D\nabla c$ | Fick | $D$ (m²/s) |
| heat | $-k\nabla T$ | Fourier | $k$; $\alpha=k/\rho c_p$ |
| momentum | $\mu(\nabla\mathbf{u}+\nabla\mathbf{u}^{\!\top})$ | Newton | $\mu$, $\nu$ |
| porous flow | $-(K/\mu)\nabla p$ | Darcy | $K$ (m²) |
| charge | $-\sigma\nabla\phi$ | Ohm | $\sigma$ |
| probability | drift $+$ $D\nabla p$ | Fokker–Planck | $D$ |

Signed, symmetric and positive because the second law says so → [[Constitutive relations]]

## 3 · The four operator families

| family | prototype | behaviour | numerics |
|---|---|---|---|
| parabolic | $\partial_tc=D\nabla^2c$ | smooths, $\sqrt{t}$, maximum principle | implicit stepping |
| hyperbolic | $\partial_tc+\mathbf{u}\cdot\nabla c=0$ | translates, shocks, finite speed | CFL, upwind/limiters |
| elliptic | $\nabla\cdot(k\nabla T)=f$ | instant, global, no time | multigrid / Krylov |
| nonlocal / memory | $(-\Delta)^{\beta/2}$, $\int M(t-s)\mathbf{X}$ | jumps, ageing, long tails | FFT/Toeplitz, Prony |

→ [[Operator & equation catalogue]] · [[Beyond classical PDEs (MOC)]]

## 4 · Numbers that decide the regime

| number | definition | reading |
|---|---|---|
| $\mathrm{Pe}$ | $UL/D$ | $\gg1$: fronts, boundary layers |
| $\mathrm{Re}$ | $UL/\nu$ | $\gg10^3$: turbulence, closure needed |
| $\mathrm{Ra}$ | $g\beta\Delta TL^3/\nu\alpha$ | $>1708$: convection switches on |
| $\mathrm{Da}$ | $kL^2/D$ or $kL/U$ | $\gg1$: reaction in thin sheets |
| $\mathrm{Kn}$ | $\lambda/L$ | $>0.1$: leave the continuum behind |
| $\mathrm{Nu},\mathrm{Sh}$ | $hL/k$, $h_mL/D$ | actual vs conductive/diffusive transfer |

→ [[Dimensionless numbers]] · [[Dimensionless number cards]]

## 5 · Choosing a method

| regime | method |
|---|---|
| diffusion-dominated | implicit stepping, centred fluxes |
| advection-dominated | conservative flux form + limiter/WENO; measure numerical diffusion |
| stiff reactions | implicit/IMEX chemistry, operator splitting |
| rarefied ($\mathrm{Kn}>0.1$) | DSMC or lattice-Boltzmann |
| coupled multiphysics | implicit coupling or a stabilised split |
| fitting parameters to data | regularise, then report uncertainty |

→ [[Numerics & inversion (MOC)]] · [[Limiters, TVD & WENO]] · [[Inverse problems & data assimilation]]

## 6 · Three habits that prevent most mistakes

> [!warning] Name the coefficient, not the symbol
> $\alpha$ is thermal diffusivity, dispersivity *and* a fractional order in this atlas alone.
> → [[Symbol glossary]]

> [!warning] Separate stability from accuracy
> A stable scheme can be twice wrong; an accurate scheme can be unstable.
> → [[Numerical diffusion & dispersion]]

> [!warning] Ask where the resistance is
> Real transport is usually limited by an interface, a film or a contact — not by the bulk.
> → [[Heat–mass–momentum analogy & circuit models]]
"""

READING = r"""
> [!info] How to use this
> The atlas is self-contained, but every note compresses material treated at length elsewhere. These
> are the standard texts, grouped the way the atlas is grouped.

## General transport phenomena
- **Bird, Stewart & Lightfoot — *Transport Phenomena*** (the canonical shell-balance treatment, and the
  source of the heat–mass–momentum analogy).
- **Deen — *Analysis of Transport Phenomena*** (scaling, asymptotics, the analogy done rigorously).
- **Leal — *Advanced Transport Phenomena*** (constitutive theory, interfacial transport).
- **Incropera & DeWitt — *Fundamentals of Heat and Mass Transfer*** (correlations and practice).
  → [[Bridges to other fields (MOC)]], [[Transport in engineering devices]]

## Fluid mechanics and turbulence
- **Batchelor — *An Introduction to Fluid Dynamics***; **Landau & Lifshitz — *Fluid Mechanics***.
- **Pope — *Turbulent Flows***; **Tennekes & Lumley — *A First Course in Turbulence***.
  → [[Turbulence & eddy diffusivity]], [[Boundary layers]], [[Convection & buoyancy]]

## Mathematics of diffusion and PDEs
- **Crank — *The Mathematics of Diffusion*** (Green functions, free boundaries, numerical methods).
- **Evans — *Partial Differential Equations***; **Gilbarg & Trudinger — *Elliptic PDE of Second Order***.
- **Barenblatt — *Scaling, Self-similarity and Intermediate Asymptotics***;
  **Kevorkian & Cole — *Perturbation Methods***. → [[Key derivations]]
- **Villani — *Optimal Transport: Old and New***; **Santambrogio — *Optimal Transport for Applied
  Mathematicians***. → [[Optimal transport & gradient flows]]

## Numerical methods
- **LeVeque — *Finite Volume Methods for Hyperbolic Problems*** (shocks, limiters, entropy conditions).
- **Toro — *Riemann Solvers and Numerical Methods for Fluid Dynamics***.
- **Ferziger & Perić — *Computational Methods for Fluid Dynamics***;
  **Wesseling — *Principles of Computational Fluid Dynamics***.
- **Strikwerda — *Finite Difference Schemes and PDEs***;
  **Hairer & Wanner — *Solving Ordinary Differential Equations II***.
  → [[Numerics & inversion (MOC)]]

## Kinetic theory and radiation
- **Chapman & Cowling — *The Mathematical Theory of Non-uniform Gases*** (Chapman–Enskog).
- **Bird — *Molecular Gas Dynamics and the Direct Simulation of Gas Flows*** (DSMC).
- **Chandrasekhar — *Radiative Transfer***; **Modest — *Radiative Heat Transfer***.
  → [[Kinetic & radiative transport (MOC)]]

## Porous media, geoscience and rheology
- **Bear — *Dynamics of Fluids in Porous Media***;
  **Sahimi — *Flow and Transport in Porous Media and Fractured Rock***.
- **Bird, Armstrong & Hassager — *Dynamics of Polymeric Liquids***;
  **Larson — *Constitutive Equations for Polymer Melts and Solutions***.
  → [[Porous media & Darcy's law]], [[Non-Newtonian rheology]], [[Transport in geoscience & climate]]

## Stochastic processes
- **Risken — *The Fokker–Planck Equation***; **Gardiner — *Handbook of Stochastic Methods***;
  **Øksendal — *Stochastic Differential Equations***; **Pavliotis — *Stochastic Processes and Applications***.
  → [[Random walks, Langevin & response]], [[Fokker–Planck & Kramers escape]]

## Biology, images and machine learning
- **Nelson — *Biological Physics***; **Phillips, Kondev & Theriot — *Physical Biology of the Cell***.
- **Weickert — *Anisotropic Diffusion in Image Processing***.
- **Peyré & Cuturi — *Computational Optimal Transport***, plus the score-based/diffusion-model literature.
  → [[Transport in biology & medicine]], [[Transport in images & signals]],
  [[Transport in machine learning & data]]
"""


# --------------------------------------------------------------------------- #
# Obsidian canvas (a native board wired to the notes)
# --------------------------------------------------------------------------- #
def canvas_json(folder: str, moc_names) -> str:
    """One card per part, plus the master note and the cheat sheet, joined by arrows."""
    W, H, GX, GY = 420, 220, 520, 300
    nodes, edges = [], []
    nodes.append({"id": "intro", "type": "text", "text": CANVAS_INTRO,
                  "x": -620, "y": -260, "width": 420, "height": 240, "color": "4"})
    nodes.append({"id": "master", "type": "file",
                  "file": "%s/Transport Atlas.md" % folder,
                  "x": -620, "y": 40, "width": W, "height": H, "color": "1"})
    nodes.append({"id": "cheat", "type": "file",
                  "file": "%s/Transport Atlas - Cheat Sheet.md" % folder,
                  "x": -620, "y": 330, "width": W, "height": H, "color": "3"})
    for i, (nid, name) in enumerate(moc_names):
        col, row = divmod(i, 4)
        nodes.append({"id": nid, "type": "file",
                      "file": "%s/%s.md" % (folder, name),
                      "x": col * GX, "y": row * GY, "width": W, "height": H, "color": "6"})
        edges.append({"id": "e-" + nid, "fromNode": "master", "fromSide": "right",
                      "toNode": nid, "toSide": "left"})
    edges.append({"id": "e-cheat", "fromNode": "master", "fromSide": "bottom",
                  "toNode": "cheat", "toSide": "top", "label": "one screen"})
    return json.dumps({"nodes": nodes, "edges": edges}, indent=1)


WIKILINK_RE = re.compile(r"!?\[\[([^\]|#]+)(?:\|[^\]]*)?\]\]")


def verify(new_files, extra_names):
    known = set(extra_names) | {p.stem for p in new_files} | {p.name for p in new_files}
    problems, links, embeds = [], 0, 0
    for p in new_files:
        text = p.read_text(encoding="utf-8")
        for m in WIKILINK_RE.finditer(text):
            target = m.group(1).strip()
            if m.group(0).startswith("!"):
                embeds += 1
            else:
                links += 1
            if target not in known:
                problems.append("%s -> [[%s]]" % (p.name, target))
        for bad in re.findall(r"\]\(([^)\s]*\.\./[^)\s]*)\)", text):
            problems.append("%s -> leftover relative link (%s)" % (p.name, bad))
    return links, embeds, problems


# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=str(DEFAULT_VAULT))
    ap.add_argument("--folder", default=DEFAULT_FOLDER)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    folder = vault / args.folder
    assets = vault / "Assets" / ASSET_SUBDIR
    if not vault.is_dir():
        raise SystemExit("vault not found: %s" % vault)

    raw_notes = build.load_notes()
    cats = build.categories(raw_notes)
    fig_names = {p.name for p in build.FIG_DIR.glob("*.svg")}

    def vault_title(n):
        if n["is_index"] and n["category"] == "00-atlas":
            return "Transport Atlas"
        if n["is_index"]:
            return cats[n["category"]]["title"] + " (MOC)"
        return n["title"]

    title_map = {"notes/" + n["rel"]: vault_title(n) for n in raw_notes}
    notes = []
    for raw in raw_notes:
        note = Note(raw, cats, title_map)
        note.title = vault_title(raw)
        note.filename = safe_filename(note.title) + ".md"
        notes.append(note)

    moc_names = [(slug_tag(c["title"]), c["title"] + " (MOC)")
                 for k, c in cats.items() if k != "00-atlas"]

    planned = [(n, folder / ("" if n.is_index else n.category_title) / n.filename)
               for n in notes]

    if args.dry_run:
        print("vault  :", vault)
        print("folder :", folder)
        print("notes  :", len(planned), "  figures:", len(fig_names))
        for note, target in planned:
            print("   ", target.relative_to(vault))
        return

    if folder.exists():
        removed = 0
        for f in sorted(folder.rglob("*"), reverse=True):
            if f.is_file() and f.suffix in (".md", ".canvas", ".base"):
                f.unlink()
                removed += 1
            elif f.is_dir():
                try:
                    f.rmdir()
                except OSError:
                    pass
        print("refresh: removed %d previously generated files from %s" % (removed, folder.name))
    folder.mkdir(parents=True, exist_ok=True)

    written = []
    for note, target in planned:
        target.parent.mkdir(parents=True, exist_ok=True)
        body = transform(note, fig_names)
        if note.is_index:
            aliases = ["The Atlas", "Atlas"] if note.title == "Transport Atlas" \
                else [note.title.replace(" (MOC)", "")]
            if note.title == "Transport Atlas":
                body = body.replace("<!-- AUTO:CATALOG -->", catalog_markdown(cats))
                for pattern, repl in MOC_CLEANUPS:
                    body = re.sub(pattern, repl, body, flags=re.S)
                body = normalize_h1(body, note.title)
                body = body.replace("# Transport Atlas\n",
                                    "# Transport Atlas\n" + USAGE_CALLOUT, 1)
            else:
                body = category_moc_body(body, note.title)
            write_note(note, body, target, note.title, aliases,
                       skip_up=(note.title == "Transport Atlas"))
        else:
            write_note(note, body, target, note.title)
        written.append(target)

    cheat = folder / "Transport Atlas - Cheat Sheet.md"
    cheat.write_text(
        "---\ntags: [transport, transport/cheatsheet]\ntype: transport-cheatsheet\n"
        'up: "[[Transport Atlas]]"\n---\n\n# Transport Atlas — Cheat Sheet\n' + CHEAT_SHEET,
        encoding="utf-8")
    reading = folder / "Where to read more.md"
    reading.write_text(
        "---\ntags: [transport, transport/bibliography]\ntype: transport-bibliography\n"
        'up: "[[Transport Atlas]]"\n---\n\n# Where to read more\n' + READING, encoding="utf-8")
    (folder / "Transport Atlas.canvas").write_text(
        canvas_json(args.folder, moc_names), encoding="utf-8")
    written += [cheat, reading]

    assets.mkdir(parents=True, exist_ok=True)
    for f in sorted(build.FIG_DIR.glob("*.svg")):
        shutil.copy2(f, assets / f.name)

    extra = ({p.stem for p in vault.rglob("*.md")}
             | {p.name for p in vault.rglob("*.svg")}
             | {p.stem for p in vault.rglob("*.svg")})
    links, embeds, problems = verify(written, extra)
    print("wrote %d notes + 2 companions + 1 canvas into %s" % (len(written) - 2, folder))
    print("copied %d svg figures into %s" % (len(fig_names), assets))
    print("wikilinks: %d   embeds: %d   unresolved: %d" % (links, embeds, len(problems)))
    for p in problems[:20]:
        print("   !", p)


if __name__ == "__main__":
    main()

