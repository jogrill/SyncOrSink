import matplotlib.pyplot as plt
import numpy as np

def genereateFigureAttackTactics(list_current, list_target):

    attack_tactics = ["Reconnaissance", "Resource Development", "Initial Access", "Execution", "Persistence", "Privilege Escalation", "Defense Evasion", "Credential Access", "Discovery", "Lateral Movement", "Collection", "Command And Control", "Exfiltration", "Impact"]

    # Bar width and position
    n = len(attack_tactics)
    x = np.arange(n)
    width = 0.35

    # Create diagram
    fig, ax = plt.subplots(figsize=(16, 8))
    bars1 = ax.bar(x - width/2, list_current, width, label="Tactics distribution in CVEs", color=(198/255, 63/255, 31/255, 0.1), edgecolor='black')
    bars2 = ax.bar(x + width/2, list_target, width, label="Tactics distribution in Playbooks", color=(0/255, 91/255, 148/255, 0.1), edgecolor='black')

    # Axis labeling and title
    ax.set_xlabel("MITRE ATT&CK Tactics", fontsize=14)
    ax.set_ylabel("Relative distribution in CVEs and playbooks (in %)", fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(attack_tactics, rotation=60, ha="right", fontsize=14)  # Rotated to 60 degrees for better readability
    ax.tick_params(axis='y', labelsize=14)
    ax.legend(fontsize=14, frameon=False)

    # Display values above the bar
    for bar in bars1:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f'{bar.get_height()}',
            ha='center', va='bottom'
        )

    for bar in bars2:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f'{bar.get_height()}',
            ha='center', va='bottom'
        )

    # Optimize and display layout
    plt.tight_layout()
    fig.savefig("Files/mitre_attack_tactics_comparison_v17_COSE.pdf", format="pdf")
    plt.show()


def genereateFigureD3fendTactics(list_current, list_target):

    d3fend_tactics = ["Model", "Harden", "Detect", "Isolate", "Deceive", "Evict", "Restore"]

    x = np.arange(len(d3fend_tactics))  # Positions of the tactics on the X-axis
    bar_width = 0.35  # Width of the bars

    # Create diagram
    fig, ax = plt.subplots(figsize=(10, 6))
    bars1 = ax.bar(x - bar_width / 2, list_target, bar_width, label='Tactics distribution in CVEs', color=(198/255, 63/255, 31/255, 0.1), edgecolor='black')
    bars2 = ax.bar(x + bar_width / 2, list_current, bar_width, label='Tactics distribution in Playbooks', color=(0/255, 91/255, 148/255, 0.1), edgecolor='black')

    # Axis labels and titles
    ax.set_xlabel("MITRE D3FEND Tactics", fontsize=14)
    ax.set_ylabel("Relative distribution in CVEs and playbooks (in %)", fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(d3fend_tactics, rotation=45, fontsize=16)
    ax.tick_params(axis='y', labelsize=16)
    ax.legend(fontsize=14, frameon=False)

    # Display values above the bar
    for bar in bars1:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f'{bar.get_height()}',
            ha='center', va='bottom'
        )

    for bar in bars2:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f'{bar.get_height()}',
            ha='center', va='bottom'
        )

    plt.tight_layout()
    fig.savefig("Files/mitre_d3fend_tactics_comparison_v17_COSE.pdf", format="pdf")
    plt.show()
