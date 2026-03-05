rows = [
    "s-1,21.5,OK",
    "s-2,not_a_float,OK",
    "s-3,19.0,BAD",
    "s-4,18.2,WARN",
    "broken_row",
    "s-5,17.1,FAIL"
]
bad_field_count = 0
bad_temp_count = 0
bad_status_count = 0

valid_count = 0

valid_rows = []
invalid_rows = []


for idx, row in enumerate(rows):
    
    parts = row.split(",")
    if len(parts) != 3:
        bad_field_count += 1
        invalid_rows.append(row)
    else:
        temp_text = parts[1].strip()
        status = parts[2].strip()
    
        try:
            temp_c = float(temp_text)
            temp_ok = True
        except ValueError:
            temp_ok = False

        if temp_ok:
            if status in ["OK","WARN","FAIL"]:
                status_ok = True
                valid_count += 1
                valid_rows.append(row)
            else:
                status_ok = False
                bad_status_count += 1
                invalid_rows.append(row)
        else:
            bad_temp_count += 1
            invalid_rows.append(row)

print("===SUMMARY===\n")
print(f"Total rows: {len(rows)}")
print(f"Valid rows: {valid_count}")
print(f"Invalid rows: {len(invalid_rows)}")
print(f"Invalid bad temp rows: {bad_temp_count}")
print(f"Invalid bad status rows: {bad_status_count}")

for idx, row in enumerate(rows):
    if row in invalid_rows:
        print(idx, row)

#THIS SHIII IS HARD ! LMAO