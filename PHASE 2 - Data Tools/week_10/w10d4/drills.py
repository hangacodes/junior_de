import pandas as pd
# '''Activation drills'''
# # 1 What does this print?

# df = pd.DataFrame({"region": ["N", "N", "S"], "sales": [10, 20, 30]})
# result = df.groupby("region").agg(total=("sales", "sum"), avg=("sales", "mean"))
# print(result.columns.tolist())
# #[total , avg]

# #A2 — Trace: After this runs, what is df["g_mean"] for each row?

# df = pd.DataFrame({"g": ["A", "A", "B"], "v": [10, 30, 50]})
# df["g_mean"] = df.groupby("g")["v"].transform("mean")
# print(df)


# # **A3 — Spot:** This pivot table should show sums, but the numbers look too small. What’s wrong?

# df = pd.DataFrame({"region": ["N", "N", "S"], "cat": ["A", "A", "A"], "sales": [10, 20, 30]})
# pt = df.pivot_table(index="region", columns="cat", values="sales", aggfunc="sum")
# print(pt)  # N,A shows 15.0 — should be 30 if summing - it was missing the aggfunc= "sum"


# '''### 6B) Guided drills

# ### B1 — Multi-column groupby + named aggregation
# Group by `["region", "category"]` and produce named columns:
# `total_sales` (sum), `avg_sales` (mean), `n_orders` (count).'''


# df = pd.DataFrame({
#     "region": ["N", "N", "S", "S", "S"],
#     "category": ["A", "B", "A", "A", "B"],
#     "sales": [10, 20, 30, 5, 40],
# })

# result = df.groupby("region").agg(total_sales = ("sales", "sum"), avg_sales=("sales", "mean"), n_orders=("sales", "count"))
# print(result)


# '''### B2 — Pivot table with explicit aggfunc
# Using the same DataFrame, create a pivot table with:
# -`index="region"`, `columns="category"`, `values="sales"`, `aggfunc="sum"`.
# Then create a second pivot with `aggfunc="count"` and compare.'''

# df = pd.DataFrame({
#     "region": ["N", "N", "S", "S", "S"],
#     "category": ["A", "B", "A", "A", "B"],
#     "sales": [10, 20, 30, 5, 40],
# })

# B2_sum = df.pivot_table(index="region", columns="category", values="sales", aggfunc="sum")
# B2_count =df.pivot_table(index="region", columns="category", values="sales", aggfunc="count")

# print(B2_sum)
# print(B2_count)


# '''### B3 — Transform + rank for per-row context
# Add two columns to the DataFrame: `region_total` using `transform("sum")` grouped by region, and `rank_in_region` using `.rank(ascending=False, method="dense")` grouped by region.'''

# df["region_total"] = df.groupby("region")["sales"].transform("sum")
# df["rank_in_region"] = df.groupby("region")["sales"].rank(ascending=False, method="dense")
# print(df)
# df = df.sort_values(by=["region", "rank_in_region"])

# print(df.reset_index(drop=True))


'''Semi-Guided'''
#Goal: Write a function store_report(df) that produces a named-aggregation summary AND adds transform columns to the original DataFrame.

def store_report(df):
    """
    1. Produce a grouped summary by store: total_sales, avg_sales, order_count
    2. Add transform columns to df: store_avg, store_total, rank_in_store
    3. Return (summary, enriched_df)
    """
    df = df.copy()

    #TODO: named aggregation grouped by "store"
    summary = df.groupby("store").agg(
        total_sales = ("sales", "sum"),
        avg_sales = ("sales", "mean"),
        order_count = ("sales", "count")

    )

    #TODO: transform — add store_avg and store_total
    df["store_avg"] = df.groupby("store")["sales"].transform("mean")
    df["store_total"] = df.groupby("store")["sales"].transform("sum")
    

    #TODO: rank — add rank_in_store (descending, dense)
    df["rank_in_store"] = df.groupby("store")["sales"].rank(ascending=False, method="dense")

    #TODO: return (summary, df)
    return summary, df

df = pd.DataFrame({
    "store": ["A", "A", "A", "B", "B", "C"],
    "rep": ["Ana", "Ben", "Cid", "Dee", "Eli", "Fay"],
    "sales": [100, 250, 180, 300, 120, 90],
})

summary, enriched = store_report(df)
print(summary)
print(enriched)