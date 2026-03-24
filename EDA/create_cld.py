"""
Causal Loop Diagram (CLD) for Nova Scotia Childhood Immunization Decision
Supports the PHMU vs Pharmacy-Led Program Decision Analysis
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Configuration
VIZ_DIR = r"C:\Users\Adithya JR\Desktop\Childhood-Immunization-Decision-NS\visualizations"

def create_cld():
    """Create a Causal Loop Diagram for the immunization decision system"""

    fig, ax = plt.subplots(figsize=(18, 14))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')
    ax.axis('off')

    # Title
    ax.text(50, 97, 'Causal Loop Diagram: Nova Scotia Childhood Immunization System',
            fontsize=16, fontweight='bold', ha='center', va='top')
    ax.text(50, 93, 'Decision Context: PHMU vs Pharmacy-Led Pediatric Vaccine Program',
            fontsize=12, ha='center', va='top', style='italic', color='gray')

    # Define variables with positions (x, y)
    # Core system variables
    variables = {
        # Primary Care Gap (top)
        'Family Doctor\nVacancy Rate': (50, 82),
        'Unattached\nPediatric Population': (75, 70),

        # Access & Coverage (middle)
        'Vaccine\nAccessibility': (50, 55),
        'Immunization\nCoverage Rate': (50, 38),

        # Outcomes (bottom left)
        'Disease\nOutbreak Risk': (25, 25),
        'Public Health\nWorkload': (25, 45),

        # Behavioral factors (right)
        'Parent Trust &\nAwareness': (75, 38),
        'Multi-dose\nCompletion Rate': (75, 55),

        # Geographic factors (left)
        'Rural/Remote\nAccess Barriers': (25, 70),
        'Zone Coverage\nDisparity': (25, 55),

        # INTERVENTION POINTS (highlighted)
        'PHMU\nCapacity': (15, 82),
        'Pharmacy Program\nCapacity': (85, 82),
    }

    # Variable colors
    core_color = '#3498DB'      # Blue - core system
    outcome_color = '#E74C3C'   # Red - outcomes/risks
    behavior_color = '#27AE60'  # Green - behavioral
    barrier_color = '#F39C12'   # Orange - barriers
    intervention_color = '#9B59B6'  # Purple - interventions

    var_colors = {
        'Family Doctor\nVacancy Rate': barrier_color,
        'Unattached\nPediatric Population': barrier_color,
        'Vaccine\nAccessibility': core_color,
        'Immunization\nCoverage Rate': core_color,
        'Disease\nOutbreak Risk': outcome_color,
        'Public Health\nWorkload': outcome_color,
        'Parent Trust &\nAwareness': behavior_color,
        'Multi-dose\nCompletion Rate': behavior_color,
        'Rural/Remote\nAccess Barriers': barrier_color,
        'Zone Coverage\nDisparity': outcome_color,
        'PHMU\nCapacity': intervention_color,
        'Pharmacy Program\nCapacity': intervention_color,
    }

    # Draw variable boxes
    for var, (x, y) in variables.items():
        color = var_colors[var]
        is_intervention = 'PHMU' in var or 'Pharmacy' in var

        # Box styling
        box_width = 14 if is_intervention else 12
        box_height = 6

        bbox = FancyBboxPatch(
            (x - box_width/2, y - box_height/2),
            box_width, box_height,
            boxstyle="round,pad=0.02,rounding_size=0.5",
            facecolor=color if is_intervention else 'white',
            edgecolor=color,
            linewidth=3 if is_intervention else 2,
            alpha=0.9
        )
        ax.add_patch(bbox)

        # Text
        text_color = 'white' if is_intervention else 'black'
        fontweight = 'bold' if is_intervention else 'normal'
        ax.text(x, y, var, fontsize=9, ha='center', va='center',
                fontweight=fontweight, color=text_color)

    # Define causal links: (from, to, polarity, curve_direction, evidence_id)
    # curve_direction: 0=straight, positive=curve right, negative=curve left
    links = [
        # Core causal chain
        ('Family Doctor\nVacancy Rate', 'Unattached\nPediatric Population', '+', 0.2, 1),
        ('Unattached\nPediatric Population', 'Vaccine\nAccessibility', '-', 0.2, 2),
        ('Vaccine\nAccessibility', 'Immunization\nCoverage Rate', '+', 0, 3),
        ('Immunization\nCoverage Rate', 'Disease\nOutbreak Risk', '-', -0.3, None),
        ('Disease\nOutbreak Risk', 'Public Health\nWorkload', '+', 0, None),
        ('Public Health\nWorkload', 'Family Doctor\nVacancy Rate', '+', -0.3, None),  # R1 loop

        # Behavioral feedback loop
        ('Immunization\nCoverage Rate', 'Parent Trust &\nAwareness', '+', 0.2, None),
        ('Parent Trust &\nAwareness', 'Multi-dose\nCompletion Rate', '+', 0.2, None),
        ('Multi-dose\nCompletion Rate', 'Immunization\nCoverage Rate', '+', 0.3, 4),  # R2 loop

        # Geographic factors
        ('Rural/Remote\nAccess Barriers', 'Vaccine\nAccessibility', '-', -0.2, None),
        ('Vaccine\nAccessibility', 'Zone Coverage\nDisparity', '-', -0.2, 5),
        ('Zone Coverage\nDisparity', 'Disease\nOutbreak Risk', '+', 0, None),

        # INTERVENTION LINKS (key decision points)
        ('PHMU\nCapacity', 'Rural/Remote\nAccess Barriers', '-', 0.3, None),
        ('PHMU\nCapacity', 'Vaccine\nAccessibility', '+', 0.4, None),
        ('Pharmacy Program\nCapacity', 'Vaccine\nAccessibility', '+', -0.4, None),
        ('Pharmacy Program\nCapacity', 'Multi-dose\nCompletion Rate', '+', 0.2, None),
    ]

    # Draw arrows
    def draw_curved_arrow(ax, start, end, polarity, curve, evidence_id=None):
        x1, y1 = variables[start]
        x2, y2 = variables[end]

        # Adjust start/end points to box edges
        dx = x2 - x1
        dy = y2 - y1
        dist = np.sqrt(dx**2 + dy**2)

        # Start point adjustment
        x1_adj = x1 + (dx/dist) * 6
        y1_adj = y1 + (dy/dist) * 3

        # End point adjustment
        x2_adj = x2 - (dx/dist) * 6
        y2_adj = y2 - (dy/dist) * 3

        # Arrow color based on polarity
        color = '#27AE60' if polarity == '+' else '#E74C3C'

        # Determine if this is an intervention link
        is_intervention_link = 'PHMU' in start or 'Pharmacy' in start
        linewidth = 2.5 if is_intervention_link else 1.5
        linestyle = '-' if is_intervention_link else '-'

        # Connection style
        if abs(curve) > 0.1:
            conn_style = f"arc3,rad={curve}"
        else:
            conn_style = "arc3,rad=0"

        arrow = FancyArrowPatch(
            (x1_adj, y1_adj), (x2_adj, y2_adj),
            connectionstyle=conn_style,
            arrowstyle='-|>',
            mutation_scale=15,
            color=color,
            linewidth=linewidth,
            linestyle=linestyle
        )
        ax.add_patch(arrow)

        # Add polarity label
        mid_x = (x1_adj + x2_adj) / 2 + curve * 8
        mid_y = (y1_adj + y2_adj) / 2 + curve * 5

        ax.text(mid_x, mid_y, polarity, fontsize=12, fontweight='bold',
                color=color, ha='center', va='center',
                bbox=dict(boxstyle='circle', facecolor='white', edgecolor=color, linewidth=1))

        # Add evidence marker if applicable
        if evidence_id:
            ax.text(mid_x + 2, mid_y + 2, f'E{evidence_id}', fontsize=8,
                   color='purple', fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor='#F5EEF8', edgecolor='purple', linewidth=1))

    # Draw all links
    for link in links:
        draw_curved_arrow(ax, link[0], link[1], link[2], link[3], link[4])

    # Add feedback loop labels
    # R1: Vicious cycle of healthcare strain
    ax.annotate('R1', xy=(30, 62), fontsize=14, fontweight='bold', color='#8E44AD',
               bbox=dict(boxstyle='circle,pad=0.3', facecolor='#F5EEF8', edgecolor='#8E44AD', linewidth=2))
    ax.text(30, 58, 'Healthcare\nStrain Cycle', fontsize=8, ha='center', color='#8E44AD')

    # R2: Confidence-completion cycle
    ax.annotate('R2', xy=(68, 45), fontsize=14, fontweight='bold', color='#8E44AD',
               bbox=dict(boxstyle='circle,pad=0.3', facecolor='#F5EEF8', edgecolor='#8E44AD', linewidth=2))
    ax.text(68, 41, 'Trust-Completion\nCycle', fontsize=8, ha='center', color='#8E44AD')

    # Legend
    legend_y = 12
    ax.text(5, legend_y + 5, 'Legend:', fontsize=11, fontweight='bold')

    # Variable type legend
    legend_items = [
        (intervention_color, 'Intervention Points (Decision Variables)'),
        (core_color, 'Core System Variables'),
        (behavior_color, 'Behavioral Factors'),
        (barrier_color, 'Access Barriers'),
        (outcome_color, 'Outcomes/Risks'),
    ]

    for i, (color, label) in enumerate(legend_items):
        ax.add_patch(plt.Rectangle((5, legend_y - i*2.5), 2, 1.5, facecolor=color, edgecolor='black'))
        ax.text(8, legend_y - i*2.5 + 0.75, label, fontsize=9, va='center')

    # Arrow legend
    ax.text(45, legend_y + 5, 'Causal Links:', fontsize=11, fontweight='bold')

    # Positive link
    ax.annotate('', xy=(52, legend_y + 2), xytext=(45, legend_y + 2),
               arrowprops=dict(arrowstyle='-|>', color='#27AE60', lw=2))
    ax.text(45, legend_y + 3.5, '+', fontsize=10, color='#27AE60', fontweight='bold')
    ax.text(53, legend_y + 2, 'Positive (same direction)', fontsize=9, va='center')

    # Negative link
    ax.annotate('', xy=(52, legend_y - 1), xytext=(45, legend_y - 1),
               arrowprops=dict(arrowstyle='-|>', color='#E74C3C', lw=2))
    ax.text(45, legend_y + 0.5, '-', fontsize=10, color='#E74C3C', fontweight='bold')
    ax.text(53, legend_y - 1, 'Negative (opposite direction)', fontsize=9, va='center')

    # Evidence markers
    ax.text(45, legend_y - 4, 'E#', fontsize=9, color='purple', fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='#F5EEF8', edgecolor='purple'))
    ax.text(49, legend_y - 4, '= Evidence-supported link (see table below)', fontsize=9, va='center')

    # Feedback loop legend
    ax.text(45, legend_y - 7, 'R#', fontsize=10, color='#8E44AD', fontweight='bold',
           bbox=dict(boxstyle='circle,pad=0.2', facecolor='#F5EEF8', edgecolor='#8E44AD'))
    ax.text(49, legend_y - 7, '= Reinforcing feedback loop', fontsize=9, va='center')

    plt.tight_layout()
    plt.savefig(f"{VIZ_DIR}/cld_immunization_system.png", dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("CLD diagram saved: cld_immunization_system.png")


def create_evidence_table():
    """Create evidence table supporting the CLD causal links"""

    fig, ax = plt.subplots(figsize=(16, 10))
    ax.axis('off')

    # Title
    ax.text(0.5, 0.98, 'Evidence Supporting Causal Loop Diagram Links',
            fontsize=16, fontweight='bold', ha='center', va='top', transform=ax.transAxes)

    ax.text(0.5, 0.93, 'Nova Scotia Childhood Immunization Decision Analysis',
            fontsize=12, ha='center', va='top', style='italic', color='gray', transform=ax.transAxes)

    # Evidence table data
    evidence = [
        ['E1', 'Family Doctor Vacancy\n→ Unattached Pediatric Pop (+)',
         'Nova Scotia has 66,768 people on the Need a Family\n'
         'Practice Registry. As physician vacancies increase,\n'
         'more children become "unattached" to primary care.',
         'Background.md:\n"66,768 people in Nova\n'
         'Scotia are without primary\ncare providers"'],

        ['E2', 'Unattached Population\n→ Vaccine Accessibility (-)',
         'Children without a family doctor have reduced access\n'
         'to routine vaccination services, requiring alternative\n'
         'delivery models (school-based, pharmacy, mobile units).',
         'Analysis shows Eastern Zone\n'
         'has lowest coverage (83.3%)\n'
         'correlating with rural access\nbarriers'],

        ['E3', 'Vaccine Accessibility\n→ Immunization Coverage (+)',
         'School-based immunization program data shows direct\n'
         'relationship: zones with better accessibility (Northern)\n'
         'achieve higher coverage rates.',
         'Zone Analysis:\n'
         'Northern: 88.3% (best access)\n'
         'Eastern: 83.3% (worst access)\n'
         'Correlation visible in heatmap'],

        ['E4', 'Multi-dose Completion\n→ Coverage Rate (+)',
         'Data shows significant dropout between doses:\n'
         'MEN-C-ACYW-135: 91.2% coverage\n'
         'TDAP: 89.2% coverage\n'
         'Single-dose vaccines outperform multi-dose series.',
         'Vaccine Summary:\n'
         'Provincial data shows\n'
         'single-dose vaccines achieve\n'
         '~3-6% higher coverage'],

        ['E5', 'Vaccine Accessibility\n→ Zone Coverage Disparity (-)',
         'Geographic analysis reveals persistent disparities:\n'
         'Eastern Zone consistently underperforms across all\n'
         'vaccine types (73-84% vs 83-93% in Central).',
         'Zone-Vaccine Matrix:\n'
         'Eastern Zone has 6 cells\n'
         'below 85% threshold\n'
         '(see viz3_heatmap.png)'],
    ]

    # Table styling
    col_widths = [0.06, 0.22, 0.42, 0.25]
    row_height = 0.14
    start_y = 0.85

    # Header
    headers = ['ID', 'Causal Link', 'Evidence Description', 'Data Source']
    header_colors = ['#2C3E50', '#2C3E50', '#2C3E50', '#2C3E50']

    x_pos = 0.02
    for i, (header, width) in enumerate(zip(headers, col_widths)):
        rect = plt.Rectangle((x_pos, start_y), width, 0.05,
                             facecolor='#2C3E50', edgecolor='black', linewidth=1,
                             transform=ax.transAxes, clip_on=False)
        ax.add_patch(rect)
        ax.text(x_pos + width/2, start_y + 0.025, header,
               fontsize=11, fontweight='bold', color='white',
               ha='center', va='center', transform=ax.transAxes)
        x_pos += width + 0.01

    # Data rows
    row_colors = ['#F8F9FA', '#FFFFFF']
    for row_idx, row_data in enumerate(evidence):
        y_pos = start_y - (row_idx + 1) * row_height
        x_pos = 0.02

        bg_color = row_colors[row_idx % 2]

        for col_idx, (cell, width) in enumerate(zip(row_data, col_widths)):
            rect = plt.Rectangle((x_pos, y_pos), width, row_height - 0.01,
                                 facecolor=bg_color, edgecolor='#BDC3C7', linewidth=0.5,
                                 transform=ax.transAxes, clip_on=False)
            ax.add_patch(rect)

            # Special formatting for ID column
            if col_idx == 0:
                ax.text(x_pos + width/2, y_pos + row_height/2, cell,
                       fontsize=11, fontweight='bold', color='#8E44AD',
                       ha='center', va='center', transform=ax.transAxes)
            else:
                ax.text(x_pos + 0.01, y_pos + row_height/2, cell,
                       fontsize=9, ha='left', va='center', transform=ax.transAxes,
                       linespacing=1.2)

            x_pos += width + 0.01

    # Key insights box
    insights_y = 0.12
    insights_box = plt.Rectangle((0.02, insights_y - 0.08), 0.96, 0.12,
                                  facecolor='#FEF9E7', edgecolor='#F39C12', linewidth=2,
                                  transform=ax.transAxes, clip_on=False)
    ax.add_patch(insights_box)

    ax.text(0.5, insights_y + 0.02, 'Key System Insights from CLD Analysis',
           fontsize=12, fontweight='bold', ha='center', transform=ax.transAxes)

    insights_text = (
        "1. R1 (Healthcare Strain Cycle): Physician shortages → unattached patients → reduced coverage → "
        "disease risk → more public health burden → more physician burnout. This reinforcing loop explains "
        "why coverage remains stuck below 95%.\n\n"
        "2. R2 (Trust-Completion Cycle): Higher coverage → more parent confidence → better multi-dose completion "
        "→ even higher coverage. Interventions should leverage this positive feedback.\n\n"
        "3. Intervention Leverage Points: Both PHMU and Pharmacy programs directly increase vaccine accessibility, "
        "but they target different barriers. PHMUs address rural/remote access; Pharmacies improve urban convenience "
        "and multi-dose follow-up."
    )

    ax.text(0.5, insights_y - 0.03, insights_text, fontsize=9,
           ha='center', va='top', transform=ax.transAxes,
           wrap=True, linespacing=1.3,
           bbox=dict(facecolor='none', edgecolor='none'))

    plt.tight_layout()
    plt.savefig(f"{VIZ_DIR}/cld_evidence_table.png", dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("Evidence table saved: cld_evidence_table.png")


def main():
    print("=" * 60)
    print("Creating Causal Loop Diagram and Evidence Table")
    print("=" * 60)

    create_cld()
    create_evidence_table()

    print("\n" + "=" * 60)
    print("CLD generation complete!")
    print("Files created:")
    print("  - cld_immunization_system.png")
    print("  - cld_evidence_table.png")
    print("=" * 60)


if __name__ == "__main__":
    main()
