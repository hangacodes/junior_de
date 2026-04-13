'''**Requirements:**

- Use these variables (numbers are yours to choose, structure must match): `coffee_qty`, `coffee_price`, `sandwich_qty`, `sandwich_price`, `tax_rate`
- Compute: item totals (`qty * price`), `subtotal`, `tax`, `total`
- Print a receipt with: a title line, one line per item (qty and amount to 2 decimals), subtotal/tax/total (2 decimals), at least one `\n` for readable spacing
**Git checkpoint 4:** Commit with `W1D3: cafe receipt deliverable (f-strings + formatting)`'''

print("\n-> PRIMARY DELIVERABLE <-")
print("-------------------------\n")

coffee_qty = 4
coffee_price = 2.99
sandwich_qty = 3
sandwich_price = 9.49
tax_rate = 0.07

coffee_total = coffee_qty * coffee_price
sandwich_total = sandwich_qty * sandwich_price
subtotal = coffee_total + sandwich_total
tax = subtotal * tax_rate
total = subtotal + tax

print("\t--- RECEIPT ---")
print("-------------------------------------")
print("\nCoffee: {coffee_qty} \t\tprice: ${coffee_total:.2f}")
print(f"Sandwich: {sandwich_qty} \t\tprice: ${sandwich_total:.2f}")
print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
print("-------------------------------------")
print("\n\t===THANK YOU===")
print("\tcome again")