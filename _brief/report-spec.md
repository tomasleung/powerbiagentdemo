# Report Spec: Live Capacity Analysis

## Report Identity
- **Report name:** Live Capacity Analysis
- **Semantic model:** Live Capacity Analysis (new, to be created)
- **Audience:** Executive leadership (CEO, VP, GM)
- **Primary purpose:** Track Fabric capacity performance and utilization metrics
- **Delivery target:** Local PBIP (no publishing)

## User Decisions and Constraints
- **Scope:** 2-3 pages (executive overview + capacity details)
- **Page count:** 2 pages (landing + detail)
- **Interactivity:** Global date slicer, cross-visual filtering
- **Design direction:** Modern, clean, high-contrast executive dashboard
- **Publishing:** Local only
- **Tooling:** Power BI Desktop, PBIP, TMDL
- **Model edit permissions:** Full (creating new semantic model)
- **Accessibility:** WCAG AA minimum contrast; alt text on all visuals
- **Data caveats:** Capacity metrics require live connection or regular refresh

## Narrative
- **Core story:** Fabric capacity utilization is healthy and on track, with early warning signals for peak periods
- **Audience promise:** Know capacity health at a glance; drill for operational detail
- **Key questions answered:**
  - What is our current total capacity usage?
  - Are we trending up or down week-over-week?
  - Which workspaces consume the most capacity?
  - Are there any bottlenecks or at-risk periods?

## Design Identity (from powerbi-report-design)
- **Tone:** Corporate Professional — modern, data-forward, high-contrast surface with semantic color coding
- **Signature:** KPI cards with trend sparklines + supporting context chart
- **Color semantics:** Blue (#107C10) for healthy/primary, Red (#DC2626) for alerts, Grey (#C0C0C0) for neutral
- **Typography:** Segoe UI, display 24–32pt for titles, body 11pt for details
- **Surface:** Clean white with subtle section dividers

## Page Plan

### Page 1: Capacity Health (Executive Summary)
- **Archetype:** Executive Summary
- **Layout variant:** A (Hero-Right)
- **Variant rationale:** 4 key KPIs + hero trend chart matches executive ≤10s scan target
- **Purpose:** Instant status comprehension for leadership
- **Core visuals:** 4 KPI cards (Total Capacity, Usage %, Peak Period, Forecast) + trend line chart
- **Key measures:** Total Capacity, Usage %, Peak Period Usage, Capacity Forecast
- **Slicers:** Global date range (default: last 30 days)

### Page 2: Capacity Details (Analytical Canvas)
- **Archetype:** Analytical Canvas
- **Layout variant:** A (Filter-Rail)
- **Variant rationale:** Multiple slicers justify F-pattern for exploration
- **Purpose:** Drill-down into workspace allocation and usage patterns
- **Core visuals:** Filter rail + horizontal bar (allocation) + stacked area (trend) + heatmap (peak hours) + detail table
- **Key dimensions:** Workspace, Capacity Pool, Hour of Day, Day of Week
- **Slicers:** Workspace dropdown, Capacity Pool, Time Grain toggle (hourly/daily)

## Canonical Design Contract

```yaml
Design Brief:
  generated_by: powerbi-report-design
  contract_version: 1
  mode: greenfield
  
  design_identity:
    tone: "Corporate Professional"
    signature: "KPI cards with trend sparklines + supporting context chart"
  
  pages:
    - name: "Capacity Health"
      role: landing
      archetype: Executive Summary
      layout_variant: A
      variant_rationale: "4 KPIs + hero trend chart; executive scan-time ≤10s"
      
      layout_contract:
        canvas: { width: 1920, height: 1080, margin: 32, gutter: 24, snap: 8 }
        grid:
          columns: 12
          rows: 12
          regions:
            header: [1, 1, 9, 2]
            filters: [9, 1, 13, 2]
            kpi_section: [1, 3, 7, 8]
            hero_chart: [8, 3, 13, 8]
            footer: [1, 9, 13, 13]
        
        placements:
          - id: page_title
            region: header
            kind: textbox
            text: "Fabric Capacity Health"
            purpose: "page headline"
          
          - id: date_slicer
            region: filters
            kind: slicer
            purpose: "global date range filter"
            field_bindings: [{ table: Date, column: Date }]
          
          - id: kpi_total_capacity
            region: kpi_section
            kind: cardVisual
            purpose: "total capacity absolute + MoM delta + sparkline"
          
          - id: kpi_usage_pct
            region: kpi_section
            kind: cardVisual
            purpose: "usage percentage + trend"
          
          - id: kpi_peak_period
            region: kpi_section
            kind: cardVisual
            purpose: "peak period usage + alert indicator"
          
          - id: kpi_forecast
            region: kpi_section
            kind: cardVisual
            purpose: "30-day forecast"
          
          - id: hero_capacity_chart
            region: hero_chart
            kind: lineChart
            purpose: "capacity trend 30-day rolling"
        
        space_audit:
          content_cell_count: 140
          placed_cell_count: 135
          empty_cell_pct: 3.6
          unplaced_regions: []
          balance_rationale: "Hero chart 35% (right); KPI cards 28% (left); footer 10% reserved; whitespace 3.6%"
    
    - name: "Capacity Details"
      role: detail
      archetype: Analytical Canvas
      layout_variant: A
      variant_rationale: "Multiple slicers (workspace, pool, time grain) justify filter rail F-pattern"
      
      layout_contract:
        canvas: { width: 1920, height: 1080, margin: 32, gutter: 24, snap: 8 }
        grid:
          columns: 12
          rows: 12
          regions:
            header: [1, 1, 12, 2]
            filter_rail: [1, 3, 3, 11]
            hero_visual: [4, 3, 12, 7]
            supporting_visual_1: [4, 8, 8, 11]
            supporting_visual_2: [9, 8, 12, 11]
            detail_matrix: [1, 12, 12, 13]
        
        placements:
          - id: page_title
            region: header
            kind: textbox
            text: "Capacity Details by Workspace"
            purpose: "page headline"
          
          - id: slicer_workspace
            region: filter_rail
            kind: slicer
            purpose: "workspace selection (searchable)"
          
          - id: slicer_pool
            region: filter_rail
            kind: slicer
            purpose: "capacity pool selection"
          
          - id: slicer_time_grain
            region: filter_rail
            kind: slicer
            purpose: "time grain toggle (hourly/daily)"
          
          - id: hero_allocation
            region: hero_visual
            kind: horizontalBarChart
            purpose: "capacity allocation by workspace, sorted descending"
          
          - id: trend_area
            region: supporting_visual_1
            kind: areaChart
            purpose: "usage trend for top 5 workspaces (stacked)"
          
          - id: heatmap_peaks
            region: supporting_visual_2
            kind: heatmap
            purpose: "peak hours by day of week"
          
          - id: detail_table
            region: detail_matrix
            kind: tableEx
            purpose: "workspace detail: allocated, used, %, peak hour, updated"
        
        space_audit:
          content_cell_count: 120
          placed_cell_count: 118
          empty_cell_pct: 1.7
          unplaced_regions: []
          balance_rationale: "Filter rail 17% left; hero 32%; supporting 2x20%; detail 100% bottom; minimal whitespace for analyst density"

  color_map:
    - measure: Total Capacity
      color_match: "#107C10"
    - measure: Usage %
      gradient: ["#FECACA", "#F59E0B", "#DC2626"]
    - measure: Peak Usage
      color_match: "#DC2626"
    - measure: Forecast
      color_match: "#D9D9D9"

  theme:
    name: "Azure Corporate"
    base_palette: ["#107C10", "#DC2626", "#C0C0C0", "#1F1F1F", "#F5F5F5"]
    surface_color: "#FFFFFF"
    fonts: { display: "Segoe UI 28pt bold", body: "Segoe UI 11pt regular" }

  accessibility:
    wcag_level: AA
    contrast_minimum_ratio: 4.5
    alt_text_all_visuals: true
    color_blind_safe: true
```

## Implementation Notes
- **Model changes:** Create workspace/capacity/date tables; define core measures
- **PBIR authoring:** Generate using powerbi-report-authoring; apply Azure Corporate theme; validate all placements
- **Desktop validation:** Open in Power BI Desktop, verify KPI population, verify slicer response, screenshot both pages
- **Publishing:** Stay local for V1
- **Risks:** Forecast measure deferred if historical data unavailable; heatmap performance if >100K rows

---

## Approval Gate

**✅ This report specification is locked and ready for implementation.**

**Approve this report spec so I can start building?**
