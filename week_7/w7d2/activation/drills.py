'''**Drill 1 (Predict):** A file contains `"A\nB\nC\n"`. What does `repr(f.read())` show?

Write your answer before running.'''
#'A\nB\nC\n'

with open ("week_7/w7d2/activation/drill1", "w", encoding="utf-8") as f:
    f.write("A\nB\nC\n")

with open ("week_7/w7d2/activation/drill1", "r", encoding="utf-8") as f:
    print(repr(f.read()))

'''**Drill 2 (Predict):** True or False: `f.readlines()` returns a string.'''
#false - returns a list of strings

'''**Drill 3 (Predict):** You call `f.readline()` once, then start `for line in f:`. How many iterations does the loop run if the file has 5 lines total?'''
#Runs 4 iterations - the first line doesn't count anymore because the cursor moved before the loop started.

'''**Drill 4 (Spot):** This code is supposed to count lines equal to `"ERROR"`, but it always prints 0. Why?'''
with open("week_7/w7d2/activation/test.txt", "w", encoding="utf-8") as f:
    f.write("ERROR\nINFO\nERROR\n")

count = 0
with open("week_7/w7d2/activation/test.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line == "ERROR":
            count += 1
print(count)        #because we never stripped the line