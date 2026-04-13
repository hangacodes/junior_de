'''**SC-03 — The ticket parser with arithmetic**

Given `code = "BER-20260209-4821"`:
1. Extract city (slicing)
2. Extract the 8-char date block: `raw_date = code[4:12]`
3. Extract year, month, day from `raw_date` using slicing
4. Compute `ticket_num = int(code[13:17])`
5. Compute `next_ticket = ticket_num + 1`
6. Print a formatted summary:
`City: BER    Date: 2026-02-09    Ticket: 4821    Next available: 4822`
7. Build and print the *next* ticket’s code by assembling parts with `+` and `str()`: `BER-20260209-4822`'''

code = "BER-20260209-4821"

city = code[0:3]
raw_date = code[4:12]

year = raw_date[0:4]
month = raw_date[4:6]
day = raw_date[6:]

ticket_num = int(code[13:17])
next_ticket = ticket_num + 1

formated_summary = (f"City: {city}    Date: {"-".join([str(year), str(month), str(day)])}     Tciket: {ticket_num}    Next available: {next_ticket} ")
print(formated_summary) # FUUUUCK YEAH GOT IT IN THE FIRST TRY HAHAH - "-".join was tricky to build

next_code = ("Next ticket: " + city + "-" + raw_date + "-" + str(next_ticket))
print(next_code)


