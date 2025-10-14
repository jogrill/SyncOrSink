import json
import ast
import Comparison_Helper as comp_helper
import Comparison_Tactics as comp_tactics
import pandas as pd

df_results = pd.read_csv("Files/results_complete_v17_COSE.csv")

with open("Files/d3fend_to_attack_v17.json", "r") as file:
    list_d3fend_to_attack_mapping = json.load(file)


def calculate_target_d3fend():
    df_attack_to_d3fend = pd.DataFrame(columns=['cve_id', 'Attack_technique', 'Attack_tactics', 'D3FEND_techniques', 'D3FEND_tactics'])

    df_cve = comp_helper.get_CVE_data()
    columns_to_count = ['Model_missing', 'Harden_missing', 'Detect_missing', 'Isolate_missing', 'Deceive_missing', 'Evict_missing', 'Restore_missing', 'Model_covered', 'Harden_covered', 'Detect_covered', 'Isolate_covered', 'Deceive_covered', 'Evict_covered', 'Restore_covered']

    count_techs = 0
    counter = 0
    for row_cve in df_cve.itertuples(index=False):
        attack_technique = row_cve.attack_technique

        row = df_results[df_results['Attack_id'] == attack_technique]

        list_techs_total = []
        for column in columns_to_count:
            if row[column].notna().any():
                row[column] = row[column].apply(ast.literal_eval)
                list_techs = row[column].iloc[0]
                counter += len(list_techs)
                list_techs_total.extend(list_techs)

        set_d3fend_tactics = set()
        for tech in list_techs_total:
            set_d3fend_tactics.add(comp_tactics.get_d3fend_tactics(tech))

        next_index = len(df_attack_to_d3fend)
        df_attack_to_d3fend.at[next_index, "cve_id"] = row_cve.cve_id
        df_attack_to_d3fend.at[next_index, "Attack_technique"] = row_cve.attack_technique
        df_attack_to_d3fend.at[next_index, "Attack_tactics"] = row_cve.attack_tactic
        df_attack_to_d3fend.at[next_index, "D3FEND_techniques"] = list_techs_total
        df_attack_to_d3fend.at[next_index, "D3FEND_tactics"] = set_d3fend_tactics

        print(f"Counter: {counter}")
        count_techs += 1
        print(f"finished Techs: {count_techs}")

    print(f"Final Count: {counter}")
    df_attack_to_d3fend.to_csv("Files/D3FEND_Target_COSE.csv", index=False)



upper_techniques = ['AssetInventory','NetworkMapping','OperationalActivityMapping','SystemMapping','AgentAuthentication',
                    'ApplicationHardening','CredentialHardening','MessageHardening','PlatformHardening','SourceCodeHardening','FileRemoval',
                    'FileAnalysis','IdentifierAnalysis','MessageAnalysis','NetworkTrafficAnalysis','PlatformMonitoring','PlattformMonitoring',
                   'ProcessAnalysis','ProcessAnalysis','UserBehaviorAnalysis','AccessMediation','AccessPolicyAdministration','ExecutionIsolation',
                    'NetworkIsolation','DecoyEnvironment','DecoyObject','ProcessEviction','RestoreAccess','RestoreObject','CredentialEviction','ObjectEviction']

def calculate_target_attack():
    df_d3fend_to_attack = pd.DataFrame(columns=['playbook_id', 'd3fend_technique', 'attack_techniques', 'attack_tactics'])

    df_playbooks = comp_helper.read_playbooks()

    counter = 0
    counter_playbooks = 0
    for row_playbook in df_playbooks.itertuples(index=False):
        list_techs = row_playbook.techniques
        for technique in list_techs:

            if technique in upper_techniques:
                continue

            for entry in list_d3fend_to_attack_mapping:
                if entry["technique"] == technique:

                    set_tactics = set()
                    set_techs = set()
                    dict_entry = entry["dict_d3fend_to_attack"]
                    for key, value in dict_entry.items():
                        set_tactics.add(key)
                        set_techs.update(value)
                    counter += len(set_techs)
                    break

            next_index = len(df_d3fend_to_attack)
            df_d3fend_to_attack.at[next_index, "playbook_id"] = row_playbook.playbook_id
            df_d3fend_to_attack.at[next_index, "d3fend_technique"] = technique
            df_d3fend_to_attack.at[next_index, "attack_techniques"] = set_techs
            df_d3fend_to_attack.at[next_index, "attack_tactics"] = set_tactics

        counter_playbooks += 1
        print(f"Playbooks: {counter_playbooks}")
        print(f"Attack Techs: {counter}")

    print(f"Final Attack Techs: {counter}")
    df_d3fend_to_attack.to_csv("Files/Attack_Target_COSE.csv", index=False)


calculate_target_d3fend()
#calculate_target_attack()