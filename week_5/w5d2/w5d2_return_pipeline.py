def clean_text(text):
    return text.strip().lower()

def parse_int_or_none(text):
    text = text.strip()
    if not text.isdigit():
        return None
    return int(text)

def line_total(qty, unit_price):
    if qty is not None and unit_price is not None:
        return qty * unit_price
    return None
def normalize_order(order):
    normalized = {
        "customer": clean_text(order["customer"]),
        "city": clean_text(order["city"]),
        "qty": parse_int_or_none(order["qty"]),
        "unit_price": parse_int_or_none(order["unit_price"])

    }
    return normalized
    
def order_total(order):
    result = normalize_order(order)
    qty = result["qty"]
    unit_price = result["unit_price"]
    return line_total(qty, unit_price)

def sum_revenue(orders):
    total = 0
    for o in orders:
        rev = order_total(o)
        if rev is not None:
            total += rev
    return total

def count_valid(orders):
    count = 0
    for o in orders:
        if order_total(o) is not None:
            count += 1
    return count

def revenue_report(orders):
    total_revenue = sum_revenue(orders)
    valid_count = count_valid(orders)
    return valid_count, total_revenue

orders = [
    {"customer": "  Mina  ", "city": " HELSINKI ", "qty": "3", "unit_price": " 19 "},
    {"customer": "Olli", "city": "Espoo", "qty": "2", "unit_price": "10"},
    {"customer": "Sara", "city": " Vantaa ", "qty": "x", "unit_price": "5"},
    {"customer": "Lee", "city": "Turku", "qty": "1", "unit_price": "oops"},
]

def run_tests():
    if clean_text(" HELLO ") == "hello":
        print("clean_text: PASS")
    else:
        print("clean_text: FAIL")

    if parse_int_or_none("12") == 12:
        print("parse_int_or_none: PASS")
    else:
        print("parse_int_or_none: FAIL")
    
    if line_total(3, 4) == 12:
        print("line_total: PASS")
    else:
        print("line_total: FAIL")

    if normalize_order({"customer": "  Mina  ", "city": " HELSINKI ", "qty": "3", "unit_price": " 19 "}) == {'customer': 'mina', 'city': 'helsinki', 'qty': 3, 'unit_price': 19}:
        print("normalize_order: PASS")
    else:
        print("normalize_order: FAIL")

    if order_total({"customer": "  Mina  ", "city": " HELSINKI ", "qty": "3", "unit_price": " 19 "}) == 57:
        print("order_total: PASS")
    else:
        print("order_total: FAIl")

    if sum_revenue(orders) == 77:
        print("sum_revenue: PASS")
    else:
        print("sum_revenue: FAIL")
    
    if count_valid(orders) == 2:
        print("count_valid: PASS")
    else:
        print("count_valid: FAIL")

    if revenue_report(orders) == (2, 77):
        print("revenue_report: PASS")
    else:
        print("revenue_report: FAIL")

    if clean_text("  ") == "":
        print("clean_text: PASS")
    else:
        print("clean_text: FAIL")

run_tests()

for o in orders:
    normed = normalize_order(o)
    total = order_total(o)
    if total is None:
        print(f"{normed['customer']} — INVALID order")
    else:
        print(f"{normed['customer']} — valid, total: {total}")
print(revenue_report(orders))