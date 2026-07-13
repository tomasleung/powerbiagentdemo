# SKILL: Decision Intelligence SVG Mockup Generation
## Animal Flow — Live Capacity Reporting

---

# Document Metadata

Skill Name

Decision Intelligence SVG Mockup Generation

Version

1.0

Purpose

Guide for converting a Decision Story Contract (DSC) and enhanced Markdown Wireframe (v2.0) into a high-fidelity SVG mockup using Microsoft Fabric report design archetypes and visual hierarchy principles.

Input Artifacts

```text
INPUT_REPORT_STORY_v1.0.md (Decision Story Contract)

OUTPUT 01 — MOCKUP_v2.0.md (Enhanced Markdown Wireframe)

Microsoft Fabric Report Design Archetypes (narrative-story, operational-monitor)
```

Output Artifact

```text
OUTPUT 06 — MOCKUP_ENHANCED_DECISION_v2.0.svg

(High-fidelity operational command centre SVG mockup)
```

Audience

Report Design Agents, SVG Developers, Mockup Designers

---

# SECTION 01 — INPUT ANALYSIS

## Input 1: Decision Story Contract (DSC)

### Purpose

The DSC defines the **decision story flow** and **business logic** that guide all visual design.

### Key Components Used

```text
Primary Decision: Which centres have sufficient capacity?

Narrative Story (8 Stories): Sequential decision journey from situation → action

Thresholds: Utilization <80% (healthy), 80-99% (monitor), ≥100% (full)

Action Matrix: Condition → Recommended Action mappings

Visual Recommendations: Chart type per section (KPI cards, tables, comparisons)
```

### Mapping to SVG

| DSC Section | SVG Section | Visual Type |
|------------|------------|------------|
| Story 0 | Provincial Capacity Snapshot | KPI Cards (6 metrics) |
| Story 1 | Action Required | Exception KPI Cards (3 alerts) |
| Story 2 | Intake Readiness | Status Cards (2×2 grid) |
| Story 3 | Placement Decision Board | Priority Table |
| Story 4 | Capacity Analysis | Comparison Bars (DOG/CAT) |
| Story 5 | Data Trust | Metric Cards + Confidence Score |
| Story 6 | Regional Health | Regional Ranking Bars |
| Story 7 | Operational Briefing | Recommendation Cards (priority colored) |

---

## Input 2: Enhanced Markdown Wireframe (v2.0)

### Purpose

The wireframe v2.0 adds **visual hierarchy structure**, **reading patterns**, and **design standards** that weren't present in v1.0.

### Key Components Used

```text
Visual Hierarchy Tiers:
  Tier 1 (Critical): Provincial Snapshot, Action Required, Intake Readiness
  Tier 2 (Support): Placement Board, Capacity Analysis
  Tier 3 (Trust): Data Trust, Regional Health
  Tier 4 (Action): Operational Briefing

Reading Pattern: ZIP/ZAP flow (top-left → right → down)

Layout Pattern: Decision Intelligence Command Centre

Design Standards: Section structure, container spacing, container hierarchy
```

### Mapping to SVG

| Wireframe Element | SVG Implementation |
|------------|------------|
| Tier 1 sections | Blue border stroke (critical emphasis) |
| Tier 2 sections | Standard gray border |
| Tier 3 sections | Light gray background |
| Tier 4 sections | Recommendation cards with priority colors |
| ZIP/ZAP flow | Top row (Snapshot, Action, Readiness) → 2nd row (Board, Analysis) → 3rd row (Trust, Health) → Bottom (Briefing) |
| Global filters | Filter bar above main content |

---

# SECTION 02 — MICROSOFT FABRIC REPORT SKILLS

## Report Design Archetypes

### Archetype 1: Narrative-Story

**Pattern**: Story-led entry point with context → risk → insight → action.

**Used For**: Landing page structure, main narrative anchor.

**Principles Applied**:
- Single anchor story question ("What is happening?")
- Guided decision journey through 8 stories
- Side annotation panel for context
- Supporting metrics at bottom

**SVG Sections**: Provincial Snapshot, Action Required, Intake Readiness form the narrative anchor.

---

### Archetype 2: Operational-Monitor

**Pattern**: Command centre dashboard with real-time monitoring, exception management, KPI tracking.

**Used For**: Full operational awareness and drill-down detail.

**Principles Applied**:
- Global filters at top for focus
- Real-time KPI cards for context
- Exception highlighting
- Status categorization (ready, monitor, full, closed)
- Capacity tracking with thresholds
- Data quality validation

**SVG Sections**: All 8 sections implement operational-monitor patterns (KPI cards, status tracking, exception management).

---

### Archetype 3: Exception-Management

**Pattern**: Highlight urgent conditions, data quality issues, operational constraints.

**Used For**: Action Required section, Data Quality Review, Operational Briefing.

**Principles Applied**:
- Color-coded status (green=ready, amber=warning, red=alert)
- Numeric exception counts
- Trend indicators (↑ risk increase)
- Recommended actions per exception
- Priority levels (IMMEDIATE, WITHIN 1 HOUR, BEFORE NEW INTAKE)

**SVG Sections**: Action Required, Data Trust, Data Quality Review, Operational Briefing.

---

## Design Principles Applied

### 1. Visual Hierarchy

**Principle**: Most critical information first; supporting details follow.

**Implementation**:
```text
Tier 1 (Blue stroke): Provincial context, urgent issues, intake status
Tier 2 (Gray stroke): Decision support (placement board, capacity analysis)
Tier 3 (Light background): Trust validation (data quality, regional monitoring)
Tier 4 (Action cards): Recommendations with priority colors
```

### 2. Reading Pattern (ZIP/ZAP)

**Principle**: F-pattern / natural eye flow from top-left → right → down.

**Implementation**:
```text
Row 1 (1260px): Header
Row 2 (200-500px): Global Filters
Row 3 (200-500px): Tier 1 sections (3 boxes: Snapshot, Action, Readiness)
Row 4 (520-780px): Tier 2 sections (2 boxes: Placement Board, Capacity Analysis)
Row 5 (800-1040px): Tier 3 sections (3 boxes: Data Trust, Regional, Quality Review)
Row 6 (1060-1360px): Tier 4 section (Briefing with 3 recommendation cards)
```

### 3. Color Coding

**Principle**: Consistent status indicators across all sections.

**Implementation**:
```text
#107c10 (Green): Healthy, Ready, Candidate
#f59e0b (Amber): Warning, Monitor, Caution
#d13438 (Red): Alert, Full, Critical
#0078d4 (Blue): Primary data, Critical tier
#2a9d8f (Teal): Secondary data, Alternative emphasis
#e2e8f0 (Light Gray): Background, Comparison baseline
```

### 4. Information Density

**Principle**: Balance density to avoid cognitive overload.

**Implementation**:
- Tier 1 sections: Large KPI cards with descriptive labels
- Tier 2 sections: Tables and comparison charts with context
- Tier 3 sections: Metric rows and risk indicators
- Tier 4 section: Priority-colored recommendation cards with action detail

---

# SECTION 03 — GENERATION METHODOLOGY

## Step 1: Extract Decision Logic from DSC

### Action

Read INPUT_REPORT_STORY_v1.0.md sections:
- Decision Model (primary & secondary decisions)
- Business Logic Model (placement eligibility criteria)
- Threshold Matrix (utilization thresholds)
- Narrative Story (8 story questions)
- Visual Recommendations (chart types per section)

### Output

Mapping of 8 business stories → 8 SVG sections with decision context.

---

## Step 2: Extract Wireframe Structure from v2.0

### Action

Read OUTPUT 01 — MOCKUP_v2.0.md sections:
- Visual Hierarchy (4 tiers)
- Reading Pattern (ZIP/ZAP flow)
- Layout Pattern (Decision Intelligence Command Centre)
- Section definitions (business question, audience, decision supported, visual containers)

### Output

Grid layout definition: header → filters → Tier 1 (3 boxes) → Tier 2 (2 boxes) → Tier 3 (3 boxes) → Tier 4 (1 box).

---

## Step 3: Apply Microsoft Fabric Archetypes

### Action

Reference Microsoft Fabric report design skills:
- **narrative-story.md**: Structure for story-led flow, context panels, annotation
- **operational-monitor.md**: KPI card patterns, real-time tracking, exception highlighting, status categories
- **exception-management**: Color coding, priority levels, recommended actions

### Output

Design patterns applied to SVG:
- Tier 1 with story flow (narrative anchor)
- Operational KPI cards throughout
- Exception highlighting (red, amber, green)
- Action-oriented briefing section with priority levels

---

## Step 4: Design SVG Structure

### Canvas Setup

```text
Width: 1920px (standard 16:9 widescreen)
Height: 1400px (full-height single-page view)
ViewBox: 0 0 1920 1400
Margin: 40px padding on all sides
```

### Color Palette (from design standards)

```text
Primary: #0078d4 (Microsoft Blue)
Secondary: #2a9d8f (Teal)
Alert: #d13438 (Red)
Warning: #f59e0b (Amber)
Success: #107c10 (Green)
Background: #f8f9fb (Light Blue)
Surface: #ffffff (White)
Border: #cbd5e1 (Light Gray)
Text Primary: #0b3d91 (Dark Blue)
Text Secondary: #6b7280 (Gray)
```

### Typography

```text
Font Family: Segoe UI, Arial, sans-serif
Title: 32px, bold, #0b3d91
Section Title: 20px, bold, #0b3d91
Label: 13px, regular, #6b7280
Value (KPI): 28px, bold, #0078d4
KPI Label: 12px, regular, #475569
Small Text: 12px, regular, #6b7280
Note: 11px, regular, #94a3b8
```

---

## Step 5: Render SVG Sections

### Section Rendering Order (ZIP/ZAP)

```text
1. Background + Header
2. Global Filter Bar
3. Tier 1 (top row):
   - Provincial Capacity Snapshot (left)
   - Action Required (center)
   - Intake Readiness (right)
4. Tier 2 (second row):
   - Placement Decision Board (left, wide)
   - Capacity Analysis (right, wide)
5. Tier 3 (third row):
   - Data Trust (left)
   - Regional Health (center)
   - Data Quality Review (right)
6. Tier 4 (bottom row):
   - Operational Briefing (full width, 3 recommendation cards)
7. Footer note (reading pattern + hierarchy explanation)
```

### Per-Section Data

**Provincial Capacity Snapshot**
- 6 KPI cards: Total DOG Spaces (1,240), Open DOG (320), DOG Util% (74%), Total CAT (840), Open CAT (180), CAT Util% (79%)
- From DSC: Section 04 (Signal Matrix - Provincial Snapshot Signals)

**Action Required**
- 3 exception cards: Emergency Closures (3), Over-Capacity (8), Data Quality Alerts (5)
- Risk trend: ↑ 15% from yesterday
- From DSC: Section 02 (Business Question Matrix - Capacity Questions) + Section 06 (Action Matrix)

**Intake Readiness**
- 2×2 status grid: Candidate (12, green), Monitor (6, amber), Full (8, red), Closed (3, red)
- From DSC: Section 03 (Business Logic Model - Placement Eligibility)

**Placement Decision Board**
- Priority table: Centre | Region | DOG Available | CAT Available | Status
- Sample rows: Victoria Centre (24 DOG, 18 CAT, Ready ✓), Surrey Centre (8 DOG, 5 CAT, Review ⚠)
- From DSC: Section 10 (Visual Recommendations - Priority Table)

**Capacity Analysis**
- DOG bar: 74% utilization (296/400px filled)
- CAT bar: 79% utilization (316/400px filled)
- Regional bars: Lower Mainland 82%, Vancouver Island 68%
- From DSC: Section 05 (Threshold Matrix - Utilization thresholds)

**Data Trust**
- 3 metric cards: Missing (0, green), Stale (5, amber), Sync (✓, green)
- Overall confidence bar: 75%
- From DSC: Section 03 (Business Logic Model - Data Trust)

**Regional Health**
- 2 regional bars: Lower Mainland 82%, Vancouver Island 68%
- Risk indicator: "Lower Mainland approaching critical levels" (amber alert)
- From DSC: Section 04 (Signal Matrix - Regional Signals)

**Data Quality Review**
- 3 quality alerts: Centre K (stale confirmation), Centre M (missing kennel), Centre Q (sync failure)
- Priority: Before new intake
- From DSC: Section 02 (Business Question Matrix - Data Quality Questions)

**Operational Briefing**
- 3 recommendation cards (priority-colored):
  1. **Route Animals** (green): Send 4 dogs to Victoria Centre | Priority: IMMEDIATE
  2. **Monitor Closely** (amber): Review Surrey before routing | Priority: WITHIN 1 HOUR
  3. **Data Cleanup** (red): Resolve stale data for Centres K, M, Q | Priority: BEFORE NEW INTAKE
- From DSC: Section 06 (Action Matrix - Condition → Recommended Action)

---

## Step 6: Apply Visual Styling

### Tier Distinction

```text
Tier 1: .tier1-bg class
  stroke: #0078d4
  stroke-width: 2
  fill: #ffffff
  (highest visual prominence)

Tier 2: .tier2-bg class
  stroke: #cbd5e1
  stroke-width: 1
  fill: #ffffff
  (standard prominence)

Tier 3: .tier3-bg class
  stroke: #cbd5e1
  stroke-width: 1
  fill: #fafbfc
  (recessed, light background)

Tier 4: .tier4-bg class
  stroke: #cbd5e1
  stroke-width: 1
  fill: #ffffff
  (action-focused, color-coded by priority)
```

### Exception Highlighting

```text
Green (#107c10): Ready status, candidate centres, positive data
Amber (#f59e0b): Warning status, monitor centres, caution
Red (#d13438): Alert status, full/closed centres, critical action
```

---

# SECTION 04 — OUTPUT ARTIFACT

## File

```text
OUTPUT 06 — MOCKUP_ENHANCED_DECISION_v2.0.svg
```

## Specifications

```text
Format: SVG (Scalable Vector Graphics)
Width: 1920px
Height: 1400px
ViewBox: 0 0 1920 1400
Embedded CSS: Design standards (colors, fonts, sizing)
```

## Content Map

```text
Header (60px): Title + decision statement
Filters (60px): Global filter bar
Tier 1 (300px): Snapshot, Action, Readiness
Tier 2 (260px): Placement Board, Capacity Analysis
Tier 3 (240px): Data Trust, Regional, Quality Review
Tier 4 (300px): Operational Briefing (3 recommendation cards)
Footer (20px): Reading pattern note
Total: 1400px
```

## Conversion Paths

```text
SVG → PNG: Use design tool (Figma, Adobe XD) for rasterization
SVG → Power BI Visual: Embed in custom Power BI visual
SVG → HTML Canvas: Convert for web dashboard
SVG → PDF: Export for reporting/sharing
```

---

# SECTION 05 — SKILL VALIDATION

The skill succeeds when:

```text
✅ DSC decision logic is fully represented in SVG layout

✅ v2.0 wireframe structure (4 tiers, ZIP/ZAP flow) is followed

✅ Microsoft Fabric archetypes are applied (narrative, operational, exception management)

✅ Visual hierarchy guides user from critical → support → trust → action

✅ Color coding is consistent (green=ready, amber=monitor, red=alert)

✅ All 8 business stories are present as SVG sections

✅ Thresholds and action logic from DSC drive visual presentation

✅ SVG renders at 1920×1400px with readable typography and spacing

✅ Stakeholders can validate information placement and reading flow
```

---

# SECTION 06 — NEXT STEPS

## For SVG Refinement

```text
1. Replace sample data with live/dynamic data sources
2. Add hover tooltips for additional detail
3. Implement drill-down interactions (click section → detailed view)
4. Animate data updates (threshold approaches, status changes)
5. Add print stylesheet for report exports
```

## For Power BI Integration

```text
1. Generate separate PBIX development specification (TRD)
2. Map SVG sections to Power BI report pages
3. Create data model measures for thresholds and status logic
4. Design filter interactions tied to global filter bar
5. Build Power Query transformations for data shapes
```

## For Mockup Evolution

```text
1. Conduct user testing on reading pattern and section hierarchy
2. Refine color palette based on accessibility testing
3. Adjust spacing/sizing based on typical monitor resolutions
4. Add variant layouts for tablet/mobile views
5. Create style guide for future mockup iterations
```

---

# SKILL SUMMARY

**Input**: DSC + v2.0 Wireframe + Microsoft Fabric Archetypes

**Process**: Decision logic extraction → Wireframe structure analysis → Archetype pattern application → SVG design + rendering

**Output**: Decision Intelligence SVG Mockup (1920×1400px, fully styled, ready for development)

**Reusability**: This skill can be applied to any report design requiring decision-driven layout, visual hierarchy tiers, and Microsoft Fabric archetype integration.
