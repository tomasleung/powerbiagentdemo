# Decision Story Agent

## Purpose

The Decision Story Agent converts a Business Requirements Document (BRD) into a Decision Story Contract (DSC).

The agent follows the Decision-Driven BI Framework and ensures report design begins with business decisions and operational actions rather than visuals, charts, or technical implementation.

The output becomes the governing design contract for all downstream agents.

---

# Agent Position

```text
BRD
↓
Decision Story Agent
↓
REPORT_STORY_MATRIX
↓
REPORT_STORY (DSC)

↓
Mockup Agent
↓
MOCKUP
↓
SVG

↓
TRD Agent
↓
TRD

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

# Inputs

## Required

```text
Business Requirements Document (BRD)
```

---

## Expected Content

```text
Business Problem

Decisions

Business Questions

Signals

Thresholds

Success Criteria

Stakeholders
```

---

# Standards

The agent must follow:

```text
REPORT_DESIGN_STANDARDS_v1.0
```

Location:

```text
standards/
```

---

# Templates

The agent populates approved templates.

Template 01

```text
REPORT_STORY_MATRIX_TEMPLATE_v1.0
```

Template 02

```text
REPORT_STORY_TEMPLATE_v1.0
```

Location:

```text
templates/
```

---

# Outputs

## Output 01

```text
REPORT_STORY_MATRIX_vX.X.md
```

Purpose

```text
Validate the decision framework.
```

---

## Output 02

```text
REPORT_STORY_vX.X.md
```

Purpose

```text
Create the governing Decision Story Contract.
```

---

# Workflow

```text
BRD
↓
Decision Analysis
↓
Business Questions
↓
Signals
↓
Thresholds
↓
Actions
↓
Story Design
↓
Layout Blueprint
↓
Visual Recommendations
↓
REPORT_STORY_MATRIX
↓
REPORT_STORY (DSC)
```

---

# Folder Structure

```text
decision-story-agent/

README.md

skill.md

standards/

templates/

test-run/

examples/
```

---

# Success Criteria

The agent succeeds when:

```text
Every Question
supports a Decision

Every Signal
supports a Question

Every Action
supports a Decision

Every Story Section
supports User Action
```

The final output must function as a:

```text
Decision Product
```

rather than a:

```text
Reporting Product
```