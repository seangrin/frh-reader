# FRH GMA Portable Review Package

Version: `v1.3 Beta`

This package is meant to be portable.
You can:

- drop it into an LLM workspace
- zip it and email it to a reviewer
- hand it to another agent as a self-contained corpus

## What Is Included

- `README.md`
- `GMA_ONBOARDING.md` — primary onboarding document for apprentice GMA reads; start here for new LLM instantiation
- `RELEASE_NOTES.md`
- `READING_PROTOCOL.md`
- `REVIEW_PROTOCOL.md`
- `NPC_OVERLAY_GUIDE.md`
- `SESSION_PRIORITY.md`
- `GMA_Gold_Star_Corpus/`

## How To Use It

**New GMA instantiation:** Point the agent to `GMA_ONBOARDING.md` first. It is LLM-agnostic and self-contained — no prior context needed.

**Reviewer or returning agent:** Point the agent to this `README.md` first.

The agent should then:

1. read `SESSION_PRIORITY.md`
2. read `READING_PROTOCOL.md`
3. read `NPC_OVERLAY_GUIDE.md`
4. open a session folder inside `GMA_Gold_Star_Corpus/sessions/`
5. read `session_wide.md`
6. read `segment_manifest.tsv`
7. read one segment Markdown file in full
8. use the matching review file for critique and refinement

## Core Rule

Do not summarize instead of reading the source segment.

The 30-minute segment files are the real training unit.

## Suggested Starting Sessions

- Session 3: Mr. Smoke
- Session 4: Kobayashi
- Session 5: Doctor Hope / Doctor Mike
- Session 1: Reagan and novice-player sidewaysness

## Notes

- Package version: `v1.3 Beta`
- This build refreshes the portable package from the latest corpus and is intended to supersede earlier stale copies.
- Key fixes in this beta:
  - Session 02: clipped the known OOC `Bartholomar` false-positive spill at `S02-06-329`
  - Session 05-07: retained restored `Sean_GM` attribution in breakout sessions
  - Session 06: added `Kobayashi`, `Hotel_Concierge`, and `Basilica_Priest` to registry; `Basilica_Priest` has no overlay lines (priest does not speak)
  - Session 07: added `Anita`, `White_Masked_Host`, `demonlings`, and `Basilica_Priest` registry/overlay coverage
- If a reviewer sees Session 07 with an empty `npc_overlay_report.tsv`, they are looking at an older package copy.

- `Sean_GM` is the stable speaker identity.
- `Sean_GM [NPC: X]` means Sean is speaking as a major NPC overlay.
- `npc_overlay_report.tsv` provides an audit trail for those overlays.
- `segment_manifest.tsv` is the navigation layer for each session.

## Packaging Intent

This bundle is designed so a reviewer does not need the original F: drive layout to use the transcript corpus productively.
Some provenance fields inside the corpus may still mention original source locations; that is intentional and does not prevent portable use.
