**Business Design Layer**
BRD
↓
REPORT_STORY_MATRIX
↓
DSC
↓
MOCKUP
↓
SVG
↓
TRD

**Data Design Layer**
TRD  (Input TRD + DSC + DATA_MODEL_STANDARDS )
↓
DATA_MODEL_MATRIX
↓
SEMANTIC_MODEL_SPEC
↓
MEASURE_CONTRACT

**Build Layer**
SEMANTIC_MODEL_SPEC
+
MEASURE_CONTRACT
↓
Microsoft Semantic Model Authoring Skill
↓
Fabric Semantic Model


Before building the Data Model Agent:
DATA_MODEL_STANDARDS_v1.0

Equivalent to what DSC became for report design.
Structure:
01 Modeling Philosophy

02 Grain-First Design

03 Fact Identification Rules

04 Dimension Identification Rules

05 Measure Design Rules

06 Relationship Rules

07 Kimball Standards

08 Microsoft Fabric Standards

09 SQLBI Standards

10 Performance Standards

11 Naming Standards

12 AI Readiness Standards


Then:

TRD
+
DATA_MODEL_STANDARDS
↓
DATA_MODEL_MATRIX
↓
SEMANTIC_MODEL_SPEC
↓
MEASURE_CONTRACT
And finally:

SEMANTIC_MODEL_SPEC
↓
Microsoft Semantic Model Authoring Skill
↓
Fabric Build


-------
I would define the Semantic Design Agent outputs as:
**OUTPUT 1
DATA_MODEL_MATRIX

OUTPUT 2
SEMANTIC_MODEL_SPEC

OUTPUT 3
MEASURE_CONTRACT**
Not just:
SEMANTIC_MODEL_SPEC
+
MEASURE_CONTRACT

because the DATA_MODEL_MATRIX is the business validation gate.

Why Keep DATA_MODEL_MATRIX?
Think of it like this:
REPORT DESIGN LAYER
REPORT_STORY_MATRIX
    ↓
REPORT_STORY (DSC)
The matrix validates the logic before the detailed design.

SEMANTIC DESIGN LAYER
DATA_MODEL_MATRIX
    ↓
SEMANTIC_MODEL_SPEC
    ↓
MEASURE_CONTRACT
The matrix validates:
Decision

Signals

Measures

Grain

Facts

Dimensions
before creating:
Tables

Columns

Data Types

Relationships

**Recommended Semantic Design Agent Outputs**
Output 1 — DATA_MODEL_MATRIX
Business / Architecture Review
Answers:
What decisions?

What signals?

What measures?

What grain?

What facts?

What dimensions?
Audience:
Business Architect

BI Architect

Data Architect

Output 2 — SEMANTIC_MODEL_SPEC
Technical Model Design
Answers:
What tables?

What columns?

What data types?

What relationships?

What cardinality?

What filter direction?
Audience:
Data Architect

Power BI Developer

Fabric Developer

Output 3 — MEASURE_CONTRACT
Measure Governance
Answers:
What measures?

What business definitions?

What logic?

What thresholds?

What decisions?
Audience:
BI Architect

Power BI Developer

Report Developer

Future Semantic Build Agent
Then the next future agent becomes:
SEMANTIC_MODEL_SPEC
+
MEASURE_CONTRACT
↓
Semantic Build Agent
↓
Fabric Semantic Model
because at build time the DATA_MODEL_MATRIX has already served its purpose.

Final Architecture
Semantic Design Agent

INPUT
-----
TRD
DSC
DATA_MODEL_STANDARDS

OUTPUT 1
---------
DATA_MODEL_MATRIX

OUTPUT 2
---------
SEMANTIC_MODEL_SPEC

OUTPUT 3
---------
MEASURE_CONTRACT

So for the Semantic Design Agent itself, keep all three outputs. For the future Build Agent, the primary handoff artifacts will be:


SEMANTIC_MODEL_SPEC
+
MEASURE_CONTRACT


