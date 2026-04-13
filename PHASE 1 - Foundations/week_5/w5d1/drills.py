# # predict
# def shout(word):
#     return word.upper()

# print(shout("data"))        #DATA
# print(shout)    #SOME NUMBERS WHERE THIS FUNCTION IS SAVED IN MEMORY Nothing basically

# #**A2 — Trace:** Walk through line by line and write the final output.
# def remove_commas(text):
#     return text.replace(",", "")

# cleaned = remove_commas("1,000,000")
# print(cleaned)  #1000000

# #**A3 — Spot the bug:**
# def get_category(line): #it was a missing colon
#     parts = line.split(",")
#     return parts[0].strip()

# print(get_category("food, 12.50"))

# #**A4 — Predict:** What does `result` contain?
# def do_nothing(x):
#     x + 10

# result = do_nothing(5)
# print(result)       #None?

# '''Guided drills:'''
# '''**B1 — Clean currency**

# Task: Write `strip_currency(amount_str)` that removes `"€"` and surrounding whitespace.

# - Hint: Chain `.replace("€", "")` and `.strip()`
# - Test: `strip_currency("€ 1.00")` → `"1.00"` and `strip_currency("€2.50")` → `"2.50"`'''

def strip_currency(amount_str):
    return amount_str.replace("€", "").strip()

# print(strip_currency("€ 1.00"))
# print(strip_currency("€2.50"))

# '''**B2 — Convert to float**

# Task: Write `to_float(number_str)` that converts a cleaned number string to a float.

# - Hint: `return float(number_str)`
# - Test: `to_float("12.50") + 1` → `13.5`'''

def to_float(number_str):
    return float(number_str)

print(to_float("12.50"))

# '''**B3 — Parse a transaction line**

# Task: Write `parse_tx_line(line)` that takes `"food, € 9.99"` and returns `{"category": "food", "amount": 9.99}`.

# - Hint: Split by `","`, clean category with `.strip()`, clean amount with `strip_currency` + `to_float`
# - Test: `parse_tx_line("transport, € 3.00")` → `{"category": "transport", "amount": 3.0}`'''

def parse_tx_line(line):
    parts = line.split(",")
    category = parts[0].strip()
    amount = to_float(strip_currency(parts[1]))
    return {
        "category": category,
        "amount" : amount
    }
# result = parse_tx_line("transport, € 3.00")
# print(result)


'''### 6C) Semi-guided drill

**Aggregator helper + pipeline builder**

Starter code:'''
def add_to_totals(totals, tx):
    """
    totals: dict category -> float total
    tx: dict with keys 'category' and 'amount'
    Update totals in-place and return totals.
    """
    category = tx["category"]
    amount = tx["amount"]
    
    #TODO: update totals using .get(category, 0.0)
    totals[category] = totals.get(category, 0.0) + amount
    #TODO: return totals
    return totals

def build_totals(lines):
    """
    lines: list of strings like 'category, € amount'
    Return totals dict category -> float total.
    """
    totals = {}
    for line in lines:
        tx = parse_tx_line(line)
        add_to_totals(totals, tx)
        

    #TODO: loop over lines
    #TODO: parse each line using parse_tx_line
    #TODO: add each parsed tx to totals

    return totals
lines = ["food, € 2.00", "transport, € 3.00", "food, € 1.50"]

print(build_totals(lines))