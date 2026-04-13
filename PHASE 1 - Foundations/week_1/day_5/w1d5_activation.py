'''Write your prediction as a comment BEFORE running.
**1 - print("  PyThOn  ".strip().lower())
What prints? 

**2 — s = "a-b-c"
print(s.replace("-", "_"))
print(s)
What prints on each line? Does `s` change?

**3 — raw = "   REPORT_2026.CSV   "
clean = raw.strip().lower()
result = clean.endswith(".csv")
What is the value of `result` after execution?

**4 — s = "hello world"
s.upper()
print(s)
The output is `hello world`, not `HELLO WORLD`. What went wrong?

**5 — s = "data_pipeline"
print(s.find("pipe"))
print(s.find("xyz"))
What two values print?'''

print("  PyThOn  ".strip().lower())     #"python"

s = "a-b-c"
print(s.replace("-", "_"))          #"a_b_c"
print(s)                            #"a-b-c"

raw = "   REPORT_2026.CSV   "
clean = raw.strip().lower()
result = clean.endswith(".csv")     #bool : True
print(type(result))
print(result)

s = "hello world"
s.upper()
print(s)        #The output is still "hello world" because we didn't assign s.upper() to any new variable
s_upper = s.upper()
print(s_upper)

s = "data_pipeline"
print(s.find("pipe"))       #this should print a int - something like 5
print(s.find("xyz"))        #this will print -1

print("All done! Moving to drills.py now")