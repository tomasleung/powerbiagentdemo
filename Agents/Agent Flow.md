# Decision-Driven BI Agent Architecture v1.0

## Purpose

Provide a structured, repeatable, and decision-first framework for designing, modeling, and building Business Intelligence solutions.

The framework separates:

```text
Business Design

Technical Design

Semantic Design

Solution Build
```

to ensure each artifact has a single responsibility and can be reviewed independently.

---

# End-to-End Flow

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
MOCKUP
↓
SVG

↓
TRD Agent
↓
TRD

↓
Semantic Design Agent
↓
DATA_MODEL_MATRIX
↓
SEMANTIC_MODEL_SPEC
↓
MEASURE_CONTRACT

↓
Semantic Build Agent (Future)
↓
Fabric Semantic Model

↓
Report Build Agent (Future)
↓
Power BI Report
```

---

# PHASE 01 — BUSINESS DESIGN LAYER

## Input

```text
Business Requirements Document (BRD)
```

Purpose

```text
Capture business goals.

Capture business questions.

Capture decisions requiring support.
```

---

# Agent 01 — Decision Story Agent

## Purpose

Convert business requirements into a decision-driven report design.

---

## Governing Standard

```text
REPORT_DESIGN_STANDARDS
```

---

## Input

```text
BRD
```

---

## Output 01

```text
REPORT_STORY_MATRIX
```

Purpose

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

## Output 02

```text
REPORT_STORY (DSC)
```

Purpose

Define:

```text
Narrative Story

Audience

Actions

Layout Blueprint

Visual Recommendations

Business Flow
```

---

## Key Question Answered

```text
What story should the report tell?
```

---

# Agent 02 — Mockup Agent

## Purpose

Convert the approved DSC into report wireframes.

---

## Input

```text
REPORT_STORY (DSC)
```

---

## Output 01

```text
MOCKUP.md
```

Purpose

Validate:

```text
Section Order

Story Flow

Information Hierarchy
```

---

## Output 02

```text
MOCKUP.svg
```

Purpose

Visual representation of the approved dashboard design.

---

## Key Question Answered

```text
What should users see?
```

---

# PHASE 02 — TECHNICAL DESIGN LAYER

# Agent 03 — TRD Agent

## Purpose

Convert report design into a high-level implementation blueprint.

---

## Input

```text
BRD

REPORT_STORY (DSC)

MOCKUP
```

---

## Output

```text
TRD
```

---

## TRD Sections

```text
01 Report Overview

02 Source & Target Mapping

03 High-Level Data Model

04 Measure Inventory

05 Visual Mapping

06 Interaction Design

07 Security Design

08 Validation Rules

09 Deployment Considerations
```

---

## Key Question Answered

```text
How will the approved report be implemented?
```

---

# PHASE 03 — SEMANTIC DESIGN LAYER

## Governing Standard

```text
DATA_MODEL_STANDARDS_v1.0
```

Built From:

```text
Decision-Driven BI Standards

Kimball Standards

Microsoft Fabric Standards

SQLBI Best Practices
```

---

# Agent 04 — Semantic Design Agent

## Purpose

Convert approved report requirements into a semantic model design.

---

## Input

```text
TRD

REPORT_STORY (DSC)

DATA_MODEL_STANDARDS
```

---

## Output 01

```text
DATA_MODEL_MATRIX
```

Purpose

Validate:

```text
Decision

Signals

Measures

Grain

Facts

Dimensions
```

---

### Key Questions Answered

```text
What decisions are supported?

What signals are required?

What measures are required?

What is the grain?

What facts are required?

What dimensions are required?
```

---

## Output 02

```text
SEMANTIC_MODEL_SPEC
```

Purpose

Define:

```text
Tables

Columns

Data Types

Relationships

Cardinality

Filter Direction
```

---

### Key Questions Answered

```text
What does the semantic model look like?
```

---

## Output 03

```text
MEASURE_CONTRACT
```

Purpose

Govern:

```text
Business Definitions

Calculations

Thresholds

Actions

Decision Traceability
```

---

### Key Questions Answered

```text
How should measures behave?
```

---

# PHASE 04 — BUILD LAYER

# Agent 05 — Semantic Build Agent (Future)

## Purpose

Build the Fabric Semantic Model.

---

## Input

```text
SEMANTIC_MODEL_SPEC

MEASURE_CONTRACT
```

---

## Implementation Standard

```text
Microsoft Fabric
Semantic Model Authoring
```

---

## Output

```text
Fabric Semantic Model

Tables

Relationships

Measures

Descriptions

Security
```

---

## Key Question Answered

```text
Build the semantic model.
```

---

# Agent 06 — Report Build Agent (Future)

## Purpose

Build the Power BI report.

---

## Input

```text
REPORT_STORY (DSC)

SVG

TRD

Semantic Model
```

---

## Output

```text
Power BI Report
```

---

## Key Question Answered

```text
Build the approved dashboard.
```

---

# Artifact Ownership Matrix

| Artifact | Owner |
|-----------|-----------|
| BRD | Business |
| REPORT_STORY_MATRIX | Decision Story Agent |
| REPORT_STORY (DSC) | Decision Story Agent |
| MOCKUP.md | Mockup Agent |
| MOCKUP.svg | Mockup Agent |
| TRD | TRD Agent |
| DATA_MODEL_MATRIX | Semantic Design Agent |
| SEMANTIC_MODEL_SPEC | Semantic Design Agent |
| MEASURE_CONTRACT | Semantic Design Agent |
| Fabric Semantic Model | Semantic Build Agent |
| Power BI Report | Report Build Agent |

---

# Guiding Philosophy

```text
Decision
↓
Business Question
↓
Signal
↓
Threshold
↓
Action
↓
Story
↓
Report Design
↓
Technical Design
↓
Semantic Design
↓
Build
```

---

# Framework Success Statement

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
supports Action
```

The result is a Decision Product rather than a Reporting Product.



```text
BRD
↓
Decision Story Agent
  - Input: BRD
  - Output: REPORT_STORY_MATRIX, REPORT_STORY (DSC)
  - Validate: decisions, questions, signals, thresholds, actions
  - Gate: approve REPORT_STORY (DSC)
↓
Mockup Agent
  - Input: REPORT_STORY (DSC)
  - Output: MOCKUP.md, MOCKUP.svg
  - Validate: story flow, section order, visual hierarchy
  - Gate: approve mockup
↓
TRD Agent
  - Input: BRD, REPORT_STORY (DSC), MOCKUP
  - Output: TRD
  - Validate: source/target mapping, measure inventory, implementation feasibility
  - Gate: approve TRD
↓
Semantic Design Agent
  - Input: TRD, REPORT_STORY (DSC), DATA_MODEL_STANDARDS
  - Output: DATA_MODEL_MATRIX, SEMANTIC_MODEL_SPEC, MEASURE_CONTRACT
  - Validate: grain, facts, dimensions, relationships, measure traceability
  - Gate: approve semantic design artifacts
↓
Semantic Build Agent (Future)
  - Input: SEMANTIC_MODEL_SPEC, MEASURE_CONTRACT
  - Output: Fabric Semantic Model
  - Validate: model build success, measure support, security
  - Gate: approve semantic model build
↓
Report Build Agent (Future)
  - Input: REPORT_STORY (DSC), SVG, TRD, Semantic Model
  - Output: Power BI Report
  - Validate: report alignment, visual layout, interactivity
  - Gate: approve report build
```

This diagram helps keep your workflow explicit and supports governance at each handoff.