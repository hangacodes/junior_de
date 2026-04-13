# '''#**Drill 1 (Predict):** What does `Path("data") / "raw" / "file.csv"` produce?

# '''
# #Produces a Path object

# '''**Drill 2 (Predict):** If `Path("ghost.txt").exists()` returns `False`, what do `is_file()` and `is_dir()` return?'''
# #Also False - or is it FileNotFoundError?

# '''**Drill 3 (Predict):** What does `Path("events.json").suffix` return — `"json"` or `".json"`?'''

# #returns .json

# '''**Drill 4 (Spot):** This code crashes on the second run. Why?'''
# from pathlib import Path
# Path("output").mkdir()

# #Because we didn't use exists_ok = True


# '''**Drill 1: Build and inspect a path**
# File name: `path_basics.py`

# Create a path to `"project/data/raw/sales.csv"` using `Path` and `/`. Print the full path, the filename (`.name`), the extension (`.suffix`), and the stem (`.stem`).

# Hint 1: `from pathlib import Path`
# Hint 2: `p = Path("project") / "data" / "raw" / "sales.csv"`'''

# from pathlib import Path

# p = Path("project") / "data" / "raw" / "i_dont_want_it_anymore.csv"
# print(p)
# print(p.name)
# print(p.suffix)
# print(p.stem)


# '''**Drill 2: Check before reading**
# File name: `safe_check.py`

# Write a function `check_and_read(path_str)` that converts `path_str` to a `Path`, checks if it exists and is a file, reads and returns its contents if so, or returns an error message if not.

# Hint 1: Use `p.exists()` and `p.is_file()`.
# Hint 2: Return a string like `"Not a file: <path>"` if the check fails.'''
# from pathlib import Path

# def check_and_read(path_str):
#     p = Path(path_str)

#     if not p.exists():
#         return f"File does not exist: {path_str}"
#     if not p.is_file():
#         return f"This is not a file: {path_str}"
#     with open(p, "r", encoding="utf-8") as f:
#         return f.read()

# '''**Drill 3: Create output directory and write a file**
# File name: `ensure_output.py`

# Write a function `write_to_output(dir_name, filename, content)` that:
# - Creates the directory if it doesn’t exist
# - Writes `content` to `dir_name/filename`
# - Returns the full path as a string

# Hint 1: `Path(dir_name).mkdir(parents=True, exist_ok=True)`
# Hint 2: `full_path = Path(dir_name) / filename`'''

# def write_to_output(dir_name, filename, content):
#     out_dir = Path(dir_name)

#     out_dir = Path.mkdir(parents=True, exist_ok=True)
#     full_path = out_dir / filename
#     with open(full_path, "w", encoding="utf-8") as f:
#         f.write(content)

#     return str(full_path)