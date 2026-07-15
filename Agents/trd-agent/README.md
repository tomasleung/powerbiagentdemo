# Semantic Design Agent
## Decision-Driven BI Framework

---

# Purpose

The Semantic Design Agent transforms approved technical design artifacts into governed semantic design artifacts.

The agent serves as the bridge between:

```text
Technical Design

↓

Semantic Design

↓

Semantic Implementation
```

The Semantic Design Agent answers:

```text
What semantic model must exist
to support the approved business decisions?
```

---

# RDLC Position

```text
BRD

↓

Decision Story Agent

↓

REPORT_STORY_MATRIX

↓

REPORT_STORY

↓

Mockup Agent

↓

MOCKUP

↓

SVG

↓

TRD Agent

↓

TRD

↓

Semantic Design Agent

↓

DATA_MODEL_MATRIX

↓

SEMANTIC_MODEL_SPEC

↓

MEASURE_CONTRACT

↓

Semantic Build Agent

↓

Microsoft Fabric Semantic Model

↓

Power BI Report
```

---

# Core Philosophy

The semantic model exists to support:

```text
Business Decisions
```

not:

```text
Source Systems
```

The Semantic Design Agent follows:

```text
Decision-Driven BI Principles

Kimball Standards

Microsoft Fabric Standards

SQLBI Best Practices

AI Readiness Standards
```

---

# Inputs

## Required

```text
TRD_vX.X.md

REPORT_STORY_vX.X.md
```

---

## Reference

```text
INPUT_BRD_vX.X.md

REPORT_STORY_MATRIX_vX.X.md
```

---

# Outputs

## Output 01

```text
DATA_MODEL_MATRIX_vX.X.md
```

Purpose:

```text
Business-to-Semantic Traceability
```

---

## Output 02

```text
SEMANTIC_MODEL_SPEC_vX.X.md
```

Purpose:

```text
Semantic Architecture Blueprint
```

---

## Output 03

```text
MEASURE_CONTRACT_vX.X.md
```

Purpose:

```text
Measure Governance Contract
```

---

# Standards

```text
standards/

DATA_MODEL_STANDARDS_v1.0.md
```

Defines:

```text
Semantic Modeling Standards

Fact Standards

Dimension Standards

Measure Standards

Relationship Standards

Fabric Standards
```

---

# Templates

```text
08_DATA_MODEL_MATRIX_TEMPLATE_v1.0.md

09_SEMANTIC_MODEL_SPEC_TEMPLATE_v1.0.md

10_MEASURE_CONTRACT_TEMPLATE_v1.0.md
```

---

# Guidelines

```text
SEMANTIC_DESIGN_GUIDELINES_v1.0.md
```

Defines:

```text
Modeling Guidance

Documentation Guidance

Validation Guidance

Handoff Guidance
```

---

# Workflow

```text
REPORT_STORY

+

TRD

↓

DATA_MODEL_MATRIX

↓

SEMANTIC_MODEL_SPEC

↓

MEASURE_CONTRACT
```

---

# Production Status

```text
Version: 1.0

Status: Production Ready

Validation: Animal Flow Test Run Passed
```

---

# Success Statement

The Semantic Design Agent succeeds when:

```text
Business Intent

↓

Semantic Architecture

↓

Measure Governance
```

remain fully traceable and implementation-ready.