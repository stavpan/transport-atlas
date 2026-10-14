/* Transport Atlas — interactive connection graph.
   Loads graph.json (nodes + links derived from the real note-to-note links) and runs a small
   force layout on a canvas. No dependencies. */
(function () {
  "use strict";
  var root = window.ATLAS_ROOT || ".";
  var cv = document.getElementById("graph");
  if (!cv) return;
  var ctx = cv.getContext("2d");
  var legend = document.getElementById("legend");
  var tip = document.getElementById("tip");
  var COLORS = ["#1f6feb", "#0d9488", "#7c3aed", "#d97706", "#e11d48", "#475569",
                "#15803d", "#0284c7", "#9333ea", "#b45309", "#0891b2", "#be185d"];
  var state = { nodes: [], links: [], hover: null, drag: null, alpha: 1,
                showLabels: true, minLevel: 4 };

  function resize() {
    var dpr = window.devicePixelRatio || 1;
    cv.width = Math.round(cv.clientWidth * dpr);
    cv.height = Math.round(cv.clientHeight * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  fetch(root + "/graph.json").then(function (r) { return r.json(); }).then(function (data) {
    data.nodes.forEach(function (n, i) {
      n.x = Math.cos(i * 2.399) * (120 + 11 * Math.sqrt(i));
      n.y = Math.sin(i * 2.399) * (120 + 11 * Math.sqrt(i));
      n.vx = n.vy = 0; n.deg = 0;
      n.color = COLORS[n.category % COLORS.length];
      n.visible = n.level <= state.minLevel;
    });
    var byId = {};
    data.nodes.forEach(function (n) { byId[n.id] = n; });
    state.nodes = data.nodes;
    state.links = data.links.map(function (l) {
      return { s: byId[l.source], t: byId[l.target], w: l.w || 1 };
    }).filter(function (l) { return l.s && l.t; });
    state.links.forEach(function (l) { l.s.deg++; l.t.deg++; });
    if (legend) {
      legend.innerHTML = data.categories.map(function (c, i) {
        return '<span class="lg"><i style="background:' + COLORS[i % COLORS.length] + '"></i>' + c + "</span>";
      }).join("");
    }
    resize(); step();
    window.addEventListener("resize", resize);
  });

  function visible(n) { return n.visible !== false; }

  function step() {
    var nodes = state.nodes.filter(visible), a = state.alpha, i, j, n, m, dx, dy, f, dist;
    for (i = 0; i < nodes.length; i++) {
      n = nodes[i];
      for (j = i + 1; j < nodes.length; j++) {
        m = nodes[j];
        dx = m.x - n.x; dy = m.y - n.y;
        var d2 = dx * dx + dy * dy + 0.01;
        if (d2 < 90000) {
          dist = Math.sqrt(d2); f = (1500 * a) / d2;
          dx /= dist; dy /= dist;
          n.vx -= dx * f; n.vy -= dy * f; m.vx += dx * f; m.vy += dy * f;
        }
      }
      n.vx -= n.x * 0.09 * a; n.vy -= n.y * 0.09 * a;
    }
    state.links.forEach(function (l) {
      if (!visible(l.s) || !visible(l.t)) return;
      dx = l.t.x - l.s.x; dy = l.t.y - l.s.y;
      dist = Math.sqrt(dx * dx + dy * dy) + 0.01;
      f = (dist - 95) * 0.03 * a * (l.w > 1 ? 1.7 : 1);
      dx /= dist; dy /= dist;
      l.s.vx += dx * f; l.s.vy += dy * f; l.t.vx -= dx * f; l.t.vy -= dy * f;
    });
    nodes.forEach(function (q) {
      if (q === state.drag) return;
      q.x += q.vx = q.vx * 0.85; q.y += q.vy = q.vy * 0.85;
    });
    state.alpha = Math.max(0.05, state.alpha * 0.994);
    draw();
    requestAnimationFrame(step);
  }

  function draw() {
    var w = cv.clientWidth, h = cv.clientHeight;
    ctx.clearRect(0, 0, w, h);
    ctx.save(); ctx.translate(w / 2, h / 2);
    var hov = state.hover, nb = {}, nodes = state.nodes.filter(visible);
    if (hov) {
      nb[hov.id] = true;
      state.links.forEach(function (l) {
        if (l.s === hov) nb[l.t.id] = true;
        if (l.t === hov) nb[l.s.id] = true;
      });
    }
    state.links.forEach(function (l) {
      if (!visible(l.s) || !visible(l.t)) return;
      var hl = hov && (l.s === hov || l.t === hov);
      ctx.strokeStyle = hl ? "rgba(31,111,235,.7)" : "rgba(140,150,165,.2)";
      ctx.lineWidth = hl ? 1.5 : 0.7;
      ctx.beginPath(); ctx.moveTo(l.s.x, l.s.y); ctx.lineTo(l.t.x, l.t.y); ctx.stroke();
    });
    nodes.forEach(function (n) {
      var r = 3.5 + Math.min(9, Math.sqrt(n.deg) * 1.6), dim = hov && !nb[n.id];
      ctx.globalAlpha = dim ? 0.22 : 1;
      ctx.beginPath(); ctx.arc(n.x, n.y, r, 0, 6.2832);
      ctx.fillStyle = n.color; ctx.fill();
      if (hov && n.id === hov.id) { ctx.lineWidth = 2; ctx.strokeStyle = "rgba(20,20,20,.75)"; ctx.stroke(); }
      if (state.showLabels && (r > 6 || (hov && nb[n.id]))) {
        ctx.fillStyle = "rgba(90,100,112,.95)";
        ctx.font = "11px system-ui, sans-serif";
        ctx.fillText(n.title.slice(0, 36), n.x + r + 3, n.y + 3);
      }
    ctx.globalAlpha = 1;
    });
    ctx.restore();
  }

  function hit(ev) {
    var r = cv.getBoundingClientRect();
    var x = ev.clientX - r.left - cv.clientWidth / 2;
    var y = ev.clientY - r.top - cv.clientHeight / 2;
    var best = null, bd = 1e9;
    state.nodes.filter(visible).forEach(function (n) {
      var d = (n.x - x) * (n.x - x) + (n.y - y) * (n.y - y);
      if (d < bd && d < 1000) { bd = d; best = n; }
    });
    return best;
  }

  function toGraph(ev) {
    var r = cv.getBoundingClientRect();
    return { x: ev.clientX - r.left - cv.clientWidth / 2,
             y: ev.clientY - r.top - cv.clientHeight / 2 };
  }

  cv.addEventListener("mousemove", function (e) {
    var n = hit(e);
    state.hover = n;
    if (state.drag) { var p = toGraph(e); state.drag.x = p.x; state.drag.y = p.y; }
    if (tip) {
      if (n) {
        var r = cv.getBoundingClientRect();
        tip.hidden = false;
        tip.innerHTML = "<b>" + n.title + "</b><br><span>" + n.category + " · level " + n.level +
          (n.url ? " · click to open" : "") + "</span>";
        tip.style.left = (e.clientX - r.left + 14) + "px";
        tip.style.top = (e.clientY - r.top + 10) + "px";
      } else { tip.hidden = true; }
    }
    cv.style.cursor = n ? "pointer" : "default";
  });
  cv.addEventListener("mousedown", function (e) {
    var n = hit(e);
    if (n) { state.drag = n; state.alpha = 0.5; }
  });
  window.addEventListener("mouseup", function () { state.drag = null; });
  cv.addEventListener("mouseleave", function () { state.hover = null; if (tip) tip.hidden = true; });
  cv.addEventListener("click", function (e) {
    var n = hit(e);
    if (n && n.url) window.location.href = root + "/" + n.url;
  });

  var lv = document.getElementById("levels");
  if (lv) lv.addEventListener("change", function () {
    state.minLevel = parseInt(lv.value, 10) || 4;
    state.nodes.forEach(function (n) { n.visible = n.level <= state.minLevel; });
    state.alpha = 0.7;
  });
  var lb = document.getElementById("labels");
  if (lb) lb.addEventListener("change", function () { state.showLabels = lb.checked; });
  var shake = document.getElementById("shake");
  if (shake) shake.addEventListener("click", function () { state.alpha = 1; });
})();
