MOCKUP_v1.0.svg — Notes and assumptions

Overview
- This is a first-pass, single-page SVG mockup (1200×900) based on `INPUT_REPORT_STORY_v1.0.md` and `OUTPUT 01 — MOCKUP_v1.0.md` in the test-run folder.

What I rendered
- Header with global filters (Animal Type, Region, Centre, Capacity Status).
- KPI row for provincial snapshot (Total/Open spaces and utilization percentages).
- Action Required area showing Emergency Closures, Full Centres, Data Quality Alerts.
- Intake Readiness panels (Candidate / Monitor / Do Not Intake).
- Placement Decision Board table (sample rows).
- Capacity Analysis placeholder with bars.
- Data Trust, Regional Health, and Operational Briefing compact cards.

Assumptions
- Colors and typography are neutral defaults (no brand palette supplied).
- Numeric values are placeholders and not driven from live data.
- Layout follows the markdown wireframe and uses simple rectangular containers and text.

How to change theme (quick)
- Provide a CSS-like palette (primary, accent, success, warning, danger, background, surface). Example:
  - primary: #0b3d91
  - accent: #2a9d8f
  - danger: #e63946
  - warning: #f4a261
  - background: #f6f8fa
  - surface: #ffffff
- I can re-generate the SVG with your palette applied.

Export to PNG
- Use Inkscape (recommended) or ImageMagick to convert the SVG to a PNG preview.

Inkscape (CLI) example:
```bash
inkscape MOCKUP_v1.0.svg --export-type=png --export-filename=MOCKUP_v1.0.png --export-width=2400 --export-height=1800
```

ImageMagick example:
```bash
magick convert MOCKUP_v1.0.svg MOCKUP_v1.0.png
```

Next steps
- If you provide a UX theme (brand colors / fonts / logo / target dimensions), I will re-generate the mockup to match and produce a PNG preview.
- If you want sample data, provide a small CSV and I will render realistic numbers in the SVG or produce a data-driven PNG.
