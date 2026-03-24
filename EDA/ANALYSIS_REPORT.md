# Nova Scotia Childhood Immunization Coverage Analysis Report

## Executive Summary

This analysis supports the strategic decision facing Nova Scotia Health's Director of Public Health: whether to prioritize **Public Health Mobile Units (PHMUs)** or **Pharmacy-Led Pediatric Vaccine Programs** to close the immunization gap for unattached children.

### Key Findings

| Metric | Value | Implication |
|--------|-------|-------------|
| Provincial Average Coverage | 85.6% | **Below 95% herd immunity target** |
| Lowest Performing Zone | Eastern (83.3%) | Priority target for interventions |
| Highest Performing Zone | Northern (88.3%) | Model for best practices |
| Most Critical Gap | HBV Dose 2 (76.1%) | Completion rates need attention |
| COVID-19 Impact | -5.4% drop (2019-20) | Recovery strategies needed |


---

## Section 1: Temporal Trend Analysis

### Coverage Trajectory (2012-2022)

```
Year     Coverage    Change    Status
2012     85.88%       -        Baseline
2013     85.63%     -0.25%     Slight decline
2014     85.93%     +0.30%     Recovery
2015     87.23%     +1.30%     PEAK YEAR
2016     86.07%     -1.16%     Decline begins
2017     88.32%     +2.24%     Recovery
2018     87.62%     -0.69%     Slight decline
2019     82.15%     -5.47%     COVID-19 IMPACT
2020     77.96%     -4.19%     Pandemic low
2021     83.90%     +5.95%     RECOVERY
```

### Key Insight
The **COVID-19 pandemic caused a 10-percentage-point decline** from peak (88.32% in 2017) to trough (77.96% in 2020). The 2021 data shows recovery (+5.95%), but coverage remains **11.1 percentage points below the 95% target**.

---

## Section 2: Geographic Zone Analysis

### Zone Performance Ranking

| Rank | Zone | Avg Coverage | Gap from Target | Priority Level |
|------|------|--------------|-----------------|----------------|
| 1 | Northern | 88.29% | 6.71% | Moderate |
| 2 | Central | 85.36% | 9.64% | High |
| 3 | Western | 84.53% | 10.47% | High |
| 4 | Eastern | 83.11% | 11.89% | **Critical** |

### Unvaccinated Population by Zone (Total 2012-2022)

| Zone | Total Eligible | Total Unvaccinated | Percentage |
|------|----------------|-------------------|------------|
| Central | 204,686 | 29,972 | 14.6% |
| Western | 90,720 | 14,035 | 15.5% |
| Eastern | 77,306 | 12,902 | 16.7% |
| Northern | 75,003 | 8,780 | 11.7% |

### Strategic Recommendation
**Eastern Zone should be the primary target** for intervention deployment (PHMU or Pharmacy programs) due to:
1. Lowest coverage rates
2. Highest percentage of unvaccinated children
3. Consistent underperformance across all vaccine types

---

## Section 3: Vaccine-Specific Analysis

### Coverage by Vaccine Type (Provincial Level)

| Vaccine | Average Coverage | Status | Notes |
|---------|------------------|--------|-------|
| MEN-C-C (historical) | 92.87% | Near target | Strong performance |
| MEN-C-ACYW-135 | 91.25% | Good | 3.75% from target |
| HPV - Dose 1 | 88.42% | Moderate | First dose uptake good |
| HBV - Dose 1 | 86.62% | Moderate | Similar pattern |
| TDAP | 89.22% | Moderate | 5.78% gap |
| HPV - Dose 2 | 82.28% | **Concern** | Completion dropout |
| HBV - Dose 2 | 76.02% | **Critical** | Major completion gap |
| HPV - Dose 3 | 75.93% | **Critical** | Lowest completion |

### The "Completion Gap" Problem
There is a consistent **10-15 percentage point drop** between first and subsequent doses:
- HBV: Dose 1 (86.6%) → Dose 2 (76.0%) = **10.6% dropout**
- HPV: Dose 1 (88.4%) → Dose 2 (82.3%) → Dose 3 (75.9%) = **12.5% dropout**

### Strategic Recommendation
Both intervention models must address the **completion gap** through:
- Automated reminder systems
- Flexible scheduling
- Follow-up protocols

---

## Section 4: Gap Analysis (Distance from 95% Target)

### Priority Matrix: Zone x Vaccine Combinations

| Priority | Zone | Vaccine | Coverage | Gap | Unvaccinated |
|----------|------|---------|----------|-----|--------------|
| **1** | Central | HBV Dose 2 | 71.4% | 23.6% | 6,061 |
| **2** | Central | HPV Dose 3 | 72.5% | 22.5% | 1,646 |
| **3** | Eastern | HPV Dose 3 | 76.8% | 18.2% | 581 |
| **4** | Western | HPV Dose 3 | 77.1% | 17.9% | 641 |
| **5** | Western | HBV | 77.5% | 17.5% | 2,025 |
| **6** | Eastern | HBV Dose 2 | 77.5% | 17.5% | 1,887 |
| **7** | Western | HBV Dose 2 | 78.4% | 16.6% | 2,084 |
| **8** | Western | HPV | 78.5% | 16.5% | 1,932 |
| **9** | Eastern | HBV | 78.6% | 16.4% | 1,589 |
| **10** | Eastern | HPV | 78.9% | 16.1% | 1,570 |

---

## Section 5: Decision Support Analysis

### PHMU vs Pharmacy Program Trade-offs

| Factor | PHMU | Pharmacy-Led |
|--------|------|--------------|
| **Geographic Reach** | Targeted to hotspots | 300+ locations province-wide |
| **Staffing** | Requires scarce nursing staff | Leverages existing workforce |
| **Data Integration** | Direct to provincial systems | Requires standardization |
| **Cost Model** | Higher per-visit cost | Lower marginal cost |
| **Scheduling Flexibility** | Limited by deployment | Extended hours possible |
| **Pediatric Training** | Existing competency | Requires PITP certification |

### Data-Driven Recommendations

**For Eastern Zone (Critical Priority):**
- Consider **PHMU deployment** first due to potentially fewer pharmacy locations in rural Eastern communities
- Target HBV and HPV completion doses specifically

**For Central Zone (Highest Volume):**
- **Pharmacy-Led Program** ideal due to highest population density and pharmacy availability
- Focus on HBV Dose 2 completion (6,061 unvaccinated)

**For Western Zone:**
- **Hybrid approach** - PHMUs for rural areas, pharmacy partnerships in urban centers

**For Northern Zone (Best Performing):**
- **Maintain current strategies** which are clearly working
- Document and share best practices

---

## Section 6: Tableau Visualization Recommendations

### Visualization 1: Temporal Coverage Trend Line
**Purpose:** Show immunization coverage trajectory over 10 years
**Chart Type:** Line chart with reference line at 95%
**Data Source:** `temporal_analysis.csv`
**Key Fields:**
- X-axis: Year_Start
- Y-axis: Overall_Coverage
- Reference Line: 0.95 (Herd Immunity Target)
- Annotations: COVID-19 impact period (2019-2021)

### Visualization 2: Zone Comparison Bar Chart
**Purpose:** Compare performance across 4 health zones
**Chart Type:** Horizontal bar chart with diverging color
**Data Source:** `zone_summary.csv`
**Key Fields:**
- Y-axis: Zone
- X-axis: Overall_Coverage
- Color: Conditional (Red if < 85%, Yellow if 85-90%, Green if > 90%)
- Sort: By coverage ascending (worst first)

### Visualization 3: Vaccine Coverage Heatmap
**Purpose:** Identify vaccine-zone combinations needing attention
**Chart Type:** Heatmap/Highlight table
**Data Source:** `zone_vaccine_matrix.csv`
**Key Fields:**
- Rows: Zone
- Columns: Vaccine
- Color: Coverage percentage (diverging scale)
- Highlight: Cells below herd immunity threshold

### Visualization 4: Gap Analysis Scatter Plot
**Purpose:** Prioritize interventions by gap size and population impact
**Chart Type:** Bubble chart / scatter plot
**Data Source:** `gap_analysis.csv`
**Key Fields:**
- X-axis: Gap_From_Target
- Y-axis: # Unvaccinated
- Size: # Eligible
- Color: Zone
- Labels: Vaccine type

---

## Section 7: Data Files Generated

| File | Description | Use Case |
|------|-------------|----------|
| `immunization_data_cleaned.csv` | Full cleaned dataset | Primary Tableau data source |
| `zone_summary.csv` | Zone-level aggregations | Zone comparison visualizations |
| `vaccine_summary.csv` | Vaccine-level aggregations | Vaccine performance analysis |
| `temporal_analysis.csv` | Year-over-year trends | Time series visualizations |
| `zone_vaccine_matrix.csv` | Pivot table format | Heatmap visualizations |
| `gap_analysis.csv` | Prioritized gap list | Intervention targeting |

---

## Section 8: Limitations and Data Gaps

### Current Data Limitations
1. **No current "Need a Family Practice" registry data** - removed from public access
2. **No pharmacy distribution data** - needed for pharmacy-led program planning
3. **No cost data** - prevents cost-effectiveness analysis
4. **School-based only** - may not capture early childhood immunization gaps

### Recommended Additional Data Sources (from TODO.md)
1. **World Bank Immunization Data** - G20 benchmarking
   - URL: https://data.worldbank.org/indicator/SH.IMM.IDPT
2. **Physicians per 1000 population** - correlate with coverage
   - URL: https://data.worldbank.org/indicator/SH.MED.PHYS.ZS

---

## Conclusion

The data strongly supports a **zone-differentiated strategy**:

1. **Immediate Action (Eastern Zone):** Deploy intervention resources to address critical 11.89% gap
2. **High Volume Focus (Central Zone):** Pharmacy partnerships for 6,000+ unvaccinated HBV Dose 2 children
3. **Completion Focus (All Zones):** Both models must include follow-up mechanisms for multi-dose vaccines
4. **Monitor Recovery:** Track post-COVID coverage recovery trajectory

The 95% herd immunity target requires an average **11.1 percentage point improvement** - this represents approximately **9,000+ additional children** requiring immunization annually.

---

*Report generated: March 2026*
*Data source: Nova Scotia Open Data Portal - School-Based Immunization Coverage*
