import pandas as pd

# '''Example1 : Column - by - column null audit'''

# df1 = pd.DataFrame({
#     "order_id": [1, 2, 3, 4, 5],
#     "customer": [10, None, 12, None, 14],
#     "country": ["FI", "FI", None, "SE", None],
#     "notes": [None, None, "rush", None, "gift"]
# })

# for col in df1.columns:
#     missing = sum(df1[col].isna())
#     rate = missing / len(df1)
#     print(f"{col}:{missing} missing ({rate * 100:.1f}%)")

# '''💡 `notes` has 60% missing — but it's optional context.
# `customer` at 40% is more alarming because downstream joins depend on it.
# Null rate alone doesn't tell you what to do; the column's role does.'''    


# '''Example2 - Drop vs fill: different strategies for different columns'''


# df2 = pd.DataFrame({
#     "user_id": [101, 102, 103, 104],
#     "email": ["a@x.com", None, None, "d@x.com"],
#     "city": ["Helsinki", None, "Espoo", None]
# })

# rows_before = len(df2)

# # email is required → drop rows missing it
# df2 = df2[df2["email"].notna()]

# # city is optional → fill with sentinel
# df2["city"] = df2["city"].fillna("UNKNOWN")

# rows_after = len(df2)
# print(f"rows:{rows_before} → {rows_after}")
# print(df2)


'''Example3 - Forward fill with sort-first discipline'''

import pandas as pd

df3 = pd.DataFrame({
    "hour": [3, 1, 4, 2],
    "temp": [None, 10.0, 13.0, None]
})

# WRONG: ffill on unsorted data
bad = df3.copy()
bad["temp"] = bad["temp"].ffill()
print("Unsorted ffill:")
print(bad)

# RIGHT: sort first, then ffill
good = df3.sort_values("hour")
good["temp"] = good["temp"].ffill()
print("\nSorted ffill:")
print(good)