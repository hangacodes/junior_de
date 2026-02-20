'''**Build:** A “ticket code parser” for codes shaped like `BER-20260209-4821`.

Format is always: City (3 chars) + dash + Date (8 chars, YYYYMMDD) + dash + Ticket ID (4 chars).

**Requirements:**

1. Parse three codes (hard-code them as `code1`, `code2`, `code3`).
2. For each code, print: `city=...`, `date=YYYY-MM-DD`, `ticket_id=...`, `ticket_last_digit=...` (use indexing for the last digit).

'''

code1 = "MSK-19950426-1118"
code2 = "OMR-19950823-2222"
code3 = "MIA-20230305-6969"

city1 = code1[0:3]
city2 = code2[0:3]
city3 = code3[0:3]

date1 = code1[4:8] + "-" + code1[8:10] + "-" + code1[10:12]
date2 = code2[4:8] + "-" + code2[8:10] + "-" + code2[10:12]
date3 = code3[4:8] + "-" + code3[8:10] + "-" + code3[10:12]

ticket_id1 = code1[13:]
ticket_id2 = code2[13:]
ticket_id3 = code3[13:]

ticket_last_digit1 = code1[-1]
ticket_last_digit2 = code2[-1]
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