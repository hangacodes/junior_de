'''**SC-01 — The cascade**

Given `raw = "  inv-042 | 120 | 0.075 "`, write code that:
1. Splits on `"|"`
2. Strips each part
3. Casts qty to `int` and rate to `float`
4. Computes `total = qty * rate` (keep 2 decimal places using `round()`)
5. Prints: `inv-042: 120 units @ 0.075 = €9.00`
6. Prints a CSV line: `inv-042,120,0.075,9.0`

File: `w1d7_sc01.py`

---

**SC-02 — The field normalizer with diagnostics**

Given these three messy column names:

```python
c1 = "  Order-ID  "
c2 = "  RAW__Events-2026.CSV  "
c3 = "Account  Balance"
```

For each one:
1. Normalize to snake_case: strip → lower → replace `-` with `_` → replace spaces with `_` → replace `__` with `_`
2. Print the cleaned value
3. Print whether it ends with `"_id"`, `".csv"`, or neither
4. Print the underscore count

**Trap:** `c2` has double underscores that survive the single replace pass. Handle it — and explain in a comment whether one pass is enough for *triple* underscores.

File: `w1d7_sc02.py`

---

**SC-03 — The ticket parser with arithmetic**

Given `code = "BER-20260209-4821"`:
1. Extract city (slicing)
2. Extract the 8-char date block: `raw_date = code[4:12]`
3. Extract year, month, day from `raw_date` using slicing
4. Compute `ticket_num = int(code[13:17])`
5. Compute `next_ticket = ticket_num + 1`
6. Print a formatted summary:
`City: BER    Date: 2026-02-09    Ticket: 4821    Next available: 4822`
7. Build and print the *next* ticket’s code by assembling parts with `+` and `str()`: `BER-20260209-4822`

File: `w1d7_sc03.py`

---

**SC-04 — The broken record hospital**

This record has problems. Your job is to diagnose each one in comments, then fix the code so it runs and prints a clean CSV line.

```python
raw = "  Ada Lovelace  , 37 , mathematician , 1.70  "
parts = raw.split(",")

name = parts[0]           #BUG 1: not stripped
age = parts[1]            #BUG 2: still a string — math on it will fail
role = parts[2].lower()
height = parts[3].strip() #BUG 3: declared float but not cast

# This should print: True (name starts with "Ada")
print(name.startswith("Ada"))

# This should print age in 10 years: 47
print(age + 10)

# This should print the height rounded to 1 decimal: 1.7
print(round(height, 1))

# This should produce: "Ada Lovelace,37,mathematician,1.7"
csv = ",".join([name, age, role, str(round(height, 1))])
print(csv)
```

Find all 3 bugs, fix them, and write a comment per bug explaining exactly what was wrong.

File: `w1d7_sc04.py`

---

**SC-05 — Time decomposer (no hints)**

Given `total_seconds = 9847`:

1. Compute `hours`, `remaining_after_hours`, `minutes`, `seconds` using `//` and `%` **only** — no division `/`, no subtraction for this part.
2. Print: `2h 44m 7s`
3. Print the total as a formatted string: `02:44:07` (zero-padded — look up `{x:02d}` format specifier on your own and figure out how to use it)

*This one requires you to find something you weren’t explicitly taught. That’s intentional — in real engineering you’ll constantly hit format specifiers you need to look up.*

File: `w1d7_sc05.py`

''' 