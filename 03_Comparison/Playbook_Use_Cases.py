import pandas as pd
import ast

list_D3fend_tactics = ["Model", "Harden", "Detect", "Isolate", "Deceive", "Evict", "Restore"]

df_top20 = pd.read_csv("Files/results_top20_v17_COSE.csv")
df_top20 = df_top20.sort_values(by='Total', ascending=False)

pd.set_option("display.max_columns", None)
#print(df_top20)

"""
for tactic in list_D3fend_tactics:
    tactic_covered = tactic + "_covered"
    df_top20_tactic = df_top20.dropna(subset=[tactic_covered])
    df_top20_tactic[tactic_covered] = df_top20_tactic[tactic_covered].apply(ast.literal_eval)
    df_exploded = df_top20_tactic.explode(tactic_covered)
    technique_counts = df_exploded[tactic_covered].value_counts()
    print(technique_counts)
    print()
"""

for tactic in list_D3fend_tactics:
    tactic_covered = tactic + "_missing"
    df_top20_tactic = df_top20.dropna(subset=[tactic_covered])
    df_top20_tactic[tactic_covered] = df_top20_tactic[tactic_covered].apply(ast.literal_eval)
    df_exploded = df_top20_tactic.explode(tactic_covered)
    technique_counts = df_exploded[tactic_covered].value_counts()
    print(technique_counts)
    print()


