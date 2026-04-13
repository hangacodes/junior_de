# file: row_parser.py
'''### Example 4 — ⭐⭐⭐⭐ Combining exception handling with a reusable module

**What it demonstrates:** building a robust parsing module + using it from a script + `__main__` guard + all four `try` clauses + `as e` for error logging'''
def parse_record(line):
    """Parse 'id|name|amount' into a dict. Let exceptions propagate."""
    parts = line.strip().split("|")
    record_id = int(parts[0])
    name = parts[1].strip().title()
    amount = float(parts[2])
    return {"id": record_id, "name": name, "amount": amount}

if __name__ == "__main__":
    print(parse_record("101|ada|19.99"))