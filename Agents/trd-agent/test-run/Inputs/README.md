# Inputs Directory
## TRD Agent v1.0

---

# Purpose

This folder contains all approved input artifacts required by the TRD Agent.

Inputs represent completed and approved deliverables from previous phases of the Decision-Driven BI Framework.

The TRD Agent consumes these artifacts and transforms them into:

```text
TRD_vX.X.md
```

---

# Input Philosophy

Inputs are the official source of truth.

The TRD Agent must:

```text
Read

Interpret

Trace

Document
```

The TRD Agent must not:

```text
Redesign

Rewrite

Replace

Override
```

approved business design artifacts.

---

# Input Flow

```text
BRD

↓

REPORT_STORY_MATRIX

↓

REPORT_STORY (DSC)

↓

MOCKUP.md

↓

MOCKUP.svg

↓

TRD Agent
```

---

# Required Inputs

## Input 01

### BRD

Artifact

```text
Business Requirements Document
```

Purpose

```text
Capture business objectives.

Capture business requirements.

Capture stakeholder expectations.

Capture scope.
```

---

## Input 02

### REPORT_STORY_MATRIX

Artifact

```text
REPORT_STORY_MATRIX_vX.X.md
```

Purpose

```text
Document:

Decisions

Business Questions

Signals

Thresholds

Actions

Story Flow
```

---

## Input 03

### REPORT_STORY (DSC)

Artifact

```text
REPORT_STORY_vX.X.md
```

Purpose

```text
Provide the approved Decision Story Contract.
```

Contains

```text
Decision Model

Signal Matrix

Threshold Matrix

Action Matrix

Narrative Story

Layout Blueprint

Visual Recommendations
```

---

## Input 04

### MOCKUP.md

Artifact

```text
MOCKUP_vX.X.md
```

Purpose

```text
Provide approved business-review layout.

Document:

Story Flow

Section Structure

Visual Containers

Information Hierarchy
```

---

## Input 05

### MOCKUP.svg

Artifact

```text
MOCKUP_vX.X.svg
```

Purpose

```text
Provide approved visual prototype.

Document:

Visual Layout

Section Placement

UX Structure

Information Presentation
```

---

# Input Priority

When conflicts exist:

```text
Priority 1

REPORT_STORY (DSC)
```

↓

```text
Priority 2

MOCKUP.md
```

↓

```text
Priority 3

MOCKUP.svg
```

↓

```text
Priority 4

BRD
```

↓

```text
Priority 5

REPORT_STORY_MATRIX
```

---

# Source Of Truth

The primary source of truth is:

```text
REPORT_STORY (DSC)
```

The DSC owns:

```text
Decisions

Questions

Signals

Thresholds

Actions

Story Flow
```

---

# Input Validation Checklist

Before generating a TRD verify:

```text
□ BRD Available

□ REPORT_STORY_MATRIX Available

□ REPORT_STORY Available

□ MOCKUP.md Available

□ MOCKUP.svg Available

□ Artifacts Approved

□ Story Flow Exists

□ Visual Mapping Exists

□ Layout Blueprint Exists

□ Decision Model Exists
```

---

# Recommended Folder Structure

```text
inputs/

README.md

INPUT_BRD_*.md

REPORT_STORY_MATRIX_vX.X.md

REPORT_STORY_vX.X.md

MOCKUP_vX.X.md

MOCKUP_vX.X.svg
```

---

# Relationship To Outputs

Inputs provide:

```text
Business Design
```

Outputs provide:

```text
Technical Design
```

Flow:

```text
Inputs

↓

TRD Agent

↓

TRD_vX.X.md
```

---

# Input Ownership

| Artifact | Owner |
|-----------|-----------|
| BRD | Business |
| REPORT_STORY_MATRIX | Decision Story Agent |
| REPORT_STORY (DSC) | Decision Story Agent |
| MOCKUP.md | Mockup Agent |
| MOCKUP.svg | Mockup Agent |

---

# Current Approved Example

## Animal Flow — Live Capacity Reporting

Required Inputs

```text
INPUT_BRD_AnimalFlow_LiveCapacity_v2.0.md

REPORT_STORY_MATRIX_v1.0.md

REPORT_STORY_v1.0.md

MOCKUP_v2.0.md

MOCKUP_v2.0.svg
```

These inputs are used to generate:

```text
TRD_v1.0.md
```

---

# Success Statement

The Inputs folder succeeds when:

```text
All required approved artifacts
are available,

traceable,

and ready for technical documentation.
```

The result is:

```text
A Reliable

Governed

Decision-Driven

Technical Design Process
```

where every TRD is built from approved business design artifacts.