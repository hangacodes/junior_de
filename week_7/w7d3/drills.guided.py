# '''**Drill 3: Normalize messy input to clean output**
# File name: `normalize_lines.py`

# Given `data = ["row 1\n", "row 2", "row 3\n\n"]`, write each item to `clean.txt` with exactly one `\n` per line.

# Hint 1: Use `item.rstrip("\n") + "\n"` for each item.
# Hint 2: Read the file back and use `repr()` to verify no double newlines.'''

# data = ["row 1\n", "row 2", "row 3\n\n"]

# with open("week_7/w7d3/clean.txt" , "w", encoding="utf-8") as f:
#     for row in data:
#         cleaned = row.rstrip("\n") + ("\n")
#         f.write(cleaned)

# with open("week_7/w7d3/clean.txt" , "r", encoding="utf-8") as f:
#     print(f.read())


'''**Drill 4: Write a helper function**
File name: `write_helper.py`

Write a function `write_lines(path, items)` that takes a file path and a list of strings, and writes each string as one line to the file (overwrite mode).
Normalize newlines. Then test it with `["alpha", "beta\n", "gamma"]`.

Hint 1: The function should open the file in `"w"` mode.
Hint 2: Use `item.rstrip("\n") + "\n"` inside the loop.'''

def write_lines(path, items):
    with open (path, "w", encoding="utf-8") as f:
        for item in items:
            cleaned = item.rstrip("\n") + ("\n")
            f.write(cleaned)

write_lines("week_7/w7d3/clean.drill4.txt" , ["alpha", "beta\n", "gamma"])

with open("week_7/w7d3/clean.drill4.txt" , "r", encoding="utf-8") as f:
    print(f.read())