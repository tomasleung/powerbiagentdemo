# SEMANTIC_MODEL_SPEC_v1.0
## Animal Flow — Live Capacity Reporting
### Semantic Model Specification

---

# Document Metadata

Document Type

```text
Semantic Model Specification
```

Version

```text
1.0
```

Capability Name

```text
Animal Flow — Live Capacity Reporting
```

Artifact Type

```text
SEMANTIC_MODEL_SPEC
```

Owner

```text
BI Architecture
```

Status

```text
Approved Test Run Output
```

Purpose

Define the detailed semantic model architecture required to support provincial capacity monitoring, intake readiness decisions, operational risk management, data quality monitoring, and regional capacity intelligence.

This document expands the approved:

```text
DATA_MODEL_MATRIX_v1.0
```

into a complete semantic architecture blueprint.

---

# Related Artifacts

```text
INPUT_BRD_AnimalFlow_LiveCapacity_v2.0.md

REPORT_STORY_MATRIX_v1.0.md

REPORT_STORY_v1.0.md

TRD_v1.0.md

DATA_MODEL_MATRIX_v1.0.md

DATA_MODEL_STANDARDS_v1.0.md
```

---

# SECTION 01 — MODEL OVERVIEW

## Capability Name

```text
Animal Flow — Live Capacity Reporting
```

---

## Business Purpose

```text
Provide a semantic model supporting
animal placement decisions,
capacity monitoring,
data quality validation,
and regional capacity management.
```

---

## Primary Decision Supported

```text
Which centres currently have sufficient
capacity to support incoming animals?
```

---

## Secondary Decisions Supported

```text
Which centres require intervention?

Which centres should be prioritized?

Which centres should be avoided?

Which centres have data quality concerns?

Which regions are experiencing capacity pressure?
```

---

## Architecture Pattern

```text
Star Schema
```

---

## Design Standards

```text
Decision-Driven BI Standards

Kimball Standards

Microsoft Fabric Standards

SQLBI Standards

Performance-Aware Modeling
```

---

## Semantic Modeling Objective

```text
Provide a reusable semantic layer
supporting operational reporting,
self-service analytics,
executive reporting,
and future Power BI solutions.
```

---

## Performance Note

```text
Use surrogate keys.

Keep fact tables narrow.

Minimize high-cardinality attributes.

Support Fabric Direct Lake readiness.
```

---

# SECTION 02 — SEMANTIC MODEL ARCHITECTURE

## Architecture Type

```text
Microsoft Fabric Semantic Model

Import / Direct Lake Ready
```

---

## Conceptual Architecture

```text
                    Dim_Date
                        │
                        ▼

Dim_Centre ─────── Fact_Capacity
      │
      │
      ├────────── Fact_Occupancy
      │
      │
      └────────── Fact_Confirmation

Dim_AnimalType
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

## Architecture Notes

```text
Star Schema

Conformed Dimensions

Single Direction Filtering

Shared Date Dimension

Shared Centre Dimension

Shared Animal Type Dimension
```

---

# SECTION 03 — FACT TABLE DEFINITIONS

## Fact_Capacity

### Business Name

```text
Capacity
```

---

### Description

```text
Capacity availability and utilization
snapshot by centre, date, and animal type.
```

---

### Business Purpose

```text
Support intake readiness,
capacity monitoring,
and utilization analysis.
```

---

### Business Grain

```text
One Centre

+

One Reporting Date

+

One Animal Type
```

---

### Source Systems

```text
CAT Master

DOG Master

Live Capacity Management
```

---

### Supported Decisions

```text
Intake Readiness

Placement Prioritization

Capacity Monitoring
```

---

### Supported Measures

```text
Total DOG Spaces

Open DOG Spaces

Total CAT Spaces

Open CAT Spaces

DOG Utilization %

CAT Utilization %

Remaining Capacity
```

---

### Fact Columns

```text
CentreID

DateKey

AnimalTypeKey

TotalCapacity

OpenCapacity

OccupiedCapacity

CapacityUtilizationPct

EmergencyClosureFlag

PlacementReadinessFlag
```

---

## Fact_Occupancy

### Business Name

```text
Occupancy
```

---

### Description

```text
Animal occupancy and operational
assignment snapshot.
```

---

### Business Purpose

```text
Support placement decisions,
operational review,
and data quality monitoring.
```

---

### Business Grain

```text
One Centre

+

One Reporting Date

+

One Animal Type
```

---

### Source Systems

```text
ShelterBuddy
```

---

### Supported Measures

```text
Animals In Care

Missing Kennel Assignments

Assignment Accuracy %

Species Occupancy Impact
```

---

### Fact Columns

```text
CentreID

DateKey

AnimalTypeKey

AnimalsInCare

MissingAssignments

AssignmentAccuracyPct

OtherSpeciesOccupancy

SpeciesOccupancyImpact
```

---

## Fact_Confirmation

### Business Name

```text
Capacity Confirmation
```

---

### Description

```text
Operational update
and data freshness tracking.
```

---

### Business Purpose

```text
Support governance review,
data confidence,
and operational compliance.
```

---

### Business Grain

```text
One Centre

+

One Reporting Date

+

One Confirmation Event
```

---

### Source Systems

```text
Power App
```

---

### Supported Measures

```text
Capacity Confirmation Rate

Stale Updates

Update Freshness
```

---

### Fact Columns

```text
CentreID

DateKey

ConfirmationStatus

UpdateTimestamp

UpdateAgeHours

StaleUpdateFlag
```

---

# FACT INVENTORY SUMMARY

| Fact Table | Business Grain |
|------------|------------|
| Fact_Capacity | Centre + Date + Animal Type |
| Fact_Occupancy | Centre + Date + Animal Type |
| Fact_Confirmation | Centre + Date + Confirmation Event |

---

# SECTION 04 — DIMENSION TABLE DEFINITIONS

## Dim_Centre

### Business Purpose

```text
Provide centre-level reporting context.
```

---

### Primary Key

```text
CentreID
```

---

### Dimension Attributes

```text
CentreID

CentreCode

CentreName

CentreType

RegionID

OperatingStatus
```

---

### Facts Supported

```text
Fact_Capacity

Fact_Occupancy

Fact_Confirmation
```

---

## Dim_Date

### Business Purpose

```text
Provide standard time intelligence.
```

---

### Primary Key

```text
DateKey
```

---

### Dimension Attributes

```text
Date

Week

Month

Quarter

Year

FiscalPeriod
```

---

### Facts Supported

```text
Fact_Capacity

Fact_Occupancy

Fact_Confirmation
```

---

## Dim_AnimalType

### Business Purpose

```text
Provide animal type segmentation.
```

---

### Primary Key

```text
AnimalTypeKey
```

---

### Dimension Attributes

```text
AnimalType

AnimalCategory
```

---

### Facts Supported

```text
Fact_Capacity

Fact_Occupancy
```

---

## Dim_Region

### Business Purpose

```text
Provide regional reporting context.
```

---

### Primary Key

```text
RegionID
```

---

### Dimension Attributes

```text
RegionID

RegionName

OperationalArea

Province
```

---

### Facts Supported

```text
Fact_Capacity

Fact_Occupancy
```

---

# SECTION 05 — KEY COLUMN SPECIFICATIONS

## CapacityUtilizationPct

### Data Type

```text
Decimal
```

---

### Description

```text
Percentage of capacity currently occupied.
```

---

### Business Rule

```text
Occupied Capacity

÷

Total Capacity
```

---

## RemainingCapacity

### Data Type

```text
Whole Number
```

---

### Description

```text
Available capacity remaining.
```

---

### Business Rule

```text
Total Capacity

-

Animals In Care
```

---

## AssignmentAccuracyPct

### Data Type

```text
Decimal
```

---

### Description

```text
Percentage of correctly assigned animals.
```

---

## UpdateAgeHours

### Data Type

```text
Whole Number
```

---

### Description

```text
Hours since last capacity confirmation.
```

---

# SECTION 06 — RELATIONSHIP DEFINITIONS

## Relationship 01

### Parent Table

```text
Dim_Centre
```

### Child Table

```text
Fact_Capacity
```

### Join Key

```text
CentreID
```

### Cardinality

```text
One-To-Many
```

### Filter Direction

```text
Single Direction
```

---

## Relationship 02

```text
Dim_Date → Fact_Capacity

DateKey

One-To-Many

Single Direction
```

---

## Relationship 03

```text
Dim_AnimalType → Fact_Capacity

AnimalTypeKey

One-To-Many

Single Direction
```

---

## Relationship 04

```text
Dim_Centre → Fact_Occupancy

CentreID

One-To-Many

Single Direction
```

---

## Relationship 05

```text
Dim_Date → Fact_Occupancy

DateKey

One-To-Many

Single Direction
```

---

## Relationship 06

```text
Dim_AnimalType → Fact_Occupancy

AnimalTypeKey

One-To-Many

Single Direction
```

---

## Relationship 07

```text
Dim_Centre → Fact_Confirmation

CentreID

One-To-Many

Single Direction
```

---

## Relationship 08

```text
Dim_Date → Fact_Confirmation

DateKey

One-To-Many

Single Direction
```

---

## Relationship 09

```text
Dim_Region → Dim_Centre

RegionID

One-To-Many

Single Direction
```

---

# SECTION 07 — CARDINALITY & FILTER STRATEGY

## Default Pattern

```text
One-To-Many

Single Direction

Dimension → Fact
```

---

## Exceptions

```text
None Currently Identified
```

---

# SECTION 08 — CONFORMED DIMENSIONS

## Shared Dimensions

```text
Dim_Centre

Dim_Date

Dim_AnimalType
```

---

## Governance Rules

```text
Consistent Naming

Consistent Definitions

Consistent Hierarchies

Reusable Across Facts
```

---

# SECTION 09 — HIERARCHY DESIGN

## Location Hierarchy

```text
Region

↓

Centre
```

---

## Calendar Hierarchy

```text
Year

↓

Quarter

↓

Month

↓

Date
```

---

# SECTION 10 — SECURITY MODEL SUPPORT

## Security Dimensions

```text
Dim_Centre

Dim_Region
```

---

## Future RLS Support

```text
Regional Security

Centre Manager Security

Executive Reporting Access
```

---

# SECTION 11 — PERFORMANCE DESIGN

## Optimization Strategy

```text
Star Schema

Conformed Dimensions

Single Direction Filtering

Explicit Measures

Surrogate Keys
```

---

## Performance Rules

```text
Keep Fact Tables Narrow

Avoid Text In Facts

Use Integer Keys

Limit High Cardinality Attributes

Avoid Many-To-Many Relationships
```

---

# SECTION 12 — AI READINESS

## Documentation Requirements

```text
Every Fact Has A Grain

Every Dimension Has A Business Purpose

Every Relationship Has A Business Purpose

Every Measure Has Traceability
```

---

## AI Readiness Goal

```text
An AI agent can explain:

Why the fact exists

Why the dimension exists

Which decision is supported

Which measures are available
```

---

# SECTION 13 — DECISION COVERAGE

| Decision | Supporting Facts |
|-----------|-----------|
| Intake Readiness | Fact_Capacity |
| Placement Prioritization | Fact_Capacity, Fact_Occupancy |
| Data Confidence | Fact_Occupancy, Fact_Confirmation |
| Regional Monitoring | Fact_Capacity |

---

# SECTION 14 — SIGNAL COVERAGE

| Signal | Supporting Fact |
|----------|----------|
| Open Capacity | Fact_Capacity |
| Utilization | Fact_Capacity |
| Assignment Accuracy | Fact_Occupancy |
| Confirmation Status | Fact_Confirmation |
| Regional Capacity | Fact_Capacity |

---

# SECTION 15 — MODEL VALIDATION

```text
✓ Star Schema Implemented

✓ Facts Defined

✓ Dimensions Defined

✓ Grain Defined

✓ Columns Defined

✓ Relationships Defined

✓ Cardinality Defined

✓ Decision Coverage Complete

✓ Signal Coverage Complete

✓ Fabric Ready

✓ AI Ready
```

---

# SECTION 16 — HANDOFF TO MEASURE_CONTRACT

## Output

```text
MEASURE_CONTRACT_v1.0.md
```

---

## Purpose

```text
Define Business Definitions

Define Business Logic

Define Thresholds

Define Actions

Define Ownership

Define Measure Governance
```

---

# SUCCESS STATEMENT

The Semantic Model Specification succeeds when:

```text
Every Fact

has a declared grain.

Every Dimension

provides business context.

Every Relationship

supports navigation.

Every Measure

has a governed source.

Every Decision

is supported by the semantic model.
```

The Semantic Model Specification becomes:

```text
The Semantic Architecture Contract
```

between:

```text
Technical Design

↓

Semantic Design

↓

Semantic Build
```