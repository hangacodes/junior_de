import pandas as pd

# df1 = pd.DataFrame({
#     "qty": [2, 1, 3],
#     "unit_price": [5.0, 12.0, 4.0]})

# df1["subtotal"] = df1["qty"] * df1["unit_price"]       # column × column
# df1["with_tax"] = df1["subtotal"] * 1.24              # column × scalar (broadcasting)
# print(df1)
# output:
#    qty  unit_price  subtotal  with_tax
# 0    2         5.0      10.0     12.40
# 1    1        12.0      12.0     14.88
# 2    3         4.0      12.0     14.88
# print(type(df1["qty"] + df1["unit_price"]))
import pandas as pd

df = pd.DataFrame({"name": ["Ada", "Bob", "Carol"], "age": [25, 30, 35]})

# columns to list
print(df.columns.tolist() )          # ["name", "age"]

# a single column (Series) to list
print(df["name"].tolist())           # ["Ada", "Bob", "Carol"]

# a single row to list
print(df.iloc[0].tolist())           # ["Ada", 25]

# all rows to list of lists
print(df.values.tolist())            # [["Ada", 25], ["Bob", 30], ["Carol", 35]]