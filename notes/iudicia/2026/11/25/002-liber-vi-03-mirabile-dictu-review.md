# Review: Liber VI Caput III (Ch63) "Mīrābile Dictū" (supine)

_2026-11-25 evening. Rubric: notes/consilia/2026/10/26/003-judging-rubric.md. Draft: notes/commentarii/2026/11/25/002-liber-vi-03-mirabile-dictu-draft.md. Published: docs/liber-vi/03-mirabile-dictu.md + docs/liber-vi/cards/03-mirabile-dictu.yml._

## Scores
- Accuracy: good after fixes (3 L1 below). Every quoted real-Latin line was checked against fetched source text (list below). Grammar claims checked against Allen and Greenough §§508–510 (Dickinson College Commentaries): *-um* after verbs of motion, may take an object; *-um īrī* = future passive infinitive, rare; *-ū* with a few adjectives and *fās, nefās, opus*; "in appearance an Ablative of Specification"; never with an object; common *-ū* supines *audītū, dictū, factū, inventū, memorātū, nātū, vīsū*; *facilis/difficilis* more often take *ad* + gerund. Macrons checked against Wiktionary for the doubtful ones (*Hadrūmētum, bīduum, Numida, supīnus, mīrābilis, cubō/cubitum, dēfendō/dēfēnsum, grātulor, queror, nūbō, Maecēnās, lippus, incrēdibilis, adfābilis, cōnflīgō, custōdiō, mercātor, lūdō/lūsum*); *emptum* short *e* per the book's settled form.
- Logic: title → *dictū* is the fourth key, doesn't agree → name (Ch25 "for later," Ch41 "grammar books name it later") → fourth-family endings (Ch23 *manum, manū*) → two cases only → *-um* as Ch8's goal accusative → real *-um* lines → five ways to say "came to buy" (Ch51, Ch61–62) → *-um īrī* (Ch41 paid off) → *-ū* as Ch35's ablative of respect (*nātū* paid off) → the short list + *fās/nefās* (Ch53's *scīre nefās* paid off) → Vergil's four *mīrābile dictū* → all verb-nouns lined up → drills → Lectiō → Auctor. Each frame is answerable from earlier frames or glosses.
- Ordering: supine only; nothing from Ch64 (no subordinate clauses inside reported speech; the Lectiō's last line uses Ch53's tucked-in question and only previews Ch64). Everything else is Book I–V grammar: goal accusative (Ch8, Ch45), ablative of respect/degree (Ch35), participles (Ch37–40), reported speech (Ch42), purpose *ut*/*quī* (Ch51), matching rule (Ch54), *cum* (Ch55), tucked-in question (Ch53), gerund/gerundive (Ch61–62). Cicero's *ut* + indicative "when" and *quīn et*, *Ō* + accusative are glossed in place.
- Structure: 16 groups g-01–g-16, every table has a marker, every `##` has a motto; 6 Law boxes + closing box; Lectiō in `::: dialogue lectio` (29 lines) and Nepos in `::: dialogue auctor` (8 lines); Speak it aloud + Vocābula (16 rows) + Homework checkboxes; 80 frames (top of band). `mkdocs build --strict` passes; rendered text checked for stray `*`, `_`, `:::`, `||` (none after the fix below).
- Usefulness: *Eō cubitum / Cubitum eāmus*, "I'm going to ___," "came to ___" five ways, "easy to say, hard to do," *mīrābile dictū*, *nefās est dictū* are everyday speaking frames; for reading, the supine is common in Caesar/Livy/Sallust and in Vergil's asides. Real lines from Vergil (×5), Plautus, Horace, Caesar (×2), Nepos (×2), Ovid, Cicero (×4), Terence, Livy, Sallust (×2).
- Cards: 83 (16 vocab = every Vocābula row, 54 forms, 7 choose with why, 6 error). All six Laws carded (f-05, f-20, f-23, f-28, f-34, f-45).

## L1 (fixed)
1. Build: two vocab cards (*fās, nefās (no other forms)*, *grātulor … sum + dat.*) didn't match the Vocābula italic text the hook compares against, so card validation would fail. → card `la` = *fās, nefās* and *grātulor, grātulārī, grātulātus sum* (the extra notes moved into `en`).
2. §9 motto cited *Mōnstrum horrendum, ingēns* as "*Aeneid* 4.181; Chapters 20 and 62," implying it was the line those chapters quoted. Chapters 20/62 quote 3.658 (the Cyclops, *mōnstrum horrendum, īnfōrme, ingēns*); 4.181 is Rumor. → "(Vergil, *Aeneid* 4.181, about Rumor; the Cyclops got nearly the same words at 3.658, Chapters 20 and 62)."
3. §15 said the elder Scipio was beaten three times "in his first year in Italy," but the first of Nepos's three places is the Rhone, in Gaul. → "as Nepos tells it, in 4.1–2 … in 218 BC, the first year of the war: at the Rhone in Gaul, then at the Po and the Trebia in Italy" (Nepos 4.1–2 checked).

## L2 (fixed)
1. §2, §7 and the Law of the *-ū* called the *-ū* supine flatly "an ablative of respect." A&G §508 says its origin is usually taken as a dative of purpose, confused early with the ablative; §510 n.1 says "in appearance an Ablative of Specification." → §2 adds "Grammar books argue about the exact history of the *-ū*; it behaves like an ablative, so that's how this book treats it"; §7 "works just like an ablative of respect … (Allen and Greenough §510: 'in appearance an Ablative of Specification,' their name for respect)"; Law "works like."
2. §11 *Avus cāseum emptum portat* was explained as "*portō* isn't a verb of going," which is shaky (carrying is motion) and skipped the real point: the spelling coincides. → "Not a supine, though it's spelled like one … Swap in eggs (*ōva*) and it changes: *Avus ōva empta portat*. A supine never changes."
3. §6 Terence: "then meanwhile a rumor comes" for *cum intereā rūmor venit* → "when meanwhile."
4. §5 motto gloss "He came to buy; he came to buy" hid the contrast. → "He came so that he might buy; he came to buy."
5. §14 Lectiō: *Hunc emō* glossed "I'll buy this one." → "I'm buying this one."
6. §4 "deponent supines are active, like everything else a deponent does except the gerundive" overclaims (cf. Ch62 L2 #5). → "like a deponent's other forms. The gerundive is the exception."
7. Law of the Supine left out *fās/nefās* for the *-ū*. → "after an adjective (or *fās, nefās*)."
8. §9 *Aeneid* 2.174 presented the leaping statue as plain narrative; it's Sinon's lying tale. → "The Greek spy Sinon tells the Trojans a story (a lie, but a good one) …" and the answer notes why *mīrābile dictū* fits a liar.
9. §15 intro "Grandpa promised more Nepos": no such promise in Ch62. → "Grandpa reads his Nepos again."
10. Render: in the Law of the Supine box, "to ___," … "in the ___ing" was eaten by the emphasis parser (same bug as Ch62 L2 #13). → underscores in every admonition line escaped (`\_\_\_`); rendered text re-checked.
11. Card f-40 printed *monstrum* without its macron (caught before copying). → *mōnstrum*.
12. §16 sound check first said the *-ū* "never takes the emphasis … the stress follows the usual rules" (muddled). → "The final *-ū* is long, but it doesn't pull the emphasis (stress): two-syllable words stress the first syllable, longer ones follow the usual rules."
13. Draft motto for §6 printed *Rūmor vēnit* (perfect); Terence has *venit* (present). → *Rūmor venit … || A rumor comes …*
14. Draft §4 Cicero note said "Cicero's '…'" for an ellipsis that is ours. → "The '…' skips Scipio telling us how tired he was."

## L3 (logged)
- 80 frames (top of band), Lectiō 29 lines, Auctor 8 lines, 83 cards.
- *Avus cāseum emptum portat* vs a supine: the book's settled short-*e* *emptum* is used throughout.
- Terence's *quom* and *populu'* printed as *cum* and *populus* (said so in the frame).
- Cicero *Rep.* 6.10 printed with an ellipsis (skips *et dē viā fessum, et quī ad multam noctem vigilāssem*).
- Nepos's "300 miles" Zama → Hadrumetum labeled as larger than modern estimates (not tied to a specific source; Zama's site is debated).
- Lectiō *-ū* phrases *mīrābilis vīsū, incrēdibile vīsū, crēdibile audītū, mīrābile audītū* are book-made (grammatical per A&G §510; not claimed as quotations). *Facile dictū, difficile factū* labeled a teaching line.
- Not taught: *opus est* + supine (*dictū opus est*), *pudet dictū* (Tac. Agr. 32, a supine with a verb), *nūptum dare/collocāre*, the poets' infinitive after adjectives (*facilēs aurem praebēre*), supine in *-ū* as a historical dative, *fore ut* as the usual future passive infinitive.
- Verified but unused: Livy pref. 10 *foedum inceptū, foedum exitū* (not fetched successfully; left out), Sallust *Cat.* 6.2 *incrēdibile memorātū est, quam facile coaluerint*, *Georgics*/Horace line 49 *namque pila lippīs inimīcum et lūdere crūdīs* (paraphrased).
- Callback opportunity: Ch56 day 24 (*Quis custōdiet ipsōs custōdēs? Ego!*) and day 25 John as Grandpa's guard — the Lectiō's *tē custōdītum* pays it off implicitly; could be named in a later recap.
- New canon: day 31, Grandpa buys a huge cheese with Marcus and John "guarding" him and Quintus "watching," doesn't taste it (*mīrābile dictū*), Grandma gives him the first piece at dinner, the cheese is eaten at dinner, the dog goes to the kitchen *cāseum quaesītum*, Grandpa will tell tomorrow *quid mercātor dīxerit* (Ch64 can open with the seller's words in reported speech).

## Real Latin verified (fetched 2026-11-25)
- Vergil, Aen. 1.439–440 (Latin Library): *Infert se saeptus nebula, mirabile dictu, / per medios, miscetque viris, neque cernitur ulli* ✓ (printed with parentheses).
- Aen. 2.174–175: *terque ipsa solo (mirabile dictu) / emicuit parmamque ferens hastamque trementem* ✓.
- Aen. 3.621: *nec visu facilis nec dictu adfabilis ulli* ✓.
- Aen. 4.181–182: *monstrum horrendum, ingens, cui quot sunt corpore plumae, / tot vigiles oculi subter (mirabile dictu)* ✓.
- Georg. 2.30–31: *quin et caudicibus sectis (mirabile dictu) / truditur e sicco radix oleagina ligno* ✓.
- Plautus, Amph. 807: *mensa ablata est, cubitum hinc abiimus* ✓.
- Horace, Sat. 1.5.48–49: *lusum it Maecenas, dormitum ego Vergiliusque; / namque pila lippis inimicum et ludere crudis* ✓.
- Caesar, BG 1.11.2: *Haedui, cum se suaque ab iis defendere non possent, legatos ad Caesarem mittunt rogatum auxilium* ✓; 1.30.1 *totius fere Galliae legati, principes civitatum, ad Caesarem gratulatum convenerunt* ✓.
- Nepos, Hann. 6.1 *Hinc invictus patriam defensum revocatus bellum gessit adversus P. Scipionem, filium eius, quem ipse primo apud Rhodanum, iterum apud Padum, tertio apud Trebiam fugarat* ✓; 6.3 *Post id factum paucis diebus apud Zamam cum eodem conflixit: pulsus - incredibile dictu - biduo et duabus noctibus Hadrumetum pervenit, quod abest ab Zama circiter milia passuum trecenta* ✓; 6.4 *In hac fuga Numidae, qui simul cum eo ex acie excesserant, insidiati sunt ei; quos non solum effugit, sed etiam ipsos oppressit* ✓; 4.1–2 (Rhone, Clastidium on the Po, Trebia) ✓.
- Ovid, AA 1.99: *Spectatum veniunt, veniunt spectentur ut ipsae* ✓.
- Cicero, Rep. 6.10: *Deinde, ut cubitum discessimus, me et de via fessum, et qui ad multam noctem vigilassem, artior, quam solebat, somnus complexus est* ✓.
- Terence, Hec. 39–40 (Latin Library and la.wikisource): *primo actu placeo; quom interea rumor venit / datum iri gladiatores, populu' convolat* ✓.
- Livy 1.39.1: *Eo tempore in regia prodigium visu eventuque mirabile fuit* ✓.
- Cicero, Phil. 2.63: *O rem non modo visu foedam, sed etiam auditu!* ✓; Sen. 13 *Quia profecto videtis nefas esse dictu miseram fuisse talem senectutem* ✓ (printed from *Vidētis*); Tusc. 5.38 *si hoc fas est dictu* ✓.
- Sallust, Cat. 7.3 *Sed civitas incredibile memoratu est adepta libertate quantum brevi creverit* ✓; 14.1 *id quod factu facillumum erat* ✓.
