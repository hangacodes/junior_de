'''**Scenario:** Parse a messy order record with labeled fields (like `qty=4`) and produce both a human-readable summary and a strict CSV line.

**Requirements:**

1. Split on comma to get 4 chunks.
2. Strip each chunk.
3. Extract `order_id` and `item` directly.
4. For `qty` and `price`: split again on `"="`, strip the value part, then cast to `int` / `float`.
5. Compute `total = qty * price`. Use `round(total, 2)` for clean output.
6. Print a human-readable summary line using an f-string.
7. Build and print a strict CSV line using `.join()`: `ORD-77,wrench,4,19.99,79.96`

**What Could Go Wrong?
** Answer in comments:
 (1) What happens if a field is missing a comma (record has only 3 chunks instead of 4)? 
 (2) What error do you get if `qty=` has no number after it?'''

raw = "  ORD-77 ,  wrench  , qty=  4, price=  19.99  "
parts = raw.split(",")

order_id = parts[0].strip()
item = parts[1].strip()

qty_txt = parts[2].split("=")
price_txt = parts[3].split("=")

qty = float(qty_txt[1].strip())
price = float(price_txt[1].strip())
total = qty * price

clear_sentence = (f"Order id: {order_id}, item: {item} x {qty} pieces @ ${price}. Total: ${total}")
print(clear_sentence)

strict_csv = ",".join([order_id, item, str(qty), str(price), str(total)])
print(strict_csv)

#