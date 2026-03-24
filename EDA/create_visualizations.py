"""
Nova Scotia Childhood Immunization Visualizations
Creates 4 data-rich but simple visualizations to support the analysis report
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

# Configuration
OUTPUT_DIR = r"C:\Users\Adithya JR\Desktop\Childhood-Immunization-Decision-NS\output"
VIZ_DIR = r"C:\Users\Adithya JR\Desktop\Childhood-Immunization-Decision-NS\visualizations"
HERD_IMMUNITY_TARGET = 0.95

# Color scheme
COLORS = {
    'target': '#C0392B',
    'below_target': '#E74C3C',
    'near_target': '#F39C12',
    'at_target': '#27AE60',
    'primary': '#2C3E50',
    'secondary': '#3498DB',
    'zones': {
        'EASTERN': '#E74C3C',
        'WESTERN': '#F39C12',
        'CENTRAL': '#3498DB',
        'NORTHERN': '#27AE60'
    }
}

def setup_style():
    """Set up consistent plot styling"""
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams['figure.figsize'] = (12, 7)
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.titleweight'] = 'bold'
    plt.rcParams['axes.labelsize'] = 12

def viz1_temporal_trend():
    """Visualization 1: Coverage Trend Over Time"""
    print("Creating Visualization 1: Temporal Trend...")

    df = pd.read_csv(f"{OUTPUT_DIR}/temporal_analysis.csv")

    fig, ax = plt.subplots(figsize=(14, 7))

    # Plot coverage line
    years = df['Year_Start']
    coverage = df['Overall_Coverage'] * 100

    ax.plot(years, coverage, marker='o', markersize=10, linewidth=3,
            color=COLORS['primary'], label='Provincial Coverage')

    # Add data labels
    for x, y in zip(years, coverage):
        ax.annotate(f'{y:.1f}%', (x, y), textcoords="offset points",
                   xytext=(0, 12), ha='center', fontsize=10, fontweight='bold')

    # Reference line at 95%
    ax.axhline(y=95, color=COLORS['target'], linestyle='--', linewidth=2,
               label='95% Herd Immunity Target')

    # Shade area below target
    ax.fill_between(years, coverage, 95, where=(coverage < 95),
                    color=COLORS['below_target'], alpha=0.2, label='Gap from Target')

    # COVID annotation
    ax.annotate('COVID-19\nImpact', xy=(2020, 78), xytext=(2018.5, 72),
                fontsize=11, ha='center',
                arrowprops=dict(arrowstyle='->', color='gray'),
                bbox=dict(boxstyle='round', facecolor='white', edgecolor='gray'))

    # Recovery annotation
    ax.annotate('Recovery\n+5.9%', xy=(2021, 84), xytext=(2021, 75),
                fontsize=10, ha='center',
                arrowprops=dict(arrowstyle='->', color='green'))

    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Immunization Coverage (%)', fontsize=12)
    ax.set_title('Nova Scotia Immunization Coverage Trend (2012-2022)\nSchool-Based Vaccination Rates',
                 fontsize=14, fontweight='bold', pad=20)

    ax.set_ylim(70, 100)
    ax.set_xlim(2011.5, 2022.5)
    ax.set_xticks(years)

    ax.legend(loc='lower left', fontsize=10)

    # Add summary box
    current_gap = 95 - coverage.iloc[-1]
    textstr = f'Current Status (2021-22):\n Coverage: {coverage.iloc[-1]:.1f}%\n Gap: {current_gap:.1f} percentage points'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    ax.text(0.98, 0.02, textstr, transform=ax.transAxes, fontsize=10,
            verticalalignment='bottom', horizontalalignment='right', bbox=props)

    plt.tight_layout()
    plt.savefig(f"{VIZ_DIR}/viz1_temporal_trend.png", dpi=150, bbox_inches='tight')
    plt.close()
    print("   Saved: viz1_temporal_trend.png")

def viz2_zone_comparison():
    """Visualization 2: Zone Performance Comparison"""
    print("Creating Visualization 2: Zone Comparison...")

    df = pd.read_csv(f"{OUTPUT_DIR}/zone_summary.csv")

    fig, ax = plt.subplots(figsize=(12, 7))

    # Sort by coverage (worst first)
    df = df.sort_values('Overall_Coverage', ascending=True)

    zones = df['Zone']
    coverage = df['Overall_Coverage'] * 100

    # Create horizontal bars with zone-specific colors
    bars = ax.barh(zones, coverage, height=0.6)

    # Color bars by zone
    for bar, zone in zip(bars, zones):
        bar.set_color(COLORS['zones'].get(zone, COLORS['primary']))
        bar.set_edgecolor('white')
        bar.set_linewidth(2)

    # Add target line
    ax.axvline(x=95, color=COLORS['target'], linestyle='--', linewidth=2,
               label='95% Target')

    # Add value labels and gap annotations
    for i, (zone, cov) in enumerate(zip(zones, coverage)):
        gap = 95 - cov
        ax.text(cov + 0.5, i, f'{cov:.1f}%', va='center', ha='left',
                fontsize=12, fontweight='bold')
        ax.text(96, i, f'Gap: {gap:.1f}%', va='center', ha='left',
                fontsize=10, color=COLORS['target'])

    ax.set_xlabel('Immunization Coverage (%)', fontsize=12)
    ax.set_ylabel('')
    ax.set_title('Immunization Coverage by Health Zone\nPriority Ranking for Intervention',
                 fontsize=14, fontweight='bold', pad=20)

    ax.set_xlim(75, 105)
    ax.set_yticks(range(len(zones)))
    ax.set_yticklabels([f'{z}\n(Priority {i+1})' for i, z in enumerate(zones)], fontsize=11)

    # Add legend
    legend_elements = [
        mpatches.Patch(facecolor=COLORS['zones']['EASTERN'], label='Eastern - Critical'),
        mpatches.Patch(facecolor=COLORS['zones']['WESTERN'], label='Western - High'),
        mpatches.Patch(facecolor=COLORS['zones']['CENTRAL'], label='Central - High'),
        mpatches.Patch(facecolor=COLORS['zones']['NORTHERN'], label='Northern - Moderate'),
        plt.Line2D([0], [0], color=COLORS['target'], linestyle='--', label='95% Target')
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=9)

    plt.tight_layout()
    plt.savefig(f"{VIZ_DIR}/viz2_zone_comparison.png", dpi=150, bbox_inches='tight')
    plt.close()
    print("   Saved: viz2_zone_comparison.png")

def viz3_heatmap():
    """Visualization 3: Zone-Vaccine Coverage Heatmap"""
    print("Creating Visualization 3: Coverage Heatmap...")

    df = pd.read_csv(f"{OUTPUT_DIR}/zone_vaccine_matrix.csv", index_col=0)

    # Convert to percentage
    data = df.values * 100

    fig, ax = plt.subplots(figsize=(12, 8))

    # Create heatmap
    im = ax.imshow(data, cmap='RdYlGn', aspect='auto', vmin=70, vmax=95)

    # Add colorbar
    cbar = ax.figure.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label('Coverage (%)', fontsize=11)

    # Set ticks and labels
    ax.set_xticks(np.arange(len(df.columns)))
    ax.set_yticks(np.arange(len(df.index)))
    ax.set_xticklabels(df.columns, fontsize=11)
    ax.set_yticklabels(df.index, fontsize=11)

    # Rotate x labels
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Add text annotations
    for i in range(len(df.index)):
        for j in range(len(df.columns)):
            value = data[i, j]
            color = 'white' if value < 80 else 'black'
            text = ax.text(j, i, f'{value:.1f}%', ha='center', va='center',
                          color=color, fontsize=11, fontweight='bold')

    # Add border for cells below 80%
    for i in range(len(df.index)):
        for j in range(len(df.columns)):
            if data[i, j] < 80:
                rect = plt.Rectangle((j-0.5, i-0.5), 1, 1, fill=False,
                                     edgecolor='red', linewidth=3)
                ax.add_patch(rect)

    ax.set_title('Coverage Matrix: Health Zone × Vaccine Type (2021-22)\nRed borders indicate critical gaps (<80%)',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xlabel('Vaccine Type', fontsize=12)
    ax.set_ylabel('Health Zone', fontsize=12)

    # Add legend annotation
    ax.text(0.5, -0.15, 'Color Scale: Red (Low Coverage) → Yellow (Moderate) → Green (High Coverage)',
            transform=ax.transAxes, ha='center', fontsize=10, style='italic')

    plt.tight_layout()
    plt.savefig(f"{VIZ_DIR}/viz3_heatmap.png", dpi=150, bbox_inches='tight')
    plt.close()
    print("   Saved: viz3_heatmap.png")

def viz4_gap_priority():
    """Visualization 4: Gap Analysis Priority Matrix"""
    print("Creating Visualization 4: Gap Priority Matrix...")

    df = pd.read_csv(f"{OUTPUT_DIR}/gap_analysis.csv")

    # Take top 15 for readability
    df = df.head(15)

    fig, ax = plt.subplots(figsize=(14, 9))

    # Create scatter plot
    for zone in df['Zone'].unique():
        zone_data = df[df['Zone'] == zone]
        scatter = ax.scatter(
            zone_data['Gap_From_Target'] * 100,
            zone_data['# Unvaccinated'],
            s=zone_data['# Eligible'] / 50,  # Scale bubble size
            c=COLORS['zones'].get(zone, 'gray'),
            alpha=0.7,
            edgecolors='white',
            linewidth=2,
            label=zone
        )

    # Add labels for top points
    for idx, row in df.head(10).iterrows():
        ax.annotate(
            f"{row['Vaccine']}\n({row['Zone'][:3]})",
            (row['Gap_From_Target'] * 100, row['# Unvaccinated']),
            textcoords="offset points",
            xytext=(10, 5),
            ha='left',
            fontsize=9,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8)
        )

    # Add quadrant lines
    ax.axvline(x=15, color='gray', linestyle=':', alpha=0.5)
    ax.axhline(y=1500, color='gray', linestyle=':', alpha=0.5)

    # Add quadrant labels
    ax.text(20, 5500, 'CRITICAL\nHigh Gap + High Impact', fontsize=10,
            ha='center', va='center', color=COLORS['target'], fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='#FADBD8', edgecolor=COLORS['target']))

    ax.text(8, 5500, 'MONITOR\nLow Gap + High Impact', fontsize=10,
            ha='center', va='center', color=COLORS['secondary'], fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='#D6EAF8', edgecolor=COLORS['secondary']))

    ax.text(20, 400, 'IMPROVE\nHigh Gap + Low Impact', fontsize=10,
            ha='center', va='center', color='#F39C12', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='#FEF9E7', edgecolor='#F39C12'))

    ax.text(8, 400, 'MAINTAIN\nLow Gap + Low Impact', fontsize=10,
            ha='center', va='center', color=COLORS['at_target'], fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='#D5F5E3', edgecolor=COLORS['at_target']))

    ax.set_xlabel('Gap from 95% Target (Percentage Points)', fontsize=12)
    ax.set_ylabel('Number of Unvaccinated Children', fontsize=12)
    ax.set_title('Intervention Priority Matrix\nGap Size vs. Population Impact (Bubble size = Eligible Population)',
                 fontsize=14, fontweight='bold', pad=20)

    # Legend
    ax.legend(title='Health Zone', loc='upper left', fontsize=10)

    # Size legend
    sizes = [5000, 10000, 20000]
    size_labels = ['5K', '10K', '20K']
    for i, (size, label) in enumerate(zip(sizes, size_labels)):
        ax.scatter([], [], s=size/50, c='gray', alpha=0.5,
                   label=f'{label} eligible', edgecolors='white')

    ax.set_xlim(5, 25)
    ax.set_ylim(0, 7000)

    plt.tight_layout()
    plt.savefig(f"{VIZ_DIR}/viz4_gap_priority.png", dpi=150, bbox_inches='tight')
    plt.close()
    print("   Saved: viz4_gap_priority.png")

def viz5_vaccine_comparison():
    """Bonus Visualization 5: TDAP vs MEN-C-ACYW-135 Coverage Comparison by Zone"""
    print("Creating Visualization 5: Vaccine Comparison (TDAP vs MEN-C)...")

    # Load vaccine summary
    vaccine_df = pd.read_csv(f"{OUTPUT_DIR}/vaccine_summary.csv")

    # Load zone-vaccine matrix for zone breakdown
    matrix_df = pd.read_csv(f"{OUTPUT_DIR}/zone_vaccine_matrix.csv", index_col=0)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    # --- Left Panel: Provincial Summary ---
    vaccines = vaccine_df['Vaccine'].tolist()
    coverage = vaccine_df['Overall_Coverage'].values * 100
    eligible = vaccine_df['# Eligible_sum'].values

    # Bar colors
    bar_colors = [COLORS['secondary'], COLORS['primary']]

    bars = ax1.bar(vaccines, coverage, color=bar_colors, edgecolor='white', linewidth=2, width=0.6)

    # Add value labels
    for bar, cov, elig in zip(bars, coverage, eligible):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{cov:.1f}%', ha='center', va='bottom', fontsize=14, fontweight='bold')
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height()/2,
                f'n={elig:,}', ha='center', va='center', fontsize=10, color='white')

    # Reference line
    ax1.axhline(y=95, color=COLORS['target'], linestyle='--', linewidth=2, label='95% Target')

    # Gap annotations
    for bar, cov in zip(bars, coverage):
        gap = 95 - cov
        ax1.annotate(f'Gap: {gap:.1f}%', xy=(bar.get_x() + bar.get_width()/2, 95),
                    xytext=(bar.get_x() + bar.get_width()/2, 97),
                    ha='center', fontsize=10, color=COLORS['target'],
                    arrowprops=dict(arrowstyle='->', color=COLORS['target'], lw=1.5))

    ax1.set_ylabel('Coverage (%)', fontsize=12)
    ax1.set_title('Provincial Coverage: TDAP vs MEN-C-ACYW-135\n(School-Based Immunization Program)',
                 fontsize=12, fontweight='bold')
    ax1.set_ylim(0, 105)
    ax1.legend(loc='lower right', fontsize=10)

    # --- Right Panel: Zone Breakdown ---
    zones = matrix_df.index.tolist()
    x = np.arange(len(zones))
    width = 0.35

    # Get TDAP and MEN-C data by zone
    tdap_by_zone = matrix_df['TDAP'].values * 100 if 'TDAP' in matrix_df.columns else np.zeros(len(zones))
    menc_by_zone = matrix_df['MEN-C-ACYW-135'].values * 100 if 'MEN-C-ACYW-135' in matrix_df.columns else np.zeros(len(zones))

    bars1 = ax2.bar(x - width/2, menc_by_zone, width, label='MEN-C-ACYW-135',
                   color=COLORS['secondary'], edgecolor='white', linewidth=2)
    bars2 = ax2.bar(x + width/2, tdap_by_zone, width, label='TDAP',
                   color=COLORS['primary'], edgecolor='white', linewidth=2)

    # Add value labels
    for bar in bars1:
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{bar.get_height():.1f}%', ha='center', va='bottom', fontsize=9, fontweight='bold')
    for bar in bars2:
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{bar.get_height():.1f}%', ha='center', va='bottom', fontsize=9, fontweight='bold')

    # Reference line
    ax2.axhline(y=95, color=COLORS['target'], linestyle='--', linewidth=2, label='95% Target')

    ax2.set_xlabel('Health Zone', fontsize=12)
    ax2.set_ylabel('Coverage (%)', fontsize=12)
    ax2.set_title('Coverage by Health Zone\n(2021-22 School Year)',
                 fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels(zones, fontsize=10)
    ax2.set_ylim(0, 105)
    ax2.legend(loc='lower right', fontsize=10)

    # Add insight box
    menc_avg = menc_by_zone.mean()
    tdap_avg = tdap_by_zone.mean()
    best_performer = 'MEN-C-ACYW-135' if menc_avg > tdap_avg else 'TDAP'
    textstr = f'Key Insight:\n{best_performer} has higher\naverage coverage\n({max(menc_avg, tdap_avg):.1f}% vs {min(menc_avg, tdap_avg):.1f}%)'
    props = dict(boxstyle='round', facecolor='#D5F5E3', alpha=0.8, edgecolor=COLORS['at_target'])
    ax2.text(0.02, 0.98, textstr, transform=ax2.transAxes, fontsize=9,
            verticalalignment='top', horizontalalignment='left', bbox=props)

    plt.tight_layout()
    plt.savefig(f"{VIZ_DIR}/viz5_vaccine_comparison.png", dpi=150, bbox_inches='tight')
    plt.close()
    print("   Saved: viz5_vaccine_comparison.png")

def create_dashboard_summary():
    """Create a combined dashboard view"""
    print("Creating Dashboard Summary...")

    fig = plt.figure(figsize=(20, 14))

    # Add title
    fig.suptitle('Nova Scotia Childhood Immunization Decision Support Dashboard\n'
                 'Supporting the PHMU vs. Pharmacy-Led Program Decision',
                 fontsize=16, fontweight='bold', y=0.98)

    # Load data
    temporal = pd.read_csv(f"{OUTPUT_DIR}/temporal_analysis.csv")
    zones = pd.read_csv(f"{OUTPUT_DIR}/zone_summary.csv").sort_values('Overall_Coverage')
    matrix = pd.read_csv(f"{OUTPUT_DIR}/zone_vaccine_matrix.csv", index_col=0)
    gaps = pd.read_csv(f"{OUTPUT_DIR}/gap_analysis.csv").head(10)

    # --- Subplot 1: Temporal Trend ---
    ax1 = fig.add_subplot(2, 2, 1)
    years = temporal['Year_Start']
    coverage = temporal['Overall_Coverage'] * 100
    ax1.plot(years, coverage, marker='o', markersize=8, linewidth=2, color=COLORS['primary'])
    ax1.axhline(y=95, color=COLORS['target'], linestyle='--', linewidth=2)
    ax1.fill_between(years, coverage, 95, where=(coverage < 95), color=COLORS['below_target'], alpha=0.2)
    ax1.set_title('Coverage Trend (2012-2022)', fontweight='bold')
    ax1.set_ylabel('Coverage (%)')
    ax1.set_ylim(70, 100)
    for x, y in zip(years, coverage):
        ax1.annotate(f'{y:.0f}%', (x, y), textcoords="offset points", xytext=(0, 8), ha='center', fontsize=8)

    # --- Subplot 2: Zone Comparison ---
    ax2 = fig.add_subplot(2, 2, 2)
    zone_colors = [COLORS['zones'].get(z, 'gray') for z in zones['Zone']]
    bars = ax2.barh(zones['Zone'], zones['Overall_Coverage'] * 100, color=zone_colors)
    ax2.axvline(x=95, color=COLORS['target'], linestyle='--', linewidth=2)
    ax2.set_title('Coverage by Zone', fontweight='bold')
    ax2.set_xlabel('Coverage (%)')
    ax2.set_xlim(75, 100)
    for bar, cov in zip(bars, zones['Overall_Coverage'] * 100):
        ax2.text(cov + 0.5, bar.get_y() + bar.get_height()/2, f'{cov:.1f}%', va='center', fontsize=9)

    # --- Subplot 3: Heatmap ---
    ax3 = fig.add_subplot(2, 2, 3)
    data = matrix.values * 100
    im = ax3.imshow(data, cmap='RdYlGn', aspect='auto', vmin=70, vmax=95)
    ax3.set_xticks(np.arange(len(matrix.columns)))
    ax3.set_yticks(np.arange(len(matrix.index)))
    ax3.set_xticklabels(matrix.columns, fontsize=9, rotation=45, ha='right')
    ax3.set_yticklabels(matrix.index, fontsize=9)
    for i in range(len(matrix.index)):
        for j in range(len(matrix.columns)):
            ax3.text(j, i, f'{data[i,j]:.0f}%', ha='center', va='center',
                    color='white' if data[i,j] < 80 else 'black', fontsize=9)
    ax3.set_title('Zone × Vaccine Matrix', fontweight='bold')

    # --- Subplot 4: Gap Priority ---
    ax4 = fig.add_subplot(2, 2, 4)
    for zone in gaps['Zone'].unique():
        zone_data = gaps[gaps['Zone'] == zone]
        ax4.scatter(zone_data['Gap_From_Target'] * 100, zone_data['# Unvaccinated'],
                   s=zone_data['# Eligible']/80, c=COLORS['zones'].get(zone, 'gray'),
                   alpha=0.7, label=zone, edgecolors='white', linewidth=1)
    ax4.axvline(x=15, color='gray', linestyle=':', alpha=0.5)
    ax4.axhline(y=2000, color='gray', linestyle=':', alpha=0.5)
    ax4.set_xlabel('Gap from 95% Target (%)')
    ax4.set_ylabel('Unvaccinated Children')
    ax4.set_title('Priority Matrix: Gap vs Impact', fontweight='bold')
    ax4.legend(fontsize=8, loc='upper right')

    # Add key metrics box
    fig.text(0.5, 0.02,
             'Key Metrics: Provincial Coverage = 83.9% | Gap from Target = 11.1% | Priority Zone = EASTERN | Key Vaccines: TDAP (89.2%), MEN-C (91.2%)',
             ha='center', fontsize=11, style='italic',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    plt.tight_layout(rect=[0, 0.04, 1, 0.95])
    plt.savefig(f"{VIZ_DIR}/dashboard_summary.png", dpi=150, bbox_inches='tight')
    plt.close()
    print("   Saved: dashboard_summary.png")

def main():
    print("=" * 60)
    print("Creating Visualizations for Analysis Report")
    print("=" * 60)

    # Create output directory
    os.makedirs(VIZ_DIR, exist_ok=True)

    # Set up styling
    setup_style()

    # Create all visualizations
    viz1_temporal_trend()
    viz2_zone_comparison()
    viz3_heatmap()
    viz4_gap_priority()
    viz5_vaccine_comparison()
    create_dashboard_summary()

    print("\n" + "=" * 60)
    print(f"All visualizations saved to: {VIZ_DIR}")
    print("=" * 60)

    # List created files
    print("\nFiles created:")
    for f in os.listdir(VIZ_DIR):
        print(f"  - {f}")

if __name__ == "__main__":
    main()
