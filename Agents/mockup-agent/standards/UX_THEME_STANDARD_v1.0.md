# UX_THEME_STANDARD_v1.0
## Decision-Driven BI UX Theme Standard

---

# Document Metadata

Document Name

UX_THEME_STANDARD

Version

1.0

Owner

Decision-Driven BI Framework

Status

Approved Standard

Purpose

Provide a standardized framework for defining, selecting, documenting, and applying dashboard UX themes.

This standard separates:

```text
Business Story

from

Visual Design
```

allowing the same story to be rendered using different visual styles while preserving business intent.

---

# SECTION 01 — UX PHILOSOPHY

## Core Principle

The theme supports the story.

The theme is not the story.

---

## Correct Relationship

```text
Decision
↓
Question
↓
Signal
↓
Action
↓
Story
↓
Layout
↓
Theme
↓
Mockup
↓
SVG
```

---

## UX Mission

Good UX should:

```text
Reduce Cognitive Load

Highlight Important Information

Improve Readability

Guide User Attention

Support Fast Decisions
```

---

# SECTION 02 — THEME FRAMEWORK

## Theme Definition

A UX Theme consists of:

```text
Typography

Color System

Spacing System

Component Library

Visual Language

Accessibility Rules
```

---

## Theme Categories

```text
Operational Command Centre

Executive Dashboard

Capacity Intelligence

Exception Monitoring

Investigative Dashboard

Narrative Intelligence

Board Reporting
```

---

# SECTION 03 — THEME SOURCES

## Supported Inputs

Themes may originate from:

```text
Power BI Theme JSON

Microsoft Fabric Community Themes

Figma

Adobe XD

Website Screenshots

Existing Dashboards

Corporate Design Systems

SVG Mockups
```

---

## Theme Extraction Rule

When theme assets exist:

Extract:

```text
Fonts

Colors

Spacing

Borders

Card Style

Layout Style

Visual Language
```

Generate:

```text
UX_THEME_PROFILE
```

---

# SECTION 04 — TYPOGRAPHY STANDARD

## Page Title

Example

```text
Segoe UI
32px
Bold
```

Purpose

```text
Primary Page Identity
```

---

## Section Header

Example

```text
Segoe UI
18px
Bold
```

Purpose

```text
Section Navigation
```

---

## Card Title

Example

```text
Segoe UI
12px
Semi Bold
```

Purpose

```text
KPI Description
```

---

## Card Value

Example

```text
Segoe UI
30px
Bold
```

Purpose

```text
Signal Emphasis
```

---

## Supporting Label

Example

```text
Segoe UI
12px
Regular
```

Purpose

```text
Supporting Information
```

---

# SECTION 05 — COLOR SYSTEM

## Neutral Palette

Background

```text
#F8FAFC
```

Surface

```text
#FFFFFF
```

Border

```text
#E2E8F0
```

Primary Text

```text
#111827
```

Secondary Text

```text
#64748B
```

---

# Status Colors

## Success

```text
#16A34A
```

Meaning

```text
Healthy
Safe
Good
```

---

## Warning

```text
#F59E0B
```

Meaning

```text
Review
Monitor
Attention
```

---

## Critical

```text
#DC2626
```

Meaning

```text
Risk
Failure
Escalation
```

---

## Information

```text
#2563EB
```

Meaning

```text
Insight
Observation
Context
```

---

# SECTION 06 — SPACING SYSTEM

Outer Margin

```text
40px
```

---

Section Gap

```text
40px
```

---

Card Gap

```text
20px
```

---

Internal Padding

```text
20px
```

---

# SECTION 07 — COMPONENT LIBRARY

## KPI Card

Structure

```text
Title

Value

Status
```

---

## Status Card

Structure

```text
Status

Count

Recommendation
```

---

## Exception Card

Structure

```text
Issue

Severity

Action
```

---

## Priority Table

Structure

```text
Entity

Signal

Status

Recommendation
```

---

## Narrative Card

Structure

```text
Observation

Impact

Recommendation
```

---

# SECTION 08 — CARD DESIGN STANDARD

Shape

```text
Rounded Rectangle
```

---

Corner Radius

```text
12px
```

---

Border

```text
1px
```

---

Shadow

```text
Soft Shadow
```

Optional

---

# SECTION 09 — VISUAL PERSONALITY

Desired Attributes

```text
Professional

Executive

Operational

Modern

Clean
```

Avoid

```text
Gaming Style

Decorative Effects

Heavy Animation

Visual Noise
```

---

# SECTION 10 — ACCESSIBILITY

Do Not Use:

```text
Color Alone
```

to communicate meaning.

Always support meaning with:

```text
Text

Icons

Labels
```

---

# SECTION 11 — THEME PROFILE

Every theme should document:

```text
Theme Name

Theme Category

Theme Source

Typography

Colors

Spacing

Components

Target Audience
```

---

# SECTION 12 — DEFAULT THEME RULE

If no theme is supplied:

Use:

```text
Decision-Driven BI Default Theme
```

---

If a theme is supplied:

```text
Theme JSON

Website

Screenshot

SVG

Figma
```

extract and apply:

```text
Typography

Colors

Spacing

Component Design

Visual Language
```

while preserving:

```text
Story

Layout

Business Logic
```

---

# UX SUCCESS STATEMENT

A UX Theme succeeds when:

```text
Visual Design

supports

Story
```

and:

```text
Story

never depends on

Visual Design
```