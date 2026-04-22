import pandas as pd

# '''### Example 1 — Basic groupby + handling missing keys

# **⭐⭐⭐** · Combines: groupby(), fillna() (W10D1), aggregation
# **What it demonstrates:** Missing group keys silently disappear — fill them before grouping.'''


# sales = pd.DataFrame({
#     "category": ["Coffee", "Coffee", None, "Sandwich"],
#     "revenue": [12.5, 8.0, 6.0, 11.0]
# })

# # Without filling: the None row vanishes
# report_bad = sales.groupby("category")["revenue"].sum()
# print("Without fill:\n", report_bad)
# # Coffee 20.5, Sandwich 11.0 — where did the $6 go?

# # With filling: the None row becomes "Unknown"
# cat = sales["category"].fillna("Unknown")
# report_good = sales.groupby(cat)["revenue"].sum()
# print("\nWith fill:\n", report_good)
# # Coffee 20.5, Sandwich 11.0, Unknown 6.0 — all revenue accounted for
# print(sum(report_good))
# print(sum(report_bad))


# '''### Example 2 — Duplicates inflate metrics (and how to detect them)

# **⭐⭐⭐⭐** · Combines: groupby(), drop_duplicates() (W10D2), count vs sum
# **What it demonstrates:** Using groupby to detect duplicate rows before they corrupt aggregations.'''


# sales = pd.DataFrame({
#     "order_id": [1001, 1002, 1002, 1003],   # order 1002 is duplicated
#     "category": ["Coffee", "Coffee", "Coffee", "Sandwich"],
#     "revenue": [12.5, 8.0, 8.0, 11.0]
# })

# # Detect: which order_ids appear more than once?
# dup_check = sales.groupby("order_id")["revenue"].count()
# suspects = dup_check[dup_check > 1]
# # print("Suspected duplicates:\n", suspects)

# # Fix: dedup before aggregating
# clean = sales.drop_duplicates(subset=["order_id"])
# report = clean.groupby("category")["revenue"].agg(["count", "sum", "mean"])
# print("\nClean report:\n", report)
# print(clean)


'''### Example 3 — Multi-metric report with agg()

**⭐⭐⭐⭐** · Combines: groupby(), agg(), drop_duplicates() (W10D2), fillna() (W10D1)
**What it demonstrates:** A realistic analysis pipeline: clean → fill → dedup → group → report.'''

import pandas as pd

sales = pd.DataFrame([
    {"date": "2026-02-01", "category": "Coffee", "order_id": 1001, "revenue": 12.5},
    {"date": "2026-02-01", "category": "Coffee", "order_id": 1002, "revenue": 8.0},
    {"date": "2026-02-02", "category": None,     "order_id": 1003, "revenue": 6.0},
    {"date": "2026-02-02", "category": "Sandwich","order_id": 1004, "revenue": 10.0},
    {"date": "2026-02-02", "category": "Coffee", "order_id": 1004, "revenue": 10.0},  # dup
])

# Step 1: fill missing categories
cat = sales["category"].fillna("Unknown")

# Step 2: dedup by order_id
clean = sales.drop_duplicates(subset=["order_id"])
cat_clean = clean["category"].fillna("Unknown")

# Step 3: aggregate
report = clean.groupby(cat_clean)["revenue"].agg(["count", "sum", "mean", "min", "max"])
print(report)
