##predict
# def f():
#     x = 10

# print(f())        #NONE

##spot the bug
# def area_rectangle(w, h):
#     #print(w * h)        #this should be return w * h
#     return w * h
# a = area_rectangle(3, 4)
# print("area:", a)

# #**A3 — Predict:** What prints on each line?
# def safe_divide(a, b):
#     if b == 0:
#         return None
#     return a / b

# print(safe_divide(10, 2))   #5
# print(safe_divide(10, 0))   #None

# #**A4 — Trace:** What is `result`?
# def double(n):
#     return n * 2

# result = double(double(3))
# print(result)   #6 ?...got this one wrong is 6 * 2 lol


'''**B1 — `parse_int_or_none(text)`**

Write a function that strips whitespace, checks `.isdigit()`, and returns `int(text)` or `None`.

- Hint: `.strip()` first, then `.isdigit()` check
- Test: `parse_int_or_none(" 42 ")` → `42`, `parse_int_or_none("x")` → `None`, `parse_int_or_none("")` → `None`'''

# def parse_int_or_none(text):
#     text = text.strip()
#     if not text.isdigit():
#         return None
#     return int(text)

# result = parse_int_or_none(" 42 ")
# result1 = parse_int_or_none("x")
# result2 = parse_int_or_none("")
# print(result)
# print(result1)
# print(result2)

'''**B2 — `tip_amount(bill, pct)`**

Return the tip (not the total). Example: `tip_amount(50, 0.10)` → `5.0`'''

# def tip_amount(bill, pct):
#     return bill * pct
# print(tip_amount(50, 0.10))

'''**B3 — Refactor print to return**

Given this “printy” function:'''
# def shout(name):
#     #print(name.strip().lower())
#     return name.strip().lower()
# #Refactor it to return the cleaned name, then use the returned value inside an f-string.

# name = shout("Maria")

# print(f"{name} come here!")

'''SEMI-GUIDED
**`normalize_order(order)` — returns a NEW dict**

Given an order dict like `{"customer": "  Mina  ", "city": " HELSINKI ", "qty": "3", "unit_price": " 19 "}`, write `normalize_order(order)` that returns a new dict with `customer` and `city` stripped+lowered, and `qty` and `unit_price` as integers (or `None` if invalid).

Starter code:'''
def parse_int_or_none(text):
    text = text.strip()
    if text.isdigit():
        return int(text)
    return None

def normalize_order(order):
    normalized = {
        "customer" : order["customer"].strip().lower(),
        "city" : order["city"].strip().lower(),
        "qty": parse_int_or_none(order["qty"]),
        "unit_price": parse_int_or_none(order["unit_price"])
        }
    
    #TODO: clean customer and city using .strip().lower()
    #TODO: parse qty and unit_price using parse_int_or_none
    return normalized


o = {"customer": "  Mina  ", "city": " HELSINKI ", "qty": "3", "unit_price": " 19 "}
print(normalize_order(o))
# {'customer': 'mina', 'city': 'helsinki', 'qty': 3, 'unit_price': 19}