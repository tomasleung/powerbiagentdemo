# Technical Requirements Document (TRD)
## Animal Flow — Capacity Intelligence

---

# Document Metadata

Document Type: TRD

Capability Name: Animal Flow — Capacity Intelligence

Version: 1.0

Status: Draft

Owner: Animal Flow

Author: Tomas Leung

Related BRD:
BRD_AnimalFlow_Capacity_Intelligence_v1.0

Related DSC:
REPORT_STORY_v1.2

---

# SECTION 01 — Technical Summary

## Purpose

Provide a provincial capacity intelligence dashboard that supports:

- Intake readiness
- Capacity monitoring
- Data quality monitoring
- Species occupancy analysis
- Regional capacity oversight

---

## Users

### Animal Flow

Primary User

Responsibilities

- Placement decisions
- Capacity monitoring
- Operational intervention

---

### Leadership

Secondary User

Responsibilities

- Regional monitoring
- Capacity planning
- Exception review

---

# SECTION 02 — Data Architecture

## Fact Tables

### Fact_Capacity

Purpose

Store centre-level capacity metrics.

Key Columns

- Centre Key
- Date Key
- Animal Type
- Total Spaces
- Open Spaces
- In Use Spaces
- Hold Spaces
- Unavailable Spaces

---

### Fact_AnimalAssignment

Purpose

Store occupancy details.

Key Columns

- Animal ID
- Centre Key
- Animal Type
- Species Category
- Kennel Assignment
- Assignment Status

---

### Fact_CentreConfirmation

Purpose

Store capacity confirmation information.

Key Columns

- Centre Key
- Confirmation Status
- Confirmation DateTime

---

## Dimensions

### Dim_Centre

- Centre Name
- Region
- Centre Manager

### Dim_Date

- Date
- Week
- Month
- Year

### Dim_AnimalType

- All
- Cat
- Dog
- Rabbit
- Small Animal
- Other

### Dim_Region

- Island
- Lower Mainland
- Interior
- North

---

# SECTION 03 — Report Filters

## Animal Type

Values

- All
- Cat
- Dog
- Rabbit
- Small Animal
- Other

Default

All

---

## Region

Values

All Regions

---

## Centre

Values

All Centres

---

# SECTION 04 — KPI Contracts

## KPI — Centres At Capacity

Business Definition

Centres operating at or above configured care capacity.

Formula

At Capacity =
Animals In Care >= Care Capacity

Threshold

Red

>=100%

---

## KPI — Available Centres

Business Definition

Centres below warning threshold.

Formula

Animals In Care / Care Capacity < 80%

---

## KPI — Data Quality Issues

Business Definition

Count of centres with one or more unresolved quality issues.

Formula

Missing Assignment Count > 0
OR
Confirmation Status = Pending

---

## KPI — Remaining Capacity

Business Definition

Remaining intake capacity.

Formula

Care Capacity
-
Animals In Care

---

## KPI — Species Occupancy Impact

Business Definition

CAT/DOG spaces occupied by non-target species.

Formula

Count Other Species Occupying Primary Species Spaces

---

# SECTION 05 — Visual Inventory

## Section 00

Operational Snapshot

Visual Type

KPI Cards

Metrics

- Total Centres
- Animals In Care
- Care Capacity
- Open Spaces
- CAT Spaces
- DOG Spaces

---

## Section 01

Action Required

Visual Type

Exception KPI Cards

Metrics

- Centres At Capacity
- Data Quality Issues
- Pending Confirmations
- Emergency Closures

---

## Section 02

Intake Readiness

Visual Type

Status Cards

Metrics

- Available Centres
- Monitor Centres
- Full Centres
- Closed Centres

---

## Section 03

Placement Decision Board

Visual Type

Table

Columns

- Centre
- Animals In Care
- Care Capacity
- Remaining Capacity
- Open Spaces
- Recommendation

Sort

Remaining Capacity DESC

---

## Section 04

Capacity vs Occupancy

Visual Type

KPI Cards + Composition Chart

Metrics

- Animals In Care
- Care Capacity
- Remaining Capacity
- Utilization %

---

## Section 05

Species Occupancy

Visual Type

Breakdown Chart

Metrics

- Cats In Care
- Dogs In Care
- Other Animals
- CAT Spaces Used by Other Animals
- DOG Spaces Used by Other Animals

---

## Section 06

Data Trust

Visual Type

Exception Cards

Metrics

- Missing Assignments
- Accuracy %
- Pending Confirmation
- Stale Updates

---

## Section 07

Regional Health

Visual Type

Horizontal Bar Chart

Metrics

- Regional Utilization %
- Regional Capacity %
- Regional Open Space %

---

## Section 08

AI Operational Briefing

Status

Future Phase

Implementation

Pending

---

# SECTION 06 — DAX Measure Inventory

## Animals In Care

```DAX
Animals In Care =
COUNTROWS ( Fact_AnimalAssignment )
```

---

## Remaining Capacity

```DAX
Remaining Capacity =
[Care Capacity]
-
[Animals In Care]
```

---

## Capacity Utilization %

```DAX
Capacity Utilization % =
DIVIDE(
    [Animals In Care],
    [Care Capacity]
)
```

---

## Centres At Capacity

```DAX
Centres At Capacity =
COUNTROWS(
    FILTER(
        Centres,
        [Capacity Utilization %] >= 1
    )
)
```

---

# SECTION 07 — Drill Through Design

## Dashboard

Capacity Intelligence

↓

## Centre Detail

Selected Centre

↓

## Live Capacity Management

Power App

↓

## ShelterBuddy

Animal Detail

---

# SECTION 08 — Refresh Requirements

Refresh Frequency

Every 30 Minutes

---

Data Sources

- Capacity Platform
- ShelterBuddy Extract
- Centre Confirmation Data

---

# SECTION 09 — Security

## Animal Flow

Access

All Centres

---

## Leadership

Access

All Centres

---

## Centre Managers (Future)

Access

Assigned Centre Only

---

# SECTION 10 — Validation Rules

## Capacity Validation

Open + In Use + Hold + Unavailable

Must equal

Total Spaces

---

## Care Capacity Validation

Animals In Care

Must not be negative

---

## Assignment Validation

Missing Assignment Count

Must reconcile with ShelterBuddy extract

---

# SECTION 11 — Acceptance Criteria

Dashboard loads successfully.

All KPIs match source systems.

Filters operate correctly.

Animal Type filtering operates correctly.

Placement Decision Board sorts correctly.

Regional metrics reconcile correctly.

Dashboard supports operational decision making within 30 seconds.

---

# SECTION 12 — Deployment Checklist

□ Semantic model approved

□ Measures validated

□ KPI contracts approved

□ Security validated

□ Deployment completed

□ User acceptance testing completed

□ Production signoff received