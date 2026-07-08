# REPORT_STORY_v1.2.md
## Animal Flow — Capacity Intelligence
### RDLC Decision Story Contract (DSC)

---

# Document Metadata

Version: 1.2

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

### Q13

How much CAT or DOG capacity is currently being consumed by non-target species?

Priority: Medium

Decision Category: Species Occupancy

---

### Q14

Which centres have CAT/DOG capacity impacted by rabbits, small animals, or other species?

Priority: Medium

Decision Category: Capacity Explanation

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
Species Occupancy
+
Data Trust
+
Emergency Closure Status
=
Intake Readiness
```

---

## Physical Capacity

Represents floor plan availability.

Examples:

- Total Spaces
- Open Spaces
- Hold Spaces
- Unavailable Spaces

---

## Care Capacity

Represents the maximum number of animals a centre can safely support operationally.

Care Capacity reflects:

- Staffing
- Workload
- Animal care resources
- Operational limits

Care Capacity is the PRIMARY intake constraint.

---

## Species Occupancy Rule

A centre may temporarily house animals outside the primary species that a space was designed for.

Examples:

```text
Rabbit occupying CAT space

Guinea Pig occupying CAT space

Small Animal occupying CAT space

Other Animal occupying DOG space
```

These occupancy conditions may reduce available CAT or DOG intake capacity and should be visible during intake decisions.

---

## Example

Centre A

```text
Total CAT Spaces = 17

Open CAT Spaces = 6

Cats In Care = 20

Other Animals In CAT Space = 5

CAT Care Capacity = 25
```

Result

```text
CAT Capacity Full
```

Although open spaces remain available, CAT capacity is constrained by occupancy from both cats and non-cat species.

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

## Species Occupancy Signals

Cats In Care

Dogs In Care

Other Animals In Care

CAT Spaces Occupied By Other Animals

DOG Spaces Occupied By Other Animals

Species Occupancy %

Species Occupancy Impact Centres

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
>3
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
<12 Hours
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
>24 Hours
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
Exclude Centre From Placement Options
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
| Missing Assignments >3 | Review Data Quality |
| Stale Updates >24 Hours | Contact Centre |
| Emergency Closure Active | Exclude Centre |
| Healthy Capacity + Available Space | Candidate Centre |
| High Other Species Occupancy | Review Alternate Housing Options |

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

How is capacity being consumed?

Output:

Species Occupancy

---

### Story 5

Can the underlying data be trusted?

Output:

Data Trust

---

### Story 6

Where is capacity pressure building?

Output:

Regional Health

---

### Story 7

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

Provide provincial context before decisions.

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

## SECTION 05 — SPECIES OCCUPANCY

Purpose

Understand how non-target species consume available capacity.

Metrics

- Cats In Care
- Dogs In Care
- Other Animals In Care
- CAT Spaces Occupied By Other Animals
- DOG Spaces Occupied By Other Animals
- Top Impact Centres

Supported Questions

```text
How much CAT capacity is being consumed by rabbits or small animals?

How much DOG capacity is being consumed by other species?

Which centres are most impacted by cross-species occupancy?
```

Supported Actions

```text
Review alternative housing options.

Restore CAT intake capacity.

Restore DOG intake capacity.

Review occupancy constraints before restricting intake.
```

---

## SECTION 06 — DATA TRUST

Purpose

Measure confidence in decision signals.

Metrics

- Missing Assignments
- Assignment Accuracy
- Pending Confirmations
- Stale Updates

---

## SECTION 07 — REGIONAL HEALTH

Purpose

Regional monitoring.

Metrics

- Regional Utilization
- Regional Capacity
- Regional Open Space

---

## SECTION 08 — AI OPERATIONAL BRIEFING

Purpose

Operational recommendations.

Outputs

- Centres Requiring Attention
- Candidate Centres
- Data Quality Risks
- Species Occupancy Risks
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
Priority Table
```

---

## Capacity vs Occupancy

Visual Type

```text
Comparison Cards + Stacked Bar
```

---

## Species Occupancy

Visual Type

```text
Species Breakdown Chart
+
Top Impact Centres Table
```

Reason

```text
Explains why care capacity may be constrained
even when physical space appears available.
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
Species Occupancy

SECTION 06
Data Trust

SECTION 07
Regional Health

SECTION 08
AI Operational Briefing
```

---

# SECTION 12 — SUCCESS CRITERIA

A successful dashboard enables Animal Flow to:

✅ Understand provincial capacity in less than 15 seconds

✅ Identify centres requiring intervention

✅ Identify eligible intake centres

✅ Understand care capacity constraints

✅ Understand species occupancy impacts

✅ Trust operational signals

✅ Receive actionable recommendations

✅ Navigate from summary to centre-level investigation

✅ Make intake decisions without manually interpreting raw metrics

---

## Dashboard Success Statement

The dashboard succeeds when users can answer:

```text
Which centres can safely receive additional animals?
```

within 30 seconds of opening the report.