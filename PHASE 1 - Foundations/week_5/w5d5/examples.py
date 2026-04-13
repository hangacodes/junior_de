####Predicate function
def is_valid_age(age):
    if age < 0:
        return False       # guard clause — reject fast
    if age > 120:
        return False       # guard clause
    return True            # passed all checks

print(is_valid_age(25))    # output: True
print(is_valid_age(-5))    # output: False
print(is_valid_age(200))   # output: False

'''Recall from W2D4: 
Guard clauses reject bad input early with `return False`,keeping the happy path flat and readable.
In predicates, this pattern is especially natural — each guard eliminates one failure case.'''


####Input sanitization
raw_email = "  Alice@Example.COM  "

# Step 1: sanitize
clean = raw_email.strip().lower()    # "alice@example.com"

# Step 2: validate (only after sanitizing)
has_at = "@" in clean                # True — would also be True unsanitized
has_space = " " in clean             # False — raw version had spaces that would fail!

print(clean)       # output: alice@example.com
print(has_at)      # output: True
print(has_space)   # output: False


#### Validation function
def is_valid_code(code):
    """Returns True if code is exactly 6 digits after stripping spaces."""
    code = code.strip()                # sanitize first
    if len(code) != 6:
        return False                   # guard: wrong length
    for ch in code:
        if ch < "0" or ch > "9":
            return False               # guard: non-digit found
    return True                        # all checks passed

print(is_valid_code("  123456  "))     # output: True
print(is_valid_code("12A456"))         # output: False
print(is_valid_code("12345"))          # output: False (only 5 chars)

####Type hint 
def greet(name: str) -> str:
    return "Hello, " + str(name)

print(greet(42))  # works fine — returns "Hello, 42"

