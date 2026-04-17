# direct-ppt

Blueprint-first PPT workflow.

## Install / handoff
- Copy this skill folder into the target agent workspace.
- Keep `assets/runtime/` with the skill.
- Prefer the host's installed `pptxgenjs` if it exists.
- Otherwise use the bundled offline runtime via `scripts/pptx-runtime.js`.
- No extra npm install is required for the bundled path.

## Workflow
1. Discuss the brief.
2. Decide the page's design lens first: **Color System / Typography / Layout System / Visual Elements / Mood & Tone**.
3. Choose the title system before drawing shapes: top title, title band, section header, or another stable structure.
4. Draft a page blueprint.
5. Wait for approval.
6. Generate editable PPTX directly from the approved blueprint.

## Design-lens guidance
For pages that need more polish, do not jump straight into coordinates. First define:
- **Color System**: page background, main color, support color, accent color, and group/stage coloring strategy.
- **Typography**: title/body/table font sizes, weights, and default font.
- **Layout System**: the page's structural layers such as title band → stage chips → table.
- **Visual Elements**: which accents are allowed and which are intentionally removed.
- **Mood & Tone**: the intended feeling, such as formal, managerial, calm, data-driven, or polished.

This design lens is already **built into `direct-ppt`**. For normal PPT work, do not require a separate `prezentit` skill just to access this thinking model.

When visual quality matters, explicitly lock these five items first, then let them guide hierarchy, grouping, and title treatment.

## Integration boundary
- `direct-ppt` now includes the useful design methodology extracted from recent `prezentit`-inspired redesign work.
- It does **not** include the external Prezentit API generation service.
- Use the separate `prezentit` skill only when the user explicitly wants that external API workflow and credentials are available.

## Title-system guidance
- For table-heavy management pages, prefer a **top title band** or another stable structural header.
- If a page already has a large rounded main container, avoid defaulting to a floating title card on top of it; that often creates visual conflict in the top-left corner.
- If the title still feels weak, strengthen structure and spacing first. Do not immediately add more decorative cards or accent shapes.
- If the user says the title and background are fighting, assume the title system is wrong before assuming the coordinates are wrong.

## Container / grouping guidance
- If a main rounded container exists, it must fully hold the title area, chips/tags, main table, and bottom safe area.
- For grouped tables, do not color only the first column unless the rest of the design clearly supports that choice.
- Default grouped-table strategy: full row-group background + stronger first-column emphasis + consistent header row.
- If stage/group information matters, make the grouping visible across the row or band, not only at the row label.

## Editable-text guidance
- Default strategy: **fixed `fontSize` + reasonable text box size + manual line breaks where needed**.
- Default font: **微软雅黑 / Microsoft YaHei** unless the user explicitly asks for another font.
- `fit: 'shrink'` is **forbidden by default**.

### Do not use `fit: 'shrink'` for
- page titles
- subtitles and section headings
- paragraphs and explanatory text
- table headers or body cells
- process steps, timelines, action plans, conclusions, and other user-editable core content

### Only allow `fit: 'shrink'` for
- very short decorative text only
- pills / chips / badges / tiny counters
- non-core text that is unlikely to be edited later

### Mandatory blueprint decisions
- State the intended `fontSize` for title / subtitle / body / note / table text.
- State the default font as **微软雅黑 / Microsoft YaHei** unless explicitly overridden by the user.
- State text box width/height or table column widths.
- State where manual line breaks are expected.
- If content is crowded, revise layout first instead of shrinking text.

### Pre-delivery checks
- Confirm core text is on fixed sizing rules.
- Confirm `fit: 'shrink'` appears only in approved exception elements.
- Confirm no important narrative text depends on auto-fit shrink.
- Confirm there is no emergency tiny text caused by last-minute shrink.

- If content feels crowded, go back to the blueprint and loosen layout, widen columns, or simplify blocks before shrinking text.
- If later editing in PowerPoint matters, keep the text body on fixed sizing rules instead of auto-fit shrink rules.

## Why PowerPoint may feel like font size cannot be changed
- `fit: 'shrink'` in `pptxgenjs` maps to PowerPoint auto-fit shrink behavior.
- That makes the visible text scale depend on the text box geometry.
- So resizing the box changes the visible text size, while manually changing the font size can feel inconsistent.
- This is an auto-fit issue, not a “PPTX cannot be edited” issue.

Use this skill for any PPT page that should be delivered as a polished `.pptx`.
