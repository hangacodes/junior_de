import pandas as pd

# #**A1 — Predict:** What does this print?

# df = pd.DataFrame({"store": ["A", "A", "B"], "revenue": [10, 20, 15]})
# result = df.groupby("store")["revenue"].sum()
# print(result.to_dict())

# # "A" : 30
# # "B" : 15

# #**A2 — Trace:** After running this, what is the value of `coffee_mean`?

# import pandas as pd

# df = pd.DataFrame({
#     "category": ["Coffee", "Coffee", "Tea"],
#     "revenue": [10.0, 8.0, 12.0]
# })

# report = df.groupby("category")["revenue"].agg(["mean", "sum"])
# coffee_mean = report.loc["Coffee", "mean"]
# #Value of coffee_mean should be 9.0
# print(report)

# '''**A3 — Spot:**
# This code groups sales by category, but the missing-category row disappears from the output. 
# What's wrong and how do you fix it?'''


# df = pd.DataFrame({
#     "category": ["Coffee", None, "Tea"],
#     "revenue": [10.0, 5.0, 8.0]
# })
# cat = df["category"].fillna("Unknown")

# report = df.groupby(cat)["revenue"].sum()

# print(report)
# # Only shows Coffee and Tea — $5 is missing from the total

# #First i had to store the category column into a series filled with "Unknown" instead of None
# # Then i had to groupby the new variable


# '''### 6B) Guided drills'''

# '''### B1 — Category mini-report with missing-key handling
# **Task:** 
# Using the `sales` DataFrame below, fill missing categories with `"Unknown"`, then produce a grouped report with `count`, `sum`, `mean` for revenue.'''


# sales = pd.DataFrame([
#     {"category": "Coffee", "revenue": 12.5},
#     {"category": "Coffee", "revenue": 8.0},
#     {"category": None,     "revenue": 6.0},
#     {"category": "Sandwich", "revenue": 11.0},
# ])

# cat = sales["category"].fillna("Unknown")

# report = sales.groupby(cat)["revenue"].agg(["count", "sum", "mean"])
# print(report)

# '''### B2 — Dedup then aggregate

# **Task:**
#  The `sales` DataFrame below has a duplicate order (1002 appears twice).
#  Remove duplicates by `order_id` first, then group by `category` and compute `sum` and `count` for revenue.'''


# sales = pd.DataFrame([
#     {"order_id": 1001, "category": "Coffee", "revenue": 12.5},
#     {"order_id": 1002, "category": "Coffee", "revenue": 8.0},
#     {"order_id": 1002, "category": "Coffee", "revenue": 8.0},
#     {"order_id": 1003, "category": "Tea",    "revenue": 7.0},
# ])
# clean = sales.drop_duplicates(subset=["order_id"])
# report = clean.groupby("category")["revenue"].agg(["count", "sum"])
# print(report)

'''### B3 — Different aggregations for different columns

**Task:** Using the DataFrame below, group by `store` and produce: `sum` and `mean` for `revenue`, and `count` for `order_id`.'''

import pandas as pd

df = pd.DataFrame([
    {"store": "Helsinki", "order_id": 1, "revenue": 10.0},
    {"store": "Helsinki", "order_id": 2, "revenue": 20.0},
    {"store": "Espoo",    "order_id": 3, "revenue": 15.0},
])

report = df.groupby("store").agg({
    "revenue": ["sum", "mean"],
    "order_id" : "count"
})
print(report)


'''Semi - Guided drill'''


def category_kpis(sales):
    """
    Produce a category KPI report from raw sales data.
    1. Fill missing categories with "Unknown"
    2. Remove duplicate orders by order_id
    3. Group by category and compute: count, sum, mean, median, min, max for revenue
    4. Return the report DataFrame
    """
    #TODO: fill missing categories
    cat = sales["category"].fillna("Unknown")
    #TODO: dedup by order_id
    sales = sales.drop_duplicates(subset=["order_id"])
    #TODO: group by filled category and aggregate revenue
    report = sales.groupby(cat)["revenue"].agg(["count", "sum", "mean", "median", "min", "max"])
    return report
    # So the answer key fills with "unknown" twice...idk why , i have to come back and check 

# Test data
sales = pd.DataFrame([
    {"order_id": 1001, "category": "Coffee",   "revenue": 12.5},
    {"order_id": 1002, "category": "Coffee",   "revenue": 8.0},
    {"order_id": 1002, "category": "Coffee",   "revenue": 8.0},
    {"order_id": 1003, "category": None,        "revenue": 6.0},
    {"order_id": 1004, "category": "Sandwich",  "revenue": 11.0},
])

report = category_kpis(sales)
print(report)