# SEMANTIC_DESIGN_GUIDELINES_v1.0
## Decision-Driven BI Semantic Design Guidelines

---

# Document Metadata

Document Name

```text
SEMANTIC_DESIGN_GUIDELINES
```

Version

```text
1.0
```

Owner

```text
Decision-Driven BI Framework
```

Status

```text
Approved Guideline
```

Purpose

Provide implementation guidance for creating semantic design artifacts within the Decision-Driven BI Framework.

These guidelines complement:

```text
DATA_MODEL_STANDARDS_v1.0
```

and define:

```text
How To Model

How To Document

How To Validate

How To Handoff
```

semantic design artifacts.

---

# SECTION 01 — GUIDING PHILOSOPHY

## Decision First

The semantic model is not designed to represent source systems.

The semantic model is designed to support decisions.

Always begin with:

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

Never begin with:

```text
Source Tables

↓

Columns

↓

Relationships
```

---

## Business Before Technical

Business intent always wins.

When conflicts occur:

```text
Business Need

↓

Semantic Design

↓

Technical Implementation
```

---

## Traceability First

Every semantic object must have a documented business purpose.

Never create:

```text
Measures

Facts

Dimensions

Relationships
```

without traceability to an approved decision.

---

# SECTION 02 — INPUT USAGE GUIDELINES

## Required Inputs

Always use:

```text
TRD_vX.X.md

REPORT_STORY_vX.X.md
```

---

## Reference Inputs

Use when clarification is required:

```text
INPUT_BRD_vX.X.md

REPORT_STORY_MATRIX_vX.X.md
```

---

## Input Priority

```text
1. REPORT_STORY

2. TRD

3. REPORT_STORY_MATRIX

4. BRD
```

The Decision Story remains the ultimate source of truth.

---

# SECTION 03 — DATA MODEL MATRIX GUIDELINES

## Purpose

The Data Model Matrix validates semantic design before implementation begins.

---

## Focus Areas

Identify:

```text
Business Decisions

Business Questions

Signals

Measures

Facts

Dimensions
```

---

## Avoid

Do not document:

```text
DAX

SQL

Column Data Types

Technical Optimizations
```

Those belong in later artifacts.

---

## Expected Outcome

A reviewer should be able to answer:

```text
Why does this fact exist?

Why does this dimension exist?

Why does this measure exist?
```

without reading the semantic model specification.

---

# SECTION 04 — SEMANTIC MODEL SPEC GUIDELINES

## Purpose

The Semantic Model Specification translates business structure into semantic architecture.

---

## Focus Areas

Document:

```text
Fact Tables

Dimension Tables

Columns

Relationships

Cardinality

Filter Direction

Hierarchies
```

---

## Required Detail

The document must contain enough information for:

```text
Data Architect

BI Developer

Fabric Developer
```

to build the semantic model.

---

## Avoid

Do not include:

```text
Power BI Report Design

Visual Design

Dashboard Layout

Business Storytelling
```

These belong to other artifacts.

---

# SECTION 05 — MEASURE CONTRACT GUIDELINES

## Purpose

Define and govern business measures.

---

## Required Documentation

Every measure must define:

```text
Business Definition

Signal Supported

Decision Supported

Business Formula

Thresholds

Actions

Dependencies

Ownership
```

---

## Formula Guidance

Use:

```text
Business Logic
```

instead of:

```text
DAX Code
```

Example:

Good

```text
Animals In Care

÷

Care Capacity
```

Bad

```text
DIVIDE([Animals In Care],[Care Capacity])
```

---

## Threshold Guidance

Document:

```text
Green

Amber

Red
```

thresholds whenever applicable.

---

## Action Guidance

Every threshold should define:

```text
Recommended Action
```

whenever possible.

---

# SECTION 06 — FACT DESIGN GUIDELINES

## Start With Grain

Always identify:

```text
Business Grain
```

before creating a fact.

---

## Good Example

```text
One Centre

+

One Date

+

One Animal Type
```

---

## Fact Responsibilities

Facts should contain:

```text
Metrics

Counts

Volumes

Utilization

Snapshots

Transactions
```

---

## Avoid

Avoid:

```text
Descriptions

Comments

Narratives

Business Notes
```

inside fact tables.

---

# SECTION 07 — DIMENSION DESIGN GUIDELINES

## Purpose

Dimensions provide business context.

---

## Typical Dimensions

```text
Date

Region

Centre

Animal Type

Department

Location
```

---

## Dimension Responsibilities

Dimensions should support:

```text
Filtering

Grouping

Drill Down

Segmentation
```

---

## Avoid

Avoid placing:

```text
Measures

Running Calculations

Threshold Logic
```

inside dimensions.

---

# SECTION 08 — RELATIONSHIP GUIDELINES

## Preferred Design

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

## Preferred Filter Direction

```text
Single Direction
```

---

## Bidirectional Filtering

Use only when:

```text
Business Need Exists

Performance Impact Reviewed
```

---

## Relationship Documentation

Every relationship should document:

```text
Parent

Child

Join Key

Purpose
```

---

# SECTION 09 — CONFORMED DIMENSIONS

## Purpose

Maximize reuse.

---

## Typical Conformed Dimensions

```text
Dim_Date

Dim_Centre

Dim_Region

Dim_AnimalType
```

---

## Guidelines

Use consistent:

```text
Definitions

Attributes

Hierarchies

Business Meaning
```

across all facts.

---

# SECTION 10 — PERFORMANCE GUIDELINES

## Preferred Model Shape

```text
Star Schema
```

---

## Fact Design

Keep facts:

```text
Narrow

Efficient

Focused
```

---

## Avoid

```text
Wide Fact Tables

Excessive Text

Duplicate Attributes

Unnecessary Columns
```

---

## Cardinality

Reduce:

```text
GUID Usage

Long Strings

Unique Values
```

where practical.

---

# SECTION 11 — MICROSOFT FABRIC GUIDELINES

## Preferred Modeling Pattern

```text
Fabric Semantic Model

↓

Star Schema

↓

Explicit Measures
```

---

## Naming

Expose business-friendly names.

Example:

Good

```text
Remaining Capacity
```

Bad

```text
Cap_Rem_Agg_01
```

---

## Reusability

The model should support:

```text
Power BI

Copilot

Self-Service Analytics

Future Reports
```

---

# SECTION 12 — AI READINESS GUIDELINES

## Documentation Requirements

Every semantic object should explain:

```text
Why It Exists

What It Means

What Decision It Supports
```

---

## Table Documentation

Document:

```text
Business Purpose

Declared Grain

Description
```

---

## Measure Documentation

Document:

```text
Business Definition

Decision Supported

Signal Supported

Business Owner
```

---

## AI Readiness Goal

An AI assistant should explain:

```text
Why the table exists

Why the measure exists

Which decision it supports

How it contributes to business outcomes
```

without additional documentation.

---

# SECTION 13 — VALIDATION GUIDELINES

## Data Model Matrix Validation

Verify:

```text
□ Decisions Identified

□ Questions Identified

□ Signals Identified

□ Measures Identified

□ Facts Identified

□ Dimensions Identified

□ Traceability Preserved
```

---

## Semantic Model Validation

Verify:

```text
□ Facts Defined

□ Dimensions Defined

□ Columns Defined

□ Relationships Defined

□ Cardinality Defined

□ Filter Direction Defined
```

---

## Measure Contract Validation

Verify:

```text
□ Business Definitions Exist

□ Dependencies Defined

□ Thresholds Defined

□ Actions Defined

□ Owners Assigned
```

---

# SECTION 14 — HANDOFF GUIDELINES

## Data Model Matrix

Output:

```text
SEMANTIC_MODEL_SPEC
```

---

## Semantic Model Spec

Output:

```text
MEASURE_CONTRACT
```

---

## Measure Contract

Output:

```text
Semantic Build Agent
```

---

## Handoff Goal

Each artifact must provide sufficient detail so the next artifact can be created without revisiting earlier phases whenever possible.

---

# SECTION 15 — COMMON MODELING MISTAKES

Avoid:

```text
Modeling From Source Systems

Undefined Grain

Orphan Measures

Orphan Dimensions

Orphan Facts

Many-to-Many Relationships

Undocumented Logic

Duplicated Measures
```

---

# GUIDELINE SUCCESS STATEMENT

Semantic Design succeeds when:

```text
Business Intent

↓

Semantic Architecture

↓

Measure Governance
```

remains fully traceable.

The result is:

```text
Decision-Driven

Business-Aligned

Fabric-Ready

AI-Ready

Semantic Models
```

that can be confidently handed to:

```text
Semantic Build

Power BI Development

Fabric Implementation
```