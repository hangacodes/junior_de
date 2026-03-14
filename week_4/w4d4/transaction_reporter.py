transactions = [
    {"id": "t1", "user": "Ava", "category": "tech", "amount": 120.00, "discount": 12.00},
    {"id": "t2", "user": "Bo",  "category": "miscellaneous",  "amount": 12.00, "discount": 2.00},
    {"id": "t3", "user": "Ava", "category": "gym", "amount": 50.00},
    {"id": "t4", "user": "Cy",  "category": "lunch",  "amount": 20.00},
    {"id": "t5", "user": "Cristian", "category": "tech", "amount": 83.95, "discount": 3.50},
    {"id": "t6", "user": "John",  "category": "lunch",  "amount": 15.30},
    {"id": "t7", "user": "Michael", "category": "gym", "amount": 50.00},
    {"id": "t8", "user": "George",  "category": "tech",  "amount": 89.99, "discount": 4.00},
    {"id": "t9", "user": "Vlad", "category": "gym", "amount": 50.00},
    {"id": "t10", "user": "Victoria",  "category": "gym",  "amount": 50.00},
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