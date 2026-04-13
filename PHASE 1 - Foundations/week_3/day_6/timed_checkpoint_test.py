#Set a timer. Close your notes. Write answers on paper or in a fresh `.py` file.
#**T1 (2 min):** 
# Create a list of 5 city names.
# Append a 6th. Remove the 3rd by index.
# Print the result.

# cities = ["New York", "San Francisco", "Berlin", "Oradea", "Budapest"]

# cities.append("Paris")
# cities.pop(3)
# print(cities)
# #1:30

#**T2 (3 min):**
# Write a `for` loop that computes the product (multiplication) of all numbers 
# in  `[2, 3, 4, 5]`.
# Print the result. (Hint: start the accumulator at `1`, not `0`.)
# total = 1
# for n in range(2,6):
#     total *= n
# print(total)

#1:30




#**T3 (3 min):**
# Write a `while` loop that collects input words until the user types `"done"`.
# Store words in a list. Print the list after the loop.

# words = []

# while True:
#     w = input("Enter a word(type: 'done' when you are done): ")

#     if w == "done":
#         break
#     words.append(w)

# print(words)




#**T4 (4 min):**
# Given `values = [15, -3, 22, 8, -7, 31, 4]`, find the running minimum and print it.

# values = [15, -3, 22, 8, -7, 31, 4]

# lowest_n = values[0]

# for n in values:
#     if n < lowest_n:
#         lowest_n = n
# print(lowest_n)



#**T5 (4 min):** Convert this loop into a comprehension:
# raw = ["  alpha ", " BETA", "gamma  "]
# clean = []
# for s in raw:
#     clean.append(s.strip().lower())

# clean_comprehention = [s.strip().lower() for s in raw]
# print(clean_comprehention)
# print(clean)


#**T6 (6 min):** Given `entries = ["alice:85", "bob:forty", "cara:92", "dan:"]`:
# -build two parallel lists: `valid_names` and `valid_scores` (integers).
#  A row is valid if the part after `:` passes `.isdigit()`.
#- Print both lists.

# entries = ["alice:85", "bob:forty", "cara:92", "dan:"]
# valid_names = []
# valid_scores = []

# for e in entries:
#     parts = e.split(":")
#     name = parts[0]
#     valid_names.append(name)

#     if parts[1].isdigit():
#         valid_scores.append(parts[1])

# print(valid_names)
# print(valid_scores)

#**T7 (8 min):** Given `readings = [23, 0, 45, -1, 67, 0, 89, -5, 12]`:
# - Build `positives` using a comprehension (keep only values > 0).
# - Compute the average of `positives` using `sum()` and `len()`.
# - Find the max using a `for` loop (NOT `max()` built-in—practice the pattern).
# - Print: the positives list, the average, and the max.

# readings = [23, 0, 45, -1, 67, 0, 89, -5, 12]

# positives = [n for n in readings if n > 0]
# average = sum(positives) / len(positives)

# highest_n = readings[0]

# for n in readings:
#     if n > highest_n:
#         highest_n = n


# print(positives)
# print(average)
# print(highest_n)

#Time left : 9m 40s !
#Finished in 20 min LFG !