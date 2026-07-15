# DATA_MODEL_MATRIX_v1.0
## Animal Flow — Live Capacity Reporting
### Semantic Design Validation Matrix

---

# Document Metadata

Document Type

```text
Data Model Matrix
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
DATA_MODEL_MATRIX
```

Owner

```text
Animal Flow / BI Architecture
```

Status

```text
Approved Test Run Output
```

Purpose

Validate the business structure of the semantic model before detailed semantic architecture, column design, relationship design, and measure governance activities begin.

This document serves as the bridge between:

```text
REPORT_STORY

↓

TRD

↓

Semantic Design
```

and ensures every semantic object has a valid business purpose.

---

# Related Artifacts

```text
INPUT_BRD_AnimalFlow_LiveCapacity_v2.0.md

REPORT_STORY_MATRIX_v1.0.md

REPORT_STORY_v1.0.md

TRD_v1.0.md

DATA_MODEL_STANDARDS_v1.0.md
```

---

# SECTION 01 — DECISION MODEL VALIDATION

## Primary Decision

```text
Which centres currently have sufficient capacity
to support incoming animals?
```

---

## Secondary Decisions

```text
Which centres require intervention?

Which centres should be prioritized for intake?

Which centres should be avoided for intake?

Which centres have data quality concerns?

Which regions are experiencing capacity pressure?
```

---

## Decision Owner

```text
Animal Flow Team
```

---

## Decision Frequency

```text
Multiple Times Daily
```

---

## Semantic Modeling Goal

The semantic model must support placement readiness decisions, operational monitoring, regional capacity management, and data quality review without requiring users to manually interpret raw operational data.

---

# SECTION 02 — BUSINESS SIGNAL INVENTORY

## Provincial Snapshot Signals

```text
Total DOG Spaces

Open DOG Spaces

Total CAT Spaces

Open CAT Spaces

DOG Utilization %

CAT Utilization %
```

---

## Intake Readiness Signals

```text
Open DOG Spaces

Open CAT Spaces

DOG Utilization %

CAT Utilization %

Emergency Closure Status

Placement Readiness
```

---

## Data Trust Signals

```text
Missing Kennel Assignments

Assignment Accuracy %

Capacity Confirmation Status

Last Capacity Update

ShelterBuddy Last Sync
```

---

## Operational Risk Signals

```text
DOG Utilization %

CAT Utilization %

Emergency Closure Status

Capacity Confirmation Status
```

---

## Regional Signals

```text
Regional Utilization %

Regional Capacity %

Regional Open Capacity %
```

---

# SECTION 03 — MEASURE INVENTORY

## Capacity Measures

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

## Placement Measures

```text
Available Centres

Centres At Capacity

Placement Readiness

Emergency Closure Count
```

---

## Data Quality Measures

```text
Missing Kennel Assignments

Assignment Accuracy %

Capacity Confirmation Rate

Stale Updates
```

---

## Regional Measures

```text
Regional Utilization %

Regional Capacity %

Regional Open Capacity %
```

---

# SECTION 04 — DECISION → QUESTION → SIGNAL → MEASURE MATRIX

| Decision | Business Question | Signal | Measure |
|-----------|-----------|-----------|-----------|
| Intake Readiness | Which centres can receive animals? | Open DOG Spaces | Open DOG Spaces |
| Intake Readiness | Which centres can receive animals? | Open CAT Spaces | Open CAT Spaces |
| Intake Readiness | Which centres can receive animals? | Placement Readiness | Remaining Capacity |
| Operational Risk | Which centres require intervention? | DOG Utilization % | DOG Utilization % |
| Operational Risk | Which centres require intervention? | CAT Utilization % | CAT Utilization % |
| Data Confidence | Can the data be trusted? | Missing Assignments | Missing Kennel Assignments |
| Data Confidence | Can the data be trusted? | Assignment Accuracy % | Assignment Accuracy % |
| Governance | Is capacity information current? | Confirmation Status | Capacity Confirmation Rate |
| Regional Health | Where is pressure building? | Regional Utilization % | Regional Utilization % |
| Regional Health | Where is pressure building? | Regional Open Capacity % | Regional Open Capacity % |

---

# SECTION 05 — GRAIN ANALYSIS

## Capacity Grain

### Business Grain

```text
One Centre

+

One Reporting Date

+

One Animal Type
```

---

### Example Row

```text
Vancouver Centre

DOG

2026-07-01
```

---

### Target Fact

```text
Fact_Capacity
```

---

### Business Purpose

```text
Store centre-level capacity availability
and utilization metrics.
```

---

## Occupancy Grain

### Business Grain

```text
One Centre

+

One Reporting Date

+

One Animal Type
```

---

### Example Row

```text
Vancouver Centre

CAT

2026-07-01
```

---

### Target Fact

```text
Fact_Occupancy
```

---

### Business Purpose

```text
Store occupancy measures and animal assignment metrics.
```

---

## Confirmation Grain

### Business Grain

```text
One Centre

+

One Reporting Date

+

One Confirmation Event
```

---

### Example Row

```text
Kamloops Centre

Capacity Confirmation

2026-07-01
```

---

### Target Fact

```text
Fact_Confirmation
```

---

### Business Purpose

```text
Store operational update status and confirmation metrics.
```

---

# SECTION 06 — FACT IDENTIFICATION MATRIX

## Fact_Capacity

### Business Purpose

```text
Store capacity availability, utilization,
and intake readiness metrics.
```

---

### Business Grain

```text
Centre

+

Date

+

Animal Type
```

---

### Supports Decisions

```text
Intake Readiness

Placement Prioritization

Capacity Monitoring
```

---

### Supports Signals

```text
Open DOG Spaces

Open CAT Spaces

DOG Utilization %

CAT Utilization %
```

---

### Supports Measures

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

### Source Systems

```text
CAT Master

DOG Master

Live Capacity Management
```

---

## Fact_Occupancy

### Business Purpose

```text
Store occupancy, assignment,
and animal placement measures.
```

---

### Business Grain

```text
Centre

+

Date

+

Animal Type
```

---

### Supports Decisions

```text
Placement Readiness

Operational Risk

Data Confidence
```

---

### Supports Signals

```text
Animals In Care

Missing Assignments

Assignment Accuracy %
```

---

### Supports Measures

```text
Animals In Care

Missing Kennel Assignments

Assignment Accuracy %

Placement Readiness
```

---

### Source Systems

```text
ShelterBuddy
```

---

## Fact_Confirmation

### Business Purpose

```text
Store operational update
and confirmation metrics.
```

---

### Business Grain

```text
Centre

+

Date

+

Confirmation Event
```

---

### Supports Decisions

```text
Governance Review

Data Confidence
```

---

### Supports Signals

```text
Capacity Confirmation Status

Stale Updates

Update Freshness
```

---

### Supports Measures

```text
Capacity Confirmation Rate

Stale Updates
```

---

### Source Systems

```text
Power App
```

---

# SECTION 07 — DIMENSION IDENTIFICATION MATRIX

## Dim_Centre

### Business Purpose

```text
Provide centre-level reporting context.
```

---

### Key Attributes

```text
Centre Name

Centre Code

Centre Type

Region

Operating Status
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
Provide time intelligence and trend analysis.
```

---

### Key Attributes

```text
Date

Week

Month

Quarter

Year
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
Provide capacity segmentation
by animal type.
```

---

### Key Attributes

```text
DOG

CAT
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

### Key Attributes

```text
Region

Operational Area

Province
```

---

### Facts Supported

```text
Fact_Capacity

Fact_Occupancy
```

---

# SECTION 08 — FACT TO DIMENSION MATRIX

| Fact Table | Connected Dimensions |
|------------|------------|
| Fact_Capacity | Dim_Centre, Dim_Date, Dim_AnimalType |
| Fact_Occupancy | Dim_Centre, Dim_Date, Dim_AnimalType |
| Fact_Confirmation | Dim_Centre, Dim_Date |
| Dim_Region | Connected Through Dim_Centre |

---

# SECTION 09 — SEMANTIC MODEL BLUEPRINT

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
Star Schema Architecture

Conformed Dimensions

Single Direction Filtering

Decision-Driven Measures

Fabric Optimized Design
```

---

# SECTION 10 — CONFORMED DIMENSION REVIEW

| Dimension | Fact Tables Using Dimension |
|------------|------------|
| Dim_Centre | Fact_Capacity, Fact_Occupancy, Fact_Confirmation |
| Dim_Date | Fact_Capacity, Fact_Occupancy, Fact_Confirmation |
| Dim_AnimalType | Fact_Capacity, Fact_Occupancy |

---

# SECTION 11 — BUSINESS QUESTION COVERAGE

| Business Question | Signal Exists | Measure Exists | Fact Exists | Dimension Exists |
|------------|------------|------------|------------|------------|
| Which centres can receive animals? | Yes | Yes | Yes | Yes |
| Which centres require intervention? | Yes | Yes | Yes | Yes |
| Can the information be trusted? | Yes | Yes | Yes | Yes |
| Where is pressure building? | Yes | Yes | Yes | Yes |

---

# SECTION 12 — DECISION COVERAGE

| Decision | Coverage Status |
|------------|------------|
| Intake Readiness | Complete |
| Operational Intervention | Complete |
| Placement Prioritization | Complete |
| Data Quality Review | Complete |
| Regional Monitoring | Complete |

---

# SECTION 13 — MODEL VALIDATION

## Validation Results

```text
✓ Primary Decision Supported

✓ Secondary Decisions Supported

✓ Signals Identified

✓ Measures Identified

✓ Grain Defined

✓ Fact Tables Identified

✓ Dimension Tables Identified

✓ Star Schema Validated

✓ Decision Coverage Complete

✓ Traceability Preserved
```

---

# SECTION 14 — HANDOFF TO SEMANTIC_MODEL_SPEC

## Required Approvers

```text
Business Architect

Data Architect

BI Architect
```

---

## Output Upon Approval

```text
SEMANTIC_MODEL_SPEC_v1.0.md
```

---

## Handoff Purpose

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

supports a Business Question

Every Business Question

supports a Signal

Every Signal

supports a Measure

Every Measure

supports a Fact

Every Fact

supports a Dimension
```

and the semantic architecture can proceed to detailed design without revisiting Business Design or Technical Design artifacts.