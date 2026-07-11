# Standards Folder

## Purpose

Contains the governing standards used by the Decision Story Agent.

These standards define how decision-driven report design must be performed.

The standards ensure deterministic, repeatable, and consistent output generation.

---

# Contents

## REPORT_DESIGN_STANDARDS_v1.0.md

Purpose

Provide the official Decision-Driven BI report design methodology.

Defines:

```text
Decision Design

Business Question Design

Signal Design

Threshold Design

Action Design

Story Design

Page Archetypes

Layout Standards

Visual Standards

DSC Standards
```

---

# Usage

The Decision Story Agent must apply:

```text
REPORT_DESIGN_STANDARDS_v1.0
```

before populating any templates.

---

# Rule

The standards folder is the:

```text
Source Of Truth
```

for report design guidance.

Templates define structure.

Standards define behavior.

Agent logic must never override these standards.

---

# Design Chain

```text
Decision
↓
Question
↓
Signal
↓
Threshold
↓
Action
↓
Story
↓
Layout
↓
Visual
```

Everything produced by the Decision Story Agent must follow this sequence.