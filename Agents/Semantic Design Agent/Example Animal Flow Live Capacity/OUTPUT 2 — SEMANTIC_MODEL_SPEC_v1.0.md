# SEMANTIC_MODEL_SPEC_v1.0
## Animal Flow — Capacity Intelligence

---

# SECTION 01 — MODEL OVERVIEW

Architecture Pattern

Star Schema

Design Standards

- Decision-Driven BI Standards
- Kimball Standards
- Microsoft Fabric Standards
- SQLBI Standards

Primary Decision Supported

Which centres can safely receive additional animals?

---

# SECTION 02 — FACT TABLES

## Fact_Capacity

Purpose

Store operational capacity metrics.

Grain

One Centre
+
One Date
+
One Animal Type

Columns

- CapacityKey (Whole Number)
- CentreKey (Whole Number)
- DateKey (Whole Number)
- AnimalTypeKey (Whole Number)
- CareCapacity (Decimal)
- OpenSpaces (Whole Number)
- InUseSpaces (Whole Number)
- HoldSpaces (Whole Number)
- UnavailableSpaces (Whole Number)
- SnapshotDateTime (DateTime)

---

## Fact_Occupancy

Purpose

Store animal occupancy details.

Grain

One Animal
+
One Centre
+
One Date

Columns

- OccupancyKey (Whole Number)
- AnimalID (Text)
- CentreKey (Whole Number)
- DateKey (Whole Number)
- AnimalTypeKey (Whole Number)
- SpeciesType (Text)
- AssignmentStatus (Text)
- AssignedSpaceType (Text)
- OccupancyDateTime (DateTime)

---

## Fact_Confirmation

Purpose

Store confirmation status and freshness information.

Grain

One Centre
+
One Confirmation Event

Columns

- ConfirmationKey (Whole Number)
- CentreKey (Whole Number)
- DateKey (Whole Number)
- ConfirmationStatus (Text)
- ConfirmationDateTime (DateTime)
- UpdatedBy (Text)
- UpdateAgeHours (Decimal)

---

# SECTION 03 — DIMENSIONS

## Dim_Centre

Columns

- CentreKey (Whole Number)
- CentreCode (Text)
- CentreName (Text)
- RegionKey (Whole Number)
- City (Text)
- ActiveFlag (Boolean)

---

## Dim_Date

Columns

- DateKey (Whole Number)
- Date (Date)
- Year (Whole Number)
- Quarter (Whole Number)
- MonthNumber (Whole Number)
- MonthName (Text)
- WeekNumber (Whole Number)
- DayOfWeek (Text)

---

## Dim_Animal_Type

Columns

- AnimalTypeKey (Whole Number)
- AnimalType (Text)
- AnimalCategory (Text)

Values

- Cat
- Dog
- Rabbit
- Small Animal
- Other

---

## Dim_Region

Columns

- RegionKey (Whole Number)
- RegionName (Text)

Values

- Interior
- Island
- Lower Mainland
- North

---

# SECTION 04 — RELATIONSHIPS

Relationship 01

Dim_Centre
→
Fact_Capacity

Cardinality

One-To-Many

Filter Direction

Single

---

Relationship 02

Dim_Centre
→
Fact_Occupancy

One-To-Many

Single

---

Relationship 03

Dim_Centre
→
Fact_Confirmation

One-To-Many

Single

---

Relationship 04

Dim_Date
→
Fact_Capacity

One-To-Many

Single

---

Relationship 05

Dim_Date
→
Fact_Occupancy

One-To-Many

Single

---

Relationship 06

Dim_Date
→
Fact_Confirmation

One-To-Many

Single

---

Relationship 07

Dim_Animal_Type
→
Fact_Capacity

One-To-Many

Single

---

Relationship 08

Dim_Animal_Type
→
Fact_Occupancy

One-To-Many

Single

---

Relationship 09

Dim_Region
→
Dim_Centre

One-To-Many

Single

---

# SECTION 05 — MODEL DIAGRAM

Dim_Region
      │
      ▼

Dim_Centre ─────► Fact_Capacity
      │
      ├───────► Fact_Occupancy
      │
      └───────► Fact_Confirmation

Dim_Date
      │
      ├───────► Fact_Capacity
      ├───────► Fact_Occupancy
      └───────► Fact_Confirmation

Dim_Animal_Type
      │
      ├───────► Fact_Capacity
      └───────► Fact_Occupancy

---

# SECTION 06 — COMPLIANCE REVIEW

✓ Star Schema

✓ Single Direction Relationships

✓ No Many-To-Many

✓ Explicit Measures Required

✓ AI Ready Documentation Required

Next Deliverable

MEASURE_CONTRACT_v1.0
