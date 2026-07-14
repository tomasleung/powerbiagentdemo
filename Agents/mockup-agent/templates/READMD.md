# Templates Directory
## Mockup Agent v2.0

---

# Purpose

This folder contains all reusable templates used by the Mockup Agent.

Templates define:

```text
Structure

Sections

Placeholders

Expected Output Format
```

Templates do not define:

```text
Business Logic

Story Content

Theme Rules

Layout Rules

Rendering Rules
```

These are provided by:

```text
REPORT_STORY

MOCKUP_STANDARDS

LAYOUT_PATTERNS

UX_THEME_STANDARD

SVG_GUIDELINES
```

---

# Templates Overview

## 03_MOCKUP_TEMPLATE_v1.0.md

Purpose

```text
Generate:

MOCKUP_vX.X.md
```

Role

```text
Business Review Template
```

Defines:

```text
Document Structure

Section Structure

Business Questions

Decision Support

Visual Containers

Layout Pattern Documentation

Validation Checklist
```

Key Question

```text
What should appear in the report?
```

---

## 04_SVG_TEMPLATE_v1.0.md

Purpose

```text
Generate:

MOCKUP_vX.X.svg
```

Role

```text
Visual Prototype Template
```

Defines:

```text
SVG Skeleton

Header Region

Filter Region

Section Regions

Card Regions

Container Structure

Rendering Placeholders
```

Key Question

```text
How should the SVG be structured?
```

---

# Template Usage

Templates are populated by the Mockup Agent using:

```text
REPORT_STORY (DSC)

+

LAYOUT_PATTERNS

+

UX_THEME_STANDARD
```

---

# Template Flow

```text
REPORT_STORY

↓

03_MOCKUP_TEMPLATE

↓

MOCKUP.md

↓

04_SVG_TEMPLATE

↓

MOCKUP.svg
```

---

# Relationship To Standards

Templates define:

```text
Structure
```

Standards define:

```text
Rules
```

Example:

```text
MOCKUP_TEMPLATE

defines

WHERE sections are documented.
```

```text
MOCKUP_STANDARDS

defines

HOW sections must behave.
```

---

# Relationship To Guidelines

Templates define:

```text
Output Skeleton
```

Guidelines define:

```text
Rendering Rules

Spacing

Margins

Accessibility

SVG Compliance
```

Example:

```text
SVG_TEMPLATE

defines

the SVG structure.
```

```text
SVG_GUIDELINES

defines

how the SVG should be rendered.
```

---

# Folder Contents

```text
03_MOCKUP_TEMPLATE_v1.0.md

04_SVG_TEMPLATE_v1.0.md
```

---

# Generated Outputs

Using the templates produces:

```text
MOCKUP_vX.X.md

MOCKUP_vX.X.svg
```

---

# Success Statement

The Templates folder succeeds when:

```text
Every Mockup

uses a consistent structure
```

and:

```text
Every SVG

uses a predictable prototype framework
```

allowing the Mockup Agent to generate repeatable and reviewable outputs across all Decision-Driven BI projects.