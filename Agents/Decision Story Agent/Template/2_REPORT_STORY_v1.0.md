# REPORT_STORY_v1.0.md
## Animal Flow — Capacity Intelligence
### Decision Story Contract (DSC)

---

# Document Metadata

Document Type: Decision Story Contract

Version: 1.0

Capability Name: Animal Flow — Capacity Intelligence

Artifact Type: DSC

Owner: Animal Flow

Status: Draft

Purpose:

Convert approved business requirements into a decision-driven report narrative, page structure, layout blueprint, and visual design contract before technical design begins.

Related Documents:

```text
BRD_AnimalFlow_Capacity_Intelligence_v1.0

REPORT_STORY_MATRIX_v1.0
```

---

# SECTION 01 — DECISION MODEL

## Primary Decision

Which centres can safely receive additional animals?

---

## Secondary Decisions

- Which centres require intervention?
- Which centres should be avoided for intake?
- Which centres require data quality review?
- Which regions require monitoring?
- Which centres should be prioritized for placement?

---

## Decision Owner

Animal Flow

---

## Decision Frequency

Multiple Times Per Day

---

## Governing Business Rule

Animal intake decisions must not be based solely on open physical space.

The governing intake decision is:

```text
Care Capacity
+
Animals In Care
+
Species Occupancy
+
Physical Space Availability
+
Data Trust
+
Emergency Closure Status
=
Intake Readiness
```

---

## Key Discovery

A centre may have:

```text
Open Space Available
```

and still be:

```text
Unable To Receive Additional Animals
```

because:

```text
Care Capacity Has Been Reached
```

---

# SECTION 02 — BUSINESS QUESTION MATRIX

## Placement Questions

| Question | Priority |
|----------|----------|
| Which centres currently have available CAT capacity? | High |
| Which centres currently have available DOG capacity? | High |
| Which centres should be prioritized for intake? | Critical |
| Which centres should be avoided? | High |

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
| Which centres have missing assignments? | High |
| Which centres have stale updates? | Medium |
| Which centres require review? | High |

---

## Species Occupancy Questions

| Question | Priority |
|----------|----------|
| How much CAT capacity is occupied by non-cat species? | Medium |
| How much DOG capacity is occupied by non-dog species? | Medium |
| Which centres are impacted by species occupancy? | Medium |

---

## Regional Questions

| Question | Priority |
|----------|----------|
| Which regions have the highest utilization? | Medium |
| Where is capacity pressure building? | Medium |

---

# SECTION 03 — BUSINESS LOGIC MODEL

## Capacity Concepts

The dashboard contains two capacity concepts:

### Physical Capacity

Represents floor plan availability.

Examples:

```text
Total Spaces

Open Spaces

In Use

Hold

Unavailable
```

---

### Care Capacity

Represents the maximum number of animals the centre can support operationally.

Examples:

```text
Staffing

Operational Load

Animal Care Requirements

Centre Operating Limits
```

---

## Species Occupancy Rule

A centre may temporarily house non-target species in CAT or DOG spaces.

Examples:

```text
Rabbit occupying CAT space

Guinea Pig occupying CAT space

Small Animal occupying CAT space

Other Animal occupying DOG space
```

These situations reduce intake flexibility and must be surfaced in the dashboard.

---

# SECTION 04 — SIGNAL MATRIX

## Operational Snapshot Signals

```text
Total Centres

Animals In Care

Care Capacity

Open Spaces

CAT Spaces

DOG Spaces
```

---

## Intake Readiness Signals

```text
Animals In Care

Care Capacity

Care Capacity %

Remaining Capacity

Open Space Count

Emergency Closure
```

---

## Physical Capacity Signals

```text
Total Spaces

Open Spaces

In Use

Hold

Unavailable
```

---

## Species Occupancy Signals

```text
Cats In Care

Dogs In Care

Other Animals

CAT Spaces Occupied By Other Animals

DOG Spaces Occupied By Other Animals

Species Occupancy Impact
```

---

## Data Trust Signals

```text
Missing Assignments

Confirmation Status

Last Update Time

Assignment Accuracy %

ShelterBuddy Synchronization Status
```

---

## Regional Signals

```text
Regional Utilization %

Regional Capacity %

Regional Open Space %
```

---

# SECTION 05 — THRESHOLD MATRIX

## Care Capacity %

| Threshold | Status | Action |
|------------|------------|------------|
| <80% | Healthy | Candidate Centre |
| 80%-99% | Monitor | Review Before Routing |
| >=100% | Full | Do Not Intake |

---

## Missing Assignments

| Threshold | Status | Action |
|------------|------------|------------|
| 0 | Healthy | No Action |
| 1-3 | Warning | Review |
| >3 | Critical | Data Cleanup Required |

---

## Capacity Confirmation

| Threshold | Status | Action |
|------------|------------|------------|
| <12 Hours | Current | Use Normally |
| 12-24 Hours | Aging | Validate |
| >24 Hours | Stale | Contact Centre |

---

## Species Occupancy Impact

| Threshold | Status | Action |
|------------|------------|------------|
| 0 | Normal | No Action |
| 1-3 | Monitor | Review Occupancy |
| >3 | Significant | Assess Alternate Housing |

---

## Emergency Closure

| Status | Action |
|----------|----------|
| Active | Exclude Centre |
| Inactive | Normal Operations |

---

# SECTION 06 — ACTION MATRIX

| Condition | Recommended Action |
|------------|------------|
| Capacity >= 100% | Do Not Intake |
| Capacity 80%-99% | Review Before Routing |
| Missing Assignments > 3 | Data Quality Review |
| Stale Updates > 24 Hours | Contact Centre |
| Emergency Closure Active | Exclude Centre |
| Species Occupancy > Threshold | Review Alternate Housing |
| Healthy Capacity + Available Space | Candidate Centre |

---

# SECTION 07 — NARRATIVE STORY

## Story Goal

Support Animal Flow in answering:

```text
Which centres can safely receive additional animals?
```

---

## Story 0

### Question

What is happening across the network today?

### Output

```text
Operational Snapshot
```

### Audience

All Users

### Action

Understand network context.

---

## Story 1

### Question

What requires immediate attention?

### Output

```text
Action Required
```

### Audience

Animal Flow

### Action

Identify urgent operational issues.

---

## Story 2

### Question

Can we intake more animals?

### Output

```text
Intake Readiness
```

### Audience

Animal Flow

### Action

Determine placement readiness.

---

## Story 3

### Question

Which centres should be prioritized?

### Output

```text
Placement Decision Board
```

### Audience

Animal Flow

### Action

Select candidate centres.

---

## Story 4

### Question

Why can or can't a centre receive animals?

### Output

```text
Capacity vs Occupancy
```

### Audience

Animal Flow

### Action

Understand operational constraints.

---

## Story 5

### Question

How is capacity being consumed?

### Output

```text
Species Occupancy
```

### Audience

Animal Flow

### Action

Identify recoverable capacity.

---

## Story 6

### Question

Can the information be trusted?

### Output

```text
Data Trust
```

### Audience

Animal Flow

### Action

Validate confidence before acting.

---

## Story 7

### Question

Where is pressure building?

### Output

```text
Regional Health
```

### Audience

Animal Flow
Leadership

### Action

Monitor regional trends.

---

## Story 8

### Question

What should Animal Flow do next?

### Output

```text
AI Operational Briefing
```

### Audience

Animal Flow

### Action

Execute recommendations.

---

# SECTION 08 — PAGE ARCHETYPE

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

# SECTION 09 — LAYOUT BLUEPRINT

```text
Animal Type Filter

↓

Operational Snapshot

↓

Action Required

↓

Intake Readiness

↓

Placement Decision Board

↓

Capacity vs Occupancy

↓

Species Occupancy

↓

Data Trust

↓

Regional Health

↓

AI Operational Briefing
```

---

# SECTION 10 — VISUAL RECOMMENDATIONS

## Operational Snapshot

Visual:

```text
Informational KPI Cards
```

Reason:

Provide context.

---

## Action Required

Visual:

```text
Exception KPI Cards
```

Reason:

Highlight urgent issues.

---

## Intake Readiness

Visual:

```text
Status KPI Cards
```

Reason:

Quick operational assessment.

---

## Placement Decision Board

Visual:

```text
Priority Table
```

Reason:

Supports ranking and placement decisions.

---

## Capacity vs Occupancy

Visual:

```text
Comparison Cards
```

Reason:

Explain capacity constraints.

---

## Species Occupancy

Visual:

```text
Breakdown Chart
```

Reason:

Explain non-target capacity consumption.

---

## Data Trust

Visual:

```text
Exception Matrix
```

Reason:

Validate confidence.

---

## Regional Health

Visual:

```text
Horizontal Bar Chart
```

Reason:

Compare regions quickly.

---

## AI Operational Briefing

Visual:

```text
Recommendation Cards
```

Reason:

Convert risks into actions.

---

# SECTION 11 — MARKDOWN WIREFRAME REFERENCE

```text
Animal Type Filter

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

---

# SECTION 12 — SUCCESS CRITERIA

The dashboard succeeds when users can:

✅ Understand network status

✅ Identify centres requiring intervention

✅ Identify candidate intake centres

✅ Understand care capacity constraints

✅ Understand species occupancy impacts

✅ Trust operational signals

✅ Receive actionable recommendations

✅ Navigate from summary to centre-level investigation

✅ Make intake decisions without manually interpreting raw metrics

---

# Approval Gate

Decision Model

☐ Approved

Business Questions

☐ Approved

Signals

☐ Approved

Thresholds

☐ Approved

Actions

☐ Approved

Narrative Story

☐ Approved

Layout Blueprint

☐ Approved

Visual Recommendations

☐ Approved

---

## Next Step

```text
Generate:

MOCKUP_v1.0.md

(Markdown Wireframe)
```