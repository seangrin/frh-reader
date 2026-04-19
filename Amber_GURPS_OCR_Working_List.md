# GURPS Amber OCR Cleanup Working List

Scope: `thread_clean_reader_site/amber_diceless/GURPS_Amber_Sean_Grinslade_1993.html`.
The structured mirror at `FRH_HTML_Reader/content/amber_diceless/GURPS_Amber_Sean_Grinslade_1993.html` should receive the same content fixes through `tools/polish_amber_adaptation.py` or another synchronized update path.

PDF reference status: `pdftotext` extracted `tools/.cache/amber_diceless_pdf.txt` successfully, but the PDF text layer is itself noisy. Use it to validate canonical Amber terms and point costs, not as a clean replacement source.

## Progress

- Applied the Tier 1 mechanical cleanup pass through `tools/polish_amber_adaptation.py`.
- Regenerated both synchronized outputs:
  - `thread_clean_reader_site/amber_diceless/GURPS_Amber_Sean_Grinslade_1993.html`
  - `FRH_HTML_Reader/content/amber_diceless/GURPS_Amber_Sean_Grinslade_1993.html`
- Fixed malformed generated headings for Logrus, Trump Artistry, Shapeshifting, Magic, and Item Shapeshifting.
- Verified no remaining `<p><h2>/<p><h3>` malformed heading patterns in the flat output.
- Remaining known hard OCR block: the shapeshifting skills paragraph around the `Ifyou...` fragment still needs human reconstruction.

## Tier 1: Safe Automatic Fixes

These are spelling, missing spaces, duplicated words, or obvious OCR substitutions that GPT can fix mechanically with low risk.

- Line 57: `it is suffice to say` -> `it is sufficient to say` or `it suffices to say`.
- Line 98: `place hands in the Pattern` -> likely `place my hands in the Pattern`.
- Lines 114-117: `Heraldry(Amber...)`, `Riding(Horse...)`, `History(Amber...)`, `Driving (Car)` need spacing normalization.
- Line 121: `Area- Knowledge` -> `Area Knowledge`.
- Line 340: `one crow dinner` -> likely `one crow's dinner` or `one crow dinner` if intentional Zelazny phrasing; easy but worth quick approval.
- Line 398: `Pattern Imprint cost` -> `Pattern Imprint costs`.
- Line 405: `seek an except` -> `seek an exception`.
- Line 410: `our roll` -> `your roll`.
- Line 411: `difterence` -> `difference`.
- Line 416: `fatigue cost will buy` -> likely `fatigue cost buys`.
- Line 419: `anger Benedict` -> `angry Benedict`.
- Line 425: `this is ability` -> `this is the ability`.
- Line 426: `effect probability` -> `affect probability`.
- Line 448: `the power your drawing` -> `the power you're drawing`.
- Line 452: `lalso` -> `also`.
- Line 452: `where every you wish` -> `wherever you wish`.
- Line 453: `yourselfif` -> `yourself if`.
- Line 459: `uslng` -> `using`.
- Line 460: `ShapeShiing` -> `Shapeshifting`.
- Line 462: `Pattemn` -> `Pattern`.
- Line 463: `inherit trait` -> `inherent trait`.
- Line 465: `the the vulnerablty user` -> likely `the vulnerable user`.
- Line 479: `minutel` -> `minute!`.
- Line 489: `raise Logrus` -> `raised Logrus`.
- Line 516: `tellif` -> `tell if`.
- Line 524: `Lorus` -> `Logrus`.
- Line 525: `clills at at 15+ 15+-` -> `skills at 15+ -`.
- Lines 550-551: `cound`, `Somtimes` -> `bound`, `Sometimes`.
- Line 559: `killit` -> `kill it`.
- Line 561: `skilto` -> `skill to`.
- Line 581: `willinstantly` -> `will instantly`.
- Lines 591-593: `fullinvested`, `record on`, `inluences` -> `fully invested`, `recorded on`, `influences`.
- Line 603: `powered ito by depends the on` contains obvious fragments; can simplify to `powered by ... depends on`.
- Lines 610, 645-646, 928, 1010, 1061, 1106, 1229, 1233, 1286: duplicated words/fragments (`are are`, `tell tell`, `the the`, `an an`, `It It`, `a A`, `item item`, `change change`, `identical identical`) are safe to dedupe.
- Line 615: `Ilf` -> `If`.
- Line 652: `gate iS open` -> `gate is open`.
- Line 662: `requires the trump` -> `requires the Trumps` or `requires the trump cards`.
- Line 720: `Itis` -> `It is`.
- Line 735: `your being strangled` -> `you're being strangled`.
- Line 745: `you've turn pitch black` -> `you've turned pitch black`.
- Line 765: `your are` -> `you are`.
- Line 767: `what ever` -> `whatever`.
- Line 792: `knock unconscious` -> `knocked unconscious`.
- Lines 796-800: `stmaller`, `ckinny`, `vorsion`, `porson`, `woek`, `lorm`, `youll`, `lobe`, `necossary`, `rearrangs`, `interal` -> obvious spelling fixes.
- Lines 806-816: `abiities`, `detal`, `ot heavity`, `tolls` -> `abilities`, `detail`, `or heavily`, `rolls`.
- Line 822: `Intemnal` -> `Internal`.
- Lines 849-851: `re-leamned`, `Image a`, `Firebal`, `FIreballGcoogle`, `(M1)` -> `re-learned`, `Imagine a`, `Fireball`, `Fireball (Google-Plex?)`, `(M/H)` pending name check.
- Line 888: `skillit` -> `skill it`.
- Line 894: `anting` -> `Wanting`.
- Line 966-967: `heart of victim`, `ictims` -> `heart of the victim`, `Victims`.
- Lines 976, 984, 1014: `Itis`, `an fantastic`, `time need` -> `It is`, `a fantastic`, `time needed`.
- Line 1010: `___ne adds ndds an an hour hour` -> likely `adds an hour`.
- Line 1069: `Secondly, the can be` -> `Secondly, they can be`.
- Line 1098: `changes the tide` -> `change the tide`.
- Line 1113: `chance seems to have role` -> `chance seems to have a role`.
- Line 1134: `useless of ilumination` -> `useless for illumination`.
- Line 1151: `hne lom toi other magical detection` -> likely remove as junk after `other magical detection`.
- Line 1173: `Psche`, `our Will` -> `Psyche`, `your Will`.
- Line 1180: `artifact of creature` -> `artifact or creature`.
- Line 1147: `It the creation is actual lost` -> `If the creation is actually lost`.
- Line 1149: `steps need` -> `steps needed`.
- Line 1157: `ormal creature`, `willpossess`, `GURP` -> `normal creatures`, `will possess`, `GURPS`.
- Line 1186: `posses` -> `possess`.
- Line 1200: `a explanation` -> `an explanation`.
- Lines 1229-1233: `- - the the item item`, `persor`, `change change` -> `- the item`, `person`, `can change`.
- Lines 1278-1287: `Itis`, `polnracte`, `didentical identical`, `o contains ntains` -> `It is`, likely `the character`, `identical`, `contains`.
- Line 1293: `arifact`, `cain`, `Iynchpins` -> `artifact`, `can`, `lynchpins`.
- Line 1336: `coula` -> `could`.
- Line 1352: `sound in every` -> `found in every`.
- Lines 1375-1376: `Find what you want`, `interrupt your desires`, `mus have` -> `Finding what you want`, `interpret your desires`, `must have`.
- Lines 1384-1386: `with in`, `: "real" Realm` -> `within`, `"real" realm`.

## Tier 2: GPT Can Draft, Human Should Approve

These have likely intended readings, but the cleanup changes meaning enough that Sean should approve.

- Lines 436-453: Advanced Pattern note is scrambled at the start (`The Advanced Pattern skills are: or Note...`). GPT can reconstruct into a note plus `Pattern Vision`, but should preserve intended rule: bring Pattern to mind = `25 - IQ` seconds and can be disrupted.
- Lines 454-466: Logrus opening paragraph is heavily scrambled. Likely intended: Logrus is Chaos, counterpart to Pattern, tendrils, Black Road, madness risk. Needs reconstruction from context plus Amber terms.
- Lines 465-480: Logrus-vs-Pattern backlash sentence is scrambled. GPT can draft: contact between Logrus and Pattern/Order causes backlash, but details need approval.
- Lines 497-505: `Logrus Combat Manipulation` and `Logrus Defense` have duplicated title text and scrambled clauses. Meaning is recoverable but should be approved.
- Lines 524-536: `Logrus Healing` wording: "healing is change" is clear, but the damaged sentence should be rewritten carefully.
- Lines 552-565: Duplicate `Control Chaos Creature` paragraph and `Shadow Manipulation` are mangled together. GPT can merge into a coherent paragraph, but must not invent rules.
- Lines 588-605: Trump Artistry special note is scrambled. Likely about whether Trump power comes from Pattern/Logrus/ambient tension; needs approval.
- Lines 610-646: Trump Lore and Trump Spying have several scrambled chunks; basic intent is recoverable from adjacent text, but exact mechanics may matter.
- Lines 662-666: Trump Jamming wording: number of people blocked and push/contact consequence need approval.
- Lines 687-711: Basic Shapeshifting skills paragraph is badly scrambled but later clean text resumes. GPT can reconstruct list headings (`Shapeshift Features`, `Heal Wounds`, etc.) only with human check.
- Lines 796-823: Advanced shapeshifting section is mostly clear after spelling fixes, but `Shapeshift Internal Structures` rating `(WH)` and prereqs need confirmation.
- Lines 833-852: Magic intro examples are readable but spell examples are corrupted; exact Shadow names like `Google-Plex` need approval.
- Lines 931-942: Lynchpins note has one or two sentence-level artifacts (`I it takes`, `three second`) that GPT can repair, but spellcasting timing should be approved.
- Lines 953-969: `Mind Touch` and `Cardiac Arrest` examples have several small rule wording issues; GPT can clean, but HT ranges and lynchpin names should be preserved.
- Lines 1029-1072: Power Words overview is mostly intact but has several grammar changes that touch mechanics (`they can be negated`, "carefully guarded", Will comparison).
- Lines 1077-1082: `Chaos Negation` and `Psychic Disrupt` are partly scrambled; GPT can draft from the spell names and context, but effect details need approval.
- Lines 1094-1106: `Neural Disrupt`, `Defensive Luck`, and `Process Stuff` are readable but have broken clauses; GPT draft should be checked.
- Lines 1149-1168: Creation five-step sequence has one badly scrambled example about basic creature/artifact costs; needs approval to avoid changing cost rules.
- Lines 1238-1253: Item shapeshifting section is damaged but recoverable: item can assume shapes and retain unique qualities. Needs approval.
- Lines 1258-1273: Trump Images / Personal Trump Deck section has several word choices affecting rules (`storage`, `cards`, `sought in shadow`).
- Lines 1308-1339: Quantity Multiplier section is mostly clear until `Horde (x3)`, which is heavily scrambled but likely recoverable from Amber Diceless PDF.
- Lines 1364-1386: Shadows section is mostly readable but has multiple odd choices (`interrupt`, `mus`, `with in`, "real" Realm) where GPT can draft clean prose.

## Tier 3: Human Eyeballs Required

These passages are too scrambled to repair confidently without either the original 1993 DOC, a clean export, or Sean's approval of a reconstructed paraphrase.

- Lines 454-466: The Logrus opening paragraph before "In game terms..." is word-salad. Needs a fresh human-approved paragraph.
- Lines 552-565: The second `Control Chaos Creature`/`Shadow Manipulation` block appears to be a duplicate plus shuffled text. Need decide whether to delete duplicate, merge, or reconstruct.
- Lines 588-605: Trump source-of-power special note is conceptually important and scrambled enough to need approval.
- Lines 637-646: Trump Spying advanced mechanics are severely scrambled; exact thresholds (`18+`, `25+`) may matter.
- Lines 687-711: Basic shapeshifting skills block is word-salad, likely from a table/list export. Need original intent.
- Lines 896-930: Merlin/Jasra/sorcery example is the worst damaged section in the page. It is not safely recoverable from context alone.
- Lines 1077-1082: `Psychic Disrupt` text around true name / Pattern / Logrus / Trump contact is too scrambled for exact mechanics.
- Lines 1104-1108: `Process Stuff` effect examples are scrambled enough to require approval.
- Lines 1149-1162: Creation Step One example is scrambled and may hide cost/rule details from the original adaptation.
- Lines 1308-1339: `Horde (x3)` quantity multiplier paragraph is severely shuffled; likely should be checked against the Amber Diceless creature/artifact rules.

## Structural HTML Cleanup

These are not OCR text issues but should be fixed while editing.

- Line 454: `<p><h3 id="logrus">...` invalid nesting. Split heading out of paragraph.
- Line 588: Trump heading is embedded mid-paragraph: `... summoner. <h3 id="trump">...`. Split into paragraph ending plus heading.
- Line 833: Magic heading embedded at end of Shapeshift Blood paragraph. Split before `<h3 id="magic">`.
- Line 1238: Shapeshifting item-power heading embedded in a paragraph. Split into a proper subsection heading, possibly not using the page-level `id="shapeshifting"` because that id already belongs in the earlier Powers section.

## Suggested Repair Order

1. Add or update generator-level replacement rules for Tier 1 spelling, spacing, and duplicate-word fixes.
2. Manually rewrite Tier 2 passages in small batches, previewing each against both output structures.
3. Pause on Tier 3 and ask Sean for approval/original text, especially the Merlin/Jasra sorcery example.
4. Re-run `tools/polish_amber_adaptation.py` so both `thread_clean_reader_site` and `FRH_HTML_Reader` remain harmonized.
5. Run link checks and a fresh artifact scan for known bad fragments.
