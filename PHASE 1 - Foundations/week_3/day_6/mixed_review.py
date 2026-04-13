# items = ["a", "b", "c"]
# items.append("d")
# items.pop(1)
# print(items)

# #this should print -> a b c d -minus b ->  so acd'''

# total = 0
# for n in [3, 1, 4]:
#     total = total + n
# print(total)        # 8

# i = 5
# while i > 2:
#     i = i - 1
# print(i)        # my answer 3 -> correct answer 2

# nums = [10, 20, 30, 40]
# big = [n for n in nums if n > 15]
# print(big)      #20,30,40


# words = ["hi", "", "bye", ""]
# count = 0
# for w in words:
#     if w == "":
#         continue
#     count = count + 1
# print(count)        #my answer : 4 -> correct answer :2 '''

# data = [4, -1, 7, 2]
# current_max = data[0]
# for n in data:
#     if n > current_max:
#         current_max = n
# print(current_max)      #7'''




'''### 3A — Lists & Mutation (D1 Review)

**A1:** Start with `colors = ["red", "green", "blue"]`. 
Write code that: (a) appends `"yellow"`,
(b) inserts `"orange"` at index 1,
(c) removes `"green"`,
(d) pops the last item into a variable called `last`.
Print the final list and `last`.'''

# colors = ["red", "green", "blue"]
# colors.append("yellow")
# colors.insert(1, "orange")
# colors.remove("green")
# last = colors.pop()

# print(colors)
# print(last)


'''
WRONG
--------
**A2:** Given `cols = ["id", "name", "email", "name"]`,
remove **all** occurrences of `"name"` using a `while` loop and the `in` operator.
Print the result.'''
# cols = ["id", "name", "email", "name"]
# while "name" in cols:
#     cols.remove("name")

# print(cols)

'''**A3:** Build a list called `evens` by starting with an empty list and appending every even number from 2 to 10 (inclusive).
Use a `for` loop with `range()`. Print `evens`.'''

# even = []

# for n in range(2, 11):
#     if n % 2 == 0:
#         even.append(n)

# print(even)

'''#I got 2/ 3 correctly - exercise A2 i didn't know'''


'''### 3B — For Loops & Accumulators (D2 Review)

**B1:** Given `prices = [12.50, 8.99, 15.00, 3.49]`, compute the total using an accumulator. Print the total rounded to 2 decimal places using `round()`.'''

# prices = [12.50, 8.99, 15.00, 3.49]

# total = 0

# for p in prices:
#     total += p
# print(round(total,2)) # i had to look at how to round again..but everything else i did good

'''
WRONG
-------
**B2:** Given `names = ["ada", "LINUS", "Grace"]`,
print each name in title case (first letter upper, rest lower) on its own line.
Use `.lower()` and string slicing `name[0].upper() + name[1:]` pattern.'''

# names = ["ada", "LINUS", "Grace"]

# for n in names:
#     fixed = n[0].upper() + n[1:].lower()
#     print(fixed)        # i looked into the answer key for this one...
  
'''**B3:** Using `enumerate()`, print each item from `steps = ["extract", "transform", "load"]` in the format `"Step 1: extract"` (starting from 1, not 0).

*Hint:* `enumerate(steps, 1)` starts counting at 1—OR use `enumerate(steps)` and add 1 in the f-string.'''

# steps = ["extract", "transform", "load"]

# for idx, step in enumerate(steps, 1):
#     print(f"Step {idx}: {step}")


'''**B4:** Count how many strings in `data = ["ok", "", "ok", "", "", "ok"]` are empty. Print the count.'''

# data = ["ok", "", "ok", "", "", "ok"]

# count = 0 

# for d in data:
#     if d == "":
#         count += 1

# print(count)

'''
WRONG- VERY
**C2:** Given `items = ["log", "skip", "log", "STOP", "log"]`,
write a `while` loop that prints each item. When it hits `"STOP"`,
print `"Stopped early"` and `break`. Do NOT print `"STOP"` itself.'''

# items = ["log", "skip", "log", "STOP", "log"]
 
# i = 0

# while i < len(items):
#     if items[i] == "STOP":
#         print("STOPPED EARLY")
#         break
#     print(items[i])
#     i = i + 1

'''**C3:** Given `values = ["3", "bad", "7", "", "2"]`, write a `while` loop that scans by index.
For each value: if it’s empty, `continue`.
Try converting to `int`—if it fails (`try/except ValueError`),
print `"skipped: <value>"` and `continue`.
Otherwise, add it to a running total.
Print the total at the end.'''

# values = ["3", "bad", "7", "", "2"]
# total = 0
# i = 0

# while i < len(values):
#     if values[i] == "":
#         i += 1
#         continue

#     try:
#         total += int(values[i])
#         i += 1
#     except ValueError:
#         print(f"skipping: {values[i]}")
#         i += 1
# print(total)
# print(i)


'''**C4:** Write a `while True` loop that asks for input with 
`input("Enter a number (q to quit): ")`. If the user types `"q"`, break.
Otherwise, convert to `int` (skip with `continue` on `ValueError`)
and add to a running total. Print the total after the loop.'''
# total = 0
# while True:
#     number_txt = input("Enter a number(or q to quit):")

#     if number_txt == "q":
#         break
#     else:
#         try:
#             number = int(number_txt)
#             total = total + number
#         except ValueError:
#             print("Enter a valid number or q to quit")
#             continue
# print(total)

'''### 3D — List Patterns (D4 Review)

**D1:** Given `temps = [22, 18, 31, 27, 14, 29]`, find the running minimum using the proper initialization (`data[0]`). Print it.'''

# temps = [22, 18, 31, 27, 14, 29]

# lowest_temp = temps[0]

# for temp in temps:
#     if temp < lowest_temp:
#         lowest_temp = temp
# print(lowest_temp)
'''
**D2:** Given `rows = ["alice,28", "bob,thirty", "cara,35", "dan,"]`,
filter into a list called `valid_rows`
containing only rows where the part after the comma is all digits.
Use `.split(",")` and `.isdigit()`.

*Hint:* Split each row, check if `parts[1].isdigit()`.'''

# rows = ["alice,28", "bob,thirty", "cara,35", "dan,"]

# valid_rows = []
# invalid_rows = []
# for row in rows:
#     parts = row.split(",")
#     if parts[1].isdigit():
#         valid_rows.append(row)
#     else:
#         invalid_rows.append(row)
# print(valid_rows)
# print(invalid_rows)

'''**D3:** Given `words = ["Data", "engineer", "Python"]`,
produce a new list where every word is lowercased.
Use the mapping pattern (for loop + append).
Then write the same thing as a list comprehension.
Print both to confirm they match.'''

# words = ["Data", "engineer", "Python"]
# lower_list = []

# for word in words:
#     lower_list.append(word.lower())

# lower_comprehention = [word.lower() for word in words]
# print(lower_comprehention)
# print(lower_list)


'''**D4:** Given `sizes = ["S", "M", "L"]` and `colors = ["red", "blue"]`, use a nested loop to produce all combinations as `"red-S"`, `"red-M"`, etc. Print the result list.'''

# sizes = ["S", "M", "L"]
# colors = ["red", "blue"]
# pairs = []
# for color in colors:
#     for size in sizes:
#         pairs.append(color + "-" + size)

# print(pairs)
'''**E1:** Convert this loop to a comprehension:

```python
nums = [1, 2, 3, 4, 5]
doubled = []
for n in nums:
    doubled.append(n * 2)
```'''
# nums = [1, 2, 3, 4, 5]
# doubled = [n * 2 for n in nums]
# print(doubled)

'''**E2:** Write a comprehension that keeps only strings longer than 3 characters from `words = ["hi", "data", "go", "pipeline", "etl"]`.'''

# words = ["hi", "data", "go", "pipeline", "etl"]

# long_words = [w for w in words if len(w) > 3]
# print(long_words)

'''**E3:** Write a comprehension that strips whitespace AND converts to lowercase from `raw = ["  HELLO ", " World  ", "  python"]`. Expected: `["hello", "world", "python"]`.'''

# raw = ["  HELLO ", " World  ", "  python"]

# clean = [w.strip().lower() for w in raw]
# print(clean)

'''**E4:** Given `nums = [0, 5, -3, 8, -1, 12]`, write one comprehension that keeps only positive numbers and squares them. Expected: `[25, 64, 144]`.'''

# nums = [0, 5, -3, 8, -1, 12]

# positive_squares = [n ** 2 for n in nums if n > 0 ]
# print(positive_squares)
'''**E5:** Explain (don’t code) why this is bad practice:

```python
result = [print(x) for x in range(5)]
```'''

#Is bad practice because result will contain a bunch of None's , values that are uselss, a side effect of print
'''**F1:** Given `raw_scores = ["85", "bad", "92", "N/A", "78", "101", ""]`:
- Use a `for` loop to build `valid_scores` (only values where `.isdigit()` is `True`, converted to `int`).
- Then use a comprehension to filter `valid_scores` into `passing` (scores >= 80).
- Print both lists and the count of passing scores.'''

# raw_scores = ["85", "bad", "92", "N/A", "78", "101", ""]

# count = 0
# valid_scores = []

# for score in raw_scores:
#     if score.isdigit():
#             score = int(score)
#             valid_scores.append(score)
#             count += 1

# passing = [score for score in valid_scores if score >= 80]
# print(valid_scores)
# print(passing)
# print(count)
# print(len(passing))

'''**F2:** Given `log = ["INFO:start", "WARN:low memory", "INFO:processing", "ERROR:crash", "INFO:done"]`:
- Use a comprehension to extract only the messages (after `:`) from entries that start with `"ERROR"`.
- Expected: `["crash"]`.'''

# log = ["INFO:start", "WARN:low memory", "INFO:processing", "ERROR:crash", "INFO:done"]

# is_error = [l.split(":")[1] for l in log if l.startswith("ERROR")]

# print(is_error)

'''**F3:** Given `data = [10, 0, 25, 0, 15, 30, 0]`:
- Count the zeros using a `for` loop with a counter.
- Find the maximum of the non-zero values using a `for` loop with proper running-max initialization.
- Compute the sum of non-zero values using an accumulator.
- Print all three results.'''

# data = [10, 0, 25, 0, 15, 30, 0]

# zero_count = 0
# higest_nr = data[0]
# total = 0

# for n in data:
#     if n == 0:
#         zero_count += 1
#     if n > higest_nr:
#         higest_nr = n    
#     if n > 0:
#         total += n

# print(zero_count)
# print(higest_nr)
# print(total)

'''**F4:** Build a list of the first 20 numbers in the “FizzBuzz” sequence:
for each number 1–20, if divisible by both 3 and 5 store `"FizzBuzz"`,
if divisible by 3 store `"Fizz"`,
if divisible by 5 store `"Buzz"`,
otherwise store the number as a string.
Use a `for` loop (comprehension would be messy here).
Print the result.'''
# result = []

# for n in range(1,21):
#     if n % 3 == 0 and n % 5 == 0:
#         result.append("FizzBuzz")
        
#     elif n % 3 == 0:
#         result.append("Fizz")
        
#     elif n % 5 == 0:
#         result.append("Buzz")
       
#     else:
#         result.append(str(n))
# print(result)

# === DEBUGGING ===
'''nums = [4, 8, 2, 6]
total = 0
for n in nums:
    total += n
print(total)'''
#There was a missing = 

'''names = ["ada", "bob", "cara"]
upper = [n.upper() for n in names]      
print(upper)        
'''
#there was a missing () after .upper

'''data = [1, 2, 3, 4, 5]
i = 0
while i < len(data):
    print(data[i])
    i = i + 1'''
#There was an extra = : while i <= len(data) was wrong'

# items = ["keep", "drop", "keep", "drop"]
# new_list = []
# for item in items:
#     if item == "keep":
#         new_list.append(item)
# print(new_list)
