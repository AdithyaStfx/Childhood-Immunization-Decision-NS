"""
Nova Scotia Childhood Immunization Data Preparation Script
Purpose: Clean, consolidate, and prepare data for Tableau visualizations
"""

import pandas as pd
import os

# Configuration
DATA_DIR = r"C:\Users\Adithya JR\Desktop\Childhood-Immunization-Decision-NS\data"
OUTPUT_DIR = r"C:\Users\Adithya JR\Desktop\Childhood-Immunization-Decision-NS\output"
HERD_IMMUNITY_TARGET = 0.95  # 95% target for herd immunity

def load_and_clean_data():
    """Load the most recent dataset and clean it for analysis"""

    # Load the latest dataset
    df = pd.read_csv(f"{DATA_DIR}/School-Based_Immunization_Coverage_in_Nova_Scotia_20260319.csv")

    # Clean column names
    df.columns = df.columns.str.strip().str.replace('"', '')

    # Clean data values
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].str.strip().str.replace('"', '')

    # Convert numeric columns
    df['# Immunized'] = df['# Immunized'].str.replace(',', '').astype(int)
    df['# Eligible'] = df['# Eligible'].str.replace(',', '').astype(int)

    # Clean coverage percentage
    df['% Coverage'] = df['% Coverage'].str.rstrip('%').astype(float)
    df['% Coverage'] = df['% Coverage'].apply(lambda x: x/100 if x > 1 else x)

    # Extract year for sorting
    df['Year_Start'] = df['Year'].str.split('-').str[0].astype(int)

    # Calculate gap from herd immunity target
    df['Gap_From_Target'] = HERD_IMMUNITY_TARGET - df['% Coverage']
    df['Gap_Percentage_Points'] = df['Gap_From_Target'] * 100
    df['Meets_Target'] = df['% Coverage'] >= HERD_IMMUNITY_TARGET

    # Calculate unvaccinated count
    df['# Unvaccinated'] = df['# Eligible'] - df['# Immunized']

    return df

def create_zone_summary(df):
    """Create summary statistics by zone"""

    # Filter out provincial totals for zone analysis
    zone_df = df[df['Zone'] != 'NOVA SCOTIA'].copy()

    summary = zone_df.groupby('Zone').agg({
        '% Coverage': ['mean', 'min', 'max', 'std'],
        '# Eligible': 'sum',
        '# Immunized': 'sum',
        '# Unvaccinated': 'sum'
    }).round(4)

    summary.columns = ['_'.join(col).strip() for col in summary.columns.values]
    summary['Overall_Coverage'] = summary['# Immunized_sum'] / summary['# Eligible_sum']
    summary['Priority_Rank'] = summary['% Coverage_mean'].rank(ascending=True)

    return summary

def create_vaccine_summary(df):
    """Create summary statistics by vaccine type"""

    # Provincial level data only
    prov_df = df[df['Zone'] == 'NOVA SCOTIA'].copy()

    summary = prov_df.groupby('Vaccine').agg({
        '% Coverage': ['mean', 'min', 'max'],
        '# Eligible': 'sum',
        '# Immunized': 'sum'
    }).round(4)

    summary.columns = ['_'.join(col).strip() for col in summary.columns.values]
    summary['Overall_Coverage'] = summary['# Immunized_sum'] / summary['# Eligible_sum']

    return summary

def create_temporal_analysis(df):
    """Analyze trends over time"""

    # Provincial level data
    prov_df = df[df['Zone'] == 'NOVA SCOTIA'].copy()

    # Group by year and calculate average coverage
    temporal = prov_df.groupby('Year_Start').agg({
        '% Coverage': 'mean',
        '# Eligible': 'sum',
        '# Immunized': 'sum',
        'Gap_From_Target': 'mean'
    }).round(4)

    temporal['Overall_Coverage'] = temporal['# Immunized'] / temporal['# Eligible']
    temporal = temporal.sort_index()

    # Calculate year-over-year change
    temporal['YoY_Change'] = temporal['Overall_Coverage'].diff()

    return temporal

def create_zone_vaccine_matrix(df):
    """Create a pivot table of zone-vaccine coverage for heatmap visualization"""

    # Use most recent year for current snapshot
    latest_year = df['Year_Start'].max()
    recent_df = df[(df['Year_Start'] == latest_year) & (df['Zone'] != 'NOVA SCOTIA')].copy()

    matrix = recent_df.pivot_table(
        values='% Coverage',
        index='Zone',
        columns='Vaccine',
        aggfunc='mean'
    ).round(4)

    return matrix

def create_gap_analysis(df):
    """Identify areas with largest coverage gaps"""

    zone_df = df[df['Zone'] != 'NOVA SCOTIA'].copy()

    gap_analysis = zone_df.groupby(['Zone', 'Vaccine']).agg({
        'Gap_From_Target': 'mean',
        '# Unvaccinated': 'sum',
        '# Eligible': 'sum',
        '% Coverage': 'mean'
    }).round(4)

    gap_analysis = gap_analysis.reset_index()
    gap_analysis = gap_analysis.sort_values('Gap_From_Target', ascending=False)

    return gap_analysis

def export_for_tableau(df, zone_summary, vaccine_summary, temporal, matrix, gap_analysis):
    """Export all datasets for Tableau consumption"""

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Main cleaned dataset
    df.to_csv(f"{OUTPUT_DIR}/immunization_data_cleaned.csv", index=False)

    # Zone summary
    zone_summary.to_csv(f"{OUTPUT_DIR}/zone_summary.csv")

    # Vaccine summary
    vaccine_summary.to_csv(f"{OUTPUT_DIR}/vaccine_summary.csv")

    # Temporal analysis
    temporal.to_csv(f"{OUTPUT_DIR}/temporal_analysis.csv")

    # Zone-Vaccine matrix
    matrix.to_csv(f"{OUTPUT_DIR}/zone_vaccine_matrix.csv")

    # Gap analysis
    gap_analysis.to_csv(f"{OUTPUT_DIR}/gap_analysis.csv", index=False)

    print(f"All files exported to {OUTPUT_DIR}")

def main():
    print("=" * 60)
    print("Nova Scotia Immunization Data Preparation")
    print("=" * 60)

    # Load and clean
    print("\n1. Loading and cleaning data...")
    df = load_and_clean_data()
    print(f"   Loaded {len(df)} records")
    print(f"   Year range: {df['Year'].min()} to {df['Year'].max()}")
    print(f"   Zones: {df['Zone'].unique().tolist()}")
    print(f"   Vaccines: {df['Vaccine'].unique().tolist()}")

    # Create summaries
    print("\n2. Creating zone summary...")
    zone_summary = create_zone_summary(df)
    print(zone_summary.to_string())

    print("\n3. Creating vaccine summary...")
    vaccine_summary = create_vaccine_summary(df)
    print(vaccine_summary.to_string())

    print("\n4. Creating temporal analysis...")
    temporal = create_temporal_analysis(df)
    print(temporal.to_string())

    print("\n5. Creating zone-vaccine matrix...")
    matrix = create_zone_vaccine_matrix(df)
    print(matrix.to_string())

    print("\n6. Creating gap analysis (top 10)...")
    gap_analysis = create_gap_analysis(df)
    print(gap_analysis.head(10).to_string())

    # Export
    print("\n7. Exporting for Tableau...")
    export_for_tableau(df, zone_summary, vaccine_summary, temporal, matrix, gap_analysis)

    print("\n" + "=" * 60)
    print("Data preparation complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
