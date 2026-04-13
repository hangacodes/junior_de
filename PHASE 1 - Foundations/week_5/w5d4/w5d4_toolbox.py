def parse_kv_line(line, pair_sep=";", kv_sep="="):
    """Parse 'a=1; b=2; c=3' into a dict of strings.
    Uses part.split(kv_sep, 1) so values containing kv_sep stay intact."""
    pairs = {}
    parts = line.split(pair_sep)
    for part in parts:
        if  part.strip() == "":
            continue
        raw_parts = part.split(kv_sep)
        pairs[raw_parts[0].strip()] = raw_parts[1].strip()
    return pairs
    #TODO: split line by pair_sep, then split each pair by kv_sep
    #TODO: strip whitespace from keys and values
    #TODO: skip empty pairs


def get_int(text, default=0):
    """Convert text to int if possible, otherwise return default."""
    try:
        return int(text.strip())
    except ValueError:
        return default
    #TODO: strip text, try int(), except ValueError return default


def make_report(title, *lines, sep="\n"):
    """Build a report string: title first, then each line, joined by sep."""
    lst = []
    lst.append(title)
    for part in lines:
        lst.append(part)
    return sep.join(lst)

    #TODO: build a list starting with title, add each line, join with sep

# '''Requirements:
# - `parse_kv_line("x=1; y=2")` → `{"x": "1", "y": "2"}`
# - `get_int("  42  ")` → `42`, `get_int("nope")` → `0`
# - `make_report("SUMMARY", "row 1", "row 2")` → `"SUMMARY\nrow 1\nrow 2"`'''

print(parse_kv_line("x=1; y=2"))
print(get_int("  42  "))
print(get_int("nope"))
print(make_report("SUMMARY", "row 1", "row 2"))

