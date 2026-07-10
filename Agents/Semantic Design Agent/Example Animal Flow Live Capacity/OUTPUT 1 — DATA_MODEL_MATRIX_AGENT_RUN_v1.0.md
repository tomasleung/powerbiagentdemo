# OUTPUT 1 — DATA_MODEL_MATRIX_AGENT_RUN_v1.0
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
Which centres should be avoided for intake?
Which centres require data quality review?
Which regions require monitoring?
Which centres should be prioritized for placement?
Which regions are approaching capacity pressure?
```

---

## Semantic Modeling Goal

The semantic model must support operational placement decisions, capacity risk monitoring, data quality review, species occupancy impact analysis, and regional pressure assessment.

It must enable users to answer the primary and secondary decisions without manual reconciliation across source systems.

---

# SECTION 02 — BUSINESS SIGNAL INVENTORY

## Intake Readiness Signals

```text
Animals In Care
Care Capacity
Remaining Capacity
Capacity Utilization %
Open Spaces
Emergency Closure
```

Decision Supported

```text
Can this centre receive additional animals?
```

---

## Capacity Signals

```text
Physical Capacity
Care Capacity
Open Spaces
Total Spaces
Space Utilization
Available Centres
Centres At Capacity
```

Decision Supported

```text
Why is capacity constrained, and which centres are intake-ready?
```

---

## Occupancy Signals

```text
Cats In Care
Dogs In Care
Other Animals
Species Occupancy Impact
```

Decision Supported

```text
How is occupancy consuming capacity by species?
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
Can the operational data be trusted for placement decisions?
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
Where is capacity pressure building regionally?
```

---

# SECTION 03 — MEASURE INVENTORY

## Measures

```text
Animals In Care
Care Capacity
Remaining Capacity
Capacity Utilization %
Available Centres
Centres At Capacity
Open Spaces
Missing Assignments
Assignment Accuracy %
Species Occupancy Impact
Regional Utilization %
Regional Capacity %
Regional Open Space %
```

Validation

```text
Each measure maps to at least one signal and supports one or more decisions.
```

---

# SECTION 04 — GRAIN ANALYSIS

## Fact_Capacity

Business Grain

One row represents the capacity snapshot for one centre, one date, and one animal type.

Example Row

Centre A + 2026-07-10 + Cat

Business Purpose

Measure available and occupied capacity for intake readiness and utilization analysis.

---

## Fact_Occupancy

Business Grain

One row represents the occupancy snapshot for one centre, one date, and one animal type.

Example Row

Centre A + 2026-07-10 + Dog

Business Purpose

Measure animals in care, assignment quality, and species occupancy impact.

---

## Fact_Confirmation

Business Grain

One row represents the confirmation status for one centre and one date.

Example Row

Centre A + 2026-07-10

Business Purpose

Measure data freshness, confirmation status, and related trust signals.

---

# SECTION 05 — FACT INVENTORY

## Fact_Capacity

Business Purpose

Support intake readiness and capacity risk decisions.

Grain

Centre + Date + Animal Type

Supported Measures

Care Capacity, Remaining Capacity, Capacity Utilization %, Open Spaces, Available Centres, Centres At Capacity

Supported Signals

Care Capacity, Remaining Capacity, Capacity Utilization %, Open Spaces, Emergency Closure, Capacity Utilization %

---

## Fact_Occupancy

Business Purpose

Support occupancy, species impact, and assignment data trust decisions.

Grain

Centre + Date + Animal Type

Supported Measures

Animals In Care, Missing Assignments, Assignment Accuracy %, Species Occupancy Impact

Supported Signals

Animals In Care, Cats In Care, Dogs In Care, Other Animals, Missing Assignments, Assignment Accuracy %, Species Occupancy Impact

---

## Fact_Confirmation

Business Purpose

Support data quality and freshness validation for placement decisions.

Grain

Centre + Date

Supported Measures

Confirmation Status, Pending Confirmation, Stale Updates, Assignment Accuracy %

Supported Signals

Confirmation Status, Pending Confirmation, Stale Updates

---

# SECTION 06 — DIMENSION INVENTORY

## Dim_Centre

Business Purpose

Provide centre-level context for placement, capacity, data trust, and regional analysis.

Attributes

Centre ID, Centre Name, Centre Type, Centre Status, Region ID, Physical Capacity, Address, Operating Hours, Facility Status

Supported Filters

By Centre, By Centre Type, By Centre Status

Supported Analysis

Centre comparison, intake readiness, intervention prioritization

---

## Dim_Date

Business Purpose

Provide time context for capacity, occupancy, and confirmation trends.

Attributes

Date, Day of Week, Week, Month, Quarter, Year, Fiscal Period

Supported Filters

By Date, By Month, By Week, By Year

Supported Analysis

Trend analysis, aging, change detection

---

## Dim_Animal_Type

Business Purpose

Provide species context for occupancy and capacity impact analysis.

Attributes

Animal Type ID, Animal Type Name, Species Category (Cat, Dog, Other), Breed Group

Supported Filters

By Animal Type, By Species Category

Supported Analysis

Species occupancy, cross-species impact, intake readiness

---

## Dim_Region

Business Purpose

Provide regional context for pressure and capacity distribution.

Attributes

Region ID, Region Name, Region Type, Region Manager

Supported Filters

By Region, By Region Type

Supported Analysis

Regional capacity pressure, geographic prioritization

---

# SECTION 07 — RELATIONSHIP MATRIX

## Fact_Capacity → Dim_Centre

Relationship

One-to-many

Cardinality

Dim_Centre (1) to Fact_Capacity (many)

Filter Direction

Single direction from Dim_Centre to Fact_Capacity

Join Key

Dim_Centre.CentreID = Fact_Capacity.CentreID

---

## Fact_Capacity → Dim_Date

Relationship

One-to-many

Cardinality

Dim_Date (1) to Fact_Capacity (many)

Filter Direction

Single direction from Dim_Date to Fact_Capacity

Join Key

Dim_Date.DateKey = Fact_Capacity.DateKey

---

## Fact_Capacity → Dim_Animal_Type

Relationship

One-to-many

Cardinality

Dim_Animal_Type (1) to Fact_Capacity (many)

Filter Direction

Single direction from Dim_Animal_Type to Fact_Capacity

Join Key

Dim_Animal_Type.AnimalTypeID = Fact_Capacity.AnimalTypeID

---

## Fact_Occupancy → Dim_Centre

Relationship

One-to-many

Cardinality

Dim_Centre (1) to Fact_Occupancy (many)

Filter Direction

Single direction from Dim_Centre to Fact_Occupancy

Join Key

Dim_Centre.CentreID = Fact_Occupancy.CentreID

---

## Fact_Occupancy → Dim_Date

Relationship

One-to-many

Cardinality

Dim_Date (1) to Fact_Occupancy (many)

Filter Direction

Single direction from Dim_Date to Fact_Occupancy

Join Key

Dim_Date.DateKey = Fact_Occupancy.DateKey

---

## Fact_Occupancy → Dim_Animal_Type

Relationship

One-to-many

Cardinality

Dim_Animal_Type (1) to Fact_Occupancy (many)

Filter Direction

Single direction from Dim_Animal_Type to Fact_Occupancy

Join Key

Dim_Animal_Type.AnimalTypeID = Fact_Occupancy.AnimalTypeID

---

## Fact_Confirmation → Dim_Centre

Relationship

One-to-many

Cardinality

Dim_Centre (1) to Fact_Confirmation (many)

Filter Direction

Single direction from Dim_Centre to Fact_Confirmation

Join Key

Dim_Centre.CentreID = Fact_Confirmation.CentreID

---

## Fact_Confirmation → Dim_Date

Relationship

One-to-many

Cardinality

Dim_Date (1) to Fact_Confirmation (many)

Filter Direction

Single direction from Dim_Date to Fact_Confirmation

Join Key

Dim_Date.DateKey = Fact_Confirmation.DateKey

---

# SECTION 08 — VALIDATION NOTES

- Every decision is mapped to supporting signals and measures.
- Grain is defined before fact identification for each subject area.
- Dimensions are defined for centre, date, animal type, and region.
- Relationships form a star schema.
- The model supports the primary decision and the secondary operational questions.
