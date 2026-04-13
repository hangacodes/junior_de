'''**Deliverable:** `validator_v1.py`

Validate **three hardcoded rows** with format `"name,age,country,status"`.

**Rules (print exactly one line per row):**
1. If wrong number of fields → `ERROR_FIELDS`
2. Else parse fields:
- If `age < 0 or age > 120` → `ERROR_AGE`
- Elif `status != "active"` → `SKIP_INACTIVE`
- Else (valid + active):
- If `country == "DE"` → `PROCESS_DE`
- Else → `PROCESS_OTHER`

**Test rows:**
- `"Mina,29,DE,active"` → `PROCESS_DE`
- `"Bo,200,DE,active"` → `ERROR_AGE`
- `"Rui,40,JP,inactive"` → `SKIP_INACTIVE`

**Constraints:**
- No `input()` (tomorrow)
- No `try`/`except` (tomorrow)
- No loops (Week 3)
- Must use at least one nested conditional and one guard clause

**What Could Go Wrong?**
- What happens if you check `status != "active"` before checking age range? Does the order matter for `"Bo,200,DE,active"`?

*You'll write similar validation code 3 times here. In Week 3, you'll handle this with a `for` loop. For now, notice the repetition—that recognition is exactly what will make loops feel natural.*

Git checkpoint: `git add -A && git commit -m "W2D4 deliverable: validator_v1 with nested routing"`

---'''