# OUTPUT 2 — SEMANTIC_MODEL_SPEC_AGENT_RUN_v2.0
## Animal Flow — Capacity Intelligence
### Semantic Model Specification

---

# Document Metadata

Document Type

Semantic Model Specification

Version

2.0

Artifact Type

Semantic Design Artifact

Owner

Data Architecture

Status

Draft

Purpose

Define the detailed semantic model design for Animal Flow capacity intelligence with performance-aware modeling guidance.

---

# SECTION 01 — MODEL OVERVIEW

Architecture Pattern

Star Schema

Design Standards

- Decision-Driven BI Standards
- Kimball Standards
- Microsoft Fabric Standards
- SQLBI Standards
- Performance-Aware Modeling

Primary Decision Supported

Which centres can safely receive additional animals?

Performance Note

Favor numeric surrogate keys and avoid wide fact payloads in the semantic model.

---

# SECTION 02 — FACT TABLE DEFINITIONS

## Fact_Capacity

Description

Capacity snapshot by centre, date, and animal type.

Grain

Centre + Date + Animal Type

Columns

- CentreID
- DateKey
- AnimalTypeID
- CareCapacity
- PhysicalCapacity
- OpenSpaces
- TotalSpaces
- SpaceUtilizationPct
- RemainingCapacity
- AvailableCentreFlag
- CentreAtCapacityFlag
- EmergencyClosureFlag

Source

Capacity Platform

Notes

Provides core intake readiness and utilization measures.

---

## Fact_Occupancy

Description

Occupancy snapshot by centre, date, and animal type.

Grain

Centre + Date + Animal Type

Columns

- CentreID
- DateKey
- AnimalTypeID
- AnimalsInCare
- CatsInCare
- DogsInCare
- OtherAnimals
- MissingAssignments
- AssignmentAccuracyPct
- SpeciesOccupancyImpact

Source

ShelterBuddy

Notes

Supports occupancy, species impact, and assignment quality measures.

---

## Fact_Confirmation

Description

Confirmation status snapshot by centre and date.

Grain

Centre + Date

Columns

- CentreID
- DateKey
- ConfirmationStatus
- PendingConfirmationCount
- StaleUpdateFlag
- UpdateFreshnessHours

Source

Capacity Confirmation Process

Notes

Supports data trust and freshness validation.

---

# SECTION 03 — DIMENSION TABLE DEFINITIONS

## Dim_Centre

Description

Master dimension for centre attributes.

Key

CentreID

Attributes

- CentreName
- CentreType
- RegionID
- RegionName
- PhysicalCapacity
- CentreStatus
- Address
- OperatingHours
- FacilityStatus

Notes

Region values are captured as attributes to avoid unnecessary 2nd-degree joins.

---

## Dim_Date

Description

Date dimension for time analysis.

Key

DateKey

Attributes

- FullDate
- DayOfWeek
- WeekOfYear
- MonthName
- Quarter
- Year
- FiscalPeriod

---

## Dim_Animal_Type

Description

Animal type dimension for species analysis.

Key

AnimalTypeID

Attributes

- AnimalTypeName
- SpeciesCategory
- BreedGroup

---

## Dim_Region

Description

Region dimension for geographic reporting.

Key

RegionID

Attributes

- RegionName
- RegionType
- RegionManager

Notes

This dimension is optional if region is modeled as an attribute on `Dim_Centre`, but it is included here for regional reporting clarity.

---

# SECTION 04 — COLUMN DEFINITIONS

## Fact Columns

### CareCapacity

Type

Decimal

Description

Available care capacity for the centre and animal type.

### RemainingCapacity

Type

Decimal

Description

CareCapacity minus AnimalsInCare.

### CapacityUtilizationPct

Type

Decimal

Description

Percentage of care capacity currently occupied.

### AssignmentAccuracyPct

Type

Decimal

Description

Percentage of validated assignments.

### SpeciesOccupancyImpact

Type

Decimal

Description

Impact of non-native species on available capacity.

---

# SECTION 05 — RELATIONSHIP DEFINITIONS

## Dim_Centre → Fact_Capacity

Cardinality

One-to-many

Filter Direction

Single-direction from Dim_Centre to Fact_Capacity

Join Key

Dim_Centre.CentreID = Fact_Capacity.CentreID

---

## Dim_Date → Fact_Capacity

Cardinality

One-to-many

Filter Direction

Single-direction from Dim_Date to Fact_Capacity

Join Key

Dim_Date.DateKey = Fact_Capacity.DateKey

---

## Dim_Animal_Type → Fact_Capacity

Cardinality

One-to-many

Filter Direction

Single-direction from Dim_Animal_Type to Fact_Capacity

Join Key

Dim_Animal_Type.AnimalTypeID = Fact_Capacity.AnimalTypeID

---

## Dim_Centre → Fact_Occupancy

Cardinality

One-to-many

Filter Direction

Single-direction from Dim_Centre to Fact_Occupancy

Join Key

Dim_Centre.CentreID = Fact_Occupancy.CentreID

---

## Dim_Date → Fact_Occupancy

Cardinality

One-to-many

Filter Direction

Single-direction from Dim_Date to Fact_Occupancy

Join Key

Dim_Date.DateKey = Fact_Occupancy.DateKey

---

## Dim_Animal_Type → Fact_Occupancy

Cardinality

One-to-many

Filter Direction

Single-direction from Dim_Animal_Type to Fact_Occupancy

Join Key

Dim_Animal_Type.AnimalTypeID = Fact_Occupancy.AnimalTypeID

---

## Dim_Centre → Fact_Confirmation

Cardinality

One-to-many

Filter Direction

Single-direction from Dim_Centre to Fact_Confirmation

Join Key

Dim_Centre.CentreID = Fact_Confirmation.CentreID

---

## Dim_Date → Fact_Confirmation

Cardinality

One-to-many

Filter Direction

Single-direction from Dim_Date to Fact_Confirmation

Join Key

Dim_Date.DateKey = Fact_Confirmation.DateKey

---

# SECTION 06 — CARDINALITY & FILTER DIRECTION

- Fact_Capacity is filtered by Dim_Centre, Dim_Date, and Dim_Animal_Type.
- Fact_Occupancy is filtered by Dim_Centre, Dim_Date, and Dim_Animal_Type.
- Fact_Confirmation is filtered by Dim_Centre and Dim_Date.
- Dim_Region is available for regional reporting without forcing extra many-to-many joins.

---

# SECTION 07 — IMPLEMENTATION NOTES

- Use star schema design for query efficiency.
- Use single-direction relationships unless bidirectional filtering is required by a business scenario.
- Keep fact tables narrow and remove unnecessary payload columns.
- Use numeric surrogate keys for all dimension primary keys.
- Document measure definitions in the `MEASURE_CONTRACT` artifact.
- Apply `DATA_MODEL_STANDARDS_v1.0` naming and grain rules.
