BRD
↓
DSC Matrix (Fast Review)
↓
DSC Document (Formal)
↓
Markdown Wireframe
↓
SVG Mockup
↓
TRD
↓
Build

**Final Skill Output Flow**
OUTPUT 1
REPORT_STORY_MATRIX_v1.0.md

OUTPUT 2
REPORT_STORY_v1.0.md

OUTPUT 3
MOCKUP_v1.0.md

OUTPUT 4
MOCKUP_v1.0.svg

OUTPUT 5
TRD_v1.0.md

Structure:
# REPORT STORY MATRIX

## Step 1 — Decision Model

### Primary Decision

Which centres can safely receive additional animals?

### Secondary Decisions

- Which centres require intervention?
- Which centres should be avoided for intake?
- Which centres require data quality review?
- Which regions are approaching capacity limits?

### Key Discovery

Intake decisions are driven by:

```text
Care Capacity
+
Animals In Care
+
Physical Space
+
Data Trust
+
Species Occupancy
```

NOT merely:

```text
Open Spaces
```

---

## Step 2 — Question Matrix

| Business Question | Priority |
|----------|----------|
| Which centres have available CAT capacity? | High |
| Which centres have available DOG capacity? | High |
| Which centres are approaching critical utilization? | High |
| Which centres have emergency closures? | High |
| Which centres require intervention? | High |

---

## Step 3 — Signal Matrix

### Placement Signals

- Animals In Care
- Care Capacity
- Care Capacity %
- Remaining Capacity
- Emergency Closure

### Physical Capacity Signals

- Total Spaces
- Open Spaces
- In Use
- Hold
- Unavailable

### Species Occupancy Signals

- Cats In Care
- Dogs In Care
- Other Animals
- CAT Spaces Occupied By Other Animals
- DOG Spaces Occupied By Other Animals

### Data Trust Signals

- Missing Assignments
- Confirmation Status
- Last Update Time

---

## Step 4 — Action Matrix

### Care Capacity %

| Threshold | Status | Action |
|-----------|---------|---------|
| <80% | Healthy | Candidate Centre |
| 80-99% | Monitor | Review Before Routing |
| 100%+ | Full | Do Not Intake |

### Missing Assignments

| Threshold | Status | Action |
|-----------|---------|---------|
| 0 | Healthy | None |
| 1-3 | Warning | Review |
| >3 | Critical | Data Cleanup |

### Stale Updates

| Threshold | Status | Action |
|-----------|---------|---------|
| <12 Hours | Current | Use |
| 12-24 Hours | Aging | Validate |
| >24 Hours | Stale | Contact Centre |

---

## Step 5 — Report Story

### Question 1

Can this centre safely take another animal?

Output:

```text
Intake Readiness
```

---

### Question 2

Which centres should be prioritized?

Output:

```text
Placement Decision Board
```

---

### Question 3

Why can or can't a centre receive animals?

Output:

```text
Capacity vs Occupancy
```

---

### Question 4

How is capacity being consumed?

Output:

```text
Species Occupancy
```

---

### Question 5

Can the data be trusted?

Output:

```text
Data Trust
```

---

### Question 6

Where is capacity pressure building?

Output:

```text
Regional Health
```

---

### Question 7

What should Animal Flow do next?

Output:

```text
AI Operational Briefing
```

---

## Step 6 — Layout Blueprint

```text
Operational Snapshot
↓
Action Required
↓
Intake Readiness
↓
Placement Decision Board
↓
Capacity vs Occupancy
↓
Species Occupancy
↓
Data Trust
↓
Regional Health
↓
AI Operational Briefing
```

---

## Step 7 — Visual Recommendations

| Section | Visual |
|----------|----------|
| Operational Snapshot | KPI Cards |
| Action Required | Exception KPI Cards |
| Intake Readiness | Status Cards |
| Placement Decision Board | Priority Table |
| Capacity vs Occupancy | KPI + Comparison |
| Species Occupancy | Breakdown Chart |
| Data Trust | Exception Matrix |
| Regional Health | Horizontal Bar |
| AI Operational Briefing | Narrative Card |

---

## Approval Checkpoint

✅ Decision Approved

✅ Questions Approved

✅ Signals Approved

✅ Actions Approved

✅ Story Approved

➡ Proceed to DSC Document

**Final Skill Output Flow**
OUTPUT 1
REPORT_STORY_MATRIX_v1.0.md

OUTPUT 2
REPORT_STORY_v1.0.md

OUTPUT 3
MOCKUP_v1.0.md

OUTPUT 4
MOCKUP_v1.0.svg

OUTPUT 5
TRD_v1.0.md

**This gives you a very clean review process:**
Matrix
↓
Narrative
↓
Layout
↓
Visual
↓
Technical