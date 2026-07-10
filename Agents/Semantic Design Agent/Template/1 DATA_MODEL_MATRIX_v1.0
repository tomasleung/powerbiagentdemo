# DATA_MODEL_MATRIX_v1.0
## Animal Flow — Capacity Intelligence
### Semantic Design Validation Matrix

---

# Document Metadata

Document Type

Data Model Matrix

Version

1.0

Artifact Type

Semantic Design Artifact

Owner

Data Architecture

Status

Draft

Purpose

Validate the business structure of the semantic model before detailed table, column, relationship, and measure design begins.

This document serves as the bridge between:

```text
TRD
↓
Business Metrics
↓
Semantic Model Design
```

Related Artifacts

```text
BRD

REPORT_STORY_MATRIX

REPORT_STORY (DSC)

TRD

DATA_MODEL_STANDARDS
```

---

# SECTION 01 — DECISION MODEL VALIDATION

## Primary Decision

```text
Which centres can safely receive additional animals?
```

---

## Secondary Decisions

```text
Which centres require intervention?

Which centres should be avoided?

Which centres require data quality review?

Which centres should be prioritized?

Which regions are approaching capacity pressure?
```

---

## Semantic Modeling Goal

The semantic model must support all approved decisions without requiring users to manually calculate capacity or interpret raw source data.

---

# SECTION 02 — BUSINESS SIGNAL INVENTORY

## Intake Readiness Signals

```text
Animals In Care

Care Capacity

Remaining Capacity

Capacity Utilization %

Open Spaces

Emergency Closure Status
```

Decision Supported

```text
Can this centre receive another animal?
```

---

## Capacity Signals

```text
Total Spaces

Open Spaces

In Use Spaces

Hold Spaces

Unavailable Spaces
```

Decision Supported

```text
Why is capacity constrained?
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

Decision Supported

```text
How is capacity being consumed?
```

---

## Data Trust Signals

```text
Missing Assignments

Assignment Accuracy %

Pending Confirmation

Stale Updates

Confirmation Status
```

Decision Supported

```text
Can the information be trusted?
```

---

## Regional Signals

```text
Regional Capacity %

Regional Utilization %

Regional Open Space %
```

Decision Supported

```text
Where is pressure building?
```

---

# SECTION 03 — MEASURE INVENTORY

## Operational Snapshot Measures

```text
Total Centres

Animals In Care

Care Capacity

Open Spaces

CAT Spaces

DOG Spaces
```

---

## Intake Readiness Measures

```text
Available Centres

Monitor Centres

Full Centres

Closed Centres

Remaining Capacity

Capacity Utilization %
```

---

## Placement Measures

```text
Animals In Care

Care Capacity

Remaining Capacity

Open Spaces

Recommendation Status
```

---

## Species Occupancy Measures

```text
Cats In Care

Dogs In Care

Other Animals

CAT Capacity Impact

DOG Capacity Impact

Species Occupancy Impact
```

---

## Data Trust Measures

```text
Missing Assignments

Assignment Accuracy %

Pending Confirmations

Stale Updates
```

---

## Regional Measures

```text
Regional Capacity %

Regional Utilization %

Regional Open Space %
```

---

# SECTION 04 — GRAIN ANALYSIS

## Capacity Grain

One row represents:

```text
One Centre

+
One Date

+
One Animal Type
```

Target Fact

```text
Fact_Capacity
```

---

## Occupancy Grain

One row represents:

```text
One Animal

+
One Centre

+
One Date
```

Target Fact

```text
Fact_Occupancy
```

---

## Confirmation Grain

One row represents:

```text
One Centre

+
One Confirmation Event
```

Target Fact

```text
Fact_Confirmation
```

---

# SECTION 05 — FACT IDENTIFICATION MATRIX

## Fact_Capacity

Business Purpose

Store centre-level capacity metrics.

Supports Signals

```text
Care Capacity

Open Spaces

Capacity Utilization

Physical Capacity
```

Supports Measures

```text
Care Capacity

Remaining Capacity

Open Spaces

Capacity %
```

---

## Fact_Occupancy

Business Purpose

Store animal occupancy metrics.

Supports Signals

```text
Animals In Care

Species Occupancy

Assignment Status
```

Supports Measures

```text
Animals In Care

CAT Occupancy Impact

DOG Occupancy Impact

Species Occupancy Impact
```

---

## Fact_Confirmation

Business Purpose

Store operational update and freshness metrics.

Supports Signals

```text
Pending Confirmation

Stale Updates

Confirmation Status
```

Supports Measures

```text
Pending Confirmations

Stale Updates
```

---

# SECTION 06 — DIMENSION IDENTIFICATION MATRIX

## Dim_Centre

Business Purpose

Provide centre context.

Attributes

```text
Centre Name

Centre Code

Region

Location
```

Used For

```text
Filtering

Grouping

Drillthrough
```

---

## Dim_Date

Business Purpose

Provide time intelligence.

Attributes

```text
Date

Week

Month

Quarter

Year
```

Used For

```text
Trend Analysis

Filtering

Aggregation
```

---

## Dim_Animal_Type

Business Purpose

Provide animal classification.

Attributes

```text
Animal Type

Animal Category
```

Values

```text
Dog

Cat

Rabbit

Small Animal

Other
```

---

## Dim_Region

Business Purpose

Provide regional grouping.

Attributes

```text
Region Name
```

Values

```text
Island

Interior

Lower Mainland

North
```

---

# SECTION 07 — FACT TO DIMENSION MATRIX

## Fact_Capacity

Connected Dimensions

```text
Dim_Centre

Dim_Date

Dim_Animal_Type
```

---

## Fact_Occupancy

Connected Dimensions

```text
Dim_Centre

Dim_Date

Dim_Animal_Type
```

---

## Fact_Confirmation

Connected Dimensions

```text
Dim_Centre

Dim_Date
```

---

# SECTION 08 — SEMANTIC MODEL BLUEPRINT

```text
                Dim_Date
                    │
                    │
                    ▼

Dim_Centre ───────────── Fact_Capacity
     │
     │
     ├────────────── Fact_Occupancy
     │
     │
     └────────────── Fact_Confirmation

Dim_Animal_Type
        │
        ├────────── Fact_Capacity
        │
        └────────── Fact_Occupancy

Dim_Region
        │
        ▼
   Dim_Centre
```

---

# SECTION 09 — MODEL VALIDATION

## Decision Validation

```text
✓ Primary Decision Supported

✓ Secondary Decisions Supported
```

---

## Signal Validation

```text
✓ All Signals Mapped

✓ No Orphan Signals
```

---

## Measure Validation

```text
✓ All Measures Identified

✓ Measures Trace To Signals
```

---

## Grain Validation

```text
✓ Fact Grain Defined

✓ No Mixed Grain Tables
```

---

## Fact Validation

```text
✓ Facts Support Measures

✓ Facts Support Decisions
```

---

## Dimension Validation

```text
✓ Dimensions Support Filtering

✓ Dimensions Support Analysis
```

---

# SECTION 10 — HANDOFF TO SEMANTIC MODEL SPEC

Approval Required

```text
Business Architect

Data Architect

BI Architect
```

---

Output Upon Approval

```text
SEMANTIC_MODEL_SPEC_v1.0
```

Purpose

```text
Expand Facts

Expand Dimensions

Define Columns

Define Data Types

Define Relationships

Define Cardinality

Define Filter Direction
```

---

# SUCCESS STATEMENT

The Data Model Matrix succeeds when:

```text
Every Decision
supports a Signal

Every Signal
supports a Measure

Every Measure
supports a Fact

Every Fact
supports a Semantic Model
```

and the architecture can be handed to a Data Architect for detailed semantic model specification.