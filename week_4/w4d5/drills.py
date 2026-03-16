# #Activation Drills
# #**A1 — Predict:** What does this print?

# products = [{"id": "P1", "name": "Pen"}, {"id": "P2", "name": "Book"}]
# idx = {}
# for p in products:
#     idx[p["id"]] = p
# print(idx["P1"]["name"]) #Pen

# #**A2 — Trace:** After this code, what is `spend[1]`?

# orders = [{"cid": 1, "total": 5.0}, {"cid": 2, "total": 12.0}, {"cid": 1, "total": 3.5}]
# spend = {}
# for o in orders:
#     cid = o["cid"]
#     spend[cid] = spend.get(cid, 0) + o["total"] # 8.5

# #**A3 — Spot:** This join crashes. What error, and on which line?
# customers = [{"id": 1, "name": "Ava"}]
# orders = [{"id": 10, "customer_id": 1, "total": 5.0}]
# idx = {}
# for c in customers:
#     idx[c["id"]] = c
# for o in orders:

#     name = idx[o["customer_id"]]["name"] # I didn't know what was the problem so i ran it, than i saw that the customer id 2 doesn't exist


# #**A4 — Predict:** What does this print?

# c = {"id": 101, "name": "Ava"}
# o = {"id": 5001, "customer_id": 101, "total": 9.99}
# print(o["customer_id"] == c["id"])  #True

'''Guided Drills:'''

'''# #**B1 — Build an index** (`build_index.py`)
# #Given:'''
# customers = [
#     {"id": 1, "name": "Ava"},
#     {"id": 2, "name": "Noah"},
#     {"id": 3, "name": "Mia"},
# ]

# idx = {}
# for c in customers:
#     idx[c["id"]] = c
# print(idx[2]["name"])
# #Build `idx` so that `idx[2]["name"]` returns `"Noah"`.
# #**Hint:** Loop customers, set `idx[c["id"]] = c`.

'''**B2 — Group orders by customer_id** (`group_orders.py`)
Given:'''
# orders = [
#     {"id": 10, "customer_id": 1, "total": 5.00},
#     {"id": 11, "customer_id": 2, "total": 12.00},
#     {"id": 12, "customer_id": 1, "total": 3.50},
# ]
# # Build `by_customer` where each key is a customer_id and each value is a list of totals. Print each customer_id and its total spend.
# # **Hint:** `.setdefault(cid, []).append(o["total"])` then `sum()`.

# by_customer = {}
# for o in orders:
#     cid = o["customer_id"]
#     by_customer.setdefault(cid, []).append(o["total"])
# for k, v in by_customer.items():
#     print(k,":", sum(v))

'''**B3 — Join orders to customer names** (`join_demo.py`)
Using B1’s `customers` and B2’s `orders`, create `enriched` — a list of dicts with `order_id`, `customer_name`, `total`.
**Hint:** Build `idx` first. Then `name = idx[o["customer_id"]]["name"]`.'''


# customers = [
#     {"id": 1, "name": "Ava"},
#     {"id": 2, "name": "Noah"},
#     {"id": 3, "name": "Mia"},
# ]
# orders = [
#     {"id": 10, "customer_id": 1, "total": 5.00},
#     {"id": 11, "customer_id": 2, "total": 12.00},
#     {"id": 12, "customer_id": 1, "total": 3.50},
# ]

# enriched = []
# idx = {}
# for c in customers:
#     idx[c["id"]] = c

# for o in orders:
#     name = idx[o["customer_id"]]["name"]
#     enriched.append({
#         "order_id" : o["id"],
#         "customer_name": name,
#         "total": o["total"]
#     })  
# for e in enriched:
#     print(e)

'''**B4 — Spot the denormalization** (`norm_check.py`)
Given these two versions of orders, write a comment explaining which is normalized and which is denormalized.
Then write code that changes Ava's name to “Ava S.” and show which version needs multiple updates.'''

# # Version A - Normalized , because he don't have a "custoner_name" separately, only a customer id that already points to the name in customers_a
# customers_a = [{"id": 1, "name": "Ava"}]
# orders_a = [{"id": 10, "customer_id": 1, "total": 5.0}]
# customers_a[0]["name"] = "Ava S"
# # Version B - Denormalized because we added a customer_name key, which will need update every time we change the name in customers_b, otherwise the values won't match anymore
# customers_b = [{"id": 1, "name": "Ava"}]
# orders_b = [{"id": 10, "customer_id": 1, "customer_name": "Ava", "total": 5.0}]
# customers_b[0]["name"] = "Ava S"
# orders_b[0]["customer_name"] = "Ava S"
# print(customers_b)
# print(orders_b)

'''SEMI GUIDED DRILL'''
customers = [
    {"id": 101, "name": "Ava",  "tier": "gold"},
    {"id": 102, "name": "Noah", "tier": "silver"},
    {"id": 103, "name": "Mia",  "tier": "gold"},
]
orders = [
    {"id": 5001, "customer_id": 101, "total": 19.99},
    {"id": 5002, "customer_id": 102, "total": 5.50},
    {"id": 5003, "customer_id": 101, "total": 12.00},
    {"id": 5004, "customer_id": 103, "total": 7.25},
    {"id": 5005, "customer_id": 103, "total": 2.75},
]
idx = {}
for c in customers:
    idx[c["id"]] = c

enriched_orders = []
revenue_by_tier = {}
for o in orders:
    customer = idx[o["customer_id"]]["name"]
    tier = idx[o["customer_id"]]["tier"]
    enriched_orders.append({
        "order_id": o["id"],
        "customer_name": customer,
        "tier" : tier,
        "total": o["total"]
    })


    
    revenue_by_tier[tier] = round(revenue_by_tier.get(tier, 0) + o["total"],2)


highest_rev = 0
max_tier = None


for tier, revenue in revenue_by_tier.items():
    if revenue > highest_rev:
        highest_rev = revenue
        max_tier = tier
for e in enriched_orders:
    print(e)    
print("Revenue by tier:", revenue_by_tier)    
print("Highest revenue:", highest_rev) 
print("Best tier:", max_tier)



#TODO 1: Build customer_index (id -> record)
#TODO 2: Build enriched_orders list[dict] with: order_id, customer_name, tier, total
#TODO 3: Build revenue_by_tier (tier -> sum of totals) from enriched_orders
#TODO 4: Print the tier with the highest revenue (running-max from W3D4)
