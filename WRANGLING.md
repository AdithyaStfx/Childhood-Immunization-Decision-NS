# Data Wrangling Documentation

## Nova Scotia Childhood Immunization Coverage Data

This document describes the data cleaning and transformation process applied to the raw immunization coverage data from the Nova Scotia Open Data Portal.

---

## 1. Raw Data Overview

### Source File
**Primary:** `data/School-Based_Immunization_Coverage_in_Nova_Scotia_20260319.csv`

### Original Data Structure

| Column | Original Format | Example |
|--------|-----------------|---------|
| Year | Quoted string | `"2017-18"` |
| Zone | Quoted string | `"WESTERN"` |
| Vaccine | Quoted string | `"HBV"` |
| # Immunized | Quoted string with commas | `"1,310"` |
| # Eligible | Quoted string with commas | `"1,583"` |
| % Coverage | Quoted string with % and decimals | `"82.75426405559%"` |
| 95% CI | Quoted string | `"80.9-84.6"` |

**Total Records:** 265 rows across 10 school years (2012-13 to 2021-22)

---

## 2. Issues Encountered in Raw Data

### Issue 1: Quoted String Values Throughout

**Problem:** All fields were enclosed in double quotes, including numeric values.

**Example:**
```csv
"Year","Zone","Vaccine","# Immunized","# Eligible","% Coverage","95% CI"
"2017-18","WESTERN","HBV","1,310","1,583","82.75426405559%","80.9-84.6"
```

**Impact:** Pandas read these as string objects, preventing numerical calculations.

---

### Issue 2: Comma-Separated Thousands in Numeric Fields

**Problem:** The `# Immunized` and `# Eligible` columns contained commas as thousand separators.

**Example:**
- `"1,310"` instead of `1310`
- `"3,594"` instead of `3594`

**Impact:** Could not perform mathematical operations or aggregations on population counts.

---

### Issue 3: Percentage Symbol in Coverage Field

**Problem:** The `% Coverage` field contained the `%` symbol and excessive decimal precision.

**Example:**
- `"82.75426405559%"` instead of `0.8275`

**Impact:**
- Could not compare coverage rates numerically
- Inconsistent precision (up to 11 decimal places)

---

### Issue 4: School Year Format Requires Parsing

**Problem:** Year field used school-year format (`"2017-18"`) rather than a single numeric year.

**Example:**
- `"2017-18"` represents the 2017-2018 school year

**Impact:** Could not sort chronologically or perform time-series analysis without extracting the start year.

---

### Issue 5: Provincial Totals Mixed with Zone Data

**Problem:** The dataset includes both zone-level records (WESTERN, NORTHERN, EASTERN, CENTRAL) and provincial totals (NOVA SCOTIA) in the same column.

**Example:**
```
WESTERN, HBV, 2017-18, ...
NOVA SCOTIA, HBV, 2017-18, ...  (provincial total)
```

**Impact:** Aggregating by zone would double-count if provincial totals were included.

---

### Issue 6: Missing Calculated Fields for Analysis

**Problem:** The raw data lacked several fields needed for decision-support analysis:
- Gap from 95% herd immunity target
- Number of unvaccinated children
- Year-over-year change metrics
- Boolean flag for target achievement

**Impact:** Could not directly assess performance against policy targets.

---

## 3. How Each Issue Was Addressed

### Solution 1: Remove Quotes from All Fields

**Method:** Applied string stripping and quote removal to all columns.

```python
# Clean column names
df.columns = df.columns.str.strip().str.replace('"', '')

# Clean data values
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].str.strip().str.replace('"', '')
```

**Result:** All fields now contain clean, unquoted values.

---

### Solution 2: Convert Population Counts to Integers

**Method:** Removed commas and converted to integer type.

```python
df['# Immunized'] = df['# Immunized'].str.replace(',', '').astype(int)
df['# Eligible'] = df['# Eligible'].str.replace(',', '').astype(int)
```

**Result:**
- `"1,310"` → `1310` (integer)
- Enables sum(), mean(), and other aggregations

---

### Solution 3: Standardize Coverage as Decimal Proportion

**Method:** Removed `%` symbol and normalized to 0-1 scale.

```python
df['% Coverage'] = df['% Coverage'].str.rstrip('%').astype(float)
df['% Coverage'] = df['% Coverage'].apply(lambda x: x/100 if x > 1 else x)
```

**Result:**
- `"82.75426405559%"` → `0.8275` (rounded for display)
- Consistent decimal format for all calculations
- Values now represent proportions (0.0 to 1.0)

---

### Solution 4: Extract Numeric Year for Time Series

**Method:** Parsed school year string to extract start year as integer.

```python
df['Year_Start'] = df['Year'].str.split('-').str[0].astype(int)
```

**Result:**
- `"2017-18"` → `2017` (integer)
- Enables chronological sorting and time-series plotting
- Original `Year` column preserved for labeling

---

### Solution 5: Filter Provincial Totals for Zone Analysis

**Method:** Created separate analysis paths for zone-level and provincial data.

```python
# For zone-level analysis (excludes provincial totals)
zone_df = df[df['Zone'] != 'NOVA SCOTIA'].copy()

# For provincial trends (uses only provincial totals)
prov_df = df[df['Zone'] == 'NOVA SCOTIA'].copy()
```

**Result:**
- Zone summaries use only the 4 health zones
- Temporal trends use provincial aggregates
- No double-counting in aggregations

---

### Solution 6: Add Calculated Fields for Analysis

**Method:** Created new columns for decision-support metrics.

```python
HERD_IMMUNITY_TARGET = 0.95

# Gap from 95% target
df['Gap_From_Target'] = HERD_IMMUNITY_TARGET - df['% Coverage']
df['Gap_Percentage_Points'] = df['Gap_From_Target'] * 100

# Target achievement flag
df['Meets_Target'] = df['% Coverage'] >= HERD_IMMUNITY_TARGET

# Unvaccinated count
df['# Unvaccinated'] = df['# Eligible'] - df['# Immunized']
```

**Result:**
| New Field | Description | Example |
|-----------|-------------|---------|
| Gap_From_Target | Decimal gap from 0.95 | 0.1225 |
| Gap_Percentage_Points | Gap in percentage points | 12.25 |
| Meets_Target | Boolean target achievement | False |
| # Unvaccinated | Count of unvaccinated | 273 |

---

## 4. Assumptions and Decisions Made During Cleaning

### Assumption 1: Latest Dataset is Most Accurate

**Decision:** Used `School-Based_Immunization_Coverage_in_Nova_Scotia_20260319.csv` as the primary data source.

**Rationale:** The March 2026 version is the most recent and likely contains any corrections or updates.

---

### Assumption 2: 95% as Herd Immunity Target

**Decision:** Used 95% as the benchmark for herd immunity across all vaccines.

**Rationale:**
- WHO recommends 95% coverage for measles herd immunity
- Canadian Immunization Guide uses 95% as the standard target
- Consistent with Background.md project context

**Limitation:** Different vaccines may have different herd immunity thresholds (e.g., measles requires ~95%, polio ~80-85%).

---

### Assumption 3: School Year Start Year Represents the Record

**Decision:** Used the first year of the school year pair (e.g., 2017 for "2017-18").

**Rationale:**
- Consistent with academic year conventions
- Enables clean integer-based time series
- Vaccination data is collected throughout the school year

---

### Assumption 4: Zone-Level Analysis Excludes Provincial Totals

**Decision:** Filtered out "NOVA SCOTIA" records when analyzing zone performance.

**Rationale:**
- Provincial totals are aggregates of zone data
- Including them would create artificial inflation in zone statistics
- Separate analysis paths for zone vs. provincial insights

---

### Assumption 5: Coverage Values > 1 Need Normalization

**Decision:** Applied conditional normalization: `x/100 if x > 1 else x`

**Rationale:**
- Raw data had coverage as percentage (e.g., 82.75)
- After removing `%`, values > 1 indicate percentage format
- Normalizing to 0-1 scale ensures consistency
- Protects against data that might already be normalized

---

### Assumption 6: Confidence Intervals Not Used in Analysis

**Decision:** Did not process or use the `95% CI` column in analysis.

**Rationale:**
- CI data is useful for statistical inference but not required for decision-support visualizations
- Adding CI analysis would increase complexity without significant decision value
- Point estimates sufficient for trend and comparison analysis

**Future Consideration:** CI data could be used for uncertainty visualization in advanced analysis.

---

## 5. Data Quality Summary

### Before Cleaning

| Issue | Count | Severity |
|-------|-------|----------|
| Quoted strings | 265 rows × 7 columns | High |
| Comma-formatted numbers | 530 values | High |
| Percentage symbols | 265 values | High |
| School year format | 265 values | Medium |
| Missing calculated fields | N/A | Medium |

### After Cleaning

| Metric | Value |
|--------|-------|
| Total records | 265 |
| Valid records | 265 (100%) |
| Null values | 0 |
| Numeric columns | 6 (# Immunized, # Eligible, % Coverage, Year_Start, Gap_From_Target, # Unvaccinated) |
| Categorical columns | 3 (Year, Zone, Vaccine) |
| Boolean columns | 1 (Meets_Target) |

---

## 6. Output Files Generated

| File | Records | Description |
|------|---------|-------------|
| `immunization_data_cleaned.csv` | 265 | Full cleaned dataset with all calculated fields |
| `zone_summary.csv` | 4 | Aggregated statistics by health zone |
| `vaccine_summary.csv` | 2 | Coverage summary for TDAP and MEN-C-ACYW-135 |
| `temporal_analysis.csv` | 10 | Year-over-year provincial trends |
| `zone_vaccine_matrix.csv` | 4×4 | Pivot table for heatmap (zone × vaccine) |
| `gap_analysis.csv` | 40 | Prioritized zone-vaccine gap rankings |

---

## 7. Reproducibility

To reproduce the data cleaning process:

```bash
cd EDA/
python data_preparation.py
```

**Requirements:**
- Python 3.8+
- pandas library

**Output Location:** `Clipped_Data/` folder

---

## 8. Changelog

| Date | Version | Changes |
|------|---------|---------|
| Mar 2026 | 1.0 | Initial data cleaning and transformation |
| Mar 2026 | 1.1 | Updated vaccine_summary.csv to focus on TDAP and MEN-C-ACYW-135 |

---

*Document prepared as part of BSAD 482 Term Project - Milestone 2*
