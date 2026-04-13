#Guided drills

'''**Drill 1: Normalize a column name**
Given `col = "  Order-ID  "`, produce the clean version `"order_id"` using a chain of methods. Print it.
*Hint:* strip → lower → replace.

**Drill 2: Diagnostic report**
Given `path = "raw/events/2026/01/file.csv"`, print: (a) the index of `"2026"`, (b) the index of `"json"`, (c) whether it ends with `".csv"`.
*Hint:* Use `.find()` twice and `.endswith()` once.

**Drill 3: Count underscores**
Given `key = "user__id"`, print `.count("_")` and `.count("__")` on separate lines. Explain (as a comment) why the counts differ.
*Hint:* Single underscores are counted individually; double-underscore is a different substring.

**Drill 4: Full cleanup pipeline**
Given `raw = "   Sales Report 2026   "`, produce `"sales_report_2026"` using method chaining. Then print whether it starts with `"sales"`.
*Hint:* strip → lower → replace spaces with underscores → startswith check.'''

#Drill 1:
col = "  Order-ID  "
clean_col = col.strip().lower().replace("-","_")
print(clean_col)
print("\n")

#Drill 2:
path = "raw/events/2026/01/file.csv"
print(path.find("2026"))
print(path.find("json"))
print(path.endswith("csv"))
print("\n")
#Drill 3:
key = "user__id"
print(key.count("_"))
print(key.count("__"))  #Because the single underscore appears twice, and the double one is basically found only once in the string.
print("\n")
#Drill 4:
raw = "   Sales Report 2026   "
clean = raw.strip().lower().replace(" ","_")
print(clean)
print(clean.startswith("sales"))

print("\nI've done all these without even looking at the hints!")

#Semi-guided drills:
#Task 1: Clean and diagnose a filename
raw = "   RAW__Events-2026.CSV   "

#TODO: Clean using strip + lower + replace "-" with "_"
#TODO: Print the cleaned version
#TODO: Print how many underscores it contains
#TODO: Print whether it starts with "raw_"
#TODO: Print whether it ends with ".csv"
clean = raw.strip().lower().replace("-","_")
print(clean)
print(clean.count("_"))
print(clean.startswith("raw_"))
print(clean.endswith(".csv"))

#And now i will just remove the two underscores and make it one so it's cleaner
clean_v2 = clean.replace("__","_")
print(clean_v2)     #it worked! 

print("\n")
#Task 2: Check column naming conventions
col1 = " user_id "
col2 = "account"
col3 = "order_id  "

#TODO: Clean each with strip().lower()
#TODO: Print whether each ends with "_id"
clean_col1 = col1.strip().lower()
clean_col2 = col2.strip().lower()
clean_col3 = col3.strip().lower()

print(clean_col1)
print(clean_col2)
print(clean_col3)
print("\n")
print(clean_col1.endswith("_id"))
print(clean_col2.endswith("_id"))
print(clean_col3.endswith("_id"))

#ALL DONE ! Deliverable next