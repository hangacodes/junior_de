# class MissingFieldError(Exception):
#     pass
# # ← uses class syntax you'll learn fully in W6D7
# # For now: class Name(Exception): pass is the pattern

# def require_field(record, field_name):
#     if field_name not in record:
#         raise MissingFieldError(f"Missing required field:{field_name}")
#     return record[field_name]

# record = {"id": "A1", "email": "a@example.com"}
# print(require_field(record, "email"))      # output: a@example.com
# # require_field(record, "age")             # raises: MissingFieldError: Missing required field: age

# # class MissingFieldError(Exception):
# #   |          |              |
# #   |          |              +-- inherits from Exception (required)
# #   |          +-- your custom name (describes the domain failure)
# #   +-- keyword: creates a new type  ← covered fully in W6D7

# #   pass  ← empty body is fine; the name + message carry the meaning
# '''### Example 1 — ⭐⭐ Raise vs return None: why raising is clearer

# **What it demonstrates:** `raise` with a message vs returning `None` and losing context'''
# # Bad pattern: None can flow silently through the program
# def parse_age_bad(text):
#     try:
#         return int(text)
#     except ValueError:
#         return None          # caller might forget to check

# # Good pattern: raise stops immediately with context
# def parse_age_good(text):
#     age = int(text)          # let ValueError propagate if not a number
#     if age < 0 or age > 120:
#         raise ValueError(f"age must be 0-120, got{age}")
#     return age

# # The caller decides policy
# for t in ["25", "bad"]:
#     try:
#         print(parse_age_good(t))
#     except ValueError as e:
#         print(f"Rejected:{e}")

# #**A1 — Predict:** What happens when you call `check("")`?
# def check(text):
#     if text == "":
#         raise ValueError("text must not be empty")
#     return text.upper()

# print(check("hello"))
# print(check(""))

# #**A2 — Predict:** What prints before the crash?
# def parse(text):
#     try:
#         return int(text)
#     except ValueError:
#         print(f"DEBUG: parse failed on{text!r}")
#         raise

# # parse("abc")
# #**A3 — Spot:** This custom exception crashes with `TypeError` when raised. Why?
# class BadDataError(Exception):
#     pass

# raise BadDataError("something went wrong")      # because it didn't have (Exception) after the class creation - i added it

#**A4 — Predict:** What does `message` contain?
try:
    raise ValueError("age must be positive")
except ValueError as e:
    message = e
print(type(message))