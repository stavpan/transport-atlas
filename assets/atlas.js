/* Transport Atlas — client-side search over the note catalog.
   Loads dist/search-index.json once, then filters on input. No dependencies. */
(function () {
  "use strict";
  var root = window.ATLAS_ROOT || ".";
  var input = document.getElementById("search");
  var box = document.getElementById("results");
  if (!input || !box) return;

  var index = null, loading = false, sel = -1;

  function load() {
    if (index || loading) return;
    loading = true;
    fetch(root + "/search-index.json")
      .then(function (r) { return r.json(); })
      .then(function (data) { index = data; loading = false; if (input.value) render(input.value); })
      .catch(function () { loading = false; });
  }

  function score(item, q) {
    var t = item.title.toLowerCase(), b = (item.blurb || "").toLowerCase();
    var g = (item.tags || []).join(" ").toLowerCase(), c = item.category.toLowerCase();
    var s = 0;
    if (t === q) s += 100;
    if (t.indexOf(q) === 0) s += 60;
    if (t.indexOf(q) > -1) s += 40;
    if (g.indexOf(q) > -1) s += 18;
    if (b.indexOf(q) > -1) s += 10;
    if (c.indexOf(q) > -1) s += 6;
    return s;
  }

  function render(q) {
    q = q.trim().toLowerCase();
    if (!q) { box.hidden = true; box.innerHTML = ""; return; }
    var hits = [];
    for (var i = 0; i < index.length; i++) {
      var s = score(index[i], q);
      if (s > 0) hits.push([s, index[i]]);
    }
    hits.sort(function (a, b) { return b[0] - a[0] || a[1].title.localeCompare(b[1].title); });
    hits = hits.slice(0, 12);
    if (!hits.length) {
      box.innerHTML = '<div class="r-blurb" style="padding:.6rem">No note matches “' +
        q.replace(/[<>&]/g, "") + '”.</div>';
      box.hidden = false; return;
    }
    box.innerHTML = hits.map(function (h) {
      var it = h[1];
      return '<a href="' + root + "/" + it.url + '">' +
        '<span class="r-cat">' + it.category + ' · L' + it.depth + '</span>' +
        '<div class="r-title">' + it.title + "</div>" +
        '<div class="r-blurb">' + (it.blurb || "") + "</div></a>";
    }).join("");
    sel = -1;
    box.hidden = false;
  }

  function linkAt(i) { return box.querySelectorAll("a")[i] || null; }

  function move(d) {
    var links = box.querySelectorAll("a");
    if (!links.length) return;
    if (sel > -1 && linkAt(sel)) linkAt(sel).classList.remove("sel");
    sel = (sel + d + links.length) % links.length;
    if (linkAt(sel)) { linkAt(sel).classList.add("sel"); linkAt(sel).scrollIntoView({ block: "nearest" }); }
  }

  input.addEventListener("focus", load);
  input.addEventListener("input", function () { load(); render(input.value); });
  input.addEventListener("keydown", function (e) {
    if (e.key === "ArrowDown") { e.preventDefault(); move(1); }
    else if (e.key === "ArrowUp") { e.preventDefault(); move(-1); }
    else if (e.key === "Enter") { var a = linkAt(sel > -1 ? sel : 0); if (a) location.href = a.href; }
    else if (e.key === "Escape") { input.value = ""; render(""); input.blur(); }
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "/" && document.activeElement !== input) { e.preventDefault(); input.focus(); }
  });
  document.addEventListener("click", function (e) {
    if (!box.contains(e.target) && e.target !== input) box.hidden = true;
  });
})();
