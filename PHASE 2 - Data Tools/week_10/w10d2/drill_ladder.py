import pandas as pd

# '''A1 - What does this print ?'''

# s = pd.Series([" ABC ", "abc", " Abc"])
# result = s.str.strip().str.lower()
# print(result.nunique())
# print(result.tolist())


# '''**A2 — Spot:** This code is supposed to dedup by `email`, but 3 rows survive. Why?'''

# df = pd.DataFrame({
#     "email": [" A@x.com", "a@x.com ", "A@X.COM"],
#     "score": [80, 90, 70]
# })

# clean = df.drop_duplicates(subset=["email"])
# print(len(df))  # prints 3 — expected 1

# #because there are no duplicated, unless we strip and lower first.

# clean["email"] = df["email"].str.strip().str.lower()
# cleaner = clean.drop_duplicates(subset=["email"])
# print(len(cleaner))



# '''**A3 — Trace:** After this code, what are the values in `nums`?'''

# prices = ["$10", "20", "FREE"]
# nums = []
# for p in prices:
#     cleaned = p.replace("$", "")
#     try:
#         nums.append(int(cleaned))
#     except ValueError:
#         nums.append(None)

# #10, 20 - nope, None is there too...great
# print(nums)



# '''Guided Drills'''

# '''### B1 — Canonicalize + dedup product codes

# **Task:**
# Given product codes like `" SKU-001 "`, `"sku-001"`, `"Sku-001"`.
# Create a `sku_canon` column (trim + lowercase), then dedup by `sku_canon` keeping the last row.

# **Hint:** Chain `.str.strip().str.lower()` for canonicalization. Use `drop_duplicates(subset=["sku_canon"], keep="last")`.'''


# b1 = pd.DataFrame({"product": ["SKU-001", "sku-001", "Sku-001"]})

# b1["sku_canon"] = b1["product"].str.strip().str.lower()

# print(b1)

# deduped = b1.drop_duplicates(subset=["sku_canon"], keep="last")

# print(deduped)


# '''### B2 — Price cleaning with failure count

# **Task:**
# Given a `price` column with values like `"$1,200"`, `"$50"`, `"N/A"`.
# Remove `$` and `,`, then convert to int row-by-row with `try/except`.
# Count how many rows failed.
# Print the failure count and the null rate of the resulting numeric column.

# **Hint:** Remove symbols with `.str.replace()` (regex=False).
# Use a for loop + try/except for conversion.
# Count failures with a counter variable.
# Use `isna().sum()` on the final column.'''

# b2 = b1
# b2["price"] = ["$1,200", "$50", "N/A"]

# print(b2)


# b2["price"] = b2["price"].str.replace("$", "", regex=False).str.replace(",", "", regex=False)
# print(b2)
# nums= []
# failures = 0
# for num in b2["price"]:
    

#     try:
#         nums.append(int(num))
#     except ValueError:
#         nums.append(None)
#         failures += 1

# b1["price_clean"] = nums
# print(f"Failed conversions:{failures}")
# print(f"Null rate after convert:{sum(b2['price_clean'].isna()) / len(b2) * 100:.1f}%")
# print(b2)


# '''### B3 — Regex whitespace + validation

# **Task:** Given a `city` column with values like `"  New   York "`, `"new york"`, `" NEW YORK"`
# Create a `city_canon` column: strip, lowercase, collapse multiple spaces with regex.
# Print unique count before and after to prove normalization worked.

# **Hint:** `r"\s+"` with `regex=True` collapses any number of spaces into one.

# ---'''

# b3 = pd.DataFrame({"city": ["    New     York      ", "new   york    ", "     NEW   YORK"
                            

# ]})

# b3["city_canon"] = b3["city"].str.strip().str.lower().str.replace(r"\s+", " ", regex=True)
# print(b3["city_canon"].nunique())
# print(b3)


'''Semi-Guided'''


def clean_products(df):
    """
    Clean a product DataFrame:
    1. Create canonical product_name (trim + lowercase + collapse spaces with regex)
    2. Dedup by canonical name, keep last
    3. Clean price: remove "$" and ",", convert to int (None for failures)
    4. Return (cleaned_df, report_dict)

    Report should include: rows_before, rows_after, unique_names_before,
    unique_names_after, price_conversion_failures
    """
    report = {}
    df = df.copy()

    #TODO: record rows_before and unique raw product_name count
    report["rows_before"] = len(df)
    report["unique_names_before"] = df["product_name"].nunique()

    #TODO: create product_canon column
    df["product_canon"] = df["product_name"].str.strip().str.lower().str.replace(r"\s+", " ", regex=True)

    #TODO: record unique_names_after (canonical)
    report["unique_names_after"] = df["product_canon"].nunique()
    #TODO: dedup by product_canon, keep="last"
    df = df.drop_duplicates(subset=["product_canon"], keep="last")

    #TODO: clean price column — remove "$" and ","
    price = df["price"].str.replace("$", "", regex=False).str.replace(",","", regex=False)
    #TODO: convert cleaned price to int row-by-row with try/except\
    nums = []
    failure = 0
    for n in price:
        try:
            nums.append(int(n))
        except ValueError:
            nums.append(None)
            failure +=1
    #TODO: record rows_after and price_conversion_failures
    report["rows_after"] = len(df)
    report["price_conversion_failures"] = failure
    df["price"] = nums
    return df, report

# Test data
products = pd.DataFrame({
    "product_name": ["  Widget Pro ", "widget pro", "WIDGET PRO", "Gadget", " gadget "],
    "price": ["$1,200", "$1200", "$1,200", "$50", "FREE"]
})

cleaned, report = clean_products(products)
print(cleaned)
print(report)