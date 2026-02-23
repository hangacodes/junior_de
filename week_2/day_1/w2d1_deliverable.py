'''### 6D — Primary Deliverable

**Deliverable:** `quality_flags_report.py`

Write a script that processes **three** hardcoded CSV-like rows and prints a quality report for each.

**Row format:** `"name,age,country"` (example: `"maria,32,DE"`)

**For each row, print:**
- `name` (the parsed string)
- `age` (as an int after conversion)
- `country`
- `age_nonnegative` flag (age >= 0)
- `age_reasonable` flag (age <= 120)
- `country_two_chars` flag (len == 2)

**Constraints:**
- No `if` statements (not introduced yet)
- No `and`/`or`/`not` (tomorrow)
- No loops (Week 3)
- Repeating code for each row is expected

**What Could Go Wrong?**
- What happens if `age` is negative (like `"-5"`)? Does your `age_nonnegative` flag catch it?
- What happens if `country` is `"USA"` (3 characters)? Does your `country_two_chars` flag catch it?

*You’ll write similar parsing code 3 times here. In Week 3, you’ll handle this with a `for` loop in 3 lines. 
For now, notice the repetition—that recognition is exactly what will make loops feel natural when you get there.*'''



#Row 1
r1 = "cristian,30,RO"
parts = r1.split(",")
name = parts[0]
age =  int(parts[1])
country = parts[2]

age_nonnegative = age >= 0
age_reasonable = age <= 120
country_two_chars = len(country) == 2

#Row 2
r2 = "michael,32,USA"
parts1 = r2.split(",")
name1 = parts1[0]
age1 =  int(parts1[1])
country1 = parts1[2]

age_nonnegative1 = age1 >= 0
age_reasonable1 = age1 <= 120
country_two_chars1 = len(country1) == 2

#Row 3
r3 = "josh,-3,US"
parts2 = r3.split(",")
name2 = parts2[0]
age2 =  int(parts2[1])
country2 = parts2[2]

age_nonnegative2 = age2 >= 0
age_reasonable2 = age2 <= 120
country_two_chars2 = len(country2) == 2


print("===SUMMARY===")

print("\nUser details:")
print(f"1st: {name} is {age} years old and is from {country}")
print(f"2nd: {name1} is {age1} years old and is from {country1}")
print(f"3rd: {name2} is {age2} years old and is from {country2}")
print("------------------------------------------------------")
print("===FLAGS===")
print("\n1st user:")
print(f"Age nonnegative: {age_nonnegative}")
print(f"Age reasonable: {age_reasonable}")
print(f"Country has two chars: {country_two_chars}")
print("------------------------------------------------------")
print("2nd user:")
print(f"Age nonnegative: {age_nonnegative1}")
print(f"Age reasonable: {age_reasonable1}")
print(f"Country has two chars: {country_two_chars1}")
print("------------------------------------------------------")
print("3rd user:")
print(f"Age nonnegative: {age_nonnegative2}")
print(f"Age reasonable: {age_reasonable2}")
print(f"Country has two chars: {country_two_chars2}")


# I did this a little differently than the answer key from the lesson but is the same and i think it looks better. I might be wrong.

#Deliverable Solution from lesson :
# quality_flags_report.py

'''
# Row 1
row1 = "maria,32,DE"
p1 = row1.split(",")
name1 = p1[0]
age1 = int(p1[1])
country1 = p1[2]

age1_nonnegative = age1 >= 0
age1_reasonable = age1 <= 120
country1_two_chars = len(country1) == 2

print("ROW 1")
print(f"name={name1}")
print(f"age={age1}")
print(f"country={country1}")
print(f"age_nonnegative={age1_nonnegative}")
print(f"age_reasonable={age1_reasonable}")
print(f"country_two_chars={country1_two_chars}")
print("-----")

# Row 2
row2 = "li,-5,USA"
p2 = row2.split(",")
name2 = p2[0]
age2 = int(p2[1])
country2 = p2[2]

age2_nonnegative = age2 >= 0
age2_reasonable = age2 <= 120
country2_two_chars = len(country2) == 2

print("ROW 2")
print(f"name={name2}")
print(f"age={age2}")
print(f"country={country2}")
print(f"age_nonnegative={age2_nonnegative}")
print(f"age_reasonable={age2_reasonable}")
print(f"country_two_chars={country2_two_chars}")
print("-----")

# Row 3
# This repeats 3x — for loops (Week 3) will collapse this to ~5 lines
row3 = "noah,121,FR"
p3 = row3.split(",")
name3 = p3[0]
age3 = int(p3[1])
country3 = p3[2]

age3_nonnegative = age3 >= 0
age3_reasonable = age3 <= 120
country3_two_chars = len(country3) == 2

print("ROW 3")
print(f"name={name3}")
print(f"age={age3}")
print(f"country={country3}")
print(f"age_nonnegative={age3_nonnegative}")
print(f"age_reasonable={age3_reasonable}")
print(f"country_two_chars={country3_two_chars}")
print("-----")
'''