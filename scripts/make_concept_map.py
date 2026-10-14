#!/usr/bin/env python3
"""
Draw the atlas concept map with graphviz (`dot`).

    python3 scripts/make_concept_map.py   ->   figures/concept-map.svg / .pdf

Nodes are written as  "id | label (\n allowed) | level | cluster".
Level sets the colour: 1 blue, 2 teal, 3 violet, 4 amber.
Edges are written as    "source: target target target".
"""
import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "figures"

NODES = r"""
balance|the balance law\nflux · divergence|1|found
matder|material derivative\nLagrangian ↔ Eulerian|1|found
tax|PDE taxonomy\n+ boundary conditions|1|found
dimless|dimensionless numbers\nPe · Re · Ra · Da · Kn|1|found
const|constitutive laws\nFick · Fourier · Darcy|1|found
spectral|Fourier, Green functions\npropagators|2|found
entropy|entropy & variational\nstructure|3|found
walks|random walks, Langevin\nfluctuation–dissipation|3|found
mem|memory & linear response\nMori–Zwanzig|4|found
adv|advection|1|bulk
conv|convection & buoyancy\nRayleigh–Bénard, Marangoni|2|bulk
vor|vorticity & pressure|3|bulk
bl|boundary layers|3|bulk
turb|turbulence &\neddy diffusivity|3|bulk
taylor|shear dispersion\nTaylor–Aris|3|bulk
mix|mixing & chaotic\nadvection|3|bulk
jets|jets · plumes · wakes|3|bulk
darcy|Darcy & porous flow|2|bulk
rheo|non-Newtonian rheology|4|bulk
diff|diffusion (Fick)|1|micro
brown|Brownian motion\nEinstein relations|2|micro
cond|conduction (Fourier)|1|micro
coefs|diffusion coefficients\nfrom kinetic theory|3|micro
knud|Knudsen & rarefied\ntransport|3|micro
cross|Soret · Dufour\nMaxwell–Stefan|4|micro
ionic|Nernst–Planck &\nelectrochemical|3|micro
anom|anomalous diffusion\nCTRW, fractional|3|micro
kin|reaction kinetics\nArrhenius|2|inter
auto|autocatalysis &\noscillations|3|inter
rd|reaction–diffusion\nTuring patterns|3|inter
front|fronts & travelling\nwaves|3|inter
taxis|chemotaxis\nKeller–Segel|3|inter
sorp|sorption & retardation|3|inter
absorb|absorption · dissolution\ninterfacial transfer|2|inter
phase|phase change\nStefan problem|2|inter
sed|sedimentation · deposition\nfiltration|2|inter
accr|accretion · ablation\nsurface growth|4|inter
wells|wells · injection · efflux\nbreakthrough|2|inter
subs|subsidence &\nporoelasticity|3|inter
diss|viscous dissipation\nJoule heating|3|inter
bolt|Boltzmann equation\nH-theorem|4|kin
bgk|BGK · Vlasov\nplasmas|4|kin
fp|Fokker–Planck\nKramers escape|3|kin
rte|radiative transfer|2|kin
neut|neutron transport|4|kin
lbm|lattice-Boltzmann\nparticle methods|4|kin
claw|conservation laws\nshocks, entropy solutions|3|beyond
hj|Hamilton–Jacobi\nviscosity solutions|4|beyond
frac|nonlocal & fractional\noperators|3|beyond
visco|memory & viscoelastic\ntransport|4|beyond
catt|Cattaneo & telegraph\nfinite-speed diffusion|4|beyond
pme|nonlinear diffusion\nporous medium|3|beyond
spde|stochastic PDEs\nrandom media|4|beyond
homo|homogenisation\n& upscaling|3|beyond
free|free boundaries\nlevel sets, phase field|3|beyond
ot|optimal transport\n& gradient flows|4|beyond
mcont|microcontinuum continua|4|beyond
vi|variational inequalities\nhysteresis|4|beyond
mhd|MHD & relativistic\ntransport|4|beyond
disc|discretisation: consistency\nstability, convergence|2|num
cfl|CFL, stiffness\ntime stepping|2|num
numerr|numerical diffusion\n& dispersion|2|num
lim|limiters · TVD · WENO|3|num
split|operator splitting\n& multiphysics coupling|3|num
lin|linear solvers\npreconditioning|3|num
nlin|nonlinear solvers\ncontinuation|3|num
mesh|adaptivity, moving meshes\nparallel decomposition|3|num
mc|particle & Monte Carlo\nhybrid methods|3|num
inv|inverse problems &\ndata assimilation|4|num
ml|machine learning &\noperator learning|4|num
vv|verification & validation|3|num
spd|structure-preserving\ndiscretisations|4|num
fin|finance|3|bridge
bio|biology & medicine|2|bridge
geo|geoscience & climate|2|bridge
plasma|plasma & astrophysics|3|bridge
eng|engineering devices|2|bridge
mldata|machine learning & data|3|bridge
img|images & signals|3|bridge
soc|networks & traffic|3|bridge
qm|quantum & condensed matter|4|bridge
unify|one mathematics of transport|4|bridge
atlas|the atlas (master note)|1|univ
flows|why everything flows\n(five universal structures)|3|univ
lookup|the translation lookup\n(object → transport form)|2|univ
mind|cognitive science & mind\n(decisions, fields, memory)|3|univ
society|social behaviour, economics\n& language|3|univ
algo|computation & algorithms\n(Dijkstra, PageRank, SGD)|3|univ
qft|physics, chemistry\n& field theory|4|univ
info|information, statistics\n& inference|4|univ
maths|mathematics itself\n(geometric flows, categories)|4|univ
limits|limits of the claim\n(where it stops)|2|univ
higherord|higher order\n& dispersive|3|found
dims|dimensions, geometry\n& manifolds|3|found
integ|integrable systems\n& solitons|4|beyond
varpr|variational principles\n& Noether|4|beyond
delayn|delay & retarded\ntransport|3|beyond
eq|equilibria &\ncritical points|1|mech
stab|linearisation\n& stability|2|mech
bif|bifurcation\ntheory|3|mech
nonlin|nonlinearity &\nmode coupling|3|mech
chaos|chaos &\npredictability|4|mech
crit|phase transitions\n& criticality|3|mech
scale|scaling & self-\nsimilarity|2|mech
dual|duality &\ntransforms|3|mech
noise|noise-induced\nphenomena|3|mech
intermap|the intersections\nmap|2|mech
biblio|bibliography\n(primary · review · sceptical)|3|mech
hera|Heraclitus\n& the river|1|panta
beauty|beauty & the flow\n(marbling, patterns)|1|panta
kuram|collective behaviour\n& synchrony|2|panta
arrow|irreversibility &\nthe arrow of time|2|panta
crossx|crossings & cross-\nfertilisation|2|panta
river|the river\nas a model|1|panta
"""

EDGES = """
balance: adv diff cond kin const
const: diff cond darcy
matder: adv conv vor turb
tax: disc claw hj free
dimless: conv bl turb knud disc rd subs
spectral: numerr disc anom
entropy: ot pme visco spde
walks: diff brown fp anom spde
mem: visco turb fp
adv: mix jets taylor claw lim numerr
conv: vor turb geo plasma
bl: turb eng coefs
turb: mix ml eng
taylor: sorp darcy geo
mix: rd
jets: eng accr
darcy: wells subs geo homo
rheo: visco vi
diff: brown coefs knud cross ionic anom pme spde img mldata bio
cond: eng rte pme catt
coefs: knud bolt lbm homo
knud: bolt lbm bgk
cross: ionic
ionic: bio eng
anom: frac spde
kin: auto rd front sorp absorb diss
auto: rd
rd: taxis free bio
front: claw phase bio
taxis: bio
sorp: eng geo
absorb: rte eng geo
phase: free pme eng
sed: geo eng wells
accr: free eng
wells: subs geo inv
subs: geo
diss: turb eng
bolt: lbm bgk coefs neut
bgk: plasma mhd
fp: anom visco bio
rte: neut plasma geo eng
neut: eng
lbm: eng ml
claw: front hj soc eng
hj: img mldata disc free
frac: spde anom vi pme
visco: catt mcont
catt: rte pme
pme: free ot img geo
spde: inv geo ml
homo: subs geo ml spd
free: phase img spd
ot: unify mldata fin entropy
mcont: spd
vi: rheo free eng
mhd: plasma
disc: cfl numerr vv spd lin
cfl: split nlin mc
numerr: lim vv spd
lim: claw
split: rd eng geo
lin: mesh nlin inv
nlin: vi rd catt
mesh: free subs spd
mc: bolt rte neut spde
inv: geo bio ml
ml: turb unify pme
vv: eng
spd: claw entropy geo
fin: unify
bio: geo soc
geo: soc
plasma: qm
eng: soc
mldata: img unify
img: soc
soc: inv
qm: unify
atlas: balance adv diff kin const
spectral: dims
tax: higherord dims
entropy: flows visco
walks: mind info
claw: integ
higherord: integ pme
integ: varpr
varpr: mhd spd maths
delayn: mind soc
flows: lookup mind society algo qft info maths limits
lookup: mind society algo qft info maths
mind: society info limits
society: limits
algo: limits
qft: maths limits
info: maths algo
maths: limits unify
eq: stab bif nonlin noise
stab: bif chaos crit
bif: chaos crit
nonlin: chaos scale dual crit
chaos: crit noise
crit: scale noise kuram
scale: dual noise intermap
dual: intermap
noise: intermap arrow
intermap: crossx biblio
hera: river arrow crossx
beauty: river
kuram: crit crossx
arrow: noise crossx
crossx: biblio limits
river: hera arrow beauty
turb: nonlin chaos crit
spectral: dual
entropy: crit arrow noise
walks: noise arrow
mix: nonlin beauty
rd: beauty crit
front: nonlin
anom: scale noise
vi: bif
phase: bif
unify: intermap crossx
mhd: qft
"""

COLORS = {1: ("#e8f0fe", "#1f4fa8"), 2: ("#e6f6f4", "#0f766e"),
          3: ("#f3ecfe", "#6d28d9"), 4: ("#fef3e2", "#b45309")}
CLUSTERS = [("found", "foundations"), ("bulk", "bulk fluid transport"),
            ("micro", "microscopic transport"), ("inter", "interaction / source / sink"),
            ("kin", "kinetic & radiative"), ("beyond", "beyond classical PDEs"),
            ("num", "numerics & inversion"), ("bridge", "bridges to other fields"),
            ("univ", "universality — the strongest claim"),
            ("mech", "recurring mechanisms — the shapes that keep returning"),
            ("panta", "panta rhei — all things flow")]


def main():
    nodes = []
    for line in NODES.strip().split(chr(10)):
        nid, label, lvl, cluster = [p.strip() for p in line.split("|")]
        nodes.append((nid, label, int(lvl), cluster))
    ids = {n[0] for n in nodes}
    lines = ["digraph atlas {",
             '  graph [rankdir=LR, splines=true, overlap=false, fontname="DejaVu Sans",'
             ' bgcolor="white", nodesep=0.25, ranksep=0.9, pad=0.3];',
             '  node [shape=box, style="rounded,filled", fontname="DejaVu Sans",'
             ' fontsize=9, penwidth=1.1, margin="0.10,0.06"];',
             '  edge [color="#9aa3b2", arrowsize=0.55, penwidth=0.7];']
    for cid, cname in CLUSTERS:
        lines.append('  subgraph cluster_%s { label="%s"; labeljust=l; fontsize=11;'
                     ' fontcolor="#475569"; color="#dfe3ea"; style=rounded;'
                     ' margin=12;' % (cid, cname))
        for nid, label, lvl, cluster in nodes:
            if cluster != cid:
                continue
            fill, stroke = COLORS[lvl]
            lines.append('    %s [label="%s", fillcolor="%s", color="%s"];'
                         % (nid, label.replace(chr(10), "\\n"), fill, stroke))
        lines.append("  }")
    seen = set()
    for line in EDGES.strip().split(chr(10)):
        src, targets = line.split(":")
        for t in targets.split():
            if src in ids and t in ids and t != src and (src, t) not in seen:
                seen.add((src, t))
                lines.append("  %s -> %s;" % (src, t))
    lines.append("}")
    src = OUT / "concept-map.dot"
    src.write_text(chr(10).join(lines), encoding="utf-8")
    for fmt in ("svg", "pdf"):
        subprocess.run(["dot", "-T" + fmt, str(src), "-o", str(OUT / ("concept-map." + fmt))],
                       check=True)
    print("concept map: %d nodes, %d edges" % (len(nodes), len(seen)))


if __name__ == "__main__":
    if not shutil.which("dot"):
        raise SystemExit("graphviz 'dot' not found")
    main()
