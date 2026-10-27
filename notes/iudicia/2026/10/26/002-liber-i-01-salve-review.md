# Review: Liber I, Caput I "Salvē!" (draft: notes/commentarii/2026/10/26/001-liber-i-01-salve-draft.md)

Rubric: notes/consilia/2026/10/26/003-judging-rubric.md. Date: 2026-10-26.

## L1 (blocks; all fixed)
1. **Wrong stress on *grātiās* / *grātīs*.** The draft wrote "grā-ti-ĀS" and "grā-TĪS". Under the penult law: in *grātiās* the penult *ti* is short, so the stress goes back to *GRĀ-ti-ās*; *grātīs* has two syllables, so *GRĀ-tīs*. Fixed in §4 and §8. They now contrast by syllable count and the final vowel, not by stress.

## L2 (all fixed)
1. **Inconsistent respelling of *Cicerō*** (KIH-keh-roh vs. KI-ke-rō). Unified to KI-ke-rō, and CHEE-che-rō for the ecclesiastical form.
2. ***agō* glossed as "I do / drive / give."** It doesn't mean "give" on its own. Now: "I do, I drive"; with *grātiās*, "I give (thanks)."
3. **Lectiō dialogue lines would collapse into one paragraph in the blockquote** (Markdown soft breaks). Fixed with hard line breaks. The old Chapter 1 had the same bug.
4. **Structure:** the site moved to `docs/liber-i/01-salve.md`; the nav is now grouped "Liber I: Prīma Verba"; the index links the new path and lists the six books. `mkdocs build --strict` passes locally.

## Checks passed
- **Accuracy:** every Latin form verified: salvē/salvēte, avē/avēte, valē/valēte, quid agis/agitis, bene, optimē, satis bene, nōn male, male, grātiās (tibi agō), et tū, quid est nōmen tibi / quod nōmen tibi est, nōmen mihi est, quaesō, iterum, lentius, (nōn) intellegō, magister/magistra, discipulī, omnēs, pānis, mālum/malum, liber/līber, grātīs. Macrons present on all long vowels. Sound values are classical (c/g hard, v = w, consonantal i = y, ae = eye, s never z, t never sh/ts).
- **Logic:** the -te law is induced from salvē → salvēte before it's stated, and reinforced with avē/valē. The -s → -tis pattern is noticed, not taught as a rule.
- **Ordering:** 2nd-person verbs (agis/agitis/intellegō/agō), datives (mihi/tibi) and the plural vocative *discipulī* appear only as explicit chunks, with forward pointers to Ch5, Ch6 and Ch11. No vocative forms that differ from the nominative are used (Iūlia, magister, magistra, pānis); Quīntus is never addressed.
- **Structure:** ~150 Q/A frames in 8 sections, 3 Law/Commandment admonitions, a vocabulary table, a 10-item Speak it aloud drill, and 6 homework items.
- **Usefulness:** delivers a full greeting conversation and classroom-survival phrases for voice practice, plus a first readable dialogue (the reading goal). It retests John's grātiās/grātīs.

## L3 (logged)
- Add audio recordings per section once a TTS/voice pipeline exists.
- Possibly add *ita / minimē* (yes/no) here or in Ch2.
- Extra respellings use English approximations. Consider an IPA appendix later.
