# FRH GMA Portable Review Package Release Notes

Version: `v1.3 Beta`
Date: `2026-04-15`

## Intent

This beta is the current candidate package for GMA-auditor review before live apprenticeship training begins.

## Included Fixes

- Session 02: removed the known OOC `Bartholomar` overlay spill at `S02-06-329`
- Session 05-07: preserved restored `Sean_GM` attribution in breakout-session corpus outputs
- Session 06: added `Kobayashi`, `Hotel_Concierge`, and `Basilica_Priest` to the session registry; `Basilica_Priest` carries no overlay lines — the priest does not speak in this session and functions as atmospheric presence only
- Session 07: added `Anita`, `White_Masked_Host`, `demonlings`, and `Basilica_Priest` to the session registry and overlay pass
- Session 07: portable package rebuilt from the updated corpus so `npc_overlay_report.tsv` is no longer empty in the current build

## Validation Notes

- Reviewers should begin with `README.md`
- `npc_overlay_report.tsv` is an audit trail, not a claim of perfect canon
- `Sean_GM` remains the base speaker identity; NPC overlays are additive

## Warning About Older Copies

If a reviewer finds any of the following, they are likely using an older package:

- Session 07 `npc_overlay_report.tsv` contains only a header row
- Session 06 `session_wide.md` has an empty Major NPC Registry
- Session 02 still shows `S02-06-329` as `Bartholomar`
