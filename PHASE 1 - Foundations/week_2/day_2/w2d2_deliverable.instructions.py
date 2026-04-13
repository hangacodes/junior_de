'''### 6D — Primary Deliverable

**Deliverable:** `boolean_rules_engine.py`

Write a script that evaluates **three scenarios** of a “nightly data load” using these rules:

**Rules to implement:**
- `can_start_load` = source is reachable AND schema is valid AND (rows within limit OR manual override)
- `should_alert` = source is NOT reachable OR schema is NOT valid
- `throughput_ok` = run_seconds is not zero AND (rows_processed / run_seconds >= 1000) — use short-circuit!

**Scenario 1:**
- `source_reachable = True`, `schema_valid = True`, `manual_override = False`
- `rows_estimate = 900`, `max_rows = 1000`
- `rows_processed = 300000`, `run_seconds = 250`

**Scenario 2:**
- `source_reachable = False`, `schema_valid = True`, `manual_override = True`
- `rows_estimate = 5000`, `max_rows = 1000`
- `rows_processed = 0`, `run_seconds = 0`

**Scenario 3:**
- `source_reachable = True`, `schema_valid = False`, `manual_override = False`
- `rows_estimate = 800`, `max_rows = 1000`
- `rows_processed = 120000`, `run_seconds = 90`

**Output format (one line per scenario):**

```
Scenario 1 -> can_start_load=True, should_alert=False, throughput_ok=True
```

**Constraints:**
- No `if` statements (tomorrow)
- No loops (Week 3)
- Repeating code for each scenario is expected

**What Could Go Wrong?**
- What happens in Scenario 2 where `run_seconds = 0`? Does your `throughput_ok` crash or handle it safely?

*You’ll write similar rule-evaluation code 3 times here. In Week 3, you’ll handle this with loops. For now, notice the pattern.*'''


'''
Answer key solution : 
# boolean_rules_engine.py

# Scenario 1
source_reachable = True
schema_valid = True
manual_override = False
rows_estimate = 900
max_rows = 1000
rows_processed = 300000
run_seconds = 250

can_start_load = source_reachable and schema_valid and ((rows_estimate <= max_rows) or manual_override)
should_alert = (not source_reachable) or (not schema_valid)
throughput_ok = (run_seconds != 0) and ((rows_processed / run_seconds) >= 1000)

print(f"Scenario 1 -> can_start_load={can_start_load}, should_alert={should_alert}, throughput_ok={throughput_ok}")

# Scenario 2
source_reachable = False
schema_valid = True
manual_override = True
rows_estimate = 5000
max_rows = 1000
rows_processed = 0
run_seconds = 0

can_start_load = source_reachable and schema_valid and ((rows_estimate <= max_rows) or manual_override)
should_alert = (not source_reachable) or (not schema_valid)
throughput_ok = (run_seconds != 0) and ((rows_processed / run_seconds) >= 1000)

print(f"Scenario 2 -> can_start_load={can_start_load}, should_alert={should_alert}, throughput_ok={throughput_ok}")

# Scenario 3
# This repeats 3x — for loops (Week 3) will collapse this pattern
source_reachable = True
schema_valid = False
manual_override = False
rows_estimate = 800
max_rows = 1000
rows_processed = 120000
run_seconds = 90

can_start_load = source_reachable and schema_valid and ((rows_estimate <= max_rows) or manual_override)
should_alert = (not source_reachable) or (not schema_valid)
throughput_ok = (run_seconds != 0) and ((rows_processed / run_seconds) >= 1000)

print(f"Scenario 3 -> can_start_load={can_start_load}, should_alert={should_alert}, throughput_ok={throughput_ok}")'''