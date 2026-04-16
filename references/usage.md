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
2. Draft a page blueprint.
3. Wait for approval.
4. Generate editable PPTX directly from the approved blueprint.

Use this skill for any PPT page that should be delivered as a polished `.pptx`.
