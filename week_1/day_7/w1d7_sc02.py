'''**SC-02 — The field normalizer with diagnostics**

Given these three messy column names:

```python
c1 = "  Order-ID  "
c2 = "  RAW__Events-2026.CSV  "
c3 = "Account  Balance"
```

For each one:
1. Normalize to snake_case: strip → lower → replace `-` with `_` → replace spaces with `_` → replace `__` with `_`
2. Print the cleaned value
3. Print whether it ends with `"_id"`, `".csv"`, or neither
4. Print the underscore count

**Trap:** `c2` has double underscores that survive the single replace pass. Handle it — and explain in a comment whether one pass is enough for *triple* underscores.'''

c1 = "  Order-ID  "
c2 = "  RAW__Events-2026.CSV  "
c3 = "Account  Balance"

c1 = c1.strip().lower().replace("-", "_").replace(" ", "_").replace("__","_")
c2 = c2.strip().lower().replace("-", "_").replace(" ", "_").replace("__","_")
c3 = c3.strip().lower().replace("-", "_").replace(" ", "_").replace("__","_")

print(f"\n-Summary {c1}:")
print(f"ends with '_id' : {c1.endswith("_id")}")
print(f"ends with '.csv' : {c1.endswith(".csv")}")
print(f"'_' appears : {c1.count("_")} times")

print(f"\n-Summary {c2}:")
print(f"ends with '_id' : {c2.endswith("_id")}")
print(f"ends with '.csv' : {c2.endswith(".csv")}")
print(f"'_' appears : {c2.count("_")} times")

print(f"\n-Summary {c3}:")
print(f"ends with '_id' : {c3.endswith("_id")}")
print(f"ends with '.csv' : {c3.endswith(".csv")}")
print("account_balance doesn't end with '_id' or '.csv'")
print(f"'_' appears : {c3.count("_")} times")