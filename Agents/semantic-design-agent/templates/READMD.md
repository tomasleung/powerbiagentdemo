# Templates
## Semantic Design Agent

---

# Purpose

This folder contains all official output templates used by the Semantic Design Agent.

Templates define:

```text
Document Structure

Required Sections

Required Metadata

Validation Requirements

Handoff Requirements
```

Templates ensure generated artifacts remain:

```text
Consistent

Governed

Reusable

Reviewable
```

across all semantic design projects.

---

# Current Templates

## 08_DATA_MODEL_MATRIX_TEMPLATE_v1.0.md

Purpose:

```text
Business-To-Semantic Traceability
```

Documents:

```text
Decisions

Business Questions

Signals

Measures

Facts

Dimensions
```

Answers:

```text
Why does this semantic model exist?

Why does this fact exist?

Why does this dimension exist?
```

Output:

```text
DATA_MODEL_MATRIX_vX.X.md
```

---

## 09_SEMANTIC_MODEL_SPEC_TEMPLATE_v1.0.md

Purpose:

```text
Semantic Architecture Blueprint
```

Documents:

```text
Fact Tables

Dimension Tables

Columns

Relationships

Cardinality

Filter Direction

Hierarchy Design

Performance Design
```

Answers:

```text
What semantic model must be built?
```

Output:

```text
SEMANTIC_MODEL_SPEC_vX.X.md
```

---

## 10_MEASURE_CONTRACT_TEMPLATE_v1.0.md

Purpose:

```text
Measure Governance Specification
```

Documents:

```text
Business Definitions

Business Logic

Thresholds

Actions

Dependencies

Ownership

Formatting

Visual Mapping
```

Answers:

```text
How should measures behave?

How should decisions be supported?
```

Output:

```text
MEASURE_CONTRACT_vX.X.md
```

---

# Output Sequence

Templates must always be executed in this order:

```text
DATA_MODEL_MATRIX

↓

SEMANTIC_MODEL_SPEC

↓

MEASURE_CONTRACT
```

Never skip a template.

Each template depends on the output produced by the previous template.

---

# Template Relationships

```text
DATA_MODEL_MATRIX

Validates Business Structure

↓

SEMANTIC_MODEL_SPEC

Designs Semantic Architecture

↓

MEASURE_CONTRACT

Defines Measure Governance
```

---

# Template Governance

Templates define:

```text
Required Structure
```

Templates do not define:

```text
Business Logic

Requirements

Decisions

Signals
```

Those are derived from approved inputs.

---

# Agent Dependency

The Semantic Design Agent must generate outputs using these templates.

Outputs generated outside these templates are considered:

```text
Non-Standard

Non-Governed

Framework Non-Compliant
```

---

# Validation

Before approving an output verify:

```text
□ Required Sections Present

□ Metadata Complete

□ Traceability Preserved

□ Validation Sections Completed

□ Handoff Sections Completed
```

---

# Success Statement

The Templates folder succeeds when:

```text
All Semantic Design Outputs

follow a consistent structure,

support a consistent review process,

and provide a repeatable handoff
to Semantic Build activities.
```

The result is:

```text
Predictable

Governed

Enterprise-Grade

Semantic Design Documentation
```