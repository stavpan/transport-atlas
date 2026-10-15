#!/usr/bin/env python3
"""
Build the Transport Atlas.

Produces (all under dist/):
    index.html                       the master (brief) note + auto-generated catalog
    notes/<category>/<slug>.html     one page per note
    figures/, assets/                copied resources
    search-index.json                client-side search index
    L1/ L2/ L3/                      level-trimmed mirrors of the whole site (--levels)
    all-in-one.html                  every note in one long page
    atlas.pdf                        printable build (--pdf, needs xelatex)

Usage:
    python3 build.py                # full HTML build
    python3 build.py --levels       # + L1/L2/L3 mirrors
    python3 build.py --all          # + all-in-one + levels + pdf
    python3 build.py --pdf
    python3 build.py --check        # link / figure audit only
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NOTES_DIR = ROOT / "notes"
FIG_DIR = ROOT / "figures"
ASSETS = ROOT / "assets"
DIST = ROOT / "dist"
PANDOC = shutil.which("pandoc") or "/home/stav/.pixi/bin/pandoc"

LEVEL_LABELS = {
    1: "L1 · the plain picture",
    2: "L2 · mechanism & form",
    3: "L3 · analysis & guarantees",
    4: "L4 · numerics, limits & frontiers",
}

DEPTH_TITLES = {
    1: "L1 · the plain picture — everyday words, no mathematics",
    2: "L2 · mechanism & form — the term in the equation, the dimensionless number",
    3: "L3 · analysis & guarantees — well-posedness, spectra, limits, invariants",
    4: "L4 · numerics, limits & frontiers — what breaks, how to compute it, what is open",
}

MIRRORS = False   # set by main(): only link to the level mirrors when they were built


def depth_switch(url: str, root: str, level: int, mirrors: bool) -> str:
    """Topbar control: the depth you are reading, and how to reach the others.

    The full build contains *every* rung, so its item is labelled `all` — a topbar reading
    "L4 · numerics, limits & frontiers" on the front page was misleading: it is a description
    of the deepest rung, not of what that page contains.
    """
    if not mirrors:
        return ('<span class="lvl-badge" title="%s">%s</span>'
                % (DEPTH_TITLES[level], LEVEL_LABELS[level]))
    base = root if level == 4 else root + "/.."      # one level up when inside a mirror
    out = ['<nav class="depth" aria-label="Depth of this rendering">',
           '<span class="depth-label">depth</span>']
    for k in (1, 2, 3):
        on = ' class="on" aria-current="page"' if k == level else ""
        out.append('<a%s href="%s/L%d/%s" title="%s">L%d</a>'
                   % (on, base, k, url, DEPTH_TITLES[k], k))
    on = ' class="on" aria-current="page"' if level == 4 else ""
    out.append('<a%s href="%s/%s" title="%s">all (L1–L4)</a>'
               % (on, base, url, DEPTH_TITLES[4]))
    out.append("</nav>")
    return "".join(out)

KATEX_HEAD = (
    '<link rel="stylesheet" crossorigin="anonymous" '
    'href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">\n'
    '<script defer crossorigin="anonymous" '
    'src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>\n'
    '<script defer crossorigin="anonymous" '
    'src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" '
    "onload=\"renderMathInElement(document.body,{delimiters:["
    "{left:'$$',right:'$$',display:true},{left:'\\\\[',right:'\\\\]',display:true},"
    "{left:'\\\\(',right:'\\\\)',display:false}],throwOnError:false});\"></script>"
)

FM_RE = re.compile(r"^---[ \t]*\n(.*?)\n---[ \t]*\n", re.S)
LADDER_RE = re.compile(r"^##\s+L([1-4])\b", re.M)


def parse_front_matter(text: str):
    """Return (meta dict, body str). Minimal YAML: scalars and [a, b] lists."""
    m = FM_RE.match(text)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, val = line.split(":", 1)
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            items = [v.strip().strip("'\"") for v in val[1:-1].split(",")]
            meta[key.strip()] = [v for v in items if v]
        else:
            meta[key.strip()] = val.strip().strip("'\"")
    return meta, text[m.end():]


def load_notes():
    """All note files, sorted by category, index first, then numeric prefix."""
    notes = []
    for path in sorted(NOTES_DIR.rglob("*.md")):
        meta, body = parse_front_matter(path.read_text(encoding="utf-8"))
        rel = path.relative_to(NOTES_DIR).as_posix()
        category = path.parent.name
        stem = path.stem
        m = re.match(r"^(\d+)[-_](.*)$", stem)
        order = int(m.group(1)) if m else 999
        slug = m.group(2) if m else stem
        notes.append({
            "path": path,
            "rel": rel,
            "category": category,
            "slug": slug,
            "order": order,
            "is_index": stem == "index",
            "title": meta.get("title", slug.replace("-", " ").title()),
            "blurb": meta.get("blurb", ""),
            "depth": int(meta.get("depth", 2)),
            "tags": meta.get("tags", []),
            "body": body,
            "meta": meta,
            "url": f"notes/{category}/{stem}.html",
            "id": rel.replace("/", ":"),
        })
    notes.sort(key=lambda n: (n["category"], 0 if n["is_index"] else 1, n["order"], n["slug"]))
    return notes


def categories(notes):
    """Ordered dict: category key -> {title, blurb, url, depth, notes:[...]}"""
    cats = {}
    for n in notes:
        c = cats.setdefault(n["category"], {"key": n["category"], "title": n["title"],
                                            "blurb": n["blurb"], "url": n["url"],
                                            "depth": n["depth"], "notes": []})
        if n["is_index"]:
            c.update(title=n["title"], blurb=n["blurb"], url=n["url"], depth=n["depth"])
        else:
            c["notes"].append(n)
    return dict(sorted(cats.items()))


def catalog_html(cats, root: str) -> str:
    """The machine-generated half of the master note: one block per category."""
    out = []
    for key, cat in cats.items():
        curl = f'{root}/{cat["url"]}'
        out.append(f'<h3 id="cat-{key}"><a href="{curl}">{cat["title"]}</a></h3>')
        if cat["blurb"]:
            out.append(f'<p><em>{cat["blurb"]}</em></p>')
        out.append('<table><thead><tr><th>Note</th><th>What it is</th>'
                   '<th style="white-space:nowrap">Starts at</th></tr></thead><tbody>')
        for n in cat["notes"]:
            out.append(f'<tr><td><a href="{root}/{n["url"]}">{n["title"]}</a></td>'
                       f'<td>{n["blurb"]}</td><td>L{n["depth"]}</td></tr>')
        out.append('</tbody></table>')
    return "\n".join(out)


def nav_html(cats, current_id: str, root: str, extras=("graph", "standalone")) -> str:
    parts = ['<nav class="sidebar">',
             f'<div class="nav-back"><a href="{root}/index.html">Atlas — all notes</a></div>']
    if "graph" in extras:
        parts.append(f'<div class="nav-back"><a href="{root}/graph.html">Connection graph</a></div>')
    if "standalone" in extras:
        parts.append(f'<div class="nav-back"><a href="{root}/atlas-standalone.html">'
                     f'Single-file edition</a></div>')
    for key, cat in cats.items():
        parts.append(f'<h3><a href="{root}/{cat["url"]}">{cat["title"]}</a></h3>')
        for n in cat["notes"]:
            cls = ' class="here"' if n["id"] == current_id else ""
            parts.append(f'<a{cls} href="{root}/{n["url"]}">{n["title"]}</a>')
    parts.append("</nav>")
    return "\n".join(parts)


def build_graph(notes, cats, out_root: Path, root: str = ".", level: int = 4):
    """Write graph.html + graph.json: the real note-to-note link graph."""
    id_of = {"notes/" + n["rel"]: n["id"] for n in notes}
    cat_index = {key: i for i, key in enumerate(cats.keys())}
    nodes, links = [], []
    for n in notes:
        nodes.append({"id": n["id"], "title": n["title"], "category": cat_index[n["category"]],
                      "level": int(n["depth"]), "url": n["url"] if not n["is_index"] else None,
                      "kind": "index" if n["is_index"] else "note"})
    seen = set()
    for n in notes:
        base = Path("notes") / n["category"]
        # structural link: note -> its category hub
        cat_id = id_of.get("notes/%s/index.md" % n["category"])
        if cat_id and cat_id != n["id"]:
            key = (n["id"], cat_id)
            if key not in seen:
                seen.add(key)
                links.append({"source": n["id"], "target": cat_id, "w": 2})
        for target in re.findall(r"\]\(([^)\s]+?\.md)(?:#[^)]*)?\)", n["body"]):
            resolved = os.path.normpath(os.path.join(base.as_posix(), target))
            tid = id_of.get(resolved)
            if not tid or tid == n["id"]:
                continue
            key = (n["id"], tid)
            if key in seen:
                continue
            seen.add(key)
            links.append({"source": n["id"], "target": tid, "w": 1})
    data = {"nodes": nodes, "links": links,
            "categories": [c["title"] for c in cats.values()]}
    (out_root / "graph.json").write_text(json.dumps(data), encoding="utf-8")

    body = """
<div class="graphwrap">
  <div class="graphbar">
    <label>depth up to&nbsp;
      <select id="levels">
        <option value="1">L1 · plain</option>
        <option value="2">L2</option>
        <option value="3">L3</option>
        <option value="4" selected>L4 · everything</option>
      </select>
    </label>
    <label><input type="checkbox" id="labels" checked> labels</label>
    <button id="shake" type="button">re-settle</button>
    <span class="hint">drag a node · hover to isolate its neighbourhood · click to open the note</span>
  </div>
  <canvas id="graph" width="900" height="620"></canvas>
  <div id="tip" class="tip" hidden></div>
  <div id="legend" class="legend"></div>
</div>
<script src="__ROOT__/assets/graph.js"></script>
""".replace("__ROOT__", root)
    fake = {"title": "Connection graph", "id": "__graph__", "url": "graph.html"}
    flat = [n for n in notes if not n["is_index"]]
    extras = ("graph", "standalone") if out_root == DIST else ("graph",)
    (out_root / "graph.html").write_text(
        render_page(fake, body, cats, flat, root, level, True, extras=extras), encoding="utf-8")



def footer_html(flat, current_id: str, root: str) -> str:
    """Prev / next across the whole ordered note list."""
    ids = [n["id"] for n in flat]
    if current_id not in ids:
        return ""
    i = ids.index(current_id)
    out = ['<div class="shortcut">']
    if i > 0:
        p = flat[i - 1]
        out.append(f'<a href="{root}/{p["url"]}">← {p["title"]}</a>')
    out.append(f'<a href="{root}/index.html">Atlas</a>')
    out.append(f'<span style="color:var(--muted)">{i + 1} / {len(flat)}</span>')
    if i < len(flat) - 1:
        nxt = flat[i + 1]
        out.append(f'<a href="{root}/{nxt["url"]}">{nxt["title"]} →</a>')
    out.append("</div>")
    out.append('<div class="keys">keys: <b>/</b> search · <b>a</b> atlas · <b>g</b> graph · '
               '<b>t</b> top · click a figure to enlarge</div>')
    return "\n".join(out)


def search_index(notes, cats) -> str:
    flat = [n for n in notes if not n["is_index"]]
    data = [{"title": n["title"], "blurb": n["blurb"], "tags": n["tags"],
             "category": cats[n["category"]]["title"], "depth": n["depth"],
             "url": n["url"]} for n in flat]
    for c in cats.values():
        data.append({"title": c["title"], "blurb": c["blurb"], "tags": [],
                     "category": c["title"], "depth": c["depth"], "url": c["url"]})
    return json.dumps(data, ensure_ascii=False, indent=0)


# --------------------------------------------------------------------------- #
# markdown -> html  (pandoc, fragment mode; the shell is assembled here)
# --------------------------------------------------------------------------- #
def pandoc_fragment(md: str, offline: bool = False, toc_depth: int = 3) -> str:
    args = [PANDOC, "-f",
            "markdown+tex_math_dollars+pipe_tables+grid_tables+footnotes"
            "+definition_lists+task_lists+implicit_figures+smart+tex_math_single_backslash",
            "-t", "html5", "--wrap=none"]
    # --mathjax in fragment mode leaves \(..\)/\[..\] for client-side KaTeX/MathJax;
    # --mathml needs no JS at all (nice for offline viewing).
    args.append("--mathml" if offline else "--mathjax")
    p = subprocess.run(args, input=md, capture_output=True, text=True)
    if p.returncode != 0:
        sys.stderr.write(p.stderr)
        raise SystemExit("pandoc failed")
    return p.stdout


def postprocess(html: str) -> str:
    """Rewrite .md links to .html and decorate ladder headings."""
    html = re.sub(r'href="([^"]+?)\.md(#([^"]*))?"',
                  lambda m: f'href="{m.group(1)}.html' + (f'#{m.group(3)}' if m.group(3) else '') + '"',
                  html)

    def ladder(m):
        lvl, rest = m.group(2), m.group(3).strip()
        rest = rest.replace(f"L{lvl}", "", 1).lstrip(" ·—-–")
        return (f'<h2 class="ladder l{lvl}" id="{m.group(1)}">'
                f'<span class="rung">L{lvl}</span>{rest}</h2>')

    html = re.sub(r'<h2 id="([^"]+)">L([1-4])[^<]*?(.*?)</h2>', ladder, html)

    # every section heading becomes a deep link ("§"), and images load lazily
    def anchor(m):
        return ('<h%s%s id="%s">%s<a class="anchor" href="#%s" aria-label="link to this '
                'section">§</a></h%s>' % (m.group(1), m.group(2), m.group(3), m.group(4),
                                          m.group(3), m.group(1)))
    html = re.sub(r'<h([23])([^>]*)\sid="([^"]+)">(.*?)</h\1>', anchor, html, flags=re.S)
    html = re.sub(r'<img (?!.*loading=)src="', '<img loading="lazy" decoding="async" src="', html)
    return html


def extract_toc(html: str, levels=(2, 3)) -> str:
    """Two-level table of contents taken straight from the rendered HTML ids."""
    items = []
    for m in re.finditer(r'<h([1-6]) id="([^"]+)">(.*?)</h\1>', html, re.S):
        lvl = int(m.group(1))
        if lvl not in levels:
            continue
        raw = re.sub(r'<a class="anchor".*?</a>', "", m.group(3), flags=re.S)
        text = re.sub(r"<[^>]+>", "", raw).strip()
        text = (text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
                .replace("&quot;", '"').replace("&#39;", "'"))
        if text:
            items.append((lvl, m.group(2), text))
    if not items:
        return ""
    top = min(levels)
    out = ['<nav class="toc"><ul>']
    prev, sub_open = None, False
    for lvl, hid, text in items:
        if lvl == top:
            if prev is not None:
                out.append("</li>")
                if sub_open:
                    out.append("</ul>")
                    sub_open = False
            out.append(f'<li><a href="#{hid}">{text}</a>')
        else:
            if not sub_open:
                sub_open = True
                out.append("<ul>")
            out.append(f'<li><a href="#{hid}">{text}</a></li>')
        prev = lvl
    if prev is not None:
        out.append("</li>")
        if sub_open:
            out.append("</ul>")
    out.append("</ul></nav>")
    return "\n".join(out)


def render_page(note, body_md, cats, notes_flat, root, level, offline, toc_depth=3,
                extras=("graph", "standalone"), depth_override=None):
    fragment = pandoc_fragment(body_md, offline=offline, toc_depth=toc_depth)
    fragment = fragment.replace("<!-- AUTO:CATALOG -->", catalog_html(cats, root))
    body = postprocess(fragment)
    toc = extract_toc(body, levels=(1, 2) if toc_depth == 1 else (2, 3))
    tpl = (ASSETS / "template.html").read_text(encoding="utf-8")
    page = (tpl
            .replace("{{MATHHEAD}}", "" if offline else KATEX_HEAD)
            .replace("{{TITLE}}", note["title"])
            .replace("{{LEVEL}}", str(level))
            .replace("{{LEVEL_LABEL}}", LEVEL_LABELS[level])
            .replace("{{DEPTH}}",
                     depth_override if depth_override is not None
                     else depth_switch(note["url"], root, level, MIRRORS))
            .replace("{{ROOT}}", root)
            .replace("{{ROOT_JSON}}", json.dumps(root))
            .replace("{{NAV}}", nav_html(cats, note["id"], root, extras))
            .replace("{{TOC}}", toc)
            .replace("{{FOOTER}}", footer_html(notes_flat, note["id"], root))
            .replace("{{BODY}}", body))
    return page


# --------------------------------------------------------------------------- #
# site assembly
# --------------------------------------------------------------------------- #
def copy_resources(out_root: Path):
    """Copy the CSS/JS and the vector figures into the built site.

    PNG versions stay in figures/ as a fallback for viewers without SVG/PDF
    support; they are large, so they are not duplicated into dist/.
    """
    for sub in ("assets", "figures"):
        src = ROOT / sub
        if not src.exists():
            continue
        dst = out_root / sub
        dst.mkdir(parents=True, exist_ok=True)
        for f in src.iterdir():
            # .png and .pdf are build artefacts for print/fallback use only; template.html is
            # consumed by build.py itself; the animated .gif files are frame-thinned fallbacks;
            # and `anim-*.svg` are the static filmstrip *posters* of animations, which exist for
            # the print build — the pages embed the animated .webp instead.
            if f.is_file() and f.suffix.lower() not in (".png", ".pdf", ".gif") \
                    and not (f.name.startswith("anim-") and f.suffix.lower() == ".svg") \
                    and f.name != "template.html":
                shutil.copy2(f, dst / f.name)


LINK_RE = re.compile(r"\]\(([^)\s]+)\)")


def relink(md: str, from_dir: str, prefix: str = ".") -> str:
    """Rebase relative links in markdown so they work from a page at `prefix`.

    A note's links are written relative to its own folder (notes/<category>/).
    When a note is re-published somewhere else — the master note copied to the
    site root, or every note concatenated into the all-in-one page — those
    links must be resolved and re-expressed from the new location.
    """
    def sub(m):
        t = m.group(1)
        if t.startswith(("http", "#", "mailto", "data:")):
            return m.group(0)
        path, sep, frag = t.partition("#")
        if not path:
            return m.group(0)
        target = os.path.normpath(os.path.join(from_dir, path)).replace(os.sep, "/")
        url = target if prefix in ("", ".") else prefix.rstrip("/") + "/" + target
        return "](" + url + (("#" + frag) if sep else "") + ")"

    return LINK_RE.sub(sub, md)


def build_site(notes, cats, level, out_root: Path, offline: bool = False) -> int:
    """Write the whole site at `level` into out_root. Returns pages written."""
    flat = [n for n in notes if not n["is_index"]]
    # the single-file edition exists only at the site root, so mirror builds drop that link
    extras = ("graph", "standalone") if out_root == DIST else ("graph",)
    out_root.mkdir(parents=True, exist_ok=True)
    copy_resources(out_root)
    (out_root / "search-index.json").write_text(search_index(notes, cats), encoding="utf-8")
    pages = 0
    for note in notes:
        body_md = trim(note["body"], level)
        depth = len(Path(note["url"]).parts) - 1
        root = "/".join([".."] * depth)
        dest = out_root / note["url"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render_page(note, body_md, cats, flat, root, level, offline,
                                    extras=extras), "utf-8")
        pages += 1
        if note["is_index"] and note["category"] == "00-atlas":
            body_root = relink(body_md, "notes/00-atlas", ".")
            page = render_page(note, body_root, cats, flat, ".", level, offline, extras=extras)
            (out_root / "index.html").write_text(page, "utf-8")
            pages += 1
    return pages


def build_standalone(notes, cats, out_root: Path, offline: bool = True):
    """One self-contained HTML file: all notes, all figures, no CDN, no server.

    Every internal link becomes an in-page anchor, every figure is inlined as SVG, and the
    search index is embedded — so the file can be emailed, put on a USB stick or dropped on
    any static host and it still works offline.
    """
    flat = [n for n in notes if not n["is_index"]]
    anchors, used = {}, {}
    for n in notes:
        a = "note-" + re.sub(r"[^a-z0-9]+", "-", n["title"].lower()).strip("-")
        used[a] = used.get(a, 0) + 1
        anchors[n["rel"]] = a if used[a] == 1 else "%s-%d" % (a, used[a])

    fig_cache = {}
    def figure_svg(name):
        if name not in fig_cache:
            p = FIG_DIR / name
            low = name.lower()
            if low.endswith((".webp", ".gif")):
                # animations (and their .gif fallback) are inlined as data URIs so that the
                # single-file edition keeps its promise: one file, no side-car assets.
                if p.exists():
                    mime = "image/webp" if low.endswith(".webp") else "image/gif"
                    fig_cache[name] = (
                        '<img class="anim" loading="lazy" alt="animation" src="data:%s;base64,%s">'
                        % (mime, base64.b64encode(p.read_bytes()).decode("ascii")))
                else:
                    fig_cache[name] = ""
                return fig_cache[name]
            svg = p.read_text(encoding="utf-8") if p.exists() else ""
            svg = re.sub(r'<svg([^>]*?)\swidth="[^"]*"([^>]*?)\sheight="[^"]*"',
                         r'<svg\1\2', svg, count=1)
            fig_cache[name] = svg
        return fig_cache[name]

    def anchor_link(note, target):
        # anchors are keyed by each note's path *relative to notes/*, so resolve against the
        # note's own category folder (no "notes/" prefix).
        resolved = os.path.normpath(os.path.join(Path(note["category"]).as_posix(), target))
        return "#" + anchors[resolved] if resolved in anchors else None

    sections, toc = [], []
    for key, cat in cats.items():
        sections.append('<h2 class="cathead" id="cat-%s">%s</h2>' % (key, cat["title"]))
        toc.append('<h3><a href="#cat-%s">%s</a></h3>' % (key, cat["title"]))
        for n in [x for x in notes if x["category"] == key]:
            toc.append('<a href="#%s">%s</a>' % (anchors[n["rel"]], n["title"]))
        for n in [x for x in notes if x["category"] == key]:
            body = n["body"]
            # links -> in-page anchors
            def sub_link(m):
                t = m.group(1)
                if t.startswith(("http", "#", "mailto")):
                    return m.group(0)
                a = anchor_link(n, t.split("#")[0])
                return "](%s)" % (a if a else t)
            body = re.sub(r"\]\(([^)\s]+?\.md)(?:#([^)]*))?\)", sub_link, body)
            html = pandoc_fragment(body, offline=offline, toc_depth=0)
            html = postprocess(html)
            # NB the tag may carry loading="lazy"/decoding/class attributes before src
            html = re.sub(r'<img\b[^>]*?src="[^"]*figures/([^"]+)"[^>]*?/?>',
                          lambda m: '<span class="fig">' + figure_svg(m.group(1)) + "</span>", html)
            html = re.sub(r'<a href="([^"]+?)\.md(#[^"]*)?"',
                          lambda m: '<a href="' + (anchor_link(n, m.group(1)) or m.group(1)) + '"', html)
            sections.append('<section class="standalone" id="%s"><h1>%s</h1>\n%s</section>'
                            % (anchors[n["rel"]], n["title"], html))

    css = (ASSETS / "style.css").read_text(encoding="utf-8")
    katex = "" if offline else KATEX_HEAD
    search = json.dumps([{"t": n["title"], "b": n["blurb"], "a": anchors[n["rel"]],
                          "c": cats[n["category"]]["title"]} for n in flat], ensure_ascii=False)
    page = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Panta Rhei — single-file edition (the Transport Atlas)</title>
<style>%s</style>
%s
<style>
.layout{grid-template-columns:20rem minmax(0,1fr) 0!important}
.standalone{border-top:1px solid var(--border);padding-top:1.4rem;margin-top:2.4rem}
.standalone h1{margin-top:0}
.fig{display:block}
.fig svg{max-width:100%%;height:auto}
#sfsearch{width:100%%;padding:.42rem .7rem;border-radius:8px;border:1px solid var(--border);
  background:var(--card);color:var(--fg);font:inherit;font-size:.9rem}
#sfhits{margin:.6rem 0 0;padding:0;list-style:none;font-size:.85rem}
#sfhits a{display:block;padding:.25rem .4rem;border-radius:6px;text-decoration:none;color:var(--fg)}
#sfhits a:hover{background:var(--accent-soft)}
.top-note{font-size:.82rem;color:var(--muted)}
body{padding-bottom:4rem}
main.content{max-width:none}
article.markdown{max-width:78ch}
</style>
</head><body>
<header class="topbar">
  <span class="brand"><span class="brand-mark">πάντα ῥεῖ</span>
    <span class="brand-name">Panta Rhei</span><span class="brand-sub">the Transport Atlas</span></span>
  <span class="lvl-badge">one file · works offline</span>
  <div class="searchwrap"><input id="search" type="search" placeholder="filter notes…" autocomplete="off">
  <div id="results" class="results" hidden></div></div>
</header>
<div class="layout">
<nav class="sidebar">
  <div class="nav-back"><a href="#top">↑ top</a></div>
  <input id="sfsearch" placeholder="filters the list below" autocomplete="off">
  <ul id="sfhits"></ul>
  %s
</nav>
<main class="content"><article class="markdown"><a id="top"></a>
<h1>Panta Rhei — the whole atlas in one file</h1>
<p class="top-note">Every note, every figure and the search index in a single HTML file: no server, no
internet, no dependencies. It works from a USB stick, an email attachment or any static host. The full
site — with the connection graph, the depth mirrors and the standalone search page — is a folder away.</p>
%s
</article></main></div>
<script>
var IDX=%s,BOX=document.getElementById("sfhits"),IN=document.getElementById("sfsearch");
function renderList(q){q=(q||"").toLowerCase();var h=IDX.filter(function(x){return !q||
 (x.t+" "+x.b+" "+x.c).toLowerCase().indexOf(q)>-1;}).slice(0,200);
 BOX.innerHTML=h.map(function(x){var H="#" + x.a;return '<li><a href="' + H + '">' + x.t +
 '<br><span style="color:var(--muted)">' + x.c + '</span></a></li>';}).join("");}
renderList("");IN.addEventListener("input",function(){renderList(IN.value);});
</script>
</body></html>""" % (css, katex, "\n".join(toc), "\n".join(sections), search)
    out = out_root / "atlas-standalone.html"
    out.write_text(page, encoding="utf-8")
    return out

def build_all_in_one(notes, cats, level, out_root: Path, offline: bool = False):
    flat = [n for n in notes if not n["is_index"]]
    chunks = []
    for n in flat:
        body = relink(trim(n["body"], level), "notes/" + n["category"], ".")
        chunks.append(f'# {n["title"]}\n\n{body}')
    fake = {"title": "Panta Rhei — the complete atlas (one scroll)", "id": "__all__",
            "url": "all-in-one.html"}
    page = render_page(fake, "\n\n".join(chunks), cats, flat, ".", level, offline, toc_depth=1,
                       depth_override='<span class="lvl-badge" title="one scroll — every note, '
                                      'every level">one scroll · every level</span>')
    (out_root / "all-in-one.html").write_text(page, encoding="utf-8")


# --------------------------------------------------------------------------- #
# PDF (printable) build
# --------------------------------------------------------------------------- #
def pdf_markdown(notes, level):
    out = ["---", 'title: "Panta Rhei"',
           'subtitle: "all things flow — the Transport Atlas: a layered reference for transport phenomena"',
           'author: "the Transport Atlas"',
           'date: "generated by build.py"', "---", ""]
    for n in notes:
        body = trim(n["body"], level)
        body = re.sub(r"\]\((?:\.\./)*figures/([^)]+?)\.svg\)", r"](\g<1>.pdf)", body)
        # animations go into print as their static frame-strip poster
        body = re.sub(r"\]\((?:\.\./)*figures/([^)]+?)\.(?:webp|gif)\)", r"](\g<1>.png)", body)
        out.append(f"\\newpage\n\n# {n['title']}\n\n" + body)
    return "\n\n".join(out)


def build_pdf(notes, level, out_file: Path):
    md = pdf_markdown(notes, level)
    (ROOT / "build").mkdir(exist_ok=True)
    src = ROOT / "build" / "atlas-print.md"
    src.write_text(md, encoding="utf-8")
    args = [PANDOC, str(src), "-f", "markdown+tex_math_dollars+pipe_tables+grid_tables"
            "+footnotes+definition_lists+implicit_figures+tex_math_single_backslash",
            "-o", str(out_file), "--pdf-engine=xelatex", "--toc", "--toc-depth=1",
            "--top-level-division=section",
            "--resource-path", f"{ROOT / 'figures'}:{ROOT}",
            "-V", "geometry:a4paper,margin=2.1cm", "-V", "fontsize=10pt",
            "-V", "colorlinks=true", "-V", "linkcolor=RoyalBlue",
            "-V", "urlcolor=RoyalBlue", "-V", "mainfont=DejaVu Serif",
            "-V", "monofont=DejaVu Sans Mono",
            "--include-in-header", str(ASSETS / "pdf-header.tex")]
    p = subprocess.run(args, capture_output=True, text=True, cwd=str(ROOT))
    if p.returncode != 0:
        sys.stderr.write(p.stderr[-4000:])
        raise SystemExit("pdf build failed (is xelatex installed?)")
    return out_file


# --------------------------------------------------------------------------- #
# link audit
# --------------------------------------------------------------------------- #
def check_links(notes):
    bad = []
    for n in notes:
        base = n["path"].parent
        for target in re.findall(r"\]\(([^)\s]+)\)", n["body"]):
            if target.startswith(("http", "#", "mailto")):
                continue
            t = target.split("#")[0]
            if not t:
                continue
            if t.endswith((".svg", ".pdf", ".png", ".webp", ".gif")):
                if not (base / t).resolve().exists():
                    bad.append(f'{n["rel"]}: missing figure {target}')
            elif t.endswith(".md"):
                if not (base / t).resolve().exists():
                    bad.append(f'{n["rel"]}: broken note link {target}')
    return bad


def trim(body: str, max_level: int) -> str:
    """Drop ladder rungs deeper than max_level; keep all non-ladder `##` sections."""
    out, keep = [], True
    for line in body.splitlines():
        m = re.match(r"^##\s+L([1-4])\b", line)
        if m:
            keep = int(m.group(1)) <= max_level
        elif re.match(r"^##\s+", line):
            keep = True
        if keep:
            out.append(line)
    return "\n".join(out)


# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--levels", action="store_true", help="also build L1/L2/L3 mirrors")
    ap.add_argument("--standalone", action="store_true", help="also build the single-file offline edition")
    ap.add_argument("--pdf", action="store_true", help="also build dist/atlas.pdf")
    ap.add_argument("--all", action="store_true", help="levels + all-in-one + pdf")
    ap.add_argument("--offline", action="store_true", help="render math as MathML (no CDN)")
    ap.add_argument("--check", action="store_true", help="audit links/figures and exit")
    args = ap.parse_args()

    global MIRRORS
    MIRRORS = bool(args.levels or args.all)

    notes = load_notes()
    cats = categories(notes)
    if not notes:
        raise SystemExit("no notes found under notes/")
    n_notes = sum(1 for n in notes if not n["is_index"])
    n_figs = len(list(FIG_DIR.glob("*.svg")))

    if args.check:
        bad = check_links(notes)
        print(f"{len(notes)} files · {n_notes} notes · {len(cats)} categories · {n_figs} svg figures")
        for b in bad:
            print("  !", b)
        print("all internal links resolve" if not bad else f"{len(bad)} problem(s)")
        return

    pages = build_site(notes, cats, 4, DIST, args.offline)
    build_graph(notes, cats, DIST, ".")
    (DIST / ".nojekyll").write_text("", encoding="utf-8")
    print(f"full  : {pages:4d} pages -> {DIST}/index.html")
    print(f"graph :    1 page  -> {DIST}/graph.html  (+ graph.json)")

    if args.standalone or args.all:
        out = build_standalone(notes, cats, DIST, offline=True)
        print(f"single:    1 file  -> {out}  ({out.stat().st_size / 1e6:.1f} MB, offline)")

    if args.levels or args.all:
        for lvl in (1, 2, 3):
            d = DIST / f"L{lvl}"
            shutil.rmtree(d, ignore_errors=True)
            print(f"level {lvl}: {build_site(notes, cats, lvl, d, args.offline):4d} pages"
                  f" -> {d}/index.html")
            build_graph(notes, cats, d, ".", lvl)
        build_all_in_one(notes, cats, 4, DIST, args.offline)
        print(f"single:   1 page  -> {DIST}/all-in-one.html")

    if args.pdf or args.all:
        print(f"pdf   : {build_pdf(notes, 4, DIST / 'atlas.pdf')}")

    bad = check_links(notes)
    if bad:
        print(f"\n{len(bad)} link problem(s):")
        for b in bad[:20]:
            print("  !", b)
    print(f"\ndone — {n_notes} notes, {len(cats)} categories, {n_figs} figures.")
    print(f"open   {DIST}/index.html     (or: python3 -m http.server -d {DIST})")


if __name__ == "__main__":
    main()

