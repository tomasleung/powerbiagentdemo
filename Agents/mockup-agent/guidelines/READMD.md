# Guidelines Directory
## Mockup Agent v2.0

---

# Purpose

This folder contains rendering and implementation guidance used by the Mockup Agent.

Guidelines define:

```text
Rendering Rules

Layout Compliance

Spacing Rules

Accessibility Requirements

Presentation Standards

Implementation Constraints
```

Guidelines do not define:

```text
Business Logic

Story Design

Layout Patterns

Theme Selection

Output Structure
```

These responsibilities belong to:

```text
REPORT_STORY

MOCKUP_STANDARDS

LAYOUT_PATTERNS

UX_THEME_STANDARD

Templates
```

---

# Guidelines Overview

## SVG_GUIDELINES_v1.0.md

Purpose

```text
Provide rendering instructions for SVG prototype generation.
```

---

## Controls

```text
Canvas Standards

Margins

Spacing

Section Rendering

Container Rendering

Typography Application

Color Application

Accessibility

SVG Compliance

Story Flow Compliance
```

---

## Key Question

```text
How should the approved mockup be rendered?
```

---

# Relationship To Standards

Standards define:

```text
Rules
```

Guidelines define:

```text
Execution
```

Example

```text
LAYOUT_PATTERNS

defines

Where content should appear.
```

```text
SVG_GUIDELINES

defines

How the layout should be rendered.
```

---

# Relationship To Templates

Templates define:

```text
Structure
```

Guidelines define:

```text
Rendering Behavior
```

Example

```text
04_SVG_TEMPLATE_v1.0

defines

SVG Regions
```

```text
SVG_GUIDELINES

defines

How those regions should behave.
```

---

# SVG Generation Flow

```text
REPORT_STORY

↓

MOCKUP.md

↓

SVG_TEMPLATE

↓

UX_THEME

↓

SVG_GUIDELINES

↓

MOCKUP.svg
```

---

# Rendering Responsibilities

The SVG renderer must follow:

```text
Approved Story Flow

Approved Layout Pattern

Approved UX Theme

Approved SVG Template
```

---

## The SVG Renderer Must

```text
Preserve Section Order

Preserve Reading Flow

Preserve Information Hierarchy

Apply Theme Consistently

Apply ZIP / ZAP Layout

Support Business Review
```

---

## The SVG Renderer Must Not

```text
Create New Sections

Change Story Sequence

Add Business Logic

Create New Decisions

Create New KPIs

Ignore Layout Patterns
```

---

# Story Flow Compliance

The renderer must preserve:

```text
REPORT_STORY Layout Blueprint
```

and

```text
Selected Layout Pattern
```

exactly.

---

## Valid

```text
Snapshot

↓

Action Required

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

## Invalid

```text
Snapshot

↓

Recommendations

↓

Analysis

↓

Trust
```

---

# Accessibility Responsibilities

SVG output should:

```text
Remain Readable

Maintain Visual Hierarchy

Use Clear Labels

Support High Contrast

Avoid Overcrowding
```

---

# Folder Contents

```text
SVG_GUIDELINES_v1.0.md
```

---

# Generated Output

Guidelines are applied during generation of:

```text
MOCKUP_vX.X.svg
```

---

# Success Statement

The Guidelines folder succeeds when:

```text
Every generated SVG

renders consistently

and

faithfully represents the approved mockup.
```

The result is:

```text
A Business Review Prototype

rather than

A Technical Wireframe
```