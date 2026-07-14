# Test Run Directory
## Mockup Agent v2.0

---

# Purpose

This folder contains all official Mockup Agent validation runs.

The purpose of the test-run folder is to:

```text
Validate Agent Behavior

Validate Standards

Validate Templates

Validate SVG Generation

Validate End-to-End Workflow

Document Results
```

before production use.

---

# Test Run Philosophy

Every test run should prove that:

```text
Inputs

↓

Standards

↓

Templates

↓

Guidelines

↓

Outputs
```

produce consistent and repeatable results.

---

# Test Run Lifecycle

```text
Input Artifact

↓

Agent Execution

↓

Output Generation

↓

Review

↓

Pass / Fail

↓

Lessons Learned
```

---

# Recommended Folder Structure

```text
test-run/

README.md

Test_Run_01/

    INPUT_REPORT_STORY_v1.0.md

    OUTPUT_MOCKUP_v1.0.md

    OUTPUT_MOCKUP_v1.0.svg

    REVIEW_NOTES.md

Test_Run_02/

    INPUT_REPORT_STORY_v1.0.md

    OUTPUT_MOCKUP_v2.0.md

    OUTPUT_MOCKUP_v2.0.svg

    REVIEW_NOTES.md
```

---

# Required Test Artifacts

## Input Artifact

Purpose

```text
Document the exact input provided to the Mockup Agent.
```

Example

```text
REPORT_STORY_v1.0.md
```

---

## Output Artifact 01

Purpose

```text
Capture generated markdown mockup.
```

Example

```text
MOCKUP_vX.X.md
```

---

## Output Artifact 02

Purpose

```text
Capture generated SVG prototype.
```

Example

```text
MOCKUP_vX.X.svg
```

---

## Review Notes

Purpose

```text
Document findings.

Document issues.

Document improvements.

Document validation results.
```

Example

```text
Pass

Fail

Improvement Opportunities

Architecture Changes

Lessons Learned
```

---

# Standard Validation Checklist

Every test run should verify:

```text
□ DSC Successfully Read

□ Story Preserved

□ Section Order Preserved

□ Business Questions Preserved

□ Visual Recommendations Preserved

□ Layout Pattern Selected

□ Layout Pattern Applied

□ Information Hierarchy Applied

□ ZIP / ZAP Flow Applied

□ MOCKUP Generated

□ SVG Generated

□ SVG Template Applied

□ UX Theme Applied

□ SVG Guidelines Applied
```

---

# Mockup Validation Checklist

Verify:

```text
□ Story Flow Clear

□ Business Journey Clear

□ Section Purpose Defined

□ Decision Support Visible

□ Visual Containers Appropriate

□ Reading Order Logical
```

---

# SVG Validation Checklist

Verify:

```text
□ Layout Pattern Visible

□ Header Present

□ Filters Present

□ Visual Hierarchy Clear

□ Cards Consistent

□ Section Order Preserved

□ Operational Briefing Appears Last

□ Theme Applied Consistently

□ Business Review Ready
```

---

# Test Results

## PASS

A test passes when:

```text
Story Preserved

Layout Preserved

Mockup Generated

SVG Generated

Business Review Successful
```

---

## FAIL

A test fails when:

```text
Story Lost

Layout Violated

Sections Reordered

SVG Incorrect

Business Intent Changed
```

---

# Current Approved Test Runs

## Test Run 01

Capability

```text
Animal Flow — Live Capacity Reporting
```

Results

```text
MOCKUP_v1.0.md

MOCKUP_v1.0.svg
```

Outcome

```text
Pass With Improvements Identified

Created UX Theme Standard

Created Layout Pattern Standard

Created SVG Template
```

---

## Test Run 02

Capability

```text
Animal Flow — Live Capacity Reporting
```

Results

```text
MOCKUP_v2.0.md

MOCKUP_v2.0.svg
```

Outcome

```text
PASS

Layout Pattern Applied

Decision Intelligence Command Centre Applied

UX Theme Applied

SVG Template Applied

Business Prototype Generated
```

---

# Lessons Learned Repository

Document:

```text
Architectural Discoveries

Template Improvements

Layout Improvements

Theme Improvements

SVG Improvements

Agent Enhancements
```

to continuously improve the Mockup Agent.

---

# Success Statement

The Test Run folder succeeds when:

```text
Every Agent Change

is validated

before production use
```

and:

```text
Every approved output

can be reproduced

using the same inputs,
standards,
templates,
and guidelines.
```

The result is:

```text
A Repeatable

Governed

Decision-Driven

Mockup Development Process
```