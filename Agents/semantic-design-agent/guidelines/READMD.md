# Guidelines
## Semantic Design Agent

---

# Purpose

This folder contains all implementation guidance used by the Semantic Design Agent.

Guidelines explain:

```text
How To Apply Standards

How To Use Templates

How To Create Outputs

How To Validate Outputs
```

Unlike standards, guidelines provide recommended practices and execution guidance.

---

# Current Guideline

## SEMANTIC_DESIGN_GUIDELINES_v1.0.md

Purpose:

```text
Provide practical guidance for
creating semantic design artifacts
within the Decision-Driven BI Framework.
```

---

# Guideline Coverage

## Semantic Design Philosophy

Defines:

```text
Decision First

Business First

Traceability First
```

The semantic model exists to support:

```text
Business Decisions
```

not:

```text
Source Systems
```

---

## Input Usage Guidance

Defines:

```text
Required Inputs

Reference Inputs

Input Priority
```

Input precedence:

```text
REPORT_STORY

↓

TRD

↓

REPORT_STORY_MATRIX

↓

BRD
```

---

## DATA_MODEL_MATRIX Guidance

Defines:

```text
Business Validation

Signal Identification

Measure Identification

Fact Identification

Dimension Identification
```

Focus:

```text
Business Structure

Not Technical Design
```

---

## SEMANTIC_MODEL_SPEC Guidance

Defines:

```text
Fact Design

Dimension Design

Column Design

Relationship Design

Hierarchy Design
```

Focus:

```text
Semantic Architecture
```

---

## MEASURE_CONTRACT Guidance

Defines:

```text
Business Definitions

Business Formulas

Thresholds

Actions

Ownership

Dependencies
```

Focus:

```text
Measure Governance
```

---

## Fact Design Guidance

Defines:

```text
Grain First

Fact Qualification

Business Purpose

Measure Alignment
```

---

## Dimension Design Guidance

Defines:

```text
Business Context

Filtering

Grouping

Drill Down

Conformed Dimensions
```

---

## Relationship Guidance

Defines:

```text
One-To-Many

Single Direction

Business Navigation
```

Preferred Pattern:

```text
Dimension

↓

Fact
```

---

## Performance Guidance

Defines:

```text
Star Schema

Lean Models

Reduced Cardinality

Fabric Optimization
```

---

## AI Readiness Guidance

Defines:

```text
Business Documentation

Object Descriptions

Decision Traceability

Copilot Readiness
```

Goal:

```text
AI agents can explain
why semantic objects exist
without external documentation.
```

---

# Relationship To Standards

```text
Standards

Define Rules

↓

Guidelines

Explain Application
```

Standards answer:

```text
What Is Required?
```

Guidelines answer:

```text
How Should It Be Applied?
```

---

# Relationship To Templates

```text
Guidelines

↓

Templates

↓

Outputs
```

Guidelines help ensure consistent use of templates.

---

# Agent Dependency

The Semantic Design Agent should always consult:

```text
SEMANTIC_DESIGN_GUIDELINES_v1.0.md
```

during:

```text
DATA_MODEL_MATRIX Creation

SEMANTIC_MODEL_SPEC Creation

MEASURE_CONTRACT Creation
```

---

# Validation

Before approving an output verify:

```text
□ Standards Applied

□ Templates Followed

□ Traceability Preserved

□ Grain Defined

□ Decision Coverage Complete

□ Measure Governance Defined
```

---

# Success Statement

The Guidelines folder succeeds when:

```text
Semantic Design Artifacts

are created consistently,

reviewed consistently,

and handed off consistently
```

across all future BI initiatives.

The result is:

```text
Repeatable

Governed

Decision-Driven

Semantic Design Practices
```