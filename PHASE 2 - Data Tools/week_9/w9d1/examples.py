#import pandas as pd
# '''### Example 1 ⭐⭐ — List of dicts becomes a DataFrame

# **What it demonstrates:** Term 2 (DataFrame), Term 5 (row-first creation), Term 6 (inspection)'''
# events = [
#     {"event": "login", "user": "u001", "hour": 9},
#     {"event": "click", "user": "u002", "hour": 10},
#     {"event": "login", "user": "u003", "hour": 14},
#     {"event": "login", "user": "u004", "hour": 20},
#     {"event": "click", "user": "u005", "hour": 1},
#     {"event": "login", "user": "u006", "hour": 40}
# ]
# df = pd.DataFrame(events)
# print("shape:", df.shape)
# print(df.head(8))
# print(df.dtypes)

# #PREDICT: What will `df.shape` print? How many columns will `dtypes` show?
# #💡 Each dict became a row. Keys became column names. Pandas inferred types automatically 
# # — `hour` is `int64`, text columns are `object`.


# '''### Example 2 ⭐⭐ — Dict of lists builds the same table, column-first

# **What it demonstrates:** Term 5 (column-first creation), contrast with row-first'''


# data = {
#     "event": ["login", "click", "login", "login", "click", "login"],
#     "user": ["u001", "u002", "u003", "u004", "u005" ,"u006"],
#     "hour": [9, 10, 14, 20, 1, 40],
# }
# df = pd.DataFrame(data)
# print(df)
# print("shape:", df.shape)

# #PREDICT: Will this produce the same table as Example 1?
# #💡 Same result, different thinking.
# # Row-first (list of dicts) feels natural when you think record-by-record.
# # Column-first (dict of lists) feels natural when you think field-by-field.
# # Real pipelines use both.


# '''### Example 3 ⭐⭐⭐ — Series: one column extracted, not a table

# **What it demonstrates:** Term 3 (Series), difference from DataFrame'''


# df = pd.DataFrame({
#     "name": ["Aino", "Mikko", "Li"],
#     "age": [29, 34, 41],
# })

# ages = df["age"]
# print(ages)
# print("type:", type(ages))
# print("type of df:", type(df))

# #PREDICT: Will `ages` print as a table or as a labeled list?

# #Selecting one column from a DataFrame gives you a Series — a labeled 1D array.
# # It prints differently (no column header, just index + values + dtype).
# # This is normal and expected.


# '''### Example 4 ⭐⭐⭐ — Custom index turns row labels into meaningful IDs

# **What it demonstrates:** Term 4 (index), inspecting with head/tail after setting index'''


# data = {
#     "city": ["Helsinki", "Espoo", "Vantaa"],
#     "pop_k": [656, 293, 239],
# }
# df = pd.DataFrame(data, index=["HEL", "ESP", "VAN"])
# print(df)
# print("shape:", df.shape)
# print(df.tail(2))
# #PREDICT: What will appear on the far-left column instead of 0, 1, 2?

# #💡 The index is not a regular column — it’s row labels.
# # Notice `shape` is `(3, 2)` not `(3, 3)` — the index doesn’t count as a column.
# # Setting the index to meaningful codes (airport codes, SKUs, user IDs) makes your data self-documenting.