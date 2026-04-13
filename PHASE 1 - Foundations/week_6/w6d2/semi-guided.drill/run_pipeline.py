# file: run_pipeline.py
from data_tools.parsers import parse_csv_row
import data_tools.validators as dv


#TODO: import parse_csv_row from data_tools.parsers (use from...import)
#TODO: import data_tools.validators as dv (use import...as)

raw_rows = [
    "101, Ada, 28",
    "102, , 35",
    "BAD, Bob, xyz",
    "104, Cara, 19"
]
for row in raw_rows:
    fields = parse_csv_row(row)
    id_ok = dv.is_int_like(fields[0])
    name_ok = dv.is_non_empty(fields[1])

    if id_ok and name_ok:
        print("Pass:", fields)
    else:
        reasons = []
        if not id_ok:
            reasons.append("bad id")
        if not name_ok:
            reasons.append("empty name")
        print("Fail: ", fields, "->", ", ".join(reasons))
#TODO: parse each row using parse_csv_row
#TODO: for each parsed row, validate that field[0] is int-like and field[1] is non-empty
#TODO: print "PASS" or "FAIL" for each row with the reason