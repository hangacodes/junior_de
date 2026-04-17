import pandas as pd
# #**A1 — Predict:** What does this print?

# s = pd.Series([5, None, 3, None, 1])
# print(sum(s.isna()))
# print(sum(s.notna()))
# #2 and 3

# #**A2 — Trace:** After this code runs, what are the values in `df["score"]`?


# df = pd.DataFrame({"score": [None, 80, None, 90]})
# df["score"] = df["score"].fillna(0)
# print(df)
# #[0, 80, 0 , 90]


# # **A3 — Spot:** This code is supposed to keep only rows where `email` is present, but it keeps all rows. Find the bug.

# df = pd.DataFrame({"email": ["a@x.com", None, "c@x.com"]})
# # clean = df[df["email"] != None]
# # Two problems:
# # 1. None and NaN are not the same thing — Pandas stores missing values as NaN internally
# # 2. != None compares the whole Series to None, not each row — every row gets True
# clean = df[df["email"].notna()]
# print(clean)


# '''Guided-drills'''

# '''### B1 — Null audit + targeted drop

# **Task:** Given a DataFrame with columns `order_id`, `customer_id`, `amount`, and `notes`, compute the null rate for each column.
# Then keep only rows where `customer_id` is present (it’s required), and fill missing `notes` with `""`.

# **Hint:** Loop through `df.columns` to compute rates. Use `df[df["customer_id"].notna()]` for the drop. Use `fillna("")` for notes.'''

# dframe = pd.DataFrame({
#     "order_id":    [101, 102, 103, 104, 105],
#     "customer_id": ["C1", None, "C3", "C4", None],
#     "amount":      [29.99, 15.00, None, 42.50, 9.99],
#     "notes":       ["Gift wrap", None, "Express", None, None]
# })

# for col in dframe.columns:
#     missing = sum(dframe[col].isna())
#     rate = missing / len(dframe)
#     print(f"{col}:{missing} missing ({rate * 100:.1f}%)")

# dframe = dframe[dframe["customer_id"].notna()]
# dframe["notes"] = dframe["notes"].fillna("")
# print(dframe)

# '''### B2 — Sort-then-fill pipeline

# **Task:**
# Given temperature readings with columns `timestamp` (integers 1–6) and `temp` (some missing), sort by timestamp, then forward-fill the temperature.
# Print before and after null counts to verify.

# **Hint:** `sort_values("timestamp")` first. Then `ffill()`. Compare `sum(df["temp"].isna())` before and after.'''


df = pd.DataFrame({
    "timestamp": [3, 1, 5, 2, 6, 4],
    "temp":      [22.5, None, 19.0, None, 21.0, None]
})

# df = df.sort_values(by=("timestamp"))
# print(sum(df["temp"].isna()))
# df["temp"] = df["temp"].ffill()
# print(sum(df["temp"].isna()))
# print(df)


'''### B3 — Before/after report function

**Task:**
Write a function `null_report(df, title)` that prints the title, then for each column prints the column name, missing count, and null rate as a percentage.
Call it once before cleaning and once after.

**Hint:** Use a `for col in df.columns` loop. Compute `sum(df[col].isna()) / len(df) * 100` for the percentage.'''

def null_report(df, title):
    print(title)
    for col in df.columns:
        missing = sum(df[col].isna())
        rate = missing / len(df)
        print(f"{col}:{missing} missing ({rate * 100:.1f}%)")
        

df = df.sort_values(by=("timestamp"))
print(sum(df["temp"].isna()))
null_report(df, "Before cleaning:")
df["temp"] = df["temp"].ffill()
print(sum(df["temp"].isna()))
null_report(df, "After cleaning:")
print(df)
