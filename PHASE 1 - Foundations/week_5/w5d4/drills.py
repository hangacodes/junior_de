# '''### 6A — Activation Drills

# **A1 (Predict):** What does this print?'''

# def f(a, b=10, c=20):
#     return a + b + c

# print(f(1, c=5))

# #1 + 10 + 5 = 16


# #**A2 (Spot):** This signature causes a `SyntaxError`. Which line is broken and why?

# def parse(line=",", sep=', '):   #this line had sep only without sep=None or sep=", " ( basically sep was not defined) 
#     #- corrrect, but the reason it returned a syntaxerror is because sep came after a defined argument, which is not correct, non-default parameters come first, after that defined parameters
#     return line.split(sep)


# #**A3 (Predict):** What does `args` contain inside the function?

# def show(*args):
#     print(args)

# show(1, "two", 3.0)     # None? -  or - A tuple ? 
# # GOT THIS ONE WRONG


# #**A4 (Trace):** After this code runs, what is `result`?
# def pick(x=None):
#     if x is None:
#         return "default"
#     return x

# result = pick()
# print(result)
# #result is none , but it will still print "default" before i print result--- I GOT THIS WRONG AGAIN 

'''GUIDED DRILLS'''
'''### Drill 1 — `clip` (defaults + slicing)

Write `clip(text, max_len=10)` that returns `text` unchanged if short enough, otherwise returns the first `max_len` characters. Test with `clip("engineering")` and `clip("engineering", max_len=5)`.

**Hint:** Use `len(text)` and `text[:max_len]`.'''

# def clip(text, max_len=10):
#     if len(text) < max_len:
#         return text
#     else:
#         return text[:max_len]
    
# print(clip("engineering"))
# print(clip("engineering", max_len=5))
# print(clip("engineering", 2))

'''### Drill 2 — `split_fields` (multiple defaults + W1D6 parsing)

Write `split_fields(line, delim=",", strip_chars=" ")` that splits a line by `delim`, strips each field of `strip_chars`, and returns the cleaned list.

**Hint:** Loop through `line.split(delim)`, append `field.strip(strip_chars)` to a result list.'''

# def split_fields(line, delim=",", strip_chars=" "):
#     cleaned = []
#     parts = line.split(delim)
#     for part in parts:
#         cleaned.append(part.strip(strip_chars))
#     return cleaned

# print(split_fields("THIS,is, SPARTA"))

'''### Drill 3 — `average` (variadic `args` + accumulator)

Write `average(*nums)` that returns `0` when no numbers are passed, otherwise returns the mean. Use the accumulator pattern from W3D4.

**Hint:** Check `len(nums) == 0` first, then loop to build `total`.'''

# def average(*nums):
#     total = 0
#     if len(nums) == 0:
#         return 0
#     else:
#         for n in nums:
#             total += n
#     return total / len(nums)


# print(average(5, 100, 100, 200))


'''### Drill 4 — `safe_get` (sentinel `None` + `.get()` from W4D3)

Write `safe_get(record, key, fallback=None)` that returns `record[key]` if the key exists, otherwise returns `fallback`. If `fallback is None`, return the string `"MISSING"` instead.

**Hint:** Use `key in record` to check existence, then `is None` for the fallback check.

Git checkpoint: `git add -A && git commit -m "W5D4 activation + guided drills"`'''

# def safe_get(record, key, fallback=None):
#     if key in record:
#         return record[key]
#     else:
#         if fallback is None:
#             return "MISSING"
#     return fallback
    

# user = {"name": "Ada", "age": 25}

# print(safe_get(user, "name"))           # key exists → "Ada"
# print(safe_get(user, "email"))          # missing, no fallback → "MISSING"
# print(safe_get(user, "email", "N/A"))   # missing, fallback given → "N/A"