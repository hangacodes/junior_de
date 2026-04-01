'''### Drill 1: `require_in_range(value, low, high)`

Write a function that raises `ValueError` if `value` is outside the range `low..high` (inclusive).
Include a message stating the range and the bad value. Test with values inside and outside the range.

**Hint 1:** `if value < low or value > high: raise ValueError(f"...")`
**Hint 2:** Use f-string to include `low`, `high`, and `value` in the message.

File: `range_check.py`'''

def require_in_range(value, low, high):
    if value  < low or value > high:
        raise ValueError(f"value must be between {low} and {high}, got {value}")
    return value

print(require_in_range(10,0,20))
print(require_in_range(10,11,20))