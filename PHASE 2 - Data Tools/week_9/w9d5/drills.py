import pandas as pd

# '''**A1 — Predict:** 
# What does `pd.Series([10, 20, 30]) * 2` produce?'''

# #Produces 20, 40, 60


# '''**A2 — Predict:**
# After `.str.strip().str.lower()` on `["  ADA  ", "bOb "]`, what values remain?'''

# #["ada" "bob"]


# '''**A3 — Spot:** This code raises an error. What's wrong?

# df = pd.DataFrame({"price": ["$5.00"]})
# df["price_num"] = df["price"].astype(float)'''

# # You cannot convert $5.00 to a float, first you need to remove the symbol than convert to float


# '''**A4 — Predict:**
# After `df = df.rename(columns={"A": "a"})`, what does `df.columns.tolist()` show if original columns were `["A", "B"]`?'''

# #["a", "B"]


# '''Guided drills'''
# '''**B1 — Column arithmetic + broadcasting**
# Start with `df = pd.DataFrame({"hours": [8, 6, 10], "rate": [25.0, 30.0, 22.0]})`. Add `pay` (hours * rate) and `with_bonus` (pay * 1.15). Print.
# - Hint: `df["pay"] = df["hours"] * df["rate"]`'''

# df = pd.DataFrame({
#     "hours": [8, 6, 10],
#     "rate":[25.0, 30.0, 22.0]
#     })

# df["pay"] = df["hours"] * df["rate"]
# df["with_bonus"] = df["pay"] * 1.15
# print(df)


# '''**B2 — String cleaning**
# Start with `df = pd.DataFrame({"city": [" HELSINKI", "espoo ", "  Tampere "]})`. Create `city_clean`: stripped + lowercased.
# - Hint: `.str.strip().str.lower()`'''

# df = pd.DataFrame({"city": [" HELSINKI", "espoo ", "  Tampere "]})

# city_clean = df["city"].str.strip().str.lower()
# print(city_clean)


# '''**B3 — Clean → convert → compute**
# Start with `df = pd.DataFrame({"amount": ["$100", "$250", "$75"]})`. Remove `$`, convert to float, add `fee` at 3%. Print.
# - Hint: `.str.replace("$", "", regex=False).astype(float)`'''

# df = pd.DataFrame({"amount": ["$100", "$250", "$75"]})

# df_b3 = pd.DataFrame({
#     "amount": ["$100", "$250", "$75"]
# })

# df["amount"] = df_b3["amount"].str.replace("$", "", regex=False).astype(float)
# df["fee"] = df["amount"] * 0.03
# print(df)


'''**B4 — Rename + drop**
Start with `df = pd.DataFrame({"FirstName": ["Ada"], "SSN": ["123-45-6789"], "Score": [95]})`. Rename to snake_case, drop SSN. Print columns.
- Hint: `df.rename(columns={...})` then `df.drop(columns=[...])`'''


df = pd.DataFrame({"FirstName": ["Ada"], "SSN": ["123-45-6789"], "Score": [95]})

df = df.rename(columns={"FirstName": "first_name","Score":"score"})

df = df.drop(columns=["SSN"])
print(df.columns)