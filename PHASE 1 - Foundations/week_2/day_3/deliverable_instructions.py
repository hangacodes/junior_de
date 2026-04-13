'''**Deliverable:** `validator_v0.py`

Write a script that validates a single “record” (three variables) and prints exactly one outcome.

**Variables:**

```python
name = "  "
age = 34
country = "US"
```

**Validation rules (check in this order, first match wins):**
1. If `name.strip() == ""` → print `"INVALID: missing name"`
2. Elif `age < 0 or age > 120` → print `"INVALID: age out of range"`
3. Elif country is not `"DE"`, `"FR"`, or `"US"` → print `"INVALID: unsupported country"`
4. Else → print `"VALID"`

**Requirements:**
- Use `if/elif/else` (not multiple separate `if` statements)
- Clean the name with `.strip()` before checking
- Exactly one message should print

**Constraints:**
- No loops (Week 3)
- No `try/except` (W2D5)

**What Could Go Wrong?**
- What happens if you check the country rule before the age rule? Does it change results for `age = -5, country = "XX"`?

Git checkpoint: `git add -A && git commit -m "W2D3 deliverable: validator_v0 with if/elif/else"`'''