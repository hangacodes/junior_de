# Raw student records — each line: "name, age, grade_percentage, city"
record_1 = "   ALICE JOHNSON , 17, 88.5,  Moscow  "
record_2 = "bob SMITH,  20 ,  72.3, london"
record_3 = " Charlie Brown,  sixteen, 95.1,NEW YORK "
record_4 = "   Diana Prince , 19,  101.5,  tokyo"
record_5 = "  EVE WILLIAMS, 22, -5, Berlin  "
record_6 = "  frank,  18,  65.0,  PARIS "
record_7 = "Grace Hopper,  21, 89.7,   "

#Parsing and Cleaning

student1_parts = record_1.split(",")
name1 = student1_parts[0].strip().title()
age1 = student1_parts[1].strip()
grade1 = student1_parts[2].strip()
city1 = student1_parts[3].strip().title()

print(f"Record 1 - Name: {name1} | Age: {age1} | Grade: {grade1} | City: {city1}")

student2_parts = record_2.split(",")
name2 = student2_parts[0].strip().title()
age2 = student2_parts[1].strip()
grade2 = student2_parts[2].strip()
city2 = student2_parts[3].strip().title()

print(f"Record 2 - Name: {name2} | Age: {age2} | Grade: {grade2} | City: {city2}")

student3_parts = record_3.split(",")
name3 = student3_parts[0].strip().title()
age3 = student3_parts[1].strip()
grade3 = student3_parts[2].strip()
city3 = student3_parts[3].strip().title()

print(f"Record 3 - Name: {name3} | Age: {age3} | Grade: {grade3} | City: {city3}")

student4_parts = record_4.split(",")
name4 = student4_parts[0].strip().title()
age4 = student4_parts[1].strip()
grade4 = student4_parts[2].strip()
city4 = student4_parts[3].strip().title()

print(f"Record 4 - Name: {name4} | Age: {age4} | Grade: {grade4} | City: {city4}")

student5_parts = record_5.split(",")
name5 = student5_parts[0].strip().title()
age5 = student5_parts[1].strip()
grade5 = student5_parts[2].strip()
city5 = student5_parts[3].strip().title()

print(f"Record 5 - Name: {name5} | Age: {age5} | Grade: {grade5} | City: {city5}")

student6_parts = record_6.split(",")
name6 = student6_parts[0].strip().title()
age6 = student6_parts[1].strip()
grade6 = student6_parts[2].strip()
city6 = student6_parts[3].strip().title()

print(f"Record 6 - Name: {name6} | Age: {age6} | Grade: {grade6} | City: {city6}")

student7_parts = record_7.split(",")
name7 = student7_parts[0].strip().title()
age7 = student7_parts[1].strip()
grade7 = student7_parts[2].strip()
city7 = student7_parts[3].strip().title()

print(f"Record 7 - Name: {name7} | Age: {age7} | Grade: {grade7} | City: {city7}")
print("\n")
#Student 1
valid1 = True
#Age Validation:
try:
    age1 = int(age1)
    if age1 <= 16 and age1 >= 65:
        print(f"{name1}: INVALID AGE - [age must be between 16 and 65]")
        valid1 = False
except ValueError:
    print(f"{name1}: Age has the wrong value")
    valid1 = False

#Grade: 
try:
    grade1_f = float(grade1)
    if not (0.0 <= grade1_f <= 100.0):
        print(f"{name1}: INVALID GRADE - [grade must be between 0 and 100]")
        valid1 = False
except ValueError:
    print(f"{name1}: INVALID GRADE - [grade must be a number]")
    valid1 = False
#City validation:
if city1 == "":
    print(f"{name1}: MISSING CITY")
    valid1 = False

#Valid Output - if everything passed:

if valid1:
    print(f"✓ {name1} - Age: {age1}, Grade: {grade1_f}%, City: {city1}")

#Student 2:
valid2 = True
#Age Validation:

try:
    age2 = int(age2)
    if age2 <= 16 and age2 >= 65:
        print(f"{name2}: INVALID AGE - [age must be between 16 and 65]")
        valid2 = False
except ValueError:
    print(f"{name2}: Age has the wrong value")
    valid2 = False

#Grade: 
try:
    grade2_f = float(grade2)
    if not (0.0 <= grade2_f <= 100.0):
        print(f"{name2}: INVALID GRADE - [grade must be between 0 and 100]")
        valid2 = False
except ValueError:
    print(f"{name2}: INVALID GRADE - [grade must be a number]")
    valid2 = False
#City validation:
if city2 == "":
    print(f"{name2}: MISSING CITY")
    valid2 = False

#Valid Output - if everything passed:

if valid2:
    print(f"✓ {name2} - Age: {age2}, Grade: {grade2_f}%, City: {city2}")

#Stundent 3 
valid3 = True

try:
    age3 = int(age3)
    if not (16 <= age3 <= 65):
        print(f"{name3}: INVALID AGE - [age must be between 16 and 65]")
        valid3 = False
except ValueError:
    print(f"{name3}: INVALID AGE - [age must be a number]")
    valid3 = False
try:
    grade3_f = float(grade3)
    if not(0.0 <= grade2_f <= 100.0):
        print(f"{name3}: INVALID GRADE - [grade must be between 0.0 and 100.0]")
        valid3 = False
except ValueError:
    print(f"{name3}: INVALID GRADE - [grade must be a number]")
    valid3 = False

if city3 == "":
    print(f"{name3}: MISSING CITY")
    valid3 = False

if valid3:
    print(f"✓ {name3} - Age: {age3}, Grade: {grade3_f}%, City: {city3}")

#Student 4
valid4 = True
#Age Validation:
try:
    age4 = int(age4)
    if age4 <= 16 and age4 >= 65:
        print(f"{name4}: INVALID AGE - [age must be between 16 and 65]")
        valid4 = False
except ValueError:
    print(f"{name4}: Age has the wrong value")
    valid4 = False

#Grade: 
try:
    grade4_f = float(grade4)
    if not (0.0 <= grade4_f <= 100.0):
        print(f"{name4}: INVALID GRADE - [grade must be between 0 and 100]")
        valid4 = False
except ValueError:
    print(f"{name4}: INVALID GRADE - [grade must be a number]")
    valid4 = False
#City validation:
if city4 == "":
    print(f"{name4}: MISSING CITY")
    valid4 = False

#Valid Output - if everything passed:

if valid4:
    print(f"✓ {name4} - Age: {age4}, Grade: {grade4_f}%, City: {city4}")

#Student 5
valid5 = True
#Age Validation:
try:
    age5 = int(age5)
    if age5 <= 16 and age5 >= 65:
        print(f"{name5}: INVALID AGE - [age must be between 16 and 65]")
        valid5 = False
except ValueError:
    print(f"{name5}: Age has the wrong value")
    valid5 = False

#Grade: 
try:
    grade5_f = float(grade5)
    if not (0.0 <= grade5_f <= 100.0):
        print(f"{name5}: INVALID GRADE - [grade must be between 0 and 100]")
        valid5 = False
except ValueError:
    print(f"{name5}: INVALID GRADE - [grade must be a number]")
    valid5 = False
#City validation:
if city5 == "":
    print(f"{name5}: MISSING CITY")
    valid5 = False

#Valid Output - if everything passed:

if valid5:
    print(f"✓ {name5} - Age: {age5}, Grade: {grade5_f}%, City: {city5}")

    #Student 6
valid6 = True
#Age Validation:
try:
    age6 = int(age6)
    if age6 <= 16 and age6 >= 65:
        print(f"{name6}: INVALID AGE - [age must be between 16 and 65]")
        valid6 = False
except ValueError:
    print(f"{name6}: Age has the wrong value")
    valid6 = False

#Grade: 
try:
    grade6_f = float(grade6)
    if not (0.0 <= grade6_f <= 100.0):
        print(f"{name6}: INVALID GRADE - [grade must be between 0 and 100]")
        valid6 = False
except ValueError:
    print(f"{name6}: INVALID GRADE - [grade must be a number]")
    valid6 = False
#City validation:
if city6 == "":
    print(f"{name6}: MISSING CITY")
    valid6 = False

#Valid Output - if everything passed:

if valid6:
    print(f"✓ {name6} - Age: {age6}, Grade: {grade6_f}%, City: {city6}")

    #Student 7
valid7 = True
#Age Validation:
try:
    age7 = int(age7)
    if age7 <= 16 and age7 >= 65:
        print(f"{name7}: INVALID AGE - [age must be between 16 and 65]")
        valid7 = False
except ValueError:
    print(f"{name7}: Age has the wrong value")
    valid7 = False

#Grade: 
try:
    grade7_f = float(grade7)
    if not (0.0 <= grade7_f <= 100.0):
        print(f"{name7}: INVALID GRADE - [grade must be between 0 and 100]")
        valid7 = False
except ValueError:
    print(f"{name7}: INVALID GRADE - [grade must be a number]")
    valid7 = False
#City validation:
if city7 == "":
    print(f"{name7}: MISSING CITY")
    valid7 = False

#Valid Output - if everything passed:

if valid7:
    print(f"✓ {name7} - Age: {age7}, Grade: {grade7_f}%, City: {city5}")

print("\n")
#Grade Classification
if valid1:
    if 90.0 <= grade1_f <= 100.0:
        label1 = "Excellent"
        letter1 = "A"
    elif 80.0 <= grade1_f <= 89.9:
        label1 = "Good"
        letter1 = "B"
    elif 70.0 <= grade1_f <= 79.9:
        label1 = "Satisfactory"
        letter1 = "C"
    elif 60.0 <= grade1_f <= 69.9:
        label1 = "Needs Improvement"
        letter1 = "D"
    else:
        label1 = "Failing"
        letter1 = "F"

    print(f"{name1}: {grade1_f}% -> {letter1} ({label1})")

if valid2:
    if 90.0 <= grade2_f <= 100.0:
        label1 = "Excellent"
        letter1 = "A"
    elif 80.0 <= grade2_f <= 89.9:
        label2 = "Good"
        letter2 = "B"
    elif 70.0 <= grade2_f <= 79.9:
        label2 = "Satisfactory"
        letter2 = "C"
    elif 60.0 <= grade2_f <= 69.9:
        label2 = "Needs Improvement"
        letter2 = "D"
    else:
        label2 = "Failing"
        letter2 = "F"

    print(f"{name2}: {grade2_f}% -> {letter2} ({label2})")

if valid3:
    if 90.0 <= grade3_f <= 100.0:
        label3 = "Excellent"
        letter3 = "A"
    elif 80.0 <= grade3_f <= 89.9:
        label3 = "Good"
        letter3 = "B"
    elif 70.0 <= grade3_f <= 79.9:
        label3 = "Satisfactory"
        letter3 = "C"
    elif 60.0 <= grade3_f <= 69.9:
        label3 = "Needs Improvement"
        letter3 = "D"
    else:
        label3 = "Failing"
        letter3 = "F"

    print(f"{name3}: {grade3_f}% -> {letter3} ({label3})")

if valid4:
    if 90.0 <= grade4_f <= 100.0:
        label4 = "Excellent"
        letter4= "A"
    elif 80.0 <= grade4_f <= 89.9:
        label4 = "Good"
        letter4 = "B"
    elif 70.0 <= grade4_f <= 79.9:
        label4 = "Satisfactory"
        letter4 = "C"
    elif 60.0 <= grade4_f <= 69.9:
        label4 = "Needs Improvement"
        letter4 = "D"
    else:
        label4 = "Failing"
        letter4 = "F"

    print(f"{name4}: {grade4_f}% -> {letter4} ({label4})")

if valid5:
    if 90.0 <= grade5_f <= 100.0:
        label5= "Excellent"
        letter5= "A"
    elif 80.0 <= grade5_f <= 89.9:
        label5 = "Good"
        letter5 = "B"
    elif 70.0 <= grade5_f <= 79.9:
        label5 = "Satisfactory"
        letter5 = "C"
    elif 60.0 <= grade5_f <= 69.9:
        label5 = "Needs Improvement"
        letter5 = "D"
    else:
        label5 = "Failing"
        letter5 = "F"

    print(f"{name5}: {grade5_f}% -> {letter5} ({label5})")

if valid6:
    if 90.0 <= grade6_f <= 100.0:
        label6= "Excellent"
        letter6= "A"
    elif 80.0 <= grade6_f <= 89.9:
        label6 = "Good"
        letter6 = "B"
    elif 70.0 <= grade6_f <= 79.9:
        label6 = "Satisfactory"
        letter6 = "C"
    elif 60.0 <= grade6_f <= 69.9:
        label6 = "Needs Improvement"
        letter6 = "D"
    else:
        label6 = "Failing"
        letter6 = "F"

    print(f"{name6}: {grade6_f}% -> {letter6} ({label6})")

if valid7:
    if 90.0 <= grade7_f <= 100.0:
        label7= "Excellent"
        letter7= "A"
    elif 80.0 <= grade7_f <= 89.9:
        label7 = "Good"
        letter7 = "B"
    elif 70.0 <= grade7_f <= 79.9:
        label7 = "Satisfactory"
        letter7 = "C"
    elif 60.0 <= grade7_f <= 69.9:
        label7 = "Needs Improvement"
        letter7 = "D"
    else:
        label7 = "Failing"
        letter7 = "F"

    print(f"{name7}: {grade7_f}% -> {letter7} ({label7})")

    #Summary Statistics 
total_records_processed = 7
total_valid_records = 3
total_invalid_records = total_records_processed - total_valid_records


average_grade = (88.5 + 72.3 + 65.0) / 3
print("═══════════════════════════════════")
print("\tSTUDENT REPORT SUMMARY")
print("═══════════════════════════════════")
print(f"\nTotal records processed: {total_records_processed}")
print(f"Valid records: {total_valid_records}")
print(f"Invalid records: {total_invalid_records}")

print(f"\nAverage grade: {average_grade:.1f}%")
print(f"Highest grade: {name1} - {grade1_f}%")
print(f"Lowest grade: {name6} - {grade6_f}%")

print(f"\nPassing (≥60%): 2 students")
print(f"Failing (<60%): 1 student")

