/* The Little Latin: wax-tablet answers. Tap to reveal; state persists per page. */
(function () {
  document.documentElement.classList.add("tll-js");
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

  // Homework checkboxes: persist per page, keyed by item index + text.
  function initTasks() {
    const boxes = document.querySelectorAll(".md-typeset .task-list-item input[type=checkbox]");
    if (!boxes.length) return;
    const K = "tll:tasks:" + location.pathname.replace(/\/+$/, "/");
    const rd = () => { try { return JSON.parse(localStorage.getItem(K)) || {}; } catch (e) { return {}; } };
    const st = rd();
    boxes.forEach((cb, i) => {
      const li = cb.closest("li");
      const key = i + ":" + (li ? li.textContent.trim().slice(0, 40) : "");
      cb.disabled = false;
      cb.checked = !!st[key];
      if (li) li.classList.toggle("tll-done", cb.checked);
      if (cb.dataset.tllReady) return;
      cb.dataset.tllReady = "1";
      cb.addEventListener("change", () => {
        const s = rd();
        if (cb.checked) s[key] = 1; else delete s[key];
        try { localStorage.setItem(K, JSON.stringify(s)); } catch (e) {}
        if (li) {
          li.classList.toggle("tll-done", cb.checked);
          li.classList.remove("tll-pop"); void li.offsetWidth; li.classList.add("tll-pop");
        }
      });
    });
  }

  function safeInit() { try { initTasks(); } catch (e) { if (window.console) console.error("tll tasks", e); }
    try { init(); } catch (e) { if (window.console) console.error("tll init", e); } }
  // Don't depend on Material's document$: init now/at DOM ready, and again on instant navigation.
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", safeInit);
  else safeInit();
  try { if (window.document$ && window.document$.subscribe) window.document$.subscribe(safeInit); } catch (e) {}
  window.addEventListener("pageshow", safeInit);
})();
