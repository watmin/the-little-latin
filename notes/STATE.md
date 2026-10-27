# STATE: resumption notes for The Little Latin

_Last updated: 2026-10-26 (America/Los_Angeles)_

## What exists
- Repo: https://github.com/watmin/the-little-latin (public). Site: https://watmin.github.io/the-little-latin/ (MkDocs Material, GitHub Actions deploy on push to main; Pages source = GitHub Actions, set by John manually).
- Published: `docs/index.md`, `docs/chapters/01-salve.md` (Book I Ch1).
- Unpublished planning in `notes/` (outside docs/, not built): scope-map.md, dependency-order.md (6 books × 12 = 72 chapters), judging.md, reviews/.
- Local working copy: /workspace/tll on the shared box. Push via `https://x-access-token:$LATIN_REPO_GH_TOKEN@github.com/watmin/the-little-latin.git`. The token is a fine-grained PAT for this repo only (Contents/Pages/Workflows write; no Administration). Never print it.

## Decisions
- Format: Little Schemer Q|A two-column tables, tiny steps, learner induces rules, Law/Commandment admonitions, playful, food/everyday examples.
- Classical (restored) pronunciation. **Macrons on every long vowel, always.** Flag ecclesiastical habits (John had Catholic-school Latin early on, classics in college).
- Goal: conversational Latin + reading real authors. Chunks before rules.
- Every chapter ends with "Speak it aloud" + Homework; grading is done by voice chat with Grok Bot.
- Chapter files: `docs/chapters/NN-slug.md` (global numbering 01–72); add each to the `nav` in mkdocs.yml. Consider nav grouping by Book once Book I has more than 3 chapters.

## John's preferences / weak spots
- Reads almost only on his phone. Retained pronunciation, remembers almost no vocabulary.
- Rusty: cases/declensions, verb person/number/tense/mood/voice, imperatives, infinitives & participles ("totally forgot"), gerunds, sentence structure, adjective/adverb agreement.
- Voice check note: said "grātis" for "grātiās". Retest.
- Wants frequent additions (a few times a day) and durable, substantial content.

## Next steps
1. Write Book I Ch2 "Quid est?" per dependency-order.md; run judging.md; review file; push.
2. Restructure mkdocs nav into Books.
3. Apply L3s from reviews/2026-10-26-scope-and-order.md when touching those chapters.
4. Maybe add a glossary/vocab page per book and a grammar-tables appendix (published).
