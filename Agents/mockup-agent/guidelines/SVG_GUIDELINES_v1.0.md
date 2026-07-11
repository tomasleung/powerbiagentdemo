# SVG_GUIDELINES_v1.0
## Decision-Driven BI SVG Rendering Standards

---

# Document Metadata

Document Name

SVG_GUIDELINES

Version

1.0

Owner

Decision-Driven BI Framework

Status

Approved Standard

Purpose

Provide a governing framework for generating SVG wireframes from approved Markdown Mockups.

The SVG represents the approved report structure and visual hierarchy.

The SVG is a rendering artifact only.

It does not create business logic.

It does not redefine the report design.

---

# SECTION 01 — SVG PHILOSOPHY

## Core Principle

The SVG visualizes the approved mockup.

The SVG does not design the report.

The SVG renders the report.

---

## Approved Flow

```text
BRD
↓
REPORT_STORY_MATRIX
↓
REPORT_STORY (DSC)
↓
MOCKUP
↓
SVG
```

---

## SVG Purpose

Allow stakeholders to validate:

```text
Page Layout

Visual Hierarchy

Information Placement

Reading Order

Section Structure
```

before development begins.

---

# SECTION 02 — SINGLE SOURCE OF TRUTH

## Governing Inputs

The SVG may only use:

```text
Approved DSC

Approved MOCKUP
```

---

## SVG Must Not Invent

```text
KPIs

Measures

Questions

Signals

Business Logic

Sections

Visual Types
```

---

## Validation Rule

Every SVG component must trace back to:

```text
MOCKUP

↓

DSC
```

If no traceability exists:

```text
Do Not Render
```

---

# SECTION 03 — SVG RENDERING OBJECTIVES

## Objective 01

Validate Information Hierarchy

---

## Objective 02

Validate Page Flow

---

## Objective 03

Validate Visual Placement

---

## Objective 04

Validate Reading Order

---

## Objective 05

Provide Developer Blueprint

---

# SECTION 04 — PAGE DIMENSIONS

## Primary Layout

Power BI Desktop

```text
16:9 Landscape
```

Recommended Canvas

```text
1600 x 900
```

---

## Alternate Layout

Executive Reporting

```text
1920 x 1080
```

---

## Mobile Layout

Not Supported

Future Version

---

# SECTION 05 — MARGIN STANDARDS

## External Margins

```text
40px
```

minimum

around outer page boundary.

---

## Section Margins

```text
20px
```

minimum

between sections.

---

## Container Margins

```text
12px
```

minimum

between containers.

---

# SECTION 06 — SECTION RENDERING STANDARDS

## Every Section Must Display

```text
Section Name

Section Boundary

Visual Container Boundary
```

---

## Section Header

Render Format

```text
SECTION NAME
```

Example

```text
OPERATIONAL SNAPSHOT

ACTION REQUIRED

DATA TRUST
```

---

## Section Boundary

Render:

```text
Border

Container

Background Area
```

---

# SECTION 07 — VISUAL CONTAINER STANDARDS

## Purpose

Represent report visuals without implementing final visuals.

---

## Supported Container Types

```text
KPI Card Container

Status Card Container

Priority Table Container

Exception Matrix Container

Comparison Container

Ranking Container

Narrative Container

Filter Container
```

---

## Container Label

Every container must display:

```text
Container Type

Purpose
```

Example

```text
KPI CARD

Open Capacity
```

---

# SECTION 08 — LAYOUT FLOW STANDARDS

## Reading Pattern

Desktop Layout

```text
Left To Right

Top To Bottom
```

---

## Story Flow

```text
Context

↓

Attention Required

↓

Decision Support

↓

Analysis

↓

Trust

↓

Recommendations
```

---

## Render Requirement

The SVG should clearly show:

```text
Where Users Start

Where Users Continue

Where Users End
```

---

# SECTION 09 — FILTER RENDERING STANDARDS

## Location

Top Of Page

---

## Appearance

Render as:

```text
Filter Placeholder

Dropdown Placeholder

Selection Box
```

---

## Example

```text
+-----------+
| Region ▼  |
+-----------+

+-----------+
| Centre ▼  |
+-----------+

+-----------+
| Type ▼    |
+-----------+
```

---

## Filter Rule

Filters are represented only.

No logic required.

---

# SECTION 10 — TYPOGRAPHY STANDARDS

## Purpose

Improve readability.

---

## Font Family

Use generic:

```text
Sans Serif
```

---

## Font Sizes

Page Title

```text
24px
```

---

Section Headers

```text
18px
```

---

Container Labels

```text
14px
```

---

Supporting Text

```text
12px
```

---

# SECTION 11 — COLOR STANDARDS

## Mockup Colors Only

Use neutral colors.

---

## Recommended Palette

Page Background

```text
#FFFFFF
```

---

Section Background

```text
#F5F5F5
```

---

Border

```text
#D9D9D9
```

---

Text

```text
#333333
```

---

## Avoid

```text
Brand Colors

Conditional Formatting

Business Significance Colors
```

These belong to report implementation.

---

# SECTION 12 — SVG COMPONENT STANDARDS

## Allowed Components

```text
Rectangle

Rounded Rectangle

Text

Line

Arrow

Container

Header

Placeholder
```

---

## Disallowed Components

```text
Actual Charts

Actual KPIs

Actual Measures

Animated Objects

Decorative Graphics
```

---

# SECTION 13 — PLACEHOLDER STANDARDS

## Purpose

Represent future visuals.

---

## KPI Placeholder

```text
+-----------+
| KPI CARD  |
+-----------+
```

---

## Table Placeholder

```text
+----------------------+
| PRIORITY TABLE       |
+----------------------+
```

---

## Chart Placeholder

```text
+----------------------+
| RANKING CHART        |
+----------------------+
```

---

## Narrative Placeholder

```text
+----------------------+
| RECOMMENDATIONS      |
+----------------------+
```

---

# SECTION 14 — SVG QUALITY CHECKLIST

Before approval verify:

```text
□ DSC Approved

□ Mockup Approved

□ Layout Matches Mockup

□ Reading Order Visible

□ Visual Hierarchy Clear

□ Section Boundaries Clear

□ Containers Labeled

□ Filters Represented

□ No New Logic Added

□ Developer Ready
```

---

# SECTION 15 — DEVELOPER HANDOFF REQUIREMENTS

SVG must help developers understand:

```text
Section Placement

Visual Placement

Container Size

Reading Order

Page Structure
```

without requiring additional explanation.

---

# SECTION 16 — SVG APPROVAL GATE

Business Owner

☐ Approved

---

Report Designer

☐ Approved

---

UX Reviewer

☐ Approved

---

Architecture Review

☐ Approved

---

# SVG SUCCESS STATEMENT

An SVG succeeds when:

```text
Every Section
matches the Mockup

Every Mockup Element
matches the DSC

Every Container
supports a Story Section

Every Layout Element
supports Reading Flow
```

The SVG therefore becomes:

```text
A Visual Blueprint
```

rather than:

```text
A Report Design
```

---

# HANDOFF

Approved SVG becomes input for:

```text
TRD Agent

Report Build Agent

Future Power BI Development
```

and serves as the official visual layout specification for implementation.