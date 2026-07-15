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

Define the business meaning, calculation governance, threshold logic, decision support, ownership, dependencies, formatting standards, and behavioral expectations for all measures within the semantic model.

This document serves as the bridge between:

```text
Business Decisions

↓

Signals

↓

Measures

↓

Semantic Model

↓

Power BI / Fabric Implementation
```

The Measure Contract prevents:

```text
Metric Disputes

Duplicate Business Logic

Ambiguous Calculations

Threshold Confusion

Inconsistent Reporting

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
Decision

↓

Business Question

↓

Signal

↓

Measure

↓

Action
```

---

## Measure Hierarchy

Preferred structure:

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

Which signal does it support?

Which decision does it support?

What action does it drive?
```

---

# SECTION 01 — MEASURE INVENTORY

| Measure Name | Classification | Signal Supported | Decision Supported | Status |
|-------------|-------------|-------------|-------------|-------------|
| [Measure] | Base | [Signal] | [Decision] | Draft |
| [Measure] | Derived | [Signal] | [Decision] | Draft |
| [Measure] | Presentation | [Signal] | [Decision] | Draft |

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

### Traceability Path

```text
Decision

↓

Question

↓

Signal

↓

Measure

↓

Action
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

### Classification

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

### Source Columns

```text
[List]
```

---

### Aggregation Type

```text
SUM

COUNT

DISTINCTCOUNT

AVERAGE

MIN

MAX
```

---

### Business Logic

```text
Business Aggregation Logic

(No DAX)
```

---

### Dependencies

```text
Fact_Table.Column
```

---

### Decision Supported

```text
[Decision]
```

---

### Notes

```text
[List]
```

---

Repeat for each base measure.

---

# SECTION 04 — DERIVED MEASURE DEFINITIONS

## Measure

### Measure Name

```text
[Measure Name]
```

---

### Classification

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

### Business Formula

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

### Dependencies

```text
Base Measures

Fact Tables

Dimensions
```

---

### Decision Supported

```text
[Decision]
```

---

### Notes

```text
[List]
```

---

Repeat for each derived measure.

---

# SECTION 05 — PRESENTATION MEASURE DEFINITIONS

## Measure

### Measure Name

```text
[Measure Name]
```

---

### Classification

```text
Presentation Measure
```

---

### Business Definition

```text
[Definition]
```

---

### Parent Measure

```text
[Measure]
```

---

### Presentation Logic

```text
Status Labels

Icons

RAG Logic

Display Variants

Formatted Output
```

---

### Example

```text
Capacity Health

Healthy

Monitor

Critical
```

---

### Decision Supported

```text
[Decision]
```

---

Repeat for every presentation measure.

---

# SECTION 06 — THRESHOLD CONTRACTS

## Measure

### Measure Name

```text
[Measure Name]
```

---

### Green Threshold

```text
[Condition]
```

---

### Amber Threshold

```text
[Condition]
```

---

### Red Threshold

```text
[Condition]
```

---

### Business Interpretation

```text
What each threshold means.
```

---

### Business Action

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

### Escalation Required

```text
Yes / No
```

---

Repeat for every threshold-driven measure.

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
[Meaning]
```

---

### Recommended Action

```text
[Action]
```

---

### Escalation Path

```text
[List]
```

---

Repeat for every decision-support measure.

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

Conditional Formatting

Display Units
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
[Fact Name]
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
[Measure Name]
```

---

### Dependencies

```text
Fact Tables

Base Measures

Derived Measures

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

### Dependency Diagram

```text
Base Measure

↓

Derived Measure

↓

Presentation Measure
```

---

Repeat for every measure.

---

# SECTION 12 — BUSINESS OWNERSHIP

## Measure

### Measure Name

```text
[Measure Name]
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

### Approval Status

```text
Draft

Approved

Retired
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

□ Action Defined

□ Business Owner Assigned

□ Dependencies Documented
```

---

## AI Summary

### Measure Name

```text
[Measure Name]
```

---

### One Sentence Explanation

```text
Explain the measure in business language.
```

Example:

```text
Remaining Capacity represents
the number of available care spaces
after current occupancy is considered.
```

---

Repeat for every measure.

---

# SECTION 14 — MEASURE VALIDATION

## Validation Matrix

| Measure | Logic Reviewed | Threshold Reviewed | Fact Mapping Verified | Owner Approved | Status |
|----------|----------|----------|----------|----------|----------|
| [Measure] | Yes/No | Yes/No | Yes/No | Yes/No | Draft |

---

## Validation Rules

Verify:

```text
□ Business Definition Exists

□ Signal Supported

□ Decision Supported

□ Action Defined

□ Dependencies Documented

□ Threshold Defined

□ Formatting Defined

□ Fact Mapping Confirmed

□ Visual Mapping Confirmed

□ Ownership Assigned
```

---

# SECTION 15 — GOVERNANCE REVIEW

## Governance Checklist

```text
□ No Duplicate Measures

□ Business Names Approved

□ Thresholds Approved

□ Decision Mapping Complete

□ Dependencies Reviewed

□ Ownership Assigned

□ Documentation Complete
```

---

## Governance Notes

```text
[List]
```

---

# SECTION 16 — HANDOFF TO BUILD PHASE

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

## Implementation Purpose

```text
Translate Business Logic

↓

DAX Measures

↓

Fabric Semantic Model

↓

Power BI Implementation
```

---

# SECTION 17 — OBSERVATIONS

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

Every Measure

has a documented dependency.

Every Threshold

is governed.

Every Calculation

is approved.

Every Business Owner

accepts accountability.
```

The Measure Contract becomes:

```text
The Measure Governance Contract
```

between:

```text
Business Design

↓

Semantic Design

↓

Semantic Build

↓

Report Development

↓

Decision Support
```