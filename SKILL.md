---
name: blueprint-pptx
description: Blueprint-first single-slide PPTX skill. Use when the user wants to turn a rough brief into a confirmed page blueprint, then render a polished editable PPTX with pptxgenjs. Best for one-page report slides, timelines, action plans, matrices, and other tightly controlled pages.
---

# Blueprint PPTX

Use this skill when the user wants a **single-slide or tightly controlled one-page PPTX** and wants a blueprint reviewed before rendering.

## When to use
- “把这一页做成 PPTX”
- “先出蓝图，确认后再出成品”
- “做领导汇报页 / 行动计划页 / 时间线页”
- “把表格页、矩阵页、流程页做成可编辑 PPTX”

## Workflow
1. Collect the minimum brief: page title, goal, audience, required blocks, forbidden directions, style.
2. Write a short markdown blueprint.
3. Wait for user approval.
4. Render the slide with `pptxgenjs`.
5. Check overlap, clipping, and unexpected wraps before delivering.

## Blueprint rules
- Main story first.
- Specify slide size, layout, block positions, table/flow structure, style rules, overflow strategy, and output filename.
- For table-like pages, budget column widths explicitly and prefer real tables.
- Avoid tiny nested frames and merged cells unless necessary.
- If a page is fragile, simplify the layout before shrinking text.

## Output rules
- Final deliverable is PPTX.
- Treat HTML as optional preview only, never as the default final artifact.
- Prefer direct PPTX generation for all approved pages.
- If the user asks for a batch, make one blueprint per page and render each page separately.

## Notes
- This skill used to be named `single-page-pptx`.
- The workflow is blueprint-first, approval-gated, and PPTX-only.
