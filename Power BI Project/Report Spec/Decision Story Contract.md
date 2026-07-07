# REPORT_STORY_v1.1.md
## Animal Flow — Capacity Intelligence
### RDLC Decision Story Contract (DSC)

---

# Document Metadata

Version: 1.1

Product: Animal Flow — Capacity Intelligence

Artifact Type: Decision Story Contract (DSC)

Owner: Animal Flow

Author: Tomas Leung

Status: Draft

Purpose:

Bridge the gap between the BRD and TRD by converting business decisions into a report story, action framework, dashboard blueprint, and visual design contract.

---

# SECTION 01 — DECISION MODEL

## Primary Decision

Which centres can safely receive additional animals?

---

## Secondary Decisions

Which centres require intervention?

Which centres should be excluded from intake decisions?

Which centres require data quality review?

Which regions are approaching capacity pressure?

Can the underlying data be trusted?

---

## Decision Owner

Animal Flow Team

---

## Review Frequency

Multiple times per day

---

# SECTION 02 — BUSINESS QUESTION MATRIX

## Capacity Questions

### Q1

Which centres currently have available DOG capacity?

Priority: High

Decision Category: Placement

---

### Q2

Which centres currently have available CAT capacity?

Priority: High

Decision Category: Placement

---

### Q3

Which centres are approaching critical utilization?

Priority: High

Decision Category: Capacity Risk

---

### Q4

Which centres have no available capacity?

Priority: High

Decision Category: Capacity Risk

---

### Q5

Which centres have emergency closures in effect?

Priority: High

Decision Category: Placement Eligibility

---

## Data Quality Questions

### Q6

Which centres have animals missing kennel assignments?

Priority: High

Decision Category: Data Trust

---

### Q7

Which centres have stale capacity updates?

Priority: High

Decision Category: Data Trust

---

### Q8

Which centres have not confirmed their capacity status?

Priority: High

Decision Category: Data Trust

---

### Q9

Which centres require data quality review?

Priority: High

Decision Category: Data Governance

---

## Operational Questions

### Q10

Which regions have the highest utilization?

Priority: Medium

Decision Category: Capacity Monitoring

---

### Q11

Which centres require intervention?

Priority: High

Decision Category: Action Management

---

### Q12

Which centres should be prioritized for intake decisions?

Priority: Critical

Decision Category: Placement

---

# SECTION 03 — BUSINESS LOGIC MODEL

## Governing Business Rule

Intake decisions are NOT determined solely by physical space.

Intake readiness is determined by:

```text
Animals In Care
+
Care Capacity
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

## Important Business Concept

### Physical Capacity

Represents kennel, portal, room, and floor plan availability.

Examples:

- Total Spaces
- Open Spaces
- Hold Spaces
- Unavailable Spaces

---

### Care Capacity

Represents the maximum number of animals a centre can support operationally.

Care Capacity considers:

- Staffing
- Workload
- Animal care requirements
- Centre operating limits

Care Capacity is the PRIMARY intake constraint.

---

## Example

Centre A

```text
Total Spaces = 17

Open Spaces = 6

Animals In Care = 25

Care Capacity = 25
```

Result:

```text
Do Not Intake
```

Reason:

```text
Care Capacity has been reached.
```

Although physical space exists, the centre has no remaining care capacity.

---

# SECTION 04 — SIGNAL MATRIX

## Operational Snapshot Signals

Total Centres

Total Animals In Care

Total Care Capacity

Total Open Spaces

Total CAT Spaces

Total DOG Spaces

---

## Intake Readiness Signals

Animals In Care

Care Capacity

Care Capacity %

Remaining Care Capacity

Emergency Closure Status

Open Space Count

---

## Physical Capacity Signals

Total Spaces

Open Spaces

In Use Spaces

Hold Spaces

Unavailable Spaces

---

## Data Trust Signals

Missing Kennel Assignments

Capacity Confirmation Status

Last Update Time

Assignment Accuracy %

ShelterBuddy Synchronization Status

---

## Regional Signals

Regional Capacity Utilization %

Regional Care Capacity %

Regional Open Space %

---

# SECTION 05 — THRESHOLD MATRIX

## Care Capacity %

Signal

```text
Animals In Care ÷ Care Capacity
```

### Healthy

Threshold

```text
< 80%
```

Action

```text
Candidate Centre
```

Status

```text
Green
```

---

### Monitor

Threshold

```text
80% - 99%
```

Action

```text
Review Before Routing
```

Status

```text
Yellow
```

---

### Full

Threshold

```text
>= 100%
```

Action

```text
Do Not Intake
```

Status

```text
Red
```

---

## Missing Kennel Assignments

### Healthy

```text
0
```

Action

```text
No Action
```

Status

```text
Green
```

---

### Warning

```text
1-3
```

Action

```text
Review Assignments
```

Status

```text
Yellow
```

---

### Critical

```text
> 3
```

Action

```text
Manager Review Required
```

Status

```text
Red
```

---

## Capacity Confirmation

### Current

```text
< 12 Hours
```

Action

```text
Use Normally
```

---

### Aging

```text
12-24 Hours
```

Action

```text
Validate Before Routing
```

---

### Stale

```text
> 24 Hours
```

Action

```text
Contact Centre
```

---

## Emergency Closure

### Active

Action

```text
Exclude Centre from Placement Options
```

Status

```text
Red
```

---

# SECTION 06 — ACTION MATRIX

| Condition | Action |
|------------|------------|
| Care Capacity >= 100% | Do Not Intake |
| Care Capacity 80%-99% | Review Before Routing |
| Missing Assignments > 3 | Review Data Quality |
| Stale Updates > 24 Hours | Contact Centre |
| Emergency Closure Active | Exclude Centre |
| Healthy Capacity + Available Space | Candidate Centre |

---

# SECTION 07 — REPORT STORY

## Story Goal

Support Animal Flow in determining:

```text
Which centres can safely receive additional animals?
```

---

## Story Sequence

### Story 0

What is happening provincially today?

Output:

Operational Snapshot

---

### Story 1

Can this centre safely receive another animal?

Output:

Intake Readiness

---

### Story 2

Which centres should be prioritized?

Output:

Placement Decision Board

---

### Story 3

Why can or can't a centre receive animals?

Output:

Capacity vs Care Capacity

---

### Story 4

Can the data be trusted?

Output:

Data Trust

---

### Story 5

Where is pressure building?

Output:

Regional Health

---

### Story 6

What should Animal Flow do next?

Output:

AI Operational Briefing

---

# SECTION 08 — PAGE ARCHETYPE

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

# SECTION 09 — PAGE LAYOUT BLUEPRINT

## SECTION 00 — OPERATIONAL SNAPSHOT

Purpose

Provide provincial context.

Classification

Informational

Decision Supported

None

---

Metrics

- Total Centres
- Total Animals In Care
- Total Care Capacity
- Total Open Spaces
- Total CAT Spaces
- Total DOG Spaces

---

## SECTION 01 — ACTION REQUIRED

Purpose

Immediate operational attention.

Metrics

- Centres At Capacity
- Data Quality Issues
- Pending Confirmations
- Emergency Closures

---

## SECTION 02 — INTAKE READINESS

Purpose

Determine placement options.

Metrics

- Available Centres
- Monitor Centres
- Full Centres
- Closed Centres

---

## SECTION 03 — PLACEMENT DECISION BOARD

Purpose

Identify recommended centres.

Metrics

- Centre
- Animals In Care
- Care Capacity
- Remaining Capacity
- Open Spaces
- Recommendation

---

Business Rule

```text
Remaining Capacity
=
Care Capacity
-
Animals In Care
```

---

## SECTION 04 — CAPACITY VS OCCUPANCY

Purpose

Explain centre readiness.

Metrics

### Care Capacity Health

- Animals In Care
- Care Capacity
- Remaining Capacity
- Care Capacity %

### Physical Space Health

- Total Space
- Open Space
- In Use
- Hold
- Unavailable

---

## SECTION 05 — DATA TRUST

Purpose

Measure confidence.

Metrics

- Missing Assignments
- Assignment Accuracy
- Pending Confirmations
- Stale Updates

---

## SECTION 06 — REGIONAL HEALTH

Purpose

Regional monitoring.

Metrics

- Regional Utilization
- Regional Capacity
- Regional Open Space

---

## SECTION 07 — AI OPERATIONAL BRIEFING

Purpose

Operational recommendations.

Outputs

- Centres Requiring Attention
- Candidate Centres
- Data Quality Risks
- Capacity Risks
- Recommended Actions

---

# SECTION 10 — VISUAL RECOMMENDATIONS

## Operational Snapshot

Visual Type

```text
Informational KPI Cards
```

---

## Action Required

Visual Type

```text
Exception KPI Cards
```

---

## Intake Readiness

Visual Type

```text
Status KPI Cards
```

---

## Placement Decision Board

Visual Type

```text
Priority Matrix Table
```

---

## Capacity vs Occupancy

Visual Type

```text
Comparison Cards + Stacked Bar
```

---

## Data Trust

Visual Type

```text
Exception Matrix
```

---

## Regional Health

Visual Type

```text
Horizontal Bar Chart
```

---

## AI Operational Briefing

Visual Type

```text
Narrative Card
```

---

# SECTION 11 — MARKDOWN WIREFRAME

```text
SECTION 00
Operational Snapshot

SECTION 01
Action Required

SECTION 02
Intake Readiness

SECTION 03
Placement Decision Board

SECTION 04
Capacity vs Occupancy

SECTION 05
Data Trust

SECTION 06
Regional Health

SECTION 07
AI Operational Briefing
```

---

# SECTION 12 — SUCCESS CRITERIA

A successful dashboard enables Animal Flow to:

✅ Understand provincial capacity in less than 15 seconds

✅ Identify centres requiring intervention

✅ Identify eligible intake centres

✅ Understand care capacity constraints

✅ Trust operational signals

✅ Receive actionable recommendations

✅ Navigate from summary to centre-level investigation

✅ Make intake decisions without manually interpreting raw metrics

---

## Dashboard Success Statement

The report succeeds when users can answer:

```text
Which centres can safely receive additional animals?
```

within 30 seconds of opening the dashboard.