'''## 5️⃣ REFACTOR B — W4D4 Transaction Reporter

This is your actual `transaction_reporter.py` from Week 4.'''

# transaction_reporter.py — ORIGINAL (flat version)

# Schema: transactions is list[dict]
# Each dict: id (str), user (str), category (str), amount (float), discount (float, optional)

# transactions = [
#     {"id": "t1", "user": "Ava", "category": "tech", "amount": 120.00, "discount": 12.00},
#     {"id": "t2", "user": "Bo",  "category": "miscellaneous",  "amount": 12.00, "discount": 2.00},
#     {"id": "t3", "user": "Ava", "category": "gym", "amount": 50.00},
#     {"id": "t4", "user": "Cy",  "category": "lunch",  "amount": 20.00},
#     {"id": "t5", "user": "Cristian", "category": "tech", "amount": 83.95, "discount": 3.50},
#     {"id": "t6", "user": "John",  "category": "lunch",  "amount": 15.30},
#     {"id": "t7", "user": "Michael", "category": "gym", "amount": 50.00},
#     {"id": "t8", "user": "George",  "category": "tech",  "amount": 89.99, "discount": 4.00},
#     {"id": "t9", "user": "Vlad", "category": "gym", "amount": 50.00},
#     {"id": "t10", "user": "Victoria",  "category": "gym",  "amount": 50.00},
# ]

# total = 0
# by_category = {}
# totals_by_category = {}

# for transaction in transactions:
#     total += transaction["amount"] - transaction.get("discount", 0)
#     by_category.setdefault(transaction["category"], []).append(transaction["amount"])

# print(by_category)
# print(total)


# for k, v in by_category.items():
#     totals_by_category[k] = sum(v)
# print(totals_by_category)


# top_category = None
# largest_amt = 0
# for cat, total in totals_by_category.items():
#     if total > largest_amt:
#         largest_amt = total
#         top_category = cat

# print(top_category)
# print(largest_amt)



'''**Function 1: `compute_net_total(transactions: list) -> float`**
- Takes the list of transaction dicts
- Returns the net total (sum of `amount - discount` for each transaction, where discount defaults to 0)
- Uses `.get("discount", 0)` like your original'''

def compute_net_total(transactions: list) -> float:
    total = 0.0
    for transaction in transactions:
        total += transaction["amount"] - transaction.get("discount", 0.0)
    return total




'''**Function 2: `group_amounts_by_category(transactions: list) -> dict`**
- Takes the list of transaction dicts
- Returns a dict-of-lists: `category → [amount1, amount2, ...]`
- Uses `.setdefault()` like your original'''

def group_amounts_by_category(transactions:list)-> dict:
    by_category = {}
    for transaction in transactions:
        by_category.setdefault(transaction["category"], []).append(transaction["amount"])
    return by_category




'''**Function 3: `compute_category_totals(by_category: dict) -> dict`**
- Takes the grouped dict from Function 2
- Returns a dict mapping each category to its total amount (`sum()` of each list)'''

def compute_category_totals(by_category: dict) -> dict:
    totals_by_category = {}
    for category, amount in by_category.items():
        totals_by_category[category] = sum(amount) 
    return totals_by_category




'''**Function 4: `find_top_category(totals: dict) -> tuple`**
- Returns `(category_name, amount)` for the highest-spending category
- Uses running-max pattern (same as your original)'''

def find_top_category(totals:dict)-> tuple:
    category_name = None
    top_amount = 0

    for category, amount in totals.items():
        if amount > top_amount:
            top_amount = amount
            category_name = category    
    return category_name, top_amount





'''**Function 5: `print_report(transactions: list, net_total: float, by_category: dict, totals: dict, top: tuple) -> None`**
- This is the one function that prints. It produces a formatted report:'''

def print_report(transactions: list, net_total:float, by_category:dict, totals:dict, top: tuple) -> None:
    print("=== TRANSACTION REPORT ===")
    print(f"Transactions: {len(transactions)}")
    print(f"Net total: ${net_total:.2f}")
    print(f"Categories: {len(by_category)}")
    print("\n")
    
    print("--- Totals by Category ---")
    for category, amount in sorted(totals.items()):
        print(f"  {category}: ${amount:.2f} ({len(by_category[category])} transactions)")
    categ, amount= top
    print("\n")
    print(f"Top category: {categ} (${amount:.2f})")
    print("=== END REPORT ===")

    
'''**Function 6: `main() -> None`**
- Defines `transactions`
- Calls functions 1–5 in order
- Passes results from each step to the next'''


def main() -> None:
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


    net_total = compute_net_total(transactions)
    by_category = group_amounts_by_category(transactions)
    totals = compute_category_totals(by_category)
    top = find_top_category(totals)
    print_report(transactions, net_total, by_category ,totals, top)

if __name__ == "__main__":
    main()