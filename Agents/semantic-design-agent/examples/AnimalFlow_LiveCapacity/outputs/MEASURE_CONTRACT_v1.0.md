# MEASURE_CONTRACT_v1.0
## Animal Flow — Live Capacity Reporting
### Measure Governance Contract

---

# Document Metadata

Document Type

```text
Measure Contract
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
MEASURE_CONTRACT
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

Define the business meaning, calculation governance, thresholds, actions, ownership, dependencies, and reporting behavior for all measures supporting Animal Flow capacity and placement decisions.

This document serves as the bridge between:

```text
Business Decisions

↓

Signals

↓

Measures

↓

Semantic Model

↓

Power BI / Fabric Implementation
```

---

# MEASURE GOVERNANCE PHILOSOPHY

## Core Principle

Every measure must support:

```text
Decision

↓

Business Question

↓

Signal

↓

Measure

↓

Action
```

---

## Measure Hierarchy

Preferred structure:

```text
Base Measure

↓

Derived Measure

↓

Presentation Measure
```

---

# SECTION 01 — MEASURE INVENTORY

| Measure Name | Classification | Signal Supported | Decision Supported |
|-------------|-------------|-------------|-------------|
| Animals In Care | Base | Occupancy | Placement Decisions |
| Care Capacity | Base | Capacity Availability | Intake Readiness |
| Open DOG Spaces | Base | Open Capacity | Intake Readiness |
| Open CAT Spaces | Base | Open Capacity | Intake Readiness |
| Remaining Capacity | Derived | Placement Readiness | Intake Prioritization |
| DOG Utilization % | Derived | Utilization | Operational Monitoring |
| CAT Utilization % | Derived | Utilization | Operational Monitoring |
| Missing Kennel Assignments | Base | Data Trust | Data Quality Review |
| Assignment Accuracy % | Derived | Data Trust | Data Quality Review |
| Capacity Confirmation Rate | Derived | Governance | Data Confidence |
| Emergency Closure Count | Presentation | Operational Risk | Intake Exclusions |
| Regional Utilization % | Derived | Regional Health | Regional Monitoring |
| Regional Open Capacity % | Derived | Regional Health | Regional Monitoring |

---

# SECTION 02 — DECISION TRACEABILITY

## Primary Decision

```text
Which centres currently have sufficient
capacity to support incoming animals?
```

---

## Traceability Pattern

```text
Decision

↓

Business Question

↓

Signal

↓

Measure

↓

Action
```

---

## Example

```text
Decision

Which centres can receive animals?

↓

Signal

Open DOG Spaces

↓

Measure

Open DOG Spaces

↓

Action

Candidate Centre
```

---

# SECTION 03 — BASE MEASURE DEFINITIONS

# MEASURE 01 — Animals In Care

## Classification

```text
Base Measure
```

---

## Business Definition

```text
Total animals currently assigned
to care at a centre.
```

---

## Source Fact

```text
Fact_Occupancy
```

---

## Source Column

```text
AnimalsInCare
```

---

## Aggregation Type

```text
SUM
```

---

## Decision Supported

```text
Placement Readiness
```

---

## Dependency

```text
Fact_Occupancy.AnimalsInCare
```

---

# MEASURE 02 — Care Capacity

## Classification

```text
Base Measure
```

---

## Business Definition

```text
Total approved care capacity
available for an animal type.
```

---

## Source Fact

```text
Fact_Capacity
```

---

## Source Column

```text
TotalCapacity
```

---

## Aggregation Type

```text
SUM
```

---

## Decision Supported

```text
Intake Readiness
```

---

## Dependency

```text
Fact_Capacity.TotalCapacity
```

---

# MEASURE 03 — Open DOG Spaces

## Classification

```text
Base Measure
```

---

## Business Definition

```text
Available DOG spaces currently open
for intake.
```

---

## Source Fact

```text
Fact_Capacity
```

---

## Source Column

```text
OpenCapacity
```

---

## Dependency

```text
Fact_Capacity.OpenCapacity
```

---

# MEASURE 04 — Open CAT Spaces

## Classification

```text
Base Measure
```

---

## Business Definition

```text
Available CAT spaces currently open
for intake.
```

---

## Source Fact

```text
Fact_Capacity
```

---

## Source Column

```text
OpenCapacity
```

---

## Dependency

```text
Fact_Capacity.OpenCapacity
```

---

# SECTION 04 — DERIVED MEASURE DEFINITIONS

# MEASURE 05 — Remaining Capacity

## Classification

```text
Derived Measure
```

---

## Business Definition

```text
Available capacity remaining after
current occupancy is considered.
```

---

## Business Formula

```text
Care Capacity

-

Animals In Care
```

---

## Dependencies

```text
Care Capacity

Animals In Care
```

---

## Decision Supported

```text
Which centres can safely
receive incoming animals?
```

---

# MEASURE 06 — DOG Utilization %

## Classification

```text
Derived Measure
```

---

## Business Definition

```text
Percentage of DOG capacity
currently occupied.
```

---

## Formula

```text
DOG Occupancy

÷

DOG Capacity
```

---

## Decision Supported

```text
Operational Monitoring
```

---

# MEASURE 07 — CAT Utilization %

## Classification

```text
Derived Measure
```

---

## Business Definition

```text
Percentage of CAT capacity
currently occupied.
```

---

## Formula

```text
CAT Occupancy

÷

CAT Capacity
```

---

## Decision Supported

```text
Operational Monitoring
```

---

# MEASURE 08 — Assignment Accuracy %

## Classification

```text
Derived Measure
```

---

## Business Definition

```text
Percentage of correctly assigned animals.
```

---

## Formula

```text
Valid Assignments

÷

Total Assignments
```

---

## Decision Supported

```text
Data Quality Review
```

---

# MEASURE 09 — Capacity Confirmation Rate

## Classification

```text
Derived Measure
```

---

## Business Definition

```text
Percentage of centres with
current capacity confirmation.
```

---

## Formula

```text
Confirmed Centres

÷

Total Centres
```

---

## Decision Supported

```text
Governance Review
```

---

# MEASURE 10 — Regional Utilization %

## Classification

```text
Derived Measure
```

---

## Business Definition

```text
Percentage of regional capacity
currently occupied.
```

---

## Formula

```text
Regional Occupancy

÷

Regional Capacity
```

---

# MEASURE 11 — Regional Open Capacity %

## Classification

```text
Derived Measure
```

---

## Business Definition

```text
Percentage of regional capacity
remaining available.
```

---

## Formula

```text
Regional Open Capacity

÷

Regional Capacity
```

---

# SECTION 05 — PRESENTATION MEASURES

# MEASURE 12 — Emergency Closure Count

## Classification

```text
Presentation Measure
```

---

## Business Definition

```text
Number of centres currently
excluded from intake activities.
```

---

## Parent Measure

```text
Emergency Closure Status
```

---

## Purpose

```text
Highlight immediate operational risks.
```

---

# SECTION 06 — THRESHOLD CONTRACTS

# DOG Utilization %

## Green

```text
< 80%
```

Action

```text
Candidate Centre
```

---

## Amber

```text
80% - 99%
```

Action

```text
Review Before Routing
```

---

## Red

```text
>= 100%
```

Action

```text
Do Not Intake
```

---

# CAT Utilization %

## Green

```text
< 80%
```

Action

```text
Candidate Centre
```

---

## Amber

```text
80% - 99%
```

Action

```text
Review Before Routing
```

---

## Red

```text
>= 100%
```

Action

```text
Do Not Intake
```

---

# Missing Kennel Assignments

## Green

```text
0
```

---

## Amber

```text
1 - 3
```

---

## Red

```text
> 3
```

---

## Action

```text
Data Cleanup Required
```

---

# Capacity Confirmation Age

## Green

```text
< 12 Hours
```

---

## Amber

```text
12 - 24 Hours
```

---

## Red

```text
> 24 Hours
```

---

## Action

```text
Contact Centre
```

---

# SECTION 07 — DECISION ACTION CONTRACTS

| Condition | Action |
|------------|------------|
| Capacity Available AND Healthy | Candidate Centre |
| Utilization 80%-99% | Review Before Routing |
| Utilization >=100% | Do Not Intake |
| Missing Assignments >3 | Data Quality Review |
| Confirmation Age >24 Hours | Contact Centre |
| Emergency Closure Active | Exclude Centre |

---

# SECTION 08 — FORMATTING CONTRACTS

| Measure | Format Type | Format String |
|----------|----------|----------|
| Animals In Care | Whole Number | #,0 |
| Care Capacity | Whole Number | #,0 |
| Open Capacity | Whole Number | #,0 |
| Remaining Capacity | Whole Number | #,0 |
| Assignment Accuracy % | Percentage | 0.0% |
| DOG Utilization % | Percentage | 0.0% |
| CAT Utilization % | Percentage | 0.0% |
| Regional Utilization % | Percentage | 0.0% |
| Regional Open Capacity % | Percentage | 0.0% |

---

# SECTION 09 — VISUAL MAPPING

| Measure | Report Section |
|----------|----------|
| Open DOG Spaces | Provincial Snapshot |
| Open CAT Spaces | Provincial Snapshot |
| DOG Utilization % | Capacity Analysis |
| CAT Utilization % | Capacity Analysis |
| Remaining Capacity | Intake Readiness |
| Assignment Accuracy % | Data Trust |
| Missing Assignments | Data Trust |
| Capacity Confirmation Rate | Data Trust |
| Regional Utilization % | Regional Health |
| Regional Open Capacity % | Regional Health |

---

# SECTION 10 — FACT MAPPING

| Measure | Source Fact |
|----------|----------|
| Animals In Care | Fact_Occupancy |
| Care Capacity | Fact_Capacity |
| Open DOG Spaces | Fact_Capacity |
| Open CAT Spaces | Fact_Capacity |
| Remaining Capacity | Fact_Capacity + Fact_Occupancy |
| Assignment Accuracy % | Fact_Occupancy |
| Capacity Confirmation Rate | Fact_Confirmation |
| Regional Utilization % | Fact_Capacity |
| Regional Open Capacity % | Fact_Capacity |

---

# SECTION 11 — DEPENDENCY MAPPING

## Remaining Capacity

```text
Care Capacity

↓

Animals In Care

↓

Remaining Capacity
```

---

## Placement Readiness

```text
Open Capacity

↓

Utilization

↓

Closure Status

↓

Placement Readiness
```

---

# SECTION 12 — BUSINESS OWNERSHIP

| Measure Group | Business Owner |
|----------|----------|
| Capacity Measures | Animal Flow |
| Placement Measures | Animal Flow |
| Data Quality Measures | Operations Leadership |
| Governance Measures | Operations Leadership |
| Regional Measures | Animal Flow Leadership |

---

# SECTION 13 — AI READINESS

## Example AI Summary

### Remaining Capacity

```text
Remaining Capacity represents the number
of spaces available after current
occupancy has been considered.
```

---

### DOG Utilization %

```text
DOG Utilization % represents the percentage
of available DOG capacity currently occupied.
```

---

# SECTION 14 — MEASURE VALIDATION

```text
✓ Business Definitions Exist

✓ Measure Dependencies Defined

✓ Thresholds Defined

✓ Actions Defined

✓ Fact Mapping Completed

✓ Visual Mapping Completed

✓ Ownership Assigned

✓ Decision Traceability Preserved
```

---

# SECTION 15 — GOVERNANCE REVIEW

```text
✓ No Duplicate Measures

✓ Threshold Logic Approved

✓ Business Definitions Approved

✓ Decision Mapping Complete

✓ Ownership Assigned
```

---

# SECTION 16 — HANDOFF TO BUILD PHASE

## Next Artifact

```text
SEMANTIC_BUILD_AGENT
```

---

## Purpose

```text
Business Logic

↓

Governed DAX Measures

↓

Fabric Semantic Model

↓

Power BI Implementation
```

---

# SUCCESS STATEMENT

The Measure Contract succeeds when:

```text
Every Measure

has a Business Definition.

Every Measure

supports a Signal.

Every Signal

supports a Decision.

Every Decision

supports an Action.

Every Calculation

is governed.

Every Threshold

is documented.

Every Business Owner

accepts accountability.
```

The Measure Contract becomes:

```text
The Measure Governance Contract
```

between:

```text
Business Design

↓

Semantic Design

↓

Semantic Build

↓

Report Development
```