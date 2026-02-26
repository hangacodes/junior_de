'''**Build:** A “ticket code parser” for codes shaped like `BER-20260209-4821`.

Format is always: City (3 chars) + dash + Date (8 chars, YYYYMMDD) + dash + Ticket ID (4 chars).

**Requirements:**

1. Parse three codes (hard-code them as `code1`, `code2`, `code3`).
2. For each code, print: `city=...`, `date=YYYY-MM-DD`, `ticket_id=...`, `ticket_last_digit=...` (use indexing for the last digit).

'''
# --- Code 1 ---
code1 = "BUC-20260218-1692"
city1 = code1[0:3]
date1 = code1[4:8] + "-" + code1[8:10] + "-" + code1[10:12]
ticket_id1 = code1[13:]
ticket_last_digit1 = code1[-1]
print("CODE 1:")
print(f"city={city1}")
print(f"date={date1}")
print(f"ticket_id={ticket_id1}")
print(f"ticket_last_digit={ticket_id1[-1]}")

#--- Code 2 ---
code2 = "NYC-20260218-1693"
city2 = code2[0:3]
date2 = code2[4:8] + "-" + code2[8:10] + "-" + code2[10:12]
ticket_id2 = code2[13:]
ticket_last_digit2 = code2[-1]
print("\nCODE 2:")
print(f"city={city2}")
print(f"date={date2}")
print(f"ticket_id={ticket_id2}")
print(f"ticket_last_digit={ticket_id2[-1]}")

#--- Code 3 ---
code3 = "MIA-20260218-1694"
city3 = code3[0:3]
date3 = code3[4:8] + "-" + code3[8:10] + "-" + code3[10:12]
ticket_id3 = code3[13:]
ticket_last_digit3 = code3[-1]

print("\nCODE 3:")
print(f"city={city3}")
print(f"date={date3}")
print(f"ticket_id={ticket_id3}")
print(f"ticket_last_digit={ticket_id3[-1]}")








