import json
import pandas as pd


# --- Dataset 1: Semicolon-delimited CSV with no header ---
csv_text = "WH-01;bolt;500;2.50\nWH-02;nut;1200;0.80\nWH-03;washer;800;0.35\nWH-01;screw;350;1.10\n"
with open("week_9/w9d2/data/parts.csv", "w") as f:
    f.write(csv_text)


#TODO 1: Read data/parts.csv with correct sep, header=None, and
#   names=["warehouse", "part", "qty", "price"].
#   Print shape, head, dtypes.
#   Hint: the file uses semicolons, not commas.
my_csv_df = pd.read_csv("week_9/w9d2/data/parts.csv", sep = ";", header=None, names=["warehouse", "part", "qty", "price"])

print(my_csv_df.shape)
print(my_csv_df.head(2))
print(my_csv_df.dtypes
      )
# --- Dataset 2: CSV with IDs and messy missing values ---
csv_text2 = "part_id,weight_kg,status\n001,1.2,ok\n002,N/A,ok\n003,0.8,MISSING\n010,,ok\n"
with open("week_9/w9d2/data/parts2.csv", "w") as f:
    f.write(csv_text2)

#TODO 2: Read data/parts_quality.csv. Protect part_id as str.
#   Normalize "N/A", "MISSING", and "" to NaN.
#   Print the DataFrame and dtypes. Verify part_id kept leading zeros.
#   Hint: dtype={"part_id": str}, na_values=["N/A", "MISSING", ""]

my_csv_df2 = pd.read_csv("week_9/w9d2/data/parts2.csv", dtype={"part_id": str}, na_values=["N/A", "MISSING", ""])
print(my_csv_df2)
print(my_csv_df2.dtypes)



# --- Dataset 3: JSON records ---
records = [
    {"part": "bolt", "supplier": "AcmeCo", "lead_days": 5},
    {"part": "nut", "supplier": "MetalInc", "lead_days": 3},
    {"part": "washer", "supplier": "AcmeCo", "lead_days": 7},
]
with open("week_9/w9d2/data/suppliers.json", "w") as f:
    json.dump(records, f)


#TODO 3: Read data/suppliers.json into a DataFrame.
#   Print shape, head, dtypes.

my_json_df = pd.read_json("week_9/w9d2/data/suppliers.json")
print(my_json_df.shape)
print(my_json_df.head(1))
print(my_json_df.dtypes)

#TODO 4: Write a function trust_check(label, df) that prints:
#   a labeled header, shape, head(3), dtypes.
#   Call it on all three DataFrames.
#   Hint: reuse the inspection pattern from W9D1.


def trust_check(label, df):
    print(f"{label}")
    print(df.shape)
    print(df.head(3))
    print(df.dtypes)


print("\n---TRUST CHECK---\n")
trust_check("Dataset1:\n",my_csv_df)
trust_check("Dataset2:\n",my_csv_df2)
trust_check("Dataset3:\n",my_json_df)