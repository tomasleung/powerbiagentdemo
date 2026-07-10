# OUTPUT 2 — SEMANTIC_MODEL_SPEC_AGENT_RUN_v1.0
## Animal Flow — Capacity Intelligence
### Semantic Model Specification

---

# Document Metadata

Document Type

Semantic Model Specification

Version

1.0

Artifact Type

Semantic Design Artifact

Owner

Data Architecture

Status

Draft

Purpose

Define the detailed semantic model design for Animal Flow capacity intelligence.

---

# SECTION 01 — FACT TABLE DEFINITIONS

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

Provides the core intake readiness and utilization measures.

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

Supports occupancy, species impact, and data trust measures.

---

## Fact_Confirmation

Description

Confirmation and freshness snapshot by centre and date.

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

Supports data trust and reliability decisions.

---

# SECTION 02 — DIMENSION TABLE DEFINITIONS

## Dim_Centre

Description

Master dimension for centre attributes and operational context.

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

---

## Dim_Date

Description

Date dimension for time-based analysis.

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

Animal type dimension for species-level analysis.

Key

AnimalTypeID

Attributes

- AnimalTypeName
- SpeciesCategory
- BreedGroup

---

## Dim_Region

Description

Region dimension for geographic analysis.

Key

RegionID

Attributes

- RegionName
- RegionType
- RegionManager

---

# SECTION 03 — COLUMN DEFINITIONS

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

Percentage of assignments that are validated and correct.

### SpeciesOccupancyImpact

Type

Decimal

Description

Impact of non-native species on available capacity for cats and dogs.

---

# SECTION 04 — RELATIONSHIP DEFINITIONS

## Dim_Centre → Fact_Capacity

Cardinality

One-to-many

Filter Direction

Dim_Centre to Fact_Capacity

Join Key

Dim_Centre.CentreID = Fact_Capacity.CentreID

---

## Dim_Date → Fact_Capacity

Cardinality

One-to-many

Filter Direction

Dim_Date to Fact_Capacity

Join Key

Dim_Date.DateKey = Fact_Capacity.DateKey

---

## Dim_Animal_Type → Fact_Capacity

Cardinality

One-to-many

Filter Direction

Dim_Animal_Type to Fact_Capacity

Join Key

Dim_Animal_Type.AnimalTypeID = Fact_Capacity.AnimalTypeID

---

## Dim_Centre → Fact_Occupancy

Cardinality

One-to-many

Filter Direction

Dim_Centre to Fact_Occupancy

Join Key

Dim_Centre.CentreID = Fact_Occupancy.CentreID

---

## Dim_Date → Fact_Occupancy

Cardinality

One-to-many

Filter Direction

Dim_Date to Fact_Occupancy

Join Key

Dim_Date.DateKey = Fact_Occupancy.DateKey

---

## Dim_Animal_Type → Fact_Occupancy

Cardinality

One-to-many

Filter Direction

Dim_Animal_Type to Fact_Occupancy

Join Key

Dim_Animal_Type.AnimalTypeID = Fact_Occupancy.AnimalTypeID

---

## Dim_Centre → Fact_Confirmation

Cardinality

One-to-many

Filter Direction

Dim_Centre to Fact_Confirmation

Join Key

Dim_Centre.CentreID = Fact_Confirmation.CentreID

---

## Dim_Date → Fact_Confirmation

Cardinality

One-to-many

Filter Direction

Dim_Date to Fact_Confirmation

Join Key

Dim_Date.DateKey = Fact_Confirmation.DateKey

---

# SECTION 05 — CARDINALITY & FILTER DIRECTION

- Fact_Capacity is filtered by Dim_Centre, Dim_Date, and Dim_Animal_Type.
- Fact_Occupancy is filtered by Dim_Centre, Dim_Date, and Dim_Animal_Type.
- Fact_Confirmation is filtered by Dim_Centre and Dim_Date.
- Dim_Region is used as an attribute in Dim_Centre to support regional filtering without additional many-to-many joins.

---

# SECTION 06 — IMPLEMENTATION NOTES

- Use star schema design for all facts and dimensions.
- Avoid snowflake relationships unless the design requires separate region master data.
- Keep filter direction single-direction from dimensions to facts for consistent analysis.
- Document measure definitions in the `MEASURE_CONTRACT` artifact.
- Use `DATA_MODEL_STANDARDS_v1.0` for naming, grain, and modeling rules.
