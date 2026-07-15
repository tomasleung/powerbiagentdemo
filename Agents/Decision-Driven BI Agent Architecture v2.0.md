# Decision-Driven BI Agent Architecture v2.0

## Purpose

Provide a structured, repeatable, decision-driven framework for designing, modeling, building, and deploying Business Intelligence solutions.

The framework separates:

```text
Business Design

↓

Technical Design

↓

Semantic Design

↓

Semantic Build

↓

Report Build
```

to ensure each artifact has a single responsibility, a defined approval process, and a governed handoff to the next phase.

The framework follows the core philosophy:

```text
Decision

↓

Business Question

↓

Signal

↓

Measure

↓

Semantic Model

↓

Report

↓

Action
```

The result is:

```text
Decision Products

not

Reporting Products
```

---

# END-TO-END FRAMEWORK FLOW

```text
PHASE 01 — BUSINESS DESIGN

BRD

↓

Decision Story Agent

INPUT
BRD

OUTPUT
REPORT_STORY_MATRIX
REPORT_STORY

↓

Mockup Agent

INPUT
REPORT_STORY

OUTPUT
MOCKUP.md
MOCKUP.svg

↓

BUSINESS APPROVAL GATE

──────────────────────────────

PHASE 02 — TECHNICAL DESIGN

TRD Agent

INPUT
REPORT_STORY
MOCKUP.md
MOCKUP.svg

OUTPUT
TRD

↓

TECHNICAL APPROVAL GATE

──────────────────────────────

PHASE 03 — SEMANTIC DESIGN

Semantic Design Agent

INPUT
TRD
REPORT_STORY

OUTPUT
DATA_MODEL_MATRIX
SEMANTIC_MODEL_SPEC
MEASURE_CONTRACT

↓

SEMANTIC APPROVAL GATE

──────────────────────────────

PHASE 04 — SEMANTIC BUILD

Semantic Build Agent

INPUT
DATA_MODEL_MATRIX
SEMANTIC_MODEL_SPEC
MEASURE_CONTRACT

OUTPUT
SEMANTIC_BUILD_SPEC
DAX_MEASURE_SPEC
TMDL_BUILD_SPEC
FABRIC_DEPLOYMENT_SPEC

↓

Power BI Authoring
(MCP / Fabric Skills)

OUTPUT
Fabric Semantic Model

↓

SEMANTIC BUILD APPROVAL GATE

──────────────────────────────

PHASE 05 — REPORT BUILD

Report Build Agent

INPUT
REPORT_STORY
MOCKUP.md
MOCKUP.svg
TRD
Fabric Semantic Model

OUTPUT
REPORT_BUILD_SPEC

↓

Power BI Authoring
(MCP / Fabric Skills)

OUTPUT
Pages
Visuals
Interactions
Power BI Report

↓

REPORT APPROVAL GATE
```

---

# PHASE 01 — BUSINESS DESIGN LAYER

## Purpose

Convert business requirements into an approved decision design and visual prototype before technical design begins.

This phase answers:

```text
What decisions require support?

What story should the report tell?

What should users see?

How should users experience the information?
```

---

# BUSINESS DESIGN FLOW

```text
BRD

↓

Decision Story Agent

↓

REPORT_STORY_MATRIX

↓

REPORT_STORY (DSC)

↓

Mockup Agent

↓

MOCKUP.md

↓

MOCKUP.svg

↓

BUSINESS APPROVAL GATE

↓

TRD Agent
```

---

# Agent 01 — Decision Story Agent

## Purpose

Convert business requirements into a decision-driven report design contract.

---

## Input

```text
BRD
```

---

## Standards

```text
REPORT_DESIGN_STANDARDS_v1.0
```

---

## Templates

```text
01_REPORT_STORY_MATRIX_TEMPLATE_v1.0

02_REPORT_STORY_TEMPLATE_v1.0
```

---

## Output 01

```text
REPORT_STORY_MATRIX_vX.X.md
```

### Purpose

Validate:

```text
Decision

Business Questions

Signals

Thresholds

Actions

Story Flow
```

---

### Key Question Answered

```text
What decisions should the report support?
```

---

## Output 02

```text
REPORT_STORY_vX.X.md
```

### Purpose

Define:

```text
Decision Model

Narrative Story

Audience

Story Flow

Layout Blueprint

Visual Recommendations

Business Journey
```

---

### Key Question Answered

```text
What story should the report tell?
```

---

## Approval Gate

```text
Approve REPORT_STORY (DSC)
```

---

# Agent 02 — Mockup Agent

## Purpose

Convert the approved Decision Story Contract into a business-review mockup and SVG prototype.

---

## Input

```text
REPORT_STORY_vX.X.md
```

---

## Standards

```text
MOCKUP_STANDARDS_v1.0

UX_THEME_STANDARD_v1.0

LAYOUT_PATTERNS_v1.0
```

---

## Templates

```text
03_MOCKUP_TEMPLATE_v1.0

04_SVG_TEMPLATE_v1.0
```

---

## Guidelines

```text
SVG_GUIDELINES_v1.0
```

---

## Output 01

```text
MOCKUP_vX.X.md
```

### Purpose

Validate:

```text
Business Journey

Story Flow

Layout Pattern

Section Order

Information Hierarchy

Visual Containers
```

---

### Key Question Answered

```text
What should users see?
```

---

## Output 02

```text
MOCKUP_vX.X.svg
```

### Purpose

Validate:

```text
Layout Pattern

Reading Flow

Visual Hierarchy

Information Placement

Stakeholder Experience
```

---

### Key Questions Answered

```text
Where should users see it?

How should users experience the story?
```

---

## Approval Gate

```text
Approve MOCKUP.md

Approve MOCKUP.svg

Approve Business Prototype
```

---

# PHASE 01 DELIVERABLES

```text
REPORT_STORY_MATRIX_vX.X.md

REPORT_STORY_vX.X.md

MOCKUP_vX.X.md

MOCKUP_vX.X.svg
```

---

# PHASE 01 EXIT CRITERIA

Approved:

```text
REPORT_STORY_MATRIX

REPORT_STORY

MOCKUP.md

MOCKUP.svg
```

Result:

```text
Business Design Complete

Ready For Technical Design
```

---

# PHASE 02 — TECHNICAL DESIGN LAYER

## Purpose

Transform approved business design artifacts into a governed technical implementation blueprint before semantic design begins.

This phase answers:

```text
What data is required?

What systems provide the data?

What technical objects are required?

How should security work?

How should the solution be validated?
```

---

# TECHNICAL DESIGN FLOW

```text
REPORT_STORY

+

MOCKUP.md

+

MOCKUP.svg

↓

TRD Agent

↓

TRD

↓

TECHNICAL APPROVAL GATE

↓

Semantic Design Agent
```

---

# Agent 03 — TRD Agent

## Purpose

Convert approved business design artifacts into a complete technical implementation contract.

---

## Inputs

```text
REPORT_STORY_vX.X.md

MOCKUP_vX.X.md

MOCKUP_vX.X.svg
```

---

## Standards

```text
TRD_STANDARDS_v1.0
```

---

## Templates

```text
05_TRD_TEMPLATE_v1.0
```

---

## Guidelines

```text
TRD_GUIDELINES_v1.0
```

---

## Output

```text
TRD_vX.X.md
```

### Purpose

Define:

```text
Report Overview

Source Systems

Source-To-Target Mapping

Fact Candidates

Dimension Candidates

Measure Inventory

Visual Mapping

Interaction Design

Security Design

Validation Rules

Deployment Considerations
```

---

### Key Question Answered

```text
How will the approved report be implemented?
```

---

## Approval Gate

Approve:

```text
TRD
```

---

# PHASE 02 DELIVERABLES

```text
TRD_vX.X.md
```

---

# PHASE 02 EXIT CRITERIA

Approved:

```text
TRD
```

Result:

```text
Technical Design Complete

Ready For Semantic Design
```

---

# PHASE 03 — SEMANTIC DESIGN LAYER

## Purpose

Transform technical requirements into governed semantic architecture and measure governance artifacts.

This phase answers:

```text
What semantic model should exist?

What facts should exist?

What dimensions should exist?

What measures should exist?

How should measures behave?
```

---

# SEMANTIC DESIGN FLOW

```text
TRD

+

REPORT_STORY

↓

Semantic Design Agent

↓

DATA_MODEL_MATRIX

↓

SEMANTIC_MODEL_SPEC

↓

MEASURE_CONTRACT

↓

SEMANTIC APPROVAL GATE

↓

Semantic Build Agent
```

---

# Governing Standard

```text
DATA_MODEL_STANDARDS_v1.0
```

Built From:

```text
Decision-Driven BI Standards

Kimball Standards

Microsoft Fabric Standards

SQLBI Standards

AI Readiness Standards
```

---

# Agent 04 — Semantic Design Agent

## Purpose

Convert approved report requirements into governed semantic architecture.

---

## Inputs

```text
TRD

REPORT_STORY

DATA_MODEL_STANDARDS
```

---

## Output 01

```text
DATA_MODEL_MATRIX_vX.X.md
```

### Purpose

Validate:

```text
Decision

Business Question

Signal

Measure

Grain

Fact

Dimension
```

---

### Key Question Answered

```text
What semantic structure is required?
```

---

## Output 02

```text
SEMANTIC_MODEL_SPEC_vX.X.md
```

### Purpose

Define:

```text
Fact Tables

Dimension Tables

Columns

Relationships

Cardinality

Filter Direction

Hierarchy Design

Performance Design
```

---

### Key Question Answered

```text
What semantic model should be built?
```

---

## Output 03

```text
MEASURE_CONTRACT_vX.X.md
```

### Purpose

Govern:

```text
Business Definitions

Business Logic

Thresholds

Actions

Dependencies

Ownership

Decision Traceability
```

---

### Key Question Answered

```text
How should measures behave?
```

---

## Approval Gate

Approve:

```text
DATA_MODEL_MATRIX

SEMANTIC_MODEL_SPEC

MEASURE_CONTRACT
```

---

# PHASE 03 DELIVERABLES

```text
DATA_MODEL_MATRIX_vX.X.md

SEMANTIC_MODEL_SPEC_vX.X.md

MEASURE_CONTRACT_vX.X.md
```

---

# PHASE 03 EXIT CRITERIA

Approved:

```text
DATA_MODEL_MATRIX

SEMANTIC_MODEL_SPEC

MEASURE_CONTRACT
```

Result:

```text
Semantic Design Complete

Ready For Semantic Build
```

---

# PHASE 04 — SEMANTIC BUILD LAYER

## Purpose

Convert approved semantic design artifacts into executable Microsoft Fabric semantic model specifications.

This phase answers:

```text
How do we build the semantic model?

How do we build measures?

How do we create TMDL?

How do we deploy the model?
```

---

# SEMANTIC BUILD FLOW

```text
DATA_MODEL_MATRIX

↓

SEMANTIC_MODEL_SPEC

↓

MEASURE_CONTRACT

↓

Semantic Build Agent

↓

SEMANTIC_BUILD_SPEC

↓

DAX_MEASURE_SPEC

↓

TMDL_BUILD_SPEC

↓

FABRIC_DEPLOYMENT_SPEC

↓

Fabric Semantic Model
```

---

# Agent 05 — Semantic Build Agent

## Status

```text
Future
```

---

## Planned Inputs

```text
DATA_MODEL_MATRIX

SEMANTIC_MODEL_SPEC

MEASURE_CONTRACT
```

---

## Planned Outputs

```text
SEMANTIC_BUILD_SPEC

DAX_MEASURE_SPEC

TMDL_BUILD_SPEC

FABRIC_DEPLOYMENT_SPEC
```

---

## Build Technologies

```text
Microsoft Fabric

PBIP

TMDL

Power BI Model Authoring MCP

semantic-model-authoring Skill

Copilot CLI

Claude Code
```

---

## Key Question Answered

```text
How should the semantic model be built?
```

---

# PHASE 04 EXIT CRITERIA

Approved:

```text
SEMANTIC_BUILD_SPEC

DAX_MEASURE_SPEC

TMDL_BUILD_SPEC

FABRIC_DEPLOYMENT_SPEC

Fabric Semantic Model
```

Result:

```text
Semantic Build Complete

Ready For Report Build
```

---

# PHASE 05 — REPORT BUILD LAYER

## Purpose

Convert approved business design artifacts and semantic models into a completed Power BI solution.

This phase answers:

```text
How should the report be implemented?

Which visuals should exist?

How should users interact with the solution?
```

---

# REPORT BUILD FLOW

```text
REPORT_STORY

↓

MOCKUP

↓

TRD

↓

Fabric Semantic Model

↓

Report Build Agent

↓

REPORT_BUILD_SPEC

↓

Power BI Pages

↓

Visuals

↓

Interactions

↓

Power BI Report
```

---

# Agent 06 — Report Build Agent

## Status

```text
Future
```

---

## Planned Inputs

```text
REPORT_STORY

MOCKUP.md

MOCKUP.svg

TRD

Fabric Semantic Model
```

---

## Planned Outputs

```text
REPORT_BUILD_SPEC

Page Specifications

Visual Specifications

Interaction Specifications

Power BI Report
```

---

## Key Question Answered

```text
How should the approved report be built?
```

---

# PHASE 05 EXIT CRITERIA

Approved:

```text
REPORT_BUILD_SPEC

Power BI Report
```

Result:

```text
Solution Complete

Ready For Production Deployment
```

---

# AGENT INVENTORY

```text
Agent 01

Decision Story Agent

Status:
✅ Production Ready

────────────────────

Agent 02

Mockup Agent

Status:
✅ Production Ready

────────────────────

Agent 03

TRD Agent

Status:
✅ Production Ready

────────────────────

Agent 04

Semantic Design Agent

Status:
✅ Production Ready

────────────────────

Agent 05

Semantic Build Agent

Status:
⬜ Future

────────────────────

Agent 06

Report Build Agent

Status:
⬜ Future
```

---

# FRAMEWORK SUCCESS STATEMENT

The framework succeeds when:

```text
Every Decision

supports a Business Question

Every Business Question

supports a Signal

Every Signal

supports a Measure

Every Measure

supports a Semantic Model

Every Semantic Model

supports a Report

Every Report

supports Business Action
```

The result is:

```text
Decision Product

not

Reporting Product
```

and every artifact provides a governed handoff to the next layer without requiring redesign of previous phases.

# AGENT DESIGN PRINCIPLE

Every agent exists to answer a specific business, design, architecture, or implementation question.

The framework follows:

```text
Question

↓

Agent

↓

Artifact

↓

Answer
```

An artifact should never exist without a clearly defined question.

Examples:

```text
What story should the report tell?

↓

Decision Story Agent

↓

REPORT_STORY

↓

Approved Decision Narrative
```

```text
What semantic model should exist?

↓

Semantic Design Agent

↓

SEMANTIC_MODEL_SPEC

↓

Approved Semantic Architecture
```

```text
How should the semantic model be built?

↓

Semantic Build Agent

↓

TMDL_BUILD_SPEC

↓

Build Instructions
```

---

# AGENT RESPONSIBILITY  MATRIX

## Agent 01 — Decision Story Agent

### Question Answered

```text
What decisions should the report support?

What business questions must be answered?

What signals must be monitored?

What story should the report tell?
```

---

## Agent 02 — Mockup Agent

### Question Answered

```text
What should users see?

Where should users see it?

How should users experience the story?

How should information be organized?

How should the business journey flow?
```

---

## Agent 03 — TRD Agent

### Question Answered

```text
How should the approved solution be implemented?

What data is required?

What systems provide the data?

What measures are required?

What security and validation rules exist?
```

---

## Agent 04 — Semantic Design Agent

### Question Answered

```text
What semantic model should exist?

What facts should exist?

What dimensions should exist?

What measures should exist?

How should measures behave?

How should business decisions be represented in the model?
```

---

## Agent 05 — Semantic Build Agent

### Question Answered

```text
How should the semantic model be built?

How should facts be implemented?

How should dimensions be implemented?

How should measures be implemented?

How should DAX be generated?

How should TMDL be generated?

How should the model be deployed?
```

---

## Agent 06 — Report Build Agent

### Question Answered

```text
How should the approved report be built?

Which pages should exist?

Which visuals should exist?

Which measures belong on which visuals?

How should users interact with the report?

How should navigation and filtering behave?
```

---

# QUESTION-TO-ARTIFACT MATRIX

| Question | Agent | Output Artifact |
|-----------|-----------|-----------|
| What decisions should the report support? | Decision Story Agent | REPORT_STORY_MATRIX |
| What story should the report tell? | Decision Story Agent | REPORT_STORY |
| What should users see? | Mockup Agent | MOCKUP.md |
| Where should users see it? | Mockup Agent | MOCKUP.svg |
| How should the approved solution be implemented? | TRD Agent | TRD |
| What semantic structure is required? | Semantic Design Agent | DATA_MODEL_MATRIX |
| What semantic model should exist? | Semantic Design Agent | SEMANTIC_MODEL_SPEC |
| How should measures behave? | Semantic Design Agent | MEASURE_CONTRACT |
| How should the semantic model be built? | Semantic Build Agent | SEMANTIC_BUILD_SPEC |
| How should DAX be implemented? | Semantic Build Agent | DAX_MEASURE_SPEC |
| How should TMDL be generated? | Semantic Build Agent | TMDL_BUILD_SPEC |
| How should the Fabric model be deployed? | Semantic Build Agent | FABRIC_DEPLOYMENT_SPEC |
| How should the approved report be built? | Report Build Agent | REPORT_BUILD_SPEC |
| What pages should exist? | Report Build Agent | Page Specifications |
| What visuals should exist? | Report Build Agent | Visual Specifications |
| How should report interactions behave? | Report Build Agent | Interaction Specifications |
| What is the final user-facing solution? | Report Build Agent | Power BI Report |

---

# FRAMEWORK DESIGN RULE

Every phase, agent, and artifact must have a clearly defined question.

Validation Rule:

```text
No Question

↓

No Agent

↓

No Artifact
```

Every artifact must be capable of answering the question that created it.

Framework Pattern:

```text
Question

↓

Agent

↓

Artifact

↓

Answer

↓

Approval

↓

Next Question
```

This ensures the entire Decision-Driven BI Framework remains:

```text
Decision Driven

Question Driven

Governed

Traceable

AI Ready

Human Reviewable
```
# CURRENT FRAMEWORK MATURITY

## Phase 01

```text
✅ Complete

Decision Story Agent

Mockup Agent
```

---

## Phase 02

```text
✅ Complete

TRD Agent
```

---

## Phase 03

```text
✅ Complete

Semantic Design Agent

Validated:
Animal Flow
```

---

## Phase 04

```text
⬜ Not Started

Semantic Build Agent
```

---

## Phase 05

```text
⬜ Not Started

Report Build Agent
```