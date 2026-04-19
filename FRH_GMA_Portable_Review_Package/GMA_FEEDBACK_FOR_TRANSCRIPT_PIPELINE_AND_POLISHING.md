# GMA Feedback For Transcript Pipeline And Polishing

Purpose: capture onboarding friction and package-level feedback discovered during
the bare-bones GMA apprenticeship test of the FRH portable review package.

Audience:
- transcription pipeline agent
- transcript/package polishing agent

## Current Feedback

### 1. Recommended session read order conflicts with practical onboarding

Issue:
- `GMA_ONBOARDING.md` recommends the read order `S03 → S04 → S01 → S02 → S05 → S06 → S07 → S08`.
- In practice, starting anywhere other than `Session 01` creates confusion for the user.
- The user reports they have always started with `Session 01`; beginning with `Session 03`
  is disorienting despite the stated recommendation.

Why this matters:
- a bare-bones GMA or other onboarding reader will naturally infer that the recommended
  order should be followed
- this can produce immediate uncertainty before transcript reading even begins
- chronological grounding appears more important than whatever training-value ordering
  motivated the current recommendation

Suggested action:
- either change the default recommendation to start with `Session 01`
- or explicitly label the `S03 → S04 → S01 ...` sequence as an optional analyst/training
  order rather than the default first read
- if retained, explain *why* that order exists in one sentence

### 2. Bare-bones GMA needs stronger "start here" guidance

Issue:
- with aggressively trimmed onboarding, any ambiguous instruction has outsized cost
- session-level orientation vs. overall package orientation can blur together

Suggested action:
- add a very explicit package-level instruction that first-pass apprenticeship reading
  begins with `Session 01` unless the user deliberately requests analyst-order reading

## Session Context Note

The user clarified that producing this package required two LLM agents in order to
fit context and maintain a reproducible pipeline for TTRPG gameplay audio to
attributed transcript. Feedback should therefore favor:

- reproducibility
- low-context onboarding clarity
- preserving attribution gains from the new transcription/diarization/attribution pipeline
- minimizing unnecessary reader confusion introduced at the package layer

### 3. Session 01 Segment 03 lane ownership / recovery note

Issue:
- during apprenticeship reading, I initially misread the "finds Auggie" lane as Matthew's.
- user clarification: it was `Crispin`, not `Matthew`, who found Auggie.
- this is important because it changes the social reading of the scene and the split-party flow.

Why this matters:
- the segment contains multiple overlapping split-party lanes
- if attribution, scene stitching, or implied subject continuity is even slightly muddy, a reader can
  assign the wrong investigative initiative to the wrong PC
- this directly affects GMA interpretation of table dynamics and character behavior

Suggested action:
- review `Session_01_2024-03-09_segment_03.md` around the transition into
  "Matthew checks back and finds Auggie"
- if the transcript actually supports `Crispin` as the acting character there, correct the scene label
  or nearby lines so the ownership is explicit
- if the transcript is itself uncertain, add a conservative note in the review/package metadata

### 4. Robust warning: split-lane ownership and pronoun drift become a major readability risk

Issue:
- once Session 01 enters heavy split-party play, the package becomes vulnerable to pronoun drift,
  lane bleed, and mistaken actor continuity.
- this risk is not limited to a single line or segment title; it appears structural whenever:
  - multiple PCs are acting in parallel
  - the camera cuts rapidly between them
  - lines use `he`, `him`, `you`, or implied subjects without explicit re-anchoring
  - local chatter and rough attribution overlap with fiction-state transitions

Observed effect during apprenticeship read:
- I could still follow the broad plot
- but I had to do repeated inference work to determine which PC currently owned the lane
- this creates avoidable interpretive error for a bare-bones GMA and especially distorts:
  - who initiated action
  - who discovered what
  - which character's psychology should be used to read a scene
  - how table dynamics should be interpreted

Why this matters:
- in a TTRPG transcript, lane ownership is not cosmetic
- it is the difference between "Matthew blundered into this" and "Crispin operationally caused this"
- once those are confused, downstream GM-style analysis also skews

Suggested action:
- in split-party scenes, prefer explicit re-anchoring at lane transitions:
  - "Meanwhile, Crispin..."
  - "Back with Matthew..."
  - "Amber, in your room..."
- when speaker certainty is not enough on its own, use scene-title or inline clarifying framing to
  preserve actor continuity
- review Session 01 segments 03-05 specifically for:
  - mislabeled lane headers
  - pronoun chains with no explicit actor reset
  - places where two male PCs in adjacent scenes can be conflated
- if conservative certainty is the goal, it is better to over-label lane resets than under-label them

### 5. Preserve ambiguity architecture; do not over-polish away superposition

Core GM-design note from user:
- the game deliberately runs on gaps, misunderstandings, table theories, jokes, fears, and partial reads
- the GM often keeps fiction in a kind of superposition and delays "collapse" until players commit to an
  interpretation or force a concrete decision
- specificity is intentionally limited; narrative language, emotional tone, and pop-culture references are used
  to keep final interpretation at a distance
- enemies/NPCs may not have fixed fully-written stats; e.g. Mr. Smoke still has no bespoke stat block beyond
  the generic chimneyrue outline in `GURPS Creatures of the Night`

Why this matters for polishing:
- some apparent vagueness is not transcript weakness; it is authentic GM method
- not every ambiguity should be "solved" by an editor
- over-normalizing or over-clarifying could erase the intended wavefunction / possibility-space that the table
  is actively playing inside

What should be clarified:
- speaker/lane ownership
- session chronology / who is where
- when a misunderstanding is transcript-caused vs. fiction-caused

What should *not* be prematurely concretized:
- unresolved enemy ontology
- exact metaphysical explanation when the table does not yet have one
- NPC capability specificity that the GM is intentionally holding loose
- jokes/theories/fears that are carrying possibility rather than settled fact

Polishing principle:
- clarify who said what and who did what
- do not collapse intentional narrative ambiguity into false certainty

### 6. Preserve Sean's fiction-first action framing; do not flatten scenes into button-click summaries

Core GM-design note from Session 01:
- Sean consistently establishes player intent, fictional method, and desired outcome before calling for a roll.
- Skill use is usually clarified in-world first: what the character is trying to do, how they are doing it,
  and which ability actually matches that action.
- The transcript value is not just "roll X succeeded/failed"; it is the conversational translation between
  player aim and system-facing resolution.

Why this matters for polishing:
- compressing too aggressively into "Matthew rolls Acting" or "Amber uses Occultism" loses part of the
  teachable GM method
- this campaign does not treat mechanics as button presses; it treats them as resolution of already-imagined action
- for bare-bones GMA onboarding, those intent-setting exchanges are part of the apprenticeship value

Suggested action:
- preserve short setup lines that clarify motivation and method before the roll
- avoid summaries that remove the distinction between player intention, Sean's adjudication, and the die result
- when tightening wording, prefer concise clarity over mechanical shorthand

### 7. Preserve environment/world-logic constraints on powers

Core Session 01 example:
- Crispin's insubstantiality is not limited by arbitrary denial; it is limited by the physical situation.
- On a moving train, loss of friction matters. If he phases carelessly, he risks passing through the train and
  being left behind.
- Similar power constraints are often embedded in location, velocity, material boundaries, wards, or social context.

Why this matters for polishing:
- these constraints are a major part of how Sean keeps strong powers interesting without making rulings feel arbitrary
- if transcript cleanup removes too much of the environmental explanation, a reader may misread the GM style as
  either vague or capricious
- the apprenticeship value includes seeing how power ceilings emerge from world logic rather than blanket prohibition

Suggested action:
- retain concise lines that explain environmental affordances and limits
- be careful not to summarize away the physical logic of moving scenes, wards, barriers, or embodied risk

### 8. Session 01 demonstrates that the real set piece may be quiet, reflective, or interior rather than action-spectacle

Core GM-design note from user:
- Sean's "set pieces" can be conversations, reflection beats, constrained character moments, or ritualized interior acts
  rather than only fights/chases/showdowns.
- In Session 01, the climax is not a conventional combat finish; it is Auggie's dangerous rite with the annotated
  `Lesser Key of Solomon`, Amber's guidance, and the aftermath of changed interior state.

Why this matters for polishing:
- an editor may be tempted to privilege louder scenes and over-compress mood beats or contemplative transitions
- doing so would distort one of the key qualities the user wants a GMA to learn from the transcripts
- the package should help a reader notice when a quiet scene is the true dramatic center

Suggested action:
- preserve scene framing that marks mood, stillness, hesitation, aesthetic posture, or ritual preparation
- avoid implying that "nothing happened" simply because a segment is introspective or low-action
- where helpful, let review metadata note when a segment functions as a character/dramatic set piece

### 9. Session 01 is a strong example of live improvisational synthesis from prepped pressure-fields rather than rigid plotting

Core GM-design note from user:
- Reagan began as a one-off fame encounter for Matthew.
- The protected train car was prepped, but its exact institutional identity was not fixed in advance.
- During live play, Sean fused those elements and made the warded car belong to Reagan's influential senator father.
- This was supported by pre-existing cosmological/historical pressure-fields: 1923, occult Washington politics,
  Harding's magical assassination, and the larger mythic arc.

Why this matters for polishing:
- the transcripts are useful partly because they show how a GM can improvise durable structure without seeming random
- over-editing toward apparent preplanned neatness may hide the improvisational craft actually being demonstrated
- preserving the sequence of emergence helps a GMA learn how player blunders and GM prep can crystallize into campaign canon

Suggested action:
- do not rewrite emergent connections so they sound predetermined if they were table-forged
- where review notes exist, it may be useful to flag moments where player choice causes a local possibility-space to collapse

### 10. Session 02 adds another attribution risk layer: Sean is carrying Amber while also GMing NPCs

Issue:
- in Session 02, Ashley is absent but Amber remains present in-world under the campaign's away-on-business / business-trip handling.
- Sean temporarily voices Amber while also voicing NPCs and adjudicating the scene.
- this compounds the already-existing split-lane/pronoun drift problem from Session 01.

Why this matters:
- a bare-bones GMA can more easily misread whether a given line is:
  - Amber speaking
  - Sean as GM clarifying fiction
  - Sean voicing an NPC
  - or table-level coordination
- this is especially important in scenes where Amber contributes occult interpretation, locating magic, or tactical advice

Suggested action:
- in Session 02, prefer extra speaker certainty checks around Amber's voiced lines
- where needed, add conservative clarifying labels in review metadata noting that Amber is GM-carried for this session
- review opening and regroup scenes for moments where Amber's lane may blur into Sean's GM narration

### 11. Normalize Preston's patron name as Merovech

Issue:
- Whisper/ASR-style transcript surfaces may mishear Preston's patron / demon lord name.
- user clarification: Preston's patron on the character sheet is `Merovech`.

Why this matters:
- this is not a flavor-only detail; it is a character-defining secret-society / patron relationship
- name drift here can confuse future corpus readers and weaken cross-session continuity

Suggested action:
- normalize Preston's patron name to `Merovech` in corpus-facing outputs
- if uncertain raw transcript spellings differ, preserve the raw text only where needed for provenance, but use `Merovech` in review/context layers

### 12. Session 02 action density makes lane re-anchoring even more important than Session 01

Issue:
- once Session 02 reaches the yard / shack / second-snatch sequence, the action alternates rapidly between:
  - Auggie investigating and reacting at the shack/pit lane
  - Preston shadowing, evaluating, and then choosing where to intervene
  - Crispin invisibly observing and sometimes assisting from a separate liminal lane
  - occasional returns to Matthew / train-car state
- in these sections, even small pronoun drift or scene-title imprecision can produce major interpretive errors.

Why this matters:
- a GMA can easily lose track of:
  - whether Preston is still following the abductors or has switched to Auggie's lane
  - whether a strange/ghostly observer is Crispin or someone/something else
  - whether Auggie is alone in the shack, being watched, or being actively joined
  - which information is shared between PCs versus only known in one lane
- because the scene is tactically dense, lane confusion here does more damage than in banter or recap scenes

Suggested action:
- add stronger lane-reset phrasing in Session 02 segments 02-04
- explicitly re-anchor when Preston changes targets or priorities
- explicitly re-anchor when Crispin is present as an invisible observer/helper
- preserve distinctions between:
  - what Auggie heard directly at the shack
  - what Preston merely inferred from observation
  - what Crispin knows from invisible proximity

### 13. Clarify the Amber absence-handling logic in Session 02 metadata/review context

User clarification:
- Ashley did not want the party to lose its healer simply because she missed the session.
- She gave Sean permission to role-play Amber for the session if needed.
- Sean partly side-stepped the burden of overplaying Amber off-camera by having Amber kidnapped early in Session 02.

Why this matters:
- without this context, a reader may misread Amber's Session 02 handling as arbitrary removal or simple plot convenience
- in fact, it is a deliberate compromise between:
  - respecting the player's absence
  - preserving the party's functional dependence on Amber as healer/support
  - and avoiding having the GM over-occupy Amber's role for the entire session

Suggested action:
- in Session 02 session-wide or review notes, clarify that Amber is player-approved as GM-carried for this session
- note that the kidnapping serves both plot function and absence-management function
- keep this explanation in metadata/review context rather than collapsing it into the in-world transcript

### 14. Session 02 needs explicit preservation of who knows what across converging lanes

Issue:
- by Segments 03-05, the party is partially reconverged, but information is still asymmetrical.
- different PCs arrive carrying different slices of truth:
  - Auggie heard "lower her into the pit for the master" and "go back for the other one"
  - Preston witnessed the second snatch, rescued Matthew, and broke a captive under coercive interrogation
  - Crispin explored the shaft/tunnel/foundry route and confirmed industrial infrastructure below the shack
  - Matthew learned through psychometry about Amber's drugged/dampened state and the soulless nature of the abductors

Why this matters:
- once the party is talking together again, an editor or downstream model may accidentally flatten that into shared knowledge
- but the scene dynamics depend on the fact that each PC earned different information through different methods
- preserving these distinctions is central to understanding Sean's clue-vector design

Suggested action:
- in review notes or tighter transcript polishing, be careful not to summarize group knowledge as if it were all mutually shared immediately
- when helpful, briefly re-anchor which character is currently reporting information versus what they directly experienced

### 15. Preserve the distinction between Mr. Smoke and Bartholomar

Issue:
- Session 02 introduces pressure from both the chimney-spider/master apparatus and a separate demonic node.
- corpus readers can easily collapse these into one being if names, overlays, or contextual phrasing are loose.

User-confirmed interpretive stakes:
- Mr. Smoke is the chimneyrue / spider-in-the-chimney / hidden mastermind pressure connected to the foundry and kidnappers.
- Bartholomar is distinct from Mr. Smoke and is the demonic party to whom the soulless abductors gave their souls.

Why this matters:
- this distinction is structurally important to FRH cosmology and to later continuity
- confusion here would blur local monster-pressure, infernal alliances, and the broader Symphony-aware layer

Suggested action:
- preserve a clear corpus-facing distinction between:
  - the spider creature in the chimney / factory master / Mr. Smoke pressure
  - Bartholomar as separate demonic actor or beneficiary in the psychometric revelation
- review Session 02 Segments 04-05 for any wording that accidentally implies they are the same entity

### 16. Session 02 Segment 05 shows a recurring readability need: distinguish individual capability limits from group planning limits

Issue:
- in the foundry approach scene, Crispin can phase through the fence and enter immediately, while the others must reckon with ordinary physical and social barriers.
- if summarized loosely, the scene can sound like the group is dithering, when in fact they are constrained by asymmetric capability.

Why this matters:
- one of Sean's central ensemble challenges is spotlighting a party where some members can bypass barriers others cannot
- preserving that asymmetry helps a GMA understand both the intra-party frustration and the practical need for plans, cover stories, and alternate vectors

Suggested action:
- when polishing group-approach scenes, keep explicit which obstacles are:
  - not obstacles for Crispin
  - still very real obstacles for Auggie, Matthew, and Preston
- preserve the moment where Auggie proposes social cover as a serious operational response rather than hesitation

### 17. Session 02 Segment 05 reinforces that Sean uses the world to answer naive action, not just the dice

Observed example:
- Matthew tries to solve the fence problem physically, loses to the fence, and eventually gets over only with help.
- the scene is funny, but it also clarifies material reality, group asymmetry, and Matthew's impulsive style.

Why this matters:
- this is a recurring Sean pattern worth preserving for training value:
  - player tries direct action
  - Sean clarifies the fiction and required rolls
  - the world answers in a consequence-rich, often character-revealing way
- over-compressing these exchanges into "failed climb roll" loses the apprenticeship value

Suggested action:
- preserve short fictional setup and aftermath around physical-comedy / failure beats
- avoid reducing them to pure mechanics, since the dramatic meaning is in how the world answers

### 18. Preserve that party construction is shaping genre in a literal, setting-reactive way

User clarification:
- the campaign's current pulp mode ("con-man occult operators with a little punch") is a direct consequence of this party's construction.
- because most PCs have social-facing skills/advantages such as Charisma, Empathy, Fast-Talk, Acting, Research, administration-style clue vectors, and other interpersonal capabilities, the setting is adapting to that style in a real and literal way.
- user notes that a differently built party (for example, one centered on more dream-facing or fae-facing characters) would have driven the campaign toward very different adventure texture, such as Near Marches / Dream Logic material.

Why this matters:
- a GMA should not read the present campaign mode as the only or default expression of FRH
- the transcripts demonstrate a specific realized branch of FRH shaped by who these PCs are and what they are good at
- this reinforces a central Sean design principle: the party helps determine not just available clues, but the genre-expression of the campaign itself

Suggested action:
- in review or training context, note that Session 02's infiltration / bluff / interrogation / social-cover mode is partly a consequence of party composition
- preserve scenes where social advantages and clue vectors visibly steer play away from brute-force solutions

### 19. Session 02 Segment 07 especially needs scene-title scaffolding or lane markers

Issue:
- Segment 07 currently has no scene titles in the metadata even though it contains multiple major lane/phase changes.
- this makes it much easier for a bare-bones GMA to lose track of the sequence and relationship between:
  - the outside infiltration conversation / plan
  - Crispin recovering Amber and encountering the whisper in the storage/changing area
  - Matthew and Auggie moving toward the body room
  - the "smell roses and black out" control beats
  - Preston resting, summoning demonlings, and then being taken out
  - Crispin's discovery of the curated escape car and his retaliatory bombing attempt
  - the hard cut to waking on the train the next morning

Why this matters:
- this is one of the densest and most consequential segments in Session 02
- without scene-title support, the transcript is still usable, but the apprenticeship value drops because a reader spends too much effort reconstructing the cut structure

Suggested action:
- add scene titles or lane headers for Segment 07 comparable to earlier segments
- at minimum, mark the major state shifts listed above

### 20. Preserve the factory as an active occult control space, not just a location

Observed in Segment 07:
- once PCs cross certain thresholds in the factory, they are subjected to a recurring hostile effect signaled by sleepiness and the smell of roses.
- this takes out Matthew, Auggie, and Preston in sequence.
- the effect appears to be environmental/territorial rather than a simple one-off attack from a visible NPC.

Why this matters:
- the segment changes the ontological status of the foundry:
  - it is no longer just the place where the bad guys work
  - it is an active hostile ritualized or controlled space
- preserving that distinction helps a GMA understand the escalation from kidnapping infrastructure to metaphysically curated threat-space

Suggested action:
- in review notes, call out the "smell roses / black out" pattern as a repeated control signature
- avoid summarizing these blackouts as generic failed rolls without the atmospheric marker

### 21. Preserve that the Kansas City end-state is curated by an overpowering intelligence

Observed in Segment 07:
- after the failed infiltrations, blackouts, and Crispin's attempted retaliation, the party wakes the next morning:
  - back on the train
  - cleaned up
  - dressed properly
  - breakfast served
  - moving east out of Kansas City
- this is not a normal scene transition; it implies a hostile or superior intelligence that can tidy the board and reposition the party.

Why this matters:
- this is one of the strongest thematic endings in Session 02
- over-compressing it into "they wake up back on the train" loses the deeply unsettling curated quality of the reset
- it is a key example of Sean ending a session on violated continuity rather than conventional victory/defeat resolution

Suggested action:
- preserve the polished, almost polite quality of the reset tableau in transcript/review context
- note that the emotional effect comes from how cleaned-up and intentional the repositioning feels

### 22. Preserve that Crispin's bombing attempt is an emotional/moral escalation, not just tactical problem-solving

Observed in Segment 07:
- after recovering Amber and hearing the whisper tied to Senator Reagan, Crispin pivots from rescue logic to retaliatory destruction.
- he interprets the curated car/escape setup as a hostile move and rejects it.
- his decision to bomb the foundry is driven by vengeance, outrage, and refusal, not merely by strategic optimization.

Why this matters:
- a summary that says "Crispin tries to blow up the foundry" misses the character meaning
- this is a major insight into Crispin's psychology under pressure and into how Sean lets strong emotions reshape operational decisions

Suggested action:
- preserve the trigger chain:
  - recover Amber
  - hear the whisper / Reagan reference
  - perceive the uncanny curated reset
  - choose annihilatory retaliation
- do not collapse the act into generic sabotage language

### 23. Session 03 needs conservative ownership recovery in the radio-argument scenes

Observed in `Session 03`, especially Segment 02:
- the session becomes densely conversational very quickly once the telegram and radio arrive.
- the core hallway exchange between Matthew and Auggie contains several `Unidentified_Player` lines at exactly the moment the emotional meaning matters most.
- this is also where Amber's arrival, Preston's procedural stance, and the room-versus-hall split all overlap.

Why this matters:
- this is one of the most important trust/governance arguments in the whole early corpus.
- if ownership drifts here, a reader can lose:
  - who is insisting on caution versus mitigation
  - who says "I'm compromised, Augie"
  - who physically leaves the room and who follows
  - who is trying to preserve group process versus who is trying to stop the radio outright
- overconfident reassignment would be bad, but under-clarified ownership here weakens one of the key apprenticeship scenes.

Suggested action:
- do a targeted speaker-ownership pass on:
  - the telegram/radio debate in the main car
  - the hand-slapping / knob-blocking exchange
  - the hallway confrontation between Matthew and Auggie
  - Amber's arrival and the passenger intimidation beat
- prioritize preserving the emotional arc and the trust fracture over perfect word-for-word certainty on every interruption
- where certainty is low, prefer short clarifying editorial notes rather than silently forcing exact attribution

### 24. Session 03 Segment 04 has several high-value readable but fuzzy stretches that deserve targeted cleanup

Observed in `Session 03`, Segment 04:
- the segment is broadly readable, but some of the highest-value lines are still partially blurred by overlap, truncation, or uncertain speaker ownership.
- the main risk cluster is:
  - the early telegram-authentication follow-through with Matthew
  - the first resumed live conversation with Mr. Smoke
  - the sequence where Crispin is outed as tied to the Outfit / Reagan fallout
  - the sequence where Mr. Smoke outs Preston's infernal contract situation
  - the handoff into Matthew's Tokyo question and Mr. Smoke's "casino" blind-spot metaphor

Why this matters:
- these are not incidental logistics lines; they carry core apprenticeship value around:
  - Sean's NPC performance
  - faction / secret-society revelation
  - internal party destabilization
  - cosmological framing
- because the scene is still understandable, this is a good candidate for conservative polishing rather than wholesale reconstruction
- if left fuzzy, a reader may miss who is being outed, what exactly Mr. Smoke is offering, and where the Tokyo/Atlantic City blind-spot line begins and ends

Suggested action:
- do a targeted readability pass on the above sub-scenes only
- prioritize:
  - exact ownership of the key revelation lines
  - preserving the sequence of who leaves, who turns the radio back on, and who is present for each revelation
- clean separation between:
    - "real telegram" verification
    - Mr. Smoke's alliance explanation
    - Crispin/Outfit exposure
    - Preston/contract exposure
    - Tokyo blind-spot / casino metaphor
- avoid over-normalizing the live-table interruptions; keep the room's volatility, but make the informational spine easier to follow

### 25. Session 04 Segment 02 would benefit from internal scene-title subdivision

Observed in `Session 04`, Segment 02:
- unlike several earlier segments, this file has no useful internal scene-title breakdown even though it clearly contains multiple distinct beats.
- natural scene breaks include:
  - train geometry / loadout clarification
  - Preston's illusion-and-concealment discussion
  - arrival into St. Louis and station sensory framing
  - platform regroup and cab acquisition
  - arrival at Kobayashi's mansion
  - drawing-room wait / statue temptation

Why this matters:
- the segment is readable, but it asks the reader to do more structural work than necessary.
- for GMA onboarding, scene-title scaffolding is especially helpful when a session is transitioning from travel logistics into a major NPC briefing.
- these sub-scenes also carry different training purposes: rules grounding, historical texture, spatial orientation, criminal-social atmosphere, and character temptation.

Suggested action:
- add or restore concise internal scene titles for the major beat shifts in Segment 02.
- do not rewrite the content; just expose the structure already present.
- this is a readability aid, not a content correction.

### 26. Session 04 Segment 03 contains at least one high-value social-beat misattribution risk

Observed in `Session 04`, Segment 03:
- the challenge/call-out after Kobayashi refers to Matthew as "Elijah" is easy to misassign on first read.
- on review with user correction, that call-out belongs to **Crispin**, not Auggie.

Why this matters:
- it changes the character read in an important way:
  - if attributed to Auggie, it reads as etiquette/boundary enforcement from the social governor
  - if attributed to Crispin, it reads as threat-sensitivity and sharp reaction to a dangerous slip from the covert assassin
- this is exactly the kind of beat where "close enough" attribution weakens apprenticeship value.

Suggested action:
- do a targeted ownership pass around the "Elijah" slip / immediate challenge sequence in Segment 03.
- prioritize accuracy on who reacts first to Kobayashi's breach of discretion.
- more broadly, flag similar high-value conversational beats where the line itself is readable but the exact owner carries meaning.

### 27. Session 04 city-signal and front-desk beats need a couple of specific ownership/POV clarifications

Observed across `Session 04`, especially Segments 02-04:
- Amber is the one perceiving the city's metaphysical overlays:
  - the pure gold heavenly beam
  - the uglier reddish emanation tied to violence / another site
- that perception is not group-common knowledge in the same way; it is coming through Amber's aura/occult perception lane.
- at the Governor front desk, Matthew is socially rescued by **Auggie**, not Crispin.
- this is also a likely **Hapless Luck** beat: the unusually favorable availability of the top-floor suites and the smooth clerk response are part of Auggie's social gravity / GM-controlled luck lane.

Why this matters:
- if the city-beam perception is flattened into shared perception, Amber loses a meaningful clue-vector distinction.
- if the front-desk rescue is misattributed, the scene loses:
  - Auggie's role as social stabilizer
  - the likely Hapless Luck activation
  - the contrast between Matthew's overreach and Auggie's graceful recovery

Suggested action:
- preserve that Amber is the one reading the occult city overlays unless the text explicitly broadens that knowledge.
- do a targeted ownership pass on the Governor front-desk exchange to clarify that Auggie steps in to help Matthew.
- where helpful, preserve or lightly annotate likely Hapless Luck moments rather than letting them disappear into generic social success.

### 28. Session 04 Segment 06 would benefit from a closing-scene label

Observed in `Session 04`, Segment 06:
- the final segment has no scene-title scaffolding even though it functions as a distinct end-of-session debrief / theory-talk / future-arc reorientation beat rather than another in-fiction St. Louis action scene.

Why this matters:
- for a bare-bones GMA, the absence of a label makes this ending feel flatter and less intentionally structured than it really is.
- this segment is doing closure work:
  - table-level recap and theory comparison
  - reminder of still-live mythic arcs
  - pop-culture shorthand around prior revelations
  - explicit transition into split-session scheduling

Suggested action:
- add a minimal internal label such as `post-session debrief and theory talk` or equivalent.
- do not over-polish the chatter; just expose that this is the session's closing reflection lane.

### 29. Sessions 05-07 confirm that breakout sessions are dramatically cleaner and deserve preservation as a distinct package strength

Observed across `Sessions 05-07`:
- once the campaign shifts into smaller breakout sessions, attribution clarity improves dramatically.
- the cleaner speaker field allows the reader to spend attention on:
  - GM philosophy
  - rules-to-fiction handling
  - character-specific problem solving
  - tone and cosmology
  rather than on constant lane untangling.
- this is especially visible in:
  - `Session 05` with Joel/Ben
  - `Session 06` with Paxton/Shane
  - `Session 07` with Paxton/Shane at even higher consequence density

Why this matters:
- the package currently emphasizes attribution pain in the large ensemble sessions, which is true, but it should also explicitly preserve the fact that the breakout format is one of the campaign's strongest training assets.
- a future GMA should understand that these sessions are not "side material"; they are some of the clearest windows into Sean's method.

Suggested action:
- preserve breakout sessions as high-value apprenticeship material.
- if the package ever includes a "best scenes for training" or "cleanest reads" note, include `Sessions 05-07`.
- do not over-normalize their quieter structure; their relative clarity is itself part of the evidence for how adult-schedule campaign branching can work well.

### 30. Session 05 should preserve the "management inspection" subtext around the dream lab

Observed in `Session 05`:
- Dr. Hope and Dr. Mike read not merely as eccentric researchers, but as subordinates performing for management during an on-site inspection.
- Auggie's elevated standing through the Brimstone Collective / Mr. Smoke lane matters here.
- the lab scene also carries a dark institutional subtext:
  - many prior experiments
  - many "volunteers" or test subjects
  - substantial hidden financing
  - a morally ambiguous research culture behind the cheerful demonstration tone

Why this matters:
- if this scene is summarized too lightly, it can flatten into "friendly exposition NPCs explain dream travel."
- the more accurate read is:
  - occult R&D under hidden patronage
  - deferential researchers trying to demonstrate results
  - the PCs functioning as both guests and experimental subjects

Suggested action:
- preserve or lightly annotate the inspection-performance tone in `Session 05`.
- when polishing, do not sand away clues that Mr. Smoke is coordinating multiple weird-science compartments and that the dream lab implies a long history of funded experimentation before the PCs arrived.

### 31. Session 06 is a strong example of mundane-first clue resolution and should be preserved that way

Observed in `Session 06`:
- the holy nail branch repeatedly resolves through:
  - wording
  - administration / common sense
  - architecture
  - institutional logic
  - careful infiltration
- powers matter, but they extend or flavor ordinary competence rather than replacing it.
- user clarification: Preston's relic-finding fortune was a quiet use of `Luck`, handled in-fiction rather than as an explicit mechanical prompt.

Why this matters:
- this session is one of the clearest demonstrations of FRH's clue philosophy:
  - the mundane person should matter more than the superpower
  - powers are not the default clue vector
- if polished carelessly, the session could be misremembered as "the occult guys use occult powers to find the relic."
- that would miss the actual lesson.

Suggested action:
- preserve the mundane/institutional reasoning beats with special care in `Session 06`.
- if any note is added, it should emphasize that the breakthrough came from `sepulcher is not basement`, not from flashy relic-sense.
- where Preston's luck-like beats are visible, consider a light annotation if needed so they are not flattened into generic coincidence.

### 32. Session 07 contains several likely hand-back worthy "mythic image" beats that should not be compressed away

Observed in `Session 07`:
- this session is one of the highest-density convergence points in the campaign:
  - Brimstone vice salon
  - Anita's real prophecy breaking through fake cold reading
  - celestial tracking mark on Preston
  - glowing body / glowing car
  - tabloid photographer
  - undercity tunnels and unseen voices
  - "sun over St. Louis" / star-like celestial presence
  - demonling cleanup
  - altar placement during feast-day mass
  - pale armored man / white warhorse implications
- several of these are not just plot points; they are campaign-defining images.

Why this matters:
- if this session gets over-summarized or "cleaned" too aggressively, it risks losing the very quality that makes it extraordinary: every attempted wind-down opens another hidden system.
- this is also one of the strongest `Illuminatus!` / Robert Anton Wilson texture sessions in the package.

Suggested action:
- preserve the following images with special care:
  - Anita's description of the cherub
  - Preston's gold mark
  - the new star over St. Louis
  - the tunnel voices / red eyes
  - the glowing car
  - the cross appearing on the altar during mass
  - the pale broad "armored" man and the white horse with blue eyes
- if a future synopsis or highlight sheet is built, `Session 07` should be represented as a major capstone rather than just "the St. Louis breakout gets chaotic."

### 33. Session 08 should be labeled as a real epilogue / debrief session, not as failed play

Observed in `Session 08`:
- this session is mostly OOC talk among Sean, Joel, and Ben.
- there is only a brief, partial attempt to re-enter campaign play, and it does not really take hold.
- however, the session still carries major apprenticeship value because it contains:
  - Sean's autobiographical / philosophical source material
  - direct statements about role-playing versus storytelling
  - one-shot and prequel thinking
  - table-culture evidence of how a long campaign trails off honestly

Why this matters:
- if treated as "nothing happened," the package will miss a meaningful kind of closure.
- `Session 08` does not provide a fictional climax, but it does provide philosophical and relational closure.
- it is especially useful for understanding why FRH feels the way it does.

Suggested action:
- formally label `Session 08` as an `epilogue / debrief / hangout closure` session.
- if the package ever distinguishes "plot advancement" from "campaign understanding," mark this session as low on the former and high on the latter.
- preserve Sean's explicit statement that role-playing is not the same thing as telling a fixed story; this may be the most direct philosophy statement in the entire corpus.

## Formalized Handoff Priorities

Highest priority to fix:
- speaker ownership where the owner changes the meaning of the beat
- split-lane drift in large ensemble sessions
- missing scene-title scaffolding where segment structure is already present but hidden
- preservation of distinctions that readers are likely to collapse:
  - Bartholomar vs. Mr. Smoke / chimneyrue machinery
  - old Watchmen / generic watchers vs. the party's chosen `The Watch`
  - player knowledge vs. character knowledge in split-lane scenes

Highest priority to preserve:
- intentional ambiguity / superposition
- Sean's fiction-first cadence and environment-based limits
- likely Hapless Luck / Luck beats that are embedded narratively
- pop-culture shorthand when it is carrying tone, space, or player-specific resonance
- the dignity of both characters and players, especially in scenes mixing comedy with emotional or moral weight

What a future polishing pass should avoid:
- over-forcing certainty where the live table was intentionally holding multiple theories open
- flattening breakout sessions into "side quests"
- translating every atmospheric image into explicit lore
- sanding away the social comedy, table warmth, or awkwardness that makes the campaign feel inhabited
