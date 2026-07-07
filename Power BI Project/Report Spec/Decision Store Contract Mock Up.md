I would propose this Decision-First Mockup v1.2 based on the updated DSC.

┌──────────────────────────────────────────────────────────────────────────────┐
│                  ANIMAL FLOW — CAPACITY INTELLIGENCE                        │
│          Provincial Intake Readiness & Operational Monitoring               │
└──────────────────────────────────────────────────────────────────────────────┘


SECTION 00 — OPERATIONAL SNAPSHOT
──────────────────────────────────────────────────────────────────────────────

┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ Centres     │ │ Animals     │ │ Care Cap.   │ │ Open Space  │
│     32      │ │   1,875     │ │   2,140     │ │    390      │
└─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘

┌─────────────┐ ┌─────────────┐
│ Cat Space   │ │ Dog Space   │
│    810      │ │    430      │
└─────────────┘ └─────────────┘


Purpose:
Provide context before decisions.



SECTION 01 — ACTION REQUIRED
──────────────────────────────────────────────────────────────────────────────

┌────────────────┐ ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
│ 🔴 At Capacity │ │ ⚠ Data Issues  │ │ 🟡 Not Confirm │ │ 🚨 Closures    │
│       4        │ │      18        │ │       3        │ │       2        │
└────────────────┘ └────────────────┘ └────────────────┘ └────────────────┘


Purpose:
Immediate operational attention.



SECTION 02 — INTAKE READINESS
──────────────────────────────────────────────────────────────────────────────

┌────────────────┐ ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
│ Available      │ │ Monitor        │ │ Full           │ │ Closed         │
│      18        │ │      7         │ │      4         │ │      2         │
└────────────────┘ └────────────────┘ └────────────────┘ └────────────────┘


Purpose:
Can we intake more animals?



SECTION 03 — PLACEMENT DECISION BOARD
──────────────────────────────────────────────────────────────────────────────

┌──────────────┬─────────┬──────────┬──────────┬──────────┬────────────────┐
│ Centre       │ Animals │ Capacity │ Remain   │ Open Spc │ Recommendation │
├──────────────┼─────────┼──────────┼──────────┼──────────┼────────────────┤
│ Kelowna      │ 15      │ 25       │ 10       │ 8        │ ✅ Candidate    │
│ Nanaimo      │ 20      │ 25       │ 5        │ 6        │ 🟡 Monitor      │
│ Victoria     │ 25      │ 25       │ 0        │ 2        │ 🔴 Do Not Intake│
│ Williams Lk  │ 25      │ 25       │ 0        │ 6        │ ⚠ Review Data   │
└──────────────┴─────────┴──────────┴──────────┴──────────┴────────────────┘


Business Rule:

Remaining Capacity
=
Care Capacity
-
Animals In Care


Purpose:
Which centres should Animal Flow use?



SECTION 04 — CAPACITY HEALTH
──────────────────────────────────────────────────────────────────────────────

┌─────────────────────────────────────┐
│ CARE CAPACITY                       │
├─────────────────────────────────────┤
│ Animals In Care         1,875       │
│ Care Capacity           2,140       │
│ Remaining Capacity        265       │
│ Capacity Used             88%       │
└─────────────────────────────────────┘


┌─────────────────────────────────────┐
│ PHYSICAL SPACE                      │
├─────────────────────────────────────┤
│ Total Spaces            1,240       │
│ Open Spaces               390       │
│ In Use                    690       │
│ Hold                       90       │
│ Unavailable                70       │
└─────────────────────────────────────┘


Purpose:
Why are centres available or unavailable?



SECTION 05 — DATA TRUST
──────────────────────────────────────────────────────────────────────────────

┌──────────────────────┐ ┌──────────────────────┐
│ Missing Assignment   │ │ Accuracy %           │
│         18           │ │        96%           │
└──────────────────────┘ └──────────────────────┘

┌──────────────────────┐ ┌──────────────────────┐
│ Pending Confirmation │ │ Stale Updates        │
│          3           │ │         2            │
└──────────────────────┘ └──────────────────────┘


Purpose:
Can I trust the data?



SECTION 06 — REGIONAL HEALTH
──────────────────────────────────────────────────────────────────────────────

Interior         █████████░░   89%   🔴 High

Island           ████████░░░   78%   🟡 Monitor

Lower Mainland   ███████░░░░   72%   🟢 Healthy

North            ██████░░░░░   61%   🟢 Healthy


Purpose:
Where is capacity pressure building?



SECTION 07 — AI OPERATIONAL BRIEFING
──────────────────────────────────────────────────────────────────────────────

TODAY'S PRIORITIES

1. Victoria
   Care Capacity reached.
   Recommendation:
   Do not intake additional animals.

2. Williams Lake
   Data quality concerns detected.
   Recommendation:
   Review ShelterBuddy assignments.

3. Kelowna
   Highest remaining capacity.
   Recommendation:
   Candidate for overflow intake.


Purpose:
What should Animal Flow do next?



SECTION 08 — QUICK ACTIONS
──────────────────────────────────────────────────────────────────────────────

[ Review Critical Centres ]

[ Review Data Quality ]

[ Open Live Capacity Management ]

[ Review Closures ]

[ Review Pending Confirmations ]

One thing I am considering
We may eventually move Placement Decision Board above Intake Readiness because it directly answers the primary decision:

Which centre can receive animals?

So the future flow could become:
Plain TextOperational Snapshot↓Action Required↓Placement Decision Board↓Intake Readiness↓Capacity Health↓Data Trust↓Regional Health↓AI BriefingShow more lines
Personally, I like that version better because it puts the primary decision immediately after the alerts. However, let's confirm this layout first before generating the polished SVG.