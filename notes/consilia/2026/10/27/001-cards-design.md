# Consilium: Tabellae (Cards page), design sketch (2026-10-27)

Status: **sketch only**. Nothing built, no site code changed. For John to react to.

## 1. What the learner sees
One published page, `docs/tabellae.md` ("Tabellae · Cards"), top-level in nav.

1. **Unlock panel** (a `::: cover` block, so it collapses on phone): one checkbox per chapter, grouped by Liber, with "all of Liber I" toggles. Only chapters that have cards appear.
2. **Options**: "Lean on newest chapter" (default on), card count (default 20), type filters (vocab / forms / choose / error).
3. **The round**: up to 20 cards rendered as a normal Question|Answer table under a `{#g-01}`-style marker, so the **existing wax-tablet reveal code in extra.js works unchanged** (tap to reveal, "Ostende omnia", "Tege"). Each row shows a small tag like `I.3 · forms`.
4. "Nova manus · new round" button = reload. Refresh also deals a new round.

Persistence (localStorage, same `tll:` prefix style):
- `tll:cards:unlocked` → `["i-01","i-02","i-03"]`
- `tll:cards:opts` → `{"lean":true,"n":20,"types":["vocab","forms","choose","error"]}`
- Revealed state is **not** persisted for the round (the reveal code keys on `tll:revealed:<path>`; the Cards page should clear that key on load, or the JS gets a `data-no-persist` opt-out). Small change to extra.js, the only change it needs.

### Drawing a round (client JS, ~60 lines, new `javascripts/cards.js` or a section of extra.js)
- Pool = all cards whose `ch` is unlocked and type is enabled. Vocab cards expand into two directions (la→en, en→la) as separate candidates, but at most one direction per word per round.
- If "lean" is on: newest unlocked chapter supplies ceil(n/2) cards (or all it has, if fewer); the rest are drawn uniformly from older unlocked chapters. Else uniform.
- Fisher–Yates shuffle, no duplicates by `id`. That's the whole "difficulty" model: picking later chapters raises it, the lean keeps new stuff in front. No separate scalar for v1.

## 2. Card data format
One YAML file per chapter, next to the chapter, inside docs but excluded from pages:

```
docs/liber-i/cards/01-salve.yml
docs/liber-i/cards/02-quid-est.yml
docs/liber-i/cards/03-magnus-et-parvus.yml
```

(MkDocs only renders `.md`; YAML under docs is just copied as a static file, which is harmless. Alternatively put them in `cards/` at repo root. Either way the hook reads them.)

### Schema
```yaml
book: i            # liber, lowercase roman
ch: 3              # chapter number within the book
page: liber-i/03-magnus-et-parvus.md   # for "where was this taught" links
cards:
  - id: i03-v-magnus        # globally unique, stable, never reused (like g-NN)
    type: vocab             # vocab | forms | choose | error
    la: "magnus · magna · magnum"
    en: "big, great"
    ref: g-01               # group where it's taught → link to page#g-01
  - id: i03-f-magnus-fpl
    type: forms
    q: "*magnus* with a feminine plural noun (*mēnsae*)"
    a: "*magnae*: *mēnsae magnae*"
    ref: g-04
  - id: i02-c-quis-quid      # choose-the-word
    type: choose
    q: "Someone knocks. ___ est? (who)"
    options: [quis, quid]
    a: quis
    why: "*Quis* asks about people, *quid* about things."
    ref: g-04
  - id: i03-e-mala-pira
    type: error
    q: "*pira bona sunt* · *pira mala est*: which is wrong?"
    a: "*pira mala est*: plural subject needs *sunt*: *pira mala sunt*."
    why: "*pira* is neuter plural; the verb is plural too."
    ref: g-07
```

Fields: `id`, `type`, `ref` required on all. vocab: `la`, `en` (plus optional `gender`, `note` like "not *malum*"). forms/error: `q`, `a`, optional `why`. choose: `q`, `options`, `a`, `why` (required). Text is markdown-lite (`*italic*`, `**bold**`), rendered with the hook's existing `_inline()`.

### Build: how cards get collected
Extend `hooks/frames.py`:
- `on_config`/`on_files`: glob `docs/liber-*/cards/*.yml`, load (PyYAML is already a mkdocs dependency), **validate** (see §4 automated checks), and fail the build under `--strict` on errors (raise `PluginError`).
- Write one merged `cards.json` into the site (`on_post_build`, or emit as a generated file) with `{"chapters":[{"key":"i-03","title":"III. Magnus et Parvus","url":...}], "cards":[...]}`. Pre-render `q/a` HTML in Python so the JS just inserts strings.
- `tabellae.md` holds a placeholder `<div id="tll-cards"></div>`; JS fetches `cards.json` relative to site root, builds the table + `{#g}`-style group-mark, then calls the existing reveal init.
- Cache-busting: add `cards.json` to `_HASHES` handling (or fetch with `?v=<hash>` injected into the page).

## 3. Real example cards from Chapters 1–3 (draft starter set)

### Caput I (Salvē)
```yaml
book: i
ch: 1
page: liber-i/01-salve.md
cards:
  - {id: i01-v-salve, type: vocab, la: "salvē · salvēte", en: "hello (to one · to many)"}
  - {id: i01-v-vale, type: vocab, la: "valē · valēte", en: "goodbye (to one · to many)"}
  - {id: i01-v-quid-agis, type: vocab, la: "quid agis?", en: "how are you?"}
  - {id: i01-v-gratias-tibi-ago, type: vocab, la: "grātiās tibi agō", en: "thank you"}
  - {id: i01-v-quaeso, type: vocab, la: "quaesō", en: "please"}
  - {id: i01-v-non-intellego, type: vocab, la: "nōn intellegō", en: "I don't understand"}
  - {id: i01-v-nomen-mihi, type: vocab, la: "nōmen mihi est…", en: "my name is…"}
  - id: i01-c-salve-salvete
    type: choose
    q: "Greeting the whole class: ___, discipulī!"
    options: [salvē, salvēte]
    a: salvēte
    why: "*-te* is for more than one person; *salvē* greets one."
  - id: i01-c-malum-malum
    type: choose
    q: "Which one is the apple?"
    options: [mālum, malum]
    a: mālum
    why: "Long *ā* = apple; short *a* = a bad thing. The macron is the whole difference."
  - id: i01-e-gratis
    type: error
    q: "Saying thanks: *grātīs tibi agō*. What's wrong?"
    a: "*Grātiās tibi agō*. *grātīs* means \"for free.\""
    why: "John's own voice-check slip; keeps the retest alive."
```
(Note: *grātīs* is formally taught in Caput III; this card should carry `ch: 3` or the "for free" gloss should be cut. Exactly the kind of thing review check C5 catches. Kept here as a worked example.)

### Caput II (Quid est?)
```yaml
cards:
  - {id: i02-v-pomum, type: vocab, la: "pōmum · pōma", gender: n, en: "fruit"}
  - {id: i02-v-caseus, type: vocab, la: "cāseus · cāseī", gender: m, en: "cheese"}
  - {id: i02-v-mensa, type: vocab, la: "mēnsa · mēnsae", gender: f, en: "table"}
  - {id: i02-v-agricola, type: vocab, la: "agricola · agricolae", gender: m, en: "farmer"}
  - {id: i02-v-minime, type: vocab, la: "minimē", en: "no, not at all"}
  - {id: i02-f-ovum-pl, type: forms, q: "One *ōvum*, two…?", a: "*ōva*"}
  - {id: i02-f-liber-pl, type: forms, q: "One *liber*, many…?", a: "*librī*"}
  - {id: i02-f-nauta-gender, type: forms, q: "Gender of *nauta*?", a: "Masculine, though it ends in *-a*."}
  - id: i02-c-quis-quid
    type: choose
    q: "Someone knocks. ___ est?"
    options: [quis, quid]
    a: quis
    why: "*Quis* is for people, *quid* for things."
  - id: i02-c-nonne-num
    type: choose
    q: "You expect yes: \"___ mālum est?\" (Isn't it an apple?)"
    options: [nōnne, num]
    a: nōnne
    why: "*Nōnne* expects yes; *num* expects no."
  - id: i02-e-est-sunt
    type: error
    q: "*Māla est.* What's wrong?"
    a: "*Māla sunt.* Plural subject, plural verb."
```

### Caput III (Magnus et Parvus)
```yaml
cards:
  - {id: i03-v-ruber, type: vocab, la: "ruber · rubra · rubrum", en: "red"}
  - {id: i03-v-frigidus, type: vocab, la: "frīgidus · frīgida · frīgidum", en: "cold"}
  - {id: i03-v-acerbus, type: vocab, la: "acerbus · acerba · acerbum", en: "sour, unripe, harsh"}
  - {id: i03-v-poculum, type: vocab, la: "pōculum · pōcula", gender: n, en: "cup"}
  - {id: i03-v-sed, type: vocab, la: "sed", en: "but"}
  - {id: i03-f-magnus-fpl, type: forms, q: "*magnus* with *mēnsae*", a: "*mēnsae magnae*"}
  - {id: i03-f-plenus-npl, type: forms, q: "\"full cups\"", a: "*pōcula plēna*"}
  - {id: i03-f-ruber-f, type: forms, q: "*ruber* with *ūva*", a: "*ūva rubra* (the -er adjective drops its e, like *liber → librī*)"}
  - id: i03-c-agricola-adj
    type: choose
    q: "*agricola* ___ (good farmer)"
    options: [bonus, bona]
    a: bonus
    why: "Agreement follows gender, not rhyme. *agricola* is masculine."
  - id: i03-c-et-que
    type: choose
    q: "\"Bread and cheese\" with one word stuck on: *pānis cāseus___*"
    options: [-que, et]
    a: "-que"
    why: "*-que* attaches to the second word: *pānis cāseusque*."
  - id: i03-e-vinum-album
    type: error
    q: "*vīnum alba*. What's wrong?"
    a: "*vīnum album*. *vīnum* is neuter."
  - id: i03-e-puer-bona
    type: error
    q: "*puer bonus*, *puella bonus*. Which is wrong?"
    a: "*puella bonus* → *puella bona*."
```
Note on John's quis / quid / quod mix-up: only *quis* and *quid* have been taught so far. *quod* (relative pronoun / interrogative adjective) arrives later in the dependency order, so the three-way choose card belongs to **that** chapter's card file, not Liber I.

## 4. Workflow additions

### Drafting
- Each chapter draft in `notes/commentarii/` gets a final `## Tabellae (draft)` section with the YAML. Target: every Vocābula row → one vocab card; 3–6 forms; 2–4 choose; 2–3 error. Roughly 25–40 cards per chapter.
- On publish, copy to `docs/liber-<roman>/cards/NN-slug.yml` next to the chapter, same commit.
- Fixing an old chapter's cards later: edit in place, never change an `id`; retire ids instead of reusing them (same stability rule as `g-NN`).

### Judging (add to 003-judging-rubric.md as dimension 6 "Cards")
Automated in the build hook (fail `--strict`):
- **C1** Unique `id` across all files; id prefix matches `book`+`ch`; retired ids (list in `notes/consilia/…/retired-card-ids` or a `retired:` key) never reappear.
- **C2** Required fields per type present; `choose` has `why`, and `a` ∈ `options`.
- **C3** `ref` points to an existing `{#g-NN}` in the chapter page.
- **C4** Vocab cards match a row in that chapter's Vocābula table exactly (macrons included). Flags drift between page and cards.

Manual, in the review file (same L1/L2/L3 scale):
- **C5 Ordering (L1)**: card uses only words/forms introduced at or before its tag. No Ch3 word in a Ch2 card, no accusative before Caput IV. Recognition-only items (e.g. *optima*) don't get production cards.
- **C6 Accuracy (L1)**: every macron, gender, and form; answer agrees with what the chapter actually says.
- **C7 One right answer (L1/L2)**: choose/error cards are unambiguous; distractors are real forms, not nonsense.
- **C8 Why notes (L2)**: present on choose cards, one line, phrased like the chapter's Law boxes.
- **C9 Coverage (L2)**: Vocābula fully carded; each Law box has at least one forms or choose card.
- **C10 Phone fit (L3)**: q and a fit on one phone line where possible.

Review file gains a line under Checks: `- **Cards:** N cards (v/f/c/e counts); C1–C4 pass in build; C5–C9 notes.`

Retro-fit: one review pass carding Chapters 1–3 (this sketch is the starting point), logged in `notes/iudicia/`.

## 5. Open questions for John
1. Name/placement: "Tabellae" top-level in nav, or one Cards page per Liber?
2. Unlock granularity: per chapter (proposed) or auto-unlock "everything up to my latest chapter" with one slider?
3. Should rounds remember anything (e.g. cards you tapped "missed" come back more often)? That's a step toward spaced repetition; v1 says no.
4. Vocab direction: both directions, or Latin→English only until a word is "seen" a few times?
5. Typed answers for forms cards, or tap-to-reveal only (proposed, matches chapters)?
6. Are voice-check slips (like *grātīs*) welcome as personal cards, or keep cards strictly chapter content?
7. Is ~50% newest-chapter the right lean, or adjustable?
