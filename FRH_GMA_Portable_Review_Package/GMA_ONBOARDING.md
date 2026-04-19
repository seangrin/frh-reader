# GMA Onboarding — Skeleton Brief
**Package version:** v1.3 Beta
**Platform:** LLM-agnostic. These instructions apply regardless of which language model, chat interface, or tool environment you are operating in.
**Purpose:** Enough FRH context to begin apprenticeship-style reads of the Gold Star Corpus. Not a world-bible. Read this before opening any transcript segment.

---

## How To Use This Document

Read this file in full before opening any corpus file. It contains everything you need to orient yourself. When you are ready to begin reading transcripts, follow the file-reading order in the "How To Read the Corpus Files" section below.

---

## What This Campaign Is

FRH (Followers of the Right Hand) is a GURPS 3e supernatural investigation campaign set in America in 1923. Five players investigate a conspiracy involving infernal beings, soul trafficking, and organized crime, all converging toward the Great Kanto Earthquake (September 1, 1923). The campaign spans 8 recorded sessions covering August 20 through August 25, 1923 in-world. Sessions 1–4 are full-group. Sessions 5–7 are breakout sub-sessions with two players each. Session 8 is a post-campaign conversation with no play.

The GM's name is Sean. This corpus teaches you how Sean GMs.

---

## Cast Key

| Real Name | Character | Notes |
|-----------|-----------|-------|
| Sean | GM | Voices all NPCs; runs all adjudication |
| Ben | Matthew | Social lead; medium-adjacent abilities |
| Joel | Auggie | Aggressive investigator; physical emphasis |
| Ashley | Amber | Magic user; absent Session 02 (Sean carries her as NPC) |
| Shane | Preston | Joins Session 02; WWI veteran; firearms |
| Paxton | Crispin | Ghost abilities; can go insubstantial |

In the corpus speaker labels:
- `Sean_GM` — Sean as GM (includes NPC embodiment when overlaid)
- `Ben_Matthew`, `Joel_Auggie`, `Ashley_Amber`, `Shane_Preston`, `Paxton_Crispin` — player voices

---

## Session Map

| Code | Date | In-World | Players | Summary |
|------|------|----------|---------|---------|
| S01 | Mar 9 | Aug 20, 1923 | Full group | Train from Chicago; Senator Reagan; sealed car incident; first supernatural contact |
| S02 | Mar 30 | Aug 20–22 | Full group | Kansas City; Amber abducted; Preston introduced; Mr. Smoke / Bartholomar; foundry |
| S03 | May 11 | Aug 22 | Full group | Train continues; Mr. Smoke radio debrief; Preston's soul contract; Crispin outed |
| S04 | May 25 | Aug 23 | Full group | St. Louis arrival; Kobayashi compound; document reveal; Ring of Setut; hotel |
| S05 | Jun 9 | Aug 25 | Joel + Ben | Chicago; Brimstone Collective op; dream laboratory; Near Marches access unlocked |
| S06 | Jun 14 | Aug 24 | Paxton + Shane | St. Louis; Basilica heist; True Nail acquired; soul contract mechanics |
| S07 | Jul 10 | Aug 24–25 | Paxton + Shane | Brimstone Collective party; mansion heist; Anita prophecy; tunnels; escape |
| S08 | Jul 13 | Post-campaign | Joel + Ben | Conversation only; design retrospective; no play |

Note: S05 and S06/S07 are parallel tracks — they happen on overlapping in-world dates. The party split is a real in-world split, not a retcon.

---

## Major NPC Registry

These are the named NPCs you must recognize. When a segment carries an `[NPC: X]` overlay, one of these is being embodied or referenced.

### Reagan
- Function: Washington power broker; social pressure and misdirection
- Session: S01 primarily
- Performance register: patrician authority, social derailment, legitimate power weaponized
- Why he matters: clearest example of how Sean handles a player who goes sideways; Reagan as social-consequence anchor

### Mr. Smoke
- Function: Hidden mastermind; chimneyrue (see below)
- Sessions: S02 (indirect, via minion testimony), S03 (radio debrief; primary performance scene)
- True form: spider body with human face; tethered to factory chimney in Kansas City
- Performance register: sparse, implication-heavy, menacing brevity; never fully explains himself
- Why he matters: best demonstration of Sean's "say less than you know" NPC principle

### Kobayashi
- Function: Japanese organized crime operator; document broker
- Session: S04 primarily; referenced in S06
- Performance register: precise wording, formal etiquette, criminal-mastermind control; compressed exposition
- Why he matters: high-value teaching material for information economy and social stakes

### Doctor Hope
- Function: Dream researcher; Chicago laboratory
- Session: S05
- Performance register: long exposition blocks; practical pacing; teaching cosmology through procedure

### Doctor Mike
- Function: Cosmology teacher; soap-bubble dreamscape model; Near Marches theory
- Session: S05
- Performance register: conceptual, methodical, analogical; partner to Doctor Hope

### Bartholomar
- Function: Demon ally of Mr. Smoke; vessel-bound operative
- Session: S02 (vessel retired by Preston and Auggie; Bartholomar sent back to Hell)
- Important distinction: Bartholomar is NOT Mr. Smoke. They are separate beings. Mr. Smoke is the chimneyrue. Bartholomar was a demon who served him.
- ASR renders this name as: Bazaroth, Beth Bazaar, Bartholomew Bazaar — normalize to Bartholomar

### Anita
- Function: Prophetic pressure / revelation trigger
- Session: S07
- Performance register: begins in cold-reading spiritualist patter, then shifts to genuine prophetic vision
- Her overlay block (S07-03-289 through S07-03-303) is her describing the cherub's appearance — muscular human body, lion's hands and feet, bull's face, eagle's wings. This is a vision delivery, not social dialogue.

### Hotel_Concierge (S06)
- Function: Elite logistics facilitator; gateway to the Brimstone Collective
- Non-speaking in the theatrical sense; delivers through GM framing

### Basilica_Priest (S06, S07)
- Function: Sacred gatekeeping presence; human witness to miracle
- Non-speaking. His scene role is physical/atmospheric, not expository. No overlay lines in S06. One text_inferred line in S07-06.

### Creature Type Note: Chimneyrue
A GURPS creature type. Material and ethereal. Spider body with a human face. Tethered to a chimney. Mr. Smoke's true form. This is canon, not metaphor.

---

## How To Read the Corpus Files

Each session folder contains five file types. Read them in this order.

### 1. `session_wide.md` — Read This First
Session metadata: in-world date, players, cast key, NPC registry, session shape, key discoveries, attribution notes. Start every session read here.

### 2. `segment_manifest.tsv` — Check Before Each Segment
Lists all segments in the session. The `npc_overlays` column tells you which major NPCs appear in that segment. The `scene_titles` column gives the headings inside the segment. Use this to orient before opening a segment file.

### 3. `npc_overlay_report.tsv` — Reference When Needed
Line-level NPC tagging with timestamps, persona, match method, and match score.

Match method values:
- `exact` — NPC name found verbatim in line text
- `fuzzy` — ASR variant of NPC name matched
- `text_inferred` — line references the NPC but does not voice them (talking *about* the NPC)
- `propagated` — line is within an NPC-active window; no direct name match

Use this file to verify which lines are NPC embodiment versus reference, and to get timestamp anchors.

### 4. `segments_md/[segment].md` — The Transcript
YAML front matter first: session, segment, time window, active overlays, scene titles. Then transcript body: line ID, speaker label, optional `[NPC: X]` overlay, timestamp, text.

Read from top to bottom without skipping. Do not summarize before reading. Do not trim banter.

### 5. `reviews_md/[segment]_review.md` — Post-Read Notes
GMA review of the segment: scene-level observations, NPC performance notes, attribution flags. Read after the segment, not before.

---

## What the GMA Is Learning

Three things. In this order.

**1. How Sean GMs**
What kind of pressure is he applying right now? Permissiveness, misdirection, adjudication, clarification, or silence? How does he handle a player going sideways? How does he re-anchor a scene that's drifting?

**2. How Sean Plays Major NPCs**
Each major NPC has a distinct register. Reagan sounds nothing like Mr. Smoke. Mr. Smoke sounds nothing like Kobayashi. Learning those distinct registers — brevity, implication, exposition style, social stakes — is the point of the NPC overlay system.

**3. Table Culture**
This group of players has chemistry, in-jokes, recovery patterns, and derailment habits. Banter is data. A joke that kills a scene is a scene-management event. A player who pushes back is a social-consequence event. Read it as such.

---

## Known Corpus Limitations

These affect reads right now. They are known quantities, not surprises.

**S01 Reagan gap (approximately 55 lines), S03 Mr. Smoke gap (13 lines).**
NPC overlay propagation dropped on short lines within confirmed NPC scenes. When you are in an NPC scene and the overlay tag disappears, assume you are still in the scene unless the transcript clearly shifts context.

**S02 has minor ASR name variants for Bartholomar.**
You may see Bazaroth, Beth Bazaar, or Bartholomew Bazaar in transcript text. Normalize all to Bartholomar.

**Attribution noise in all sessions.**
Short player responses may be absorbed into GM blocks. Player first-person action narration may be labeled Sean_GM. When a label conflicts with what the text is doing, trust the text and note the conflict. Speaker labels are your best current guess, not ground truth.

**Recommended read order:**
S03 → S04 → S01 → S02 → S05 → S06 → S07 → S08

---

## One Rule

Speaker labels are your best current guess, not ground truth. When a label conflicts with what the text is doing — a player label on a line that sounds like GM framing, a GM label on a line that sounds like a player interjection — trust the text and note the conflict. Attribution errors are known and documented. Do not let them collapse your read.

---

## GM Philosophy and Intellectual Genealogy

This section is not background color. It is load-bearing. The transcripts make more sense when you know where the GM is coming from — not just his TTRPG history, but the intellectual tradition he is working inside. These influences are not accidental. They are the architecture.

---

### Part One: The Intellectual Spine

**Albert Camus — The Absurd and the Sisyphus Question**

Sean's explicit design goal for FRH: *can a single person make an ethical, meaningful choice in what may be a pointless, absurd universe?* This is Camus's question from *The Myth of Sisyphus* (1942), taken seriously as a design premise, not as a philosophy lecture. The party investigates real conspiracies, defeats real enemies, and accomplishes real things. The universe is also probably indifferent and possibly a joke. Both are simultaneously true. The campaign does not resolve this tension. It lives in it.

The five-node moral gradient (Amber, Matthew, Auggie, Crispin, Preston) is five different philosophical positions on how to carry the absurd. Not five alignment slots. Five answers to Sisyphus.

**Robert Anton Wilson and Robert Shea — Illuminatus!, the Fnord Principle, and Reality Tunnels**

Wilson and Shea's *Illuminatus! trilogy* (1975) is not just an influence — Sean names it as the designed world structure of FRH. Every conspiracy is simultaneously true and competing. There is no bottom. The case is always a window into a larger case.

The fnord principle is the structural theory behind Mr. Smoke's design: a symbol invisible until you learn to see it, then it is everywhere and you cannot unsee it. Smoke's fingerprints were on every PC's situation from session one. Before the party noticed, none of the threads connected. Once they noticed, everything connected.

Wilson's concept of the reality tunnel — that every individual constructs their reality through the mesh of their beliefs and symbols — underlies the campaign's epistemological ground rule: what the players theorize shapes the waveform of outcomes. Investigation does not just reveal what is there; it collapses possibility into actuality.

**The Epistle of James — Faith Without Works**

Sean's personal theology maps directly onto the campaign's moral architecture: James-before-Paul design. The Epistle of James is the outlier in the Pauline tradition: faith without works is dead. What you believe is less important than what you do with it. The FRH investigators are not asked to hold the correct doctrine. They are asked to enact meaning in an ambiguous universe.

**Steven Brust — To Reign in Hell (Political Tragedy, Not Moral Fable)**

Brust's *To Reign in Hell* (1984) retells the War in Heaven as a political tragedy. Everyone had reasons. Nobody was simply evil. FRH's cosmology is built in this register. When you read a scene where an angel speaks with complete authority about God's will, the Brust frame tells you: this is a being with genuine conviction operating on genuinely partial information inside a system too large for any created being to fully see. Confident voices. Limited sight. Always.

**Robert Heinlein — Job: A Comedy of Justice**

Heinlein's *Job* (1984) — a man who tries to do right inside a game whose rules keep changing, whose entire life is structured by a cosmic wager he was never told about. This is Preston's situation literally. It is the party's situation structurally: Fate-chosen investigators doing genuinely meaningful work, simultaneously pieces in a game at a level of reality they cannot see.

**Bob Dobbs and the Church of the SubGenius — Slack and the Cosmic Joke**

Bob Dobbs sits at the outermost frame of the FRH cosmological stack. Slack defeats probability. The Cosmic Joke is not hostile; it is the possibility that the universe is structured like a grift that somehow comes out right. Bob's cosmological position in FRH: over/next to/sideways to Fate. Not opposing it, not serving it. Where Fate works through probability fields, Bob operates through Slack — structurally immune to the Fate mechanism.

---

### Part Two: The TTRPG Genealogy — 46 Years of GMing

**1978 — El Paso, Fort Bliss Adjacent**

September 1978. Sixth grade. H.E. Charles Junior High, El Paso TX. A friend's father had transferred from Fort Irwin to Fort Bliss and brought the Basic D&D box set. First character sheets were 3x5 index cards.

The condition of that entry point matters more than the fact of it. This was the Braunsteinian condition: pre-internet, pre-theory, no authoritative model of what a TTRPG should be. Each group built its own entirely. Sean bought Greyhawk, Blackmoor, Eldritch Wizardry, and Gods/Demi-Gods and Heroes from that era without knowing they were add-ons to a system he did not own yet. Hybrid play from day one. **Blackmoor is in this pile.** Dave Arneson's Blackmoor was the proto-RPG — the Braunsteinian wargame-to-narrative-game inflection.

In 1979 his father bought the AD&D Dungeon Master's Guide at Sears. Player's Handbook and Monster Manual followed. Real AD&D by September 1979.

**1978-1979 — The Tolkien Inflection**

Bakshi's Lord of the Rings film ended the dungeon-crawl phase. The result: open-air campaigns, continent-wide stakes, characters as witnesses who were not always able to affect outcomes. Characters became fully fleshed-out persons. Players started writing family histories. The group stopped grinding from first level and started at fifth. This is the origin of FRH's insistence that player characters are fully-realized persons with histories, not blank slates.

**1981-1982 — T&T, Champions, CoC**

Tunnels and Trolls arrived through an eighth-grade history teacher named Mr. Hayden who ran lunch sessions. T&T mattered structurally: d6-based, solitaire-compatible, lighter than AD&D. Champions introduced point-buy character building — the idea that a character is a collection of deliberately chosen capabilities and deliberately chosen limitations, priced against each other. This is the soul of GURPS character design. Call of Cthulhu arrived around 1982. What CoC contributed architecturally: investigators are small; the cosmos is vast and largely indifferent; power does not guarantee safety; fear comes from the unknown rather than from superior force. This is permanently embedded in FRH.

**1986 — The GURPS Transition**

Sean declined to buy AD&D Second Edition. GURPS 3rd Edition was chosen for three reasons mapping exactly onto prior system history: d6 dice (like T&T), point-buy (like Champions), homebrew-friendly (no assumed setting). Steve Jackson's GURPS 3rd Edition introduction explicitly names M.A.R. Barker's *Empire of the Petal Throne* as a formative influence — the designed-from-lifetime-synthesis game world. Sean chose the system built in that genealogy. He has been using GURPS Third Edition ever since.

**1992 — The New York Campaign (FRH's Direct Design Ancestor)**

500-point GURPS Supers. Players: Joel (alien Brick, nigh-invulnerable except his eyes), Brandon (Paxton's brother — Shadow-type, secretly vampire-thralled, sided with the vampires at the climax and blinded Joel), Paxton, and Kathy. The campaign opened with a smashed-car mystery: an invisible 30-foot Wendigo a rogue vampire had summoned and then lost control of. The Wendigo was never explained during that campaign. It was finally explained in Session 8 of the FRH recordings in 2024 — three decades later. Brandon's betrayal — secret allegiance revealed at climax, a party member working a different agenda the entire time — is structurally identical to the mandatory Secret Society disadvantages in FRH.

**The Yesterday Ghost One-Shot**

A pick-up dark superhero game that improvised into a ghost redemption story. During the session, Sean mentioned that the destination sign on a bus read "Yesterday" — a spur-of-the-moment color detail with no planned significance. The players connected it to the ghost going home to his family. That connection crystallized the entire one-shot into its perfect ending. This is the canonical example of how legendary moments work: not scripted, emergent from a phase transition in the narrative's liquid state, nucleated from a tiny detail thrown in for texture.

**The Design Influences That Built FRH's Structure**

*Paranoia (Gelber/Goldberg/Costikyan, 1984)* — information asymmetry as mandatory architecture. Secret Power plus Secret Society as character creation requirements means intra-party tension is structural, not emergent. Paranoia figured this out as comedy. FRH runs it straight.

*Amber Diceless (Erick Wujcik, 1991)* — narrative-first gameplay. Fiction before mechanics. Characters are genuinely powerful but face opposition that is also cosmologically significant — power does not resolve the problem. GURPS dice appear as punctuation and validation in FRH, not as the primary resolution system.

*Feng Shui (Robin D. Laws, 1996)* — mooks, Named NPCs, and Set Pieces; but reframed. The Set Piece in FRH is not the action sequence. It is the morning-after conversation. The foundry fight is setup. The party talk the next morning — cleaned up, quiet, back on the train — is the actual Set Piece. The spectacular location creates pressure. The intimate enclosed location holds the crystallization.

*In Nomine (Derek Pearcy, 1997)* — the celestial/infernal machinery as hidden operating system. Angels, demons, the Symphony, tethers, Songs — all operating in reality whether the investigators know it or not. Sean absorbed the cosmology and rebuilt it under a Brustian political-tragedy frame, a Heinlein-Job cosmic-bet frame, and a Camus absurdist frame simultaneously.

**The Literary Target**

Roger Zelazny. *Creatures of Light and Darkness*. *Lord of Light*. *Jack of Shadows*. *Eye of Cat*. *The Doors of His Face, the Lamps of His Mouth*.

The Zelazny register: characters who are cosmologically significant but personally small simultaneously. Power does not resolve the person. The investigator who can shatter metaphysical realities is still uncertain, still wounded, still reaching for something they can name but not quite hold.

Sean said: "I know I won't ever achieve that goal but that is my hope."

FRH already has this structural DNA. The 375-point Wild Cards Aces who genuinely huddled from a purple color on the window glass — that is it. When reading transcripts, weight moments where power coexists with personal smallness. Those are what the campaign is reaching for.
