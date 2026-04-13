'''raw = [" Ada ", "", "LIN", "  "]

cleaned = []

for name in raw:
    trimmed = name.strip()
    if trimmed != "":
        cleaned.append(trimmed.lower())

print(cleaned)'''

'''rows = ["Ada,34", "Lin,bad", "Sam,28"]

valid_count = 0
age_total = 0

for row in rows:
    parts = row.split(",")
    if len(parts) == 2:
        age_text = parts[1].strip()
        age_ok = True
        try:
            age = int(age_text)
        except ValueError:
            age_ok = False
        if age_ok:
            valid_count = valid_count + 1
            age_total = age_total + age

print(f"valid:{valid_count}, Total age: {age_total}")

'''

'''cols = ["user_id", "emailAddress", "Created_At"]

for idx, col in enumerate(cols):
    lower_col = col.strip().lower()
    if lower_col != col:
        print(f"Column {idx} needs cleaning: '{col}' -> '{lower_col}' ")

print("Audit complete")'''

'''total = 0
for n in [4, 5 , 6]:
    total = total + n
print(total)'''


'''words = ["a", "data", "ok", "pipeline", "hi"]

count = 0
for w in words:
    if len(w) <= 2:
        count = count + 1
print(count)
'''
'''for i in range(1, 6):
    print(i)'''


'''nums = [2,4,6]
total = 0
for num in nums:
    total = total + num
print(total)'''


#ROW PARSING + COUNTING VALID AGES
'''rows = ["Ada,34", "Lin,not_a_number", "Sam,18", "Jo,  "]

count = 0

for row in rows:
    parts = row.split(",")
    age_text = parts[1].strip()
    age_ok = True
    try:
        age = int(age_text)
    except ValueError:
        age_ok = False
    if age_ok:
        count = count + 1

print(count)'''

#Range with step ( odd numbers)
'''for n in range (1, 10, 2):
    print(n)'''

#Semi-Guided
raw_names = [" Ada ", "LINguine", " samuel", "Cristian", ""]

count_names = 0
total_chars = 0
    #TODO: skip empty cleaned names using if
    #TODO: update count_names
    #TODO: update total_chars using len(cleaned.lower())

#TODO: print count_names, total_chars, and average

for raw in raw_names:
    cleaned = raw.strip()
    if cleaned != "":
        count_names = count_names + 1
        total_chars = total_chars + len(cleaned.lower())

print(count_names)
print(total_chars)
average = total_chars / count_names
print(average)

    #TODO: skip empty cleaned names using if
    #TODO: update count_names
    #TODO: update total_chars using len(cleaned.lower())

#TODO: print count_names, total_chars, and average