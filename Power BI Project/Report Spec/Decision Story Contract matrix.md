Step 1 — Extract Decision Model
Primary Decision
	Which centres can safely receive additional animals?

Secondary Decisions
	Which centres require intervention?
	Which centres should be avoided for intake?
	Which centres require data quality review?
	Which regions are approaching capacity limits?

Key Discovery
After reviewing your Power App, the actual intake decision is driven by:



Plain Text
Care Capacity
+
Animals In Care
+
Physical Space
+
Data Trust
Show more lines
NOT merely:



Plain Text
Open Spaces
Show more lines

Step 2 — Build Question Matrix
Business Question	Priority
Which centres currently have available DOG capacity?	High
Which centres currently have available CAT capacity?	High
Which centres are approaching critical utilization?	High
Which centres have no available capacity?	High
Which centres have emergency closures?	High
Which centres have missing kennel assignments?	Medium
Which centres have stale updates?	Medium
Which centres require intervention?	High
Which centres should be prioritized?	High

Step 3 — Build Signal Matrix
Placement Signals
Animals In Care
Care Capacity
Care Capacity %
Open Spaces
Emergency Closure
Show more lines

Physical Capacity Signals
Total Space
Open Space
In Use
Hold
Unavailable
Show more lines

Data Trust Signals

Missing Assignment Count
Confirmation Status
Last Update Time
ShelterBuddy Sync Status
Show more lines

Step 4 — Action Matrix
This is where the dashboard becomes useful.
Care Capacity %
Threshold	Status	Action
<80%	Healthy	Candidate Centre
80%-99%	Monitor	Review Before Routing
100%+	Full	Do Not Intake

Missing Assignments
Threshold	Status	Action
0	Healthy	None
1-3	Warning	Review
>3	Critical	Data Cleanup Required

Capacity Update Age
Threshold	Status	Action
<12 Hours	Current	Use Normally
12-24 Hours	Aging	Validate
>24 Hours	Stale	Contact Centre

Step 5 — Report Story
This is the story I believe Animal Flow actually needs.

Question 1
Can this centre safely take another animal?
This becomes:
Intake Readiness

Question 2
Why can or can't the centre accept animals?
This becomes:
Capacity vs Care Capacity

Question 3
Can I trust the information?
This becomes:
Data Trust

Question 4
Which centres need immediate attention?
This becomes:
Action Queue

Question 5
What should Animal Flow do next?
This becomes:
AI Operational Briefing

Proposed Markdown Wireframe v3
