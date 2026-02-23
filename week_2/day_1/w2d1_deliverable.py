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




r1 = "cristian,30,RO"
parts = r1.split(",")
name = parts[0]
age =  int(parts[1])
country = parts[2]

age_nonnegative = age >= 0
age_reasonable = age <= 120
country_two_chars = len(country) == 2



r2 = "michael,32,USA"
parts1 = r2.split(",")
name1 = parts1[0]
age1 =  int(parts1[1])
country1 = parts1[2]

age_nonnegative1 = age1 >= 0
age_reasonable1 = age1 <= 120
country_two_chars1 = len(country1) == 2



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
