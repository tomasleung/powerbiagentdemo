# REPORT_STORY_MATRIX_v1.0.md
## Animal Flow — Capacity Intelligence
### Decision Story Matrix

---

# Document Metadata

Document Type: Decision Story Matrix

Version: 1.0

Capability: Animal Flow — Capacity Intelligence

Purpose:

Provide a fast-review decision framework before generating the full Decision Story Contract (DSC).

Audience:

- Product Owner
- Business Owner
- Report Designer
- BI Developer

Approval Gate:

This artifact must be approved before creating the full DSC.

---

# STEP 01 — DECISION MODEL

## Primary Decision

Which centres can safely receive additional animals?

---

## Secondary Decisions

- Which centres require intervention?
- Which centres should be avoided for intake?
- Which centres require data quality review?
- Which regions are approaching capacity pressure?
- Which centres should be prioritized for placement?

---

## Decision Owner

Animal Flow

---

## Decision Frequency

Multiple Times Per Day

---

## Key Discovery

The actual intake decision is driven by:

```text
Care Capacity
+
Animals In Care
+
Physical Space Availability
+
Species Occupancy
+
Data Trust
+
Emergency Closure Status
```

NOT merely:

```text
Open Spaces
```

---

## Governing Business Rule

A centre may show available physical space while still being unable to accept additional animals due to care capacity limits.

Example:

```text
Open Spaces = 6

Animals In Care = 25

Care Capacity = 25

Result:

Do Not Intake
```

---

# STEP 02 — BUSINESS QUESTION MATRIX

| Business Question | Decision Category | Priority |
|-------------------|------------------|----------|
| Which centres currently have available CAT capacity? | Placement | High |
| Which centres currently have available DOG capacity? | Placement | High |
| Which centres are approaching critical utilization? | Capacity Risk | High |
| Which centres have no available capacity? | Capacity Risk | High |
| Which centres have emergency closures? | Placement Eligibility | High |
| Which centres have missing kennel assignments? | Data Trust | High |
| Which centres have stale updates? | Data Trust | Medium |
| Which centres require intervention? | Operations | High |
| Which centres should be prioritized for intake? | Placement | Critical |
| Which regions have the highest utilization? | Regional Monitoring | Medium |
| How much CAT/DOG capacity is consumed by non-target species? | Species Occupancy | Medium |
| Which centres are most affected by cross-species occupancy? | Capacity Explanation | Medium |

---

# STEP 03 — SIGNAL MATRIX

## Placement Signals

- Animals In Care
- Care Capacity
- Care Capacity %
- Remaining Capacity
- Open Space Count
- Emergency Closure Status

Supported Decision:

```text
Can this centre receive another animal?
```

---

## Physical Capacity Signals

- Total Spaces
- Open Spaces
- In Use Spaces
- Hold Spaces
- Unavailable Spaces

Supported Decision:

```text
Why is physical capacity constrained?
```

---

## Species Occupancy Signals

- Cats In Care
- Dogs In Care
- Other Animals In Care
- CAT Spaces Occupied By Other Animals
- DOG Spaces Occupied By Other Animals
- Species Occupancy Impact %

Supported Decision:

```text
How much CAT/DOG capacity is being consumed by non-target species?
```

---

## Data Trust Signals

- Missing Assignment Count
- Capacity Confirmation Status
- Last Update Time
- Assignment Accuracy %
- ShelterBuddy Sync Status

Supported Decision:

```text
Can the displayed capacity be trusted?
```

---

## Regional Signals

- Region Utilization %
- Region Capacity %
- Region Open Space %

Supported Decision:

```text
Where is capacity pressure building?
```

---

# STEP 04 — ACTION MATRIX

## Care Capacity %

| Threshold | Status | Action |
|------------|----------|----------|
| <80% | Healthy | Candidate Centre |
| 80%-99% | Monitor | Review Before Routing |
| 100%+ | Full | Do Not Intake |

Supported Decision:

```text
Can this centre receive additional animals?
```

---

## Missing Assignments

| Threshold | Status | Action |
|------------|----------|----------|
| 0 | Healthy | No Action |
| 1-3 | Warning | Review |
| >3 | Critical | Data Cleanup Required |

Supported Decision:

```text
Can the capacity numbers be trusted?
```

---

## Capacity Confirmation Age

| Threshold | Status | Action |
|------------|----------|----------|
| <12 Hours | Current | Use Normally |
| 12-24 Hours | Aging | Validate |
| >24 Hours | Stale | Contact Centre |

Supported Decision:

```text
Should this centre be reviewed before routing?
```

---

## Emergency Closure

| Status | Action |
|----------|----------|
| Active | Exclude Centre |
| Inactive | Normal Operations |

Supported Decision:

```text
Is this centre eligible for intake?
```

---

## Species Occupancy Impact

| Threshold | Status | Action |
|------------|----------|----------|
| 0 | Normal | No Action |
| 1-3 | Monitor | Review Occupancy |
| >3 | Impacting Capacity | Assess Alternate Housing |

Supported Decision:

```text
Can CAT or DOG capacity be recovered?
```

---

# STEP 05 — REPORT STORY

## Question 1

Can this centre safely receive another animal?

Output:

```text
Intake Readiness
```

Audience:

```text
Animal Flow
```

Action:

```text
Identify placement options.
```

---

## Question 2

Which centres should be prioritized?

Output:

```text
Placement Decision Board
```

Audience:

```text
Animal Flow
```

Action:

```text
Select candidate centres.
```

---

## Question 3

Why can or can't a centre receive animals?

Output:

```text
Capacity vs Occupancy
```

Audience:

```text
Animal Flow
```

Action:

```text
Understand capacity constraints.
```

---

## Question 4

How is capacity being consumed?

Output:

```text
Species Occupancy
```

Audience:

```text
Animal Flow
```

Action:

```text
Identify recoverable capacity.
```

---

## Question 5

Can the information be trusted?

Output:

```text
Data Trust
```

Audience:

```text
Animal Flow
```

Action:

```text
Validate decision confidence.
```

---

## Question 6

Where is pressure building?

Output:

```text
Regional Health
```

Audience:

```text
Leadership
Animal Flow
```

Action:

```text
Monitor regional trends.
```

---

## Question 7

What should Animal Flow do next?

Output:

```text
AI Operational Briefing
```

Audience:

```text
Animal Flow
```

Action:

```text
Execute recommended actions.
```

---

# STEP 06 — PAGE ARCHETYPE

Primary Archetype

```text
Operational Command Centre
```

Secondary Archetype

```text
Capacity Intelligence Dashboard
```

Supporting Archetype

```text
Exception Management
```

---

# STEP 07 — LAYOUT BLUEPRINT

```text
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

# STEP 08 — VISUAL RECOMMENDATIONS

| Section | Visual |
|----------|----------|
| Operational Snapshot | KPI Cards |
| Action Required | Exception KPI Cards |
| Intake Readiness | Status Cards |
| Placement Decision Board | Priority Table |
| Capacity vs Occupancy | KPI + Comparison View |
| Species Occupancy | Breakdown Chart |
| Data Trust | Exception Matrix |
| Regional Health | Horizontal Bar Chart |
| AI Operational Briefing | Narrative / Recommendation Cards |

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

## Next Step

```text
Generate:

REPORT_STORY_v1.0.md

(Decision Story Contract)
```