import pandas as pd

# You run a chain of small warehouses. Here's the raw data.
raw_records = [
    {"warehouse_id": "WH-N", "city": "Oulu", "capacity": 5000, "current_stock": 3200},
    {"warehouse_id": "WH-S", "city": "Turku", "capacity": 3200, "current_stock": 3100},
    {"warehouse_id": "WH-E", "city": "Joensuu", "capacity": 4100, "current_stock": 1800},
    {"warehouse_id": "WH-W", "city": "Vaasa", "capacity": 2800, "current_stock": 2750},
]
ids = []
for rec in raw_records:
    ids.append(rec["warehouse_id"])

#TODO 1: Build a DataFrame from raw_records with warehouse_id as the index
#   Hint: create the DataFrame first, then think about how to use the
#   warehouse_id column as the index. One approach: pass index= with a list
#   of the IDs extracted from the records.
my_df = pd.DataFrame(raw_records, index=ids)
print(my_df)


#TODO 2: Write a function report(label, df) that prints:
#   - a header line with the label
#   - shape
#   - head (default rows)
#   - dtypes
#   Then call it on your DataFrame.
def report(label, df):
    print(f"{label}")
    print(df.shape)
    print(df.head(2))
    print(df.dtypes)

report("My first report", my_df)
#TODO 3: Extract the "current_stock" column as a Series.
#   Print it and confirm its type is Series (not DataFrame).

current_stock = my_df["current_stock"]
print(current_stock)
print(type(current_stock))
print(current_stock.shape)

#TODO 4: Build the SAME data as a dict of lists and create a second DataFrame.
#   Use report() on it and verify it matches the first.

raw_records = [
    {"warehouse_id": "WH-N", "city": "Oulu", "capacity": 5000, "current_stock": 3200},
    {"warehouse_id": "WH-S", "city": "Turku", "capacity": 3200, "current_stock": 3100},
    {"warehouse_id": "WH-E", "city": "Joensuu", "capacity": 4100, "current_stock": 1800},
    {"warehouse_id": "WH-W", "city": "Vaasa", "capacity": 2800, "current_stock": 2750},
]

modified_records = {"warehouse_id": ["WH-N", "WH-S", "WH-E", "WH-W"], "city": ["Oulu", "Turku", "Joensuu", "Vaasa"], "capacity":[5000, 3200,4100,2800], "current_stock":[3200,3100,1800,2750]}
modified_ids = modified_records["warehouse_id"]
second_df = pd.DataFrame(modified_records, index=modified_ids)
# same_report = report("Second report", second_df)
print(second_df)
report("My second report", second_df)