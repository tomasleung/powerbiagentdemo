# 04_SVG_TEMPLATE_v1.0
## Decision-Driven BI SVG Template

---

# Purpose

Provide the base SVG structure used by the Mockup Agent.

This template defines:

```text
Page Skeleton

Section Containers

Header Area

Filter Area

Layout Zones

Container Zones
```

This template does not define:

```text
Business Logic

KPIs

Colors

Fonts

Story Content
```

These must come from:

```text
REPORT_STORY

UX_THEME_STANDARD

LAYOUT_PATTERNS
```

---

# SVG STRUCTURE

```text
SVG Canvas

↓

Header Area

↓

Filter Area

↓

Section Containers

↓

Footer Area
```

---

# SVG LAYOUT SKELETON

```svg
<svg
    width="[CANVAS_WIDTH]"
    height="[CANVAS_HEIGHT]"
    viewBox="0 0 [CANVAS_WIDTH] [CANVAS_HEIGHT]"
    xmlns="http://www.w3.org/2000/svg">

    <!-- Page Background -->

    <rect
        width="[CANVAS_WIDTH]"
        height="[CANVAS_HEIGHT]"
        class="background"/>

    <!-- ================================================= -->
    <!-- PAGE HEADER                                      -->
    <!-- ================================================= -->

    <g id="header">

        <text class="header">
            [REPORT_TITLE]
        </text>

        <text class="subheader">
            [REPORT_SUBTITLE]
        </text>

    </g>

    <!-- ================================================= -->
    <!-- FILTER AREA                                      -->
    <!-- ================================================= -->

    <g id="filters">

        [FILTER_CONTAINERS]

    </g>

    <!-- ================================================= -->
    <!-- SECTION 01                                       -->
    <!-- ================================================= -->

    <g id="section_01">

        [SECTION_01_HEADER]

        [SECTION_01_CONTAINERS]

    </g>

    <!-- ================================================= -->
    <!-- SECTION 02                                       -->
    <!-- ================================================= -->

    <g id="section_02">

        [SECTION_02_HEADER]

        [SECTION_02_CONTAINERS]

    </g>

    <!-- ================================================= -->
    <!-- SECTION 03                                       -->
    <!-- ================================================= -->

    <g id="section_03">

        [SECTION_03_HEADER]

        [SECTION_03_CONTAINERS]

    </g>

    <!-- ================================================= -->
    <!-- SECTION N                                        -->
    <!-- ================================================= -->

    <g id="section_n">

        [SECTION_HEADER]

        [SECTION_CONTAINERS]

    </g>

</svg>
```

---

# REQUIRED PAGE ZONES

## Zone 01

Header

Purpose

```text
Report Identity
```

---

## Zone 02

Filters

Purpose

```text
User Context Selection
```

---

## Zone 03

Story Sections

Purpose

```text
Decision Support
```

---

## Zone 04

Recommendations

Purpose

```text
Operational Actions
```

---

# REQUIRED SVG COMPONENTS

## Header Component

```text
Page Title

Page Subtitle
```

---

## Filter Component

```text
Filter Pill

Dropdown

Selection Box
```

---

## Section Component

```text
Section Header

Section Boundary

Container Region
```

---

## Container Component

```text
Card Container

Table Container

Chart Container

Narrative Container
```

---

# SECTION TEMPLATE

Every story section must render:

```svg
<g id="[SECTION_NAME]">

    <text class="section">
        [SECTION_TITLE]
    </text>

    <rect class="sectionContainer"/>

    [VISUAL_CONTAINERS]

</g>
```

---

# CARD TEMPLATE

Every card container should render:

```svg
<rect class="card"/>

<text class="cardTitle">
    [CARD_TITLE]
</text>

<text class="cardValue">
    [CARD_VALUE]
</text>
```

---

# TABLE TEMPLATE

Table areas should render:

```svg
<rect class="card"/>

<text class="cardTitle">
    [TABLE_NAME]
</text>

<text class="label">
    TABLE PLACEHOLDER
</text>
```

---

# CHART TEMPLATE

Chart areas should render:

```svg
<rect class="card"/>

<text class="cardTitle">
    [CHART_NAME]
</text>

<text class="label">
    CHART PLACEHOLDER
</text>
```

---

# NARRATIVE TEMPLATE

Recommendation areas should render:

```svg
<rect class="card"/>

<text class="cardTitle">
    [RECOMMENDATION_TITLE]
</text>

<text class="label">
    [RECOMMENDATION_TEXT]
</text>
```

---

# STORY FLOW REQUIREMENT

Sections must render in the exact sequence defined by:

```text
REPORT_STORY

Layout Blueprint

Layout Pattern
```

---

# NOT ALLOWED

SVG template must never introduce:

```text
New Sections

New KPIs

New Measures

New Questions

New Story Steps

New Decisions
```

---

# SVG TEMPLATE SUCCESS STATEMENT

The SVG template succeeds when:

```text
Every Story Section

renders consistently

Every Page

uses the same structure

Every Mockup

produces predictable SVG output
```

The SVG template becomes the reusable structural skeleton for all Decision-Driven BI report prototypes.