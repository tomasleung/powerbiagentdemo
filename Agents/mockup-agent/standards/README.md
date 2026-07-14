# Standards Directory
## Mockup Agent v2.0

---

# Purpose

This folder contains all governing standards used by the Mockup Agent.

Standards define:

```text
Rules

Governance

Constraints

Design Principles

Required Behaviors
```

Standards do not generate outputs directly.

Instead, standards ensure all outputs are:

```text
Consistent

Traceable

Reusable

Decision-Driven
```

---

# Standards Overview

## MOCKUP_STANDARDS_v1.0.md

Purpose

```text
Define mockup design rules.

Control:

Information Hierarchy

Section Structure

Reading Order

Story Flow

Container Governance

Business Alignment
```

Key Question

```text
How should mockups be constructed?
```

---

## UX_THEME_STANDARD_v1.0.md

Purpose

```text
Define user experience standards.

Control:

Typography

Colors

Spacing

Component Design

Card Design

Visual Language

Accessibility
```

Key Question

```text
How should the prototype look and feel?
```

---

## LAYOUT_PATTERNS_v1.0.md

Purpose

```text
Define approved dashboard storytelling patterns.

Control:

Page Architecture

Section Order

Business Journey

ZIP / ZAP Flow

Reading Flow

Dashboard Layout
```

Key Question

```text
How should information be organized?
```

---

# Relationship Between Standards

```text
MOCKUP_STANDARDS

↓

Defines

What rules govern the mockup?
```

```text
LAYOUT_PATTERNS

↓

Defines

Where does information appear?
```

```text
UX_THEME_STANDARD

↓

Defines

How does the experience look?
```

---

# Mockup Agent Architecture

```text
REPORT_STORY (DSC)

+

MOCKUP_STANDARDS

+

LAYOUT_PATTERNS

+

UX_THEME_STANDARD

↓

Mockup Agent

↓

MOCKUP.md

↓

MOCKUP.svg
```

---

# Standard Usage

Every mockup generation must:

```text
Follow MOCKUP_STANDARDS

Select a LAYOUT_PATTERN

Apply a UX_THEME
```

The agent may not:

```text
Ignore approved standards

Create new layout patterns

Create new theme rules

Introduce conflicting governance
```

---

# Folder Contents

```text
MOCKUP_STANDARDS_v1.0.md

UX_THEME_STANDARD_v1.0.md

LAYOUT_PATTERNS_v1.0.md
```

---

# Success Statement

The Standards folder succeeds when:

```text
Every generated mockup

follows

the same decision-driven design principles
```

while allowing:

```text
Different Stories

Different Layout Patterns

Different UX Themes
```

to be implemented consistently.