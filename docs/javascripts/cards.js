/* The Little Latin: Tabellae (cards). One component, three scopes (data-scope = all | book | chapter).
   Only the global selection persists (tll:cards:unlocked, tll:cards:types). No answer history. */
(function () {
  const N = 20;
  const TYPES = { vocab: "vocab", forms: "forms", choose: "choose", error: "error" };
  const ROMAN = ["i", "ii", "iii", "iv", "v", "vi"];
  const get = (k, d) => { try { const v = JSON.parse(localStorage.getItem(k)); return v == null ? d : v; } catch (e) { return d; } };
  const put = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} };
  let dataP = null;
  function data(root) {
    if (!dataP) {
      const base = document.querySelector("script[src*='javascripts/cards.js']").src.split("javascripts/cards.js")[0];
      dataP = fetch(base + "cards.json", { cache: "no-cache" }).then((r) => r.json()).then((d) => { d.base = base; return d; });
    }
    return dataP;
  }
  function shuffle(a) { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }
  const el = (tag, cls, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; };

  function draw(cards) {
    // Uniform over the pool: each card equally likely. A vocab card gets a random direction,
    // so both directions appear across rounds but only one per word per round.
    return shuffle(cards.slice()).slice(0, N).map((c) => ({ c, dir: c.type === "vocab" ? (Math.random() < 0.5 ? "la" : "en") : null }));
  }

  function render(mount, d, keys, types) {
    const box = mount.querySelector(".tll-quiz-round") || mount.appendChild(el("div", "tll-quiz-round"));
    box.innerHTML = "";
    const titles = {}; d.chapters.forEach((c) => (titles[c.key] = c));
    const pool = d.cards.filter((c) => keys.includes(c.key) && types.includes(c.type));
    if (!pool.length) { box.appendChild(el("p", "tll-quiz-empty", "No cards in this selection yet. Open <em>Librī</em> and pick a chapter.")); return; }
    const round = draw(pool);
    box.appendChild(el("p", "tll-quiz-count", round.length + " of " + pool.length + " cards"));
    const mark = el("p", "group-mark", '<a class="group-id" id="g-quiz" href="#g-quiz" title="This round">🂠 round</a>');
    box.appendChild(mark);
    const t = el("table", "tll-quiz-table", "<thead><tr><th>Question</th><th>Answer</th></tr></thead>");
    const tb = el("tbody");
    round.forEach(({ c, dir }) => {
      const ch = titles[c.key];
      let q, a;
      if (c.type === "vocab") {
        q = dir === "la" ? '<span lang="la">' + c.la + "</span> = ?" : c.en + " → <em>Latīnē?</em>";
        a = dir === "la" ? c.en : '<span lang="la">' + c.la + "</span>";
      } else { q = c.q; a = c.a; }
      const tag = '<a class="tll-card-tag" href="' + d.base + c.ref + '">' + ch.book.toUpperCase() + "." + ch.ch + " · " + c.type + "</a>";
      const tr = el("tr");
      tr.appendChild(el("td", null, q + "<br>" + tag));
      tr.appendChild(el("td", null, a));
      tb.appendChild(tr);
    });
    t.appendChild(tb);
    box.appendChild(t);
    const again = el("p", "tll-quiz-again");
    const b = el("button", "tll-ctl", "Nova manus · new round"); b.type = "button";
    b.addEventListener("click", () => { render(mount, d, keys, types); if (window.tllInit) window.tllInit(); mount.scrollIntoView({ behavior: "smooth" }); });
    again.appendChild(b); box.appendChild(again);
  }

  function selector(mount, d, onChange) {
    const all = d.chapters.map((c) => c.key);
    let unlocked = get("tll:cards:unlocked", null);
    if (!Array.isArray(unlocked) || !unlocked.length) unlocked = all.slice();
    unlocked = unlocked.filter((k) => all.includes(k));
    if (!unlocked.length) unlocked = all.slice();
    let types = get("tll:cards:types", Object.keys(TYPES));
    if (!Array.isArray(types) || !types.length) types = Object.keys(TYPES);
    const outer = el("details", "tll-sel");
    const sum = el("summary"); outer.appendChild(sum);
    const books = ROMAN.filter((b) => d.chapters.some((c) => c.book === b));
    const refresh = () => {
      sum.textContent = "Librī · " + unlocked.length + "/" + all.length + " capita";
      outer.querySelectorAll("details.tll-sel-book").forEach((bd) => {
        const b = bd.dataset.book, ks = d.chapters.filter((c) => c.book === b).map((c) => c.key);
        const n = ks.filter((k) => unlocked.includes(k)).length;
        bd.querySelector("summary").textContent = "Liber " + b.toUpperCase() + " · " + n + "/" + ks.length + " capita";
        const whole = bd.querySelector("input.tll-sel-whole");
        whole.checked = n === ks.length; whole.indeterminate = n > 0 && n < ks.length;
        bd.querySelectorAll("input[data-key]").forEach((i) => (i.checked = unlocked.includes(i.dataset.key)));
      });
    };
    const save = () => { put("tll:cards:unlocked", unlocked); put("tll:cards:types", types); refresh(); onChange(unlocked, types); };
    books.forEach((b) => {
      const bd = el("details", "tll-sel-book"); bd.dataset.book = b;
      bd.appendChild(el("summary"));
      const ks = d.chapters.filter((c) => c.book === b);
      const wl = el("label", "tll-sel-row tll-sel-wholerow"); const w = el("input", "tll-sel-whole"); w.type = "checkbox";
      w.addEventListener("change", () => { const keys = ks.map((c) => c.key); unlocked = unlocked.filter((k) => !keys.includes(k)); if (w.checked) unlocked = unlocked.concat(keys); save(); });
      wl.append(w, " Tōtus liber · whole book"); bd.appendChild(wl);
      ks.forEach((c) => {
        const l = el("label", "tll-sel-row"); const i = el("input"); i.type = "checkbox"; i.dataset.key = c.key;
        i.addEventListener("change", () => { unlocked = unlocked.filter((k) => k !== c.key); if (i.checked) unlocked.push(c.key); save(); });
        l.append(i, " " + c.title); bd.appendChild(l);
      });
      outer.appendChild(bd);
    });
    const tf = el("div", "tll-sel-types"); tf.appendChild(el("span", null, "Genera: "));
    Object.keys(TYPES).forEach((ty) => {
      const l = el("label", "tll-sel-type"); const i = el("input"); i.type = "checkbox"; i.checked = types.includes(ty);
      i.addEventListener("change", () => { types = types.filter((x) => x !== ty); if (i.checked) types.push(ty); save(); });
      l.append(i, " " + ty); tf.appendChild(l);
    });
    outer.appendChild(tf);
    mount.appendChild(outer);
    refresh();
    return [unlocked, types];
  }

  function mountOne(mount) {
    if (mount.dataset.tllQuizReady) return;
    mount.dataset.tllQuizReady = "1";
    data().then((d) => {
      const loading = mount.querySelector(".tll-quiz-loading"); if (loading) loading.remove();
      const scope = mount.dataset.scope;
      let keys, types = Object.keys(TYPES);
      if (scope === "all") {
        [keys, types] = selector(mount, d, (k, t) => { render(mount, d, k, t); if (window.tllInit) window.tllInit(); });
      } else if (scope === "book") {
        keys = d.chapters.filter((c) => c.book === mount.dataset.book).map((c) => c.key);
      } else {
        keys = d.chapters.filter((c) => c.book === mount.dataset.book && String(c.ch) === mount.dataset.ch).map((c) => c.key);
      }
      render(mount, d, keys, types);
      if (window.tllInit) window.tllInit();
    }).catch((e) => { mount.textContent = "Couldn't load cards."; if (window.console) console.error("tll cards", e); });
  }
  function init() { document.querySelectorAll(".tll-quiz").forEach(mountOne); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
  try { if (window.document$ && window.document$.subscribe) window.document$.subscribe(init); } catch (e) {}
})();
