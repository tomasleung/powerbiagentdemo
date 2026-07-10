# DATA_MODEL_MATRIX_v1.0
## Animal Flow — Capacity Intelligence

---

# SECTION 01 — DECISION MODEL

## Primary Decision

Which centres can safely receive additional animals?

### Supported By

- Capacity Availability
- Occupancy
- Species Impact
- Data Trust
- Centre Status

---

## Secondary Decisions

### Placement

- Which centres should receive additional animals?
- Which centres should be prioritized?

### Risk

- Which centres require intervention?
- Which centres should be avoided?

### Data Trust

- Can the information be trusted?

### Regional

- Which regions are approaching capacity pressure?

---

# SECTION 02 — SIGNAL INVENTORY

## Capacity Signals

- Animals In Care
- Care Capacity
- Open Spaces
- Remaining Capacity
- Capacity Utilization %
- Emergency Closure

Supported Decision

Can this centre receive another animal?

---

## Species Occupancy Signals

- Cats In Care
- Dogs In Care
- Other Animals
- CAT Occupancy Impact
- DOG Occupancy Impact

Supported Decision

Can capacity be recovered?

---

## Data Trust Signals

- Missing Assignments
- Assignment Accuracy %
- Pending Confirmation
- Stale Updates
- Confirmation Status

Supported Decision

Can the information be trusted?

---

## Regional Signals

- Regional Utilization %
- Regional Capacity %
- Regional Open Space %

Supported Decision

Where is capacity pressure building?

---

# SECTION 03 — MEASURE INVENTORY

## Operational Snapshot

- Total Centres
- Animals In Care
- Care Capacity
- Open Spaces
- CAT Spaces
- DOG Spaces

---

## Intake Readiness

- Available Centres
- Monitor Centres
- Centres At Capacity
- Remaining Capacity
- Capacity Utilization %

---

## Data Trust

- Missing Assignments
- Assignment Accuracy %
- Pending Confirmations
- Stale Updates

---

## Species Occupancy

- Species Occupancy Impact
- CAT Capacity Impact
- DOG Capacity Impact

---

## Regional

- Regional Utilization %
- Regional Capacity %
- Regional Open Space %

---

# SECTION 04 — GRAIN ANALYSIS

## Fact_Capacity

Business Grain

One Centre
+
One Date
+
One Animal Type

Business Purpose

Store operational capacity metrics.

---

## Fact_Occupancy

Business Grain

One Animal
+
One Centre
+
One Date

Business Purpose

Store occupancy and assignment details.

---

## Fact_Confirmation

Business Grain

One Centre
+
One Confirmation Event

Business Purpose

Store freshness and confirmation status.

---

# SECTION 05 — FACT IDENTIFICATION

## Fact_Capacity

Supports Signals

- Care Capacity
- Open Spaces
- Capacity Utilization

Supports Measures

- Care Capacity
- Remaining Capacity
- Open Spaces
- Capacity Utilization %

---

## Fact_Occupancy

Supports Signals

- Animals In Care
- Species Occupancy
- Assignment Status

Supports Measures

- Animals In Care
- Missing Assignments
- Assignment Accuracy %
- Species Occupancy Impact

---

## Fact_Confirmation

Supports Signals

- Confirmation Status
- Update Freshness

Supports Measures

- Pending Confirmations
- Stale Updates

---

# SECTION 06 — DIMENSION IDENTIFICATION

## Dim_Centre

Purpose

Business location and organizational context.

Attributes

- Centre Code
- Centre Name
- Region
- Location

---

## Dim_Date

Purpose

Time intelligence.

Attributes

- Date
- Week
- Month
- Quarter
- Year

---

## Dim_Animal_Type

Purpose

Animal classification.

Attributes

- Animal Type
- Animal Category

Values

- Cat
- Dog
- Rabbit
- Small Animal
- Other

---

## Dim_Region

Purpose

Regional grouping.

Attributes

- Region Name

Values

- Interior
- Island
- Lower Mainland
- North

---

# SECTION 07 — FACT TO DIMENSION MATRIX

Fact_Capacity

- Dim_Centre
- Dim_Date
- Dim_Animal_Type

Fact_Occupancy

- Dim_Centre
- Dim_Date
- Dim_Animal_Type

Fact_Confirmation

- Dim_Centre
- Dim_Date

---

# SECTION 08 — SEMANTIC MODEL BLUEPRINT

Dim_Region
      ↓

Dim_Centre
      ↓

Fact_Capacity

Dim_Centre
      ↓

Fact_Occupancy

Dim_Centre
      ↓

Fact_Confirmation

Dim_Date
      ↓

All Facts

Dim_Animal_Type
      ↓

Fact_Capacity

Dim_Animal_Type
      ↓

Fact_Occupancy

---

# APPROVAL STATUS

□ Decision Model Approved

□ Signals Approved

□ Measures Approved

□ Grain Approved

□ Facts Approved

□ Dimensions Approved

Next Deliverable

SEMANTIC_MODEL_SPEC_v1.0