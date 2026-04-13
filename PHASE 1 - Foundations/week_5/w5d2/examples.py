# def tag(label, value):
#     return label + "=" + str(value)

# items = ["food", "transport", "books"]
# results = []
# for item in items:
#     if len(item) > 4:
#         results.append(tag("long", item))
# print(results)

# def greet(name):
#     print(f"Hello, {name}!")

# value = greet("Mina")

# def find_first_negative(numbers):

#     for n in numbers:
#         if n < 0:
#             return n
#     return None

# print(find_first_negative([3, -1, -2]))
# print(find_first_negative([3, -1, 5]))
# print(find_first_negative([3, 1, -25]))
# def wrong_total(a, b):
#     print(a + b)             # shows 7, but returns None

# def right_total(a, b):
#     return a + b             # returns 7

# x = wrong_total(2, 5)
# y = right_total(2, 5)
# print("x is:", x)
# print("y is:", y)
# print("y + 10 =", y + 10)

'''### Example 1 — ⭐⭐ Return + reuse

**What it demonstrates:** return value, storing and reusing the result'''
def add_tax(price, rate):
    return price * (1 + rate)

final = add_tax(100, 0.24)
print("Final:", final)
discounted = final - 10
print("After discount:", discounted)

#❓ PREDICT: What two numbers print?
#124
#114

'''### Example 2 — ⭐⭐⭐ Early return for safe parsing

**What it demonstrates:** early return, `None` as intentional signal, `.isdigit()` validation'''
# def parse_int_or_none(text):
#     text = text.strip()
#     if not text.isdigit():
#         return None
#     return int(text)
# #SKIP THIS SECOND PART IS FKING USELESS
# values = ["42", " 7 ", "oops", "", "100"]
# for v in values:
#     result = parse_int_or_none(v)
#     if result is not None:
#         print(f"{v!r} →{result}")
#     else:
#         print(f"{v!r} → skipped (invalid)")

'''### Example 3 — ⭐⭐⭐ Composition pipeline

**What it demonstrates:** function composition, pure functions chained together'''

# def clean_text(text):
#     return text.strip().lower()

# def is_valid_name(name):
#     cleaned = clean_text(name)
#     return len(cleaned) > 0

# def normalize_record(record):
#     return {
#         "name": clean_text(record["name"]),
#         "city": clean_text(record["city"])
#     }

# raw = {"name": "  ADA  ", "city": " LONDON "}
# if is_valid_name(raw["name"]):
#     normed = normalize_record(raw)
#     print(normed)

'''### Example 4 — ⭐⭐⭐⭐ Multiple return values + None handling in a real pipeline

**What it demonstrates:** multiple return values, None guard, accumulator with composition'''
def parse_order(order):
    qty = order["qty"].strip()
    price = order["unit_price"].strip()
    if not qty.isdigit() or not price.isdigit():
        return None, None
    return int(qty), int(price)

def order_revenue(order):
    qty, price = parse_order(order)
    if qty is None:
        return None
    return qty * price

orders = [
    {"name": "Mina", "qty": "3", "unit_price": "19"},
    {"name": "Olli", "qty": "2", "unit_price": "10"},
    {"name": "Sara", "qty": "x", "unit_price": "5"},
]

total = 0
valid = 0
for o in orders:
    rev = order_revenue(o)
    if rev is not None:
        total = total + rev
        valid = valid + 1

print(f"Valid orders:{valid}, Total revenue:{total}")