# REPORT_STORY_MATRIX_v1.0
## Animal Flow — Live Capacity Reporting
### Decision Story Matrix

---

# Document Metadata

Document Type

Decision Story Matrix

Version

1.0

Capability

Animal Flow — Live Capacity Reporting

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

Which centres currently have sufficient capacity to support incoming animals?

---

## Secondary Decisions

- Which centres require operational intervention?
- Which centres should be prioritized for intake?
- Which centres should be avoided for intake?
- Which centres have data quality concerns?
- Which regions are experiencing capacity pressure?

---

## Decision Owner

Animal Flow Team

---

## Decision Frequency

Multiple Times Daily

---

## Key Discovery

The placement decision is driven by:

```text
DOG Capacity
+
CAT Capacity
+
DOG Utilization
+
CAT Utilization
+
Emergency Closure Status
+
Data Quality
+
Capacity Confirmation
```

NOT merely:

```text
Open Spaces
```

---

## Governing Business Rule

A centre may have open physical space while still being unsuitable for intake due to operational capacity, emergency closures, stale updates, or data quality concerns.

---

## Decision Success Criteria

Users must be able to answer:

```text
Which centres can safely receive incoming animals?
```

within:

```text
30 Seconds
```

---

# STEP 02 — BUSINESS QUESTION MATRIX

| Business Question | Decision Category | Priority |
|-------------------|------------------|----------|
| Which centres currently have available DOG capacity? | Placement | Critical |
| Which centres currently have available CAT capacity? | Placement | Critical |
| Which centres are approaching critical utilization? | Capacity Risk | High |
| Which centres have no available capacity? | Capacity Risk | High |
| Which centres have emergency closures? | Placement Eligibility | High |
| Which centres have animals missing kennel assignments? | Data Trust | High |
| Which centres have stale capacity updates? | Data Trust | High |
| Which centres have not confirmed capacity status? | Governance | High |
| Which centres require intervention? | Operations | High |
| Which centres should be prioritized for intake decisions? | Placement | Critical |
| Which regions have the highest utilization? | Regional Monitoring | Medium |

---

# STEP 03 — SIGNAL MATRIX

## Placement Signals

- Total DOG Spaces
- Open DOG Spaces
- Total CAT Spaces
- Open CAT Spaces
- DOG Utilization %
- CAT Utilization %
- Emergency Closure Status

Supported Decision

```text
Which centres can safely receive incoming animals?
```

---

## Data Quality Signals

- Missing Kennel Assignments
- Assignment Accuracy %
- Capacity Confirmation Status
- Last Capacity Update
- ShelterBuddy Last Sync

Supported Decision

```text
Can the information be trusted?
```

---

## Operational Signals

- DOG Utilization %
- CAT Utilization %
- Emergency Closure Status
- Capacity Confirmation Status

Supported Decision

```text
Which centres require intervention?
```

---

## Regional Signals

- Regional DOG Utilization %
- Regional CAT Utilization %
- Regional Open Capacity %
- Regional Capacity Availability

Supported Decision

```text
Which regions are experiencing pressure?
```

---

# STEP 04 — ACTION MATRIX

## DOG Utilization %

| Threshold | Status | Action |
|------------|------------|------------|
| <80% | Healthy | Candidate Centre |
| 80%-99% | Monitor | Review Before Routing |
| >=100% | Full | Do Not Intake |

Supported Decision

```text
Can this centre receive additional DOG intake?
```

---

## CAT Utilization %

| Threshold | Status | Action |
|------------|------------|------------|
| <80% | Healthy | Candidate Centre |
| 80%-99% | Monitor | Review Before Routing |
| >=100% | Full | Do Not Intake |

Supported Decision

```text
Can this centre receive additional CAT intake?
```

---

## Missing Kennel Assignments

| Threshold | Status | Action |
|------------|------------|------------|
| 0 | Healthy | No Action |
| 1-3 | Warning | Review |
| >3 | Critical | Data Cleanup Required |

Supported Decision

```text
Can capacity information be trusted?
```

---

## Capacity Confirmation Age

| Threshold | Status | Action |
|------------|------------|------------|
| <12 Hours | Current | Use Normally |
| 12-24 Hours | Aging | Validate |
| >24 Hours | Stale | Contact Centre |

Supported Decision

```text
Should this centre be reviewed before placement?
```

---

## Emergency Closure Status

| Status | Action |
|------------|------------|
| Active | Exclude Centre |
| Inactive | Normal Operations |

Supported Decision

```text
Is the centre eligible for intake?
```

---

# STEP 05 — REPORT STORY

## Question 1

What is happening across the province today?

Output

```text
Provincial Capacity Snapshot
```

Audience

```text
Animal Flow
Leadership
```

Action

```text
Understand overall operating conditions.
```

---

## Question 2

What requires immediate attention?

Output

```text
Action Required
```

Audience

```text
Animal Flow
```

Action

```text
Identify urgent risks and issues.
```

---

## Question 3

Which centres can receive incoming animals?

Output

```text
Intake Readiness
```

Audience

```text
Animal Flow
```

Action

```text
Identify intake candidates.
```

---

## Question 4

Which centres should be prioritized?

Output

```text
Placement Decision Board
```

Audience

```text
Animal Flow
```

Action

```text
Select preferred placement locations.
```

---

## Question 5

Why are centres constrained?

Output

```text
Capacity Analysis
```

Audience

```text
Animal Flow
```

Action

```text
Understand operational constraints.
```

---

## Question 6

Can the information be trusted?

Output

```text
Data Trust
```

Audience

```text
Animal Flow
```

Action

```text
Validate confidence before acting.
```

---

## Question 7

Where is regional pressure building?

Output

```text
Regional Health
```

Audience

```text
Animal Flow
Leadership
```

Action

```text
Monitor regional capacity trends.
```

---

## Question 8

What should we do next?

Output

```text
Operational Briefing
```

Audience

```text
Animal Flow
```

Action

```text
Execute recommended actions.
```

---

# STEP 06 — PAGE ARCHETYPE

Primary Archetype

```text
Operational Command Centre
```

---

Secondary Archetype

```text
Capacity Intelligence
```

---

Supporting Archetype

```text
Exception Management
```

---

# STEP 07 — LAYOUT BLUEPRINT

```text
Provincial Capacity Snapshot

↓

Action Required

↓

Intake Readiness

↓

Placement Decision Board

↓

Capacity Analysis

↓

Data Trust

↓

Regional Health

↓

Operational Briefing
```

---

# STEP 08 — VISUAL RECOMMENDATIONS

| Section | Visual | Reason |
|----------|----------|----------|
| Provincial Capacity Snapshot | KPI Cards | Provide operational context |
| Action Required | Exception KPI Cards | Highlight urgent issues |
| Intake Readiness | Status Cards | Quickly assess intake readiness |
| Placement Decision Board | Priority Table | Support ranking and placement |
| Capacity Analysis | Comparison Cards | Explain constraints |
| Data Trust | Exception Matrix | Assess confidence levels |
| Regional Health | Horizontal Bar Chart | Compare regional performance |
| Operational Briefing | Recommendation Cards | Convert findings into actions |

---

# APPROVAL CHECKPOINT

Decision Model

☐ Approved

Question Matrix

☐ Approved

Signal Matrix

☐ Approved

Action Matrix

☐ Approved

Report Story

☐ Approved

Page Archetype

☐ Approved

Layout Blueprint

☐ Approved

Visual Recommendations

☐ Approved

---

## Next Step

```text
Generate:

REPORT_STORY_v1.0.md

(Decision Story Contract)
```