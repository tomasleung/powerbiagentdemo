# MOCKUP_v1.0.md
## Animal Flow — Capacity Intelligence
### Markdown Wireframe

---

# Document Metadata

Document Type: Markdown Wireframe

Version: 1.0

Capability: Animal Flow — Capacity Intelligence

Purpose:

Validate report story, information hierarchy, KPI placement, and user decision flow before SVG rendering and technical design.

Related Documents:

```text
BRD_AnimalFlow_Capacity_Intelligence_v1.0

REPORT_STORY_MATRIX_v1.0

REPORT_STORY_v1.0
```

---

# Dashboard Objective

Support Animal Flow in answering:

```text
Which centres can safely receive additional animals?
```

within 30 seconds of opening the dashboard.

---

# Narrative Flow

```text
What is happening today?

↓

What requires attention?

↓

Can we intake more animals?

↓

Which centres should be prioritized?

↓

Why can or can't a centre receive animals?

↓

How is capacity being consumed?

↓

Can the information be trusted?

↓

Where is pressure building?

↓

What actions should Animal Flow take?
```

---

# Dashboard Layout

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

# SECTION 00 — ANIMAL TYPE FILTER

Purpose

Allow users to evaluate capacity intelligence for a specific animal type without changing report structure.

Filter Values

```text
All

Cat

Dog

Rabbit

Small Animal

Other
```

Default

```text
All
```

---

# SECTION 01 — OPERATIONAL SNAPSHOT

Purpose

Provide immediate network context.

Decision Supported

```text
None

Informational Context Only
```

---

Visual Type

```text
KPI Cards
```

---

Metrics

```text
Total Centres

Animals In Care

Care Capacity

Open Spaces

CAT Spaces

DOG Spaces
```

---

Business Question

```text
What is happening across the network today?
```

---

# SECTION 02 — ACTION REQUIRED

Purpose

Highlight issues requiring immediate attention.

Decision Supported

```text
What requires operational intervention?
```

---

Visual Type

```text
Exception KPI Cards
```

---

Metrics

```text
Centres At Capacity

Data Quality Issues

Pending Confirmations

Emergency Closures
```

---

Expected Layout

```text
┌────────────┐
│ At Capacity│
└────────────┘

┌────────────┐
│ Data Issues│
└────────────┘

┌────────────┐
│ Pending    │
└────────────┘

┌────────────┐
│ Closures   │
└────────────┘
```

---

# SECTION 03 — INTAKE READINESS

Purpose

Provide an overall intake readiness assessment.

Decision Supported

```text
Can we accept more animals?
```

---

Visual Type

```text
Status KPI Cards
```

---

Metrics

```text
Available Centres

Monitor Centres

Full Centres

Closed Centres
```

---

Business Rules

```text
Healthy

<80%

Monitor

80%-99%

Full

>=100%
```

---

# SECTION 04 — PLACEMENT DECISION BOARD

Purpose

Identify the best candidate centres.

Decision Supported

```text
Which centres should Animal Flow prioritize?
```

---

Visual Type

```text
Priority Table
```

---

Columns

```text
Centre

Animals In Care

Care Capacity

Remaining Capacity

Open Spaces

Recommendation
```

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

Expected Layout

```text
Centre

Animals

Capacity

Remaining

Recommendation
```

---

Sort Order

```text
Remaining Capacity DESC
```

---

# SECTION 05 — CAPACITY VS OCCUPANCY

Purpose

Explain centre readiness.

Decision Supported

```text
Why can or can't a centre receive animals?
```

---

Visual Types

```text
Comparison Cards

Capacity Summary
```

---

Care Capacity Health

```text
Animals In Care

Care Capacity

Remaining Capacity

Capacity Utilization %
```

---

Physical Space Health

```text
Total Spaces

Open Spaces

In Use Spaces

Hold Spaces

Unavailable Spaces
```

---

# SECTION 06 — SPECIES OCCUPANCY

Purpose

Explain how CAT and DOG capacity are impacted by non-target species.

Decision Supported

```text
How is capacity being consumed?
```

---

Visual Type

```text
Breakdown Summary
```

---

Metrics

```text
Cats In Care

Dogs In Care

Other Animals

CAT Spaces Occupied By Other Animals

DOG Spaces Occupied By Other Animals
```

---

Business Questions

```text
How much CAT capacity is occupied by rabbits or small animals?

How much DOG capacity is occupied by non-dog species?
```

---

Business Actions

```text
Review Alternate Housing

Restore Available Capacity

Review Species Placement
```

---

# SECTION 07 — DATA TRUST

Purpose

Measure confidence in capacity data.

Decision Supported

```text
Can the information be trusted?
```

---

Visual Type

```text
Exception Summary
```

---

Metrics

```text
Missing Assignments

Assignment Accuracy %

Pending Confirmation

Stale Updates
```

---

Business Rules

```text
Missing Assignments > 3

Review Required

Update Age > 24 Hours

Stale
```

---

# SECTION 08 — REGIONAL HEALTH

Purpose

Provide regional monitoring.

Decision Supported

```text
Where is capacity pressure building?
```

---

Visual Type

```text
Regional Ranking
```

---

Metrics

```text
Regional Utilization %

Regional Capacity %

Regional Open Space %
```

---

Expected Layout

```text
Interior

Island

Lower Mainland

North
```

Sorted by:

```text
Utilization DESC
```

---

# SECTION 09 — AI OPERATIONAL BRIEFING

Purpose

Convert signals into decisions and actions.

Decision Supported

```text
What should Animal Flow do next?
```

---

Visual Type

```text
Recommendation Cards
```

---

Card Categories

```text
Capacity Risks

Species Occupancy Risks

Data Quality Risks

Recommended Actions
```

---

Example Outputs

### Capacity Risks

```text
Victoria has reached 100% Care Capacity.

Recommendation:

Do Not Intake
```

---

### Species Occupancy Risks

```text
Nanaimo CAT capacity is impacted by
non-cat occupancy.

Recommendation:

Review Alternate Housing
```

---

### Data Quality Risks

```text
Williams Lake contains six animals
without valid kennel assignments.

Recommendation:

Review ShelterBuddy Assignments
```

---

### Recommended Actions

```text
1. Pause intake to Victoria.

2. Review species occupancy in Nanaimo.

3. Resolve assignment issues in Williams Lake.

4. Prioritize Kelowna for placement.
```

---

# Final User Journey

```text
Open Dashboard

↓

Understand Network Status

↓

Review Critical Exceptions

↓

Determine Intake Readiness

↓

Review Candidate Centres

↓

Understand Capacity Constraints

↓

Verify Data Confidence

↓

Review Regional Pressure

↓

Execute Recommended Actions
```

---

# Wireframe Approval Checklist

Operational Snapshot

☐ Approved

---

Action Required

☐ Approved

---

Intake Readiness

☐ Approved

---

Placement Decision Board

☐ Approved

---

Capacity vs Occupancy

☐ Approved

---

Species Occupancy

☐ Approved

---

Data Trust

☐ Approved

---

Regional Health

☐ Approved

---

AI Operational Briefing

☐ Approved

---

## Next Step

```text
Generate:

MOCKUP_v1.0.svg

(SVG Wireframe)
```