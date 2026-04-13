# '''**Drill 1 (Predict):** What does `"name,age,city".split(",")` return?'''

# #[name, age, city]

# '''**Drill 2 (Predict):** Given `headers = ["name", "age"]` and `fields = ["Ada", "29"]`, what dict do you get if you pair them by index?'''

# #{ "name": " Ada" , "age": "29"}

# '''**Drill 3 (Spot):** This code is supposed to split `'A,"B,C",D'` into 3 fields but produces 4. Why?
# row = 'A,"B,C",D'
# fields = row.split(",")
# print(fields)
# '''

# #It produces 4 because is not quote aware, doesn't use the cvs_line_split function that only splits (",") if is not between " " - here, "B,C" is one field

# '''**Drill 4 (Trace):** After running `int("42")`, what type and value do you have? After `int("not_a_number")`, what happens?'''

# #running int("42") gives me a int - 42
# #running int("not_a_number") raises ValueError


# '''### 6B — Guided Drills

# **Drill 1: Write `split_csv_line(line)`**
# File name: `csv_splitter.py`

# Implement the quote-aware splitter from Term 3. Test it with `'A,"B,C",D'` → `["A", "B,C", "D"]`.

# Hint 1: Use a `while` loop and an `in_quotes` boolean.
# Hint 2: Only split on comma when `in_quotes` is `False`.'''

# def split_csv_line(line, delimiter= ","):
#     fields = []
#     current = ""
#     in_quotes = False

#     i = 0
#     while i <len(line):
#         ch = line[i]
#         if ch == '"':
#             in_quotes = not in_quotes
#         elif ch == delimiter and not in_quotes:
#             fields.append(current)
#             current = ""
#         else:
#             current += ch
#         i += 1

#     fields.append(current)
#     return fields

# print(split_csv_line('A,"B,C",D'))
# '''**Drill 2: Parse header + one data row into a dict**
# File name: `row_to_dict.py`

# Given `header_line = "name,age,city"` and `data_line = "Ada,29,Berlin"`, parse both and produce `{"name": "Ada", "age": "29", "city": "Berlin"}`.

# Hint 1: Split the header line to get keys.
# Hint 2: Split the data line to get values.
# Hint 3: Use a `for` loop with `range(len(headers))` to pair them.'''

# header_line = "name,age,city"
# data_line ="Ada,29,Berlin"

# headers = split_csv_line(header_line)
# fields = split_csv_line(data_line)
# record = {}
# for i in range(len(headers)):
#         record[headers[i]] = fields[i]

# print(record)


# '''**Drill 3: Detect wrong field count**
# File name: `field_check.py`

# Write a function `check_field_count(headers, fields, row_num, raw_line)` that returns an error dict if `len(fields) != len(headers)`, or `None` if they match.

# Hint 1: Return `{"row": row_num, "error": "wrong field count", "raw": raw_line}` on mismatch.
# Hint 2: Return `None` when counts match.'''

# def check_field_count(headers, fields, row_num, raw_line):
#     if len(fields) != len(headers):
#         return {"row":row_num ,"error":"wrong field count", "raw":raw_line}
#     else:
#         return None


# '''**Drill 4: Cast one record using a schema**
# File name: `cast_demo.py`

# Write a function that takes `record = {"name": "Ada", "age": "29"}` and `schema = {"age": int}`,
# and returns a typed version where `"29"` becomes `29`. If casting fails, return `None` and an error message.

# Hint 1: Loop through `schema.items()` — only cast fields listed in the schema.
# Hint 2: Use `try/except ValueError` around the cast.'''

# record = {"name": "Ada", "age": "29"}
# schema = {"age": int}

# def cast_record(record, schema):
#     typed = {}

#     for key in record:
#         typed[key] = record[key]

#     for col in schema:
#         target_type = schema[col]
#         value = record[col].strip()

#         if value == "":
#             return None, f"Empty value for required column:{col}"
        
#         try:
#             typed[col] = target_type(value)
#         except ValueError:
#             return None, f"Cannot cast '{value}' to {target_type.__name__} for column '{col}'"

#     return typed, ""

