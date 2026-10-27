/* The Little Latin: wax-tablet answers. Tap to reveal; state persists per page. */
(function () {
  const KEY = () => "tll:revealed:" + location.pathname.replace(/\/+$/, "/");
  const load = () => { try { return JSON.parse(localStorage.getItem(KEY())) || {}; } catch (e) { return {}; } };
  const save = (s) => { try { localStorage.setItem(KEY(), JSON.stringify(s)); } catch (e) {} };

  function setCell(td, open, state, persist) {
    td.classList.toggle("is-revealed", open);
    td.setAttribute("aria-expanded", open ? "true" : "false");
    td.setAttribute("aria-label", open ? "Answer (tap to hide)" : "Hidden answer: tap to reveal");
    if (persist) { if (open) state[td.dataset.tllKey] = 1; else delete state[td.dataset.tllKey]; save(state); }
  }

  function init() {
    const state = load();
    const marks = document.querySelectorAll(".md-typeset .group-mark");
    if (!marks.length) return;
    marks.forEach((mark) => {
      if (mark.dataset.tllReady) return;
      mark.dataset.tllReady = "1";
      const a = mark.querySelector(".group-id");
      let next = mark.nextElementSibling;
      const table = next && (next.tagName === "TABLE" ? next : next.querySelector("table"));
      if (!a || !table) return;
      const gid = a.id;
      const cells = [];
      table.querySelectorAll("tbody tr").forEach((tr, i) => {
        const td = tr.cells[1];
        if (!td) return;
        td.classList.add("tll-answer");
        td.dataset.tllKey = gid + ":" + i;
        td.tabIndex = 0;
        td.setAttribute("role", "button");
        setCell(td, !!state[td.dataset.tllKey], state, false);
        const toggle = (e) => {
          if (e.target.closest("a")) return;
          setCell(td, !td.classList.contains("is-revealed"), load(), true);
        };
        td.addEventListener("click", toggle);
        td.addEventListener("keydown", (e) => {
          if (e.key === "Enter" || e.key === " ") { e.preventDefault(); toggle(e); }
        });
        cells.push(td);
      });
      const mk = (label, open) => {
        const b = document.createElement("button");
        b.type = "button"; b.className = "tll-ctl"; b.textContent = label;
        b.setAttribute("aria-label", (open ? "Reveal" : "Hide") + " all answers in group " + gid.slice(2));
        b.addEventListener("click", () => { const s = load(); cells.forEach((td) => setCell(td, open, s, true)); });
        return b;
      };
      mark.prepend(mk("Ostende omnia · reveal all", true), mk("Tege · hide all", false));
    });
    const article = document.querySelector(".md-content__inner");
    if (article && document.querySelector(".tll-answer") && !document.querySelector(".tll-reset")) {
      const wrap = document.createElement("p");
      wrap.className = "tll-reset-wrap";
      const b = document.createElement("button");
      b.type = "button"; b.className = "tll-ctl tll-reset";
      b.textContent = "Dēlē tabulās · hide every answer on this page";
      b.addEventListener("click", () => {
        try { localStorage.removeItem(KEY()); } catch (e) {}
        document.querySelectorAll(".tll-answer").forEach((td) => setCell(td, false, {}, false));
      });
      wrap.appendChild(b);
      article.appendChild(wrap);
    }
  }

  if (typeof document$ !== "undefined") document$.subscribe(init);
  else document.addEventListener("DOMContentLoaded", init);
})();
