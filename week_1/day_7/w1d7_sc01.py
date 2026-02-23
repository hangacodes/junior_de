'''**SC-01 — The cascade**

Given `raw = "  inv-042 | 120 | 0.075 "`, write code that:
1. Splits on `"|"`
2. Strips each part
3. Casts qty to `int` and rate to `float`
4. Computes `total = qty * rate` (keep 2 decimal places using `round()`)
5. Prints: `inv-042: 120 units @ 0.075 = €9.00`
6. Prints a CSV line: `inv-042,120,0.075,9.0`'''

raw = "  inv-042 | 120 | 0.075 "

parts = raw.split("|")
invoice_id = parts[0].strip()

qty = int(parts[1].strip())
price = float(parts[2].strip())
total = round(qty * price)

print(f"{invoice_id} : {qty} units @ {price} = ${total}")
csv_line =",".join([invoice_id, str(qty), str(price), str(total)])
print(csv_line)