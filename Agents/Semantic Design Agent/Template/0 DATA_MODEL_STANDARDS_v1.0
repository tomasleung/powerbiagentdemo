# DATA_MODEL_STANDARDS_v1.0
## Decision-Driven BI Semantic Modeling Standards

---

# Document Metadata

Document Name:
DATA_MODEL_STANDARDS

Version:
1.0

Owner:
Decision-Driven BI Framework

Status:
Approved Standard

Purpose:

Provide a governing semantic modeling framework for all Decision-Driven BI solutions.

This standard combines:

```text
Decision-Driven BI Principles
+
Kimball Dimensional Modeling
+
Microsoft Fabric Semantic Modeling Standards
+
SQLBI Best Practices
```

The goal is to ensure all semantic models are:

```text
Decision Driven

Business Focused

Consistent

Scalable

Performant

Maintainable

AI Ready
```

---

# SECTION 01 — MODELING PHILOSOPHY

## Core Principle

The semantic model exists to support business decisions.

The model must not be driven by source systems.

The model must be driven by decision requirements.

---

## Incorrect Design Approach

```text
Source Tables
↓
Columns
↓
Relationships
↓
Dashboard
```

---

## Correct Design Approach

```text
Decision
↓
Business Question
↓
Signal
↓
Measure
↓
Grain
↓
Fact
↓
Dimension
↓
Semantic Model
```

---

## Decision Traceability Rule

Every element within the semantic model must trace back to a business decision.

Example

```text
Decision

Can this centre receive another animal?

↓

Signal

Care Capacity

↓

Measure

Remaining Capacity

↓

Fact

Capacity

↓

Dashboard
```

---

## Model Success Criteria

A semantic model is successful when:

```text
Every measure supports a signal.

Every signal supports a business question.

Every business question supports a decision.
```

---

# SECTION 02 — GRAIN-FIRST DESIGN

## Governing Rule

Always define grain before creating a fact table.

Fact tables must never determine their own grain.

---

## Grain Definition

Grain answers:

```text
What does one row represent?
```

---

## Examples

### Good

```text
Centre
+
Date
+
Animal Type
```

---

### Good

```text
Animal
+
Centre
+
Date
```

---

### Bad

```text
Capacity
+
Animal Occupancy
```

within the same table.

---

## Grain Declaration Rule

Every fact table must explicitly declare:

```text
Business Grain

Example Row

Business Purpose
```

---

## Grain Validation Test

Ask:

```text
Can every row be described in one sentence?
```

Example:

```text
One row represents a centre's capacity
for a given date and animal type.
```

If not:

```text
Grain is not defined correctly.
```

---

# SECTION 03 — FACT IDENTIFICATION RULES

## Fact Definition

Facts contain measurable events or measurable states.

---

## Fact Qualification Test

A table is a fact when it stores:

```text
Counts

Volumes

Amounts

Quantities

Capacities

Utilization

Transactions

Snapshots
```

---

## Fact Characteristics

Facts must:

```text
Have declared grain

Contain measurable values

Relate to dimensions

Contain foreign keys

Support business calculations
```

---

## Fact Naming Standard

Physical Layer

```text
Fact_Capacity

Fact_Occupancy

Fact_Confirmation
```

---

Logical Layer

```text
Capacity

Occupancy

Confirmation
```

---

## Fact Design Rules

Facts should:

```text
Be narrow

Be additive where possible

Avoid descriptive columns

Avoid free-form text

Avoid business commentary
```

---

## Fact Validation

A fact table should answer:

```text
What happened?

How many?

How much?

How often?
```

---

# SECTION 04 — DIMENSION IDENTIFICATION RULES

## Dimension Definition

Dimensions provide business context.

---

## Dimension Qualification Test

Users naturally ask:

```text
By Centre

By Region

By Date

By Animal Type

By Department
```

Those are dimensions.

---

## Dimension Characteristics

Dimensions should contain:

```text
Names

Descriptions

Classifications

Hierarchies

Grouping Attributes
```

---

## Standard Shared Dimensions

Preferred dimensions include:

```text
Date

Time

Region

Centre

Location

Animal Type
```

---

## Dimension Rules

Dimensions must:

```text
Be business-friendly

Support filtering

Support grouping

Support drill-down
```

---

## Dimension Validation

A dimension should answer:

```text
Where?

Who?

What?

When?
```

---

# SECTION 05 — MEASURE DESIGN RULES

## Measure First Principle

Before building facts:

```text
Define Measures First
```

---

## Measure Template

Every measure must contain:

```text
Measure Name

Business Definition

Decision Supported

Threshold

Action
```

---

## Example

Measure

```text
Remaining Capacity
```

Business Definition

```text
Available Care Capacity
```

Decision Supported

```text
Can this centre receive another animal?
```

---

## Explicit Measures Only

Always create explicit measures.

Avoid implicit aggregation.

---

## Measure Validation Test

Ask:

```text
What decision becomes easier because of this measure?
```

If no answer exists:

```text
The measure should not exist.
```

---

# SECTION 06 — RELATIONSHIP RULES

## Standard Relationship Pattern

```text
Dimension
      ↓
Fact
```

---

## Preferred Cardinality

```text
One-to-Many
```

---

## Avoid

```text
Many-to-Many
```

unless justified.

---

## Filter Direction

Default

```text
Single Direction
```

Dimension → Fact

---

## Bidirectional Filtering

Use only when:

```text
Business requirement exists

Performance impact reviewed
```

---

## Relationship Validation

Relationships should:

```text
Be understandable

Be documented

Support business questions
```

---

# SECTION 07 — KIMBALL STANDARDS

## Star Schema First

Default architecture:

```text
Dimensions
      ↓
Fact
```

---

## Conformed Dimensions

Shared dimensions must be reused.

Examples:

```text
Date

Region

Centre
```

---

## Business-Focused Design

Model for:

```text
Analysis
```

not:

```text
Source System Convenience
```

---

## Declare Grain First

Kimball Rule:

```text
Grain Before Fact
```

Always.

---

# SECTION 08 — MICROSOFT FABRIC STANDARDS

## Semantic Model Principles

Follow Microsoft Fabric semantic modeling guidance.

---

## Star Schema

Default architecture.

---

## Explicit Measures

All calculations must use measures.

---

## Lean Models

Only include:

```text
Required Tables

Required Columns

Required Measures
```

---

## Memory Optimization

Avoid unnecessary:

```text
GUIDs

Large Text Fields

Transaction IDs

Unused Attributes
```

---

## Business Naming

Expose:

```text
Care Capacity

Animals In Care

Region
```

not technical names.

---

# SECTION 09 — SQLBI STANDARDS

## DAX Philosophy

Use:

```text
Measures
```

before:

```text
Calculated Columns
```

---

## Base Measure Pattern

Preferred structure:

```text
Base Measure

↓

Derived Measure

↓

Presentation Measure
```

---

## Context Awareness

Measures should be designed with awareness of:

```text
Filter Context

Row Context

Evaluation Context
```

---

## Reusability

Measures should be reusable across reports.

---

# SECTION 10 — PERFORMANCE STANDARDS

## Lean Models

Only load required data.

---

## Column Reduction

Remove:

```text
Unused Columns

Duplicate Attributes

Unused Flags
```

---

## Cardinality Management

Reduce:

```text
Free Text

Long Strings

GUIDs

Unique Keys
```

whenever possible.

---

## Relationship Simplicity

Prefer:

```text
One-to-Many

Single Direction
```

---

## Optimization Goal

The model should satisfy:

```text
Simplicity

Maintainability

Performance
```

---

# SECTION 11 — NAMING STANDARDS

## Naming Philosophy

Use business language.

---

## Good Examples

```text
Centre

Region

Animals In Care

Care Capacity

Remaining Capacity
```

---

## Bad Examples

```text
tblCentre

dim_region

FACT_OCCUPANCY

spCapacity
```

---

## Measure Naming Rules

Use:

```text
Readable Names
```

Example:

```text
Remaining Capacity

Species Occupancy Impact

Capacity Utilization %
```

---

## Table Naming Rules

Physical Model

```text
Fact_Capacity

Dim_Centre
```

---

Business Layer

```text
Capacity

Centre
```

---

# SECTION 12 — AI READINESS STANDARDS

## Purpose

Prepare the semantic model for:

```text
Copilot

Data Agents

Natural Language Queries

Semantic Search
```

---

## Table Documentation

Every table must include:

```text
Description

Business Purpose

Declared Grain
```

---

## Column Documentation

Every business column should include:

```text
Definition

Business Meaning
```

---

## Measure Documentation

Every measure must include:

```text
Business Definition

Decision Supported

Owner
```

---

## Relationship Documentation

Relationships should be understandable to non-technical users.

---

## AI Readiness Goal

An AI agent should be able to explain:

```text
Why the table exists.

Why the measure exists.

Which decision is supported.

Which business question is answered.
```

without external documentation.

---

# FINAL MODEL VALIDATION CHECKLIST

Before approving any semantic model:

```text
□ Decision Supported

□ Business Questions Mapped

□ Signals Identified

□ Measures Defined

□ Grain Defined

□ Fact Tables Identified

□ Dimension Tables Identified

□ Relationship Design Reviewed

□ Star Schema Followed

□ Microsoft Fabric Standards Followed

□ SQLBI Standards Followed

□ Performance Reviewed

□ Naming Standards Applied

□ AI Readiness Verified
```

---

# STANDARD SUCCESS STATEMENT

A semantic model succeeds when:

```text
Every Measure
supports a Signal

Every Signal
supports a Business Question

Every Business Question
supports a Decision

Every Decision
supports Business Action
```

The semantic model is therefore a decision product,
not merely a collection of tables and measures.