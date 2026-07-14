# 09_SEMANTIC_MODEL_SPEC_TEMPLATE_v1.0
## Semantic Model Specification

---

# Document Metadata

Document Type

```text
Semantic Model Specification
```

Version

```text
[Version]
```

Capability Name

```text
[Capability Name]
```

Artifact Type

```text
SEMANTIC_MODEL_SPEC
```

Owner

```text
[Owner]
```

Status

```text
Draft
```

Purpose

Define the detailed semantic model architecture required to support approved business decisions, signals, measures, and reporting requirements.

This document expands the approved:

```text
DATA_MODEL_MATRIX
```

into a complete semantic architecture blueprint.

---

# Related Artifacts

```text
INPUT_BRD_vX.X.md

REPORT_STORY_MATRIX_vX.X.md

REPORT_STORY_vX.X.md

TRD_vX.X.md

DATA_MODEL_MATRIX_vX.X.md

DATA_MODEL_STANDARDS_v1.0.md
```

---

# SECTION 01 — MODEL OVERVIEW

## Capability Name

```text
[Capability Name]
```

---

## Business Purpose

```text
[Purpose]
```

---

## Primary Decision Supported

```text
[Primary Decision]
```

---

## Secondary Decisions Supported

```text
[List]
```

---

## Architecture Pattern

```text
Star Schema
```

---

## Design Standards

```text
Decision-Driven BI Standards

Kimball Standards

Microsoft Fabric Standards

SQLBI Standards

Performance-Aware Modeling
```

---

## Semantic Modeling Objective

```text
Describe how the semantic model supports
approved decisions, signals, measures,
and reporting requirements.
```

---

## Performance Note

```text
Favor numeric surrogate keys.

Keep fact tables narrow.

Minimize high-cardinality attributes.

Support scalable Power BI and Fabric semantic models.
```

---

# SECTION 02 — SEMANTIC MODEL ARCHITECTURE

## Architecture Type

```text
Import

Direct Lake

DirectQuery

Hybrid
```

---

## Conceptual Architecture

```text
                 [Dim_Date]
                       │
                       ▼

[Dim_Centre] ───── [Fact_A]

      │

      ├────────── [Fact_B]

      │

      └────────── [Fact_C]


[Dim_AnimalType]

      ├────────── [Fact_A]

      └────────── [Fact_B]


[Dim_Region]

      │
      ▼

[Dim_Centre]
```

---

## Architecture Notes

```text
Conformed Dimensions

Role Playing Dimensions

Shared Dimensions

Bridge Tables

Special Design Considerations
```

---

# SECTION 03 — FACT TABLE DEFINITIONS

## Fact Table

### Table Name

```text
[Fact_Name]
```

---

### Business Name

```text
[Business Name]
```

---

### Description

```text
[Description]
```

---

### Business Purpose

```text
[Purpose]
```

---

### Business Grain

```text
[Grain]
```

Example:

```text
One Centre

+

One Date

+

One Animal Type
```

---

### Source Systems

```text
[List]
```

---

### Supported Decisions

```text
[List]
```

---

### Supported Signals

```text
[List]
```

---

### Supported Measures

```text
[List]
```

---

### Fact Columns

| Column Name | Business Name | Data Type | Description |
|------------|------------|------------|------------|
| [Column] | [Business Name] | [Type] | [Description] |

---

### Notes

```text
Design Notes

Business Rules

Special Considerations
```

---

## Fact Validation

Verify:

```text
□ Grain Defined

□ Source Identified

□ Measures Identified

□ Decisions Identified

□ Signals Identified

□ Business Purpose Defined
```

---

Repeat for every fact table.

---

# FACT INVENTORY SUMMARY

| Fact Table | Grain | Measures | Source Systems |
|------------|------------|------------|------------|
| [Fact] | [Grain] | [Measures] | [Sources] |
| [Fact] | [Grain] | [Measures] | [Sources] |

---

# SECTION 04 — DIMENSION TABLE DEFINITIONS

## Dimension

### Table Name

```text
[Dim_Name]
```

---

### Business Name

```text
[Business Name]
```

---

### Description

```text
[Description]
```

---

### Business Purpose

```text
[Purpose]
```

---

### Primary Key

```text
[Key]
```

---

### Source System

```text
[Source]
```

---

### Facts Supported

```text
[List]
```

---

### Dimension Attributes

| Column Name | Business Name | Data Type | Description |
|------------|------------|------------|------------|
| [Attribute] | [Business Name] | [Type] | [Description] |

---

### Hierarchies

```text
[List]
```

---

### Business Usage

```text
Filtering

Grouping

Drill Down

Segmentation

Analysis
```

---

### Notes

```text
Conformed Dimension Notes

Data Quality Notes

Special Modeling Rules
```

---

Repeat for every dimension.

---

# DIMENSION INVENTORY SUMMARY

| Dimension | Business Purpose | Facts Supported |
|------------|------------|------------|
| [Dimension] | [Purpose] | [Facts] |
| [Dimension] | [Purpose] | [Facts] |

---

# SECTION 05 — COLUMN SPECIFICATIONS

## Fact Columns

### Column Name

```text
[Column Name]
```

---

### Business Name

```text
[Business Name]
```

---

### Data Type

```text
[Type]
```

---

### Description

```text
[Description]
```

---

### Source Column

```text
[Source Column]
```

---

### Business Rule

```text
[Rule]
```

---

Repeat as required.

---

## Dimension Columns

### Column Name

```text
[Column Name]
```

---

### Business Name

```text
[Business Name]
```

---

### Data Type

```text
[Type]
```

---

### Description

```text
[Description]
```

---

### Business Meaning

```text
[Meaning]
```

---

Repeat as required.

---

# SECTION 06 — RELATIONSHIP DEFINITIONS

## Relationship

### Parent Table

```text
[Parent]
```

---

### Child Table

```text
[Child]
```

---

### Join Key

```text
[Key]
```

---

### Cardinality

```text
One-to-Many

Many-to-One

Many-to-Many
```

---

### Filter Direction

```text
Single Direction

Both Directions
```

---

### Business Purpose

```text
[Purpose]
```

---

Repeat for every relationship.

---

# RELATIONSHIP MATRIX

| Parent | Child | Join Key | Cardinality | Filter Direction |
|----------|----------|----------|----------|----------|
| [Parent] | [Child] | [Key] | [Type] | [Direction] |
| [Parent] | [Child] | [Key] | [Type] | [Direction] |

---

# SECTION 07 — CARDINALITY & FILTER STRATEGY

## Default Pattern

```text
One-To-Many

Single Direction

Dimension → Fact
```

---

## Exceptions

```text
[List]
```

---

## Justification

```text
Business Need

Performance Review

Modeling Constraints
```

---

# SECTION 08 — CONFORMED DIMENSIONS

## Shared Dimension

### Dimension Name

```text
[Dimension]
```

---

### Used By

```text
[List]
```

---

### Business Purpose

```text
[Purpose]
```

---

### Governance Rules

```text
Consistent Definitions

Consistent Attributes

Consistent Hierarchies

Reusable Across Facts
```

---

Repeat for every conformed dimension.

---

# SECTION 09 — HIERARCHY DESIGN

## Hierarchy

### Hierarchy Name

```text
[Hierarchy]
```

---

### Levels

```text
Level 1

↓

Level 2

↓

Level 3
```

---

### Business Purpose

```text
[Purpose]
```

---

Repeat as required.

---

# SECTION 10 — SECURITY MODEL SUPPORT

## Security Dimensions

```text
[List]
```

---

## Security Attributes

```text
[List]
```

---

## Future RLS Considerations

```text
Regional Security

Centre Security

Department Security

Executive Access
```

---

# SECTION 11 — PERFORMANCE DESIGN

## Optimization Strategy

```text
Star Schema

Explicit Measures

Conformed Dimensions

Reduced Cardinality

Surrogate Keys
```

---

## High Cardinality Review

| Column | Reason | Action |
|----------|----------|----------|
| [Column] | [Reason] | [Action] |

---

## Performance Rules

```text
Keep Fact Tables Narrow

Use Integer Surrogate Keys

Minimize String Filtering

Avoid Unnecessary Snowflaking

Prefer Single Direction Filtering
```

---

## Optimization Notes

```text
[List]
```

---

# SECTION 12 — AI READINESS

## Table Documentation

Verify:

```text
□ Business Purpose

□ Description

□ Declared Grain
```

---

## Column Documentation

Verify:

```text
□ Business Meaning

□ Description
```

---

## Relationship Documentation

Verify:

```text
□ Relationship Purpose Explained
```

---

## AI Readiness Goal

An AI Agent should explain:

```text
Why the table exists

Why the dimension exists

Why the relationship exists

Which measures are supported

Which decision is supported
```

without additional documentation.

---

# SECTION 13 — DECISION COVERAGE

## Decision Coverage Matrix

| Decision | Facts | Dimensions | Status |
|-----------|-----------|-----------|-----------|
| [Decision] | [Facts] | [Dimensions] | Complete |

---

## Validation Rule

Every decision must be supported by:

```text
Fact Tables

Dimensions

Measures

Relationships
```

---

# SECTION 14 — SIGNAL COVERAGE

## Signal Coverage Matrix

| Signal | Fact | Measure | Status |
|-----------|-----------|-----------|-----------|
| [Signal] | [Fact] | [Measure] | Complete |

---

## Validation Rule

Every signal must trace to:

```text
Measure

↓

Fact

↓

Dimension
```

---

# SECTION 15 — MODEL VALIDATION

Verify:

```text
□ Star Schema Implemented

□ Grain Defined

□ Facts Defined

□ Dimensions Defined

□ Columns Defined

□ Relationships Defined

□ Cardinality Defined

□ Filter Directions Defined

□ Conformed Dimensions Reviewed

□ Decision Coverage Complete

□ Signal Coverage Complete

□ Performance Reviewed

□ AI Readiness Reviewed
```

---

# SECTION 16 — HANDOFF TO MEASURE CONTRACT

## Required Approvers

```text
Data Architect

BI Architect

Analytics Lead
```

---

## Approval Status

```text
Draft

Review

Approved
```

---

## Output Upon Approval

```text
MEASURE_CONTRACT_vX.X.md
```

---

## Purpose

```text
Define Calculation Logic

Define Formatting Rules

Define Threshold Logic

Define Action Logic

Define Measure Governance
```

---

# SECTION 17 — MODELING OBSERVATIONS

## Assumptions

```text
[List]
```

---

## Constraints

```text
[List]
```

---

## Risks

```text
[List]
```

---

## Special Considerations

```text
[List]
```

---

# SUCCESS STATEMENT

The Semantic Model Specification succeeds when:

```text
Every Fact

has a declared grain.

Every Dimension

provides business context.

Every Column

has business meaning.

Every Relationship

supports business navigation.

Every Measure

has a valid source.

Every Signal

has model coverage.

Every Decision

is supported by the semantic model.
```

The Semantic Model Specification becomes:

```text
The Semantic Architecture Contract
```

between:

```text
Business Design

↓

Technical Design

↓

Semantic Design

↓

Measure Design
```