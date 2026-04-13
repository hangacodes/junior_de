'''**SC-04 — The broken record hospital**

This record has problems. Your job is to diagnose each one in comments, then fix the code so it runs and prints a clean CSV line.

# This should print: True (name starts with "Ada")
print(name.startswith("Ada"))

# This should print age in 10 years: 47
print(age + 10)

# This should print the height rounded to 1 decimal: 1.7
print(round(height, 1))

# This should produce: "Ada Lovelace,37,mathematician,1.7"
csv = ",".join([name, age, role, str(round(height, 1))])
print(csv)


Find all 3 bugs, fix them, and write a comment per bug explaining exactly what was wrong.
'''
raw = "  Ada Lovelace  , 37 , mathematician , 1.70  "
parts = raw.split(",")

name = parts[0].strip()           
age = int(parts[1])            
role = parts[2].lower()
height = float(parts[3].strip()) 
# This should print: True (name starts with "Ada") 
print(name.startswith("Ada")) 
#- i stripped the name

# This should print age in 10 years: 47
print(age + 10)
# - i changed the type from str to int

# This should print the height rounded to 1 decimal: 1.7
print(round(height, 1))
#- had to change it to float , from str

# This should produce: "Ada Lovelace,37,mathematician,1.7"
csv = ",".join([name, str(age), role, str(round(height, 1))])
print(csv)

# just changed the age to str


