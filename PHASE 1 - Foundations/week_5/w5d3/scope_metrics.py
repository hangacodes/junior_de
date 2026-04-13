rows = [
    "Ava, 29",
    "BROKEN",
    "Noah, 41",
    "Mia, not_a_number",
    "Leo, 18",
    "Too, many, commas"
]

def batch_metrics(rows):
    good = 0 
    bad = 0
    last_error = None
    total = 0

    def mark_bad(msg):
        nonlocal bad, last_error
        bad += 1
        last_error = msg

    for row in rows:
        parts = row.split(",")
        if len(parts) != 2:
            mark_bad(row)
        
            continue

        name = parts[0].strip()
        age_str = parts[1].strip()

        try:
            age = int(age_str)
        except ValueError:
            mark_bad("ERROR: age is not a number:")
            continue
        good += 1
    total = good + bad
    
    print("=== Batch Metrics Report ===")
    print("good:", good)
    print("bad:", bad)
    print("last_error:", last_error)
    print("total:", total)
    return {"good": good, "bad": bad, "last_error": last_error, "total": total}
batch_metrics(rows)