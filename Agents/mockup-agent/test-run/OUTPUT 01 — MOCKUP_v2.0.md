# MOCKUP_v2.0.md
## Animal Flow — Live Capacity Reporting
### Markdown Wireframe

---

# Document Metadata

Document Type

Markdown Wireframe

Version

2.0

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

The mockup represents:

```text
Story Flow

Section Layout

Information Hierarchy

Visual Placement

Reading Order
```

The mockup follows:

```text
REPORT_STORY_v1.0

MOCKUP_STANDARDS_v1.0

LAYOUT_PATTERNS_v1.0

Decision Intelligence Command Centre
```

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
capacity risks, operational constraints,
data quality concerns, and recommended actions.
```

---

# LAYOUT PATTERN

## Selected Layout Pattern

```text
Decision Intelligence Command Centre
```

---

## Layout Purpose

```text
Support operational decision making through a guided decision journey.
```

---

## Business Journey

```text
What Is Happening?

↓

What Requires Attention?

↓

What Decisions Must Be Made?

↓

Where Should Action Be Taken?

↓

Why?

↓

Can The Information Be Trusted?

↓

Where Is Risk Building?

↓

What Should We Do Next?
```

---

# GLOBAL FILTER AREA

## Purpose

Allow users to focus operational analysis.

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
+-------------------------------------------------------------+
|                    GLOBAL FILTER BAR                        |
+-------------------------------------------------------------+

[Animal Type]
[Region]
[Centre]
[Capacity Status]
```

---

# SECTION 01

## Section Name

```text
Provincial Capacity Snapshot
```

---

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

Provide immediate provincial context before decisions are made.

---

## Visual Containers

```text
Total DOG Spaces

Open DOG Spaces

Total CAT Spaces

Open CAT Spaces

DOG Utilization %

CAT Utilization %
```

---

## Mockup Layout

```text
+-------------------------------------------------------------+
|             PROVINCIAL CAPACITY SNAPSHOT                    |
+-------------------------------------------------------------+

+-----------+-----------+-----------+-----------+-----------+
| KPI Card  | KPI Card  | KPI Card  | KPI Card  | KPI Card  |
+-----------+-----------+-----------+-----------+-----------+
```

---

# SECTION 02

## Section Name

```text
Action Required
```

---

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
Identify urgent operational issues.
```

---

## Purpose

Surface critical exceptions requiring review.

---

## Visual Containers

```text
Emergency Closures

Full Centres

Data Quality Issues
```

---

## Mockup Layout

```text
+-------------------------------------------------------------+
|                    ACTION REQUIRED                          |
+-------------------------------------------------------------+

+----------------+----------------+----------------+
| Exception KPI  | Exception KPI  | Exception KPI  |
+----------------+----------------+----------------+
```

---

# SECTION 03

## Section Name

```text
Intake Readiness
```

---

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
Identify intake candidates.
```

---

## Purpose

Provide rapid operational placement guidance.

---

## Visual Containers

```text
Candidate Centres

Monitor Centres

Full Centres

Closed Centres
```

---

## Mockup Layout

```text
+-------------------------------------------------------------+
|                     INTAKE READINESS                        |
+-------------------------------------------------------------+

+----------------+----------------+
| Status Card    | Status Card    |
+----------------+----------------+

+----------------+----------------+
| Status Card    | Status Card    |
+----------------+----------------+
```

---

# SECTION 04

## Section Name

```text
Placement Decision Board
```

---

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
Select preferred placement locations.
```

---

## Purpose

Rank and prioritize intake destinations.

---

## Visual Containers

```text
Priority Table
```

---

## Mockup Layout

```text
+-------------------------------------------------------------+
|                 PLACEMENT DECISION BOARD                    |
+-------------------------------------------------------------+

+-------------------------------------------------------------+
|                     PRIORITY TABLE                          |
+-------------------------------------------------------------+
```

---

# SECTION 05

## Section Name

```text
Capacity Analysis
```

---

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
Understand operational constraints.
```

---

## Purpose

Explain utilization and availability conditions.

---

## Visual Containers

```text
DOG Capacity Comparison

CAT Capacity Comparison
```

---

## Mockup Layout

```text
+-------------------------------------------------------------+
|                    CAPACITY ANALYSIS                        |
+-------------------------------------------------------------+

+----------------------+----------------------+
| DOG Comparison       | CAT Comparison       |
+----------------------+----------------------+
```

---

# SECTION 06

## Section Name

```text
Data Trust
```

---

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

Assess operational data quality and reliability.

---

## Visual Containers

```text
Missing Assignments

Confirmation Status

Data Freshness

ShelterBuddy Sync Status
```

---

## Mockup Layout

```text
+-------------------------------------------------------------+
|                        DATA TRUST                           |
+-------------------------------------------------------------+

+----------------------+----------------------+
| Trust Container      | Trust Container      |
+----------------------+----------------------+

+----------------------+----------------------+
| Trust Container      | Trust Container      |
+----------------------+----------------------+
```

---

# SECTION 07

## Section Name

```text
Regional Health
```

---

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

Identify regional capacity pressure and trends.

---

## Visual Containers

```text
Regional Capacity Ranking

Regional Summary
```

---

## Mockup Layout

```text
+-------------------------------------------------------------+
|                     REGIONAL HEALTH                         |
+-------------------------------------------------------------+

+----------------------+----------------------+
| Ranking Container    | Summary Container    |
+----------------------+----------------------+
```

---

# SECTION 08

## Section Name

```text
Operational Briefing
```

---

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

Convert findings into actionable recommendations.

---

## Visual Containers

```text
Capacity Risk Recommendation

Data Quality Recommendation

Placement Recommendation
```

---

## Mockup Layout

```text
+-------------------------------------------------------------+
|                  OPERATIONAL BRIEFING                       |
+-------------------------------------------------------------+

+-------------------------------------------------------------+
| Recommendation Card                                         |
+-------------------------------------------------------------+

+-------------------------------------------------------------+
| Recommendation Card                                         |
+-------------------------------------------------------------+

+-------------------------------------------------------------+
| Recommendation Card                                         |
+-------------------------------------------------------------+
```

---

# FULL PAGE WIREFRAME

## Selected Layout Pattern

```text
Decision Intelligence Command Centre
```

---

## Story Flow

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

# VISUAL HIERARCHY

## Tier 1 — Mission Critical

```text
Provincial Capacity Snapshot

Action Required

Intake Readiness
```

---

## Tier 2 — Decision Support

```text
Placement Decision Board

Capacity Analysis
```

---

## Tier 3 — Trust & Monitoring

```text
Data Trust

Regional Health
```

---

## Tier 4 — Action

```text
Operational Briefing
```

---

# READING PATTERN

```text
ZIP / ZAP Flow

Top Left

→

Top Right

↓

Middle Left

→

Middle Right

↓

Bottom Left

→

Bottom Right
```

---

# MOCKUP VALIDATION

Information Hierarchy

☑ Approved

---

Reading Order

☑ Approved

---

Story Flow

☑ Approved

---

Layout Pattern Applied

☑ Approved

---

Decision Support

☑ Approved

---

Visual Placement

☑ Approved

---

DSC Alignment

☑ Approved

---

# MOCKUP SUCCESS STATEMENT

The mockup succeeds when:

```text
Every Section
supports a Business Question

Every Business Question
supports a Decision

Every Visual Container
supports a Section

Every Layout Element
supports the Story
```

and stakeholders can validate:

```text
What Appears

Where It Appears

Why It Appears
```

before SVG rendering begins.

---

# NEXT STEP

```text
Generate:

MOCKUP_v2.0.svg

Using:

Decision Intelligence Command Centre

+

UX_THEME_STANDARD_v1.0

+

04_SVG_TEMPLATE_v1.0

+

SVG_GUIDELINES_v1.0
```