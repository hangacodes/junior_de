# with open("week_7/w7d1/report.txt", "w", encoding="utf-8") as f:
#     f.write("Daily Report\n")
#     f.write(f"Rows processed:{120}\n")
#     f.write(f"Errors:{3}\n")

# with open("week_7/w7d1/report.txt", "r", encoding="utf-8") as f:
#     content = f.read()

# print(content)


# # Start fresh
# with open("week_7/w7d1/log.txt", "w", encoding="utf-8") as f:
#     f.write("=== LOG START ===\n")

# # Simulate two separate "runs" appending
# with open("week_7/w7d1/log.txt", "a", encoding="utf-8") as f:
#     f.write("Run 1: processed 50 rows\n")

# with open("week_7/w7d1/log.txt", "a", encoding="utf-8") as f:
#     f.write("Run 2: processed 75 rows\n")

# with open("week_7/w7d1/log.txt", "r", encoding="utf-8") as f:
#     print(f.read())


# def read_file_safe(path):
#     try:
#         with open(path, "r", encoding="utf-8") as f:
#             return f.read()
#     except FileNotFoundError:
#         return f"ERROR:{path} not found"

# # File that exists
# with open("week_7/w7d1/exists.txt", "w", encoding="utf-8") as f:
#     f.write("I exist!\n")

# print(read_file_safe("week_7/w7d1/exists.txt"))
# print(read_file_safe("week_7/w7d1/ghost.txt"))

# users = ["Ada", "Lin", "Max", "Zoe"]
# scores = [92, 68, 85, 91]

# with open("week_7/w7d1/scores.txt", "w", encoding="utf-8") as f:
#     f.write("=== SCORE REPORT ===\n")
#     for i in range(len(users)):
#         line = f"{users[i]}:{scores[i]}\n"
#         f.write(line)

# with open("week_7/w7d1/scores.txt", "r", encoding="utf-8") as f:
#     print(f.read())


# '''DRILLS'''
# #What does this print ?
# with open("test.txt", "w", encoding="utf-8") as f:
#     f.write("A")
#     f.write("B")

# with open("test.txt", "r", encoding="utf-8") as f:
#     print(repr(f.read()))

# #Drill 2 (Predict): What happens when this runs?
# with open("mystery.txt", "w", encoding="utf-8") as f:
#     f.write("first\n")

# with open("mystery.txt", "w", encoding="utf-8") as f:
#     f.write("second\n")

# with open("mystery.txt", "r", encoding="utf-8") as f:
#     print(f.read())

# # #Drill 3 (Spot): This code is supposed to read a file, but it crashes. Name the error type and explain why.
# # with open("data.txt", "r", encoding="utf-8") as f:
# #     f.write("new data\n")           #Because it gets opened with r - so is read only - you cannot use f.write inside a read only opened file - also the file doesn't exist
# #     #so is FileNotFoundError

# #**Drill 4 (Trace):** After this code runs, what is the content of `log.txt`? Trace each step.
# with open("log.txt", "w", encoding="utf-8") as f:
#     f.write("START\n")

# with open("log.txt", "a", encoding="utf-8") as f:
#     f.write("MIDDLE\n")

# with open("log.txt", "a", encoding="utf-8") as f:
#     f.write("END\n")

'''Guided'''

# '''**Drill 1: Fix the mode bug**
# File name: `fix_mode.py`

# This code is supposed to write three numbers into a file, but it crashes. Fix it.
# Hint 1: What mode lets you write?
# Hint 2: Does the file need to exist before you write to it in `"w"` mode?'''

# with open("week_7/w7d1/guided/numbers.txt", "w", encoding="utf-8") as f:
#     f.write("1\n2\n3\n")




# '''**Drill 2: Append without erasing**
# File name: `append_events.py`

# Write `"START\n"` to `events.txt` using `"w"`. Then append `"EVENT 1\n"` and `"EVENT 2\n"` using `"a"`. Read the file back and print it.

# Hint 1: You need three separate `with` blocks — one for writing, one for appending, one for reading.
# Hint 2: `"a"` never erases. `"w"` always erases.'''

# with open ("week_7/w7d1/guided/events.txt", "w" , encoding="utf-8") as f:
#     f.write("START\n")

# with open("week_7/w7d1/guided/events.txt", "a", encoding="utf-8") as f:
#     f.write("EVENT 1\n")
#     f.write("EVENT 2\n")

# with open("week_7/w7d1/guided/events.txt", "r" , encoding="utf-8") as f:
#     print(f.read())

# '''**Drill 3: Write a list to a file with proper newlines**
# File name: `write_cities.py`

# Given `cities = ["Moscow", "Berlin", "Tokyo", "Lagos"]`, write each city on its own line in `cities.txt`, then read and print the file contents.

# Hint 1: Use a `for` loop inside a `with open("cities.txt", "w", ...)` block.
# Hint 2: Don’t forget `\n` after each city name.'''

# cities = ["Moscow", "Berlin", "Tokyo", "Lagos"]

# with open ("week_7/w7d1/guided/cities.txt", "w" , encoding="utf-8") as f:
#     for city in cities:
#         f.write(city + "\n")

# with open("week_7/w7d1/guided/cities.txt", "r" , encoding="utf-8") as f:
#     print(f.read())


'''**Drill 4: Safe reader function**
File name: `safe_reader.py`

Write a function `read_or_default(path, default_text)` that returns the file’s contents if it exists, or returns `default_text` if the file is missing.
Test it with a file that exists and one that doesn’t.

Hint 1: Wrap `open()` in `try/except FileNotFoundError`.
Hint 2: The function should `return` the text, not print it.'''

def read_or_default(path, default_text):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return default_text
    
print(read_or_default("week_7/w7d1/log.txt", "idk"))
print(read_or_default("week_7/w7d1/ghost.txt", "idk"))

