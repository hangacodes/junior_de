'''**`parse_order(line: str) -> dict or None`**
- Splits a single line by `" | "`
- If the line doesn’t have exactly 6 fields, return `None`
- If any required field (customer, product) is empty after stripping, return `None`
- If quantity or unit_price can’t convert to number, return `None`
- On success, return a dict:
`{"id": str, "customer":str, "product": str, "quantity": int, "unit_price": float, "status": str}`'''

raw_orders = [
    "ORD001 | Alice | Widget A | 3 | 12.50 | shipped",
    "ORD002 | Bob | Widget B | 1 | 45.00 | pending",
    "ORD003 | Alice | Widget C | 2 | 8.75 | shipped",
    "ORD004 | Charlie | | 5 | 10.00 | shipped",
    "ORD005 | Bob | Widget A | abc | 12.50 | pending",
    "ORD006 | Alice | Widget B | 1 | 45.00 | cancelled",
    "ORD007 | Dave | Widget A | 4 | 12.50 | shipped",
    "ORD008 | | Widget C | 2 | 8.75 | pending",
    "ORD009 | Charlie | Widget B | 1 | | shipped",
    "ORD010 | Bob | Widget A | 2 | 12.50 | shipped",
    "ORD011 | Alice | Widget A | 1 | 12.50 | shipped",
    "ORD012 | Dave | Widget C | 3 | 8.75 | pending",
    "MALFORMED LINE WITH NO PIPES",
    "ORD013 | Charlie | Widget A | 2 | 12.50 | shipped",
    "ORD014 | Alice | Widget B | 1 | 45.00 | shipped",
]
    
def parse_order(line: str) -> dict:
    parts = line.split("|")
    if len(parts) != 6:
        return None

    order_id = parts[0].strip()
    customer = parts[1].strip()
    product = parts[2].strip()
    status = parts[5].strip()
    if customer == "":
        return None
    if product == "":
        return None
    
    try:
        quantity = int(parts[3].strip())
        unit_price = float(parts[4].strip())
    except ValueError:
        return None
   


    return {
        "id": order_id,
        "customer": customer,
        "product": product,
        "quantity": quantity,
        "unit_price": unit_price,
        "status": status
    }

'''**`parse_all_orders(lines: list) -> tuple`**
- Calls `parse_order` on each line
- Returns `(valid_orders_list, rejected_count)`'''

def parse_all_orders(lines:list) -> tuple:
    valid_orders_list = []
    rejected_count = 0
    for line in lines:
        line = parse_order(line)
        if line == None:
            rejected_count += 1
        else:
            valid_orders_list.append(line)
    return valid_orders_list, rejected_count


'''**`compute_order_total(order: dict) -> float`**
- Returns `quantity * unit_price` for a single order'''

def compute_order_total(order: dict) -> float:
    return order["quantity"] * order["unit_price"]


'''**`add_totals(orders: list) -> list`**
- Adds an `"order_total"` key to each order dict
- Calls `compute_order_total` inside
- Returns the updated list'''

def add_totals(orders: list) -> list:
    
    for order in orders:
        order["order_total"] = compute_order_total(order)
        
    return orders


'''**`group_by_status(orders: list) -> dict`**
- Groups orders into a dict-of-lists by their `"status"` value'''

def group_by_status(orders:list)-> dict:
    groupped = {}
    for order in orders:
        groupped.setdefault(order["status"], []).append(order)

    return groupped

'''**`compute_status_summary(grouped: dict) -> dict`**
- For each status, compute: count of orders, total revenue
- Returns: `{"shipped": {"count": N, "revenue": X.XX}, "pending": {...}, ...}`'''
# So i have grouped - a dict where each key is a status and each value is a list of orders
#i need the count and the total revenue for each key
def compute_status_summary(grouped: dict) -> dict:
    status_summary = {}
    for k, v in grouped.items():
        count = len(v)
        total_revenue = 0
        for order in v:
          total_revenue += order["order_total"]
        status_summary[k] = {"count": count,"revenue": round(total_revenue, 2)} 



    return status_summary



'''**`find_top_customer(orders: list) -> tuple`**
- Compute total spending per customer
- Return `(customer_name, total_spent)` for the biggest spender'''

def find_top_customer(orders: list) -> tuple:
    # Step 1: build a dict of customer → total spent
    customer_totals = {}
    for order in orders:
        customer_totals[order["customer"]] = customer_totals.get(order["customer"], 0) + order["order_total"]
    
    # Step 2: find the customer with the highest total
    top_name = None
    top_spent = 0
    for name, spent in customer_totals.items():
        if spent > top_spent:
            top_spent = spent
            top_name = name
    
    return top_name, round(top_spent, 2)


'''**`is_high_value_order(order: dict, threshold: float = 50.0) -> bool`**
- Predicate: returns `True` if `order_total >= threshold`'''


def is_high_value_order(order:dict, threshold: float = 50.0) -> bool:
    return order["order_total"] >= threshold


'''**`generate_summary(orders: list, rejected: int, status_summary: dict, top_customer: tuple) -> str`**
- Returns a formatted report string (does NOT print)
- Include: total processed, rejected count, breakdown by status, top customer, count of high-value orders
'''

def generate_summary(orders:list, rejected: int, status_summary: dict, top_customer:tuple)-> str:
    lines = []
    lines.append("=== ORDER PROCESSING REPORT ===")
    lines.append(f"Lines processed:{len(orders) + rejected}")
    lines.append(f"Valid orders:{len(orders)}")
    lines.append(f"Rejected lines:{rejected}")
    lines.append("")
    lines.append("--- By Status ---")
    for status in sorted(status_summary.keys()):
        info = status_summary[status]
        lines.append(f"{status + ':':11s}{info['count']} orders, ${info['revenue']:.2f} revenue")
    lines.append("")
    top_name, top_spent = top_customer
    lines.append(f"Top customer:{top_name} (${top_spent:.2f})")

    high_value_count = 0
    for order in orders:
        if is_high_value_order(order):
            high_value_count += 1
    lines.append(f"High-value orders (>=$50.00):{high_value_count}")
    lines.append("")
    lines.append("=== END REPORT ===")
    return "\n".join(lines)


def main() -> None:
    raw_orders = [
    "ORD001 | Alice | Widget A | 3 | 12.50 | shipped",
    "ORD002 | Bob | Widget B | 1 | 45.00 | pending",
    "ORD003 | Alice | Widget C | 2 | 8.75 | shipped",
    "ORD004 | Charlie | | 5 | 10.00 | shipped",
    "ORD005 | Bob | Widget A | abc | 12.50 | pending",
    "ORD006 | Alice | Widget B | 1 | 45.00 | cancelled",
    "ORD007 | Dave | Widget A | 4 | 12.50 | shipped",
    "ORD008 | | Widget C | 2 | 8.75 | pending",
    "ORD009 | Charlie | Widget B | 1 | | shipped",
    "ORD010 | Bob | Widget A | 2 | 12.50 | shipped",
    "ORD011 | Alice | Widget A | 1 | 12.50 | shipped",
    "ORD012 | Dave | Widget C | 3 | 8.75 | pending",
    "MALFORMED LINE WITH NO PIPES",
    "ORD013 | Charlie | Widget A | 2 | 12.50 | shipped",
    "ORD014 | Alice | Widget B | 1 | 45.00 | shipped",
]
    orders, rejected = parse_all_orders(raw_orders)
    orders = add_totals(orders)
    grouped = group_by_status(orders)
    status_summary = compute_status_summary(grouped)
    top_customer = find_top_customer(orders)
    report = generate_summary(orders, rejected, status_summary, top_customer)
    print(report)


if __name__ == "__main__":
    main()