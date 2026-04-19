# Joe Bob Gray Shapeshifters Engineering Note

Date:

- `2026-03-20`

Purpose:

- document the GM-facing engineering correction to `Joe Bob Gray`
- record that the old `Supers`-style transformation expression was replaced with the clearer `Shapeshifters` workflow already used on `Edwin March`
- note that this file is source/engineering material and is **not** intended for Release promotion

## What Changed

Human form:

- the old cheap transformation shell was replaced
- current human-side expression is:
  - `Alternate Form (Werewolf) [296]`
  - `Uncontrolled Change 4 [-50]`
  - `Secret (Uncontrollable Werewolf) [-20]`

Werewolf form:

- the werewolf sheet was re-read as a true alternate-form workbench
- the old fake `Transformation (Werewolf)` shell was removed
- `Uncontrolled Change` was moved off the form so curse-control lives on the human sheet
- shared campaign baggage that should not distort form math was stripped from the werewolf workbench

## Why It Changed

The original `Supers` implementation captured the trope but badly underpriced the form.

Old expression:

- `Transformation (Werewolf) [4]`

That was not close to the real value of Joe Bob's werewolf state.

Using the project `Shapeshifters` workflow:

1. human sheet stays canonical
2. monster sheet becomes a template/workbench
3. `PPT/NPT` is estimated from human-to-form deltas
4. the alternate-form cost is back-ported onto the human sheet

That brought Joe Bob into line with the newer Edwin March implementation and gives GMs and players one readable alternate-form method to check against the book.

## Current Working Read

- Joe Bob now uses the same man -> monster -> back-port logic as Edwin
- this makes the werewolf cost honest enough for play and much easier to audit
- it also leaves room for the human investigator side to be competent instead of being crushed by an unrealistically cheap but badly structured transformation shell

## Release Boundary

This note is GM-facing engineering documentation.

For Release:

- promote the character PDFs
- optionally promote selected PDF notes if useful

Do **not** treat this markdown note as player-facing Release material unless that policy changes later.
