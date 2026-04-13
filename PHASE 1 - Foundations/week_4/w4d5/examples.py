'''Examples'''
# #Join concept
# customers = [{"id": 101, "name": "Ava"}, {"id": 102, "name": "Noah"}]
# orders = [
#     {"id": 5001, "customer_id": 101, "total": 19.99},
#     {"id": 5002, "customer_id": 102, "total": 5.50},
#     {"id": 5003, "customer_id": 101, "total": 12.00},
# ]

# # Step 1: Build index on the entity you're looking up
# idx = {}
# for c in customers:
#     idx[c["id"]] = c

# print(idx)

# # Step 2: Loop through orders, match FK → PK via index
# enriched = []
# for o in orders:
#     cust = idx[o["customer_id"]]          # instant lookup
#     enriched.append({
#         "order_id": o["id"],
#         "customer_name": cust["name"],    # field from customers
#         "total": o["total"],              # field from orders
#     })

# for e in enriched:
#     print(e)



# # #### Example 1 — ⭐⭐ Build and use an index
# # #**What it demonstrates:** index pattern (id → record), replacing list scanning with dict lookup
# # #💡 Building the index is one loop. After that, every lookup is instant — no scanning.

# # products = [
# #     {"id": "P1", "name": "Notebook", "price": 3.25},
# #     {"id": "P2", "name": "Pen",      "price": 1.50},
# #     {"id": "P3", "name": "Eraser",   "price": 0.75},
# # ]

# # product_idx = {}
# # for p in products:
# #     product_idx[p["id"]] = p

# # print(product_idx)
# # print(product_idx["P2"])
# # print(product_idx["P2"]["price"])


# #### Example 2 — ⭐⭐⭐ Join orders to customers
# #**What it demonstrates:** join pattern — build index on one entity, loop the other, match keys
# #💡 The join doesn’t duplicate customer data permanently — it creates a combined view on demand.

# customers = [{"id": 1, "name": "Ava"}, {"id": 2, "name": "Noah"}]
# orders = [
#     {"id": 10, "customer_id": 1, "total": 5.00},
#     {"id": 11, "customer_id": 2, "total": 12.00},
#     {"id": 12, "customer_id": 1, "total": 3.50},
# ]

# idx = {}
# for c in customers:
#     idx[c["id"]] = c

# enriched = []
# for o in orders:
#     name = idx[o["customer_id"]]["name"]
#     enriched.append({"order_id": o["id"], "customer_name": name, "total": o["total"]})
    
# for e in enriched:
#     print(e["customer_name"], "spent", e["total"])

# #### Example 3 — ⭐⭐⭐ Group records by an attribute + summarize
# #**What it demonstrates:** grouping records (W4D3 pattern) applied to a list-of-dicts model, then computing per-group totals
# #💡 Grouping by foreign key gives you “all orders per customer” — the same shape as SQL `GROUP BY`.
# orders = [
#     {"id": 10, "customer_id": 1, "total": 5.00},
#     {"id": 11, "customer_id": 2, "total": 12.00},
#     {"id": 12, "customer_id": 1, "total": 3.50},
# ]

# by_customer = {}
# for o in orders:
#     cid = o["customer_id"]
#     by_customer.setdefault(cid, []).append(o["total"])

# for cid, totals in by_customer.items():
#     print("Customer", cid, "-> orders:", len(totals), "total:", sum(totals))

#### Example 4 — ⭐⭐⭐⭐ Full pipeline: join + group + find top

#**What it demonstrates:** combining index, join, and grouping in a realistic multi-step pipeline

customers = [
    {"id": 1, "name": "Ava", "tier": "gold"},
    {"id": 2, "name": "Noah", "tier": "silver"},
    {"id": 3, "name": "Mia", "tier": "gold"},
]
orders = [
    {"id": 10, "customer_id": 1, "total": 20.00},
    {"id": 11, "customer_id": 2, "total": 5.50},
    {"id": 12, "customer_id": 1, "total": 12.00},
    {"id": 13, "customer_id": 3, "total": 7.25},
]

# Step 1: Index customers
idx = {}
for c in customers:
    idx[c["id"]] = c

# Step 2: Group order totals by tier (join + group in one pass)
revenue_by_tier = {}
for o in orders:
    tier = idx[o["customer_id"]]["tier"]
    revenue_by_tier[tier] = revenue_by_tier.get(tier, 0) + o["total"]

print(revenue_by_tier)
