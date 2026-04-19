# FRH Optional Pregenerated Characters Library Packaging Plan

## Goal

Create an optional companion package to the `FRH_New_Player_Packet_Beta_v1.3` that offers:

- more pregenerated character choices
- more worked examples of successful FRH concepts
- a stronger player-facing shelf for people who want to browse character fantasies before building their own

## Why This Package Exists

The core `NPP` should remain:

- approachable
- fairly compact
- onboarding-focused

The optional library can safely be:

- larger
- more varied
- more advanced
- more example-heavy

## Proposed Package Shape

### 1. Ready-To-Play Pregens

Use for:

- strong, table-ready characters with stable canonical finals

Current likely inclusions:

- `Adrian Draik`
- `Gabriel Voss`
- `Siegfried Vane`
- `Tomas Solis`

### 2. Character Examples

Use for:

- good characters that teach FRH tone or build ideas
- characters that may be excellent references even if they are not default pregens for every new player

Current likely inclusion:

- `Suzette Vale`

### 3. Advanced And Exotic Options

Use for:

- stranger concepts
- higher-complexity supernatural lanes
- concepts that are better for curious or experienced players

Current likely inclusions:

- `Father Elias Kane`
- `Silas Rourke`

### 4. How To Use These Characters

Short player-facing notes:

- pick one and play it mostly as written
- customize names, background details, and a few skills/quirks if desired
- use these as examples if building a new character from concept

## Source Of Truth

Engineering source:

- `GCB_Tests`

Player-facing packaged source:

- the selected canonical final files copied into this optional library

Current beta-side feed shelf:

- `01_Ready_To_Play_Pregens\\Library_Feed`
- `02_Character_Examples\\Library_Feed`

Practical rule:

- keep the engineering shelf and the player shelf separate
- do not expose the full builder/version trail in the player package by default

## Future Nice-To-Haves

- one-page character blurbs
- character role tags like:
  - investigator
  - occultist
  - protector
  - social predator
  - bruiser-caster
- a simple chooser guide:
  - "play this if you want..."
