'''#Challenge 1 : Type converter 
first = "42.7"

second = float(first)
third = int(second)

print(type(first))
print(type(second))
print(type(third))'''

#Challenge 2 : String surgery

'''raw = "   John DOE, age:29, city:moscow   "

parts = raw.split(",")

name = parts[0].strip().lower()

age_parts = parts[1].split(":")
age = int(age_parts[1])

city_txt = parts[2].split(":")
city = city_txt[1].strip()

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(type(age))'''

#Challenge 3: Operator Gauntlet
#Without running the code first, predict the output of each line. 
#Then run it and check yourself.

'''print(17 // 5)  #3
print(17 % 5)   #2
print(2 ** 3 ** 2)  #64? - wrong
print(10 / 3) #3.33 - ... wrong i guess
print(10 // 3)  #3
print(bool(0)) #True - wrong - 0 is always falsy fk.
print(bool("")) #False
print(bool(" ")) #True
print(bool("False")) #False - wrong - ofc, it's a string lol'''

#Challenge 4 : Slice master
'''Using only slicing (no methods), extract:
1. `"data"`
2. `"engineering"`
3. `"2026"`
4. `"6202_gnireenigne_atad"` (reversed)
5. `"dt_niern_02"` (every other character)'''

'''text = "data_engineering_2026"

first = text[0:4]
print(first)

second = text[5:16]
print(second)

year = text[17:]
print(year)

reversed_text = text[::-1]
print(reversed_text)

every_other = text[::2]
print(every_other)
'''

#Challenge 5: Input validator
'''Write a script that asks the user for their age and validates it:
- Must convert to an integer (catch `ValueError`)
- Must be between 0 and 150 (inclusive)
- Must not be empty input
- Print a clear success or error message for each failure mode

Test it with these inputs: `25`, `abc`, `-5`, `200`, ``(empty),`30.5`'''

'''age_text = input("Enter your age: ")

if age_text == "":
    print("ERROR: you must type your age")
else:
    try:
        age = int(age_text)
        if age <= 0 or age >= 150:
            print("ERROR: enter a valid age ( above 0 and below 150)")
        else:
            print("Age OK")
    except ValueError:
        print("ERROR: you must enter a number")


'''

#Challenge 6: Multi Condition Logic
'''Write a script that takes a year as input and determines if it’s a leap year.
#WHAT IS A LEAP YEAR !? LOL - got it, a year with 366 days

Rules (implement all of them):
- Divisible by 4 → leap year
- BUT divisible by 100 → NOT a leap year
- BUT divisible by 400 → IS a leap year

Test with: `2024`, `1900`, `2000`, `2023`

Use guard clauses — avoid nesting more than two levels deep.'''

'''try:
    year = int(input("Enter a year: "))
    if year % 400 == 0:
        print("This is a leap year!")
    elif year % 100 ==0:
        print("This is not a leap year")
    elif year % 4 != 0:
        print("This is not a leap year!")
    else: 
        print("This is leap year!")
except ValueError:
    print("ERROR: please enter a year number")'''

#Challenge 7 : Data Cleaner

'''Requirements:
- Strip all whitespace
- Name should be title case
- City should be title case
- Age should be converted to int
- If age conversion fails, print an error message for that row and continue?????'''

row1 = "  alice , 28,  MOSCOW "
row2 = "BOB,  35 ,london"
row3 = "  Charlie,22,  NEW YORK  "
row4 = "  diana,  41, tokyo "
row5 = "EVE ,30,   BERLIN  "

row1_parts = row1.split(",")
row2_parts = row2.split(",")
row3_parts = row3.split(",")
row4_parts = row4.split(",")
row5_parts = row5.split(",")


#Row1
name_raw1 = row1_parts[0].strip().lower().title()
age_txt1 = row1_parts[1].strip()
city_raw1 = row1_parts[2].strip().lower().title()
try:
    age1 = int(age_txt1)
except ValueError:
    print("ERROR: invalid age for row 1, skipping")

#Row2
name_raw2 = row2_parts[0].strip().lower().title()
age_txt2 = row2_parts[1].strip()
city_raw2 = row2_parts[2].strip().lower().title()
try:
    age2 = int(age_txt2)
except ValueError:
    print("ERROR: invalid age for row 2, skipping")

#Row3
name_raw3 = row3_parts[0].strip().lower().title()
age_txt3 = row3_parts[1].strip()
city_raw3 = row3_parts[2].strip().lower().title()
try:
    age3 = int(age_txt3)
except ValueError:
    print("ERROR: invalid age for row 3, skipping")

#Row4
name_raw4 = row4_parts[0].strip().lower().title()
age_txt4 = row4_parts[1].strip()
city_raw4 = row4_parts[2].strip().lower().title()
try:
    age4 = int(age_txt4)
except ValueError:
    print("ERROR: invalid age for row 4, skipping")

#Row5
name_raw5 = row5_parts[0].strip().lower().title()
age_txt5 = row5_parts[1].strip()
city_raw5 = row5_parts[2].strip().lower().title()
try:
    age5 = int(age_txt5)
except ValueError:
    print("ERROR: invalid age for row 5, skipping")

#For each row, parse and clean it , then print:
'''Name: Alice | Age: 28 | City: Moscow
Name: Bob | Age: 35 | City: London
...'''

print(f"Name: {name_raw1} | Age: {age1} | City: {city_raw1}")
print(f"Name: {name_raw2} | Age: {age2} | City: {city_raw2}")
print(f"Name: {name_raw3} | Age: {age3} | City: {city_raw3}")
print(f"Name: {name_raw4} | Age: {age4} | City: {city_raw4}")
print(f"Name: {name_raw5} | Age: {age5} | City: {city_raw5}")
