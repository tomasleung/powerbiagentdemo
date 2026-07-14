# 08_DATA_MODEL_MATRIX_TEMPLATE_v1.0
## Semantic Design Validation Matrix

---

# Document Metadata

Document Type

```text
Data Model Matrix
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
DATA_MODEL_MATRIX
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

Validate the business structure of the semantic model before detailed table, column, relationship, and measure design begins.

This document serves as the bridge between:

```text
TRD

↓

Business Metrics

↓

Semantic Model Design
```

and ensures every semantic object has a valid business purpose and traceable business justification.

---

# Related Artifacts

```text
BRD

REPORT_STORY_MATRIX

REPORT_STORY (DSC)

TRD

DATA_MODEL_STANDARDS
```

---

# SECTION 01 — DECISION MODEL VALIDATION

## Primary Decision

```text
[Primary Decision]
```

---

## Secondary Decisions

```text
[List]
```

---

## Semantic Modeling Goal

Describe how the semantic model will support all approved decisions without requiring users to manually calculate metrics or interpret raw source data.

---

# SECTION 02 — BUSINESS SIGNAL INVENTORY

## Signal Category

### Signal Group

```text
[Signal Group]
```

---

### Signals

```text
[List]
```

---

### Decision Supported

```text
[Decision]
```

---

### Business Purpose

```text
[Purpose]
```

---

Repeat sections as required.

Typical categories:

```text
Operational Signals

Capacity Signals

Utilization Signals

Data Quality Signals

Governance Signals

Regional Signals

Executive Signals
```

---

# SECTION 03 — MEASURE INVENTORY

## Measure Category

### Measures

```text
[List]
```

---

### Business Purpose

```text
[Purpose]
```

---

### Decisions Supported

```text
[List]
```

---

Repeat sections as required.

Typical categories:

```text
Operational Snapshot Measures

Decision Support Measures

Placement Measures

Capacity Measures

Utilization Measures

Data Quality Measures

Regional Measures

Executive Measures
```

---

# SECTION 04 — DECISION → QUESTION → SIGNAL → MEASURE MATRIX

| Decision | Business Question | Signal | Measure |
|-----------|-----------|-----------|-----------|
| [Decision] | [Question] | [Signal] | [Measure] |
| [Decision] | [Question] | [Signal] | [Measure] |

---

## Validation Rule

Every measure must trace back to:

```text
Decision

↓

Business Question

↓

Signal

↓

Measure
```

---

# SECTION 05 — GRAIN ANALYSIS

## Fact Candidate

### Business Grain

One row represents:

```text
[Business Grain]
```

---

### Example Row

```text
[Example]
```

---

### Target Fact

```text
[Fact Name]
```

---

### Business Purpose

```text
[Purpose]
```

---

Repeat for every fact candidate.

---

# GRAIN VALIDATION

Verify:

```text
□ Grain Declared

□ Example Row Defined

□ Business Purpose Defined

□ Measures Align To Grain

□ No Mixed Grain

□ One Sentence Row Definition Exists
```

---

# SECTION 06 — FACT IDENTIFICATION MATRIX

## Fact Table

### Fact Name

```text
[Fact Name]
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

---

### Supports Decisions

```text
[List]
```

---

### Supports Signals

```text
[List]
```

---

### Supports Measures

```text
[List]
```

---

### Source Systems

```text
[List]
```

---

Repeat for every fact.

---

# FACT INVENTORY SUMMARY

| Fact Table | Grain | Measures Supported | Decisions Supported |
|------------|------------|------------|------------|
| [Fact] | [Grain] | [Measures] | [Decision] |
| [Fact] | [Grain] | [Measures] | [Decision] |

---

# SECTION 07 — DIMENSION IDENTIFICATION MATRIX

## Dimension

### Dimension Name

```text
[Dimension Name]
```

---

### Business Purpose

```text
[Purpose]
```

---

### Key Attributes

```text
[List]
```

---

### Used For

```text
Filtering

Grouping

Drill Down

Analysis
```

---

### Facts Supported

```text
[List]
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

# SECTION 08 — FACT TO DIMENSION MATRIX

## Fact Table

### Connected Dimensions

```text
[List]
```

---

### Business Purpose

```text
[Purpose]
```

---

Repeat for all facts.

---

# FACT TO DIMENSION SUMMARY

| Fact Table | Connected Dimensions |
|------------|------------|
| [Fact] | [Dimensions] |
| [Fact] | [Dimensions] |

---

# SECTION 09 — SEMANTIC MODEL BLUEPRINT

## Conceptual Architecture

```text
                 [Dim_Date]
                       │
                       │
                       ▼

[Dim_Centre] ───── [Fact_A]

      │

      ├────────── [Fact_B]

      │

      └────────── [Fact_C]


[Dim_Animal_Type]

      ├────────── [Fact_A]

      └────────── [Fact_B]


[Dim_Region]

      │
      ▼

[Dim_Centre]
```

---

## Design Notes

```text
Conformed Dimensions

Shared Dimensions

Star Schema Strategy

Relationship Intent
```

---

# SECTION 10 — CONFORMED DIMENSION REVIEW

## Shared Dimensions

| Dimension | Fact Tables Using Dimension |
|------------|------------|
| [Dimension] | [Facts] |
| [Dimension] | [Facts] |

---

## Validation

Verify:

```text
□ Shared Across Facts

□ Consistent Naming

□ Consistent Definitions

□ Reusable Across Reports
```

---

# SECTION 11 — BUSINESS QUESTION COVERAGE

## Coverage Matrix

| Business Question | Signal Exists | Measure Exists | Fact Exists | Dimension Exists |
|------------|------------|------------|------------|------------|
| [Question] | Yes/No | Yes/No | Yes/No | Yes/No |
| [Question] | Yes/No | Yes/No | Yes/No | Yes/No |

---

# SECTION 12 — DECISION COVERAGE

## Coverage Matrix

| Decision | Coverage Status | Notes |
|------------|------------|------------|
| [Decision] | Complete | [Notes] |
| [Decision] | Complete | [Notes] |

---

## Validation Rule

Every decision must have:

```text
Question

↓

Signal

↓

Measure

↓

Fact

↓

Dimension
```

coverage.

---

# SECTION 13 — MODEL VALIDATION

## Decision Validation

```text
✓ Primary Decision Supported

✓ Secondary Decisions Supported
```

---

## Signal Validation

```text
✓ All Signals Mapped

✓ No Orphan Signals
```

---

## Measure Validation

```text
✓ All Measures Identified

✓ Measures Trace To Signals
```

---

## Grain Validation

```text
✓ Fact Grain Defined

✓ No Mixed Grain Tables
```

---

## Fact Validation

```text
✓ Facts Support Measures

✓ Facts Support Decisions
```

---

## Dimension Validation

```text
✓ Dimensions Support Filtering

✓ Dimensions Support Analysis
```

---

## Traceability Validation

```text
✓ Decision Traceability Preserved

✓ No Orphan Measures

✓ No Orphan Facts

✓ No Orphan Dimensions
```

---

# SECTION 14 — HANDOFF TO SEMANTIC MODEL SPEC

## Required Approvers

```text
Business Architect

Data Architect

BI Architect
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
SEMANTIC_MODEL_SPEC_vX.X.md
```

---

## Purpose

```text
Expand Facts

Expand Dimensions

Define Columns

Define Data Types

Define Relationships

Define Cardinality

Define Filter Direction
```

---

# SECTION 15 — MODELING OBSERVATIONS

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

# FINAL VALIDATION CHECKLIST

Before approval verify:

```text
□ Decisions Identified

□ Business Questions Identified

□ Signals Identified

□ Measures Identified

□ Grain Defined

□ Fact Tables Identified

□ Dimension Tables Identified

□ Fact To Dimension Mapping Complete

□ Conformed Dimensions Identified

□ Question Coverage Complete

□ Decision Coverage Complete

□ Semantic Blueprint Reviewed

□ Traceability Preserved
```

---

# SUCCESS STATEMENT

The Data Model Matrix succeeds when:

```text
Every Decision

supports a Business Question

Every Business Question

supports a Signal

Every Signal

supports a Measure

Every Measure

supports a Fact

Every Fact

supports a Dimension

Every Dimension

supports Analysis
```

and the architecture can be handed to a Data Architect for creation of:

```text
SEMANTIC_MODEL_SPEC_vX.X.md
```

with complete confidence that business intent, traceability, and semantic structure have been preserved.

The Data Model Matrix becomes:

```text
The Semantic Traceability Contract
```

between:

```text
Business Design

↓

Technical Design

↓

Semantic Design
```