# INPUT_BRD_AnimalFlow_LiveCapacity_v2.0.md
## BC SPCA — Animal Flow Capacity Intelligence

---

# Document Metadata

Document Type

Business Requirements Document (BRD)

Version

2.0

Capability Name

Animal Flow — Live Capacity Reporting

Capability Domain

Operations / Animal Flow

Department

Animal Flow

Author

Tomas Leung

Status

Draft

Decision Support

Monitor capacity availability, utilization, and data quality across all Community Animal Centres (CACs) to support animal placement, operational prioritization, and capacity management decisions. 【1-835748】

---

# SECTION 01 — BUSINESS SUMMARY

## Purpose

Provide Animal Flow with a centralized analytical view of:

- Capacity utilization
- Capacity availability
- Data quality
- Centre comparisons
- Regional monitoring
- Operational prioritization

The solution complements the Live Capacity Management Power App by providing provincial and regional intelligence across all centres. 【1-835748】

---

## Business Goals

- Improve animal placement decisions
- Reduce manual centre review
- Improve operational visibility
- Improve capacity planning
- Improve identification of data quality issues
- Provide actionable operational insights

---

# SECTION 02 — BUSINESS PROBLEM

## Current Challenges

Animal Flow currently reviews centres individually.

Current limitations include:

- No provincial dashboard
- No regional rollup
- No executive KPI monitoring
- No comparative centre analysis
- Limited trend visibility
- Limited narrative insights

Consequences include:

- Placement opportunities may be missed
- Capacity constraints may go unnoticed
- Data quality issues may remain unresolved
- Operational reviews require significant manual effort
- Decision making is slower than desired 【1-835748】

---

# SECTION 03 — DECISION MODEL

## Primary Decision

Which centres currently have sufficient capacity to support incoming animals? 【1-835748】

### Decision Owner

Animal Flow Team

### Decision Frequency

Multiple Times Daily

---

## Secondary Decision A

Which centres require operational attention because of:

- Capacity limitations
- Stale updates
- Emergency closures
- Data quality concerns

### Decision Owner

Animal Flow Leadership

### Decision Frequency

Daily Operational Review

---

## Secondary Decision B

Which regions are experiencing capacity pressure and require operational adjustments?

### Decision Owner

Animal Flow Management

### Decision Frequency

Weekly
Monthly

---

# SECTION 04 — CURRENT STATE (AS-IS)

Current Process

```text
Animal Flow
↓
Live Capacity Management App
↓
Review One Centre At A Time
↓
Manual Comparison
↓
Operational Decision
```

Current limitations:

- Provincial visibility unavailable
- Regional visibility unavailable
- Data quality review separated from capacity review
- Decisions rely on local observations rather than aggregate intelligence 【1-835748】

---

# SECTION 05 — FUTURE STATE (TO-BE)

## Provincial Monitoring

Required capabilities:

- Total DOG Capacity
- Total CAT Capacity
- Open Space Availability
- Utilization Metrics
- Emergency Closure Monitoring

---

## Regional Monitoring

Required capabilities:

- Capacity By Region
- Capacity By Centre
- Capacity Comparison
- Operational Risk Monitoring

---

## Data Quality Monitoring

Required capabilities:

- Missing Kennel Assignments
- Unconfirmed Capacity Updates
- Stale Data
- Assignment Accuracy

---

## Decision Support

Required capabilities:

- Centre Prioritization
- Capacity Risk Identification
- Operational Exception Management
- Narrative Analysis
- Commentary

---

# SECTION 06 — BUSINESS QUESTIONS

## Capacity Questions

- Which centres currently have available DOG capacity?
- Which centres currently have available CAT capacity?
- Which centres are approaching critical utilization?
- Which centres have no available capacity?
- Which centres have emergency closures in effect?

---

## Data Quality Questions

- Which centres have animals missing kennel assignments?
- Which centres have stale capacity updates?
- Which centres have not confirmed capacity status?
- Which centres require data quality review?

---

## Operational Questions

- Which regions have the highest utilization?
- Which centres require intervention?
- Which centres should be prioritized for intake decisions?

---

## Future Questions (Out Of Scope)

- Predictive capacity forecasting
- Seasonal trend modelling
- Capacity demand forecasting
- Automated placement recommendations 【1-835748】

---

# SECTION 07 — REQUIRED INFORMATION (SIGNALS)

## Capacity Signals

- Total DOG Spaces
- Open DOG Spaces
- Total CAT Spaces
- Open CAT Spaces
- DOG Utilization %
- CAT Utilization %
- Emergency Closure Status

Purpose

Identify capacity availability and placement opportunities. 【1-835748】

---

## Data Quality Signals

- Missing Kennel Assignments
- Assignment Accuracy %
- Capacity Confirmation Status
- Last Capacity Update
- ShelterBuddy Last Sync

Purpose

Validate confidence and trust in the operational information. 【1-835748】

---

# SECTION 08 — KPI CONTRACTS

## Capacity Utilization %

Business Definition

Percentage of operational spaces currently occupied.

Calculation

```text
In Use Spaces
÷
Total Capacity
```

Owner

Animal Flow

Type

Operational KPI

Update Frequency

Near Real-Time

---

## Missing Assignment Count

Business Definition

Animals assigned to a shelter location without a valid kennel.

Owner

Centre Manager

Type

Data Quality KPI

Update Frequency

Near Real-Time

---

## Capacity Confirmation Rate

Business Definition

Percentage of centres that have confirmed capacity status.

Owner

Animal Flow

Type

Governance KPI

Update Frequency

Daily 【1-835748】

---

# SECTION 09 — DATA SOURCES

| Data Domain | Source System | Purpose |
|------------|--------------|----------|
| Capacity Configuration | CAT Master | Space Inventory |
| Capacity Configuration | DOG Master | Space Inventory |
| Animal Occupancy | ShelterBuddy | Occupancy Source |
| Capacity Confirmation | Power App | Operational Sign-off |
| Utilization Summary | Live Capacity Management | KPI Generation |

Source systems identified for reporting implementation. 【1-835748】

---

# SECTION 10 — SCOPE

## In Scope

- Provincial Capacity Dashboard
- Regional Capacity Dashboard
- Centre Comparison Reporting
- Capacity Utilization KPIs
- Data Quality KPIs
- Confirmation Tracking
- Narrative Analysis
- Power App Drillthrough Links

---

## Out Of Scope

- Capacity Management
- Floor Plan Editing
- ShelterBuddy Record Maintenance
- Kennel Configuration Management
- Predictive Analytics
- Automated Animal Placement 【1-835748】

---

# SECTION 11 — ASSUMPTIONS

- Live Capacity Management is the operational source of truth.
- ShelterBuddy is the authoritative occupancy source.
- Centres maintain information accurately.
- Power App information is available for reporting. 【1-835748】

---

# SECTION 12 — CONSTRAINTS

- Reporting depends on operational updates.
- Data quality depends on centre compliance.
- Narrative insights depend on underlying data quality.
- Data latency depends on synchronization schedules. 【1-835748】

---

# SECTION 13 — SUCCESS CRITERIA

## Visibility

Animal Flow can monitor all centres through a single dashboard.

Regional and provincial capacity can be reviewed without opening multiple centre views.

---

## Decision Support

Capacity-related decisions become faster.

Priority centres can be identified quickly.

---

## Data Quality

Missing kennel assignments are visible.

Stale or unconfirmed data is easily identified.

---

## Adoption

Power BI becomes the monitoring layer.

Power App remains the operational management layer. 【1-835748】

---

# SECTION 14 — DATA VALIDATION REQUIREMENTS

The solution must validate:

- Dashboard totals reconcile to Live Capacity Management
- Capacity counts reconcile to floor plan calculations
- Missing assignment counts reconcile to ShelterBuddy
- Data freshness indicators are accurate
- Narrative insights align with metrics 【1-835748】

---

# SECTION 15 — ACCEPTANCE CRITERIA

## Governance

- Product Owner Approval
- Data Owner Approval
- KPI Definitions Approved

---

## Operational Readiness

- Provincial Dashboard Available
- Regional Dashboard Available
- Centre Drillthrough Operational

---

## Data Integrity

- Capacity Counts Reconcile
- Data Quality Metrics Validated
- Dashboard Refresh Successful

---

# SECTION 16 — STAKEHOLDERS

## Product Owner

Cynthia Boulter

---

## Data Owner

Kahlee Demers

---

## Data Architecture

Tomas Leung

---