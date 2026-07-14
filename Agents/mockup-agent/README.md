# Mockup Agent v2.0
## Decision-Driven BI Framework

---

# Purpose

The Mockup Agent converts an approved Decision Story Contract (DSC) into:

```text
Business Review Mockup

(MOCKUP.md)

↓

Visual Prototype

(MOCKUP.svg)
```

before technical design begins.

The Mockup Agent ensures stakeholders can validate:

```text
What appears?

Where does it appear?

Why does it appear?
```

before Power BI development occurs.

---

# RDLC Position

```text
BRD

↓

Decision Story Agent

↓

REPORT_STORY_MATRIX

↓

REPORT_STORY (DSC)

↓

Mockup Agent

↓

MOCKUP.md

↓

MOCKUP.svg

↓

TRD Agent
```

---

# Inputs

## Required

```text
REPORT_STORY_vX.X.md
```

---

# Standards

Located in:

```text
standards/
```

Files:

```text
MOCKUP_STANDARDS_v1.0.md

UX_THEME_STANDARD_v1.0.md

LAYOUT_PATTERNS_v1.0.md
```

---

# Templates

Located in:

```text
templates/
```

Files:

```text
03_MOCKUP_TEMPLATE_v1.0.md

04_SVG_TEMPLATE_v1.0.md
```

---

# Guidelines

Located in:

```text
guidelines/
```

Files:

```text
SVG_GUIDELINES_v1.0.md
```

---

# Outputs

## Output 01

```text
MOCKUP_vX.X.md
```

Purpose:

```text
Business Review Artifact
```

---

## Output 02

```text
MOCKUP_vX.X.svg
```

Purpose:

```text
Visual Prototype Artifact
```

---

# Workflow

```text
REPORT_STORY

↓

Select Layout Pattern

↓

Generate MOCKUP.md

↓

Apply UX Theme

↓

Apply SVG Template

↓

Apply SVG Guidelines

↓

Generate MOCKUP.svg
```

---

# Validation

Before completion verify:

```text
✓ Story Preserved

✓ Layout Pattern Applied

✓ Section Order Preserved

✓ Information Hierarchy Clear

✓ UX Theme Applied

✓ SVG Generated
```

---

# Success Statement

The Mockup Agent succeeds when:

```text
The approved story

becomes

an approved visual prototype
```

without introducing new business logic.