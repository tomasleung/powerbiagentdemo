# TRD_v1.0
## Technical Requirements Document (TRD)

---

# Document Metadata

Document Type

Technical Requirements Document

Version

1.0

Capability Name

Animal Flow — Live Capacity Reporting

Artifact Type

TRD

Owner

Animal Flow

Status

Draft

Purpose

Transform approved business design artifacts into a technical implementation blueprint supporting provincial capacity monitoring, intake readiness decisions, operational risk identification, data quality monitoring, and regional capacity management.

---

# Related Artifacts

```text
INPUT_BRD_AnimalFlow_LiveCapacity_v2.0.md

REPORT_STORY_MATRIX_v1.0.md

REPORT_STORY_v1.0.md

MOCKUP_v2.0.md

MOCKUP_v2.0.svg
```

---

# 01 REPORT OVERVIEW

## Capability Name

```text
Animal Flow — Live Capacity Reporting
```

---

## Report Purpose

Provide a centralized provincial capacity intelligence solution supporting animal placement decisions, operational monitoring, capacity management, and data quality review across all BC SPCA Community Animal Centres.

---

## Primary Decision Supported

```text
Which centres currently have sufficient capacity to support incoming animals?
```

---

## Secondary Decisions

```text
Which centres require intervention?

Which centres should be prioritized for intake?

Which centres should be avoided?

Which centres have data quality concerns?

Which regions are experiencing capacity pressure?
```

---

## Primary Users

```text
Animal Flow

Animal Flow Leadership

Operations Leadership
```

---

## Business Owner

```text
Animal Flow Team
```

---

## Technical Owner

```text
Business Intelligence Team
```

---

## In Scope

```text
Provincial Capacity Dashboard

Regional Capacity Monitoring

Centre Comparison Reporting

Capacity Utilization Monitoring

Data Quality Monitoring

Capacity Confirmation Tracking

Operational Prioritization

Narrative Recommendations

Power App Drillthrough Integration
```

---

## Out Of Scope

```text
Capacity Management

ShelterBuddy Maintenance

Floor Plan Editing

Kennel Configuration

Predictive Analytics

Automated Placement Recommendations
```

---

# 02 SOURCE & TARGET MAPPING

## Source System 01

### Source Name

```text
CAT Master
```

### Purpose

```text
CAT Capacity Inventory
```

### Data Domain

```text
Capacity Configuration
```

### Target

```text
Fact Capacity Availability
```

---

## Source System 02

### Source Name

```text
DOG Master
```

### Purpose

```text
DOG Capacity Inventory
```

### Data Domain

```text
Capacity Configuration
```

### Target

```text
Fact Capacity Availability
```

---

## Source System 03

### Source Name

```text
ShelterBuddy
```

### Purpose

```text
Animal Occupancy Source
```

### Data Domain

```text
Animal Occupancy
```

### Target

```text
Fact Capacity Utilization

Fact Data Quality
```

---

## Source System 04

### Source Name

```text
Power App
```

### Purpose

```text
Capacity Confirmation

Operational Sign-Off
```

### Data Domain

```text
Operational Governance
```

### Target

```text
Fact Capacity Confirmation
```

---

## Source System 05

### Source Name

```text
Live Capacity Management
```

### Purpose

```text
Operational KPI Generation
```

### Data Domain

```text
Capacity Intelligence
```

### Target

```text
Fact Capacity Performance
```

---

## Source To Target Mapping

```text
CAT Master
    ↓
Capacity Inventory

DOG Master
    ↓
Capacity Inventory

ShelterBuddy
    ↓
Occupancy Measures

Power App
    ↓
Capacity Confirmation Metrics

Live Capacity Management
    ↓
Operational KPI Layer
```

---

# 03 HIGH-LEVEL DATA MODEL

## Fact Table

### Fact_Capacity_Utilization

Purpose

```text
Store centre-level capacity utilization metrics.
```

Business Grain

```text
Centre

Animal Type

Reporting Date
```

Measures Supported

```text
DOG Utilization %

CAT Utilization %

Open DOG Spaces

Open CAT Spaces
```

---

## Fact Table

### Fact_Data_Quality

Purpose

```text
Store operational data quality indicators.
```

Business Grain

```text
Centre

Reporting Date
```

Measures Supported

```text
Missing Assignments

Assignment Accuracy %

Capacity Confirmation Rate
```

---

## Fact Table

### Fact_Regional_Performance

Purpose

```text
Store regional capacity and utilization metrics.
```

Business Grain

```text
Region

Reporting Date
```

Measures Supported

```text
Regional Capacity

Regional Utilization

Regional Open Capacity
```

---

# Dimension Tables

## Dim_Centre

Purpose

```text
Centre Reporting Context
```

Key Attributes

```text
Centre

Centre Type

Region

Operating Status
```

---

## Dim_Region

Purpose

```text
Regional Reporting Context
```

Key Attributes

```text
Region

Province

Operational Area
```

---

## Dim_AnimalType

Purpose

```text
Capacity Segmentation
```

Key Attributes

```text
DOG

CAT
```

---

## Dim_Date

Purpose

```text
Time Intelligence
```

Key Attributes

```text
Date

Week

Month

Quarter

Year
```

---

# Conceptual Relationship Model

```text
Dim Region
        ↓
Dim Centre
        ↓
Fact Capacity Utilization

Dim Animal Type
        ↓
Fact Capacity Utilization

Dim Date
        ↓
Fact Capacity Utilization
```

---

# 04 MEASURE INVENTORY

## Measure

### Total DOG Spaces

Business Definition

```text
Total operational dog capacity.
```

Decision Supported

```text
Capacity Availability
```

Related Story Section

```text
Provincial Capacity Snapshot
```

---

## Measure

### Open DOG Spaces

Business Definition

```text
Available dog spaces for intake.
```

Decision Supported

```text
Intake Readiness
```

Related Story Section

```text
Provincial Capacity Snapshot

Intake Readiness
```

---

## Measure

### Total CAT Spaces

Business Definition

```text
Total operational cat capacity.
```

Decision Supported

```text
Capacity Availability
```

---

## Measure

### Open CAT Spaces

Business Definition

```text
Available cat spaces for intake.
```

Decision Supported

```text
Intake Readiness
```

---

## Measure

### DOG Utilization %

Business Definition

```text
Percentage of occupied dog capacity.
```

Decision Supported

```text
Placement Readiness
```

---

## Measure

### CAT Utilization %

Business Definition

```text
Percentage of occupied cat capacity.
```

Decision Supported

```text
Placement Readiness
```

---

## Measure

### Missing Kennel Assignments

Business Definition

```text
Animals without a valid kennel assignment.
```

Decision Supported

```text
Data Confidence
```

---

## Measure

### Assignment Accuracy %

Business Definition

```text
Percentage of correctly assigned animals.
```

Decision Supported

```text
Data Trust
```

---

## Measure

### Capacity Confirmation Rate

Business Definition

```text
Percentage of centres with current confirmation status.
```

Decision Supported

```text
Governance Review
```

---

## Measure

### Emergency Closure Count

Business Definition

```text
Number of centres currently unavailable for intake.
```

Decision Supported

```text
Operational Risk
```

---

# 05 VISUAL MAPPING

## Provincial Capacity Snapshot

Business Question

```text
What is happening across the province today?
```

Visual Type

```text
Informational KPI Cards
```

Measures

```text
Total DOG Spaces

Open DOG Spaces

Total CAT Spaces

Open CAT Spaces

DOG Utilization %

CAT Utilization %
```

Decision Supported

```text
Situational Awareness
```

---

## Action Required

Visual Type

```text
Exception KPI Cards
```

Measures

```text
Emergency Closure Count

Stale Updates

Data Quality Exceptions

Full Centres
```

Decision Supported

```text
Operational Intervention
```

---

## Intake Readiness

Visual Type

```text
Status Cards
```

Measures

```text
Open Capacity

Utilization Status

Closure Status
```

Decision Supported

```text
Placement Eligibility
```

---

## Placement Decision Board

Visual Type

```text
Priority Table
```

Measures

```text
Placement Score

Open Capacity

Utilization

Operational Status
```

Decision Supported

```text
Centre Prioritization
```

---

## Capacity Analysis

Visual Type

```text
Comparison Cards
```

Measures

```text
DOG Utilization %

CAT Utilization %
```

Decision Supported

```text
Constraint Analysis
```

---

## Data Trust

Visual Type

```text
Exception Matrix
```

Measures

```text
Missing Assignments

Assignment Accuracy %

Capacity Confirmation Status
```

Decision Supported

```text
Validate Confidence
```

---

## Regional Health

Visual Type

```text
Horizontal Bar Chart
```

Measures

```text
Regional Utilization

Regional Open Capacity
```

Decision Supported

```text
Regional Monitoring
```

---

## Operational Briefing

Visual Type

```text
Recommendation Cards
```

Measures

```text
Derived Narrative Metrics
```

Decision Supported

```text
Operational Action
```

---

# 06 INTERACTION DESIGN

## Filters

```text
Animal Type

Region

Centre

Capacity Status
```

---

## Cross Filtering

Purpose

```text
Allow users to move between provincial, regional,
and centre level analysis.
```

---

## Drillthrough Navigation

### Capacity Dashboard

```text
Provincial

↓

Region

↓

Centre
```

---

### Operational Workflow

```text
Dashboard

↓

Power App
```

Purpose

```text
Investigate operational issues and perform action.
```

---

# 07 SECURITY DESIGN

## Role

### Animal Flow

Access Level

```text
Full Reporting Access
```

Purpose

```text
Daily intake decision support.
```

---

## Role

### Leadership

Access Level

```text
Provincial Summary Access
```

Purpose

```text
Operational oversight.
```

---

## Role

### Centre Manager

Access Level

```text
Centre / Regional Access
```

Purpose

```text
Monitor local operational performance.
```

---

## Role

### Read Only

Access Level

```text
Consumer Access
```

Purpose

```text
View reporting only.
```

---

# 08 VALIDATION RULES

## Validation Rule

### Capacity Reconciliation

Purpose

```text
Dashboard totals must reconcile to
Live Capacity Management.
```

---

## Validation Rule

### Floor Plan Validation

Purpose

```text
Capacity counts must reconcile to
approved floor plan calculations.
```

---

## Validation Rule

### ShelterBuddy Validation

Purpose

```text
Missing assignment counts must reconcile
to ShelterBuddy.
```

---

## Validation Rule

### Freshness Validation

Purpose

```text
Capacity update timestamps must reflect
actual operational update times.
```

---

## Validation Rule

### Narrative Validation

Purpose

```text
Operational recommendations must align
with supporting metrics.
```

---

# 09 DEPLOYMENT CONSIDERATIONS

## Environment Flow

```text
Development

↓

Test

↓

Production
```

---

## Dependencies

```text
ShelterBuddy

Power App

CAT Master

DOG Master

Live Capacity Management

Power BI Service
```

---

## Assumptions

```text
Live Capacity Management is the source of truth.

ShelterBuddy is authoritative for occupancy.

Centres maintain data accurately.

Power App data remains available.
```

---

## Known Risks

```text
Operational update delays

Data quality issues

Synchronization latency

Capacity confirmation compliance
```

---

## Deployment Readiness Checklist

```text
□ Sources Available

□ Security Reviewed

□ Measures Validated

□ Visual Mapping Approved

□ Data Quality Rules Approved

□ Reconciliation Rules Validated

□ UAT Completed

□ Production Approval Granted
```

---

# TRACEABILITY MATRIX

```text
Decision

↓

Business Question

↓

Signal

↓

Measure

↓

Visual

↓

Technical Object
```

Example:

```text
Which centres can safely receive animals?

↓

Open DOG Spaces

↓

Open DOG Spaces Measure

↓

Intake Readiness

↓

Fact_Capacity_Utilization
```

---

# TRD VALIDATION

```text
☑ Sources Identified

☑ Targets Identified

☑ Fact Tables Identified

☑ Dimensions Identified

☑ Measures Identified

☑ Visual Mapping Complete

☑ Interaction Design Complete

☑ Security Design Complete

☑ Validation Rules Complete

☑ Deployment Considerations Complete

☑ Traceability Preserved
```

---

# TRD SUCCESS STATEMENT

The TRD succeeds when:

```text
A Power BI Developer,

Fabric Developer,

or Semantic Model Designer

can implement the approved solution
without revisiting:

BRD

REPORT_STORY_MATRIX

REPORT_STORY (DSC)

MOCKUP.md

MOCKUP.svg
```

The TRD becomes:

```text
The Technical Implementation Contract
```

between:

```text
Business Design

↓

Technical Design

↓

Semantic Design
```