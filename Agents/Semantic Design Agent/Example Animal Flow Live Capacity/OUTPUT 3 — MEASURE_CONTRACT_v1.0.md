# MEASURE_CONTRACT_v1.0
## Animal Flow — Capacity Intelligence

---

# MEASURE — Animals In Care

Business Definition

Current occupied animal count.

Business Question

How many animals are currently being supported?

Signal

Animal Occupancy

Source Fact

Fact_Occupancy

Calculation Logic

Count Active Animal Occupancy Records

Decision Supported

Capacity Monitoring

---

# MEASURE — Care Capacity

Business Definition

Maximum operational animal capacity.

Business Question

How much capacity exists?

Signal

Care Capacity

Source Fact

Fact_Capacity

Calculation Logic

Sum Care Capacity

Decision Supported

Capacity Monitoring

---

# MEASURE — Remaining Capacity

Business Definition

Available care capacity after occupancy.

Business Question

Which centres can receive another animal?

Signal

Remaining Capacity

Source Fact

Fact_Capacity

Calculation Logic

Care Capacity
-
Animals In Care

Thresholds

Green

Greater Than 0

Action

Candidate Centre

Decision Supported

Which centres can safely receive additional animals?

---

# MEASURE — Capacity Utilization %

Business Definition

Percentage of care capacity currently utilized.

Business Question

How close is a centre to being full?

Signal

Capacity Utilization

Source Fact

Fact_Capacity
+
Fact_Occupancy

Calculation Logic

Animals In Care
/
Care Capacity

Thresholds

<80%
Healthy
Candidate Centre

80%-99%
Monitor
Review Before Routing

>=100%
Full
Do Not Intake

Decision Supported

Can this centre safely receive additional animals?

---

# MEASURE — Available Centres

Business Definition

Count of centres below warning threshold.

Business Question

How many centres are intake ready?

Signal

Capacity Utilization %

Calculation Logic

Count Centres
Where Utilization < 80%

Decision Supported

Can we intake more animals?

---

# MEASURE — Monitor Centres

Business Definition

Centres approaching capacity.

Business Question

Which centres require review?

Signal

Capacity Utilization %

Calculation Logic

Count Centres
Between 80% And 99%

Decision Supported

Which centres require intervention?

---

# MEASURE — Centres At Capacity

Business Definition

Count of centres operating at or above care capacity.

Business Question

Which centres should be avoided?

Signal

Capacity Utilization %

Calculation Logic

Count Centres
>= 100%

Decision Supported

Which centres should be avoided for intake?

---

# MEASURE — Missing Assignments

Business Definition

Animals without valid assignments.

Business Question

Can the data be trusted?

Signal

Assignment Completeness

Source Fact

Fact_Occupancy

Calculation Logic

Count Missing Assignments

Thresholds

0
Healthy

1–3
Warning

>3
Critical

Actions

Healthy
No Action

Warning
Review

Critical
Data Cleanup Required

Decision Supported

Can the information be trusted?

---

# MEASURE — Assignment Accuracy %

Business Definition

Percentage of valid assignment records.

Business Question

How accurate is operational data?

Signal

Assignment Accuracy

Source Fact

Fact_Occupancy

Calculation Logic

Valid Assignments
/
Total Assignments

Decision Supported

Can the information be trusted?

---

# MEASURE — Species Occupancy Impact

Business Definition

Capacity occupied by non-target species.

Business Question

Can capacity be recovered through housing review?

Signal

Species Occupancy

Source Fact

Fact_Occupancy

Calculation Logic

Count Non-Target Species Occupying Target Capacity

Thresholds

0
Normal

1–3
Monitor

>3
Significant

Actions

Review Housing

Recover Capacity

Decision Supported

Can capacity be recovered?

---

# MEASURE — Regional Utilization %

Business Definition

Average utilization across centres within a region.

Business Question

Which regions are under pressure?

Signal

Regional Utilization

Calculation Logic

Regional Occupancy
/
Regional Capacity

Thresholds

<80%
Healthy

80%-89%
Monitor

>=90%
High Pressure

Decision Supported

Where is capacity pressure building?

---

# MEASURE DEPENDENCY MAP

Animals In Care
      │
      ├── Remaining Capacity
      │
      └── Capacity Utilization %

Care Capacity
      │
      ├── Remaining Capacity
      │
      └── Capacity Utilization %

Missing Assignments
      │
      └── Assignment Accuracy %

Species Occupancy Impact
      │
      ├── CAT Capacity Impact
      │
      └── DOG Capacity Impact

---

# GOVERNANCE REVIEW

✓ Explicit Measures

✓ Business Definitions

✓ Decision Traceability

✓ Threshold Mapping

✓ Action Mapping

✓ Documentation Complete