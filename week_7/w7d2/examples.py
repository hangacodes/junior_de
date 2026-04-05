# with open("week_7/w7d2/readline_demo.txt", "w", encoding="utf-8") as f:
#     f.write("HEADER: version 2\n")
#     f.write("Ada,92\n")
#     f.write("Lin,68\n")

# with open("week_7/w7d2/readline_demo.txt", "r", encoding="utf-8") as f:
#     header = f.readline()
#     first_data = f.readline()

# print("header:", repr(header))     # output: header: 'HEADER: version 2\n'
# print("first_data:", repr(first_data))  # output: first_data: 'Ada,92\n'


# with open("week_7/w7d2/readlines_demo.txt", "w", encoding="utf-8") as f:
#     f.write("red\ngreen\nblue\n")

# with open("week_7/w7d2/readlines_demo.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()

# print(lines)               # output: ['red\n', 'green\n', 'blue\n']
# print(repr(lines[0]))      # output: 'red\n'
# print(lines[0].strip())    # output: red
# '''### Example 1 — ⭐⭐ `readline()` for headers vs data

# **What it demonstrates:** Using `readline()` to separate a header from data lines, then `for line in f:` for the rest.'''
# with open("week_7/w7d2/ex1.txt", "w", encoding="utf-8") as f:
#     f.write("name,score\n")
#     f.write("Ada,92\n")
#     f.write("Lin,68\n")
#     f.write("Max,85\n")

# with open("week_7/w7d2/ex1.txt", "r", encoding="utf-8") as f:
#     header = f.readline().strip()
#     print(f"Header:{header}")
#     for line in f:
#         print(f"  Data:{line.strip()}")


# '''### Example 2 — ⭐⭐⭐ Streaming a file to count matching lines

# **What it demonstrates:** `for line in f:` + `.strip()` + conditional logic + counter pattern from W3D4'''
# with open("week_7/w7d2/ex2.log", "w", encoding="utf-8") as f:
#     f.write("INFO started\n")
#     f.write("WARN retrying\n")
#     f.write("\n")
#     f.write("ERROR timeout\n")
#     f.write("ERROR disk full\n")
#     f.write("INFO healthy\n")

# error_count = 0
# with open("week_7/w7d2/ex2.log", "r", encoding="utf-8") as f:
#     for line in f:
#         cleaned = line.strip()
#         if cleaned == "":
#             continue
#         level = cleaned.split()[0]
#         if level == "ERROR":
#             error_count += 1

# print(f"Errors found:{error_count}")

'''### Example 3 — ⭐⭐⭐ `readlines()` vs `for line in f:` — same result, different cost

**What it demonstrates:** Both approaches process every line, but `readlines()` loads everything into memory while `for line in f:` streams.'''

with open("week_7/w7d2/ex3.txt", "w", encoding="utf-8") as f:
    for i in range(1, 11):
        f.write(f"row{i}\n")

# Approach 1: readlines() — loads all into a list
with open("week_7/w7d2/ex3.txt", "r", encoding="utf-8") as f:
    all_lines = f.readlines()
print(f"readlines gave{len(all_lines)} items")
print(f"First item:{repr(all_lines[0])}")

# Approach 2: for line in f — streams one at a time
stream_count = 0
with open("week_7/w7d2/ex3.txt", "r", encoding="utf-8") as f:
    for line in f:
        stream_count += 1
print(f"Streaming counted{stream_count} lines")