# TRD_v1.0.md
## Animal Flow — Capacity Intelligence
### Technical Requirements Document (TRD)

---

# Document Metadata

Document Type: Technical Requirements Document

Version: 1.0

Capability Name: Animal Flow — Capacity Intelligence

Artifact Type: TRD

Owner: Animal Flow

Status: Draft

Author: Tomas Leung

Related Documents

```text
BRD_AnimalFlow_Capacity_Intelligence_v1.0

REPORT_STORY_MATRIX_v1.0

REPORT_STORY_v1.0

MOCKUP_v1.0.md

MOCKUP_v1.0.svg
```

---

# SECTION 01 — Technical Summary

## Purpose

Provide a provincial operational dashboard to support:

```text
Animal Placement Decisions

Capacity Monitoring

Data Quality Monitoring

Species Occupancy Monitoring

Regional Capacity Oversight
```

---

## Primary Decision

```text
Which centres can safely receive additional animals?
```

---

## Primary Audience

```text
Animal Flow
```

---

## Secondary Audience

```text
Leadership

Operations Management

Regional Managers
```

---

## Decision Frequency

```text
Multiple Times Per Day
```

---

# SECTION 02 — Solution Architecture

## Source Systems

### Capacity Platform

Purpose

```text
Centre Capacity Information
```

Data Domains

```text
Care Capacity

Physical Capacity

Open Spaces

Occupancy
```

---

### ShelterBuddy

Purpose

```text
Animal Management
```

Data Domains

```text
Animals

Assignments

Species

Centre Occupancy
```

---

### Capacity Confirmation Data

Purpose

```text
Operational Confirmation Tracking
```

Data Domains

```text
Confirmation Status

Update Timestamps
```

---

## Reporting Platform

```text
Microsoft Fabric

Power BI
```

---

# SECTION 03 — Data Model

## Fact Tables

### Fact_Capacity

Purpose

Store capacity metrics by centre.

Columns

```text
CentreKey

DateKey

AnimalType

TotalSpaces

OpenSpaces

InUseSpaces

HoldSpaces

UnavailableSpaces

CareCapacity
```

---

### Fact_AnimalOccupancy

Purpose

Store occupancy information.

Columns

```text
AnimalId

CentreKey

AnimalType

SpeciesType

AssignmentStatus

SpaceType
```

---

### Fact_CentreConfirmation

Purpose

Store confirmation data.

Columns

```text
CentreKey

ConfirmationDate

ConfirmationStatus

UpdatedDateTime
```

---

## Dimension Tables

### Dim_Centre

Columns

```text
CentreKey

CentreName

Region

Location
```

---

### Dim_Date

Columns

```text
Date

Month

Quarter

Year
```

---

### Dim_AnimalType

Columns

```text
AnimalType

AnimalCategory
```

Values

```text
All

Cat

Dog

Rabbit

Small Animal

Other
```

---

### Dim_Region

Columns

```text
RegionName
```

Values

```text
Island

Interior

Lower Mainland

North
```

---

# SECTION 04 — Report Filters

## Animal Type

Purpose

Allow users to evaluate specific species.

Values

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

## Region

Purpose

Regional analysis.

Default

```text
All Regions
```

---

## Centre

Purpose

Centre-level review.

Default

```text
All Centres
```

---

# SECTION 05 — KPI CONTRACTS

## KPI — Centres At Capacity

Business Definition

Centres operating at or above configured care capacity.

Calculation

```DAX
Centres At Capacity =
COUNTROWS(
    FILTER(
        Centres,
        [Capacity Utilization %] >= 1
    )
)
```

Threshold

```text
>=100%
```

Status

```text
Red
```

Action

```text
Do Not Intake
```

---

## KPI — Available Centres

Business Definition

Centres currently below warning threshold.

Calculation

```DAX
Available Centres =
COUNTROWS(
    FILTER(
        Centres,
        [Capacity Utilization %] < .80
    )
)
```

Status

```text
Green
