#Danger zone drills ( Predict before running )
# These are not easy. Each one contains a trap or a subtle interaction between concepts. Write your prediction as a comment, then run and compare.


#**DR-01 — The invisible type difference**


a = "100"
b = 100
print(a + a)
print(b + b)

#❓ What does each line print? Are they the same?
# first line should print an error - got this wrong - it concatenates them
#second line prints 200

# **DR-02 — Three assignment questions**
x = 5
x = x + 3
x = x * 2
print(x)

#❓ What prints? - it prints 16 - because x was assigned everytime with the new value.

#**DR-03 — Precedence ambush**
print(100 - 20 / 4)
print((100 - 20) / 4)
print(100 - 20 // 4)
#❓ What does each line print? Write all three answers before running.
'''
1st: 95 
2nd : 20
3rd : 95
i guess i got 2 wrong , cause those return floats. 
'''

#**DR-04 — Division types**
print(type(10 / 2))
print(type(10 // 2))
print(10 / 2 == 10 // 2)
#❓ What does each line print? Is the last line `True` or `False`? Why?

#1st : float
#2nd : int
#3rd : false ? Because one is int one is float? 
#It was true...cause it's still the same number. 

#DR-05 — The f-string you forgot to mark
name = "Ada"
score = 98.5
print("Name:{name}, Score:{score:.1f}")
#❓ What actually prints? What did the writer forget?
#He forgot to put f in front of the quotes so it printed "Name:{name}, Score:{score:.1f}" instead of Name : Ada, Score: 98.5

#**DR-06 — Slicing: the boundary game**
s = "data_engineer"
print(s[0:4])
print(s[5:13])
print(s[5:])
print(s[-8:])
print(s[::3])

#❓ Write all 5 outputs before running.
#1: data
#2: engineer
#3: engineer
#4: engineer
#5: teie - got this one wrong ofc. starts with the first letter then it jumps 3 each time. I jumped instantly

#**DR-07 — `len()` vs last index**
#word = "pipeline"
#print(word[len(word)])
#❓ What happens? Write the exact error type. - i have no ideea why this IndexError happened 
#Appearantly IndexError: string index out of range. len("pipeline") is 8; last valid index is 7. word[8] crashes.
'''BOOOOM huge confusion for a second'''

#**DR-08 — The silent slicing forgiveness**
s = "cat"
print(s[0:1000])
print(s[500:600])
print(len(s[500:600]))
#❓ What does each line print? Does any line crash?
#I AM SUPPER CONFUSED AGAIN LOL 
'''cat        ← truncated silently to end of string
           ← empty string (prints blank line)
0          ← len of empty string
Damn this is how advanced i have to think ? I feel lost hahahah'''


#**DR-09 — Immutability trap**
filename = "sales-2026.csv"
filename.replace("-", "_")
print(filename)
#❓ What prints? Is it `sales_2026.csv` or `sales-2026.csv`? Why? 
#It prints "sales-2026.csv" because we never assigned the new filename to any variable

#**DR-10 — The `.find()` index trap**
s = "pipeline_data"
pos = s.find("xyz")
print(s[pos])
#❓ Does this crash? If not, what does it print — and why is that dangerous?
#HOW AM I SUPPOSED TO KNOW ALL THESE ? LMAO 😰
'''**DR-10:**
Does NOT crash. `.find("xyz")` returns `-1`. `s[-1]` is the last character, `"a"` (from `"pipeline_data"`). 
**This is dangerous** 
— you silently get the last character of the string instead of an error, making the bug invisible.

So I was normally supposed to know this?? When did I miss this ?
WOW...just wow : ChatGPT: The trap in one sentence

.find() uses -1 to mean “not found”, but indexing with -1 means “last character” — so the two meanings collide.'''

#**DR-11 — Chaining into a non-string**
s = "raw_events_2026"
result = s.lower().replace("_", "-").count("-")
print(result)
print(type(result))
#❓ What type is `result`? Can you call `.upper()` on it? Why or why not?

#result should be str no ?
#Well nope...cause it ends with .count("-") and that returns an int haha
#You cannot call .upper() on a int type. WOW again

#**DR-12 — Split on missing delimiter**
row = "Alice|Berlin|DE"
parts = row.split(",")
print(len(parts))
print(parts[0])
#print(parts[1])
#❓ What prints for `len(parts)` and `parts[0]`? What does `parts[1]` do?

#Len parts prints 14? - nope nope nope
#parts[0] prints A - nope for this one either
#parts[1] prints l ? - nope for this one ...i'm so bad at this

#**DR-13 — The join type check**
name = "Bob"
age = 29
country = "US"
line = ",".join([name, str(age), country])
print(line)
#❓ Does this crash? If yes, name the error type and fix it in one line.
#This is probably crashing because we are trying to join a int ( age ) instead of a str(age)
#Error name idk...
#Ok so I was right that it crashed withouit str(age) - TypeError i guess i need to remember this

#**DR-14 — Double split + cast**
raw = "qty=  42 "
value_text = raw.split("=")[1].strip()
value = int(value_text)
print(value + 8)
#❓ What prints? Trace through each step before running.
#It should print 50 -> split raw and get 2 parts, qty and 42 , then you choose 42 with [1] and strip it -> then you transformit it from str to int and add 8
#Well at least i got this one right 

#**DR-15 — `round()` vs `:.2f`**
total = 19.997
rounded = round(total, 2)
print(rounded)
print(type(rounded))
print(f"{total:.2f}")
print(type(f"{total:.2f}"))
#❓ What does each line print? What types do you get?
#1st: 20
#2nd: int
#3rd : 20.00
#4th float