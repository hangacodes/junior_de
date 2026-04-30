import pandas as pd

# '''### Example 1 — Multi-column groupby + named aggregation
# - Combines: multi-column groupby, named aggregation
# **What it demonstrates:** Building a report-ready summary with clear column names from a two-key groupby.'''

# df = pd.DataFrame({
#     "region": ["N", "N", "S", "S", "S"],
#     "category": ["A", "B", "A", "A", "B"],
#     "sales": [10, 20, 30, 5, 40],
#     "units": [1, 2, 3, 1, 4],
# })

# report = df.groupby(["region", "category"]).agg(
#     total_sales=("sales", "sum"),
#     avg_sales=("sales", "mean"),
#     total_units=("units", "sum"),
#     order_count=("sales", "count"),
# )
# print(report)

# '''### Example 2 — Pivot table for dashboard-style output
# · Combines: pivot_table(), multi-column groupby (contrast)
# **What it demonstrates:** Same data, two presentations — groupby gives rows, pivot gives a matrix.
# '''

# df = pd.DataFrame({
#     "region": ["N", "N", "S", "S", "S"],
#     "category": ["A", "B", "A", "A", "B"],
#     "sales": [10, 20, 30, 5, 40],
# })

# # Grouped form (long):
# grouped = df.groupby(["region", "category"])["sales"].sum()
# print("GROUPED (long form):")
# print(grouped)

# # Pivot form (wide matrix):
# pt = df.pivot_table(index="region", columns="category", values="sales", aggfunc="sum")
# print("\nPIVOT (matrix form):")
# print(pt)


'''### Example 3 — transform() vs agg(): the row-count test

· Combines: transform(), agg() (W10D3), rank
**What it demonstrates:** agg shrinks to 2 rows; transform keeps 5 rows; rank labels within groups.'''

df = pd.DataFrame({
    "region": ["N", "N", "N", "S", "S"],
    "rep": ["Ana", "Ben", "Cid", "Dee", "Eli"],
    "sales": [100, 250, 180, 300, 120],
})

# agg: shrinks to one row per region
agg_result = df.groupby("region")["sales"].agg(["mean", "sum"])
print(f"agg rows:{len(agg_result)}")
print(agg_result)

# transform: keeps all 5 rows, stamps group mean onto each
df["region_avg"] = df.groupby("region")["sales"].transform("mean")
df["rank_in_region"] = df.groupby("region")["sales"].rank(ascending=False, method="dense")
print(f"\ntransform rows:{len(df)}")
print(df)
df = df.sort_values(by=["region", "rank_in_region"])
print(df)
df = df.reset_index
print(df)