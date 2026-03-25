"""
Shifting the Burden Archetype Diagram
Mapped to Nova Scotia Childhood Immunization Context
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

# Configuration
IMG_DIR = r"C:\Users\Adithya JR\Desktop\Childhood-Immunization-Decision-NS\img"

def create_archetype_diagram():
    """Create the Shifting the Burden archetype diagram"""

    fig, ax = plt.subplots(figsize=(16, 12))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Colors
    COLORS = {
        'problem': '#E74C3C',      # Red
        'symptomatic': '#F39C12',  # Orange
        'fundamental': '#27AE60',  # Green
        'side_effect': '#9B59B6',  # Purple
        'delay': '#3498DB',        # Blue
        'arrow_neg': '#E74C3C',    # Red for negative
        'arrow_pos': '#27AE60',    # Green for positive
        'loop': '#8E44AD',         # Purple for loops
    }

    # Title
    ax.text(50, 96, 'SHIFTING THE BURDEN ARCHETYPE', fontsize=18, fontweight='bold',
            ha='center', va='top', color='#2C3E50')
    ax.text(50, 92, 'Applied to Nova Scotia Childhood Immunization Decision',
            fontsize=14, ha='center', va='top', style='italic', color='#7F8C8D')

    # ========== PROBLEM SYMPTOM (Top Center) ==========
    problem_box = FancyBboxPatch((35, 72), 30, 12,
                                  boxstyle="round,pad=0.02,rounding_size=1",
                                  facecolor=COLORS['problem'], edgecolor='#C0392B',
                                  linewidth=3, alpha=0.9)
    ax.add_patch(problem_box)
    ax.text(50, 78, 'PROBLEM SYMPTOM', fontsize=11, fontweight='bold',
            ha='center', va='center', color='white')
    ax.text(50, 75, 'Low Immunization Coverage', fontsize=10,
            ha='center', va='center', color='white')
    ax.text(50, 72.5, '(83.9% vs 95% Target)', fontsize=9,
            ha='center', va='center', color='white', style='italic')

    # ========== SYMPTOMATIC SOLUTION (Left) ==========
    symp_box = FancyBboxPatch((8, 42), 28, 18,
                               boxstyle="round,pad=0.02,rounding_size=1",
                               facecolor=COLORS['symptomatic'], edgecolor='#D68910',
                               linewidth=3, alpha=0.9)
    ax.add_patch(symp_box)
    ax.text(22, 57, 'SYMPTOMATIC SOLUTION', fontsize=10, fontweight='bold',
            ha='center', va='center', color='white')
    ax.text(22, 53, '(Quick Fix)', fontsize=9, ha='center', va='center',
            color='white', style='italic')
    ax.text(22, 49, '• PHMU Expansion', fontsize=9, ha='center', va='center', color='white')
    ax.text(22, 46, '• Pharmacy-Led Program', fontsize=9, ha='center', va='center', color='white')
    ax.text(22, 43, 'Bypass primary care system', fontsize=8,
            ha='center', va='center', color='white', style='italic')

    # ========== FUNDAMENTAL SOLUTION (Right) ==========
    fund_box = FancyBboxPatch((64, 42), 28, 18,
                               boxstyle="round,pad=0.02,rounding_size=1",
                               facecolor=COLORS['fundamental'], edgecolor='#1E8449',
                               linewidth=3, alpha=0.9)
    ax.add_patch(fund_box)
    ax.text(78, 57, 'FUNDAMENTAL SOLUTION', fontsize=10, fontweight='bold',
            ha='center', va='center', color='white')
    ax.text(78, 53, '(Root Cause Fix)', fontsize=9, ha='center', va='center',
            color='white', style='italic')
    ax.text(78, 49, '• Recruit family doctors', fontsize=9, ha='center', va='center', color='white')
    ax.text(78, 46, '• Train more NPs', fontsize=9, ha='center', va='center', color='white')
    ax.text(78, 43, '• Address burnout/retention', fontsize=8,
            ha='center', va='center', color='white', style='italic')

    # ========== SIDE EFFECT (Bottom Center) ==========
    side_box = FancyBboxPatch((35, 15), 30, 12,
                               boxstyle="round,pad=0.02,rounding_size=1",
                               facecolor=COLORS['side_effect'], edgecolor='#7D3C98',
                               linewidth=3, alpha=0.9)
    ax.add_patch(side_box)
    ax.text(50, 24, 'SIDE EFFECT', fontsize=10, fontweight='bold',
            ha='center', va='center', color='white')
    ax.text(50, 21, 'Reduced urgency to fix', fontsize=9,
            ha='center', va='center', color='white')
    ax.text(50, 18, 'primary care shortage', fontsize=9,
            ha='center', va='center', color='white')
    ax.text(50, 15.5, '(Addiction to workaround)', fontsize=8,
            ha='center', va='center', color='white', style='italic')

    # ========== DELAY BOX (Right side) ==========
    delay_box = FancyBboxPatch((75, 28), 18, 8,
                                boxstyle="round,pad=0.02,rounding_size=0.5",
                                facecolor=COLORS['delay'], edgecolor='#2874A6',
                                linewidth=2, alpha=0.8)
    ax.add_patch(delay_box)
    ax.text(84, 33, 'DELAY', fontsize=9, fontweight='bold',
            ha='center', va='center', color='white')
    ax.text(84, 30, '8-12 years to train', fontsize=8,
            ha='center', va='center', color='white')
    ax.text(84, 28.5, 'new physicians', fontsize=8,
            ha='center', va='center', color='white')

    # ========== ARROWS ==========

    # Arrow 1: Problem → Symptomatic (B1 loop)
    arrow1 = FancyArrowPatch((42, 72), (30, 60),
                              connectionstyle="arc3,rad=-0.2",
                              arrowstyle='-|>', mutation_scale=20,
                              color=COLORS['arrow_neg'], linewidth=2.5)
    ax.add_patch(arrow1)
    ax.text(32, 68, 'B1', fontsize=12, fontweight='bold', color=COLORS['loop'],
            bbox=dict(boxstyle='circle,pad=0.3', facecolor='white', edgecolor=COLORS['loop']))
    ax.text(32, 64, '(-)', fontsize=11, fontweight='bold', color=COLORS['arrow_neg'])

    # Arrow 2: Symptomatic → Problem (completing B1)
    arrow2 = FancyArrowPatch((30, 60), (42, 72),
                              connectionstyle="arc3,rad=-0.3",
                              arrowstyle='-|>', mutation_scale=20,
                              color=COLORS['arrow_neg'], linewidth=2.5, linestyle='--')
    ax.add_patch(arrow2)

    # Arrow 3: Problem → Fundamental (B2 loop)
    arrow3 = FancyArrowPatch((58, 72), (70, 60),
                              connectionstyle="arc3,rad=0.2",
                              arrowstyle='-|>', mutation_scale=20,
                              color=COLORS['arrow_neg'], linewidth=2.5)
    ax.add_patch(arrow3)
    ax.text(68, 68, 'B2', fontsize=12, fontweight='bold', color=COLORS['loop'],
            bbox=dict(boxstyle='circle,pad=0.3', facecolor='white', edgecolor=COLORS['loop']))
    ax.text(68, 64, '(-)', fontsize=11, fontweight='bold', color=COLORS['arrow_neg'])

    # Arrow 4: Fundamental → Problem (completing B2)
    arrow4 = FancyArrowPatch((70, 60), (58, 72),
                              connectionstyle="arc3,rad=0.3",
                              arrowstyle='-|>', mutation_scale=20,
                              color=COLORS['arrow_neg'], linewidth=2.5, linestyle='--')
    ax.add_patch(arrow4)

    # Arrow 5: Symptomatic → Side Effect
    arrow5 = FancyArrowPatch((22, 42), (40, 27),
                              connectionstyle="arc3,rad=0.2",
                              arrowstyle='-|>', mutation_scale=15,
                              color=COLORS['side_effect'], linewidth=2)
    ax.add_patch(arrow5)
    ax.text(28, 33, '(+)', fontsize=10, fontweight='bold', color=COLORS['side_effect'])

    # Arrow 6: Side Effect → Fundamental (weakening)
    arrow6 = FancyArrowPatch((60, 21), (75, 32),
                              connectionstyle="arc3,rad=-0.1",
                              arrowstyle='-|>', mutation_scale=15,
                              color=COLORS['arrow_neg'], linewidth=2)
    ax.add_patch(arrow6)
    ax.text(70, 25, '(-)', fontsize=10, fontweight='bold', color=COLORS['arrow_neg'])

    # Arrow 7: Delay indicator
    arrow7 = FancyArrowPatch((84, 36), (78, 42),
                              connectionstyle="arc3,rad=0",
                              arrowstyle='-|>', mutation_scale=12,
                              color=COLORS['delay'], linewidth=2)
    ax.add_patch(arrow7)

    # ========== LEGEND ==========
    legend_y = 8
    ax.text(5, legend_y, 'Legend:', fontsize=10, fontweight='bold')

    # Loop indicators
    ax.text(5, legend_y - 3, 'B1, B2 = Balancing Feedback Loops', fontsize=9)
    ax.text(5, legend_y - 5.5, '(+) = Same direction change', fontsize=9, color=COLORS['side_effect'])
    ax.text(5, legend_y - 8, '(-) = Opposite direction change', fontsize=9, color=COLORS['arrow_neg'])

    # Key insight box
    insight_box = FancyBboxPatch((45, 2), 52, 10,
                                  boxstyle="round,pad=0.02,rounding_size=0.5",
                                  facecolor='#FEF9E7', edgecolor='#F39C12',
                                  linewidth=2, alpha=0.9)
    ax.add_patch(insight_box)
    ax.text(71, 10, 'KEY INSIGHT FOR DECISION', fontsize=10, fontweight='bold',
            ha='center', va='center', color='#9A7D0A')
    ax.text(71, 7, 'Both PHMU and Pharmacy options are symptomatic solutions.', fontsize=9,
            ha='center', va='center', color='#7D6608')
    ax.text(71, 4.5, 'Choose the one that is most sustainable while the fundamental', fontsize=9,
            ha='center', va='center', color='#7D6608')
    ax.text(71, 2.5, 'solution (primary care access) is addressed in parallel.', fontsize=9,
            ha='center', va='center', color='#7D6608')

    plt.tight_layout()
    plt.savefig(f"{IMG_DIR}/archetype_shifting_burden.png", dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("Archetype diagram saved: archetype_shifting_burden.png")


def create_scenario_comparison_diagram():
    """Create a visual comparison of the three scenarios"""

    fig, axes = plt.subplots(1, 3, figsize=(18, 8))

    scenarios = [
        {
            'name': 'Status Quo',
            'subtitle': '"The Slow Decline"',
            'color': '#E74C3C',
            'coverage': 78,
            'eastern': 75,
            'completion': 68,
            'risk': 'HIGH',
            'risk_color': '#C0392B',
            'investment': '$0',
            'icon': 'A'
        },
        {
            'name': 'PHMU Expansion',
            'subtitle': '"The Mobile Solution"',
            'color': '#F39C12',
            'coverage': 88,
            'eastern': 89,
            'completion': 76,
            'risk': 'MODERATE',
            'risk_color': '#D68910',
            'investment': '~$8.5M',
            'icon': 'B'
        },
        {
            'name': 'Pharmacy Program',
            'subtitle': '"The Community Network"',
            'color': '#27AE60',
            'coverage': 91,
            'eastern': 87,
            'completion': 85,
            'risk': 'LOW',
            'risk_color': '#1E8449',
            'investment': '~$3.2M',
            'icon': 'C'
        }
    ]

    for ax, scenario in zip(axes, scenarios):
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.axis('off')

        # Background
        ax.add_patch(plt.Rectangle((0, 0), 100, 100, facecolor=scenario['color'], alpha=0.1))

        # Title
        ax.text(50, 95, f"{scenario['icon']} {scenario['name']}", fontsize=16, fontweight='bold',
                ha='center', va='top', color=scenario['color'])
        ax.text(50, 88, scenario['subtitle'], fontsize=12, ha='center', va='top',
                style='italic', color='#7F8C8D')

        # Metrics
        metrics_y = 75
        ax.text(50, metrics_y, 'PROJECTED 2031 METRICS', fontsize=11, fontweight='bold',
                ha='center', va='center', color='#2C3E50')

        # Coverage bar
        ax.add_patch(plt.Rectangle((15, 60), 70, 8, facecolor='#ECF0F1', edgecolor='#BDC3C7'))
        ax.add_patch(plt.Rectangle((15, 60), scenario['coverage'] * 0.7, 8,
                                    facecolor=scenario['color'], alpha=0.8))
        ax.axvline(x=15 + 95 * 0.7, color='#C0392B', linestyle='--', linewidth=2, ymin=0.58, ymax=0.72)
        ax.text(10, 64, 'Coverage:', fontsize=9, ha='right', va='center')
        ax.text(88, 64, f"{scenario['coverage']}%", fontsize=11, fontweight='bold',
                ha='left', va='center', color=scenario['color'])

        # Eastern Zone bar
        ax.add_patch(plt.Rectangle((15, 48), 70, 8, facecolor='#ECF0F1', edgecolor='#BDC3C7'))
        ax.add_patch(plt.Rectangle((15, 48), scenario['eastern'] * 0.7, 8,
                                    facecolor=scenario['color'], alpha=0.6))
        ax.text(10, 52, 'Eastern:', fontsize=9, ha='right', va='center')
        ax.text(88, 52, f"{scenario['eastern']}%", fontsize=11, fontweight='bold',
                ha='left', va='center', color=scenario['color'])

        # Completion bar
        ax.add_patch(plt.Rectangle((15, 36), 70, 8, facecolor='#ECF0F1', edgecolor='#BDC3C7'))
        ax.add_patch(plt.Rectangle((15, 36), scenario['completion'] * 0.7, 8,
                                    facecolor=scenario['color'], alpha=0.6))
        ax.text(10, 40, 'Multi-dose:', fontsize=9, ha='right', va='center')
        ax.text(88, 40, f"{scenario['completion']}%", fontsize=11, fontweight='bold',
                ha='left', va='center', color=scenario['color'])

        # Risk and Investment
        ax.text(50, 25, f"Outbreak Risk: {scenario['risk']}", fontsize=12, fontweight='bold',
                ha='center', va='center', color=scenario['risk_color'])
        ax.text(50, 18, f"5-Year Investment: {scenario['investment']}", fontsize=11,
                ha='center', va='center', color='#2C3E50')

        # Bottom assessment
        if scenario['name'] == 'Status Quo':
            assessment = "X Unacceptable"
        elif scenario['name'] == 'PHMU Expansion':
            assessment = "GOOD (Rural Focus)"
        else:
            assessment = "BEST Overall"

        ax.text(50, 8, assessment, fontsize=13, fontweight='bold',
                ha='center', va='center', color=scenario['color'])

    plt.tight_layout()
    plt.savefig(f"{IMG_DIR}/scenario_comparison.png", dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("Scenario comparison saved: scenario_comparison.png")


def main():
    print("=" * 60)
    print("Creating Milestone 3 Diagrams")
    print("=" * 60)

    create_archetype_diagram()
    create_scenario_comparison_diagram()

    print("\n" + "=" * 60)
    print("Diagrams complete!")
    print("Files created:")
    print("  - archetype_shifting_burden.png")
    print("  - scenario_comparison.png")
    print("=" * 60)


if __name__ == "__main__":
    main()
