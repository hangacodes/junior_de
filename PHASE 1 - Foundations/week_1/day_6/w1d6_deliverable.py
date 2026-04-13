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
       
'''This went pretty smootly.
I parsed the qty and price directly without doing parts and then qty_text separately and then qty = int(qty_text) 
- the answer key from the lesson attached below, did it separately
Did I do it wrong?'''

'''### 10C) Primary Deliverable Solution


raw = "  ORD-77 ,  wrench  , qty=  4 , price=  19.99  "
parts = raw.split(",")

order_id = parts[0].strip()
item = parts[1].strip()

qty_part = parts[2].strip()          # "qty=  4"
price_part = parts[3].strip()        # "price=  19.99"

qty_text = qty_part.split("=")[1].strip()
price_text = price_part.split("=")[1].strip()

qty = int(qty_text)
price = float(price_text)
total = round(qty * price, 2)

print(f"Order{order_id}:{item} x{qty} @{price} ={total}")

csv_line = ",".join([order_id, item, str(qty), str(price), str(total)])
print(csv_line)

# What Could Go Wrong?
# 1) Missing comma: parts has only 3 elements instead of 4.
#    parts[3] raises IndexError: list index out of range.
# 2) qty= with no number: qty_part.split("=")[1] gives "" (empty string).
#    int("") raises ValueError: invalid literal for int() with base 10: ''
'''