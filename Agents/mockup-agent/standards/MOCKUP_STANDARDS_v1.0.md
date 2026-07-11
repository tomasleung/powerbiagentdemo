# MOCKUP_STANDARDS_v1.0
## Decision-Driven BI Mockup Design Standards

---

# Document Metadata

Document Name

MOCKUP_STANDARDS

Version

1.0

Owner

Decision-Driven BI Framework

Status

Approved Standard

Purpose

Provide a governing framework for dashboard wireframes, page layouts, information hierarchy, and visual composition.

This standard ensures mockups are generated consistently, follow the approved Decision Story Contract (DSC), and maintain decision-driven storytelling.

---

# SECTION 01 — MOCKUP PHILOSOPHY

## Core Principle

The mockup exists to visualize the approved decision story.

The mockup does not create the story.

The mockup does not redefine the story.

The mockup visualizes the story.

---

## Correct Relationship

```text
Decision
↓
Question
↓
Signal
↓
Threshold
↓
Action
↓
Story
↓
DSC
↓
Mockup
```

---

## Incorrect Relationship

```text
Visual
↓
Dashboard
↓
Hope User Finds Insight
```

---

## Mockup Goal

The mockup should allow stakeholders to answer:

```text
What information appears?

Where does it appear?

Why does it appear?

What decision does it support?
```

before visual development begins.

---

# SECTION 02 — SINGLE SOURCE OF TRUTH

## Governing Document

The DSC is the source of truth.

```text
REPORT_STORY (DSC)
```

---

## Mockup Rule

The mockup must only contain:

```text
Approved Sections

Approved Story Flow

Approved KPIs

Approved Questions

Approved Visuals
```

---

## The Mockup May Not

Create:

```text
New KPIs

New Signals

New Questions

New Decisions

New Visual Sections

New Business Rules
```

---

# SECTION 03 — NARRATIVE FIRST DESIGN

## Governing Rule

Design follows story.

Never:

```text
Visual
↓
Story
```

Always:

```text
Story
↓
Visual
```

---

## Recommended Narrative Flow

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

Action
```

---

## Reader Journey

A user should naturally progress from:

```text
What Is Happening?

↓

What Requires Attention?

↓

What Decision Must Be Made?

↓

Why?

↓

Can I Trust It?

↓

What Should I Do?
```

---

# SECTION 04 — INFORMATION HIERARCHY

## Hierarchy Rule

Information importance determines placement.

---

## Tier 1

Mission Critical

Location

```text
Top Of Page
```

Examples

```text
Operational Snapshot

Action Required

Intake Readiness
```

---

## Tier 2

Decision Support

Location

```text
Middle Of Page
```

Examples

```text
Placement Board

Capacity Analysis

Operational Detail
```

---

## Tier 3

Supporting Context

Location

```text
Lower Page
```

Examples

```text
Data Trust

Regional Health

Trends
```

---

## Tier 4

Recommendations

Location

```text
Bottom Of Page
```

Examples

```text
Operational Briefing

AI Recommendations
```

---

# SECTION 05 — SECTION DESIGN STANDARDS

## Rule

Each section must answer one business question.

---

## Required Definition

Every section must contain:

```text
Business Question

Audience

Decision Supported

Purpose
```

---

## Section Validation

If a section cannot answer:

```text
Why does this exist?
```

the section should be removed.

---

# SECTION 06 — READING ORDER STANDARDS

## Reading Pattern

Desktop reading order:

```text
Left To Right

Top To Bottom
```

---

## Story Sequence

```text
1. Snapshot

2. Exceptions

3. Decisions

4. Analysis

5. Trust

6. Recommendations
```

---

## Validation

Users should not need to:

```text
Jump Randomly

Search For Information

Interpret Layout Logic
```

---

# SECTION 07 — FILTER DESIGN STANDARDS

## Purpose

Filters modify analysis.

Filters do not become the story.

---

## Preferred Placement

```text
Top Of Page
```

---

## Recommended Filters

```text
Date

Region

Centre

Animal Type

Status
```

---

## Filter Rule

Filters should support:

```text
Investigation

Segmentation

Comparison
```

---

# SECTION 08 — KPI DESIGN STANDARDS

## KPI Rule

KPIs must support decisions.

---

## Every KPI Must Define

```text
Signal

Threshold

Status

Action

Decision
```

---

## KPI Placement Rules

Mission-critical KPIs:

```text
Top Section
```

Supporting KPIs:

```text
Middle Sections
```

---

## KPI Validation

If the KPI does not influence:

```text
Decision

Action
```

remove it.

---

# SECTION 09 — VISUAL CONTAINER STANDARDS

## Purpose

Mockups define containers.

Not final visuals.

---

## Allowed Containers

```text
KPI Card Container

Status Card Container

Priority Table Container

Exception List Container

Comparison Container

Ranking Container

Narrative Container
```

---

## Container Rule

Containers should describe:

```text
Purpose

Data Role

Supported Decision
```

not technical implementation.

---

# SECTION 10 — WIREFRAME STANDARDS

## Mockup Fidelity

Mockups are:

```text
Structure First
```

not:

```text
Visual Design First
```

---

## Represent

```text
Layout

Sections

Visual Locations

Reading Sequence
```

---

## Do Not Represent

```text
Colors

Fonts

Themes

Branding

Artistic Effects
```

---

# SECTION 11 — PAGE DESIGN STANDARDS

## One Page = One Story

Every page must support:

```text
Single Primary Decision
```

---

## Avoid

```text
Multiple Unrelated Decisions

Multiple Report Purposes
```

on a single page.

---

## Validation

Users should immediately understand:

```text
Why This Page Exists
```

within seconds.

---

# SECTION 12 — SVG DESIGN STANDARDS

## SVG Purpose

The SVG is a rendering artifact.

---

## SVG May

Render:

```text
Sections

Containers

Flow

Hierarchy

Layout
```

---

## SVG Must Not

Invent:

```text
Questions

KPIs

Signals

Tables

Business Logic

Thresholds
```

---

## SVG Rule

Everything shown in the SVG must exist in:

```text
Approved DSC

Approved Mockup
```

---

# SECTION 13 — RESPONSIVE LAYOUT STANDARDS

## Desktop First

Primary mockup target:

```text
Power BI Desktop
```

---

## Layout Design

Use:

```text
Horizontal Sections

Logical Grouping

Consistent Container Size
```

---

## Avoid

```text
Crowded Layouts

Excessive Scrolling

Orphan Sections
```

---

# SECTION 14 — MOCKUP QUALITY CHECKLIST

Before approval verify:

```text
□ Uses Approved DSC

□ No New Logic Added

□ Story Flow Preserved

□ Information Hierarchy Clear

□ Reading Order Clear

□ Decision Support Visible

□ KPI Placement Logical

□ Sections Have Purpose

□ Visual Containers Defined

□ SVG Can Be Generated
```

---

# MOCKUP SUCCESS STATEMENT

A mockup succeeds when:

```text
Every Section
supports a Question

Every Question
supports a Decision

Every Visual Container
supports a Section

Every Layout Element
supports the Story
```

The mockup therefore becomes:

```text
A Story Visualization Artifact
```

rather than:

```text
A Dashboard Sketch
```

---

# HANDOFF

Upon approval the mockup becomes input for:

```text
SVG Generation

TRD Agent

Future Report Build Agent
```

and serves as the official visualization blueprint for report implementation.