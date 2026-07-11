# MOCKUP_v1.0.md
## Animal Flow — Live Capacity Reporting
### Markdown Wireframe

---

# Document Metadata

Document Type

Markdown Wireframe

Version

1.0

Capability Name

Animal Flow — Live Capacity Reporting

Artifact Type

Mockup

Owner

Animal Flow

Status

Draft

Purpose

Provide an implementation-independent visual blueprint of the report before SVG generation, Power BI development, or technical implementation.

---

# PAGE OVERVIEW

## Primary Decision

```text
Which centres currently have sufficient capacity to support incoming animals?
```

---

## Audience

```text
Animal Flow

Leadership
```

---

## Page Archetype

```text
Operational Command Centre
```

---

## Story Goal

```text
Enable Animal Flow to rapidly identify intake-ready centres,
operational risks, capacity constraints, and data quality concerns
from a single provincial dashboard.
```

---

# PAGE STRUCTURE

```text
Global Filters

↓

Provincial Capacity Snapshot

↓

Action Required

↓

Intake Readiness

↓

Placement Decision Board

↓

Capacity Analysis

↓

Data Trust

↓

Regional Health

↓

Operational Briefing
```

---

# GLOBAL FILTER AREA

## Purpose

Allow users to focus analysis by location and animal type.

---

## Supported Decisions

```text
Which centres can receive incoming animals?

Which regions require intervention?

Which centres require review?
```

---

## Filters

```text
Animal Type

Region

Centre

Capacity Status
```

---

## Mockup Layout

```text
+--------------------------------------------------------------+
|                      GLOBAL FILTER BAR                       |
+--------------------------------------------------------------+

+------------+------------+------------+----------------------+
| Animal     | Region     | Centre     | Capacity Status      |
| Type ▼     | ▼          | ▼          | ▼                    |
+------------+------------+------------+----------------------+
```

---

# SECTION 01 — PROVINCIAL CAPACITY SNAPSHOT

## Business Question

```text
What is happening across the province today?
```

---

## Audience

```text
Animal Flow

Leadership
```

---

## Decision Supported

```text
Understand current operating conditions.
```

---

## Purpose

Provide immediate operational context.

---

## Visual Containers

```text
Total DOG Spaces

Open DOG Spaces

DOG Utilization %

Open CAT Spaces

CAT Utilization %
```

---

## Mockup Layout

```text
+--------------------------------------------------------------+
|                PROVINCIAL CAPACITY SNAPSHOT                  |
+--------------------------------------------------------------+

+------------+------------+------------+------------+----------+
| DOG Total  | DOG Open   | DOG Util % | CAT Open   | CAT Util |
+------------+------------+------------+------------+----------+
```

---

# SECTION 02 — ACTION REQUIRED

## Business Question

```text
What requires immediate attention?
```

---

## Audience

```text
Animal Flow
```

---

## Decision Supported

```text
Identify urgent conditions.
```

---

## Purpose

Highlight operational exceptions.

---

## Visual Containers

```text
Emergency Closures

Full Centres

Data Quality Alerts
```

---

## Mockup Layout

```text
+--------------------------------------------------------------+
|                     ACTION REQUIRED                          |
+--------------------------------------------------------------+

+----------------+----------------+----------------+
| Emergency      | Full           | Data Quality   |
| Closures       | Centres        | Alerts         |
+----------------+----------------+----------------+
```

---

# SECTION 03 — INTAKE READINESS

## Business Question

```text
Which centres can safely receive incoming animals?
```

---

## Audience

```text
Animal Flow
```

---

## Decision Supported

```text
Determine intake eligibility.
```

---

## Purpose

Surface operational status.

---

## Visual Containers

```text
Candidate Centres

Monitor Centres

Do Not Intake Centres

Capacity Readiness
```

---

## Mockup Layout

```text
+--------------------------------------------------------------+
|                     INTAKE READINESS                         |
+--------------------------------------------------------------+

+----------------+----------------+
| Candidate      | Monitor        |
| Centres        | Centres        |
+----------------+----------------+

+----------------+----------------+
| Do Not Intake  | Capacity       |
| Centres        | Readiness      |
+----------------+----------------+
```

---

# SECTION 04 — PLACEMENT DECISION BOARD

## Business Question

```text
Which centres should be prioritized?
```

---

## Audience

```text
Animal Flow
```

---

## Decision Supported

```text
Select placement destinations.
```

---

## Purpose

Provide ranked intake recommendations.

---

## Visual Containers

```text
Priority Table
```

---

## Mockup Layout

```text
+--------------------------------------------------------------+
|                 PLACEMENT DECISION BOARD                     |
+--------------------------------------------------------------+

+--------------------------------------------------------------+
| Centre | Region | Open Capacity | Status | Recommendation   |
+--------------------------------------------------------------+
|                                              Priority Table |
+--------------------------------------------------------------+
```

---

# SECTION 05 — CAPACITY ANALYSIS

## Business Question

```text
Why can or cannot centres receive additional animals?
```

---

## Audience

```text
Animal Flow
```

---

## Decision Supported

```text
Understand capacity constraints.
```

---

## Purpose

Explain operating conditions.

---

## Visual Containers

```text
DOG Capacity Analysis

CAT Capacity Analysis
```

---

## Mockup Layout

```text
+--------------------------------------------------------------+
|                    CAPACITY ANALYSIS                         |
+--------------------------------------------------------------+

+-----------------------------+-----------------------------+
| DOG Capacity Comparison     | CAT Capacity Comparison     |
+-----------------------------+-----------------------------+
```

---

# SECTION 06 — DATA TRUST

## Business Question

```text
Can the information be trusted?
```

---

## Audience

```text
Animal Flow
```

---

## Decision Supported

```text
Validate confidence before acting.
```

---

## Purpose

Support operational trust.

---

## Visual Containers

```text
Missing Assignments

Confirmation Status

Data Freshness

Sync Status
```

---

## Mockup Layout

```text
+--------------------------------------------------------------+
|                         DATA TRUST                           |
+--------------------------------------------------------------+

+----------------------+----------------------+
| Missing Assignments  | Confirmation Status  |
+----------------------+----------------------+

+----------------------+----------------------+
| Data Freshness       | Sync Status          |
+----------------------+----------------------+
```

---

# SECTION 07 — REGIONAL HEALTH

## Business Question

```text
Where is capacity pressure building?
```

---

## Audience

```text
Animal Flow

Leadership
```

---

## Decision Supported

```text
Monitor regional operating conditions.
```

---

## Purpose

Identify regional pressure.

---

## Visual Containers

```text
Regional Capacity Ranking

Regional Summary
```

---

## Mockup Layout

```text
+--------------------------------------------------------------+
|                      REGIONAL HEALTH                         |
+--------------------------------------------------------------+

+-----------------------------+-----------------------------+
| Regional Ranking            | Regional Summary            |
+-----------------------------+-----------------------------+
```

---

# SECTION 08 — OPERATIONAL BRIEFING

## Business Question

```text
What should we do next?
```

---

## Audience

```text
Animal Flow
```

---

## Decision Supported

```text
Execute recommended actions.
```

---

## Purpose

Convert insights into action.

---

## Visual Containers

```text
Recommendation Card

Recommendation Card

Recommendation Card
```

---

## Mockup Layout

```text
+--------------------------------------------------------------+
|                   OPERATIONAL BRIEFING                       |
+--------------------------------------------------------------+

+--------------------------------------------------------------+
| Recommendation #1                                            |
+--------------------------------------------------------------+

+--------------------------------------------------------------+
| Recommendation #2                                            |
+--------------------------------------------------------------+

+--------------------------------------------------------------+
| Recommendation #3                                            |
+--------------------------------------------------------------+
```

---

# FULL PAGE WIREFRAME

```text
GLOBAL FILTERS

↓

PROVINCIAL CAPACITY SNAPSHOT

↓

ACTION REQUIRED

↓

INTAKE READINESS

↓

PLACEMENT DECISION BOARD

↓

CAPACITY ANALYSIS

↓

DATA TRUST

↓

REGIONAL HEALTH

↓

OPERATIONAL BRIEFING
```

---

# MOCKUP VALIDATION

Information Hierarchy

☑ Complete

Reading Order

☑ Complete

Story Flow

☑ Complete

Decision Support

☑ Complete

Visual Placement

☑ Complete

DSC Alignment

☑ Complete

---

# NEXT STEP

```text
Generate:

MOCKUP_v1.0.svg
```