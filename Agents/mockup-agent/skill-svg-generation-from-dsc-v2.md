# SVG Mockup Generation Agent Skill
## Decision Intelligence SVG from DSC + Wireframe v2.0 + Microsoft Fabric Archetypes

---

# SKILL PURPOSE

Transform a Decision Story Contract (DSC) + Enhanced Markdown Wireframe (v2.0) + Microsoft Fabric report design archetypes into a high-fidelity SVG mockup.

---

# SKILL INPUTS

## Input 1: Decision Story Contract

File Path

```text
INPUT_REPORT_STORY_v1.0.md
```

Required Sections

```text
SECTION 01 — Decision Model

SECTION 02 — Business Question Matrix

SECTION 03 — Business Logic Model

SECTION 04 — Signal Matrix

SECTION 05 — Threshold Matrix

SECTION 06 — Action Matrix

SECTION 07 — Narrative Story (8 stories)

SECTION 10 — Visual Recommendations
```

---

## Input 2: Enhanced Markdown Wireframe v2.0

File Path

```text
OUTPUT 01 — MOCKUP_v2.0.md
```

Required Sections

```text
Visual Hierarchy (Tier 1, Tier 2, Tier 3, Tier 4)

Reading Pattern (ZIP/ZAP flow)

Layout Pattern (Decision Intelligence Command Centre)

Section definitions (8 sections with business questions)

LAYOUT PATTERN section
```

---

## Input 3: Microsoft Fabric Report Skills

Source

```text
https://github.com/microsoft/skills-for-fabric/tree/main/plugins/powerbi-authoring/skills/powerbi-report-design/references/archetypes
```

Archetypes to Apply

```text
narrative-story.md → Story flow structure

operational-monitor.md → KPI cards, real-time tracking, exception highlighting

exception-management → Color coding, priority levels, recommended actions
```

---

# SKILL PROCESS

## Step 1: Extract Decision Logic

### Action

Parse DSC document and extract:

```text
Primary Decision

Secondary Decisions

Thresholds (utilization, age, status)

Action Matrix (condition → recommendation)

Visual Recommendations (chart types per section)

Signal definitions (what data appears where)
```

### Output

Decision logic map for use in Step 5.

---

## Step 2: Extract Wireframe Structure

### Action

Parse v2.0 wireframe and extract:

```text
Visual Hierarchy Tiers (1, 2, 3, 4)

Tier assignments per section

Reading Pattern (ZIP/ZAP)

Section reading order

Section dimensions (approximate)

Layout container hierarchy
```

### Output

Layout grid specification for SVG canvas.

---

## Step 3: Define SVG Canvas

### Action

Create SVG canvas specification:

```text
Width: 1920px
Height: 1400px
ViewBox: 0 0 1920 1400
Margin: 40px padding

Tier 1 Row: y=200, height=300px (critical sections)
Tier 2 Row: y=520, height=260px (support sections)
Tier 3 Row: y=800, height=240px (trust sections)
Tier 4 Row: y=1060, height=300px (action section)
Footer Row: y=1380
```

### Output

Canvas ready for section rendering.

---

## Step 4: Design Color & Typography

### Action

Apply Microsoft Fabric design standards:

#### Color Palette

```text
Primary: #0078d4 (Blue - critical tier, primary data)
Secondary: #2a9d8f (Teal - secondary data)
Success: #107c10 (Green - healthy, ready, candidate)
Warning: #f59e0b (Amber - monitor, caution)
Alert: #d13438 (Red - critical, full, alert)
Background: #f8f9fb (Light blue)
Surface: #ffffff (White)
Border: #cbd5e1 (Light gray)
Text Primary: #0b3d91 (Dark blue)
Text Secondary: #6b7280 (Gray)
```

#### Typography

```text
Font: Segoe UI, Arial, sans-serif
Title: 32px, bold, #0b3d91
Section Title: 20px, bold, #0b3d91
Label: 13px, regular, #6b7280
Value (KPI): 28px, bold, #0078d4
KPI Label: 12px, regular, #475569
Small Text: 12px, regular, #6b7280
Note: 11px, regular, #94a3b8
```

#### Tier Stroke Definition

```text
Tier 1: stroke #0078d4, stroke-width 2 (prominent)
Tier 2: stroke #cbd5e1, stroke-width 1 (standard)
Tier 3: stroke #cbd5e1, stroke-width 1 (recessed)
Tier 4: stroke #cbd5e1, stroke-width 1 (action-colored)
```

### Output

CSS style definitions embedded in SVG.

---

## Step 5: Render SVG Sections

### Action

For each of 8 sections, extract data from DSC and render to SVG coordinates:

#### Section 01: Provincial Capacity Snapshot

**Tier**: 1 (critical)

**Position**: x=40, y=200, width=600, height=300

**Data from DSC Section 04** (Signal Matrix - Provincial Snapshot Signals):

```text
Total DOG Spaces: [value from KPI]
Open DOG Spaces: [value from KPI]
DOG Utilization %: [value with threshold color]
Total CAT Spaces: [value from KPI]
Open CAT Spaces: [value from KPI]
CAT Utilization %: [value with threshold color]
```

**Visual**: 6 KPI cards (3 per row)

**Color**: Apply threshold status
- <80% = #107c10 (green)
- 80-99% = #f59e0b (amber)
- ≥100% = #d13438 (red)

---

#### Section 02: Action Required

**Tier**: 1 (critical)

**Position**: x=680, y=200, width=600, height=300

**Data from DSC Section 06** (Action Matrix conditions):

```text
Emergency Closures: Count from Signal Matrix
Full Centres: Count from Action Matrix
Data Quality Alerts: Count from Signal Matrix
Risk Trend: Calculate change from baseline
```

**Visual**: 3 exception KPI cards + risk trend bar

**Color**: Always #d13438 (alert red) for exceptions

---

#### Section 03: Intake Readiness

**Tier**: 1 (critical)

**Position**: x=1320, y=200, width=560, height=300

**Data from DSC Section 03** (Business Logic Model - Placement Eligibility):

```text
Candidate Centres: Count where capacity available AND emergency inactive AND data current
Monitor Centres: Count where 80-99% utilization
Full Centres: Count where ≥100% utilization
Closed Centres: Count where emergency closure active
```

**Visual**: 2×2 status grid

**Color**: Per status type
- Candidate = #107c10 (green)
- Monitor = #f59e0b (amber)
- Full = #d13438 (red)
- Closed = #d13438 (red)

---

#### Section 04: Placement Decision Board

**Tier**: 2 (support)

**Position**: x=40, y=520, width=940, height=260

**Data from DSC Section 02** (Business Question Matrix):

```text
Centre Name: [from dataset]
Region: [from dataset]
DOG Available: [Open DOG Spaces]
CAT Available: [Open CAT Spaces]
Status: Apply rules from Section 03 (Candidate/Monitor/Full)
```

**Visual**: Table with 2 sample rows

**Color**: Status color (green/amber/red)

---

#### Section 05: Capacity Analysis

**Tier**: 2 (support)

**Position**: x=1000, y=520, width=880, height=260

**Data from DSC Section 05** (Threshold Matrix):

```text
DOG Utilization Bar: [DOG Util %] ÷ 100 × bar width
CAT Utilization Bar: [CAT Util %] ÷ 100 × bar width
Regional Pressure: [Regional Utilization %] per region
```

**Visual**: Horizontal stacked bars + regional ranking

**Color**: #0078d4 (blue for filled portion)

---

#### Section 06: Data Trust

**Tier**: 3 (trust)

**Position**: x=40, y=800, width=560, height=240

**Data from DSC Section 03** (Business Logic Model - Data Trust):

```text
Missing Kennel Assignments: Count
Stale Confirmation: Count
Sync Status: Current/Stale
Overall Confidence Score: Calculate from trust signals
```

**Visual**: 3 metric cards + confidence bar

**Color**: Per metric status (green/amber)

---

#### Section 07: Regional Health

**Tier**: 3 (trust)

**Position**: x=620, y=800, width=560, height=240

**Data from DSC Section 04** (Signal Matrix - Regional Signals):

```text
Regional Utilization %: [per region]
Regional Capacity %: [per region]
Risk Indicator: If any region ≥80% utilization, show warning
```

**Visual**: Regional ranking bars + risk alert

**Color**: #0078d4 (blue for bars), #f59e0b (amber for warning)

---

#### Section 08: Data Quality Review

**Tier**: 3 (trust)

**Position**: x=1200, y=800, width=680, height=240

**Data from DSC Section 02** (Business Question Matrix - Data Quality Questions):

```text
Missing Assignment Centres: Centre names
Stale Confirmation Centres: Centre names + age
Sync Failure Centres: Centre names + error
```

**Visual**: Alert rows (amber/red based on severity)

**Color**: #f59e0b (amber for warning), #d13438 (red for critical)

---

#### Section 09: Operational Briefing

**Tier**: 4 (action)

**Position**: x=40, y=1060, width=1840, height=300

**Data from DSC Section 06** (Action Matrix):

```text
Recommendation 1: Route Animals
  Condition: Healthy Capacity + Available Space
  Action: Send [X] animals to [Centre]
  Priority: IMMEDIATE

Recommendation 2: Monitor Closely
  Condition: 80-99% Utilization
  Action: Review before routing
  Priority: WITHIN 1 HOUR

Recommendation 3: Data Cleanup
  Condition: Data Quality Issues
  Action: Resolve stale/missing data
  Priority: BEFORE NEW INTAKE
```

**Visual**: 3 recommendation cards (priority-colored)

**Color**: 
- Card 1 (Route) = #ecfdf5 background + #10b981 border (green)
- Card 2 (Monitor) = #fef3c7 background + #f59e0b border (amber)
- Card 3 (Cleanup) = #fef2f2 background + #d13438 border (red)

---

## Step 6: Apply Archetype Patterns

### Narrative-Story Pattern

**Applied to**: Tier 1 sections (Snapshot, Action, Readiness)

**Pattern**: Story flow from situation → risk → decision

**Implementation**:
- Provincial Snapshot answers "What is happening?"
- Action Required answers "What requires attention?"
- Intake Readiness answers "Which centres can receive animals?"

---

### Operational-Monitor Pattern

**Applied to**: Tier 2 sections (Placement, Capacity)

**Pattern**: Real-time KPI tracking + decision support detail

**Implementation**:
- Global filters at top
- Status categorization (Candidate/Monitor/Full/Closed)
- Capacity comparison with thresholds
- Priority ranking

---

### Exception-Management Pattern

**Applied to**: Tier 3 & 4 sections (Data Trust, Regional, Quality, Briefing)

**Pattern**: Highlight urgent conditions, recommend actions

**Implementation**:
- Color-coded status (green/amber/red)
- Numeric exception counts
- Trend indicators
- Priority levels (IMMEDIATE, WITHIN 1 HOUR, BEFORE NEW INTAKE)
- Recommended actions per exception

---

## Step 7: Embed CSS and Render

### Action

1. Create SVG `<defs>` section with embedded CSS
2. Render background + header
3. Render filter bar
4. Render sections in order: Tier 1 → 2 → 3 → 4
5. Render footer note explaining reading pattern
6. Validate SVG syntax

### Output

Complete SVG file ready for rendering.

---

# SKILL OUTPUTS

## Output Artifact

File Name

```text
OUTPUT 06 — MOCKUP_ENHANCED_DECISION_v2.0.svg
```

Format

```text
SVG (Scalable Vector Graphics)

Dimensions: 1920 × 1400 px

Embedded CSS: Design standards + color palette + typography

Markup: XML-valid SVG structure

Readiness: Ready for rendering, web deployment, or Power BI embedding
```

---

## Output Validation

The SVG succeeds when:

```text
✅ All 8 DSC stories are present as SVG sections

✅ Visual hierarchy tiers are visually distinct (Tier 1 blue, others gray)

✅ ZIP/ZAP reading pattern is followed (top-left → right → down)

✅ Thresholds from DSC drive color coding (green/amber/red)

✅ All decision logic from Action Matrix appears in Briefing section

✅ Global filters bar is functional in layout

✅ All sections are labeled with business questions from DSC

✅ Typography is consistent and readable at 1920px width

✅ Color palette follows Microsoft Fabric standards

✅ SVG renders without errors in standard SVG viewers
```

---

# SKILL APPLICATION

## When to Use This Skill

```text
✓ Converting approved DSC + v2.0 wireframe to visual prototype
✓ Creating high-fidelity mockup before Power BI development
✓ Presenting mockup to stakeholders for feedback
✓ Using mockup as developer blueprint for report build
✓ Documenting report design for audit trail
```

## When NOT to Use This Skill

```text
✗ DSC is not yet approved
✗ Wireframe v2.0 is not complete
✗ Business logic / thresholds are undefined
✗ Decision story flow has not been validated
✗ Report should be built directly without mockup
```

---

# SKILL DEPENDENCIES

## Required Inputs

```text
1. INPUT_REPORT_STORY_v1.0.md (Decision Story Contract)
2. OUTPUT 01 — MOCKUP_v2.0.md (Enhanced Wireframe)
3. Microsoft Fabric Archetype Descriptions (narrative-story, operational-monitor, exception-management)
```

## Required Standards

```text
1. MOCKUP_STANDARDS_v1.0.md
2. UX_THEME_STANDARD_v1.0.md
3. LAYOUT_PATTERNS_v1.0.md
4. SVG_GUIDELINES_v1.0.md
```

---

# SKILL SUCCESS CRITERIA

All items must be true:

```text
☑ SVG file generated successfully

☑ All 8 sections present and labeled

☑ Visual hierarchy tiers applied

☑ ZIP/ZAP reading pattern evident

☑ Decision logic from DSC visible in layout

☑ Color coding consistent with thresholds

☑ Recommendation cards show priority levels

☑ SVG renders at 1920×1400px

☑ Typography is readable and consistent

☑ All data mappings from DSC are accurate
```

---

# NEXT STEPS AFTER SKILL EXECUTION

## For Mockup Refinement

```text
1. User testing on section hierarchy
2. Accessibility audit (color contrast, readability)
3. Responsive layout variants (tablet, mobile)
4. Interactive prototype (add hover tooltips, drill-down)
5. Animation design (data updates, threshold changes)
```

## For Development

```text
1. Generate TRD (Technical Report Document) from SVG sections
2. Build Power BI semantic model (measures, hierarchies, filters)
3. Create Power BI report pages matching SVG layout
4. Implement interactive filters and drill-down
5. Connect live data sources
```

## For Stakeholder Sign-Off

```text
1. Present SVG mockup to decision owners
2. Validate section placement and reading flow
3. Confirm color coding and status categories
4. Approve recommendation logic
5. Sign approval gate before development begins
```
