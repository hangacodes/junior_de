def write_report(path, title, metrics):
    with open(path, "w", encoding="utf-8") as f:
        f.write(title + "\n")
        for k, v in metrics.items():
            f.write(f"{k}: {v}\n")

def append_run(path, run_id, status):
    with open(path, "a", encoding="utf-8") as f :
        f.write(f"{run_id.rstrip('\n')},{status.rstrip('\n')} \n" )



# Test
write_report("week_7/w7d3/status.txt", "PIPELINE STATUS", {"rows_in": 500, "rows_out": 487, "errors": 13})
append_run("week_7/w7d3/runs.log", "R-001", "OK")
append_run("week_7/w7d3/runs.log", "R-002", "FAIL")

# Verify
with open("week_7/w7d3/status.txt", "r", encoding="utf-8") as f:
    print(f.read())

with open("week_7/w7d3/runs.log", "r", encoding="utf-8") as f:
    print(f.read())