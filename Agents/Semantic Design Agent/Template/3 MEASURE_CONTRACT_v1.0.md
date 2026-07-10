# MEASURE_CONTRACT_v1.0
## Animal Flow — Capacity Intelligence
### Measure Governance Contract

---

# Document Metadata

Document Type

Measure Contract

Version

1.0

Artifact Type

Semantic Design Artifact

Owner

BI Architecture

Status

Draft

Purpose

Provide governance, business definitions, calculation requirements, threshold rules, and decision traceability for all semantic model measures.

This document serves as the authoritative reference for:

```text
Measure Design

Business Definitions

Calculation Logic

Threshold Rules

Action Mapping

Decision Traceability
```

Related Artifacts

```text
BRD

REPORT_STORY_MATRIX

REPORT_STORY (DSC)

TRD

DATA_MODEL_MATRIX

SEMANTIC_MODEL_SPEC

DATA_MODEL_STANDARDS
```

---

# SECTION 01 — MEASURE DESIGN STANDARDS

## Governing Principle

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
Threshold
↓
Action
```

---

## Measure Requirements

Every measure must define:

```text
Measure Name

Business Definition

Business Question

Signal

Calculation Logic

Threshold

Action

Decision Supported
```

---

## Explicit Measures Only

All calculations must be created as explicit measures.

Do not rely on:

```text
Implicit SUM

Implicit COUNT

Implicit AVERAGE
```

---

# SECTION 02 — OPERATIONAL SNAPSHOT MEASURES

# Total Centres

Business Definition

Total active centres participating in capacity reporting.

Business Question

```text
How large is the operating network?
```

Signal

```text
Centre Count
```

Calculation Logic

```text
Distinct Count of Active Centres
```

Threshold

```text
None
```

Action

```text
Informational
```

Decision Supported

```text
Network Context
```

---

# Animals In Care

Business Definition

Current occupied animal count.

Business Question

```text
How many animals are currently being supported?
```

Signal

```text
Animal Occupancy
```

Calculation Logic

```text
Count Active Animal Occupancy Records
```

Threshold

```text
None
```

Action

```text
Informational
```

Decision Supported

```text
Capacity Monitoring
```

---

# Care Capacity

Business Definition

Maximum operational animal capacity.

Business Question

```text
How much care capacity is available?
```

Signal

```text
Care Capacity
```

Calculation Logic

```text
Sum Centre Care Capacity
```

Threshold

```text
None
```

Action

```text
Informational
```

Decision Supported

```text
Capacity Monitoring
```

---

# Open Spaces

Business Definition

Physical spaces currently available.

Business Question

```text
How much physical space remains?
```

Signal

```text
Open Space Count
```

Calculation Logic

```text
Sum Open Spaces
```

Threshold

```text
None
```

Action

```text
Informational
```

Decision Supported

```text
Capacity Monitoring
```

---

# SECTION 03 — INTAKE READINESS MEASURES

# Remaining Capacity

Business Definition

Available care capacity after current occupancy.

Business Question

```text
Which centres can receive another animal?
```

Signal

```text
Remaining Capacity
```

Calculation Logic

```text
Care Capacity
-
Animals In Care
```

Threshold

```text
Greater than 0
```

Action

```text
Candidate Centre
```

Decision Supported

```text
Can this centre safely receive another animal?
```

---

# Capacity Utilization %

Business Definition

Percentage of care capacity currently utilized.

Business Question

```text
How close is a centre to operating capacity?
```

Signal

```text
Capacity Utilization
```

Calculation Logic

```text
Animals In Care
/
Care Capacity
```

Thresholds

```text
<80%
Healthy

80%-99%
Monitor

>=100%
Full
```

Actions

```text
Healthy
Candidate Centre

Monitor
Review Before Routing

Full
Do Not Intake
```

Decision Supported

```text
Can this centre safely receive another animal?
```

---

# Available Centres

Business Definition

Count of centres below utilization warning levels.

Business Question

```text
How many centres are currently available?
```

Signal

```text
Centre Capacity Status
```

Calculation Logic

```text
Count Centres
where Utilization < 80%
```

Threshold

```text
Healthy
```

Action

```text
Candidate Centre
```

Decision Supported

```text
Can we intake more animals?
```

---

# Monitor Centres

Business Definition

Count of centres approaching capacity.

Business Question

```text
Which centres require monitoring?
```

Signal

```text
Capacity Utilization %
```

Calculation Logic

```text
Count Centres
between 80% and 99%
```

Threshold

```text
Monitor
```

Action

```text
Review Before Routing
```

Decision Supported

```text
Which centres require review?
```

---

# Centres At Capacity

Business Definition

Count of centres at or above operational capacity.

Business Question

```text
Which centres should not receive additional animals?
```

Signal

```text
Capacity Utilization %
```

Calculation Logic

```text
Count Centres
>=100%
```

Threshold

```text
Full
```

Action

```text
Do Not Intake
```

Decision Supported

```text
Which centres should be avoided?
```

---

# SECTION 04 — DATA TRUST MEASURES

# Missing Assignments

Business Definition

Animals without valid assignment records.

Business Question

```text
Can occupancy calculations be trusted?
```

Signal

```text
Assignment Completeness
```

Calculation Logic

```text
Count Missing Assignments
```

Thresholds

```text
0
Healthy

1-3
Warning

>3
Critical
```

Actions

```text
Healthy
No Action

Warning
Review

Critical
Data Cleanup Required
```

Decision Supported

```text
Can the data be trusted?
```

---

# Assignment Accuracy %

Business Definition

Percentage of occupancy records with valid assignments.

Business Question

```text
How accurate is assignment data?
```

Signal

```text
Assignment Accuracy
```

Calculation Logic

```text
Valid Assignments
/
Total Assignments
```

Thresholds

```text
>=98%
Healthy

95%-97%
Warning

<95%
Critical
```

Actions

```text
Review Data Quality
```

Decision Supported

```text
Can the data be trusted?
```

---

# Pending Confirmations

Business Definition

Centres awaiting operational confirmation.

Business Question

```text
Which centres require update validation?
```

Signal

```text
Confirmation Status
```

Calculation Logic

```text
Count Pending Confirmations
```

Threshold

```text
Pending
```

Action

```text
Contact Centre
```

Decision Supported

```text
Can current capacity values be trusted?
```

---

# Stale Updates

Business Definition

Centres exceeding freshness thresholds.

Business Question

```text
Which centres may contain outdated information?
```

Signal

```text
Update Freshness
```

Calculation Logic

```text
Update Age > Threshold
```

Thresholds

```text
<12 Hours
Current

12-24 Hours
Aging

>24 Hours
Stale
```

Actions

```text
Validate

Contact Centre
```

Decision Supported

```text
Can current information be trusted?
```

---

# SECTION 05 — SPECIES OCCUPANCY MEASURES

# Species Occupancy Impact

Business Definition

Capacity occupied by non-target species.

Business Question

```text
How much capacity is being consumed by alternate species?
```

Signal

```text
Species Occupancy
```

Calculation Logic

```text
Count Occupied Spaces
by Non-Target Species
```

Thresholds

```text
0
Normal

1-3
Monitor

>3
Significant
```

Actions

```text
Review Housing

Recover Capacity
```

Decision Supported

```text
Can capacity be recovered?
```

---

# CAT Capacity Impact

Business Definition

CAT capacity consumed by non-cat species.

Business Question

```text
Why is CAT availability lower than expected?
```

Signal

```text
CAT Occupancy Impact
```

Decision Supported

```text
Can additional CAT intake occur?
```

---

# DOG Capacity Impact

Business Definition

DOG capacity consumed by non-dog species.

Business Question

```text
Why is DOG availability lower than expected?
```

Signal

```text
DOG Occupancy Impact
```

Decision Supported

```text
Can additional DOG intake occur?
```

---

# SECTION 06 — REGIONAL MEASURES

# Regional Utilization %

Business Definition

Average utilization of all centres within a region.

Business Question

```text
Which regions are under pressure?
```

Signal

```text
Regional Utilization
```

Calculation Logic

```text
Regional Occupancy
/
Regional Capacity
```

Thresholds

```text
<80%
Healthy

80%-89%
Monitor

>=90%
High Pressure
```

Action

```text
Monitor Region
```

Decision Supported

```text
Where is capacity pressure building?
```

---

# SECTION 07 — AI OPERATIONAL BRIEFING MEASURES

# Capacity Risk Count

Business Definition

Count of centres currently at capacity.

Decision Supported

```text
Which centres require intervention?
```

---

# Data Quality Risk Count

Business Definition

Count of centres with unresolved issues.

Decision Supported

```text
Can recommendations be trusted?
```

---

# Species Occupancy Risk Count

Business Definition

Count of centres impacted by non-target occupancy.

Decision Supported

```text
Can capacity be recovered?
```

---

# Recommended Intake Centres

Business Definition

Centres meeting intake readiness requirements.

Decision Supported

```text
Where should Animal Flow route animals?
```

---

# SECTION 08 — MEASURE DEPENDENCY MAP

```text
Animals In Care
          │
          ├─────────► Remaining Capacity
          │
          └─────────► Capacity Utilization %

Care Capacity
          │
          ├─────────► Remaining Capacity
          │
          └─────────► Capacity Utilization %

Species Occupancy Impact
          │
          ├─────────► CAT Capacity Impact
          │
          └─────────► DOG Capacity Impact
```

---

# SECTION 09 — MEASURE COMPLIANCE REVIEW

Explicit Measures

```text
✓ Required
```

Decision Traceability

```text
✓ Required
```

Threshold Mapping

```text
✓ Required
```

Action Mapping

```text
✓ Required
```

Business Definition

```text
✓ Required
```

Documentation

```text
✓ Required
```

---

# SUCCESS STATEMENT

A measure contract succeeds when:

```text
Every Measure
supports a Signal

Every Signal
supports a Business Question

Every Business Question
supports a Decision

Every Decision
supports an Action
```

and every measure can be implemented, governed, audited, and explained without additional business clarification.