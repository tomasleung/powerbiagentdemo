# REPORT_STORY_v1.0.md
## Animal Flow — Live Capacity Reporting
### Decision Story Contract (DSC)

---

# Document Metadata

Document Type

Decision Story Contract

Version

1.0

Capability Name

Animal Flow — Live Capacity Reporting

Artifact Type

DSC

Owner

Animal Flow

Status

Draft

Purpose

Convert approved business requirements into a decision-driven report narrative, page structure, layout blueprint, and visual design contract before technical design begins.

Related Documents

```text
INPUT_BRD_AnimalFlow_LiveCapacity_v2.0

REPORT_STORY_MATRIX_v1.0
```

---

# SECTION 01 — DECISION MODEL

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

## Governing Business Rule

Animal placement decisions must not rely solely on available space.

The governing placement decision is:

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
Capacity Confirmation Status
=
Placement Readiness
```

---

## Key Discovery

A centre may have:

```text
Available Physical Space
```

and still be:

```text
Unable To Receive Additional Animals
```

because:

```text
Capacity Threshold Has Been Reached

OR

Emergency Closure Is Active

OR

Data Cannot Be Trusted
```

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

# SECTION 02 — BUSINESS QUESTION MATRIX

## Placement Questions

| Question | Priority |
|----------|----------|
| Which centres currently have available DOG capacity? | Critical |
| Which centres currently have available CAT capacity? | Critical |
| Which centres should be prioritized for intake? | Critical |
| Which centres should be avoided for intake? | High |

---

## Capacity Questions

| Question | Priority |
|----------|----------|
| Which centres are approaching critical utilization? | High |
| Which centres have no available capacity? | High |
| Which centres have emergency closures? | High |

---

## Data Quality Questions

| Question | Priority |
|----------|----------|
| Which centres have missing kennel assignments? | High |
| Which centres have stale updates? | High |
| Which centres have not confirmed capacity status? | High |
| Which centres require data quality review? | High |

---

## Regional Questions

| Question | Priority |
|----------|----------|
| Which regions have the highest utilization? | Medium |
| Which regions are experiencing capacity pressure? | Medium |

---

# SECTION 03 — BUSINESS LOGIC MODEL

## Capacity Availability

Capacity availability is determined through:

```text
Available DOG Spaces

Available CAT Spaces

DOG Utilization %

CAT Utilization %
```

---

## Placement Eligibility

A centre is eligible when:

```text
Capacity Available

AND

Emergency Closure Inactive

AND

Capacity Information Current

AND

Data Quality Acceptable
```

---

## Data Trust

Data confidence is determined through:

```text
Missing Kennel Assignments

Assignment Accuracy %

Capacity Confirmation Status

Last Capacity Update

ShelterBuddy Synchronization Status
```

---

## Regional Monitoring

Regional pressure is evaluated using:

```text
Regional Utilization %

Regional Capacity %

Regional Open Capacity %
```

---

# SECTION 04 — SIGNAL MATRIX

## Provincial Snapshot Signals

```text
Total DOG Spaces

Open DOG Spaces

Total CAT Spaces

Open CAT Spaces

DOG Utilization %

CAT Utilization %
```

---

## Intake Readiness Signals

```text
Open DOG Spaces

Open CAT Spaces

DOG Utilization %

CAT Utilization %

Emergency Closure Status
```

---

## Data Trust Signals

```text
Missing Kennel Assignments

Assignment Accuracy %

Capacity Confirmation Status

Last Capacity Update

ShelterBuddy Last Sync
```

---

## Operational Risk Signals

```text
DOG Utilization %

CAT Utilization %

Emergency Closure Status

Capacity Confirmation Status
```

---

## Regional Signals

```text
Regional DOG Utilization %

Regional CAT Utilization %

Regional Capacity %

Regional Open Capacity %
```

---

# SECTION 05 — THRESHOLD MATRIX

## DOG Utilization %

| Threshold | Status | Action |
|------------|------------|------------|
| <80% | Healthy | Candidate Centre |
| 80%-99% | Monitor | Review Before Routing |
| >=100% | Full | Do Not Intake |

---

## CAT Utilization %

| Threshold | Status | Action |
|------------|------------|------------|
| <80% | Healthy | Candidate Centre |
| 80%-99% | Monitor | Review Before Routing |
| >=100% | Full | Do Not Intake |

---

## Missing Kennel Assignments

| Threshold | Status | Action |
|------------|------------|------------|
| 0 | Healthy | No Action |
| 1-3 | Warning | Review |
| >3 | Critical | Data Cleanup Required |

---

## Capacity Confirmation Age

| Threshold | Status | Action |
|------------|------------|------------|
| <12 Hours | Current | Use Normally |
| 12-24 Hours | Aging | Validate |
| >24 Hours | Stale | Contact Centre |

---

## Emergency Closure

| Status | Action |
|------------|------------|
| Active | Exclude Centre |
| Inactive | Normal Operations |

---

# SECTION 06 — ACTION MATRIX

| Condition | Recommended Action |
|------------|------------|
| DOG Utilization >= 100% | Do Not Intake |
| CAT Utilization >= 100% | Do Not Intake |
| DOG/CAT Utilization 80%-99% | Review Before Routing |
| Missing Assignments > 3 | Data Quality Review |
| Capacity Update > 24 Hours | Contact Centre |
| Emergency Closure Active | Exclude Centre |
| Healthy Capacity + Available Space | Candidate Centre |

---

# SECTION 07 — NARRATIVE STORY

## Story Goal

Support Animal Flow in answering:

```text
Which centres currently have sufficient capacity to support incoming animals?
```

---

## Story 0

### Question

What is happening across the province today?

### Output

```text
Provincial Capacity Snapshot
```

### Audience

```text
Animal Flow
Leadership
```

### Action

```text
Understand overall operating conditions.
```

---

## Story 1

### Question

What requires immediate attention?

### Output

```text
Action Required
```

### Audience

```text
Animal Flow
```

### Action

```text
Identify urgent risks and operational issues.
```

---

## Story 2

### Question

Which centres can safely receive incoming animals?

### Output

```text
Intake Readiness
```

### Audience

```text
Animal Flow
```

### Action

```text
Identify placement candidates.
```

---

## Story 3

### Question

Which centres should be prioritized?

### Output

```text
Placement Decision Board
```

### Audience

```text
Animal Flow
```

### Action

```text
Select preferred placement locations.
```

---

## Story 4

### Question

Why can or cannot centres receive additional animals?

### Output

```text
Capacity Analysis
```

### Audience

```text
Animal Flow
```

### Action

```text
Understand operational constraints.
```

---

## Story 5

### Question

Can the information be trusted?

### Output

```text
Data Trust
```

### Audience

```text
Animal Flow
```

### Action

```text
Validate decision confidence.
```

---

## Story 6

### Question

Where is capacity pressure building?

### Output

```text
Regional Health
```

### Audience

```text
Animal Flow
Leadership
```

### Action

```text
Monitor regional operating conditions.
```

---

## Story 7

### Question

What should we do next?

### Output

```text
Operational Briefing
```

### Audience

```text
Animal Flow
```

### Action

```text
Execute recommended actions.
```

---

# SECTION 08 — PAGE ARCHETYPE

## Primary Archetype

```text
Operational Command Centre
```

---

## Secondary Archetype

```text
Capacity Intelligence
```

---

## Supporting Archetype

```text
Exception Management
```

---

# SECTION 09 — LAYOUT BLUEPRINT

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

# SECTION 10 — VISUAL RECOMMENDATIONS

## Provincial Capacity Snapshot

Visual

```text
Informational KPI Cards
```

Reason

```text
Provide provincial operating context.
```

---

## Action Required

Visual

```text
Exception KPI Cards
```

Reason

```text
Highlight urgent issues.
```

---

## Intake Readiness

Visual

```text
Status Cards
```

Reason

```text
Quickly identify eligible centres.
```

---

## Placement Decision Board

Visual

```text
Priority Table
```

Reason

```text
Support centre ranking and intake decisions.
```

---

## Capacity Analysis

Visual

```text
Comparison Cards
```

Reason

```text
Explain utilization and availability constraints.
```

---

## Data Trust

Visual

```text
Exception Matrix
```

Reason

```text
Assess confidence before acting.
```

---

## Regional Health

Visual

```text
Horizontal Bar Chart
```

Reason

```text
Compare regional performance.
```

---

## Operational Briefing

Visual

```text
Recommendation Cards
```

Reason

```text
Convert findings into action.
```

---

# SECTION 11 — MARKDOWN WIREFRAME REFERENCE

```text
Provincial Capacity Snapshot

Action Required

Intake Readiness

Placement Decision Board

Capacity Analysis

Data Trust

Regional Health

Operational Briefing
```

---

# SECTION 12 — SUCCESS CRITERIA

The solution succeeds when users can:

✅ Understand provincial capacity conditions

✅ Identify centres requiring intervention

✅ Identify candidate intake centres

✅ Understand capacity constraints

✅ Trust the operational data

✅ Monitor regional pressure

✅ Prioritize placement decisions

✅ Take action without manually reviewing every centre

---

## Report Validation

Users should be able to:

```text
Understand The Situation

Identify Risks

Validate Data Quality

Make A Placement Decision

Take Action
```

without manually interpreting raw operational data.

---

# APPROVAL GATE

Decision Model

☐ Approved

---

Business Questions

☐ Approved

---

Business Logic

☐ Approved

---

Signals

☐ Approved

---

Thresholds

☐ Approved

---

Actions

☐ Approved

---

Narrative Story

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

# DSC SUCCESS STATEMENT

A Decision Story Contract succeeds when:

```text
Every Story Section
supports a Business Question

Every Business Question
supports a Decision

Every Signal
supports a Question

Every Visual
supports a Signal

Every Action
supports a Decision
```

The DSC becomes the governing design contract for:

```text
Mockup Agent

TRD Agent

Semantic Design Agent

Future Report Build Agent
```

---

## Next Step

```text
Generate:

MOCKUP_v1.0.md

(Markdown Wireframe)
```