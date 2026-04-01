#**A1 — Predict:** What prints?

# class Product:
#     def __init__(self, name, price):
#         self.name  = name
#         self.price = price
#         self.stock = 0

#     def restock(self, qty):
#         self.stock += qty
#         return self.stock

# p = Product("Widget", 9.99)
# p.restock(50)
# count = p.restock(20)
# print(p.name, p.stock, count)       #Widget, 70, 70



# #A2 — Trace: What is the final value of LogEntry.total_entries and e1.total_entries?

# class LogEntry:
#     total_entries = 0

#     def __init__(self, level):
#         self.level = level
#         LogEntry.total_entries += 1

# e1 = LogEntry("INFO")
# e2 = LogEntry("ERROR")
# e3 = LogEntry("WARN")
# print(LogEntry.total_entries)
# print(e1.total_entries)
# #3
# #3


# #A3 — Spot the bug: This code crashes. What is the error type and which line is wrong?

# class PipelineRun:
#     def __init__(self, pipe_id):
#         self.pipe_id = pipe_id

#     def describe(self):     #self was missing from this line
#         return f"Run:{self.pipe_id}"

# r = PipelineRun("PIPE-01")
# print(r.describe())

# #**A4 — Predict:** What prints for each line?

# class Config:
#     version = "1.0"

#     def __init__(self, env):
#         self.env = env

# dev  = Config("development")
# prod = Config("production")
# Config.version = "2.0"

# print(dev.version)  #2.0
# print(prod.version) #2/0
# print(dev.env)  #development

# '''### 6B) Guided drills

# **B1 — Build DataRecord**

# Task: Create a `DataRecord` class that stores `record_id` (str), `fields` (dict), and `is_processed` (default `False`).
# Add a method `mark_processed()` that sets `is_processed` to `True` and returns the `record_id`.
# Add a method `get_field(key, default=None)` that safely retrieves a field value using the dict `.get()` pattern you know from W4D1.

# - Hint 1: `get_field` is one line — `return self.fields.get(key, default)` — same pattern as W4D3
# - Hint 2: `is_processed` is set in `__init__` as `False` and flipped to `True` by the method
# - Test: Create a record with id `"R001"` and fields `{"name": "Ada", "age": "30"}`. Print `get_field("name")`, `get_field("email", "N/A")`, then mark processed and print the returned id.

# File: `w6d4_data_record.py`'''

# class DataRecord:

#     def __init__(self, record_id, fields):

#         self.record_id = record_id
#         self.fields = fields
#         self.is_processed = False

#     def mark_processed(self):
#         self.is_processed = True

#         return self.record_id
    
#     def get_field(self, key, default = None):
#         return self.fields.get(key, default)
    
# record = DataRecord("R001", {"name": "Ada", "age": "30"})
# print(record.get_field("name"))           # Ada
# print(record.get_field("email", "N/A"))   # N/A
# print(record.mark_processed())            # R001
# print(record.is_processed)
# record.email = "asd@asd"
# print(record.email)
# print(record)

# print(record.__dict__)
# print(record.get_field("email", "N/A"))   # N/A


