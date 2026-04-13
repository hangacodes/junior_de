import json
'''**Goal:** Write a function that reads a JSON file containing a list of run records, computes summary stats, and writes the summary to a new JSON file.'''

def summarize_runs(input_path, output_path):
    """
    Read a JSON file with structure: {"runs": [{"id": N, "status": "...", "rows": N}, ...]}
    Write a JSON summary with: total_runs, success_count, failed_count, total_rows
    """
    with open(input_path, "r") as f:
        result = json.load(f)
    #TODO: read input_path with json.load()
    # Hint: use with open(input_path, "r") as f:
    success_count = 0
    fail_count = 0
    total = 0
    total_rows = 0
    for record in result["runs"]:
        if record["status"] == "success":
            success_count += 1
            total +=1
        else:
            fail_count +=1
            total +=1
        total_rows += record["rows"]
    #TODO: loop through data["runs"]
    #   - count successes (status == "success") and failures
    #   - accumulate total rows
    # Hint: use the counter pattern from W4D3

    summary = {"total_runs": total,
               "success_count": success_count,
               "failed_count": fail_count,
               "total_rows": total_rows}
    
    with open(output_path, "w") as f:
        json.dump(summary, f, indent=2)
    return result
    #TODO: build summary dict with total_runs, success_count, failed_count, total_rows
    #TODO: write summary to output_path with json.dump(summary, f, indent=2)
    # Hint: use with open(output_path, "w") as f:
    pass


# Test setup: create input file
test_data = {
    "runs": [
        {"id": 1, "status": "success", "rows": 1200},
        {"id": 2, "status": "failed", "rows": 0},
        {"id": 3, "status": "success", "rows": 850},
        {"id": 4, "status": "success", "rows": 430},
    ]
}

with open("week_7/w7d5/drills/runs_input.json", "w") as f:
    json.dump(test_data, f, indent=2)

summarize_runs("week_7/w7d5/drills/runs_input.json", "week_7/w7d5/drills/runs_summary.json")

# Verify
with open("week_7/w7d5/drills/runs_summary.json", "r") as f:
    print(json.load(f))
# expect: {'total_runs': 4, 'success_count': 3, 'failed_count': 1, 'total_rows': 2480}