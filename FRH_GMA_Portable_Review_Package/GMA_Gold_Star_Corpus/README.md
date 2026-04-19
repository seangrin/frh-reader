# FRH GMA Gold-Star Corpus

Version: `v1.3 Beta`

This corpus is a reusable training and DR layer built on top of the WhisperX + SpeechBrain outputs.

## Current Notes

- Session 02 clips the known OOC `Bartholomar` false-positive spill at `S02-06-329`.
- Session 05-07 preserve restored `Sean_GM` attribution in breakout-session outputs.
- Session 06 and Session 07 now include explicit NPC registry and overlay coverage for the highest-value breakout-session NPCs.

## Structure

- `sessions/<session>/session_wide.md`
- `sessions/<session>/segment_manifest.tsv`
- `sessions/<session>/npc_overlay_report.tsv`
- `sessions/<session>/segments_md/*.md`
- `sessions/<session>/reviews_md/*_review.md`

## Design Rules

- Base speaker identity stays stable.
- Major NPC performance overlays are additive, not replacements for `Sean_GM`.
- Segment files are the apprenticeship reading unit.
- Review files are the critique / coaching unit.
- Session-wide files preserve legacy context plus structured NPC registry metadata.

