'''Write a function `count_lines_with_keyword(path, keyword)` that:
- Opens the file at `path` and streams through it line by line
- Counts how many lines **contain** the keyword (use `in`, not `==`)
- Strips each line before checking
- Returns `0` if the file doesn’t exist (`try/except FileNotFoundError`)'''


def count_lines_with_keyword(path, keyword):
    """Count lines containing keyword, streaming line-by-line."""
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                cleaned = line.strip()
                if cleaned =="":
                    continue
                if keyword in cleaned:
                    count += 1
            return count
    except FileNotFoundError:
        return 0
        
    # Hint: wrap open() in try/except FileNotFoundError
    # Hint: for each line, strip it, then check if keyword is in the cleaned line
    # Hint: return 0 inside the except block
    

    


# Test setup
with open("week_7/w7d2/semi-guided/test_log.txt", "w", encoding="utf-8") as f:
    f.write("ERROR connection refused\n")
    f.write("INFO server started\n")
    f.write("ERROR timeout on query\n")
    f.write("WARN slow response\n")

print(count_lines_with_keyword("week_7/w7d2/semi-guided/test_log.txt", "ERROR"))   # expect 2
print(count_lines_with_keyword("week_7/w7d2/semi-guided/test_log.txt", "slow"))    # expect 1
print(count_lines_with_keyword("week_7/w7d2/semi-guided/ghost.txt", "ERROR"))      # expect 0