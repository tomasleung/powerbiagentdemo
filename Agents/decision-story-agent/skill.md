# Decision-Driven BI Report Design Skill v1.0

## Purpose

Transform a Business Requirements Document (BRD) into a Decision-Driven BI report design by starting with business decisions and required actions before considering visuals, layouts, or Power BI implementation.

The skill follows the Decision-Driven BI Framework:

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
Narrative Story
↓
Page Design
↓
Visual Selection
↓
Decision Story Contract (DSC)
↓
Markdown Wireframe
↓
SVG Mockup
↓
Technical Requirements Document (TRD)
↓
Build
```

---

# Design Philosophy

Traditional BI Process

```text
Data
↓
Chart
↓
Dashboard
↓
User Figures It Out
```

Decision-Driven BI Process

```text
Decision
↓
Question
↓
Signal
↓
Action
↓
Story
↓
Dashboard
```

The purpose of the dashboard is not to display data.

The purpose of the dashboard is to help users make decisions.

---

# Core Principles

## Rule 1 — Decision First

Never start with visuals.

Start with:

- Decision Supported
- Business Questions
- User Personas
- Thresholds
- Operational Actions

If the decision cannot be clearly stated, stop before continuing.

---

## Rule 2 — Every KPI Must Support Action

All page-one KPIs must support:

```text
Signal
↓
Threshold
↓
Status
↓
Action
↓
Decision
```

Example

```text
KPI:
Care Capacity %

Signal:
Animals In Care ÷ Care Capacity

Thresholds:

<80%
Healthy

80%-99%
Monitor

100%+
Full

Actions:

Healthy
Candidate Centre

Monitor
Review Before Routing

Full
Do Not Intake

Decision:
Can this centre safely receive another animal?
```

---

## Rule 3 — If No Action Exists, Remove the KPI

Do not place a KPI on Page 1 unless it supports a decision.

Bad KPI

```text
Total Animals
```

Good KPI

```text
Remaining Care Capacity
```

because it supports intake decisions.

---

## Rule 4 — Story Before Visuals

Never choose charts before defining the report story.

Incorrect

```text
Data
↓
Chart
```

Correct

```text
Decision
↓
Question
↓
Signal
↓
Action
↓
Story
↓
Visual
```

---

## Rule 5 — SVG Must Not Invent Logic

The SVG wireframe may only visualize approved content from the DSC.

SVG is a rendering artifact.

The SVG must never introduce:

- New KPIs
- New Questions
- New Business Rules
- New Decisions

---

# Required Inputs

The skill expects the following BRD content.

## Mandatory

```text
Decision Supported

Business Questions

Required Information

Signals

Threshold Rules

Success Criteria

User Personas
```

## Optional

```text
KPI Contracts

Data Sources

Governance Rules

Existing Reports

Mockups
```

---

# Skill Workflow

## Step 1 — Extract Decision Model

Purpose

Identify the business decision the report exists to support.

Output

```text
Primary Decision

Secondary Decisions

Decision Owner

Decision Frequency

Key Discovery
```

Example

```text
Primary Decision

Which centres can safely receive additional animals?

Secondary Decisions

Which centres require intervention?

Which centres should be avoided?

Which centres require data quality review?

Decision Owner

Animal Flow

Frequency

Multiple Times Per Day
```

Output Artifact

```text
Decision Summary
```

---

## Step 2 — Build Business Question Matrix

Purpose

Convert business questions into decision categories.

Output Format

```text
Question

Decision Category

Priority
```

Example

```text
Which centres currently have available CAT capacity?

Decision Category
Placement

Priority
High
```

Output Artifact

```text
Business Question Matrix
```

---

## Step 3 — Build Signal Matrix

Purpose

Map questions to measurable signals.

Output Format

```text
Question

Supporting Signals
```

Example

```text
Question

Can this centre receive another animal?

Signals

Animals In Care

Care Capacity

Remaining Capacity

Physical Space

Emergency Closure
```

Output Artifact

```text
Signal Matrix
```

---

## Step 4 — Build Threshold Matrix

Purpose

Convert signals into operational states.

Output Format

```text
Signal

Threshold

Status

Action
```

Example

```text
Care Capacity %

<80%
Healthy
Candidate Centre

80%-99%
Monitor
Review Before Routing

100%+
Full
Do Not Intake
```

Output Artifact

```text
Threshold Matrix
```

---

## Step 5 — Build Action Matrix

Purpose

Define operational responses.

Output Format

```text
Condition

Recommended Action
```

Example

```text
Capacity >=100%

Action

Do Not Intake
```

Output Artifact

```text
Action Matrix
```

---

## Step 6 — Generate Narrative Story

Purpose

Determine how the report tells its story.

Output Format

```text
Question

Output Section

Audience

Intended Action
```

Example

```text
Question

Can this centre safely take another animal?

Output

Intake Readiness

Audience

Animal Flow

Action

Determine Placement Options
```

Output Artifact

```text
Narrative Story
```

---

## Step 7 — Select Page Archetype

Purpose

Identify report behavior.

Available Archetypes

```text
Operational Command Centre

Capacity Intelligence

Executive Monitoring

Data Quality Investigation

Regional Performance

Exception Management
```

Output Artifact

```text
Page Archetype
```

---

## Step 8 — Build Layout Blueprint

Purpose

Define reading order.

Output Format

```text
Section

Purpose

Audience

Decision Supported
```

Example

```text
Operational Snapshot

Purpose

Provide Context

Audience

All Users

Decision

None
```

Output Artifact

```text
Layout Blueprint
```

---

## Step 9 — Select Visuals

Purpose

Map business questions to visual types.

Output Format

```text
Question

Visual

Reason
```

Example

```text
Question

Which centres should receive animals?

Visual

Priority Table

Reason

Supports ranking and action.
```

Output Artifact

```text
Visual Recommendations
```

---

# Output Artifact 01

# Decision Story Contract (DSC)

File Name

```text
REPORT_STORY_vX.X.md
```

Purpose

Convert business requirements into an approved report narrative and design blueprint.

Required Sections

```text
Document Metadata

01 Decision Model

02 Business Question Matrix

03 Business Logic Model

04 Signal Matrix

05 Threshold Matrix

06 Action Matrix

07 Narrative Story

08 Page Archetype

09 Layout Blueprint

10 Visual Recommendations

11 Markdown Wireframe

12 Success Criteria
```

Approval Required

```text
Business Owner

Product Owner

Report Designer
```

---

# Output Artifact 02

# Markdown Wireframe

File Name

```text
MOCKUP_vX.X.md
```

Purpose

Validate report structure and information hierarchy before visual design.

Contents

```text
Section Layout

Reading Order

Business Purpose

Decision Support

KPI Placement

Narrative Flow
```

Example

```text
Operational Snapshot

Action Required

Intake Readiness

Placement Decision Board

Capacity vs Occupancy

Species Occupancy

Data Trust

Regional Health

AI Operational Briefing
```

Approval Required

```text
Business Owner

Report Designer
```

---

# Output Artifact 03

# SVG Wireframe

File Name

```text
MOCKUP_vX.X.svg
```

Purpose

Visual representation of the approved Markdown Wireframe.

Rules

```text
Must not add new logic.

Must follow DSC.

Must follow approved layout.

Must preserve narrative sequence.
```

Approval Required

```text
Business Owner

UX Reviewer

Report Designer
```

---

# Output Artifact 04

# Technical Requirements Document (TRD)

File Name

```text
TRD_vX.X.md
```

Purpose

Define implementation requirements.

Generated only after:

```text
DSC Approved

Markdown Approved

SVG Approved
```

Contains

```text
Data Model

Measures

KPI Contracts

Visual Inventory

Interactions

Drillthroughs

Security

Refresh

Validation Rules

Deployment
```

---

# Deliverable Sequence

The skill must always generate outputs in this order.

```text
Output 1

Decision Story Contract (DSC)

↓↓↓

Output 2

Markdown Wireframe

↓↓↓

Output 3

SVG Wireframe

↓↓↓

Output 4

Technical Requirements Document (TRD)
```

Never skip an output.

Never generate SVG before DSC approval.

Never generate TRD before SVG approval.

---

# Success Criteria

The skill succeeds when:

✅ Decision is clear

✅ Business questions are mapped

✅ Signals are identified

✅ Thresholds exist

✅ Actions are defined

✅ Narrative story is approved

✅ SVG reflects the approved story

✅ TRD can be produced without redesign

✅ Users can answer:

```text
What should I do?
```

within 30 seconds of opening the report.

The final output must behave as a decision product rather than a reporting product.