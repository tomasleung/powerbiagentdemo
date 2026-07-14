# Utilities
## Decision-Driven BI Framework

---

# Purpose

The Utilities layer provides reusable framework capabilities that are shared across multiple agents.

Utilities exist to perform:

```text
Publishing

Conversion

Formatting

Packaging

Automation Support
```

Utilities do not:

```text
Create Business Requirements

Create Business Design

Create Technical Design

Create Semantic Design
```

Those responsibilities belong to framework agents.

---

# Core Philosophy

Agents generate content.

Utilities publish, transform, or package content.

---

# Architecture

```text
Agent

↓

Framework Artifact

↓

Utility

↓

Published Artifact
```

---

# Example

```text
TRD Agent

↓

TRD_v1.0.md

↓

Word Publisher

↓

TRD_v1.0.docx
```

---

# Current Utilities

## Word Publisher

Purpose

```text
Convert Markdown Framework Artifacts

into

Executive Review Word Documents.
```

Location

```text
word-publisher/
```

---

# Utility Design Principles

Each utility should:

```text
Be Reusable

Be Independent

Have Single Responsibility

Support Multiple Agents

Avoid Owning Business Logic
```

---

# Utility Ownership

Utilities do not own artifacts.

Utilities only transform artifacts.

Example:

```text
TRD Agent

owns

TRD_vX.X.md
```

```text
Word Publisher

owns

TRD_vX.X.docx generation
```

---

# Current Architecture

```text
Decision Story Agent
        ↓
REPORT_STORY

Mockup Agent
        ↓
MOCKUP

TRD Agent
        ↓
TRD

Word Publisher Utility
        ↓
DOCX
```

---

# Future Utility Candidates

```text
Word Publisher

PDF Publisher

SVG Renderer

Diagram Generator

Validation Runner

Artifact Packager

Release Publisher
```

---

# Success Statement

The Utilities layer succeeds when:

```text
Framework Artifacts

can be transformed

into business-ready deliverables

without changing the original content.
```

The result is:

```text
Reusable

Governed

Framework-Wide Capabilities
```