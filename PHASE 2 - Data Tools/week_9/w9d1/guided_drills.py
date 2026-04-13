import pandas as pd

# '''**B1 — Two ways to build the same table**
# Create a DataFrame with columns `dept` and `headcount` and rows: Engineering/42, Marketing/18, Sales/31.
# Build it once from a list of dicts and once from a dict of lists. Print both and verify `shape` matches.
# - Hint: list of dicts → each dict has `"dept"` and `"headcount"` keys. Dict of lists → `{"dept": [...], "headcount": [...]}`.'''

# rows = pd.DataFrame([{"dept":"Engineering" , "headcount":42},{"dept":"Marketing" , "headcount":18}, {"dept":"Sales" , "headcount":31}])
# print(rows)
# print(rows.shape)

# cols = pd.DataFrame({"dept": ["Engineering", "Marketing", "Sales"], "headcount":[42,18,31]})
# print(cols)
# print(cols.shape)

# '''**B2 — Custom index + full inspection**
# Create a DataFrame with columns `warehouse` and `capacity` containing: North/5000, South/3200, East/4100.
# Set the index to `["WH-N", "WH-S", "WH-E"]`.
# Run the full S.H.T.D. routine and print each result with a clear label.
# - Hint: `pd.DataFrame(data, index=[...])`. Remember `shape` and `dtypes` have no parentheses.'''
# warehouses = {"warehouse": ["North", "South", "East"], "capacity": [5000, 3200, 4100]}
# the_frame = pd.DataFrame(warehouses, index= ["WH-N", "WH-S", "WH-E"])

# print(the_frame.shape)
# print(the_frame.head())
# print(the_frame.dtypes)

# '''**B3 — Function that inspects any DataFrame**
# Write a function `inspect(label, df)` that prints a header with the label, then shape, head, tail, and dtypes — each with a text label.
# Call it on two different DataFrames.
# - Hint: Use f-strings for the header. `df.head()` and `df.tail()` use parentheses; `df.shape` and `df.dtypes` do not.'''

# df1 = pd.DataFrame({"a": [1, 2], "b": [10, 20]})
# df2 = pd.DataFrame({"x": ["hi", "lo"], "y": [True, False]})


# def inspect(label, df):
#     print(f"This is {label}")
#     print(f"Shape of the dataframe is: {df.shape}")
#     print("head:\n", df.head(2), sep="")
#     print(f"tail:")
#     print(df.tail(2))
#     print(f"The types:")
#     print(df.dtypes)

# inspect("first table", df1)
# inspect("second table", df2)

# '''**B4 — Extract a Series and prove it's 1D**
# Create a DataFrame with at least 3 columns.
# Extract one column into a variable. Print the variable, its `type()`, and its `.shape`.
# Confirm shape is `(N,)` — one dimension, not two.
# - Hint: `type(my_series)` shows the class. A Series `.shape` is a 1-element tuple.'''

# my_series = {
#     "day": ["Mon", "Tue" , "Wed" ,"Thu", "Fri", "Sat", "Sun"], 
#     "workout": ["Legs - Glutes and femural focus", "Chest + biceps + abs", "Back and tris", "Rest day", "Legs - front focus", "Cardio and Abs", "Rest"]
#     }

# my_dataframe = pd.DataFrame(my_series)
# weekdays = my_dataframe["day"]
# print(type(my_dataframe))
# print(my_dataframe)
# print(weekdays.dtype)
# print(weekdays.shape)