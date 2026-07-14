<!-- Copilot Instructions for PowerBIAgentTest -->
# Copilot / AI assistant guidance — PowerBIAgentTest

Purpose: short, actionable instructions so an AI coding agent can become productive quickly in this repository.

1) Big picture (what this repo does)
- This repo contains a family of "Agent" design artifacts and templates for turning Business Requirements into report designs, mockups, TRDs, and semantic models. Key flows:
  - Business Design → Decision Story (DSC) → Mockup (SVG) → TRD → Semantic Design
  - See: Agents/Decision Story Agent/README.md, Agents/Semantic Design Agent/README.md, _brief/report-spec.md

2) Major components and where to look
- Agents/: contains domain agent specs (Decision Story, TRD, Semantic Design, Mockup, utilities). Read the README in each subfolder for expected inputs/outputs and templates.
- Power BI Project/: contains PBIP and semantic model artifacts. Key files: Live Capacity Analysis.pbip and Live Capacity Analysis.SemanticModel/definition.pbism — useful when referencing real model shape.
- _brief/: contains canonical report-specs (example: report-spec.md) — good for concrete requirements used by agents.

3) Expected artifacts & naming patterns
- DSC/Report Story matrix → files named like REPORT_STORY_MATRIX_vX.X.md and REPORT_STORY_vX.X.md (see Agents/Decision Story Agent templates).
- Mockups: Markdown wireframes + SVG mockups (MOCKUP_v1.0.md, MOCKUP_v1.0.svg).
- TRD outputs: TRD_vX.X.md (see Agents/trd-agent/templates/05_TRD_TEMPLATE_v1.0.md).

4) Developer workflows & commands (how humans operate)
- Power BI authoring: use Power BI Desktop for PBIP files. These are not runnable here; expect manual verification in Power BI Desktop.
- Semantic model authoring references: use the TMDL/TMDL scripts under Power BI Project/Live Capacity Analysis.SemanticModel/TMDLScripts when creating or updating semantic models.
- There are no automated build scripts in repo; treat the agent documents and templates as source-of-truth for manual or scripted agent runs.

5) Project-specific conventions and patterns
- Agents are organized by design layer: Decision Story (report design), Mockup (visual), TRD (technical), Semantic Design (data model). Each agent README documents its inputs, outputs, templates and standards.
- Use the directory "standards/" and "templates/" inside each agent folder (e.g., Agents/trd-agent/standards/) as authoritative patterns.
- Naming convention: include version suffixes like _v1.0 or _vX.X in outputs and templates.

6) Integration points & external dependencies
- Power BI Desktop and Fabric tooling are external dependencies (human-run). Expect manual steps to open PBIP files and validate visuals.
- Semantic model builds reference Microsoft Fabric tooling (authoring skills described in Agents/Semantic Design Agent/README.md).

7) How the AI agent should operate here (practical rules)
- Prefer editing or adding Markdown artifacts and templates (DSC, MOCKUP, TRD, DATA_MODEL_MATRIX) rather than attempting to modify PBIP binaries.
- When asked to generate outputs, follow templates in the corresponding agent folder (use the exact headings and versioning format).
- Reference concrete examples when proposing text or artifacts: use content from _brief/report-spec.md, Agents/Decision Story Agent/README.md, Agents/trd-agent/README.md.

8) Quick examples (where to read templates)
- Generate a DSC: follow Agents/Decision Story Agent/Template/ or Agents/decision-story-agent/templates/02_REPORT_STORY_TEMPLATE_v1.0.md
- Generate a TRD: use Agents/trd-agent/templates/05_TRD_TEMPLATE_v1.0.md and follow the validation checklist in Agents/trd-agent/README.md

9) When to ask the user
- If a change affects a PBIP or semantic model file, request human verification and provide clear, short instructions for the manual validation steps in Power BI Desktop.
- If inputs (BRD, DSC, MOCKUP) are missing or ambiguous, list the exact missing files/sections and propose a minimal required example.

10) Feedback loop
- After producing any agent artifact, show a diff-style summary and state which template was used and which fields were inferred vs. provided.

If anything here is unclear or you'd like more examples extracted into this file (for a specific agent), tell me which agent or template and I'll extend the guidance.
