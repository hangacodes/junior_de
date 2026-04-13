#Guided Drills

### 6B — Guided Drills

'''**B1 — Compound validation**
Create `status = "active"` and `role = "analyst"`. Create a flag `can_run_job` that is `True` only if status equals `"active"` AND role does not equal `"banned"`.
*Hint:* `(status == "active") and (role != "banned")`

**B2 — Precedence practice**
Create three boolean variables `A = True`, `B = False`, `C = True`. Print both:
- `rule1 = A or (B and C)` (meaning: A alone is enough, OR need both B and C)
- `rule2 = (A or B) and C` (meaning: need C, plus either A or B)

**B3 — De Morgan rewrite**
Given `A = True` and `B = False`, print `not (A or B)` and then print `(not A) and (not B)`. Verify they’re equal.

**B4 — Safe division**
Create `denom = 0` and `num = 100`. Write a flag `safe_result` that is `True` only if `denom != 0` AND `num / denom > 5`. Use short-circuit to prevent crashing.'''

#b1 :
status = "active"
role = "analyst"
can_run_job = (status == "active") and (role != "banned")
print(can_run_job)
print("\n")

#b2:
A = True
B = False
C = True
rule1 = A or (B and C)
rule2 = (A or B) and C
print(rule1)
print(rule2)
print("\n")

#b3:
A1 = True
B1 = False

left = not (A or B)
right = (not A) and (not B)
print(left)
print(right)
print("\n")
#b4:
denom = 0
num = 100

safe_result = (denom != 0) and (num / denom > 5)
print(safe_result)


#Semi-Guided Drill:
#**Starter code — fill the `???` placeholders:**

# Scenario: decide if a data load is allowed

source_status = "reachable"   # "reachable" or "down"
schema_status = "valid"       # "valid" or "broken"
manual_override = False

rows_estimate = 1200
max_rows = 1000

#TODO 1: True only if source is reachable AND schema is valid
allowed_by_health = (source_status == "reachable") and (schema_status == "valid")

#TODO 2: True if rows within limit OR manual override is True
allowed_by_volume = (rows_estimate <= max_rows) or (manual_override)

#TODO 3: True only if both health AND volume are allowed
can_run = allowed_by_health and allowed_by_volume

print(f"allowed_by_health={allowed_by_health}")
print(f"allowed_by_volume={allowed_by_volume}")
print(f"can_run={can_run}")