# def format_record(name, age, city):
#     return name + " (" + str(age) + "), " + city

# # Positional: order determines which parameter gets which value
# print(format_record("Ada", 36, "London"))       # name="Ada", age=36, city="London"

# # Keyword: names determine binding — order doesn't matter
# print(format_record(city="London", name="Ada", age=36))  # same result

# # Mixed: positional first, then keyword
# print(format_record("Ada", age=36, city="London"))        # also works


# def log_event(message, level="INFO", **kwargs):
#     """Return a log line with optional metadata key=value pairs."""
#     parts = [level + ": " + str(message)]
#     for k, v in kwargs.items():
#         parts.append(str(k) + "=" + str(v))
#     return " | ".join(parts)

# print(log_event("started"))
# print(log_event("failed", level="ERROR", code=500, service="api"))
# # output: INFO: started
# # output: ERROR: failed | code=500 | service=api
# '''Anatomy of a variadic signature:

# def f(a, b, *args, **kwargs):
#       |  |    |        |
#       |  |    |        +-- extra keyword args → dict {"key": value, ...}
#       |  |    +-- extra positional args → tuple (val1, val2, ...)
#       |  +-- required parameter
#       +-- required parameter

# Order rule: required → *args → keyword-only → **kwargs'''

# def build_report(title, *sections, separator="---", **metadata):
#     """Build a report string from a title, sections, and optional metadata."""
#     parts = ["REPORT: " + str(title)]
#     for key, value in metadata.items():
#         parts.append(str(key) + ": " + str(value))
#     parts.append(separator)
#     for section in sections:
#         parts.append(str(section))
#     return "\n".join(parts)

# print(build_report(
#     "Sales Q1",
#     "Revenue was up 12%",
#     "Costs stayed flat",
#     "Team hit all targets",
#     separator="===",
#     author="Ana",
#     date="2026-03-20",
#     region="EU"
# ))
# '''def build_report(title, *sections, separator="---", **metadata):
#                   |        |            |               |
#                   |        |            |               +-- any number of keyword args
#                   |        |            |                   (author=, date=, region=)
#                   |        |            |
#                   |        |            +-- default parameter, comes after *sections
#                   |        |
#                   |        +-- collects extra positional args into a tuple
#                   |            ("Revenue was up 12%", "Costs stayed flat", ...)
#                   |
#                   +-- required positional argument (always first)'''


# #**What it demonstrates:** default parameter + keyword override + `.split()` integration
# #predict:
# def make_path(folder, filename, ext="txt"):
#     return folder + "/" + filename + "." + ext

# print(make_path("data", "users"))
# print(make_path("data", "events", ext="csv"))

# #data/users.txt
# #data/events.csv    # GOT THIS ONE RIGHT
#💡 Defaults serve the common case. The caller only speaks up when they need something different — no extra `if` logic needed.
#
# # **What it demonstrates:** sentinel `None` default + `is None` + safe `maxsplit` usage with `.split()`
#  #predict:
# def parse_pair(text, sep=None):
#     """Split text into a key-value tuple. Default separator is '='."""
#     if sep is None:
#         sep = "="
#     left, right = text.split(sep, 1)
#     return left.strip(), right.strip()

# print(parse_pair("name = Ada"))
# print(parse_pair("host:9090", sep=":"))

# #[name, Ada]  wrong
# #[host 9090]  got this one wrong, it actually returns a tuple because " return left, right "-> the comma creates a tuple

# #💡 `None` + `is None` is cleaner than using `""` as a default because `""` could be a legitimate separator value the caller actually wants.
# #
# # 
# # **What it demonstrates:** multiple defaults + keyword arguments + docstring + `.get()` from W4D3
# # predict :
# def summarize_field(records, field="status", missing_label="UNKNOWN"):
#     """Count occurrences of a field value across a list of dicts.
#     Missing keys are counted under missing_label."""
#     counts = {}
#     for r in records:
#         value = r.get(field, missing_label)
#         counts[value] = counts.get(value, 0) + 1
#     return counts

# data = [
#     {"user": "ada", "status": "active"},
#     {"user": "bob"},
#     {"user": "cal", "status": "active"},
#     {"user": "dee", "status": "inactive"}
# ]
# print(summarize_field(data))
# print(summarize_field(data, field="user", missing_label="N/A"))
# #what does the first print count, what about the second ?
# #💡 Keyword arguments shine when a function has 3+ parameters — the call `summarize_field(data, field="user")` is self-documenting compared to `summarize_field(data, "user")`.


#**What it demonstrates:** `**kwargs` for flexible metadata + docstring + accumulator from W3D4

# def build_log_line(message, level="INFO", **meta):
#     """Build a structured log line with optional metadata.
#     Returns: 'LEVEL: message | key=value | key=value'"""
#     parts = [str(level) + ": " + str(message)]
#     for k, v in meta.items():
#         parts.append(str(k) + "=" + str(v))
#     return " | ".join(parts)

# print(build_log_line("job started"))
# print(build_log_line("row rejected", level="WARN", row=42, reason="null_id"))
# #❓ **PREDICT:** What format does each line follow?
# #💡 `**kwargs` is powerful for open-ended metadata but risky for strict interfaces — a typo like `reaosn="null_id"` would silently pass through.