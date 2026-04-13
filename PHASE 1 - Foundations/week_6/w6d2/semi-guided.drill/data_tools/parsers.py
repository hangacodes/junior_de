def parse_csv_row(line, delimiter=","):
    lst = []
    parts = line.split(delimiter)
    for part in parts:
        lst.append(part.strip())
    return lst
    #TODO: split line by delimiter, strip each field, return as a list
    # Hint: use .split(delimiter) then a loop with .strip() — accumulator pattern from W3D4
    

def parse_kv_pair(text, sep="="):
    parts = text.split(sep, 1)
    k = parts[0].strip()
    v = parts[1].strip()

    return {
        "key": k,
        "value": v
    }
    #TODO: split on sep (max 1 split), strip key and value, return as a dict {"key": k, "value": v}
    # Hint: text.split(sep, 1) limits to one split — handles values containing "="
    