# # Quick deduplication (order lost)
# ids = [10, 10, 22, 22,99, 35, 105, 111, 120,9034]
# unique_ids = list(set(ids))
# # print(unique_ids)  # [35, 10, 22] (order may vary!)

# # Order-preserving deduplication (seen set pattern)
# events = ["login", "logout", "login", "purchase", "login"]
# seen = set()
# first_seen = []

# for e in events:
#     if e not in seen:       # membership test on set (fast)
#         first_seen.append(e)
#         seen.add(e)

# print(first_seen)  # ['login', 'logout', 'purchase'] (order preserved!)
# print(seen)

'''### Example 1 — ⭐⭐ Deduplicate + count unique items

**What it demonstrates:** `set()` for quick deduplication, `len()` for unique count'''

# raw_ids = [10, 10, 10, 22, 22, 35, 35, 35, 35]
# unique_ids = set(raw_ids)

# print("raw count:", len(raw_ids)) # 9
# print("unique count:", len(unique_ids)) #3
# print("duplicates removed:", len(raw_ids) - len(unique_ids))    #6

'''### Example 2 — ⭐⭐⭐ Order-preserving deduplication with seen set

**What it demonstrates:** The seen-set pattern for dedup that keeps first-appearance order'''
# events = ["login", "logout", "login", "purchase", "login", "purchase", "refund"]

# seen = set()
# first_seen = []

# for e in events:
#     if e not in seen:
#         first_seen.append(e)
#         seen.add(e)

# print("first_seen:", first_seen)    #login , logout, purchase, refund
# print("unique count:", len(seen))   #4

'''### Example 3 — ⭐⭐⭐ Compare two data sources with set operations

**What it demonstrates:** union, intersection, and difference applied to a real comparison scenario'''

# crm_emails  = ["a@x.com", "b@x.com", "c@x.com", "c@x.com"]
# shop_emails = ["b@x.com", "c@x.com", "d@x.com"]

# crm  = set(crm_emails)
# shop = set(shop_emails)

# total_reach = crm.union(shop)
# overlap     = crm.intersection(shop)
# crm_only    = crm.difference(shop)
# shop_only   = shop.difference(crm)

# print("total reach:", len(total_reach))     #4
# print("overlap:", overlap)  #b and c
# print("CRM-only:", crm_only)    #a@x.com
# print("shop-only:", shop_only)  #d@x.com

'''### Example 4 — ⭐⭐⭐⭐ Sets + dicts: dedup IDs before joining

**What it demonstrates:** combining sets (for dedup/validation) with dict patterns (for data processing) — bridging W4D3-D5 concepts with today's new tool'''

# Transactions with duplicate IDs (bad data!)
transactions = [
    {"id": 1, "amount": 10.0},
    {"id": 2, "amount": 5.0},
    {"id": 1, "amount": 10.0},
    {"id": 3, "amount": 7.0},
    {"id": 2, "amount": 5.0},
]

seen_ids = set()
clean = []

for txn in transactions:
    if txn["id"] not in seen_ids:
        clean.append(txn)
        seen_ids.add(txn["id"])

print("raw:", len(transactions), "clean:", len(clean))      #3

total = 0
for txn in clean:
    total += txn["amount"]
print("total (deduped):", total)        #22