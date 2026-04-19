import pandas as pd

'''### Example 1 — Canonicalize before dedup

**⭐⭐⭐** · Combines: normalization, drop_duplicates()
**What it demonstrates:** Why you must normalize BEFORE deduplicating — otherwise “duplicates” look different to the computer.'''



df1 = pd.DataFrame({
    "email": [" Alice@X.com ", "alice@x.com", "ALICE@x.com"],
    "plan": ["free", "pro", "enterprise"]
})

# Without canonicalization: dedup sees 3 unique emails
dedup_raw = df1.drop_duplicates(subset=["email"])
print("Without canon:", len(dedup_raw))  # 3 — all "different"

# With canonicalization: dedup sees 1 unique email
df1["email_canon"] = df1["email"].str.strip().str.lower()
dedup_clean = df1.drop_duplicates(subset=["email_canon"], keep="last")
print("With canon:", len(dedup_clean))    # 1 — correctly collapsed
print(dedup_clean)


'''### Example 2 — Clean-then-convert pipeline with failure handling

**⭐⭐⭐⭐** · Combines: str.replace (W9D5), try/except (W2D5), failure mode, null rate (W10D1)
**What it demonstrates:** Real-world type conversion where some values can’t convert, and counting failures instead of crashing.'''


df = pd.DataFrame({
    "item": ["Widget", "Gadget", "Doohickey"],
    "price": ["$1,200", "$50", "TBD"]
})

# Step 1: remove symbols (T-N-R-C: Replace step)
cleaned = (
    df["price"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

# Step 2: convert row-by-row so one bad value doesn't crash everything
failed = 0
nums = []
for v in cleaned:
    try:
        nums.append(int(v))
    except ValueError:
        nums.append(None)
        failed += 1

df["price_num"] = nums
print(f"Failed conversions:{failed}")
print(f"Null rate after convert:{sum(df['price_num'].isna()) / len(df) * 100:.1f}%")
print(df)


'''### Example 3 — Regex: collapsing inconsistent whitespace

**⭐⭐⭐** · Combines: regex, normalization, nunique() check
**What it demonstrates:** When literal replace can’t fix the problem and you need a pattern.'''


df = pd.DataFrame({"name": ["  Alice   Smith  ", "Bob  Jones", "Cara      Ray"]})

# Trim outer spaces + collapse inner spaces to exactly one
df["name_clean"] = (
    df["name"]
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
)

print(df)
print("Unique names:", df["name_clean"].nunique())