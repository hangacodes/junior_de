from pathlib import Path
import pandas as pd
import json
'''### Example 1 ⭐⭐ — Basic CSV read + trust check

**What it demonstrates:** Term 1 (read_csv), S.H.T.D. verification from W9D1'''

Path("data").mkdir(exist_ok=True)
csv_text = "name,age,city\nAva,34,Helsinki\nBo,29,Espoo\nCal,41,Tampere\n"
with open("data/people.csv", "w", encoding="utf-8") as f:
    f.write(csv_text)

df = pd.read_csv("data/people.csv")
print("shape:", df.shape)
print(df.head())
print(df.dtypes)

#The simplest read: one line loads the file, then S.H.T.D. confirms it worked.
# If `shape` or `dtypes` surprise you, something went wrong in the read.

'''### Example 2 ⭐⭐⭐ — Wrong delimiter produces a broken table

**What it demonstrates:** Term 1 (delimiter handling), what failure looks like'''

Path("data").mkdir(exist_ok=True)
text = "name|age|city\nAva|34|Helsinki\nBo|29|Espoo\n"

with open("data/piped.txt", "w") as f:
    f.write(text)

#WRONG - default assumes comma
bad_df = pd.read_csv("data/piped.txt")
print("BAD SHAPE:", bad_df.shape)
print(bad_df.head())

#CORRECT - specity the pipe delimiter
good_df = pd.read_csv("data/piped.txt", delimiter="|")
print("GOOD shape:", good_df.shape)
print(good_df.head())

#A wrong delimiter doesn’t crash — it silently produces a DataFrame with one column containing the entire row as a string.
# Shape is your first clue: `(2, 1)` when you expected 3 columns means the delimiter is wrong.

'''### Example 3 ⭐⭐⭐⭐ — dtype protection + na_values normalization together

**What it demonstrates:** Term 2 (dtype), Term 3 (NaN + na_values), combined defensive reading'''


csv_text = "customer_id,age,status\n001,34,active\n002,NA,inactive\n010,?,active\n"

with open("data/customers.csv" , "w") as f :
    f.write(csv_text)

df = pd.read_csv(
    "data/customers.csv", 
    dtype={"customer_id": str},
    na_values=["NA", "?", ""]
)
print(df)
print(df.dtypes)
#💡 Two defenses in one read: `dtype` preserved the leading zeros, and `na_values` turned `"NA"` and `"?"` into `NaN`.
# Notice `age` became `float64` — that’s because `NaN` forces the column from integer to float.
# This is expected behavior, not a bug.

'''### Example 4 ⭐⭐⭐ — Reading JSON records into a DataFrame

**What it demonstrates:** Term 1 (read_json), creating test data with json module from W7D5'''

records = [
    {"user_id": "u1", "plan": "free", "active": True},
    {"user_id": "u2", "plan": "pro", "active": True},
    {"user_id": "u3", "plan": "free", "active": False},
]

with open("data/users.json", "w") as f:
    json.dump(records,f, indent=2)

df = pd.read_json("data/users.json")

print(df)
print("shape:", df.shape)
print(df.dtypes)