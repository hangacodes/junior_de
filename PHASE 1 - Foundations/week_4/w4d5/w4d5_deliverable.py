#Schema:
#There are 2 lists of dicts: customers and orders
#Customers keys: id, name, tier; Orders keys: id, customer_id and total.
#Each customer can have multiple orders
customers = [
    {"id": 101, "name": "Ava",  "tier": "gold"},
    {"id": 102, "name": "Noah", "tier": "silver"},
    {"id": 103, "name": "Mia",  "tier": "gold"},
    {"id": 104, "name": "Chris",  "tier": "platinum"},
    {"id": 105, "name": "Gucci", "tier": "platinum"},
    {"id": 106, "name": "Victoria",  "tier": "gold"}
]
orders = [
    {"id": 5001, "customer_id": 101, "total": 19.99},
    {"id": 5002, "customer_id": 102, "total": 5.50},
    {"id": 5003, "customer_id": 101, "total": 12.00},
    {"id": 5004, "customer_id": 103, "total": 7.25},
    {"id": 5005, "customer_id": 104, "total": 69.99},
    {"id": 5006, "customer_id": 105, "total": 38.00},
    {"id": 5007, "customer_id": 106, "total": 10.50},
    {"id": 5008, "customer_id": 104, "total": 99.00},
    {"id": 5009, "customer_id": 105, "total": 27.25},
    {"id": 5010, "customer_id": 102, "total": 11.75},
]
idx = {}
for c in customers:
    idx[c["id"]] = c

enriched_orders = []
revenue_by_tier = {}
for o in orders:
    cust = idx.get(o["customer_id"], None)
    if cust is None:
        continue
    customer = cust["name"]
    tier = cust["tier"]
    enriched_orders.append({
        "order_id": o["id"],
        "customer_name": customer,
        "tier" : tier,
        "total": o["total"]
    })

    revenue_by_tier[tier] = round(revenue_by_tier.get(tier, 0) + o["total"],2)

for e in enriched_orders:
    print(e)
print("Orders lenght:", len(enriched_orders))
print("Revenues by tier:")
for k,v in revenue_by_tier.items():
    print(k,"-",v)

highest_rev = 0
max_tier = None


for tier, revenue in revenue_by_tier.items():
    if revenue > highest_rev:
        highest_rev = revenue
        max_tier = tier
  
print("Highest revenue:", highest_rev) 
print("Best tier:", max_tier)