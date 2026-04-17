---
name: direct-ppt
description: Blueprint-first PPTX skill for any PowerPoint page. Use when the user wants to turn a rough brief into a confirmed blueprint, then directly generate a polished editable PPTX with bundled runtime support and a built-in presentation design lens. Best for any PPT page that should be designed once and delivered straight as PPTX.
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
2. Decide the page's **design lens** before layout: `Color System / Typography / Layout System / Visual Elements / Mood & Tone`.
3. Decide the page's **title system** before drawing blocks: plain top title, title band, section header, or another stable structure. Do not default to patching extra cards/decorations onto a weak title area.
4. Write a short markdown blueprint.
5. Wait for user approval.
6. Render the approved blueprint with `pptxgenjs`.
7. Check overlap, clipping, unexpected wraps, tiny/pale text, and visual conflicts before delivering.
8. If the page is part of a batch, repeat the same process page by page before merging/package output.

## Blueprint rules
- Main story first.
- Specify slide size, layout, block positions, table/flow structure, style rules, overflow strategy, and output filename.
- Unless the user explicitly requests otherwise, set the default slide font to **微软雅黑 / Microsoft YaHei**.
- For table-like pages, budget column widths explicitly and prefer real tables.
- Avoid tiny nested frames and merged cells unless necessary.
- If a page is fragile, simplify the layout before shrinking text.
- For cover pages, keep only the title and minimal supporting elements.
- For process pages, prefer clear blocks or step flows rather than dense micro-cards.
- For timeline/action-plan pages, use a real table and line breaks inside cells only when necessary.
- **Choose one coherent title system before styling**. If the title area still feels conflicted after local tweaks, stop patching and rebuild the title system.
- **If a main container exists, it must truly carry the content**. Budget title area, chips/tags, main table, and bottom safe area before drawing the container.
- **Do not let the top-left corner become a conflict zone** by stacking rounded background corners, title cards, accent bars, and decorative shapes in the same sensitive region.
- **If stage/group color is used, make it read as a group**, not as a single colored first column disconnected from the rest of the row.

## Design-lens rules
Before finalizing a blueprint, define these five items in plain language:
- **Color System**: main color, support color, accent color, page background, and how group/stage colors are assigned.
- **Typography**: title/body/table font sizes, weight hierarchy, and default font.
- **Layout System**: what the structural layers are (for example: title band → stage chips → main table).
- **Visual Elements**: which decorative elements are allowed, and which are intentionally removed.
- **Mood & Tone**: what the page should feel like (for example: formal, managerial, steady, presentation-ready).

This design lens is now considered **built into `direct-ppt`**. For normal PPT design work, do **not** require a separate `prezentit` skill just to get this methodology.

When a page needs stronger visual polish, use this built-in presentation design lens first: define the five items above, then let that design lens drive layout choices instead of patching visuals after the layout is already crowded.

### Integration boundary
- `direct-ppt` now absorbs the **design methodology** that proved useful in recent redesign work.
- This does **not** mean `direct-ppt` bundles or proxies the external Prezentit API service.
- Only use the separate `prezentit` skill when the user explicitly wants external Prezentit API generation and valid credentials are available.

### Title-system rules
- Prefer a **top title band** or another stable structural header for table-heavy management pages.
- Do **not** default to a floating title card if the page already has a large rounded main container; that combination often creates visual conflict instead of hierarchy.
- If a title needs help standing out, first strengthen structure (title band, spacing, safe area) before adding decorative cards or shapes.
- Decorative accents near the title must stay subordinate to the title. If the user says the title and background are "fighting", remove or weaken decoration first.

### Container and grouping rules
- If a page uses a large rounded container, all core content must sit fully inside it.
- Budget title height + chip/tag height + table height + bottom safe area before rendering.
- Treat group/stage color as a **row-group system** or **full-band system**, not a single-cell trick.
- For timeline / action-plan pages, default to: header row + grouped body rows + light row-band background + slightly stronger first-column emphasis.

## Editable-text rules
- **Default to editable text, not auto-shrunk text.**
- Unless the user explicitly requests otherwise, use **微软雅黑 / Microsoft YaHei** as the default font for titles, body copy, tables, notes, labels, and page numbers.
- In the blueprint stage, decide a reasonable fixed `fontSize`, text box width/height, line breaks, and column widths first.
- For titles, body copy, table cells, conclusions, and most labels: prefer **fixed `fontSize` + reasonable text box size**.
- **Treat `fit: 'shrink'` as forbidden by default, not optional by default.**

### Forbidden default uses of `fit: 'shrink'`
- Do **not** use `fit: 'shrink'` for page titles.
- Do **not** use `fit: 'shrink'` for subtitles and section headings.
- Do **not** use `fit: 'shrink'` for paragraphs, explanatory copy, conclusions, or notes.
- Do **not** use `fit: 'shrink'` for table headers or table body cells.
- Do **not** use `fit: 'shrink'` for process steps, timeline items, action plans, or any text the user is likely to edit later.
- Do **not** use `fit: 'shrink'` as a rescue mechanism for overcrowded layouts.

### Allowed exceptions for `fit: 'shrink'`
- Only allow `fit: 'shrink'` for a few short decorative elements such as pills, badges, tiny counters, and other non-core text that must stay inside a tight visual chip.
- These exception texts should normally be **very short** and should not carry key narrative meaning.
- If the element is likely to be edited, expanded, or reused by the user, do **not** treat it as an exception.

### Blueprint-stage mandatory text decisions
- The blueprint must state the intended `fontSize` bands for title / subtitle / body / note / table text.
- The blueprint must state the default font as **微软雅黑 / Microsoft YaHei** unless the user explicitly approves another font.
- The blueprint must state whether a text block uses fixed sizing or an allowed shrink exception.
- The blueprint must state column widths or block widths for table-like layouts.
- The blueprint must state manual line-break strategy when the text is multi-line.
- If a text block is crowded, revise layout first: widen block, reduce text amount, split the block, or simplify structure.

### Pre-delivery editable-text checklist
- Check that titles, body text, and tables are on fixed sizing rules.
- Check that `fit: 'shrink'` appears only in approved exception elements.
- Check that no core conclusion or explanatory text depends on shrink.
- Check that there is no obvious tiny text caused by emergency shrink.
- Check that the slide remains readable without relying on PowerPoint auto-fit behavior.

- If a layout is fragile, simplify the layout before shrinking text.
- Prefer manual line breaks and wider columns over runtime auto-shrink.
- If text still overflows after reasonable sizing, go back to the blueprint and adjust layout instead of hiding the problem with blanket shrink.

## Why text may look hard to edit
- When `pptxgenjs` uses `fit: 'shrink'`, it writes PowerPoint text-body auto-fit behavior.
- In practice this can make PowerPoint re-compute the visible text scale from the text box size.
- The result is: changing the text box size visibly changes the text, while manually changing font size may feel inconsistent or “not taking effect”.
- This does **not** mean the PPTX is uneditable; it means the text is controlled by auto-fit shrink behavior.

## Output rules
- Final deliverable is PPTX.
- HTML is optional preview only, never the default final artifact.
- Prefer direct PPTX generation for all approved pages.
- If the user asks for a batch, make one blueprint per page and render each page separately.

## Notes
- The point is speed, consistency, and editable PPTX output.
- This workflow is blueprint-first, approval-gated, and PPTX-only.
