# '''### Example 1 — ⭐⭐ Counter pattern with `.get()`'''

# # **What it demonstrates:** counter pattern, `.get()` with default


# words = ["data", "pipe", "data", "job", "data", "pipe"]
# counts = {}

# for w in words:
#     counts[w] = counts.get(w, 0) + 1

# print(counts)
# #❓ PREDICT: What will the count be for "data"?


# '''### Example 2 — ⭐⭐⭐ Frequency table → text histogram'''
# #**What it demonstrates:** counter pattern output displayed 
# # as a visual bar chart using string repetition

# grades = ["A", "B", "A", "C", "B", "A", "B", "C", "A"]
# freq = {}

# for g in grades:
#     freq[g] = freq.get(g, 0) + 1

# for grade, count in freq.items():
#     bar = "*" * count
#     print(grade + ": " + bar + " (" + str(count) + ")")
# #❓ PREDICT: Which letter gets the longest bar?
# print(freq)

# '''### Example 3 — ⭐⭐⭐ Grouping + summing with `.setdefault()`'''
# #**What it demonstrates:** grouping pattern producing a dict-of-lists,
# # then summarizing each group

# rows = ["sales,Ava", "sales,Ben", "it,Amy", "sales,Noah", "it,Zoe"]
# groups = {}

# for row in rows:
#     dept, name = row.split(",")
#     groups.setdefault(dept, []).append(name)

# for dept, members in groups.items():
#     print(dept, "->", len(members), "people:", members)
#     #❓ **PREDICT:** How many names end up under `"sales"`?


# '''### Example 4 — ⭐⭐⭐⭐ Combined: count + group + lookup in one pass'''
# #**What it demonstrates:** Running multiple dict patterns simultaneously in a single loop
# events = ["u1,login", "u2,login", "u1,click", "u1,logout", "u2,click"]
# severity = {"login": 1, "click": 2, "logout": 1}  # lookup table

# action_counts = {}
# by_user = {}

# for e in events:        #looping over events

#     user, action = e.split(",")     #user and action are split into 2 parts
#     action_counts[action] = action_counts.get(action, 0) + 1    # count
#     #creates a new key and gives it the default 0 then counts + 1 every time that action it's met
#     by_user.setdefault(user, []).append(action)                  # group
#     #creates a dictionary with the user as a key , then appends the actions that correspond to that user
# print("action_counts:", action_counts)
# print("by_user:", by_user)

# for action, count in action_counts.items(): #creates separate items

#     sev = severity.get(action, 0)    # lookup
#     #creates sev variable -> points to an int value, corresponding to each actions from the "severity" dict
#     print(action, "-> count:", count, "severity:", sev)
#     #❓ **PREDICT:** Which action has the highest count? What severity does `"click"` get?

# '''WHAT DOES THIS PRINT?'''

# data = ["x", "y", "x", "x", "z", "y"]
# c = {}
# for d in data:
#     c[d] = c.get(d, 0) + 1
# print(c["x"], c["z"])       
# #-> I think it prints {"x":3, "y":2, "z":1} my bad.... it didn't print all of them just x and z 

# '''**A2 — Trace:** After this code runs, what is `totals["food"]`?''' # -> 18
# rows = ["food,10", "books,7", "food,5", "food,3"]
# totals = {}
# for row in rows:
#     cat, amt = row.split(",")
#     totals[cat] = totals.get(cat, 0) + float(amt)      
# print(totals["food"])

# '''**A3 — Spot:** This code should group words by first letter,
# but only the last word per letter survives. What line is wrong and why?'''

# words = ["apple", "ant", "bat", "ape"]
# groups = {}
# for w in words:
    
#    #groups[w[0]] = w # this line is wrong, it should be :
#    groups.setdefault(w[0], []).append(w)

# print(groups)
# '''**A4 — Predict:** What does this print?'''
# codes = {"A": "Active", "I": "Inactive"}
# tags = ["A", "X", "I", "A"]
# for t in tags:
#     print(codes.get(t, "UNKNOWN"))

# '''**A5 — Trace:** After this runs, what is `len(g["sales"])`?'''
# lines = ["sales,Ava", "it,Bo", "sales,Cy", "sales,Di"]
# g = {}
# for line in lines:
#     dept, name = line.split(",")
#     g.setdefault(dept, []).append(name)  #2 - missed ava lol i dind't see it...but i knew what it wants from me

# print(len(g["sales"]))


# '''**B1 — Word frequency from a sentence** (`freq_counter.py`)
# Given `text = "data jobs need data skills and data tools"`,
# build `freq` mapping each word to its count. Then print the word with the highest count.
# **Hint 1:** `words = text.split()` then counter pattern.
# **Hint 2:** To find the max, loop `freq.items()` and track the highest count with an accumulator
# (W3D4 running-max pattern).'''

# text = "data jobs need data skills and data tools"
# freq = {}

# words = text.split(" ")

# for word in words:
#     freq[word] = freq.get(word, 0) + 1
# print(freq)

# max_words = 0
# freq_word = None
# for k, v in freq.items():
#     if v > max_words:
#         max_words = v
#         freq_word = k
# print(max_words)
# print(freq_word)

# print(f"Highest count: {max_words} of the word: {freq_word}")


# '''**B2 — Category totals (summing pattern)** (`category_totals.py`)
# Given `rows = ["food,10.0", "books,7.5", "food,2.5", "tools,3.0", "books,12.0"]`, build `totals`
# mapping each category to its total spend. Print each category and its total.
# **Hint:** Same shape as counter pattern, but add `float(amt)` instead of `+ 1`.'''

# rows = ["food,10.0", "books,7.5", "food,2.5", "tools,3.0", "books,12.0"]

# totals = {}
# for row in rows:
#     category, price = row.split(",")
   
#     totals[category ]= totals.get(category, 0) + float(price)
# print(totals)

'''**B3 — Group names by first letter + count** (`letter_groups.py`)
Given `names = ["Ava", "Amy", "Ben", "Bao", "Zoe", "Ali"]`,
build `groups` mapping each first letter to a list of names. Then print each letter, its names, and how many.
**Hint:** `.setdefault(letter, []).append(name)` then loop `.items()` with `len()`.'''

# names = ["Ava", "Amy", "Ben", "Bao", "Zoe", "Ali"]

# groups = {}

# for name in names:
#     letter = name[0]
#     groups.setdefault(letter, []).append(name)
# for letter, name in groups.items():
#     print(f"Letter: {letter}: {len(name)} times : {name}")

'''**B4 — Translate airport codes with a lookup table** (`airport_lookup.py`)
Given `airports = {"HEL": "Helsinki", "ARN": "Stockholm", "OSL": "Oslo"}`
and `route = ["HEL", "OSL", "CPH", "ARN", "JFK"]`,
print each code and city. Use `"UNKNOWN"` for missing codes. Count how many codes were unknown.
**Hint:** `.get(code, "UNKNOWN")` for translation; compare the result to `"UNKNOWN"` to count misses.'''

# airports = {"HEL": "Helsinki", "ARN": "Stockholm", "OSL": "Oslo"}
# route = ["HEL", "OSL", "CPH", "ARN", "JFK"]
# count = 0
# for code in route:
#     city = airports.get(code, "UNKNOWN")
#     print(code, "->", city)

    
#     if city == "UNKNOWN":
#         count += 1

# print(count)



rows = ["Helsinki,34", "Espoo,29", "Helsinki,40", "Espoo,31", "Vantaa,22"]
by_city = {}
city_counts = {}

for  row in rows:
    parts = row.split(",")
    city, age_txt = parts   
    age = int(age_txt)
    by_city.setdefault(city, []).append(age)
    city_counts[city] = city_counts.get(city, 0) + 1

for city, ages in by_city.items():
    average = sum(ages) / city_counts[city]
    print(f"{city}: {ages} with an average of: {average}")

#TODO: For each row:
#   1. Split into city and age, convert age to int
#   2. Append age into by_city[city] (use .setdefault)
#   3. Count how many people per city in city_counts (counter pattern)

#TODO: Print each city, its ages, and the average age
# (average = sum of ages / count — use sum() from W3D4 on each list)

print(by_city)
print(city_counts)


# Expected output shape: `by_city = {"Helsinki": [34, 40], ...}` and average ages printed per city.'''