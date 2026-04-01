'''### Drill 2: `require_field` with custom exception

Create `class MissingFieldError(Exception): pass`. Write `require_field(record, field)` that raises `MissingFieldError` when the key is missing.
Test with a dict that has the key and one that doesn’t. Catch the error in a loop and print the message using `as e`.

**Hint 1:** `if field not in record: raise MissingFieldError(...)`**Hint 2:** In the test loop: `except MissingFieldError as e: print(f"Caught: {e}")`

File: `field_check.py`'''

class MissingFieldError(Exception):
    pass

def require_field(record, field):
    if field not in record:
        raise MissingFieldError(f"Missing field: {field!r} is not in this record")
    return record, field

records = [
    {"id": "A1", "email": "a@example.com"},
    {"id": "A2"},
]

for record in records:
    try:
        require_field(record, "email")
        print(f"OK: {record}")
    except MissingFieldError as e:
        print(f"Caught: {e}")