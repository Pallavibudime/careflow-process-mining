import pandas as pd
import pm4py

# 1. Read event log
df = pd.read_csv("event_log.csv")

# 2. Convert Timestamp
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# 3. Rename columns for PM4Py
df = df.rename(columns={
    "Case_ID": "case:concept:name",
    "Activity": "concept:name",
    "Timestamp": "time:timestamp"
})

# 4. Sort events
df = df.sort_values(
    ["case:concept:name", "time:timestamp"]
)

print("Event log loaded successfully!")
print(df)

# 5. Convert Pandas DataFrame to PM4Py event log
log = pm4py.format_dataframe(
    df,
    case_id="case:concept:name",
    activity_key="concept:name",
    timestamp_key="time:timestamp"
)

# 6. Discover process model
process_tree = pm4py.discover_process_tree_inductive(log)

# 7. Print discovered process
print("\n========== DISCOVERED PROCESS ==========")
print(process_tree)

# 8. Save process tree as PNG
pm4py.save_vis_process_tree(
    process_tree,
    "process_tree.png"
)

print("\nProcess mining completed successfully!")
print("Created: process_tree.png")