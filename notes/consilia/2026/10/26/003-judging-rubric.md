# Judging Rubric (run on every new chapter and every plan change)

Score each dimension; record findings as L1/L2/L3 in `notes/iudicia/YYYY/MM/DD/NNN-<slug>.md`.

## Dimensions
1. **Accuracy**: Latin forms, macrons (every long vowel marked: ā ē ī ō ū ȳ), meanings, classical pronunciation claims, grammar explanations. Check doubtful macrons against a dictionary (e.g., Lewis & Short / Wiktionary / Dickinson Core Vocab).
2. **Logic**: each frame follows from prior frames; questions are answerable from what's been shown; induced rules are actually supported by the examples; no contradictions.
3. **Ordering / prerequisites**: nothing analyzed before its prerequisites (see `notes/consilia/2026/10/26/002-dependency-order.md`); early-use forms are explicitly framed as chunks.
4. **Structural correctness**: Q|A tables render, admonitions valid, macrons in headings/nav, mkdocs builds `--strict`, chapter added to nav, ~40–80 frames, ends with Speak-it-aloud drill + homework. **Every frame row has an `{#f-NNN}` anchor; published anchors are unchanged (diff against main: no anchor renumbered, removed numbers not reused; inserts use letter suffixes).** Every `##` section has a `:: Latin || gloss` motto.
5. **Directional usefulness**: does it move John toward *speaking* (usable phrases, drill) and *reading real texts* (real constructions, real vocab by frequency)? Playful Little-Schemer tone, food/everyday examples, tiny steps.

## Severity
- **L1 (blocks)**: wrong Latin, wrong grammar claim, missing/incorrect macrons on taught words, prerequisite violation that confuses, broken build. *Must fix before publish.*
- **L2 (fix now)**: unclear or skipped step, missing drill/homework, weak tie to speaking/reading, inconsistent notation, minor ordering issue. *Fix in same pass.*
- **L3 (taste)**: tone, example choice, extra jokes, optional additions. *Log; fix if cheap.*

## Procedure
1. Read target top to bottom as the learner.
2. Verify every Latin form/macron, including the section mottos (grammar, macrons, the attribution if any, and that the gloss is faithful).
3. Check against dependency graph.
4. Build locally / in CI.
5. Write review file; fix L1/L2; note L3s.
