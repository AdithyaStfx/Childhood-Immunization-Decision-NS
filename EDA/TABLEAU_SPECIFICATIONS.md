# Tableau Visualization Specifications for Milestone 2

## Overview
This document provides step-by-step instructions for creating the 4 required visualizations in Tableau to support the NS Childhood Immunization Decision Analysis.

---

## Data Connection Setup

### Primary Data Source
**File:** `output/immunization_data_cleaned.csv`

### Supplementary Data Sources (for specific charts)
- `output/zone_summary.csv`
- `output/temporal_analysis.csv`
- `output/zone_vaccine_matrix.csv`
- `output/gap_analysis.csv`

---

## Visualization 1: Coverage Trend Over Time

### Purpose
Show how immunization coverage has changed over the 10-year period, highlighting the COVID-19 impact and distance from the 95% herd immunity target.

### Chart Type
Dual-axis line chart with reference line

### Step-by-Step Instructions

1. **Data Preparation:**
   - Connect to `temporal_analysis.csv`
   - Ensure Year_Start is set as a Date/Dimension

2. **Build the Chart:**
   - Drag `Year_Start` to Columns
   - Drag `Overall_Coverage` to Rows
   - Change Mark type to Line

3. **Add Reference Line:**
   - Right-click on Y-axis → Add Reference Line
   - Set Value to Constant: 0.95
   - Label: "95% Herd Immunity Target"
   - Line: Dashed, Red color

4. **Formatting:**
   - Title: "Nova Scotia Immunization Coverage Trend (2012-2022)"
   - Y-axis: Format as Percentage (0-100%)
   - Add annotation for 2020 point: "COVID-19 Impact: -5.5%"

5. **Color Encoding:**
   - Create calculated field: `IF [Overall_Coverage] >= 0.95 THEN "At Target" ELSE "Below Target" END`
   - Color line by this field (Green/Red)

### Key Insights to Highlight
- Peak coverage: 88.3% (2017)
- Lowest coverage: 78.0% (2020)
- Current gap: 11.1 percentage points below target

---

## Visualization 2: Zone Performance Comparison

### Purpose
Compare immunization coverage across the 4 health zones to identify priority intervention areas.

### Chart Type
Horizontal bar chart with conditional coloring

### Step-by-Step Instructions

1. **Data Preparation:**
   - Connect to `zone_summary.csv`
   - Or filter main dataset: Zone ≠ "NOVA SCOTIA"

2. **Build the Chart:**
   - Drag `Zone` to Rows
   - Drag `Overall_Coverage` (or AVG[% Coverage]) to Columns
   - Sort by coverage ascending (worst performers at top)

3. **Add Reference Line:**
   - Constant line at 0.95 (95% target)

4. **Conditional Coloring:**
   - Create calculated field:
   ```
   IF [Overall_Coverage] < 0.85 THEN "Critical"
   ELSEIF [Overall_Coverage] < 0.90 THEN "Moderate"
   ELSE "Good"
   END
   ```
   - Apply color: Red (Critical), Yellow (Moderate), Green (Good)

5. **Add Labels:**
   - Show percentage on bars
   - Add gap annotation: `STR(ROUND((0.95 - [Overall_Coverage])*100, 1)) + "% gap"`

6. **Formatting:**
   - Title: "Immunization Coverage by Health Zone"
   - X-axis: 0% to 100% range

### Expected Results
```
Eastern  |████████████████████████████░░░░░| 83.3%  (-11.7% gap)
Western  |█████████████████████████████░░░░| 84.5%  (-10.5% gap)
Central  |██████████████████████████████░░░| 85.4%  (-9.6% gap)
Northern |███████████████████████████████░░| 88.3%  (-6.7% gap)
```

---

## Visualization 3: Vaccine-Zone Coverage Heatmap

### Purpose
Identify specific vaccine-zone combinations requiring intervention through a matrix view.

### Chart Type
Highlight table / Heatmap

### Step-by-Step Instructions

1. **Data Preparation:**
   - Connect to `zone_vaccine_matrix.csv`
   - Or use main dataset grouped by Zone and Vaccine

2. **Build the Chart:**
   - Drag `Zone` to Rows
   - Drag `Vaccine` to Columns
   - Drag `% Coverage` (or AVG) to both Text and Color

3. **Color Configuration:**
   - Edit Colors → Diverging palette
   - Center: 0.90 (90%)
   - Below center: Red shades
   - Above center: Green shades
   - Stepped color: 5 steps

4. **Formatting:**
   - Title: "Coverage Matrix: Zone × Vaccine Type"
   - Format numbers as percentages
   - Add borders between cells
   - Tooltip: "Zone: [Zone], Vaccine: [Vaccine], Coverage: [% Coverage]"

5. **Highlight Critical Cells:**
   - Add conditional formatting for cells < 80%
   - Bold or bordered for lowest values

### Expected Insight
The heatmap should clearly show:
- Northern zone performs best across all vaccines
- Eastern zone underperforms across all vaccines
- HBV and HPV have lowest coverage (red cells)
- MEN-C has highest coverage (green cells)

---

## Visualization 4: Gap Analysis Priority Matrix

### Purpose
Combine gap size with population impact to prioritize intervention targets.

### Chart Type
Bubble chart / Scatter plot

### Step-by-Step Instructions

1. **Data Preparation:**
   - Connect to `gap_analysis.csv`
   - Ensure all numeric fields are properly typed

2. **Build the Chart:**
   - Drag `Gap_From_Target` to Columns
   - Drag `# Unvaccinated` to Rows
   - Drag `# Eligible` to Size
   - Drag `Zone` to Color
   - Drag `Vaccine` to Label/Detail

3. **Reference Lines:**
   - Add vertical line at X = 0.15 (15% gap threshold)
   - Add horizontal line at Y = 2000 (high-impact threshold)
   - This creates 4 quadrants

4. **Quadrant Labels:**
   - Top-Right: "CRITICAL: High Gap + High Impact"
   - Top-Left: "MONITOR: Low Gap + High Impact"
   - Bottom-Right: "IMPROVE: High Gap + Low Impact"
   - Bottom-Left: "MAINTAIN: Low Gap + Low Impact"

5. **Formatting:**
   - Title: "Intervention Priority Matrix: Gap vs. Population Impact"
   - X-axis: "Gap from 95% Target"
   - Y-axis: "Number of Unvaccinated Children"
   - Legend: Zone colors

6. **Tooltip Configuration:**
   ```
   Zone: <Zone>
   Vaccine: <Vaccine>
   Gap: <Gap_From_Target> percentage points
   Unvaccinated: <# Unvaccinated> children
   Eligible: <# Eligible> total
   Coverage: <% Coverage>
   ```

### Expected Results
- Top-right quadrant (Critical): Central-HBV Dose 2, Central-HPV Dose 3
- Action items clearly visible by position and size

---

## Dashboard Assembly

### Recommended Layout

```
┌─────────────────────────────────────────────────────────────┐
│  NOVA SCOTIA CHILDHOOD IMMUNIZATION DECISION SUPPORT        │
│  Closing the Coverage Gap: PHMU vs Pharmacy-Led Analysis    │
├─────────────────────────────┬───────────────────────────────┤
│                             │                               │
│  Viz 1: Trend Line          │  Viz 2: Zone Comparison       │
│  (Coverage over Time)       │  (Horizontal Bars)            │
│                             │                               │
├─────────────────────────────┼───────────────────────────────┤
│                             │                               │
│  Viz 3: Heatmap             │  Viz 4: Priority Matrix       │
│  (Zone x Vaccine)           │  (Gap vs Impact)              │
│                             │                               │
├─────────────────────────────┴───────────────────────────────┤
│  Filters: Year Range | Zone | Vaccine                       │
│  Key Insight: Currently 11.1% below herd immunity target    │
└─────────────────────────────────────────────────────────────┘
```

### Interactive Features
1. **Zone Filter:** Apply to all charts
2. **Year Range Slider:** For trend analysis
3. **Vaccine Type Selector:** For deep-dive analysis
4. **Highlight Actions:** Click zone in bar chart → highlight in other views

### Color Palette Recommendation
- Provincial data: Navy Blue (#1C4587)
- Eastern Zone: Red (#DC3545)
- Western Zone: Orange (#FD7E14)
- Central Zone: Yellow (#FFC107)
- Northern Zone: Green (#28A745)
- Target Line: Dashed Red (#C0392B)
- Below Target: Red gradient
- Above Target: Green gradient

---

## Calculated Fields Reference

### For Main Dataset
```tableau
// Gap from target
Gap_From_95 = 0.95 - [% Coverage]

// Gap as percentage points
Gap_Percentage_Points = [Gap_From_95] * 100

// Performance category
Performance_Category =
  IF [% Coverage] >= 0.95 THEN "At Target"
  ELSEIF [% Coverage] >= 0.90 THEN "Near Target"
  ELSEIF [% Coverage] >= 0.85 THEN "Moderate Gap"
  ELSE "Critical Gap"
  END

// Intervention priority
Priority_Score = [Gap_From_95] * [# Unvaccinated]
```

---

## Export Settings

### For Presentation
- Size: 1920 x 1080 (Full HD)
- Format: PDF for print, PNG for digital

### For Report
- Size: 8.5" x 11" (Letter)
- Include title and annotations

---

*Document prepared for BSAD 482 Term Project - Milestone 2*
