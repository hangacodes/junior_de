'''**Build:** A “ticket code parser” for codes shaped like `BER-20260209-4821`.

Format is always: City (3 chars) + dash + Date (8 chars, YYYYMMDD) + dash + Ticket ID (4 chars).

**Requirements:**

1. Parse three codes (hard-code them as `code1`, `code2`, `code3`).
2. For each code, print: `city=...`, `date=YYYY-MM-DD`, `ticket_id=...`, `ticket_last_digit=...` (use indexing for the last digit).

'''
# --- Code 1 ---
code1 = "MSK-19950426-1111"
city1 = code1[0:3]
date1 = code1[4:8] + "-" + code1[8:10] + "-" + code1[10:12]
ticket_id1 = code1[13:]
ticket_last_digit1 = code1[-1]

#--- Code 2 ---
code2 = "OMR-19950823-2222"
city2 = code2[0:3]
date2 = code2[4:8] + "-" + code2[8:10] + "-" + code2[10:12]
ticket_id2 = code2[13:]
ticket_last_digit2 = code2[-1]


#--- Code 3 ---
code3 = "MIA-20230305-6969"
city3 = code3[0:3]
date3 = code3[4:8] + "-" + code3[8:10] + "-" + code3[10:12]
ticket_id3 = code3[13:]
ticket_last_digit3 = code3[-1]

print(len(code1))
print(code1[16])
print(city1)
print(city2)
print(city3)

print(date1)
print(date2)
print(date3)

print(ticket_id1)
print(ticket_id2)
print(ticket_id3)

print(ticket_last_digit1)
print(ticket_last_digit2)
print(ticket_last_digit3)

# This deliverable was made strictly from my head. The example in the lesson, looks a little better. I can do that too. I just didn't name the variables for year, month and day. I just instantly added them
# Which way is better ?
#Example : 
'''
code1 = "BER-20260209-4821"
code2 = "PAR-20261205-1099"
code3 = "ROM-20250101-0007"

# --- Code 1 ---
city      = code1[0:3]
raw_date  = code1[4:12]
ticket_id = code1[13:17]

year  = raw_date[0:4]
month = raw_date[4:6]
day   = raw_date[6:8]

print("CODE 1")
print(f"city={city}")
print(f"date={year}-{month}-{day}")
print(f"ticket_id={ticket_id}")
print(f"ticket_last_digit={ticket_id[-1]}")
print()

# --- Code 2 ---
city      = code2[0:3]
raw_date  = code2[4:12]
ticket_id = code2[13:17]

year  = raw_date[0:4]
month = raw_date[4:6]
day   = raw_date[6:8]

print("CODE 2")
print(f"city={city}")
print(f"date={year}-{month}-{day}")
print(f"ticket_id={ticket_id}")
print(f"ticket_last_digit={ticket_id[-1]}")
print()

# --- Code 3 ---
city      = code3[0:3]
raw_date  = code3[4:12]
ticket_id = code3[13:17]

year  = raw_date[0:4]
month = raw_date[4:6]
day   = raw_date[6:8]

print("CODE 3")
print(f"city={city}")
print(f"date={year}-{month}-{day}")
print(f"ticket_id={ticket_id}")
print(f"ticket_last_digit={ticket_id[-1]}")
'''







