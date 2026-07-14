# 10_MEASURE_CONTRACT_TEMPLATE_v1.0
## Measure Governance Contract

---

# Document Metadata

Document Type

```text
Measure Contract
```

Version

```text
[Version]
```

Capability Name

```text
[Capability Name]
```

Artifact Type

```text
MEASURE_CONTRACT
```

Owner

```text
[Owner]
```

Status

```text
Draft
```

Purpose

Define the business, semantic, and calculation governance rules for all measures within the semantic model.

This document serves as the bridge between:

```text
Semantic Model Design

↓

Business Calculations

↓

Power BI Measures

↓

Decision Support
```

The Measure Contract prevents:

```text
Metric Disputes

Duplicate Logic

Inconsistent Calculations

Threshold Confusion

Decision Misalignment
```

---

# Related Artifacts

```text
INPUT_BRD_vX.X.md

REPORT_STORY_MATRIX_vX.X.md

REPORT_STORY_vX.X.md

TRD_vX.X.md

DATA_MODEL_MATRIX_vX.X.md

SEMANTIC_MODEL_SPEC_vX.X.md

DATA_MODEL_STANDARDS_v1.0.md
```

---

# MEASURE GOVERNANCE PHILOSOPHY

## Core Principle

Every measure must support:

```text
A Signal

↓

A Business Question

↓

A Decision

↓

An Action
```

---

## Measure Hierarchy

Preferred design:

```text
Base Measure

↓

Derived Measure

↓

Presentation Measure
```

---

## Measure Success Criteria

Every measure should answer:

```text
Why does this measure exist?

Which decision does it support?

Which action does it drive?
```

---

# SECTION 01 — MEASURE INVENTORY

| Measure Name | Type | Decision Supported | Status |
|-------------|-------------|-------------|-------------|
| [Measure] | Base | [Decision] | Draft |
| [Measure] | Derived | [Decision] | Draft |
| [Measure] | Presentation | [Decision] | Draft |

---

# SECTION 02 — DECISION TRACEABILITY

## Measure

### Measure Name

```text
[Measure Name]
```

---

### Business Question

```text
[Question]
```

---

### Signal Supported

```text
[Signal]
```

---

### Decision Supported

```text
[Decision]
```

---

### Action Supported

```text
[Action]
```

---

Repeat for every measure.

---

# SECTION 03 — BASE MEASURE DEFINITIONS

## Measure

### Measure Name

```text
[Measure Name]
```

---

### Measure Classification

```text
Base Measure
```

---

### Business Definition

```text
[Definition]
```

---

### Business Purpose

```text
[Purpose]
```

---

### Source Fact

```text
[Fact Table]
```

---

### Source Column(s)

```text
[List]
```

---

### Aggregation Type

```text
SUM

COUNT

DISTINCTCOUNT

MIN

MAX

AVERAGE
```

---

### Business Rule

```text
[Rule]
```

---

### Notes

```text
[List]
```

---

Repeat for every base measure.

---

# SECTION 04 — DERIVED MEASURE DEFINITIONS

## Measure

### Measure Name

```text
[Measure Name]
```

---

### Measure Classification

```text
Derived Measure
```

---

### Business Definition

```text
[Definition]
```

---

### Business Purpose

```text
[Purpose]
```

---

### Dependent Measures

```text
[List]
```

---

### Calculation Logic

```text
Business Formula

(No DAX)
```

Example:

```text
Remaining Capacity

=

Care Capacity

-

Animals In Care
```

---

### Business Rule

```text
[Rule]
```

---

### Notes

```text
[List]
```

---

Repeat for every derived measure.

---

# SECTION 05 — PRESENTATION MEASURE DEFINITIONS

## Measure

### Measure Name

```text
[Measure Name]
```

---

### Measure Classification

```text
Presentation Measure
```

---

### Business Definition

```text
[Definition]
```

---

### Business Purpose

```text
[Purpose]
```

---

### Parent Measure

```text
[Measure]
```

---

### Presentation Logic

```text
Formatting

Icons

Status Labels

Threshold Labels

Display Variants
```

---

### Example

```text
Capacity Status

Healthy

Monitor

Critical
```

---

Repeat for every presentation measure.

---

# SECTION 06 — THRESHOLD CONTRACTS

## Threshold Measure

### Measure Name

```text
[Measure Name]
```

---

### Green Threshold

```text
[Rule]
```

---

### Yellow Threshold

```text
[Rule]
```

---

### Red Threshold

```text
[Rule]
```

---

### Business Interpretation

```text
What each threshold means.
```

---

### Action Required

```text
Healthy

↓

Monitor

↓

Investigate

↓

Act
```

---

Repeat as required.

---

# SECTION 07 — DECISION ACTION CONTRACTS

## Measure

### Measure Name

```text
[Measure Name]
```

---

### Measure Result

```text
[Condition]
```

---

### Business Interpretation

```text
[Interpretation]
```

---

### Recommended Action

```text
[Action]
```

---

### Escalation Required

```text
Yes / No
```

---

Repeat as required.

---

# SECTION 08 — FORMATTING CONTRACTS

## Measure

### Measure Name

```text
[Measure Name]
```

---

### Data Type

```text
Whole Number

Decimal

Percentage

Currency

Duration
```

---

### Format String

```text
#,0

#,0.00

0.0%

$#,0
```

---

### Decimal Precision

```text
[Precision]
```

---

### Display Rules

```text
Thousands Separator

Percentage Format

Units

Abbreviations
```

---

Repeat as required.

---

# SECTION 09 — VISUAL MAPPING

## Measure

### Measure Name

```text
[Measure Name]
```

---

### Visuals Used

```text
[List]
```

---

### Report Sections

```text
[List]
```

---

### Dashboard Usage

```text
[List]
```

---

### Story Usage

```text
[List]
```

---

Repeat for every measure.

---

# SECTION 10 — FACT MAPPING

## Measure

### Measure Name

```text
[Measure Name]
```

---

### Source Fact

```text
[Fact]
```

---

### Source Columns

```text
[List]
```

---

### Grain Alignment

```text
Confirmed

Not Confirmed
```

---

### Validation Notes

```text
[List]
```

---

Repeat for every measure.

---

# SECTION 11 — DEPENDENCY MAPPING

## Measure

### Measure Name

```text
[Measure]
```

---

### Depends On

```text
Base Measures

Dimensions

Attributes
```

---

### Dependency Type

```text
Direct

Indirect
```

---

Repeat as required.

---

# SECTION 12 — BUSINESS OWNERSHIP

## Measure

### Measure Name

```text
[Measure]
```

---

### Business Owner

```text
[Owner]
```

---

### Data Owner

```text
[Owner]
```

---

### Review Frequency

```text
Monthly

Quarterly

Annually
```

---

Repeat for every measure.

---

# SECTION 13 — AI READINESS

## Measure Documentation Review

Verify:

```text
□ Business Definition Exists

□ Signal Identified

□ Decision Identified

□ Business Owner Assigned

□ Action Defined
```

---

## AI Readiness Goal

An AI agent should explain:

```text
What the measure means.

Why it exists.

How it is calculated.

Which decision it supports.

Which action it drives.
```

without external documentation.

---

# SECTION 14 — MEASURE VALIDATION

## Validation Matrix

| Measure | Logic Reviewed | Threshold Reviewed | Owner Approved | Status |
|----------|----------|----------|----------|----------|
| [Measure] | Yes/No | Yes/No | Yes/No | Draft |
| [Measure] | Yes/No | Yes/No | Yes/No | Draft |

---

## Validation Rules

Verify:

```text
□ Business Definition Exists

□ Measure Supports Signal

□ Measure Supports Decision

□ Measure Supports Action

□ Threshold Defined

□ Formatting Defined

□ Fact Mapping Confirmed

□ Visual Mapping Confirmed
```

---

# SECTION 15 — HANDOFF TO BUILD PHASE

## Required Approvers

```text
Business Owner

Data Architect

BI Architect

Analytics Lead
```

---

## Approval Status

```text
Draft

Review

Approved
```

---

## Next Artifact

```text
Semantic Build Agent
```

---

## Purpose

```text
Translate Measure Contracts

↓

DAX Measures

↓

Semantic Model Implementation
```

---

# SECTION 16 — OBSERVATIONS

## Assumptions

```text
[List]
```

---

## Constraints

```text
[List]
```

---

## Risks

```text
[List]
```

---

## Special Considerations

```text
[List]
```

---

# SUCCESS STATEMENT

The Measure Contract succeeds when:

```text
Every Measure

has a Business Definition.

Every Measure

supports a Signal.

Every Signal

supports a Decision.

Every Decision

supports an Action.

Every Threshold

is documented.

Every Calculation

is governed.
```

The Measure Contract becomes:

```text
The Metric Governance Contract
```

between:

```text
Business Design

↓

Semantic Design

↓

Report Development

↓

Decision Support
```