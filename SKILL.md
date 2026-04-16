---
name: direct-ppt
description: Blueprint-first PPTX skill for any PowerPoint page. Use when the user wants to turn a rough brief into a confirmed blueprint, then directly generate a polished editable PPTX with bundled runtime support. Best for any PPT page that should be designed once and delivered straight as PPTX.
---

# Direct PPT

Use this skill when the user wants **any PPT page** to be delivered directly as editable `.pptx` after a blueprint review.

## When to use
- “这个 PPT 直接出成品”
- “先出蓝图，确认后直出 PPTX”
- “做任何汇报页、封面页、目录页、路线图页、时间线页”
- “把一页 PPT 按蓝图直接生成，可编辑、可交付”
- “做 PPT 任务就用这个 skill，不区分单页/多页”

## Scope
- This is the **single entry skill for all PPT creation tasks**.
- Use it for cover pages, single pages, and multi-page batches.
- For multi-page work, still keep **one blueprint per page** and render pages separately, then package the outputs.

## Bundled runtime
- The skill includes an offline-friendly runtime in `assets/runtime/`.
- Prefer the bundled runtime when the environment cannot install npm packages.
- Runtime files:
  - `assets/runtime/pptxgen.bundle.js`
  - `assets/runtime/jszip.min.js`
- Loader helper:
  - `scripts/pptx-runtime.js`

## Quick install
1. Copy the whole `direct-ppt/` skill folder into the target agent workspace.
2. Keep `assets/runtime/` next to `SKILL.md`.
3. If the host already has `pptxgenjs`, the skill can use it directly.
4. If not, the bundled runtime will fall back to the vendored files automatically.
5. Start with the brief, lock the blueprint, then render the approved slide to `.pptx`.

## Workflow
1. Collect the minimum brief: page title, goal, audience, required blocks, forbidden directions, style.
2. Write a short markdown blueprint.
3. Wait for user approval.
4. Render the approved blueprint with `pptxgenjs`.
5. Check overlap, clipping, unexpected wraps, and tiny/pale text before delivering.
6. If the page is part of a batch, repeat the same process page by page before merging/package output.

## Blueprint rules
- Main story first.
- Specify slide size, layout, block positions, table/flow structure, style rules, overflow strategy, and output filename.
- For table-like pages, budget column widths explicitly and prefer real tables.
- Avoid tiny nested frames and merged cells unless necessary.
- If a page is fragile, simplify the layout before shrinking text.
- For cover pages, keep only the title and minimal supporting elements.
- For process pages, prefer clear blocks or step flows rather than dense micro-cards.
- For timeline/action-plan pages, use a real table and line breaks inside cells only when necessary.

## Output rules
- Final deliverable is PPTX.
- HTML is optional preview only, never the default final artifact.
- Prefer direct PPTX generation for all approved pages.
- If the user asks for a batch, make one blueprint per page and render each page separately.

## Notes
- The point is speed, consistency, and editable PPTX output.
- This workflow is blueprint-first, approval-gated, and PPTX-only.
