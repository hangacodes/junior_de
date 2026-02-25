#Guided drills 
'''**B1 — Fix the indentation**
Make it print `"OK"` when `age >= 18` AND `has_id == True`:'''
age = 19
has_id = True

if age >= 18:
    print("Adult")
    if has_id:
        print("OK")
    else:
        print("Needs ID")


'''**B2 — Add a guard clause**
Print an error if the row doesn't have 3 comma-separated fields, otherwise print `"OK fields"`:'''

row = "Kai,31,DE"
parts = row.split(",")
#TODO: guard clause for field count
if len(parts) != 3:
    print("ERROR: wrong fields")
else:
    print("Ok fields")

'''**B3 — Reorder conditions**
Fix this so negative ages are caught first:'''
age = -10
if age < 0:
    print("ERROR: negative")
elif age > 120:
    print("ERROR: too large")
else:
    print("OK")


#Semi-Guided
'''**C1 — Status + country routing**

Complete the nested logic:'''
row = "Lia,44,FR,active"
parts = row.split(",")

name = parts[0].strip()
age = int(parts[1].strip())
country = parts[2].strip()
status = parts[3].strip()

#TODO: if status is not "active" → print "SKIP"
#TODO: else (active):
#   if country is "DE" or "FR" → print "EU_RULES"
#   else → print "GENERAL_RULES"
if status != "active":
    print("SKIP")
else:
    if country == "DE" or country == "FR":
        print("EU_RULES")
    else:
        print("GENERAL_RULES")

'''**C2 — Refactor to flatten**

Rewrite this with guard-first pattern (same behavior, fewer indent levels):'''

row = "Sam,20"
parts = row.split(",")

'''if len(parts) == 2:
    age = int(parts[1])
    if age >= 0:
        if age <= 120:
            print("OK age")
        else:
            print("ERROR: too high")
    else:
        print("ERROR: negative")
else:
    print("ERROR: wrong fields")'''

if len(parts) != 2:
    print("ERROR: wrong fields")
else:
    age = int(parts[1])
    if age < 0:
        print("ERROR: negative")
    elif age > 120:
        print("ERROR:too high")
    else:
        print("OK age")