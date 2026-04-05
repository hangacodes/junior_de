'''
Function for smart CSV splitting - quotes aware
'''
def split_csv_line(line, delimiter=","):
    
    # the three things we track throughout the whole walk
    fields = []       # completed fields go here
    current = ""      # we're building the current field character by character
    in_quotes = False # are we currently inside a quoted section?

    i = 0
    while i < len(line):       # walk every character, one at a time
        ch = line[i]           # ch = the character at position i

        if ch == '"':
            # a quote flips the switch — opens if closed, closes if open
            # same character does both jobs, so we can't hardcode True or False
            in_quotes = not in_quotes

        elif ch == delimiter and not in_quotes:
            # a comma OUTSIDE quotes = real delimiter = end of this field
            fields.append(current)  # save what we built so far
            current = ""            # reset for the next field

        else:
            # anything else (letters, digits, spaces, commas INSIDE quotes)
            # just gets added to the field we're currently building
            current += ch

        i += 1  # move to the next character

    # the loop ends without saving the last field (no trailing comma to trigger it)
    # so we do it manually here
    fields.append(current)
    return fields

'''### Example 1 — ⭐⭐ Why `split(",")` fails on real CSV

**What it demonstrates:** The comma-inside-quotes problem that makes naive splitting wrong.'''
row = 'Ana,"Helsinki, Finland",29'
naive = row.split(",")
print(f"Naive split ({len(naive)} pieces):{naive}")

proper = split_csv_line(row)  # using the function from Term 3
print(f"Quote-aware ({len(proper)} pieces):{proper}")



# print(split_csv_line('Ada,"Berlin, Germany",29'))
# # output: ['Ada', 'Berlin, Germany', '29']

# row = 'Ana,"Helsinki, Finland",29'
# naive = row.split(",")
# print(f"Naive split ({len(naive)} pieces):{naive}")

# proper = split_csv_line(row)  # using the function from Term 3
# print(f"Quote-aware ({len(proper)} pieces):{proper}")


'''### Example 2 — ⭐⭐⭐ Parsing a complete CSV string into a list of dicts

**What it demonstrates:** Header extraction + row-by-row mapping using `split_csv_line()` + `for` loop with `range()`.'''
# The raw CSV text — \n represents a line break (a new row)
csv_text = 'name,city,age\nAda,"Helsinki, Finland",29\nBob,Tokyo,31'

# .strip() removes leading/trailing whitespace, .split("\n") breaks into a list of lines
lines = csv_text.strip().split("\n")

# lines[0] is always the header row — we parse it into a list of column names
headers = split_csv_line(lines[0])
# headers = ['name', 'city', 'age']

records = []

# i starts at 1 (not 0) to skip the header row — we only want data rows
for i in range(1, len(lines)):

    # parse the current line into a list of field values
    fields = split_csv_line(lines[i])

    record = {}

    # j is the position — used to match headers[j] (the key) with fields[j] (the value)
    for j in range(len(headers)):

        if j < len(fields):
            # normal case — a value exists at this position, strip any extra whitespace
            record[headers[j]] = fields[j].strip()
        else:
            # the row is short — fewer fields than headers, so we fill the gap with ""
            record[headers[j]] = ""

    # the completed record dict gets added to the list
    records.append(record)

# print each record on its own line
for r in records:
    print(r)


'''### Example 3 — ⭐⭐⭐ Cast + validate + separate good from bad

**What it demonstrates:** The full pipeline — parsing, casting, validating, error reporting — in one flow.'''
def cast_record(record, schema):
    typed = {}
    for key in record:
        typed[key] = record[key]  # copy all fields as-is first

    for col in schema:
        target_type = schema[col]
        value = record[col].strip()
        if value == "":
            return None, f"Empty value for required column:{col}"
        try:
            typed[col] = target_type(value)
        except ValueError:
            return None, f"Cannot cast '{value}' to {target_type.__name__} for column '{col}'"

    return typed, ""


def validate_record(record):
    if record["name"].strip() == "":
        return False, "name is empty"
    if record["age"] < 0 or record["age"] > 120:
        return False, "age out of range"
    return True, ""


# Multi-line string — Python joins these into one string automatically
# Each line ends with \n to represent a new row
csv_text = (
    "name,city,age\n"
    "Ada,Berlin,29\n"
    ",Tokyo,31\n"       # name is empty — will fail validation
    "Cara,Lagos,xyz\n"  # age is not a number — will fail casting
    "Dan,Moscow,999"    # age is a number but 999 — will fail validation
)

# the rules: which columns need type conversion and to what type
schema = {"age": int}

# break the full string into a list of lines, strip any trailing whitespace first
lines = csv_text.strip().split("\n")

# parse the first line into column names
headers = split_csv_line(lines[0])
# headers = ['name', 'city', 'age']

# two buckets — rows that pass everything go here
good_records = []
# rows that fail any check go here, with a reason attached
error_report = []

# start at 1 to skip the header row
for i in range(1, len(lines)):

    # row_num tracks the human-readable row number (header counts as row 1)
    row_num = i + 1

    # the raw unparsed text of this line — saved for the error report
    raw = lines[i]

    # split the line into individual field values
    fields = split_csv_line(raw)

    # CHECK 1: does this row have exactly as many fields as the header?
    if len(fields) != len(headers):
        error_report.append({"row": row_num, "error": "wrong field count", "raw": raw})
        continue  # skip the rest of the loop for this row, move to the next

    # build the record dict by pairing headers[j] with fields[j]
    record = {}
    for j in range(len(headers)):
        record[headers[j]] = fields[j].strip()

    # CHECK 2: try to cast values to their required types (e.g. "29" → 29)
    # cast_record returns (typed_record, "") on success or (None, error_message) on failure
    typed, cast_error = cast_record(record, schema)
    if typed is None:
        error_report.append({"row": row_num, "error": cast_error, "raw": raw})
        continue  # casting failed — skip validation, move to next row

    # CHECK 3: run business rules (e.g. name can't be empty, age must be realistic)
    # validate_record returns (True, "") on success or (False, reason) on failure
    ok, reason = validate_record(typed)
    if not ok:
        error_report.append({"row": row_num, "error": reason, "raw": raw})
    else:
        # passed all three checks — this is a clean record
        good_records.append(typed)

# summary line
print(f"Good:{len(good_records)}, Bad:{len(error_report)}")

# print each clean record
for r in good_records:
    print(f"  ✓{r}")

# print each bad record with its row number and reason
for e in error_report:
    print(f"  ✗ Row{e['row']}:{e['error']}")