# OUTPUT 3 — MEASURE_CONTRACT_AGENT_RUN_v2.0
## Animal Flow — Capacity Intelligence
### Measure Governance Specification

---

# Document Metadata

Document Type

Measure Contract

Version

2.0

Artifact Type

Semantic Design Artifact

Owner

BI Architecture

Status

Draft

Purpose

Define business measures, calculation logic, thresholds, actions, dependencies, and decision support for the Animal Flow model.

---

# MEASURE 01 — Animals In Care

Business Definition

The total number of animals currently assigned to care at a centre for a specific animal type.

Calculation Logic

Sum(AnimalsInCare)

Thresholds

Normal: > 0

Actions

Use for intake readiness and occupancy monitoring.

Dependencies

Fact_Occupancy.AnimalsInCare

Decision Supported

Which centres can safely receive additional animals?

---

# MEASURE 02 — Care Capacity

Business Definition

The total care capacity available for an animal type at a centre.

Calculation Logic

Sum(CareCapacity)

Thresholds

Normal: ≥ 0

Actions

Use to determine intake readiness and remaining capacity.

Dependencies

Fact_Capacity.CareCapacity

Decision Supported

Which centres can safely receive additional animals?

---

# MEASURE 03 — Remaining Capacity

Business Definition

The difference between care capacity and current animals in care for a centre and animal type.

Calculation Logic

CareCapacity - AnimalsInCare

Thresholds

Green: > 0
Amber: = 0
Red: < 0

Actions

Prioritize intake at centres with positive remaining capacity; flag centres with zero or negative remaining capacity.

Dependencies

Fact_Capacity.CareCapacity
Fact_Occupancy.AnimalsInCare

Decision Supported

Which centres are intake-ready and which are at capacity?

---

# MEASURE 04 — Capacity Utilization %

Business Definition

The percentage of care capacity currently occupied by animals in care.

Calculation Logic

Case when CareCapacity > 0 then AnimalsInCare / CareCapacity * 100 else null end

Thresholds

Normal: < 80%
Watch: 80–95%
Critical: > 95%

Actions

Identify centres approaching or exceeding critical utilization.

Dependencies

Fact_Capacity.CareCapacity
Fact_Occupancy.AnimalsInCare

Decision Supported

Which centres are approaching critical utilization?

---

# MEASURE 05 — Available Centres

Business Definition

The count of centres with positive available capacity.

Calculation Logic

Count where RemainingCapacity > 0

Thresholds

Normal: > 0

Actions

Identify intake-ready centres.

Dependencies

Fact_Capacity.RemainingCapacity

Decision Supported

Which centres should receive additional animals?

---

# MEASURE 06 — Centres At Capacity

Business Definition

The count of centres operating at or above care capacity.

Calculation Logic

Count where RemainingCapacity <= 0

Thresholds

Normal: 0
Warning: 1–3
Critical: > 3

Actions

Trigger intake restrictions and risk review.

Dependencies

Fact_Capacity.RemainingCapacity

Decision Supported

Which centres should be avoided for intake?

---

# MEASURE 07 — Missing Assignments

Business Definition

The number of animal assignment records that are incomplete or missing.

Calculation Logic

Sum(MissingAssignments)

Thresholds

Normal: 0
Warning: 1–5
Critical: > 5

Actions

Trigger investigation and reconciliation of occupancy data.

Dependencies

Fact_Occupancy.MissingAssignments

Decision Supported

Which centres require data quality review?

---

# MEASURE 08 — Assignment Accuracy %

Business Definition

The percentage of assignment records that are validated and correct.

Calculation Logic

Sum(ValidAssignments) / Sum(TotalAssignments) * 100

Thresholds

Normal: ≥ 95%
Warning: 80–94%
Critical: < 80%

Actions

Trigger review for centres below threshold.

Dependencies

Fact_Occupancy.AssignmentAccuracyPct

Decision Supported

Which centres require data quality review?

---

# MEASURE 09 — Species Occupancy Impact

Business Definition

The amount of capacity occupied by animals that do not match the centre's intended species type.

Calculation Logic

Case when AnimalType = Cat then OtherAnimals else if AnimalType = Dog then OtherAnimals else 0 end

Thresholds

Normal: 0
Warning: > 0

Actions

Investigate cross-species occupancy and update placement policies.

Dependencies

Fact_Occupancy.OtherAnimals
Fact_Occupancy.SpeciesOccupancyImpact

Decision Supported

How much capacity is occupied by non-native species?

---

# MEASURE 10 — Regional Utilization %

Business Definition

The percentage of care capacity used across a region.

Calculation Logic

Sum(AnimalsInCare) / Sum(CareCapacity) * 100 by Region

Thresholds

Normal: < 80%
Watch: 80–95%
Critical: > 95%

Actions

Monitor regions with rising pressure and prioritize intake avoidance.

Dependencies

Fact_Capacity.CareCapacity
Fact_Occupancy.AnimalsInCare
Dim_Centre.RegionID

Decision Supported

Where is capacity pressure building?

---

# MEASURE 11 — Regional Capacity %

Business Definition

The percentage of total region capacity that is currently available.

Calculation Logic

Sum(RemainingCapacity) / Sum(CareCapacity) * 100 by Region

Thresholds

Normal: > 20%
Warning: 10–20%
Critical: < 10%

Actions

Identify regions requiring intake restriction.

Dependencies

Fact_Capacity.RemainingCapacity
Dim_Centre.RegionID

Decision Supported

Where is capacity pressure building regionally?

---

# MEASURE 12 — Regional Open Space %

Business Definition

The percentage of total region care capacity represented by open spaces.

Calculation Logic

Sum(OpenSpaces) / Sum(CareCapacity) * 100 by Region

Thresholds

Normal: > 20%
Warning: 10–20%
Critical: < 10%

Actions

Determine regions with available intake capacity.

Dependencies

Fact_Capacity.OpenSpaces
Dim_Centre.RegionID

Decision Supported

Which regions have the highest available capacity?

---

# SECTION 13 — GOVERNANCE REVIEW

- Explicit measures are defined for all key decisions.
- Measures include business definitions, calculation logic, thresholds, and actions.
- Dependencies are aligned to fact tables.
- Performance guidance is addressed by limiting measure complexity and using aggregate logic where possible.
