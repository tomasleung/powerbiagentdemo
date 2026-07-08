┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│                     ANIMAL FLOW — CAPACITY INTELLIGENCE                                     │
│         Provincial Intake Readiness • Capacity Intelligence • Decision Support              │
└──────────────────────────────────────────────────────────────────────────────────────────────┘


ANIMAL TYPE
──────────────────────────────────────────────────────────────────────────────────────────────

[ All ]    [ Cat ]    [ Dog ]    [ Rabbit ]    [ Small Animal ]    [ Other ]

(Default = All)



SECTION 00 — OPERATIONAL SNAPSHOT
──────────────────────────────────────────────────────────────────────────────────────────────

Purpose:
Provide provincial context before reviewing decisions.

┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Total Centres│ │ Animals Care │ │ Care Capacity│ │ Open Spaces  │
│      32      │ │    1,875     │ │    2,140     │ │     390      │
└──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘

┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ CAT Spaces   │ │ DOG Spaces   │ │ Care Cap %   │
│     810      │ │     430      │ │     88%      │
└──────────────┘ └──────────────┘ └──────────────┘


Key Question

What is happening across the network today?



SECTION 01 — ACTION REQUIRED
──────────────────────────────────────────────────────────────────────────────────────────────

Purpose:
Immediate operational attention.

┌────────────────┐ ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
│ 🔴 At Capacity │ │ ⚠ Data Issues  │ │ 🟡 Not Confirm │ │ 🚨 Closures    │
│       4        │ │      18        │ │       3        │ │       2        │
└────────────────┘ └────────────────┘ └────────────────┘ └────────────────┘


Key Question

What needs my attention right now?



SECTION 02 — INTAKE READINESS
──────────────────────────────────────────────────────────────────────────────────────────────

Purpose:
Determine overall intake readiness.

┌────────────────┐ ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
│ Available      │ │ Monitor        │ │ Full           │ │ Closed         │
│      18        │ │       7        │ │       4        │ │       2        │
└────────────────┘ └────────────────┘ └────────────────┘ └────────────────┘


Business Rules

Available
=
Care Capacity < 80%

Monitor
=
Care Capacity 80% - 99%

Full
=
Care Capacity >= 100%

Closed
=
Emergency Closure Active


Key Question

Can we intake more animals today?



SECTION 03 — PLACEMENT DECISION BOARD
──────────────────────────────────────────────────────────────────────────────────────────────

Purpose:
Identify candidate centres.

┌──────────────┬─────────┬──────────┬──────────┬──────────┬────────────────┐
│ Centre       │ Animals │ Capacity │ Remaining│ Open Spc │ Recommendation │
├──────────────┼─────────┼──────────┼──────────┼──────────┼────────────────┤
│ Kelowna      │   15    │    25    │    10    │    8     │ ✅ Candidate    │
│ Nanaimo      │   20    │    25    │     5    │    6     │ 🟡 Monitor      │
│ Victoria     │   25    │    25    │     0    │    2     │ 🔴 Do Not Intake│
│ Williams Lk  │   25    │    25    │     0    │    6     │ ⚠ Review Data   │
└──────────────┴─────────┴──────────┴──────────┴──────────┴────────────────┘


Business Rule

Remaining Capacity
=
Care Capacity
-
Animals In Care


Key Question

Which centres should Animal Flow use first?



SECTION 04 — CAPACITY VS OCCUPANCY
──────────────────────────────────────────────────────────────────────────────────────────────

Purpose:
Explain why centres can or cannot receive animals.

┌────────────────────────────────────────┐
│ CARE CAPACITY HEALTH                   │
├────────────────────────────────────────┤
│ Animals In Care             1,875      │
│ Care Capacity               2,140      │
│ Remaining Capacity            265      │
│ Capacity Utilization          88%      │
└────────────────────────────────────────┘


┌────────────────────────────────────────┐
│ PHYSICAL SPACE HEALTH                  │
├────────────────────────────────────────┤
│ Total Spaces                1,240      │
│ Open Spaces                   390      │
│ In Use Spaces                 690      │
│ Hold Spaces                    90      │
│ Unavailable                    70      │
└────────────────────────────────────────┘


Key Question

Why are centres available or unavailable?




SECTION 05 — SPECIES OCCUPANCY
──────────────────────────────────────────────────────────────────────────────────────────────

Purpose:
Understand how non-target species consume capacity.

┌────────────────────────────────────────┐
│ ANIMAL BREAKDOWN                       │
├────────────────────────────────────────┤
│ Cats In Care                 925       │
│ Dogs In Care                 620       │
│ Other Animals                330       │
└────────────────────────────────────────┘


┌────────────────────────────────────────┐
│ CAPACITY IMPACT                         │
├────────────────────────────────────────┤
│ CAT Spaces Used By Other Animals   12  │
│ DOG Spaces Used By Other Animals    3  │
└────────────────────────────────────────┘


Top Impact Centres

┌──────────────┬─────────────────────────┐
│ Centre       │ Species Occupancy Impact│
├──────────────┼─────────────────────────┤
│ Nanaimo      │ 5                       │
│ Kelowna      │ 4                       │
│ Victoria     │ 3                       │
└──────────────┴─────────────────────────┘


Supported Questions

How much CAT capacity is being consumed by rabbits or small animals?

How much DOG capacity is being consumed by non-dog species?

Which centres have capacity constrained by other species?



SECTION 06 — DATA TRUST
──────────────────────────────────────────────────────────────────────────────────────────────

Purpose:
Measure confidence in the information.

┌──────────────────────┐ ┌──────────────────────┐
│ Missing Assignment   │ │ Assignment Accuracy  │
│         18           │ │        96%           │
└──────────────────────┘ └──────────────────────┘

┌──────────────────────┐ ┌──────────────────────┐
│ Pending Confirm      │ │ Stale Updates        │
│          3           │ │          2           │
└──────────────────────┘ └──────────────────────┘


Business Rules

Missing Assignments > 3
=
Review Required

Update Age > 24 Hours
=
Contact Centre


Key Question

Can I trust the data?



SECTION 07 — REGIONAL HEALTH
──────────────────────────────────────────────────────────────────────────────────────────────

Purpose:
Monitor pressure across regions.

Interior         █████████░░   89%   🔴 High

Island           ████████░░░   78%   🟡 Monitor

Lower Mainland   ███████░░░░   72%   🟢 Healthy

North            ██████░░░░░   61%   🟢 Healthy


Key Question

Where is capacity pressure building?



SECTION 08 — AI OPERATIONAL BRIEFING
──────────────────────────────────────────────────────────────────────────────────────────────

Purpose:
Provide recommended actions.

TODAY'S PRIORITIES

1. Victoria

   Care Capacity has been reached.

   Recommendation:
   Do not route additional animals.


2. Williams Lake

   Data quality issues detected.

   Recommendation:
   Review ShelterBuddy assignments.


3. Kelowna

   Highest remaining care capacity.

   Recommendation:
   Candidate for overflow intake.


4. Nanaimo

   CAT capacity is being impacted by
   non-cat species occupancy.

   Recommendation:
   Review alternate housing options.



SECTION 09 — QUICK ACTIONS
──────────────────────────────────────────────────────────────────────────────────────────────

[ Review Critical Centres ]

[ Review Data Quality Issues ]

[ Review Species Occupancy ]

[ Open Live Capacity Management ]

[ Review Emergency Closures ]

[ Review Pending Confirmations ]