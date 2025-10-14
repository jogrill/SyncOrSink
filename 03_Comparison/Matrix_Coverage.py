import pandas as pd
import numpy as np

list_ATTACK_tactics = ["reconnaissance", "resource-development", "initial-access", "execution", "persistence", "privilege-escalation", "defense-evasion", "credential-access", "discovery", "lateral-movement", "collection", "command-and-control", "exfiltration", "impact"]
list_D3fend_tactics = ["Model", "Harden", "Detect", "Isolate", "Deceive", "Evict", "Restore"]


def coverage_matrix():

    for attack_tactic in list_ATTACK_tactics:

        df_tactic = df_results[df_results["Attack_tactics"].apply(lambda x: attack_tactic in x)]

        coverage_total = 0
        for tactic_name_D3fend, tactic_data_D3fend in df_tactic.items():

            if tactic_name_D3fend not in list_D3fend_tactics:
                continue

            tactic_data_D3fend = tactic_data_D3fend.dropna()

            #count_not_covered = (tactic_data_D3fend == 0).sum()
            count_not_covered_half = (tactic_data_D3fend < 0.5).sum()
            #count_not_covered_full = (tactic_data_D3fend < 1.0).sum()

            if len(tactic_data_D3fend) > 0:
                coverage_attack_tactic = 1 - (count_not_covered_half / len(tactic_data_D3fend))
            else:
                coverage_attack_tactic = np.nan
            print(f"Tactic: {tactic_name_D3fend}: {coverage_attack_tactic}")

            if coverage_attack_tactic is not np.nan:
                coverage_total += coverage_attack_tactic
        coverage_total_avg = coverage_total / 7
        print(f"Total Coverage: {coverage_total_avg}")
        print("-----------------------------")


df_results = pd.read_csv("Files/results_complete_v17_COSE.csv")
pd.set_option("display.max_columns", None)
coverage_matrix()
