# Standards
## Semantic Design Agent

---

# Purpose

This folder contains all governing standards used by the Semantic Design Agent.

Standards define:

```text
What Good Looks Like

Required Modeling Rules

Required Governance Rules

Required Validation Rules
```

Standards are mandatory.

Templates and outputs must comply with these standards.

---

# Current Standards

## DATA_MODEL_STANDARDS_v1.0

Purpose:

```text
Define enterprise semantic modeling standards
for Decision-Driven BI solutions.
```

Includes:

```text
Decision-Driven BI Principles

Kimball Dimensional Modeling

Microsoft Fabric Standards

SQLBI Best Practices

AI Readiness Standards
```

---

# Standards Coverage

The standard governs:

## Decision Traceability

```text
Decision

↓

Business Question

↓

Signal

↓

Measure

↓

Fact

↓

Dimension
```

---

## Fact Design

Defines:

```text
Fact Identification

Fact Qualification

Fact Naming

Fact Governance

Fact Validation
```

---

## Dimension Design

Defines:

```text
Dimension Identification

Conformed Dimensions

Dimension Governance

Dimension Validation
```

---

## Measure Design

Defines:

```text
Base Measures

Derived Measures

Presentation Measures

Measure Traceability

Measure Governance
```

---

## Relationship Design

Defines:

```text
Cardinality

Filter Direction

Relationship Governance
```

---

## Semantic Architecture

Defines:

```text
Star Schema

Conformed Dimensions

One-To-Many Relationships

Performance Standards
```

---

## Fabric Standards

Defines:

```text
Semantic Model Standards

Business Naming

Model Simplicity

Performance Optimization
```

---

## AI Readiness

Defines:

```text
Documentation Requirements

Business Definitions

Semantic Discoverability

Copilot Readiness
```

---

# Agent Dependency

The Semantic Design Agent must always follow:

```text
DATA_MODEL_STANDARDS_v1.0.md
```

before generating:

```text
DATA_MODEL_MATRIX

SEMANTIC_MODEL_SPEC

MEASURE_CONTRACT
```

---

# Standards Hierarchy

```text
DATA_MODEL_STANDARDS

↓

Semantic Design Agent

↓

DATA_MODEL_MATRIX

↓

SEMANTIC_MODEL_SPEC

↓

MEASURE_CONTRACT
```

---

# Success Statement

The Standards folder succeeds when:

```text
Every Semantic Design Artifact

is generated

using the same modeling rules,

governance rules,

and validation standards.
```

The result is:

```text
Consistent

Governed

Reusable

Decision-Driven Semantic Models
```