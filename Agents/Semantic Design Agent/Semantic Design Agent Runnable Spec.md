# Semantic Design Agent Runnable Spec

## Purpose

This document defines a runnable specification for the Semantic Design Agent. It turns your design framework into a concrete, executable agent workflow that can generate the required artifacts from approved inputs.

## Agent Name

Semantic Design Agent

## Goal

Convert approved business and technical requirements into governed semantic model design artifacts using decision-driven BI standards.

## Required Inputs

- `TRD` (Technical Requirements Document)
- `DSC` (Decision Story / REPORT_STORY)
- `DATA_MODEL_STANDARDS_v1.0`

## Optional Inputs

- `BRD`
- `REPORT_STORY_MATRIX`
- `SVG Mockup`
- `Existing Semantic Model`
- `Existing Power BI Dataset`
- `Data Dictionary`

## Outputs

1. `DATA_MODEL_MATRIX_v1.0`
2. `SEMANTIC_MODEL_SPEC_v1.0`
3. `MEASURE_CONTRACT_v1.0`

## Template References

The agent should use the existing template artifacts in `Template/` to understand the first specification shape:

- `Template/0 DATA_MODEL_STANDARDS_v1.0`
- `Template/1 DATA_MODEL_MATRIX_v1.0`
- `Template/2 SEMANTIC_MODEL_SPEC_v1.0`
- `Template/3 MEASURE_CONTRACT_v1.0.md`

These template files define the expected sections and structure for each output.

## Example Reference

The agent should also review the example input and output case in `Example Animal Flow Live Capacity/` to learn a concrete example of input format and expected result:

- `Example Animal Flow Live Capacity/INPUT 01 — REPORT_STORY_v1.0 (DSC).md`
- `Example Animal Flow Live Capacity/INPUT 02 — TRD_v1.0.md`
- `Example Animal Flow Live Capacity/INPUT 03 — DATA_MODEL_STANDARDS_v1.0.md`
- `Example Animal Flow Live Capacity/OUTPUT 1 — DATA_MODEL_MATRIX_v1.0.md`
- `Example Animal Flow Live Capacity/OUTPUT 2 — SEMANTIC_MODEL_SPEC_v1.0.md`
- `Example Animal Flow Live Capacity/OUTPUT 3 — MEASURE_CONTRACT_v1.0.md`

The example case should serve as a reference run to validate the agent's output style and completeness.

## Execution Flow

1. Review approved inputs.
2. Extract the decision model.
3. Build the signal inventory.
4. Build the measure inventory.
5. Define business grain for each subject area.
6. Identify fact tables.
7. Identify dimension tables.
8. Design relationships.
9. Generate `DATA_MODEL_MATRIX`.
10. Generate `SEMANTIC_MODEL_SPEC`.
11. Generate `MEASURE_CONTRACT`.

## Workflow Steps

### Step 1 — Review Approved Inputs

Inputs:
- `TRD`
- `DSC`
- `DATA_MODEL_STANDARDS`

Actions:
- Read the TRD and DSC.
- Extract decisions, signals, measures, filters, and visual requirements.

Output:
- Business Modeling Context

### Step 2 — Extract Decision Model

Actions:
- Identify primary and secondary decisions.
- Identify decision owners and decision frequency.
- Confirm every measure supports a decision.

Output:
- Decision Validation

### Step 3 — Build Signal Inventory

Actions:
- List all approved signals.
- Ensure every signal maps to a decision.
- Confirm no orphan signals.

Output:
- Signal Inventory

### Step 4 — Build Measure Inventory

Actions:
- List all approved measures.
- Map each measure to a supporting signal.
- Confirm every measure has a business definition.

Output:
- Measure Inventory

### Step 5 — Define Grain

Actions:
- Define business grain for each subject area.
- Capture purpose and example row for each grain.

Output:
- Grain Matrix

### Step 6 — Identify Facts

Actions:
- Identify fact tables from the measures and grain definitions.
- Define business purpose, grain, supported measures, and signals for each fact.

Output:
- Fact Inventory

### Step 7 — Identify Dimensions

Actions:
- Identify required dimensions.
- Define dimension purpose, attributes, filters, and supported analysis.
- Review dimension design for query performance, filter efficiency, and common user scenarios.

Output:
- Dimension Inventory

### Step 8 — Design Relationships

Actions:
- Define relationships between facts and dimensions.
- Specify cardinality, filter direction, and join keys.
- Validate star schema and avoid unnecessary many-to-many relationships.
- Optimize relationships for query performance and filter propagation.

Output:
- Relationship Matrix

### Step 9 — Generate DATA_MODEL_MATRIX

Purpose:
- Business validation artifact.

Contents:
- Decision Model
- Signal Inventory
- Measure Inventory
- Grain Analysis
- Fact Identification
- Dimension Identification
- Semantic Blueprint

Audience:
- Business Architect
- BI Architect
- Data Architect

### Step 10 — Generate SEMANTIC_MODEL_SPEC

Purpose:
- Technical model design.

Contents:
- Fact Tables
- Dimension Tables
- Columns
- Data Types
- Relationships
- Cardinality
- Filter Direction
- Documentation Requirements

Audience:
- Data Architect
- Power BI Developer
- Fabric Developer

### Step 11 — Generate MEASURE_CONTRACT

Purpose:
- Measure governance specification.

Contents:
- Business Definition
- Calculation Logic
- Thresholds
- Actions
- Dependencies
- Decision Supported

Audience:
- Business Owner
- BI Architect

## Output Templates

### DATA_MODEL_MATRIX

Section structure:
- Decision Model
- Signal Inventory
- Measure Inventory
- Grain Matrix
- Fact Inventory
- Dimension Inventory
- Relationship Matrix

### SEMANTIC_MODEL_SPEC

Section structure:
- Fact Table Definitions
- Dimension Table Definitions
- Column Definitions
- Relationship Definitions
- Cardinality and Filter Direction
- Implementation Notes

### MEASURE_CONTRACT

Section structure:
- Measure Name
- Business Definition
- Calculation Logic
- Threshold or Target
- Decision Supported
- Dependencies
- Notes

## Validation Rules

Before the agent completes, verify:

- Every decision supports at least one signal.
- Every signal supports at least one measure.
- Every measure maps to at least one fact.
- Every fact has a declared grain and example row.
- Every dimension has a clear business purpose.
- Relationships form a star schema unless justified.
- Models use performance-aware design patterns.
- All outputs follow `DATA_MODEL_STANDARDS_v1.0`.

## Performance Considerations

Before the agent completes, verify:

- The model minimizes unnecessary columns and wide fact table payloads.
- Grain is appropriate to avoid overly high-cardinality facts.
- Keys are simplified to numeric surrogate keys where possible.
- Measures are defined to support common query patterns and aggregations.
- Relationships are single-direction unless a business case justifies both directions.
- The semantic model avoids unnecessary many-to-many joins.
- The output includes notes on performance trade-offs or expected query behavior.

## Example Run Input

Input files:
- `TRD.md`
- `DSC.md`
- `DATA_MODEL_STANDARDS_v1.0.md`

Expected artifacts:
- `DATA_MODEL_MATRIX_v1.0.md`
- `SEMANTIC_MODEL_SPEC_v1.0.md`
- `MEASURE_CONTRACT_v1.0.md`

## Recommended File Naming

- `Semantic Design Agent Runnable Spec.md`
- `DATA_MODEL_MATRIX_v1.0.md`
- `SEMANTIC_MODEL_SPEC_v1.0.md`
- `MEASURE_CONTRACT_v1.0.md`

## How to Use This Spec

1. Load the required inputs from `Example Animal Flow Live Capacity/` or the current project.
2. Review the `Template/` files to understand the expected output structure.
3. Follow the `Execution Flow` and `Workflow Steps` sequentially.
4. Generate each output artifact in order:
   - `DATA_MODEL_MATRIX_v1.0`
   - `SEMANTIC_MODEL_SPEC_v1.0`
   - `MEASURE_CONTRACT_v1.0`
5. Validate outputs using the `Validation Rules` section.
6. Compare generated outputs to the example artifacts for format and completeness.

## Notes

This file is the runnable specification for the Semantic Design Agent. It should be used by the agent as the execution plan, by reviewers as the acceptance checklist, and by developers as the implementation guide.