# Single Page PPTX

## Overview

Create one-slide PPTX files directly from a confirmed page blueprint. Use this skill when the user wants to discuss requirements first, then review a blueprint, and only after approval have the slide rendered into `.pptx`.

## What this skill is for

Use this skill when the request is something like:
- “把这一页做成 PPTX”
- “先给我蓝图，确认后再出成品”
- “按页做领导汇报风格的单页 PPT”
- “把表格页 / 流程页 / 时间线页做成稳定的 PPTX”

It is meant for **single-slide or tightly controlled one-page pages**, not general web pages.

## Blueprint specification

The blueprint must be a **plain markdown page spec** before any rendering starts. Keep it concise and structured.

Recommended fields:
- page number
- page title
- page goal
- audience / usage scene
- layout sketch
- content blocks
- each block's position and size
- table structure or flow structure
- style rules
- forbidden elements
- overflow / wrap strategy
- output filename

Good blueprint rules:
- state the page's main story first
- specify whether the page is a cover, table, matrix, process, timeline, or summary page
- mark which blocks need card backgrounds and which should stay flat
- for tables, list column priorities and no-wrap expectations
- for fragile pages, say whether to simplify layout before shrinking text

## Rendering tool

Use **`pptxgenjs`** to build the final `.pptx`.

Rendering expectations:
- generate the slide directly in code
- use real tables when the content is table-like
- use shapes only when they make the layout clearer
- keep the page projection-friendly and stable
- treat overlap, wrap failures, and clipping as build failures

Do not switch to HTML as the final output unless the user explicitly asks for HTML preview or the workflow requires a temporary preview artifact.

## End-to-end workflow

### Step 0. Confirm the page goal
Collect only the minimum needed:
- page number
- page title
- page goal
- audience / usage scene
- required content blocks
- forbidden directions
- style expectations

If the user already gave a clear brief, skip re-asking and move on.

### Step 1. Write a page blueprint
Create a short markdown blueprint for the page.
The blueprint must state:
- slide size / canvas
- layout structure
- each block's position and size
- key text content
- table columns / row strategy if needed
- color and emphasis rules
- overflow strategy

The blueprint should be specific enough that a renderer can build the page without guessing.

### Step 2. Show the blueprint and wait
Do **not** generate PPTX until the user confirms the blueprint.
If the user changes direction, revise the blueprint first.

### Step 3. Render the PPTX
Convert the approved blueprint into a `pptxgenjs` script and render the slide.

### Step 4. Check the output
Before sending, verify:
- no overlap
- no clipped text
- no unexpected line wraps
- no tiny or pale text
- no too-many nested frames
- table pages still look like tables

### Step 5. Deliver
Send the final `.pptx` to the user.

## Required blueprint shape

A usable blueprint should include these fields in plain language:
- page purpose
- content blocks
- layout sketch
- table or flow structure
- emphasis points
- what must not appear
- output filename

## Rendering rules

- The blueprint is the source of truth.
- The script is only a translator from blueprint to PPTX API calls.
- Prefer direct PPTX generation over HTML when the final deliverable is a slide deck.
- Treat overflow, clipping, and overlap as hard failures to fix before delivery.
- For table-heavy pages, prefer real `pptxgenjs` tables over fake block grids when the content shape allows it.
- Avoid row/column merging unless it is necessary; merged cells can trigger PPT repair or unstable rendering.
- Keep major sections on a single soft container/card if needed; avoid many tiny nested frames.
- Do not place a smaller inset “overall frame” inside an already styled slide background unless it serves a clear information purpose.
- Prefer fewer, larger visual blocks over many small bordered blocks.
- For tables, prioritize no-wrap copy, explicit column budgeting, and layout change over shrinking text.
- If a table is likely to wrap or collide, redesign the page before rendering.
- Use semantic fills and symbols for matrix pages: e.g. red/green status cells, check/cross, and a concise summary strip.
- For process pages, prefer a clear vertical 3-block flow or a clean step flow with strong section separation instead of stacked micro-cards.
- Action-plan / timeline pages should be real tables, not three disconnected color blocks.
- Page 5-style “expected output” pages should anchor on the specific scenario workflow first, then list the output assets.

## Practical output pattern

### Normal use
1. user gives page requirements
2. write blueprint
3. user approves
4. render PPTX
5. send PPTX

### If the user asks for a whole batch
- make one blueprint per page
- render each page separately
- then merge or package the outputs only after each page is stable

### If the page is fragile
- table wraps badly → widen columns or change layout
- many small blocks → collapse into fewer major blocks
- too much nesting → flatten into one main card + small accents
- text collision → reduce content, not just font size

## Failure handling

If the page cannot be rendered cleanly:
- stop and revise the blueprint
- do not ship a slide with overlap or unreadable tables
- do not hide layout problems by shrinking everything
- if a page remains unstable, simplify the page structure first

## Notes

- Use this skill for single-slide or tightly controlled one-page decks.
- For multi-page decks, create one blueprint per page and render each approved page directly into PPTX.
- Keep content concise and projection-friendly.
- If a page looks like a table, use a real table first; only fall back to block layouts when the table structure is too fragile.
