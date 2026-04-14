from pathlib import Path
import json
import pandas as pd

# '''**A1 — Predict:**
# You have a file `data/items.csv` containing `"item;price;qty\nbolt;2.50;100\nnut;0.80;500\n"`.
# What happens if you run `pd.read_csv("data/items.csv")` without specifying `sep`?
# How many columns will `shape` report?''' 

# Path("data/drills").mkdir(exist_ok=True)

# items = "item;price;qty\nbolt;2.50;100\nnut;0.80;500\n"
# with open("data/drills/items.csv", "w") as f:
#     f.write(items)

# #If i run this with pd.read_csv without specifying sep , i will get a 2, 1 shape , because every line will be one string

# bad_df = pd.read_csv("data/drills/items.csv")
# print(bad_df.shape)

# #Good one is :
# good_df = pd.read_csv("data/drills/items.csv", delimiter=";")
# print(good_df.shape)


# '''**A2 — Spot:**
# This code is supposed to preserve the customer ID `"007"`, but it doesn't.
# What's wrong and what's the fix?'''

# with open("data/drills/agents.csv", "w") as f:
#     f.write("agent_id,name\n007,Bond\n008,Smith\n")
# df = pd.read_csv("data/drills/agents.csv", dtype={"agent_id":str})      
# #we must add dtype= to make the agent id str , because read_csv guesses 007 is just int 7 otherwise. So we override that and ask for a str.
# print(df["agent_id"].tolist())  # prints [7] instead of ["007"]


# '''**A3 — Predict:**
# A CSV has this content: `"name,score\nAva,88\nBo,NA\nCal,?\n"`.
# After reading with `pd.read_csv("data/scores.csv", na_values=["NA", "?"])`, what type will `score` be — `int64`, `float64`, or `object`?'''

# with open("data/drills/scores.csv", "w") as f:
#     f.write("name,score\nAva,88\nBo,NA\nCal,?\n")

# #Object - got this wrong appearantly is float64

# test = pd.read_csv("data/drills/scores.csv", na_values=["NA", "?"])
# print(test.dtypes)
# print(test)


# '''**A4 — Trace:**
# After running this code, what does `df.shape` return? What does the first row look like?'''


# text = "10,Ava\n20,Bo\n30,Cal\n"
# with open("data/drills/no_head.csv", "w") as f:
#     f.write(text)
# df = pd.read_csv("data/drills/no_head.csv", header=None, names=["id", "name"])
# #first row will be 0  10  ava - the header will be id and name, the shape will be 2, 2 -- WRONG shape is 3, 2 i didn't read the line properly
# print(df.shape)
# print(df)

# """---GUIDED DRILLS---"""

# '''**B1 — Headerless pipe-delimited file**
# Create a file `data/inventory.txt` with pipe-delimited data (no header row):
# 3 items with fields for item name, quantity, and warehouse code.
# Read it with the correct `sep`, `header=None`, and `names=`. Print `shape`, `head`, and `dtypes`.
# - Hint: `sep="|"`, `header=None`, `names=["item", "qty", "warehouse"]`.'''

# items = "Monitor|20|WH-N\nMacbook|69|WH-S\nMouse|23|WH-N\n"

# with open("data/drills/inventory.txt", "w", encoding="utf-8") as f:
#     f.write(items)

# my_df =pd.read_csv("data/drills/inventory.txt",sep="|", header=None, names=["item name", "quantity", "warehouse code"])


# print(my_df.shape)
# print(my_df.head())
# print(my_df.dtypes)


# '''**B2 — ID protection**
# Create a file `data/employees.csv` with a header and 4 rows.
# Include an `emp_id` column with leading zeros (like `"0042"`, `"0108"`).
# Read it once WITHOUT `dtype` and once WITH `dtype={"emp_id": str}`.
# Print both DataFrames and show the difference.
# - Hint: Compare `df["emp_id"].tolist()` from both reads.'''

# employees = "emp_id,name,score\n0042,Ava,88\n0059,Bo,NA\n0109,Cal,79\n0011,Michael,100\n"

# with open("data/drills/employees.csv", "w", encoding="utf-8") as f:
#     f.write(employees)

# bad_df = pd.read_csv("data/drills/employees.csv")

# good_df = pd.read_csv("data/drills/employees.csv", dtype={"emp_id":str})

# print(bad_df["emp_id"])
# print(good_df["emp_id"])

# print(bad_df["emp_id"].tolist() == good_df["emp_id"].tolist())

# '''**B3 — Custom missing markers**
# Create a file `data/readings.csv` with columns `sensor`, `value`, `status`.
# Use `"-"` and `"MISSING"` as missing markers in some cells.
# Read with `na_values=["-", "MISSING"]` and verify the affected cells show `NaN`.
# - Hint: After reading, print `df` and check that `dtypes` reflects the expected types.'''

# readings = "sensor,value,status\nsensorA,23.2,-\nsensorB,MISSING,-\nsensorC,23.8,ok"

# with open("data/drills/readings.csv", "w", encoding="utf-8") as f:
#     f.write(readings)

# my_dataframe = pd.read_csv("data/drills/readings.csv", na_values=["-", "MISSING"])

# print(my_dataframe)


# '''**B4 — JSON round-trip**
# Write a list of 4 dicts to a JSON file using `json.dump()` (recall W7D5).
# Read it back with `pd.read_json()`. Print `shape`, `head`, and `dtypes`.
# - Hint: The JSON must be a flat list of same-shaped objects for `read_json` to produce a clean table.'''

# records = [
#     {"name": "Ava", "score": 88, "city": "Helsinki"},
#     {"name": "Bo", "score": 72, "city": "Espoo"},
#     {"name": "Cal", "score": 95, "city": "Tampere"},
#     {"name": "Dan", "score": 61, "city": "Oulu"},
# ]

# with open ("data/drills/peeps.json", "w") as f:
#     json.dump(records, f, indent=2)

# my_json_df = pd.read_json("data/drills/peeps.json")
# print(my_json_df.shape)
# print(my_json_df.head(2))
# print(my_json_df.dtypes)