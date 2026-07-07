# Decision-Driven BI Report Design Skill
## Purpose

Transform a Business Requirements Document (BRD) into a Power BI report design by starting with decisions and actions rather than visuals.

This skill follows the Decision-Driven BI Framework:

Decision
↓
Business Question
↓
Signal
↓
Threshold
↓
Action
↓
Story
↓
Visual
↓
Report Design

---

# Core Principles

## Rule 1 — Decision First

Never start with visuals.

Start with:

- Decision Supported
- Business Questions
- User Personas
- Required Actions

If the decision is unclear, stop and clarify before designing.

---

## Rule 2 — Every KPI Must Support Action

Every KPI must contain:

Signal
↓
Threshold
↓
Action
↓
Decision

Example:

KPI:
Care Capacity %

Signal:
Animals In Care ÷ Care Capacity

Threshold:
<80% Healthy
80%-99% Monitor
100%+ Full

Action:
Healthy → Continue Intake
Monitor → Review
Full → Do Not Intake

Decision:
Can this centre safely receive another animal?

---

## Rule 3 — If No Action Exists, Remove the KPI

Do not place metrics on Page 1 that do not support a decision.

Bad:

Total Animals

Good:

Care Capacity Remaining

because it supports intake decisions.

---

## Rule 4 — Story Before Visuals

Do not select charts until the report story has been defined.

Wrong:

Data → Chart

Correct:

Decision → Question → Signal → Action → Story → Chart

---

# Required Inputs

The skill expects the following BRD inputs:

Decision Supported
Business Questions
Required Information / Signals
KPI Contracts
Threshold Rules
User Personas
Scope

---

# Step 1 — Extract Decision Model

Generate:

Primary Decision
Secondary Decisions
Decision Owner
Decision Frequency

Output Format:

Primary Decision:
Which centre can safely receive additional animals?

Secondary Decisions:
Which centres require intervention?
Which centres require data quality review?

Decision Owner:
Animal Flow

Frequency:
Daily Operational Monitoring

---

# Step 2 — Build Business Question Matrix

Convert BRD business questions into a decision matrix.

Output Format:

Question:
Which centres currently have available CAT capacity?

Decision Category:
Placement

Priority:
High

Question:
Which centres have stale updates?

Decision Category:
Data Trust

Priority:
High

---

# Step 3 — Build Signal Matrix

Map each question to supporting signals.

Output Format:

Question:
Which centres can receive additional animals?

Signals:
Care Capacity
Animals in Care
Open Spaces

Question:
Can the data be trusted?

Signals:
Missing Assignments
Stale Updates
Confirmation Status

---

# Step 4 — Build Threshold Matrix

All operational signals must have thresholds.

Output Format:

Signal:
Care Capacity %

Thresholds:

<80%
Status: Healthy
Action: Continue Intake

80%-99%
Status: Monitor
Action: Review Centre

100%+
Status: Full
Action: Do Not Intake

---

Signal:
Missing Kennel Assignments

Thresholds:

0
Status: Healthy
Action: None

1-3
Status: Warning
Action: Review

>3
Status: Critical
Action: Correct Immediately

---

# Step 5 — Generate Report Story

The report story defines reading order and business flow.

Output Format:

Story Sequence:

1. Can we accept more animals?
2. Which centres are best positioned for intake?
3. What operational risks exist?
4. Can the data be trusted?
5. Which regions require attention?
6. What action should Animal Flow take today?

---

# Step 6 — Identify Page Archetype

Select the page purpose.

Available Archetypes:

Operational Command Centre
Executive Monitoring
Capacity Intelligence
Data Quality Investigation
Regional Performance
Exception Management

Output:

Primary Archetype:
Operational Command Centre

Secondary Archetype:
Exception Management

---

# Step 7 — Build Layout Blueprint

Generate a markdown dashboard wireframe.

Output Example:

ROW 1 — ACTION REQUIRED

Critical Centres
Data Quality Issues
Pending Confirmations
Emergency Closures

ROW 2 — PLACEMENT DECISION BOARD

Recommended Centres
Care Capacity Remaining
Intake Candidates

ROW 3 — CAPACITY HEALTH

Open Capacity
Utilization
Physical Space

ROW 4 — DATA TRUST

Missing Assignments
Stale Updates
Confirmation Status

ROW 5 — REGIONAL HEALTH

Region Utilization
Capacity Pressure

ROW 6 — AI BRIEFING

Operational Priorities
Recommended Actions

---

# Step 8 — Select Visuals

Only after the story is approved.

Output Format:

Question:
Which centres should receive animals?

Visual:
Priority Table

Reason:
Supports ranking and action.

---

Question:
Which regions are under pressure?

Visual:
Horizontal Bar Chart

Reason:
Easy comparison across regions.

---

Question:
Can the data be trusted?

Visual:
Exception Matrix

Reason:
Highlights operational risks.

---

# Step 9 — Generate Report Mockups

Generate outputs in sequence:

1. Markdown Wireframe
2. SVG Wireframe
3. Power BI Design Contract

Never generate Power BI visuals before the report story is approved.

---

# Page 1 Requirements

Page 1 must always answer:

What should I do?

Not:

What does the data say?

---

# Output Structure

Every report design must deliver:

Decision Summary
Question Matrix
Signal Matrix
Threshold Matrix
Action Matrix
Report Story
Page Archetype
Layout Blueprint
Visual Recommendations
Markdown Mockup
SVG Mockup
Design Contract

---

# Success Criteria

A successful report allows a user to:

Understand the decision
Identify the action required
Trust the supporting signals
Navigate from summary to detail
Take action without interpreting raw metrics

The final report should behave like a decision product rather than a reporting product.