import pandas as pd

# '''--- Column selection'''

# df = pd.DataFrame({
#     "name": ["Ava", "Bo", "Cal"],
#     "age": [34, 28, 40],
#     "city": ["Helsinki", "Espoo", "Tampere"],
# })

# # Single column → Series
# ages = df["age"]
# print(ages)
# print(type(ages))
# # 0    34
# # 1    28
# # 2    40
# # Name: age, dtype: int64
# # <class 'pandas.core.series.Series'>

# # Multiple columns → DataFrame
# subset = df[["name", "city"]]
# print(subset)
# print(type(subset))
# #   name      city
# # 0  Ava  Helsinki
# # 1   Bo     Espoo
# # 2  Cal   Tampere
# # <class 'pandas.core.frame.DataFrame'>


# '''---.loc vs .iloc'''


# df = pd.DataFrame(
#     {"name": ["Ava", "Bo", "Cal", "Dee"], "score": [88, 72, 95, 60]},
#     index=["u1", "u2", "u3", "u4"],
# )

# # .loc — by LABEL
# print(df.loc["u2"])           # row with label "u2"
# # name     Bo
# # score    72

# print(df.loc["u2":"u3"])      # label slice: includes BOTH u2 AND u3
# #    name  score
# # u2   Bo     72
# # u3  Cal     95

# # .iloc — by POSITION
# print(df.iloc[1])             # row at position 1 (second row)
# # name     Bo
# # score    72

# print(df.iloc[1:3])           # position slice: includes 1 and 2, NOT 3
# #    name  score
# # u2   Bo     72
# # u3  Cal     95


# '''---Boolean mask'''



# df = pd.DataFrame({
#     "name": ["Ava", "Bo", "Cal", "Dee"],
#     "age": [34, 28, 40, 28],
# })

# mask = df["age"] >= 30
# print(mask)
# # 0     True
# # 1    False
# # 2     True
# # 3    False
# # Name: age, dtype: bool

# filtered = df.loc[mask]     # ← only rows where mask is True
# print(filtered)
# #   name  age
# # 0  Ava   34
# # 2  Cal   40

# #wrong use:


# df1 = pd.DataFrame({"x": [1, 2, 3]})
# df2 = pd.DataFrame({"x": [10, 20]})
# mask = df2["x"] > 15
# mask2 = (df1.loc[mask]) # wrong- lenght is not the same
# print(mask)
# print(mask2)

# '''---SettingWithCopyWarning'''


# df = pd.DataFrame({
#     "name": ["Ava", "Bo", "Cal"],
#     "status": ["active", "inactive", "active"],
# })

# mask = df["status"] == "inactive"

# # RISKY — chained selection (may modify a copy, not df):
# mask2 = df[mask]["status"] = "removed"       # ← ChainedAssignmentError

# # SAFE — single .loc call:
# #df.loc[mask, "status"] = "removed"     # ← modifies df directly
# print(df)
# #   name    status
# # 0  Ava    active
# # 1   Bo   removed
# # 2  Cal    active
# print(mask)

'''### Example 1 ⭐⭐ — Single column returns a Series, double brackets return a DataFrame

**What it demonstrates:** Term 1 (column selection), Series vs DataFrame from W9D1'''

