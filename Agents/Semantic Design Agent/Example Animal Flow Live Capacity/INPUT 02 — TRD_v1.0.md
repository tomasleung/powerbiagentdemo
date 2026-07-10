# TRD_v1.0
## Animal Flow — Capacity Intelligence

# Report Overview

Purpose

Provide operational decision support for Animal Flow by identifying:

- Intake-ready centres
- Capacity risks
- Data quality concerns
- Species occupancy impacts
- Regional pressure

Primary Decision Supported

Which centres can safely receive additional animals?

---

# Source & Target Mapping

## Source Systems

### Capacity Platform

Target

Fact_Capacity

Provides

- Care Capacity
- Physical Capacity
- Open Spaces
- Space Utilization

---

### ShelterBuddy

Target

Fact_Occupancy

Provides

- Animal Records
- Occupancy
- Assignment Information
- Species Information

---

### Capacity Confirmation Process

Target

Fact_Confirmation

Provides

- Confirmation Status
- Update Time
- Freshness Metrics

---

# High-Level Data Model

## Fact Tables

Fact_Capacity

Fact_Occupancy

Fact_Confirmation

---

## Dimension Tables

Dim_Centre

Dim_Date

Dim_Animal_Type

Dim_Region

---

# Measure Inventory

Animals In Care

Care Capacity

Remaining Capacity

Capacity Utilization %

Available Centres

Monitor Centres

Centres At Capacity

Open Spaces

Missing Assignments

Assignment Accuracy %

Species Occupancy Impact

Regional Utilization %

Regional Capacity %

Regional Open Space %

---

# Visual Mapping

Operational Snapshot
→ KPI Cards

Action Required
→ Exception KPI Cards

Intake Readiness
→ Status KPI Cards

Placement Decision Board
→ Table

Capacity vs Occupancy
→ Comparison Summary

Species Occupancy
→ Breakdown Summary

Data Trust
→ Exception Summary

Regional Health
→ Regional Ranking

AI Operational Briefing
→ Recommendation Cards

---

# Interaction Design

Animal Type Filter

Region Filter

Centre Selection

Drillthrough Navigation

---

# Security Design

Animal Flow
→ All Centres

Leadership
→ All Centres

Future Centre Managers
→ Assigned Centre Only

---

# Validation Rules

Open + Hold + In Use + Unavailable
=
Total Space

Animals In Care ≥ 0

Care Capacity ≥ 0

Missing Assignments must reconcile with ShelterBuddy

---

# Deployment Considerations

Development

↓

Test

↓

Production

Dependencies

- Capacity Platform
- ShelterBuddy
- Capacity Confirmation Process
- Microsoft Fabric
- Power BI