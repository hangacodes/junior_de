#Guided drills
'''**Drill 1: Parse and clean a CSV row**
Given `row = "  Alice   ,  29  ,  Berlin  "`, split on comma, strip each field, cast age to `int`, and print name, age + 1, and city on separate lines.
*Hint:* `parts = row.split(",")`, then `.strip()` each part, then `int()` the age.'''

row = "  Alice   ,  29  ,  Berlin  "

parts = row.split(",")
print(parts)
name = parts[0].strip()
age_text = parts[1].strip()
city = parts[2].strip()
age = int(age_text)

print(name)
print(age + 1)
print(city)

'''**Drill 2: Build a CSV line with .join()**
Given `name = "Ada Lovelace"`, `age = 37`, `country = "DE"`, produce exactly `"Ada Lovelace,37,DE"` using `.join()`.
*Hint:* `.join()` needs a list of strings — use `str(age)`.'''

name = "Ada Lovelace"
age = 37
country = "DE"
age_text = str(age)
csv = (",").join([name, age_text, country])
print(csv)

'''**Drill 3: Parse a pipe-delimited invoice**
Given `raw = "  INV-009 |  nails  |  120  |  0.07  "`, split on `"|"`, strip each field, cast qty to `int` and price to `float`, compute total, and print a summary line with an f-string.
*Hint:* `total = qty * price`. Use `round(total, 2)` if the result has ugly decimals.'''

raw = "  INV-009 |  nails  |  120  |  0.07  "
parts1 = raw.split("|")
invoice_id = parts1[0].strip()
item = parts1[1].strip()
qty_txt = parts1[2].strip()
price_txt = parts1[3].strip()
qty = int(qty_txt)
price = float(price_txt)

total = qty * price
print(f"Receipt code: {invoice_id}, item: {item} ,quantity: {qty}, price for each piece: {price}. The total is: {total}")

'''**Drill 4: Whitespace-split a log line**
Given `log = "WARN   2026-02-09   service=billing   code=503"`, split on whitespace (no argument), and print the severity level (token 0) and the service token (token 2).
*Hint:* `.split()` with no argument handles the irregular spacing.'''

log = "WARN   2026-02-09   service=billing   code=503"

parts2 = log.split()
print(parts)        #just making sure it worked
print(type(parts))  #making sure is a list

print(parts2[0])
print(parts2[2])


#Confusing : how to name each part from raw = "  INV-009 |  nails  |  120  |  0.07  "....
#This took me 18 minutes, shit is getting serious I really had to think about these, the first 5 days were much easier


#Semi-Guided : Task: Parse a messy invoice record and produce clean output.
raw = "  INV-042 |  bolts  |  250  |  0.12  "
parts3 = raw.split("|")

#TODO: Strip each part and store in invoice_id, item, qty (int), price (float)
#TODO: Compute total_cost = qty * price
#TODO: Print a human-readable summary using an f-string
#TODO: Build and print a strict CSV line: "INV-042,bolts,250,0.12,30.0"
#       using .join() — remember str() for numbers

invoice_id2 = parts3[0].strip()
item2 = parts3[1].strip()
qty2 = int(parts3[2].strip())
price2 = float(parts3[3].strip())

total_cost = qty2 * price2

summary = (f"Invoice id: {invoice_id2}, item: {item2} x {qty2} pieces @ ${price2}. Total cost : ${total_cost}")
print(summary)
strict_csv = ",".join([invoice_id2, item2, str(qty2), str(price2), str(total_cost)])
print(strict_csv)