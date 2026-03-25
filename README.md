# Closing the Immunization Gap: Strategic Resource Allocation for Unattached Pediatric Populations in Nova Scotia

## The Decision

Should Nova Scotia Health prioritize the expansion of **Public Health Mobile Units (PHMUs)** or establish a specialized **Pharmacy-Led Pediatric Vaccine Program** to close the immunization gap for unattached children?

---

## Project Summary

Nova Scotia is currently facing a critical challenge in maintaining herd immunity for its youngest residents. While provincial policy requires proof of immunization for school entry, the delivery of these vaccines has historically relied on primary care providers (family doctors and nurse practitioners). However, as of early 2026, over 65,000 Nova Scotians remain on the Need a Family Practice Registry. This "primary care gap" has directly contributed to a decline in childhood immunization coverage; recent data indicates that while over 93% of two-year-olds have received their first measles dose, only 78.6% are fully vaccinated with both required shots significantly below the national safety target of 95%.

This project provides a decision-support analysis for the Director of Public Health at Nova Scotia Health (NSH). The Director must decide how to best allocate limited provincial resources to reach these "unattached" pediatric populations before they enter the school system. The analysis evaluates two primary strategic paths:

1. **Expanding Public Health Mobile Units (PHMUs)**: A direct-delivery model that brings NSH nurses into underserved rural and urban zones.

2. **Standardizing a Pharmacy-Led Pediatric Program**: A community-integrated model that leverages the province's existing network of 300+ pharmacies to administer routine childhood injections beyond the traditional flu and COVID-19 scope.

Through a combination of systems thinking and data analysis, this portfolio explores the trade-offs between these two options. It considers constraints such as the current nursing shortage, the legislative pressures of Bill 210, and the geographic disparities in vaccine access across the four health zones.

---

## Data Sources

### Primary Data: Nova Scotia Open Data Portal

**Source:** [School-Based Immunization Coverage in Nova Scotia](https://data.novascotia.ca/)

The primary dataset contains school-based immunization coverage records from the Nova Scotia Department of Health and Wellness. Three versions of this dataset are maintained in the `data/` folder:

| File | Date | Records | Description |
|------|------|---------|-------------|
| `School-Based_Immunization_Coverage_in_Nova_Scotia_20260319.csv` | Mar 19, 2026 | 265 | Latest version (primary) |
| `School-Based_Immunization_Coverage_in_Nova_Scotia_20260211.csv` | Feb 11, 2026 | 265 | Previous version |
| `School-Based_Immunization_Coverage_in_Nova_Scotia.csv` | Original | 265 | Baseline version |

**Data Structure:**
- **Temporal Coverage:** 2012-13 to 2021-22 (10 school years)
- **Geographic Zones:** Western, Northern, Eastern, Central, Nova Scotia (provincial total)
- **Vaccines Tracked:** HBV, HPV, MEN-C-ACYW-135, TDAP (plus dose-specific breakdowns)
- **Metrics:** # Immunized, # Eligible, % Coverage, 95% Confidence Interval

### Exploratory Data Analysis (EDA) Outputs

The `EDA/` folder contains processed analysis files and scripts:

| File | Purpose |
|------|---------|
| `data_preparation.py` | Python script for data cleaning and transformation |
| `create_visualizations.py` | Visualization generation script |
| `create_cld.py` | Causal Loop Diagram generation script |
| `ANALYSIS_REPORT.md` | Comprehensive analysis with key findings |
| `TABLEAU_SPECIFICATIONS.md` | Tableau visualization specifications |
| `FUTURE_EXPLORATION.md` | Recommended future research avenues |

### Cleaned Data Outputs (`Clipped_Data/`)

| File | Description |
|------|-------------|
| `immunization_data_cleaned.csv` | Main cleaned dataset with calculated fields |
| `zone_summary.csv` | Aggregated statistics by health zone |
| `vaccine_summary.csv` | Coverage summary for TDAP and MEN-C-ACYW-135 |
| `temporal_analysis.csv` | Year-over-year trend analysis |
| `zone_vaccine_matrix.csv` | Pivot table for heatmap visualization |
| `gap_analysis.csv` | Prioritized intervention targets |

---

## Key Visualizations

### 1. Temporal Coverage Trend (2012-2022)

![Temporal Trend](img/viz1_temporal_trend.png)

**Description:** This line chart tracks Nova Scotia's provincial immunization coverage over a 10-year period. The red dashed line represents the 95% herd immunity target. The shaded area highlights the persistent gap between actual coverage and target.

**Key Insights:**
- Coverage peaked at **88.3% in 2017** before declining
- COVID-19 caused a significant **5.5 percentage point drop** in 2020 (from 82.1% to 77.9%)
- Recovery is underway but coverage remains **11.1 percentage points below target**

---

### 2. Zone Performance Comparison

![Zone Comparison](img/viz2_zone_comparison.png)

**Description:** Horizontal bar chart comparing immunization coverage across Nova Scotia's four health zones, ranked from lowest to highest performance.

**Key Insights:**
- **Eastern Zone (83.3%)** is the lowest performer and should be the primary intervention target
- **Northern Zone (88.3%)** performs best, suggesting potential best practices to replicate
- All zones remain below the 95% herd immunity target
- The 5-percentage-point spread between zones indicates significant geographic disparity

---

### 3. Coverage Heatmap: Zone × Vaccine

![Coverage Heatmap](img/viz3_heatmap.png)

**Description:** A matrix visualization showing coverage rates for each zone-vaccine combination. Colors range from red (low coverage) to green (high coverage). Red borders highlight critical gaps below 80%.

**Key Insights:**
- **6 zone-vaccine combinations** fall below the 80% critical threshold
- Eastern Zone underperforms across **all vaccine types**
- MEN-C-ACYW-135 consistently achieves the highest coverage across all zones
- HBV and HPV show the largest coverage gaps

---

### 4. Intervention Priority Matrix

![Priority Matrix](img/viz4_gap_priority.png)

**Description:** A bubble chart plotting coverage gap (x-axis) against number of unvaccinated children (y-axis). Bubble size represents eligible population. The chart is divided into four quadrants to guide intervention prioritization.

**Key Insights:**
- **CRITICAL quadrant (top-right):** High gap + high unvaccinated count = immediate action needed
- Central Zone HBV Dose 2 has the largest absolute gap with ~6,000 unvaccinated children
- Eastern Zone appears frequently in high-gap areas across multiple vaccines
- Interventions should prioritize points in the upper-right quadrant for maximum impact

---

### 5. Vaccine Coverage Comparison (TDAP vs MEN-C-ACYW-135)

![Vaccine Comparison](img/viz5_vaccine_comparison.png)

**Description:** Side-by-side comparison of the two key single-dose vaccines in the school-based program, showing provincial totals and zone-by-zone breakdown.

**Key Insights:**
- **MEN-C-ACYW-135 (91.2%)** outperforms **TDAP (89.2%)** at the provincial level
- MEN-C achieves higher coverage consistently across all zones
- Both vaccines show the same geographic pattern: Northern > Central > Western > Eastern
- The gap from 95% target is smaller for these single-dose vaccines compared to multi-dose series

---

### 6. Dashboard Summary

![Dashboard Summary](img/dashboard_summary.png)

**Description:** A consolidated 4-panel dashboard combining the key visualizations for executive presentation.

---

## Causal Loop Diagram (CLD)

### System Dynamics Model

![CLD Immunization System](img/cld_immunization_system.png)

**Description:** This Causal Loop Diagram maps the interconnected variables affecting childhood immunization coverage in Nova Scotia. The diagram identifies 12 key variables, their causal relationships (positive and negative links), and two critical feedback loops.

### Key Feedback Loops

#### R1: Healthcare Strain Cycle (Reinforcing - Vicious)

**Loop Path:** Family Doctor Vacancy Rate → (+) Unattached Pediatric Population → (-) Vaccine Accessibility → (+) Immunization Coverage Rate → (-) Disease Outbreak Risk → (+) Public Health Workload → (+) Family Doctor Vacancy Rate

**Implications for Decision:**
- This vicious cycle explains why coverage remains stuck below 95% despite interventions
- Physician shortages create unattached populations, reducing vaccine access, which lowers coverage
- Lower coverage increases disease risk, adding burden to an already strained healthcare system
- **Breaking this loop requires interventions that bypass the primary care bottleneck** — both PHMUs and Pharmacy programs achieve this by providing alternative access points

#### R2: Trust-Completion Cycle (Reinforcing - Virtuous)

**Loop Path:** Immunization Coverage Rate → (+) Parent Trust & Awareness → (+) Multi-dose Completion Rate → (+) Immunization Coverage Rate

**Implications for Decision:**
- This virtuous cycle can be leveraged to accelerate coverage improvement
- As coverage increases, parents gain confidence in the system
- Higher confidence leads to better follow-through on multi-dose vaccines
- **Interventions should emphasize visibility and trust-building** — Pharmacy programs may have an advantage here due to community presence and accessibility

### Intervention Leverage Points

The CLD identifies two key intervention points (shown in purple):

| Intervention | Primary Effect | Secondary Effects |
|--------------|----------------|-------------------|
| **PHMU Capacity** | Reduces rural/remote access barriers | Directly increases vaccine accessibility; targets geographic disparity |
| **Pharmacy Program Capacity** | Increases overall vaccine accessibility | Improves multi-dose completion through convenient follow-up; leverages existing infrastructure |

### Evidence-Supported Links

![CLD Evidence Table](img/cld_evidence_table.png)

Five causal links in the diagram are supported by data from this analysis:

| Link | Evidence |
|------|----------|
| E1: Doctor Vacancy → Unattached Pop | 66,768 people on NS Family Practice Registry |
| E2: Unattached Pop → Accessibility | Eastern Zone has lowest coverage (83.3%) correlating with access barriers |
| E3: Accessibility → Coverage | Northern Zone (88.3%) vs Eastern Zone (83.3%) demonstrates access-coverage relationship |
| E4: Multi-dose Completion → Coverage | Single-dose vaccines (MEN-C: 91.2%) outperform multi-dose series by 3-6% |
| E5: Accessibility → Zone Disparity | Eastern Zone has 6 zone-vaccine cells below 85% threshold |

---

## Repository Structure

```
Childhood-Immunization-Decision-NS/
├── README.md                    # This file
├── WRANGLING.md                 # Data cleaning documentation
├── Background.md                # Project background and context
├── TODO.md                      # Project task tracking
│
├── data/                        # Raw data files
│   ├── School-Based_Immunization_Coverage_in_Nova_Scotia.csv
│   ├── School-Based_Immunization_Coverage_in_Nova_Scotia_20260211.csv
│   └── School-Based_Immunization_Coverage_in_Nova_Scotia_20260319.csv
│
├── Clipped_Data/                # Cleaned and processed data
│   ├── immunization_data_cleaned.csv
│   ├── zone_summary.csv
│   ├── vaccine_summary.csv
│   ├── temporal_analysis.csv
│   ├── zone_vaccine_matrix.csv
│   └── gap_analysis.csv
│
├── EDA/                         # Exploratory Data Analysis
│   ├── data_preparation.py
│   ├── create_visualizations.py
│   ├── create_cld.py
│   ├── ANALYSIS_REPORT.md
│   ├── TABLEAU_SPECIFICATIONS.md
│   └── FUTURE_EXPLORATION.md
│
└── img/                         # Visualization outputs
    ├── viz1_temporal_trend.png
    ├── viz2_zone_comparison.png
    ├── viz3_heatmap.png
    ├── viz4_gap_priority.png
    ├── viz5_vaccine_comparison.png
    ├── dashboard_summary.png
    ├── cld_immunization_system.png
    └── cld_evidence_table.png
```

---

## Key Findings Summary

| Metric | Value | Implication |
|--------|-------|-------------|
| Provincial Coverage (2021-22) | 83.9% | 11.1% below 95% target |
| Lowest Performing Zone | Eastern (83.3%) | Priority intervention area |
| Highest Performing Zone | Northern (88.3%) | Model for best practices |
| COVID-19 Impact | -5.5% (2019-2020) | Recovery still underway |
| Best Performing Vaccine | MEN-C-ACYW-135 (91.2%) | Single-dose advantage |
---

[Analysis.md](Analysis.md)