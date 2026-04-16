---
name: single-page-pptx
description: "Use when the user wants a single-slide PPTX created end-to-end from requirements discussion: first confirm the brief, then draft a page blueprint, wait for user approval, and finally generate the PPTX directly from the blueprint with pptxgenjs. Best for one-page leadership slides, roadmap slides, and other tightly controlled presentation pages."
---

# Single Page PPTX

## Overview

Create one-slide PPTX files directly from a confirmed page blueprint. Use this skill when the user wants to discuss requirements first, then review a blueprint, and only after approval have the slide rendered into `.pptx`.

## Workflow

1. **Confirm the brief**
   - Clarify page goal, audience, key message, content blocks, and style.
   - Keep this round focused on what belongs on the slide, not implementation details.

2. **Draft a page blueprint**
   - Produce a concise blueprint in markdown.
   - Include slide size, element positions, typography, colors, spacing, and content budget.
   - Make the blueprint specific enough that it can be rendered without guesswork.

3. **Wait for approval**
   - Do not generate the PPTX until the user confirms the blueprint is correct.
   - If the user requests changes, update the blueprint first.

4. **Render the PPTX**
   - Convert the approved blueprint into a rendering script.
   - Use `pptxgenjs` to draw the slide directly.
   - Output the `.pptx` file and send it to the user.

## Blueprint Requirements

The blueprint should capture:

- slide size / canvas
- element coordinates: `x`, `y`, `w`, `h`
- typography: font size, weight, color, line height
- shapes: fill, border, radius, shadow
- tables: column widths, row heights, content limits
- overflow handling: shorten, split, shrink, or change layout

## Rendering Principles

- The blueprint is the source of truth.
- The script is a translator from blueprint to PPTX API calls.
- Prefer direct PPTX generation over HTML when the final deliverable is a slide deck.
- Treat overflow, clipping, and overlap as hard failures to fix before delivery.
- For table-heavy pages, prefer real `pptxgenjs` tables over fake block grids when the content shape allows it.
- Avoid row/column merging unless it is necessary; merged cells can trigger PPT repair or unstable rendering.

## Practical Output Pattern

When the user asks for a PPT:

1. discuss requirements
2. draft blueprint
3. wait for approval
4. generate PPTX
5. optionally provide HTML only as a preview artifact if explicitly useful

## Notes

- Use this skill for single-slide or tightly controlled one-page decks.
- For multi-page decks, create one blueprint per page and render each approved page directly into PPTX.
- Keep content concise and projection-friendly.
- If a page looks like a table, use a real table first; only fall back to block layouts when the table structure is too fragile.
