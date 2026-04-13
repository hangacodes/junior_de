'''### Example 1 — ⭐⭐ Building paths and extracting parts

**What it demonstrates:** Path joining with `/`, `.name`, `.suffix`, `.stem`
'''
from pathlib import Path

# p = Path("data") / "raw" / "sales_2026.csv"

# print(f"Full path:{p}")
# print(f"Filename:{p.name}")
# print(f"Extension:{p.suffix}")
# print(f"Stem:{p.stem}")


# '''### Example 2 — ⭐⭐⭐ Check before you act — validating a path

# **What it demonstrates:** Using `exists()`, `is_file()`, `is_dir()` to decide what to do.'''



# def describe_path(path_str):
#     p = Path(path_str)
#     if not p.exists():
#         return f"{path_str}: does not exist"
#     elif p.is_file():
#         return f"{path_str}: is a file ({p.suffix})"
#     elif p.is_dir():
#         return f"{path_str}: is a directory"
#     else:
#         return f"{path_str}: exists but unknown type"

# # Setup
# Path("week_7/w7d6/check_demo").mkdir(exist_ok=True)
# with open(Path("week_7/w7d6/check_demo") / "test.txt", "w") as f:
#     f.write("hello\n")

# print(describe_path("week_7/w7d6/check_demo"))
# print(describe_path("week_7/w7d6/check_demo/test.txt"))
# print(describe_path("week_7/w7d6/ghost.txt"))


# '''### Example 3 — ⭐⭐⭐ Creating output directories safely

# **What it demonstrates:** `mkdir(parents=True, exist_ok=True)` + writing a file into the new directory.'''



# output_dir = Path("week_7/w7d6/pipeline_output") / "reports"
# output_dir.mkdir(parents=True, exist_ok=True)

# report_path = output_dir / "summary.txt"
# with open(report_path, "w", encoding="utf-8") as f:
#     f.write("Pipeline ran successfully.\n")
#     f.write(f"Report saved to:{report_path}\n")

# print(f"Report written to:{report_path}")
# print(f"Directory exists:{output_dir.is_dir()}")

'''### Example 4 — ⭐⭐⭐⭐ Finding and processing files by extension

**What it demonstrates:** `glob("*.csv")` to find files, then reading each one — combining path operations with file I/O from earlier this week.'''


# Setup: create test CSV files
data_dir = Path("week_7/w7d6/glob_pipeline")
data_dir.mkdir(exist_ok=True)

for name in ["users.csv", "orders.csv", "notes.txt"]:
    with open(data_dir / name, "w", encoding="utf-8") as f:
        if name.endswith(".csv"):
            f.write("id,value\n1,100\n2,200\n")
        else:
            f.write("Just a note.\n")

# Find and process only CSV files
csv_files = []
for p in data_dir.glob("*.csv"):
    if p.is_file():
        csv_files.append(p)

print(f"Found{len(csv_files)} CSV files:")
for csv_path in csv_files:
    with open(csv_path, "r", encoding="utf-8") as f:
        line_count = 0
        for line in f:
            line_count += 1
    print(f"{csv_path.name}:{line_count} lines")