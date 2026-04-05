# '''**Drill 1: Spot the newline**
# File name: `spot_newline.py`

# Create a file with two lines. Read the first line with `readline()` and print both `line` and `repr(line)` so you can see the hidden `\n`.

# Hint 1: Write the file first with `"w"` mode.
# Hint 2: `repr()` shows escape characters that `print()` hides.'''
# with open ("week_7/w7d2/guided/drill1", "w" ,encoding="utf-8") as f:
#     f.write("A\n")
#     f.write("B\n")

# with open ("week_7/w7d2/guided/drill1", "r" ,encoding="utf-8") as f:
#     print(repr(f.read()))
    
# '''**Drill 2: Count matching lines with streaming**
# File name: `count_errors.py`

# Create a file with these exact lines: `"ERROR\n"`, `"INFO\n"`, `"ERROR\n"`, `"WARN\n"`. Then stream through it and count how many lines equal `"ERROR"` after stripping.

# Hint 1: Use `for line in f:` — not `readlines()`.
# Hint 2: `clean = line.strip()` before comparing.'''

# with open ("week_7/w7d2/guided/drill2", "w" ,encoding="utf-8") as f:
#     f.write("ERROR\n")
#     f.write("WARN\n")
#     f.write("ERROR\n")
#     f.write("INFO\n")

# with open ("week_7/w7d2/guided/drill2", "r" ,encoding="utf-8") as f:
#     count = 0
#     for line in f:
#         line = line.strip()
#         if line == "ERROR":
#             count += 1
#         print(line)
# print(f"'ERROR' appears {count} times")


# '''**Drill 3: Extract the header separately**
# File name: `extract_header.py`

# Create a file where the first line is `"HEADER: v2\n"` followed by three data lines. Read the header with `readline()`, then loop through the remaining data lines and print each one (stripped).

# Hint 1: `readline()` gets one line and moves the cursor.
# Hint 2: After `readline()`, a `for` loop starts from line 2.'''

# with open ("week_7/w7d2/guided/drill3", "w" ,encoding="utf-8") as f:
#     f.write("HEADER: v2\n")
#     f.write("ERROR\n")
#     f.write("WARN\n")
#     f.write("ERROR\n")



# with open ("week_7/w7d2/guided/drill3", "r" ,encoding="utf-8") as f:
#     header = f.readline()
#     print(header)
#     for line in f:
#         cleaned = line.strip()
#         print(cleaned)    


'''**Drill 4: Build a summary dict from a file**
File name: `level_counter.py`

Create a log file with lines starting with `INFO`, `WARN`, or `ERROR`. Stream through it, strip each line, extract the first word with `.split()[0]`, and count occurrences of each level in a dictionary.

Hint 1: Start with `counts = {"INFO": 0, "WARN": 0, "ERROR": 0}`.
Hint 2: Skip blank lines with `if cleaned == "": continue`.'''

with open ("week_7/w7d2/guided/drill4.log", "w" ,encoding="utf-8") as f:
    f.write("INFO\n")
    f.write("WARN\n")
    f.write("ERROR\n")
    f.write("INFO\n")

counts = {"INFO": 0, "WARN": 0, "ERROR": 0}

with open ("week_7/w7d2/guided/drill4.log", "r" ,encoding="utf-8") as f:

    for line in f :
        cleaned = line.strip()
        if cleaned == "":
            continue

        level = cleaned.split()[0]
        if level in counts:
            counts[level] += 1
print(counts)