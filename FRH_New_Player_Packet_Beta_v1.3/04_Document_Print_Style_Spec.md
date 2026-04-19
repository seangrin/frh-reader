# FRH NPP Document Print Style Spec

This file defines the printer-ready presentation target for the main New Player Packet documents.

The goal is:

- keep the improved content from newer drafts
- restore the stronger visual and page-design qualities from older authored `.docx` files
- produce PDFs that look intentional, readable, and worth printing

## Scope

Apply this spec primarily to:

- `01_Edgar Von Haupt Letter`
- `02_Character_Creation_Guide_FRH`
- `03_Cloudburg`
- `04_Pre-generated_Character_Mechanics_Overview`
- `05_Tiberius_Example_Playthrough`

## Baseline Model

Use [04_Pre-generated_Character_Mechanics_Overview_beta_v4.1.docx](C:\Users\seang\OneDrive\Documents\ChatGPT_FRH\FRH_New_Player_Packet_Beta_v1.3\04_Pre-generated_Character_Mechanics_Overview_beta_v4.1.docx) as the visual model.

Use [04_Pre-generated_Character_Mechanics_Overview_beta_v4.2.docx](C:\Users\seang\OneDrive\Documents\ChatGPT_FRH\FRH_New_Player_Packet_Beta_v1.3\04_Pre-generated_Character_Mechanics_Overview_beta_v4.2.docx) as the content model.

Short version:

- `v4.1` had better document design
- `v4.2` has better packet structure and current content

## Page Setup

Target page setup:

- Letter size
- margins close to `0.5"` on all sides
- single-column layout
- no unnecessary page breaks inside short character entries

The packet should feel compact but not cramped.

## Typography

Use a real document hierarchy, not default Word styling.

Recommended heading scale:

- `Heading 1`: approximately `24 pt`, bold
- `Heading 2`: approximately `18 pt`, bold
- `Heading 3`: approximately `14 pt`, bold
- `Body Text`: approximately `11-12 pt`

Body text should be the default paragraph style for prose.

Avoid building the document mostly out of:

- `Normal`
- raw blank paragraphs
- default bullet style with no spacing control

## Paragraph Rhythm

Prefer style-driven spacing rather than empty spacer paragraphs.

Body text target:

- `1.1` to `1.15` line spacing
- modest space after paragraphs
- no first-line indent unless the document intentionally uses one

Headings should have:

- visible space before
- controlled space after
- `keep with next` where appropriate

## Dividers And Section Rhythm

Major document sections should be visually separated.

Use one of:

- a divider style similar to the old `Horizontal Line`
- extra section spacing with consistent rules
- occasional page breaks only where a major section truly needs one

Do not rely on random blank lines to create shape.

## Lists

Use bullets only when the content is truly list-shaped.

Good uses:

- what a character highlights
- packet contents
- required structural features

Avoid over-bulleting short prose that reads better as paragraphs.

For `04`, specifically:

- archetype lines should probably be styled body text, not bullets
- “What this highlights” sections can remain bullets

## Markdown Artifact Cleanup

Do not allow markdown syntax to survive into printer-ready `.docx` files.

Remove:

- literal backticks
- markdown-style pseudo-emphasis
- markdown-looking list carryovers if they degrade print appearance

Convert them into:

- italics
- bold
- proper headings
- proper bullets

## Document 04 Specific Guidance

For [04_Pre-generated_Character_Mechanics_Overview_beta_v4.2.docx](C:\Users\seang\OneDrive\Documents\ChatGPT_FRH\FRH_New_Player_Packet_Beta_v1.3\04_Pre-generated_Character_Mechanics_Overview_beta_v4.2.docx):

1. Keep the current content structure.
2. Restore a stronger title and section hierarchy.
3. Replace `Normal`-heavy layout with `Body Text`.
4. Remove literal backticks from phrases like point totals and trait bundles.
5. Add stronger visual separation between:
   - Standard Packet Pregens
   - Advanced Evolution Examples
   - Advanced Appendix Note
   - Structural Notes
   - Final Guidance
6. Make sure each character entry opens cleanly and does not visually blur into the next.

## Printer-Ready Quality Bar

A document is ready when:

- it reads well on paper
- it does not look like a markdown export
- headings are visually strong
- spacing feels deliberate
- the PDF can be skimmed quickly by a new player
- the packet feels like a curated game handout, not an internal draft

## Working Recommendation

For final packet release PDFs:

- do not rely on automatic markdown-to-docx generation alone
- maintain a styled `.docx` master for each core packet document
- use the release builder only after the printer-ready `.docx` has been manually polished
