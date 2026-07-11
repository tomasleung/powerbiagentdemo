# 01_REPORT_STORY_MATRIX_TEMPLATE_v1.0
## [Capability Name]
### Decision Story Matrix

---

# Document Metadata

Document Type

Decision Story Matrix

Version

[Version]

Capability

[Capability Name]

Purpose

Provide a fast-review decision framework before generating the full Decision Story Contract (DSC).

Audience

- Product Owner
- Business Owner
- Report Designer
- BI Developer

Approval Gate

This artifact must be approved before creating the full DSC.

---

# STEP 01 — DECISION MODEL

## Primary Decision

[Primary Decision]

---

## Secondary Decisions

- [Secondary Decision 01]
- [Secondary Decision 02]
- [Secondary Decision 03]
- [Secondary Decision 04]
- [Secondary Decision 05]

---

## Decision Owner

[Decision Owner]

---

## Decision Frequency

[Decision Frequency]

Examples

```text
Real Time

Hourly

Daily

Weekly

Monthly

Quarterly
```

---

## Key Discovery

Describe the most important business insight discovered during requirements gathering.

Example

```text
The business currently evaluates capacity using physical space.

The actual decision requires:

Care Capacity
+
Occupancy
+
Availability
+
Data Trust

rather than physical space alone.
```

---

## Governing Business Rule

Document the controlling rule that drives the decision.

Example

```text
A centre may have available space while still being unable to receive additional animals because care capacity has been reached.
```

---

## Decision Success Criteria

Users must be able to answer:

```text
[Decision Outcome]
```

within:

```text
[Time Requirement]
```

Example

```text
30 Seconds
```

---

# STEP 02 — BUSINESS QUESTION MATRIX

| Business Question | Decision Category | Priority |
|-------------------|------------------|----------|
| [Question] | [Category] | [Priority] |
| [Question] | [Category] | [Priority] |
| [Question] | [Category] | [Priority] |
| [Question] | [Category] | [Priority] |

---

## Decision Categories

Examples

```text
Placement

Operations

Risk

Monitoring

Capacity

Compliance

Finance

Sales

Customer

Regional Monitoring

Data Quality

Executive Oversight
```

---

## Priority Levels

```text
Critical

High

Medium

Low
```

---

# STEP 03 — SIGNAL MATRIX

## Signal Group Name

Signals

- [Signal]
- [Signal]
- [Signal]
- [Signal]

Supported Decision

```text
[Decision Supported]
```

---

## Signal Group Name

Signals

- [Signal]
- [Signal]
- [Signal]
- [Signal]

Supported Decision

```text
[Decision Supported]
```

---

## Signal Group Name

Signals

- [Signal]
- [Signal]
- [Signal]
- [Signal]

Supported Decision

```text
[Decision Supported]
```

---

## Signal Validation

Every signal must:

```text
Support A Question

Support A Decision

Be Measurable

Be Actionable
```

---

# STEP 04 — ACTION MATRIX

## Signal Name

| Threshold | Status | Action |
|------------|------------|------------|
| [Threshold] | [Status] | [Action] |
| [Threshold] | [Status] | [Action] |
| [Threshold] | [Status] | [Action] |

Supported Decision

```text
[Decision Supported]
```

---

## Signal Name

| Threshold | Status | Action |
|------------|------------|------------|
| [Threshold] | [Status] | [Action] |
| [Threshold] | [Status] | [Action] |
| [Threshold] | [Status] | [Action] |

Supported Decision

```text
[Decision Supported]
```

---

## Signal Name

| Threshold | Status | Action |
|------------|------------|------------|
| [Threshold] | [Status] | [Action] |
| [Threshold] | [Status] | [Action] |
| [Threshold] | [Status] | [Action] |

Supported Decision

```text
[Decision Supported]
```

---

## Action Validation

Every threshold must produce:

```text
Status

Action

Decision Outcome
```

---

# STEP 05 — REPORT STORY

## Question 01

[Business Question]

Output

```text
[Output Section]
```

Audience

```text
[Audience]
```

Action

```text
[Intended Action]
```

---

## Question 02

[Business Question]

Output

```text
[Output Section]
```

Audience

```text
[Audience]
```

Action

```text
[Intended Action]
```

---

## Question 03

[Business Question]

Output

```text
[Output Section]
```

Audience

```text
[Audience]
```

Action

```text
[Intended Action]
```

---

## Question 04

[Business Question]

Output

```text
[Output Section]
```

Audience

```text
[Audience]
```

Action

```text
[Intended Action]
```

---

## Question 05

[Business Question]

Output

```text
[Output Section]
```

Audience

```text
[Audience]
```

Action

```text
[Intended Action]
```

---

## Story Validation

The report story should flow from:

```text
Context

↓

Attention Required

↓

Decision Support

↓

Explanation

↓

Trust

↓

Recommended Action
```

---

# STEP 06 — PAGE ARCHETYPE

## Primary Archetype

```text
[Primary Archetype]
```

---

## Secondary Archetype

```text
[Secondary Archetype]
```

---

## Supporting Archetype

```text
[Supporting Archetype]
```

---

## Approved Archetypes

```text
Operational Command Centre

Executive Monitoring

Capacity Intelligence

Exception Management

Regional Monitoring

Data Quality Investigation

Performance Monitoring
```

---

# STEP 07 — LAYOUT BLUEPRINT

```text
[Section 01]

↓

[Section 02]

↓

[Section 03]

↓

[Section 04]

↓

[Section 05]

↓

[Section 06]

↓

[Section 07]

↓

[Section 08]

↓

[Section 09]
```

---

## Layout Purpose

The reading order must support:

```text
Context

↓

Analysis

↓

Decision

↓

Action
```

---

# STEP 08 — VISUAL RECOMMENDATIONS

| Section | Visual | Reason |
|----------|----------|----------|
| [Section] | [Visual] | [Reason] |
| [Section] | [Visual] | [Reason] |
| [Section] | [Visual] | [Reason] |
| [Section] | [Visual] | [Reason] |
| [Section] | [Visual] | [Reason] |

---

## Approved Visual Types

```text
KPI Cards

Status Cards

Exception Cards

Priority Table

Comparison Matrix

Breakdown Chart

Horizontal Bar Chart

Ranking Table

Exception Matrix

Recommendation Cards

Narrative Summary
```

---

## Visual Validation

Every visual must support:

```text
Business Question

Signal

Decision

Action
```

---

# APPROVAL CHECKPOINT

Decision Model

☐ Approved

---

Question Matrix

☐ Approved

---

Signal Matrix

☐ Approved

---

Action Matrix

☐ Approved

---

Report Story

☐ Approved

---

Page Archetype

☐ Approved

---

Layout Blueprint

☐ Approved

---

Visual Recommendations

☐ Approved

---

# MATRIX SUCCESS STATEMENT

The Decision Story Matrix succeeds when:

```text
Every Question
supports a Decision

Every Signal
supports a Question

Every Action
supports a Decision

Every Story Section
supports a User Action
```

and stakeholders agree the decision logic is complete before generating the full Decision Story Contract.

---

## Next Step

```text
Generate:

REPORT_STORY_v1.0.md

(Decision Story Contract)
```