# REPORT_DESIGN_STANDARDS_v1.0
## Decision-Driven BI Report Design Standards

---

# Document Metadata

Document Name

REPORT_DESIGN_STANDARDS

Version

1.0

Owner

Decision-Driven BI Framework

Status

Approved Standard

Purpose

Provide a governing framework for designing decision-driven reports, dashboards, scorecards, and operational command centres.

The standard ensures report design begins with business decisions and required actions rather than visuals, KPIs, or data structures.

---

# SECTION 01 — REPORT DESIGN PHILOSOPHY

## Core Principle

The purpose of a report is to support business decisions.

The purpose of a dashboard is not to display data.

The purpose of a dashboard is to help users take action.

---

## Traditional BI Approach

```text
Data
↓
Charts
↓
Dashboard
↓
User Figures Out What To Do
```

---

## Decision-Driven BI Approach

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
Layout
↓
Visual
```

---

## Success Definition

A report succeeds when users can answer:

```text
What should I do?
```

within 30 seconds of opening the report.

---

# SECTION 02 — DECISION-FIRST DESIGN

## Governing Rule

Every report must begin with a decision.

Never begin with:

```text
Data

Metrics

Charts

Visuals

Layouts
```

---

## Required Decision Declaration

Every report must identify:

```text
Primary Decision

Secondary Decisions

Decision Owner

Decision Frequency
```

---

## Example

Primary Decision

```text
Which centres can safely receive additional animals?
```

Secondary Decisions

```text
Which centres require intervention?

Which centres should be avoided?

Which centres should be prioritized?
```

---

## Validation Rule

If the primary decision cannot be clearly stated:

```text
STOP REPORT DESIGN
```

until the decision is defined.

---

# SECTION 03 — BUSINESS QUESTION DESIGN

## Purpose

Business questions bridge decisions and reporting requirements.

---

## Required Structure

Every question must support:

```text
Decision Category

Priority

Desired Action
```

---

## Example

Question

```text
Which centres currently have available CAT capacity?
```

Decision Category

```text
Placement
```

Priority

```text
High
```

---

## Validation Rule

Every question must support a decision.

If a question does not support a decision:

```text
Remove It
```

---

# SECTION 04 — SIGNAL DESIGN

## Signal Definition

A signal is measurable information used to answer a business question.

---

## Signal Hierarchy

```text
Decision
↓
Question
↓
Signal
```

---

## Signal Requirements

Every signal must:

```text
Support a Question

Support a Decision

Be Measurable

Be Explainable
```

---

## Example

Question

```text
Can this centre receive another animal?
```

Signals

```text
Animals In Care

Care Capacity

Remaining Capacity

Emergency Closure
```

---

## Validation Rule

If a signal cannot influence a decision:

```text
Remove It
```

---

# SECTION 05 — THRESHOLD DESIGN

## Purpose

Signals become useful only when thresholds create meaning.

---

## Threshold Structure

Every threshold requires:

```text
Threshold

Status

Action
```

---

## Example

Signal

```text
Capacity Utilization %
```

Threshold

```text
<80%
```

Status

```text
Healthy
```

Action

```text
Candidate Centre
```

---

## Threshold Validation

Every threshold must support:

```text
Action
```

If no action exists:

```text
Threshold Not Needed
```

---

# SECTION 06 — ACTION DESIGN

## Purpose

Every signal must lead to an operational action.

---

## Action Structure

```text
Condition

Recommended Action

Decision Supported
```

---

## Example

Condition

```text
Capacity >= 100%
```

Action

```text
Do Not Intake
```

Decision Supported

```text
Can this centre receive another animal?
```

---

## Action Validation

Every action must support:

```text
Human Decision

Human Response

Business Process
```

---

# SECTION 07 — KPI DESIGN

## KPI Purpose

KPIs are decision signals.

KPIs are not decorative metrics.

---

## KPI Qualification Test

Every KPI must answer:

```text
What action becomes easier because of this KPI?
```

---

## Valid KPI

```text
Remaining Capacity
```

Supports:

```text
Can This Centre Accept Animals?
```

---

## Invalid KPI

```text
Total Animals
```

if it supports no decision.

---

## KPI Structure

Every KPI must contain:

```text
Signal

Threshold

Status

Action

Decision
```

---

# SECTION 08 — REPORT STORY DESIGN

## Purpose

Reports tell a decision story.

---

## Story Sequence

Recommended structure:

```text
What Is Happening?

↓

What Requires Attention?

↓

What Decision Must Be Made?

↓

Why?

↓

Can The Information Be Trusted?

↓

What Action Should Be Taken?
```

---

## Story Validation

Each section must answer a business question.

---

## Story Progression Rule

Reports should move from:

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

# SECTION 09 — PAGE ARCHETYPE DESIGN

## Purpose

Every page should operate as a recognizable decision pattern.

---

## Approved Archetypes

```text
Operational Command Centre

Capacity Intelligence

Executive Monitoring

Exception Management

Regional Monitoring

Data Quality Investigation

Performance Monitoring
```

---

## Validation Rule

Every page must declare:

```text
Primary Archetype

Secondary Archetype
```

---

# SECTION 10 — LAYOUT DESIGN

## Purpose

Define report reading order.

---

## Reading Order Rule

Users should naturally progress through:

```text
Context

↓

Exceptions

↓

Decision Support

↓

Analysis

↓

Action
```

---

## Recommended Layout Pattern

```text
Operational Snapshot

↓

Action Required

↓

Decision Support

↓

Analysis

↓

Data Trust

↓

Recommendations
```

---

## Validation Rule

Layout must support report story sequence.

---

# SECTION 11 — VISUAL DESIGN

## Purpose

Visuals exist only to support decisions.

---

## Visual Selection Rule

Never choose visuals first.

Always choose:

```text
Decision

↓

Question

↓

Signal

↓

Visual
```

---

## Visual Mapping Examples

Question

```text
Which centres should be prioritized?
```

Visual

```text
Priority Table
```

Reason

```text
Supports operational ranking.
```

---

Question

```text
Where is pressure building?
```

Visual

```text
Regional Ranking
```

Reason

```text
Supports regional comparison.
```

---

## Visual Validation

Every visual must support:

```text
Decision

Question

Signal
```

---

# SECTION 12 — SVG DESIGN STANDARDS

## Purpose

SVG is a rendering artifact.

---

## SVG May

```text
Render Approved Layout

Render Approved Sections

Render Approved KPI Placement

Render Approved Visuals
```

---

## SVG May Not

```text
Create New KPI

Create New Measures

Create New Signals

Create New Decisions

Create New Layout Sections
```

---

## Render Rule

SVG must exactly reflect:

```text
Approved DSC

Approved Mockup
```

---

# SECTION 13 — DECISION STORY CONTRACT (DSC)

## Purpose

The DSC is the governing report design document.

---

## DSC Required Sections

```text
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

---

## Approval Requirements

```text
Business Owner

Product Owner

Report Designer
```

---

# SECTION 14 — REPORT QUALITY CHECKLIST

Before approval, verify:

```text
□ Primary Decision Identified

□ Secondary Decisions Identified

□ Questions Defined

□ Signals Defined

□ Thresholds Defined

□ Actions Defined

□ Story Approved

□ Archetype Selected

□ Layout Approved

□ Visuals Approved

□ SVG Matches Story

□ Users Can Take Action
```

---

# FINAL REPORT VALIDATION

Every report must satisfy:

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
Layout
↓
Visual
```

Nothing should enter the report unless it can be traced back through this chain.

---

# STANDARD SUCCESS STATEMENT

A report succeeds when:

```text
Every Visual
supports a Signal

Every Signal
supports a Question

Every Question
supports a Decision

Every Decision
supports Business Action
```

The report therefore becomes a:

```text
Decision Product
```

rather than a:

```text
Reporting Product
```