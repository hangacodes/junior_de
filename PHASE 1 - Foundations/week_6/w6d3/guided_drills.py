# '''### Drill 1: `safe_float` with `else`

# Write `safe_float(text)` that tries to convert text to float. On `ValueError`, return `None`. On success (use `else`), return the float value. Test with `["12.5", "N/A", "7", ""]`.

# **Hint 1:** Put `float(text.strip())` in `try` — strip first to handle `" 12.5 "`.
# **Hint 2:** Return the value in `else`, not inside `try` — this keeps success logic separate.

# File: `safe_float.py`'''
# def safe_float(text):
#     try:
#         value = float(text.strip())
#     except ValueError:
#         return None
#     else:
#         return value
    
# txt = ["12.5", "N/A", "7", ""]
# for value in txt:
#     print(safe_float(value))


# '''### Drill 2: `safe_divide` with multiple except blocks

# Write `safe_divide(a_text, b_text)` that converts both to int and divides.
# Return `None` for `ValueError` (bad number) and `None` for `ZeroDivisionError` (divide by zero), with different print messages for each.
# Use `as e` on at least one handler and include the exception message in the print. Test with `[("10","2"), ("10","0"), ("x","2")]`.

# **Hint 1:** You need two separate `except` blocks — `ValueError` first, then `ZeroDivisionError`.
# **Hint 2:** Combine with W5D5 pattern: return `None` as a sentinel so the caller can check.

# File: `safe_divide.py`'''


# def safe_divide(a_text, b_text):
#     try:
#         divided = int(a_text.strip()) / int(b_text.strip())
#     except ValueError as e:
#         print(f"Bad number:{e}")
#         return None
#     except ZeroDivisionError as e:
#         print(f"Devision by zero:{e}")
#         return None
#     else:
#         return divided
# lst = [("10","2"), ("10","0"), ("x","2")]
# for values in lst:
#     a , b = values


#     print(safe_divide(a, b))

'''### Drill 3: `parse_required_key` with `KeyError`

Write `parse_required_key(record, key)` that accesses `record[key]` inside `try`.
Return `None` on `KeyError`. Use `as e` and include the missing key in your print message.
Test with `{"user_id": "101"}` looking up `"user_id"` and `"age"`.

**Hint:** Dict access `record[key]` raises `KeyError` when the key doesn’t exist — don’t use `.get()` here because the whole point is practicing exception handling.

File: `parse_key.py`'''

def parse_required_key(record, key):

        try:
            the_key = record[key]
        except KeyError as e:
            print(f"Missing key: {e!r}")
            return None
        else:
            return the_key
        
record = {"user_id": "101"}
print(parse_required_key(record, "user_id"))
print(parse_required_key(record, "age"))

