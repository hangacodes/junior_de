
'''Activation drills:
1. Given `s = "DATA"`, print the first character.
2. Given `s = "DATA"`, print the last character using a negative index.
3. Given `s = "engineer"`, print `len(s)`.
4. Given `s = "abcdef"`, print `s[1:4]`.
5. Given `s = "abcdef"`, print `s[::-1]`.'''

s = "DATA"

print(s[0])
print(s[-1])

s1 = "engineer"

print(len(s1))

s2 = "abcdef"

print(s2[1:4])
print(s2[::-1])

'''Guided drills with hints
**Drill 1: Pick characters**
Task: `word = "pipeline"` → print the 2nd character and the 5th character (each on its own line).
Hint: “2nd character” is index `1`. “5th character” is index `4`.

**Drill 2: Date slicing**
Task: `date = "2026-12-05"` → extract year, month, day into variables and print: `year=2026 month=12 day=05`.
Hint: year is `date[0:4]`, month is `date[5:7]`, day is `date[8:10]`.

**Drill 3: Safe last character (math version)**
Task: `s = "Berlin"` → print the last character **without** using `-1`.
Hint: use `len(s) - 1`.

**Drill 4: Off-by-one check**
Task: `s = "ABCDE"` → print `"BCD"` using slicing.
Hint: start at index 1; stop must be one past the last character you want
'''
print("\n")
word = "pipeline"

print(word[1])
print(word[4])
print("\n")
data = "2026-12-05"

year = data[0:4]
month = data[5:7]
day = data[8:10]
print(year)
print(month)
print(day)

city = "Berlin"
last_char = city[len(city) -1]
print(last_char)

alphabet = "ABCDE"
print(alphabet[1:4])
print("\n")

#Semi-guided drills
'''**Goal:** Parse a fixed-format record with known separator positions.


**Your tasks:**

1. Add `record_len = len(record)` and print it as `record_len=...`
2. Create `last_char = record[len(record) - 1]` and print it as `last_char=...`
3. Create `user_num = user_id[3:7]` and print it as `user_num=...`'''

#Starter code:

record = "USR0007|Berlin|2026-02-09"

user_id = record[0:7]
city    = record[8:14]
date    = record[15:25]

year  = date[0:4]
month = date[5:7]
day   = date[8:10]

record_len = len(record)
last_char = record[len(record)-1]
user_num = user_id[3:7]

print(f"user_id={user_id}")
print(f"city={city}")
print(f"date={year}-{month}-{day}")
print(record_len)
print(last_char)
print(user_num)