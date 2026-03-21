# #**A1 (Predict):** What does this print?
# def is_short(text: str) -> bool:
#     if len(text) > 5:
#         return False

# print(is_short("hi"))   #True--- WRONG _ false 
# #**A1:** `None`. The `if` branch returns `False` for long strings, but for short strings like `"hi"`, execution falls through without hitting any `return` — Python returns `None`.


# #**A2 (Spot):** This function has a bug. What does it return for `is_even(7)` and why?

# def is_even(n: int) -> bool:
#     if n % 2 == 0:
#         return True
    
# print(is_even(7)) # same issue like above, The program is not told what to do if the n % 2 != 0...so it returns None

# #**A3 (Predict):** For each value, write `truthy` or `falsy`: `""`, `"0"`, `0`, `[]`, `[0]`, `None`.

# ''' 
# "" - falsy;
# "0" truthy ( non empty string);
# 0 falsy ;
# [] empty list - falsy;
# [0] non empty list - truthy;
# None-  Falsy '''

# #**A4 (Trace):** After sanitization, what does `email` equal inside the function?

# def check(email: str) -> bool:
#     email = email.strip().lower()       #email will be == with ada@example.com
#     return "@" in email

# check("  Ada@Example.COM  ")    # this will return true

# '''Guided Drills'''

# '''### Drill 1 — `is_blank_or_spaces` (sanitization + predicate)

# Write `is_blank_or_spaces(text: str) -> bool` that returns `True` if `text` is empty or contains only spaces.'''

# def is_blank_or_spaces(text: str) -> bool:
#     if text.strip() == "":
#         return True
#     else:
#         return False
    
# '''### Drill 2 — `has_dot_after_at` (string methods + guard clauses)

# Write `has_dot_after_at(email: str) -> bool` that returns `True` only if the email has exactly one `@` and a `.` somewhere after it. Sanitize with strip/lower first.'''

# def has_dot_after_at(email:str) -> bool:
#     cleaned = email.strip().lower()
#     pos = cleaned.find("@")
#     if "@"  in cleaned and "."  in cleaned[pos+1:] and cleaned.count("@") == 1:
#         return True    
#     else:
#         return False


# '''### Drill 3 — `is_valid_country_code` (character checking + guard)

# Write `is_valid_country_code(code: str) -> bool`. Valid if, after strip and upper, it’s exactly 2 characters and both are letters A–Z.

# **Hint:** Loop through characters, check `ch >= "A" and ch <= "Z"`.'''

# def is_valid_country_code(code:str)->bool:
#     cleaned = code.strip().upper()
#     if len(cleaned) != 2:
#         return False
  
#     for ch in cleaned:
#         if ch < 'A' or ch > 'Z':
#             return False
#     return True
    

'''### Drill 4 — `is_valid_score` (try/except + range check from W2D5)

Write `is_valid_score(text: str) -> bool`. Sanitize, then try converting to `int`. Valid if conversion succeeds and value is 0–100 inclusive.

**Hint:** Wrap `int(text.strip())` in `try/except ValueError`.'''

def is_valid_score(text: str) -> bool:
    text = text.strip()
    if text == "":
        return False
    try:
        score = int(text)
        if score >= 0 and score <= 100:
            return True
        else: return False
    except ValueError:
        return False