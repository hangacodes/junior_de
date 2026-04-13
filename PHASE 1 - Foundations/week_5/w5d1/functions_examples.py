'''### Example 1 — ⭐⭐ Define vs call + return

**What it demonstrates:** function definition, calling, return value'''
# def wrap_brackets(text):
#     return "[" + text + "]"

# label = wrap_brackets("food")
# print(label)
# print(wrap_brackets("transport"))

'''### Example 2 — ⭐⭐ Parameters + arguments with real data

**What it demonstrates:** parameter, argument, combining with dict operations'''

# def add_to_totals(totals, category, amount):
#     totals[category] = totals.get(category, 0.0) + amount
#     return totals

# running = {}
# add_to_totals(running, "food", 2.0)
# add_to_totals(running, "food", 3.5)
# add_to_totals(running, "transport", 1.0)
# print(running)


'''### Example 3 — ⭐⭐⭐ Call stack with functions calling functions

**What it demonstrates:** call stack, nested calls, separate frames'''

# def strip_currency(raw):
#     return raw.replace("€", "").strip()

# def parse_tx(line):
#     parts = line.split(",")
#     category = parts[0].strip()
#     amount = float(strip_currency(parts[1]))
#     return {"category": category, "amount": amount}

# tx = parse_tx("books, € 10.00")
# print(tx)

'''### Example 4 — ⭐⭐⭐ Planning with `pass` then implementing

**What it demonstrates:** `pass` as a planning tool, incremental implementation'''

# # Step 1: sketch the shapes
# def clean_field(text):
#     pass

# def build_record(line):
#     pass

# # Step 2: implement one at a time
# def clean_field(text):
#     return text.strip().lower()

# def build_record(line):
#     parts = line.split(",")
#     return {
#         "name": clean_field(parts[0]),
#         "city": clean_field(parts[1])
#     }

# print(build_record("  Ada ,  LONDON "))

