# '''### Example 1 — ⭐⭐ Multiple exception types with different handling

# **What it demonstrates:** catching `ValueError` and `ZeroDivisionError` separately + `else` for success'''
# def compute_rate(count_text, total_text):
#     try:
#         count = int(count_text)
#         total = int(total_text)
#         rate = count / total
#     except ValueError as e:
#         print(f"  Bad number:{e}")
#         return None
#     except ZeroDivisionError:
#         print(f"  Division by zero: total={total_text}")
#         return None
#     else:
#         return round(rate, 4)

# pairs = [("25", "200"), ("10", "0"), ("abc", "50"), ("30", "300")]
# for c, t in pairs:
#     result = compute_rate(c, t)
#     print(f"  ({c},{t}) ->{result}")

# '''### Example 2 — ⭐⭐⭐ `finally` for guaranteed counting in a data pipeline

# **What it demonstrates:** `finally` increments a counter regardless of success or failure + tuple syntax for shared handling + combining with W4 dict counter pattern'''
# def load_records(raw_lines):
#     records = []
#     stats = {"processed": 0, "loaded": 0, "rejected": 0}

#     for line in raw_lines:
#         try:
#             parts = line.split("|")
#             name = parts[0].strip().title()
#             score = int(parts[1].strip())
#         except (ValueError, IndexError) as e:
#             # Tuple syntax: both errors get the same handler
#             # as e gives us the specific message for the log
#             stats["rejected"] += 1
#             print(f"  Reject ({e}):{line.strip()}")
#         else:
#             records.append({"name": name, "score": score})
#             stats["loaded"] += 1
#         finally:
#             stats["processed"] += 1

#     return records, stats

# lines = ["Ada|88", "Bob|bad", "Cara", "Dee|91"]
# records, stats = load_records(lines)
# print("Records:", records)
# print("Stats:", stats)

# ''' "Bob|bad" fails on int("bad") → ValueError.
# "Cara" has no |, so parts[1] raises IndexError.
# Both are caught by except (ValueError, IndexError) — tuple syntax means one block handles both.
# type(e).__name__ prints the exception’s class name as a string, which distinguishes them in the log without needing separate handlers.
# finally increments processed for every line — this guarantees processed == loaded + rejected.'''

# '''### Example 3 — ⭐⭐⭐ Reading a traceback to find the real problem

# **What it demonstrates:** traceback anatomy + the “bottom-up” reading habit'''
# def clean_field(text):
#     return text.strip().lower()

# def parse_sensor(line):
#     parts = line.split(",")
#     station = clean_field(parts[0])
#     temp = float(clean_field(parts[1]))
#     unit = clean_field(parts[4])         # crashes if only 2 fields
#     return {"station": station, "temp": temp, "unit": unit}

# # This line triggers the crash:
# print(parse_sensor("StationA, 22.5"))

'''### Example 4 — ⭐⭐⭐⭐ Combining exception handling with a reusable module

**What it demonstrates:** building a robust parsing module + using it from a script + `__main__` guard + all four `try` clauses + `as e` for error logging'''
# file: run_loader.py
import row_parser

lines = ["101|Ada|19.99", "BAD|Bob|5.00", "103|Cara", "104|Dee|12.50"]
loaded = []
errors = []
count = 0

for line in lines:
    try:
        record = row_parser.parse_record(line)
    except (ValueError, IndexError) as e:
        errors.append({"line": line, "error": str(e)})
    else:
        loaded.append(record)
    finally:
        count += 1

print(f"Processed:{count}, Loaded:{len(loaded)}, Errors:{len(errors)}")
for err in errors:
    print(f"  REJECT:{err['line']} ->{err['error']}")
'''💡 The module (`row_parser.py`) is “dumb” — it parses or crashes.
The script (`run_loader.py`) is “smart” — it catches exceptions, logs errors with context using `as e`, and keeps going.
`str(e)` converts the exception object to its message string so it can be stored in the dict.
This separation is a common pattern in real pipelines: parsing functions throw, callers catch.'''