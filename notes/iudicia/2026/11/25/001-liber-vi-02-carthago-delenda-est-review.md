# Review: Liber VI Caput II (Ch62) "Carthāgō Dēlenda Est" (gerundive)

_2026-11-25 morning. Rubric: notes/consilia/2026/10/26/003-judging-rubric.md. Draft: notes/commentarii/2026/11/25/001-liber-vi-02-carthago-delenda-est-draft.md. Published: docs/liber-vi/02-carthago-delenda-est.md + docs/liber-vi/cards/02-carthago-delenda-est.yml._

## Scores
- Accuracy: good after fixes (2 L1 below). Every quoted real-Latin line was checked against fetched source text (list below). Macrons checked against Wiktionary for the doubtful ones (*īnfitior, inexpiābilis, dēcerpō, dēmō, Nāsīca, cēnseō, pactum* short *a*, *mehercule* short vowels).
- Logic: title → "is it a gerund?" (Ch61's Missing Nominative test) → name → fourth verb-adjective (fills the passive/ahead corner of Ch37–39) → Cato's real words → forms → must-be → dative doer → it-must → the swap → plain adjective → reported speech → gerund-vs-gerundive test → drills → Lectiō → Auctor. Each frame is answerable from earlier frames or glosses.
- Ordering: gerundive only; no supine (Ch63 named only in the closing box). Nepos 1.1 *antecēdat* (subjunctive in a subordinate clause of reported speech) is flagged as Chapter 64, not taught. Florus's *nē metū ablātō …* clause left out (paraphrased in English). Everything else uses Book I–V grammar: acc + inf (Ch42), *cum* (Ch55), tucked-in question/command (Ch53/56), not-really if (Ch57), *quamquam* (Ch59), future imperative (Ch47), untied pair (Ch40).
- Structure: 16 groups g-01–g-16, every table has a marker, every `##` has a motto; 6 Law boxes + closing box; Lectiō in `::: dialogue lectio` (28 lines) and Pliny in `::: dialogue auctor` (7 lines); Speak it aloud + Vocābula (16 rows) + Homework checkboxes; 77 frames (in band). `mkdocs build --strict` passes.
- Usefulness: "I have to ___" (*Mihi … est / Mihi eundum est*), "must / must not be done," "I think it must be" are everyday speaking frames; the swap unlocks a very common prose pattern (Caesar's *ad eās rēs cōnficiendās*). Real lines from Caesar, Horace, Juvenal, Cicero, Nepos, Vergil, Pliny, Florus, *On Famous Men*.
- Cards: 83 (16 vocab = every Vocābula row, 54 forms, 7 choose with why, 6 error). All six Laws carded (f-10, f-18, f-22, f-27, f-33, f-46).

## L1 (fixed)
1. §15 Auctor label said "15.74 from *namque* to the end, and the first sentence of 15.75 … the rest of 15.75 left out," but the passage shown runs through the *second* sentence of 15.75 (*Statimque sūmptum est … raptō*). → "15.74 from *namque* to the end and 15.75 up to *raptō* … the opening sentence of 15.74 and the last sentence of 15.75 are left out"; also notes the added quotation marks.
2. §2 claimed "What ancient writers do give is a gerundive in reported speech, every time," but Plutarch (Greek) has no gerundive. → "What the Latin writers who report it do give is a gerundive in reported speech, every one of them."

## L2 (fixed)
1. §2 "Both are modern summaries (around 1800)": only the short slogan dates from then; the long *Cēterum cēnseō* form is also modern but not dated. → "Both are modern forms (the short slogan took shape around 1800)."
2. §2 "After Hannibal's war … he ended every speech": the campaign was some fifty years after Zama. → "Long after Hannibal's war."
3. §2 *On Famous Men* dated "about AD 400": usually put in the 4th century. → "from the 300s AD."
4. §7 Caesar BG 1.3.1 dated "58 BC": the Helvetian plan is 61 BC (departure set for the third year). → "A few years before Caesar arrives."
5. §3 "The one form where a deponent really is passive" overclaims (a few deponent perfect participles are used passively). → "Deponents have active meanings everywhere else, but their gerundive is passive."
6. §15 *quamquam Catōne annō sequente raptō* (quamquam with an ablative absolute, no verb) was unexplained. → glossed in the Auctor intro as Ch59 *quamquam* + Ch40 untied pair.
7. §14 intro said yesterday's cheese is "still on the table," but Ch61's reading game handed out bits of it. → "What's left of Grandma's new cheese … is back on the table."
8. §14 Lectiō English for *Nēminī? Etiam Avō?* ("Not by anyone? Not even by Grandpa?") didn't match the Latin. → "By nobody? Even by Grandpa?"
9. §8 *iūs* glossed as "a right, a binding word" (loose). → "law, a binding formula."
10. §9 Nasica's reason paraphrased as "Rome would grow careless" (Florus: *luxuriārī fēlīcitās urbis*). → "Rome's good fortune would run wild."
11. Florus cited only as 1.31. → "1.31 (2.15 in some editions)."
12. Build: two Auctor lines lacked the English speaker (`|| Pliny | …`), which crashed hooks/frames.py. → added.
13. Render: the closing success box's "___ing" … "___ed" pair, followed by `*`/`**` markup, was eaten by the emphasis parser (garbled text). → underscores escaped in that line; rendered text re-checked for stray `*`/`_` (none).
14. Lectiō used *ēmptum esse / ēmptus est*; the book's settled form is *emptum* (iudicia 2026/11/06/002; Ch37 on). → *emptum / emptus* (Pliny's *dēmptam* keeps the long *ē* of *dē-*).

## L3 (logged)
- Chapter 39 (docs/liber-iv/03-laudaturus.md, g-06) says the passive periphrastic "waits for Liber V"; it came in Liber VI. Ch62 g-01 acknowledges it ("it waited one book longer"). A one-word touch-up to Ch39 (V → VI) is cheap; left for John to OK.
- 77 frames, 83 cards (more forms cards than usual because of the real lines).
- Pliny's *hanc pōmum … dēmptam* explained as agreement by sense with *fīcus* (f.); standard explanation, not checked against a commentary.
- *tertium ante diem* translated "three days ago" (the usual rendering; Roman inclusive counting would make it two by our count). Not mentioned.
- Not taught: gerundive of *ūtor/fruor/potior* (*ūtendus*), *cūrō* + gerundive (*pontem faciendum cūrat*), gerundive with *dō/trādō*, the dative gerundive of purpose (*decemvirī lēgibus scrībundīs*), *nōn est quod*. Possible later readings.
- Nepos 12.5 *neque sibi diūtius vītam esse retinendam* (real dative of agent; Hannibal's death) verified but left out on tone.
- Caesar 2.20.1 printed with commas and ellipses for the original semicolons.
- New canon: day 30, the family "senate" (Grandpa as Cato, Grandma as Scipio Nasica), the dog "destroys" the cheese (*Cāseus dēlētus est*), Grandpa to the forum tomorrow *cāseī emendī causā* (Ch63 can open there).

## Real Latin verified (fetched 2026-11-25)
- Pliny, NH 15.74–75 (la.wikisource and LacusCurtius, both Mayhoff; also agoraclass): *namque perniciali odio Carthaginis flagrans nepotumque securitatis anxius, cum clamaret omni senatu Carthaginem delendam, adtulit quodam die in curiam praecocem ex ea provincia ficum ostendensque patribus: Interrogo vos, inquit, quando hanc pomum demptam putetis ex arbore. cum inter omnes recentem esse constaret: Atqui tertium, inquit, ante diem scitote decerptam Carthagine. tam prope a moeris habemus hostem! statimque sumptum est Punicum tertium bellum, quo Carthago deleta est, quamquam Catone anno sequente rapto* ✓.
- Florus, Epit. 1.31 (Latin Library florus1, ch. XXXI): *Cato inexpiabili odio delendam esse Carthaginem, et cum de alio consuleretur, pronuntiabat, Scipio Nasica servandam* ✓.
- *De viris illustribus* 47.8 (Latin Library victor.ill): *Carthaginem delendam censuit* ✓.
- Plutarch, Cato Maior 27.1 (Greek, socratos/Perrin): *δοκεῖ δέ μοι καὶ Καρχηδόνα μὴ εἶναι*; figs dropped from the toga, "three days' sail" ✓.
- Caesar BG 2.20.1: *Caesari omnia uno tempore erant agenda: vexillum proponendum … signum tuba dandum; ab opere revocandi milites; qui paulo longius aggeris petendi causa processerant arcessendi; acies instruenda; milites cohortandi; signum dandum* ✓.
- Caesar BG 1.3.1 *Ad eas res conficiendas biennium sibi satis esse duxerunt* ✓; 1.3.3 *Ad eas res conficiendas Orgetorix deligitur* ✓.
- Horace, Odes 1.37.1–2: *Nunc est bibendum, nunc pede libero / pulsanda tellus* ✓.
- Juvenal 10.356: *orandum est ut sit mens sana in corpore sano* ✓.
- Cicero, Cat. 1.17: *Servi mehercule mei si me isto pacto metuerent, ut te metuunt omnes cives tui, domum meam relinquendam putarem* ✓.
- Vergil, Aen. 3.658: *monstrum horrendum, informe, ingens* ✓.
- Nepos, Hann. 1.1 *non est infitiandum Hannibalem tanto praestitisse ceteros imperatores prudentia, quanto populus Romanus antecedat fortitudine cunctas nationes* ✓; 8.3 *in agendo bello* ✓; 10.3 *Ad hunc interficiundum talem iniit rationem* ✓; 10.4 *dolo erat pugnandum, cum par non esset armis* ✓; 11.3 *ad irridendum eum* ✓ (Ch61).
