# Guidelines Directory
## TRD Agent v1.0

---

# Purpose

This folder contains implementation guidance used by the TRD Agent.

Guidelines help ensure Technical Requirements Documents (TRDs) are:

```text
Consistent

Readable

Traceable

Implementation Focused

Developer Friendly
```

Guidelines define:

```text
Writing Style

Level Of Detail

Documentation Practices

Technical Scope

Boundary Management
```

Guidelines do not define:

```text
Business Requirements

Technical Standards

Document Structure
```

These responsibilities belong to:

```text
BRD

TRD_STANDARDS_v1.0

05_TRD_TEMPLATE_v1.0
```

---

# Guidelines Overview

## TRD_GUIDELINES_v1.0.md

Purpose

```text
Provide instructions for documenting
technical implementation requirements.
```

---

# Controls

The guideline governs:

```text
Documentation Style

Technical Detail Level

Traceability Documentation

Source Documentation

Measure Documentation

Visual Documentation

Security Documentation

Validation Documentation

Deployment Documentation
```

---

# Key Question

```text
How should a TRD be written?
```

---

# Relationship To Standards

Standards define:

```text
What is required.
```

Guidelines define:

```text
How it should be documented.
```

Example

```text
TRD_STANDARDS

defines

Every Measure must identify
the Decision Supported.
```

```text
TRD_GUIDELINES

defines

How measures should be described.
```

---

# Relationship To Templates

Templates define:

```text
Document Structure
```

Guidelines define:

```text
Documentation Approach
```

Example

```text
TRD_TEMPLATE

defines

the Measure Inventory section.
```

```text
TRD_GUIDELINES

defines

how measures should be documented
within that section.
```

---

# TRD Creation Flow

```text
Approved Business Design

↓

TRD Template

↓

TRD Standards

↓

TRD Guidelines

↓

TRD_vX.X.md
```

---

# Documentation Responsibilities

The TRD should document:

```text
Source Systems

Target Systems

Conceptual Data Model

Measures

Visual Requirements

Interactions

Security Requirements

Validation Requirements

Deployment Requirements
```

---

# Documentation Boundaries

The TRD should remain:

```text
Implementation Focused

Technology Neutral

Business Traceable
```

---

## Do Include

```text
Business Context

Measure Definitions

Source Mapping

Visual Mapping

Interaction Behavior

Security Expectations

Validation Requirements

Deployment Considerations
```

---

## Do Not Include

```text
DAX

SQL

Power Query

Fabric Pipelines

Physical Data Models

Deployment Scripts

Build Instructions
```

These belong to future implementation agents.

---

# Traceability Expectations

Every TRD should preserve:

```text
Decision

↓

Business Question

↓

Signal

↓

Measure

↓

Visual

↓

Technical Requirement
```

---

# Audience Expectations

A completed TRD should support:

```text
Solution Architects

BI Developers

Power BI Developers

Fabric Developers

Semantic Model Designers

Technical Reviewers
```

without requiring them to revisit:

```text
BRD

REPORT_STORY_MATRIX

REPORT_STORY (DSC)

MOCKUP

SVG
```

---

# Quality Expectations

Every TRD should be:

```text
Clear

Complete

Consistent

Traceable

Reviewable

Maintainable
```

---

# Folder Contents

```text
TRD_GUIDELINES_v1.0.md
```

---

# Generated Output

The guideline supports generation of:

```text
TRD_vX.X.md
```

---

# Success Statement

The Guidelines folder succeeds when:

```text
Every TRD

is written in a consistent manner,

contains the appropriate level of detail,

and provides sufficient information
for technical implementation.
```

The result is:

```text
Reliable

Governed

Decision-Driven

Technical Documentation
```

across all Business Intelligence solutions.