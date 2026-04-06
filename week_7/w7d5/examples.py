import json

'''### Example 1 — ⭐⭐ Round-trip: Python → JSON string → Python

**What it demonstrates:** `json.dumps()` + `json.loads()` preserving types through a round-trip'''

original = {"sensor": "temp_01", "reading": 22.5, "active": True, "error": None}

# Python → JSON string
as_json = json.dumps(original)
print("JSON string:", as_json)
print("Type:", type(as_json))

# JSON string → Python
restored = json.loads(as_json)
print("Restored:", restored)
print("reading type:", type(restored["reading"]))
print("active type:", type(restored["active"]))

#💡 JSON preserves numeric types, booleans, and null/None through the round-trip.
# This is a huge advantage over CSV, where everything starts as a string and you must cast manually.

'''### Example 2 — ⭐⭐⭐ Write JSON to file, read it back

**What it demonstrates:** `json.dump()` + `json.load()` with file handles + `indent` for readability'''


config = {
    "db_host": "localhost",
    "db_port": 5432,
    "max_retries": 3,
    "debug": False,
}

# Write to file
with open("week_7/w7d5/config.json", "w") as f:
    json.dump(config, f, indent=2)

# Read back
with open("week_7/w7d5/config.json", "r") as f:
    loaded = json.load(f)

print(loaded)
print("Port:", loaded["db_port"])
print("Port type:", type(loaded["db_port"]))
#💡 Compare this to CSV: if you wrote `5432` to a CSV and read it back, you’d get the string `"5432"` and need `int()` to convert it.
# JSON keeps it as `5432` automatically.


'''### Example 3 — ⭐⭐⭐ Navigating nested JSON

**What it demonstrates:** Chained key/index access on nested structures + safe access with `.get()`'''



json_text = '''{
    "pipeline": "nightly_etl",
    "runs": [
        {"id": 1, "status": "success", "rows": 1200},
        {"id": 2, "status": "failed", "rows": 0, "error": "timeout"},
        {"id": 3, "status": "success", "rows": 850}
    ]
}'''

data = json.loads(json_text)

# Access the pipeline name
print(data["pipeline"])

# Access the second run's status
print(data["runs"][1]["status"])

# Loop through runs and summarize
total_rows = 0
for run in data["runs"]:
    total_rows += run["rows"]
    error = run.get("error", "none")
    print(f"Run{run['id']}:{run['status']} — error:{error}")

print("Total rows:", total_rows)
#💡 `.get("error", "none")` returns the default when the key is missing — exactly the same W4D3 pattern you already know.
# JSON navigation is just dict/list access with more nesting.


'''### Example 4 — ⭐⭐⭐⭐ Read JSON file → process → write results

**What it demonstrates:** Full pipeline: `json.load()` → loop + accumulate → `json.dump()` — combining file I/O with nested navigation and W3D4 accumulator patterns'''
# Create a test input file
input_data = {
    "team": "data_eng",
    "members": [
        {"name": "Ana", "hours": [8, 7, 9, 8, 6]},
        {"name": "Bo", "hours": [6, 8, 8, 7, 5]},
        {"name": "Cy", "hours": [9, 9, 8, 9, 8]},
    ],
}

with open("week_7/w7d5/team_hours.json", "w") as f:
    json.dump(input_data, f, indent=2)

# Read, process, write
with open("week_7/w7d5/team_hours.json", "r") as f:
    data = json.load(f)

summary = {"team": data["team"], "member_summaries": []}

for member in data["members"]:
    total = 0
    for h in member["hours"]:
        total += h
    avg = round(total / len(member["hours"]), 1)
    summary["member_summaries"].append({
        "name": member["name"],
        "total_hours": total,
        "avg_hours": avg,
    })

with open("week_7/w7d5/team_summary.json", "w") as f:
    json.dump(summary, f, indent=2)

# Verify
with open("week_7/w7d5/team_summary.json", "r") as f:
    print(json.load(f))

'''💡 This is the pattern you'll use in W7D7 and Week 8:
-read structured input → compute results → write structured output.
JSON makes the input/output step trivial — the real work is the processing logic in the middle.'''