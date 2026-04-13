def strip_currency(amount_str):
    return amount_str.replace("€", "" ).strip()

def to_float(number_str):
    return float(number_str)

def parse_tx_line(line):
    parts = line.split(",")
    category = parts[0].strip()
    amount = to_float(strip_currency(parts[1]))
    return {
        "category":category,
        "amount": amount
    }
def add_to_totals(totals, tx):
    category = tx["category"]
    amount = tx["amount"]

    totals[category] = totals.get(category, 0.0) + amount

    return totals

def build_totals(lines):
    totals = {}
    for line in lines:
        tx = parse_tx_line(line)
        add_to_totals(totals, tx)
    return totals

lines = [
    "food, € 2.00",
    "transport, € 3.00",
    "food, € 1.50",
    "books, € 10.00"
]
print(build_totals(lines))
def print_report(totals):
    print("=== Totals ===")
    print(build_totals(lines))
        

print(print_report(build_totals(lines)))