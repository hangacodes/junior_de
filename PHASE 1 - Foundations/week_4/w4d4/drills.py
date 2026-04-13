# '''Example 1 — ⭐⭐Looping over a list of dicts to sum a field'''
# # transactions = [
# #     {"id": "t1", "amount": 4.50},
# #     {"id": "t2", "amount": 12.00},
# #     {"id": "t3", "amount": 3.25},
# # ]

# # total = 0
# # for txn in transactions:
# #     total += txn["amount"]

# # print(round(total, 2))
# '''Example 2 — ⭐⭐⭐ Nested loop over orders → items'''
# # orders = [
# #     {"id": "o1", "items": [{"name": "pen", "price": 2}, {"name": "book", "price": 10}]},
# #     {"id": "o2", "items": [{"name": "pen", "price": 2}]},
# # ]

# # grand_total = 0
# # for order in orders:
# #     for item in order["items"]:     # order["items"] is a list
# #         grand_total += item["price"] # item is a dict

# # print(grand_total)

# '''Example 3 — ⭐⭐⭐ Dict-of-lists: summarizing each group'''
# # by_category = {
# #     "coffee": [4.50, 3.25, 2.75],
# #     "lunch":  [12.00, 8.00],
# # }

# # for cat, amounts in by_category.items():
# #     cat_total = sum(amounts)
# #     print(cat, "-> total:", cat_total, "count:", len(amounts))

# '''### Example 4 — ⭐⭐⭐⭐ Safe access with `.get()` on optional fields'''

# # transactions = [
# #     {"id": "t1", "amount": 10.0, "discount": 2.0},
# #     {"id": "t2", "amount": 8.0},
# #     {"id": "t3", "amount": 5.0, "discount": 1.0},
# # ]

# # net_total = 0
# # for txn in transactions:
# #     net = txn["amount"] - txn.get("discount", 0)
# #     net_total += net

# # print("Net total:", net_total)

# '''What does this print ?'''
# data = [{"a": [10, 20]}, {"a": [30]}]
# print(data[0]["a"][1])      #20
# print(data[1]["a"][0])      #30

# '''**A2 — Trace:** After this runs, what are `type(data)`, `type(data[0])`, `type(data[0]["a"])`, and `type(data[0]["a"][1])`?'''

# data = [{"a": [10, 20]}, {"a": [30]}]

# print(type(data)) # this will be a list
# print(type(data[0])) # this will be a dict
# print(type(data[0]["a"])) # will be a list
# print(type(data[0]["a"][1])) # will be an int

# '''**A3 — Spot:** This code should print `"Ava"` but crashes. What is the error type, and what line is wrong?'''

# people = [{"name": "Ava"}, {"name": "Bo"}]
# print(people[0]["name"])   #is missing [0] to pull the first item in the list - error type ? TypeError i think FK YEAH

# '''**A4 — Predict:** What does this print?'''

# config = {"db": {"host": "localhost", "port": 5432}}
# print(config["db"]["port"] + 1) #5433 - int


# '''**A5 — Trace:** After this loop, what is `total`?'''
# records = [{"v": 3}, {"v": 7}, {"v": 10}]
# total = 0
# for r in records:
#     if r["v"] > 5:
#         total += r["v"]
# print(total)    #17

'''**B1 — Sum nested item prices** (`nested_sum.py`)
Compute and print the total of all item prices across all orders.
**Hint 1:** Outer loop: `for order in orders`. Inner loop: `for item in order["items"]`.
**Hint 2:** Accumulate `item["price"]` into a total.
Given:'''
# orders = [
#     {"id": "o1", "items": [{"price": 2}, {"price": 10}]},
#     {"id": "o2", "items": [{"price": 2}, {"price": 5}]},
# ]

# total = 0

# for order in orders:
#     for item in order["items"]:
#         total += item["price"]

# print(total)

# '''**B2 — Build a dict-of-lists from a list of dicts** (`group_by_cat.py`)
# Build `grouped = {"coffee": [4.50, 3.25], "lunch": [12.00]}` using the grouping pattern from W4D3.
# **Hint:** `grouped.setdefault(cat, []).append(amt)`.
# Given:'''

# transactions = [
#     {"category": "coffee", "amount": 4.50},
#     {"category": "lunch",  "amount": 12.00},
#     {"category": "coffee", "amount": 3.25},
# ]

# grouped = {}
# for d in transactions:
#     cat = d["category"]
#     amt = d["amount"]
#     grouped.setdefault(cat, []).append(amt)
# print(grouped)

# '''**B3 — Dict-of-lists → dict-of-totals** (`group_totals.py`)
# Given the `grouped` dict from B2, produce `totals = {"coffee": 7.75, "lunch": 12.0}`.
# **Hint:** Loop `.items()`, use `sum()` on each list.'''

# totals = {}
# for k, d in grouped.items():
#     totals[k] = sum(d)

# print(totals)


# '''**B4 — Access nested config safely** (`config_reader.py`)
# Print the db host, db port, and app debug value. Then try to access `config["cache"]["ttl"]` safely using `.get()` so it prints `"not configured"` instead of crashing.
# **Hint:** `config.get("cache", {}).get("ttl", "not configured")` chains two safe accesses.
# Given:'''
# config = {
#     "db": {"host": "localhost", "port": 5432},
#     "app": {"debug": True},
# }

# print(config["db"]["host"])
# print(config["db"]["port"])
# print(config["app"]["debug"])

# print(config.get("chace", {}.get("ttl", "not configured")))

transactions = [
    {"id": "t1", "user": "Ava", "category": "coffee", "amount": 4.50},
    {"id": "t2", "user": "Bo",  "category": "lunch",  "amount": 12.00, "discount": 2.00},
    {"id": "t3", "user": "Ava", "category": "coffee", "amount": 3.25},
    {"id": "t4", "user": "Cy",  "category": "lunch",  "amount": 8.00},
]


total = 0
by_category = {}
totals_by_category = {}

#TODO 1: Compute net_total (amount minus discount; discount defaults to 0)
for transaction in transactions:
    total += transaction["amount"] - transaction.get("discount", 0)
    
#TODO 2: Build by_category as a dict-of-lists of amounts

    by_category.setdefault(transaction["category"], []).append(transaction["amount"])
print(by_category)
print(total)

#TODO 3: From by_category, compute totals_by_category (category -> sum)
for k, v in by_category.items():
    totals_by_category[k] = sum(v)
print(totals_by_category)


top_category = None
largest_amt = 0
for cat, total in totals_by_category.items():
    if total > largest_amt:
        largest_amt = total
        top_category = cat

print(top_category)
print(largest_amt)
#TODO 4: Find the top category by total (running-max pattern from W3D4)