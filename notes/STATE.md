# STATE: resumption notes for The Little Latin

_Last updated: 2026-10-26 (America/Los_Angeles)_

## What exists
- Repo: https://github.com/watmin/the-little-latin (public). Site: https://watmin.github.io/the-little-latin/ (MkDocs Material, GitHub Actions deploy on push to main; Pages source = GitHub Actions, set by John manually).
- Published: `docs/index.md` (intro + list of the six books), `docs/liber-i/01-salve.md` (Liber I Caput I "Salvē!", rewritten in full 2026-10-26; the original proof-of-concept chapter was scrapped).
- Site path convention: `docs/liber-<roman>/NN-slug.md` (NN = chapter within the book), nav grouped as "Liber I: Prīma Verba" etc.
- Unpublished workshop in `notes/` (outside docs/, never built). Convention: `notes/<category>/YYYY/MM/DD/NNN-slug-name.md`, ASCII paths with no macrons, NNN = per-day sequence per category. Categories: `consilia/` (plans), `iudicia/` (reviews), `acta/` (session logs, grades, voice results), `commentarii/` (working notes). See `notes/README.md`.
- Current files:
  - `notes/consilia/2026/10/26/001-scope-map.md`: full grammar/skills inventory, cross-checked against Wheelock, LLPSI, and CLC
  - `notes/consilia/2026/10/26/002-dependency-order.md`: prerequisite graph + 6 books × 12 = 72 chapters
  - `notes/consilia/2026/10/26/003-judging-rubric.md`: rubric (accuracy, logic, ordering, structure, usefulness; L1/L2/L3)
  - `notes/iudicia/2026/10/26/001-scope-and-order-review.md`: first judging pass
  - `notes/commentarii/2026/10/26/001-liber-i-01-salve-draft.md`: Ch1 draft (published copy is canonical)
  - `notes/iudicia/2026/10/26/002-liber-i-01-salve-review.md`: Ch1 judging pass (1 L1, 4 L2, all fixed)
  - `notes/acta/`: empty so far
- Local working copy: /workspace/tll on the shared box. Push via `https://x-access-token:$LATIN_REPO_GH_TOKEN@github.com/watmin/the-little-latin.git`. The token is a fine-grained PAT for this repo only (Contents/Pages/Workflows write; no Administration). Never print it.

## Decisions
- Format: Little Schemer Q|A two-column tables, tiny steps, learner induces rules, Law/Commandment admonitions, playful, food/everyday examples.
- Classical (restored) pronunciation. **Macrons on every long vowel, always.** Flag ecclesiastical habits (John had Catholic-school Latin early on, classics in college).
- Goal: conversational Latin + reading real authors. Chunks before rules.
- Every chapter ends with "Speak it aloud" + Homework; grading is done by voice chat with Grok Bot.
- Chapter files: `docs/liber-<roman>/NN-slug.md`; add each to the `nav` in mkdocs.yml under its Liber. Workflow: draft in commentarii → judge → review in iudicia → fix L1/L2 → copy to docs → `mkdocs build --strict` (local venv at /tmp/mk, may need recreating) → push → confirm deploy. Consider nav grouping by Book once Book I has more than 3 chapters.

## John's preferences / weak spots
- Reads almost only on his phone. Retained pronunciation, remembers almost no vocabulary.
- Rusty: cases/declensions, verb person/number/tense/mood/voice, imperatives, infinitives & participles ("totally forgot"), gerunds, sentence structure, adjective/adverb agreement.
- Voice check note: said "grātis" for "grātiās". Retest.
- Wants frequent additions (a few times a day) and durable, substantial content.

## Next steps
1. Write Liber I Caput II "Quid est?" (docs/liber-i/02-quid-est.md) per the dependency order; run the judging rubric; write the review into notes/iudicia/<date>/; push. Log voice grades in notes/acta/<date>/.
3. Apply L3s from notes/iudicia/2026/10/26/001-scope-and-order-review.md when touching those chapters.
4. Maybe add a glossary/vocab page per book and a grammar-tables appendix (published).

## Chapter markup conventions (implemented by hooks/frames.py)
- **Group bookmarks (one per question group, not per question):** put a marker line `{#g-NN}` directly above each Question|Answer table. It renders as a tappable 🔖 NN badge with id `g-NN`, so `…/01-salve/#g-07` is a bookmarkable link. Numbering is per chapter.
- **Stability rule:** markers are never renumbered once published. A group inserted later takes the previous marker plus a letter suffix (`g-07a`, `g-07b`). A removed group's number is retired, never reused. Run `python3 tools/number_frames.py <file>` to fill in missing markers: a file with no markers gets g-01, g-02, …; otherwise new groups get suffixes. Individual frames have no anchors (an earlier per-frame `f-NNN` scheme was dropped on 2026-10-26 at John's request).
- **Section mottos:** right after each `##` heading, add one line `:: Latin motto || English gloss`. Use simple, accurate Latin with macrons; famous sayings are OK if attributed. It renders as the Latin with a small italic gloss beneath.
- **Heading permalinks:** `toc: permalink: true` is on; headings show a ¶ link.
- Styles: docs/stylesheets/extra.css. The bookmarked group's table is outlined when it's the URL target.

## Hidden answers ("wax tablets"; docs/javascripts/extra.js + extra.css)
- Only tables directly after a `{#g-NN}` group marker count as frame tables. Their Answer column (2nd cell of each body row) is covered by a wax-tablet texture with the hint "tange ✎". Vocabulary and Law tables are untouched.
- Tap, click, Enter, or Space reveals the answer (a short melt/fade-in); tapping again re-covers it. Cells are role=button, focusable, with aria-expanded and aria-label.
- Persistence: localStorage key `tll:revealed:<page path>`, an object of `<group id>:<row index>` → 1. Because group IDs are stable, a group's revealed state survives reloads. If rows are later inserted in a published group, row indexes shift; that only affects which answers are shown, never the content.
- Controls: each group's badge row has "Ostende omnia · reveal all" and "Tege · hide all"; the page ends with "Dēlē tabulās · hide every answer on this page" (clears that page's key).
- Works with Material instant navigation via `document$.subscribe`. Has dark-mode wax colors and honors prefers-reduced-motion.

## Homework checkboxes
- Write homework as task-list items, `- [ ] item`. pymdownx.tasklist (custom_checkbox, clickable_checkbox) renders real checkboxes, and extra.js re-enables them. State is saved in localStorage under `tll:tasks:<page path>`, keyed `<index>:<first 40 chars>`, using the same robust init as the reveal code.
- Styling: each box is a wax tablet with a Roman red (#8b1e1e) border and a gold ring. When ticked, a gold Cinzel ✓ pops in. Ticked text turns italic with a gold strikethrough. A small press animation runs on tap (skipped with reduced motion). The tap target is the whole 2.9em left gutter. Dark mode uses deeper wax.

## Coverable blocks (toggles instead of "cover it with your hand")
- Markdown:
  ```
  ::: cover <id> "<label>" shown|hidden
  …any markdown…
  :::
  ```
  `hooks/frames.py` turns this into a `div.tll-cover`. `extra.js` adds a red-and-gold Cinzel button above it ("Ostende · show <label>" / "Tege · hide <label>", at least 44px tall). A covered block sits under a wax tablet; tapping the tablet also uncovers it. State is saved in localStorage under `tll:covers:<page path>` → `{id: shown|hidden}`, with the same robust init as the other features. Use a unique `<id>` per block within a page, and never rename it once published.
- Never write "cover X with your hand/thumb" in prose; use a cover block. Ch1 Lectiō has `lectio-la` (Latin, shown) and `lectio-en` (English translation, hidden by default).
- Reveal robustness: extra.js covers every Question|Answer table between a group marker and the next marker or heading, so a Law box or prose in the middle of a group is fine. Row keys: the first table is `g-NN:<row>`, later tables are `g-NN:t<k>:<row>`. All plain tables render full width.

## Two-column dialogue (reading texts)
- Markdown, one line per utterance:
  ```
  ::: dialogue <id>
  Magistra | Salvēte, discipulī! || Teacher | Hello, students!
  :::
  ```
  The format is `Latin speaker | Latin text || English speaker | English text`, with inline `*em*` / `**strong**` allowed. hooks/frames.py renders a two-column grid at every width (phone included), Latin on the left and English (italic) on the right, one row per line, under a Latīna | Anglica header. The font is compact at 390px with wrapping and no horizontal scroll.
- extra.js: every cell has its own tap-to-toggle wax cover; Latin is shown by default and English covered. Tap or Enter toggles one cell. Bar buttons: "Ostende/Tege Anglica" (all English) and "Ostende/Tege Latīna" (all Latin, for the reverse drill). State is saved per line under `tll:dlg:<page path>` → `<id>:<line>:<la|en>`. Uses the same robust init. Don't reorder lines once published; append new ones.
- Ch1 Lectiō uses `::: dialogue lectio` (it replaced the earlier two `::: cover` blocks; the cover pattern remains available).
