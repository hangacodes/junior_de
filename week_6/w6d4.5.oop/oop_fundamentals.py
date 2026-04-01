# '''### Example 1 — ⭐⭐ Your Week 5 parse function becomes a class

# **What it demonstrates:** class definition, `__init__`, `self`, attribute, method — built from a function pattern you already know

# This is your `parse_product` function from W6D3, rewritten as a class:'''
# # # Before: standalone function + dict (your Week 5 style)
# # def parse_product(line):
# #     parts = line.split("|")
# #     return {
# #         "product_id": parts[0].strip(),
# #         "name":       parts[1].strip(),
# #         "price":      float(parts[2].strip()),
# #         "quantity":   int(parts[3].strip()),
# #     }

# # def compute_value(record):
# #     return record["price"] * record["quantity"]

# # def is_in_stock(record):
# #     return record["quantity"] > 0

# # After: same logic, bundled into a class
# class Product:
#     def __init__(self, line):
#         parts = line.split("|")
#         self.product_id = parts[0].strip()
#         self.name       = parts[1].strip()
#         self.price      = float(parts[2].strip())
#         self.quantity   = int(parts[3].strip())
#         # same parsing as before — just stored on self instead of in a dict

#     def compute_value(self):
#         return self.price * self.quantity   # self.price instead of record["price"]

#     def is_in_stock(self):
#         return self.quantity > 0

# p = Product("|Widget|9.99|50")
# print(p.name)               # Widget
# print(p.compute_value())    # 499.5
# print(p.is_in_stock())      # True

# p2 = Product("|Bolt|0.75|99")
# print(p2.is_in_stock())     # False — separate object, separate data
# print(p2.compute_value()) 

# '''### Example 2 — ⭐⭐⭐ Your log analyzer counter pattern as a class

# **What it demonstrates:** method calling `.get()` pattern (W4D3), class attribute as shared counter, methods that build on each other

# This is your W4D3 log analyzer logic, wrapped in a class:'''

# class LogEntry:
#     total_entries = 0                           # class attribute: shared counter

#     def __init__(self, line):
#         parts = line.split(",")
#         self.level   = parts[0].strip()
#         self.service = parts[1].strip()
#         self.message = parts[2].strip()
#         LogEntry.total_entries += 1

#     def is_error(self):
#         return self.level == "ERROR"

#     def is_warn(self):
#         return self.level == "WARN"

#     def describe(self):
#         return f"[{self.level}]{self.service}:{self.message}"

#     def severity(self, severity_map=None):      # default parameter (W5D4)
#         if severity_map is None:
#             severity_map = {"INFO": 1, "WARN": 2, "ERROR": 3}
#         return severity_map.get(self.level, 0)  # .get() with default (W4D1)

# lines = [
#     "INFO,auth,login",
#     "WARN,auth,bad_password",
#     "ERROR,shop,payment_failed",
#     "INFO,auth,logout",
# ]

# entries = []
# for line in lines:
#     entries.append(LogEntry(line))

# for e in entries:
#     print(e.describe(), "→ severity:", e.severity())

# errors = [e for e in entries if e.is_error()]      # list comprehension (W3D5)
# print(f"\nErrors:{len(errors)} /{LogEntry.total_entries} total")
# for entry in entries:
#     print(type(entry))


'''### Example 3 — ⭐⭐⭐ Multiple instances in a list — your pipeline auditor, but as objects

**What it demonstrates:** class attribute, multiple instances, `for` loop over objects (W3D2), accumulator (W3D4), filtering (W3D5)

This is the same data from your `pipeline_auditor.py` in W1D7, but now each record is an object instead of a parsed string:'''

class PipelineRun:
    completed_count = 0                             # class attribute

    def __init__(self, pipe_id, job_name, rows, duration_s, status):
        self.pipe_id    = pipe_id
        self.job_name   = job_name
        self.rows       = rows
        self.duration_s = duration_s
        self.status     = status
        PipelineRun.completed_count += 1

    def rows_per_second(self):
        if self.duration_s == 0:
            return 0
        return round(self.rows / self.duration_s, 1)

    def is_healthy(self):                           # predicate (W5D5)
        return self.status == "SUCCESS"

runs = [
    PipelineRun("PIPE-01", "etl_customers", 8420,  127, "SUCCESS"),
    PipelineRun("PIPE-02", "etl_orders",   12450,  203, "SUCCESS"),
    PipelineRun("PIPE-03", "etl_products",   891,   45, "WARN"),
    PipelineRun("PIPE-04", "etl_events",   99103, 3782, "FAILED"),
]

# Total rows — accumulator pattern (W3D4)
total_rows = 0
for run in runs:
    total_rows += run.rows

# Filter to healthy only — comprehension (W3D5)
healthy = [r for r in runs if r.is_healthy()]

# Running max — same pattern as W3D4
slowest = runs[0]
for run in runs:
    if run.rows_per_second() < slowest.rows_per_second():
        slowest = run

print(f"Total rows:{total_rows:,}")
print(f"Healthy:{len(healthy)} /{PipelineRun.completed_count}")
print(f"Slowest:{slowest.job_name} at{slowest.rows_per_second()} rows/sec")