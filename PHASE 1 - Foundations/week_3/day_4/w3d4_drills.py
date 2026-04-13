'''scores = [ -10, -20, -5, -15,3]
current_max = scores[0]
for s in scores:
    if s > current_max:
        current_max = s

print("max:", current_max)

temps = [ 23, 26, 99, 105,]
current_min = temps[0]
for temp in temps:
    if temp < current_min:
        current_min = temp
print("min:", current_min)

'''


'''ages = [ 12, 16, 26, 30 , -1, 0, 62, 23, 18,-23, 1, -26]

valid = []
rejected = 0
for age in ages:
    if age > 0:
        valid.append(age)
    else:
        rejected += 1
print(valid)
print(rejected)
'''

'''names = ["ALICE", "Bob", "cHarLiE"]
cleaned = []
for name in names:
    cleaned.append(name.lower().title())

print(cleaned)
print(names)'''

'''colors = ["red", "blue", "green", "black", "grey", "turquose"]
sizes = ["XS", "S", "M", "L", "XL"]
combos = []

for c in colors:
    for s in sizes:
        combos.append(c + "-" + s)

print(combos)
print(len(combos))'''

'''n = 4
# Single loop: O(n) — 4 steps
single_ops = 0

for i in range(n):
    single_ops = single_ops + 1

    
    # Nested loop: O(n²) — 16 steps
nested_ops = 0
for i in range(n):
    for j in range(n):
        nested_ops = nested_ops + 1

print(single_ops)
print(nested_ops)'''

#Drill ladder
#6A) Activation

'''#A1 - Predict : What does total equal?
nums = [4, 4, 4]
total = 0
for n in nums:
    total = total + n
print(total)        #12 checked

#**A2 — Trace:** What list does `kept` become?
kept = []
for n in [5, 10, 15]:
    if n >= 10:
        kept.append(n)
print(kept)         # [ 10, 15] correct'''

#**A3 — Spot:** What is wrong with this running minimum?
'''nums = [-3, -7, -1]
current_min = nums[0]
for n in nums:
    if n < current_min:
        current_min = n
print(current_min)      #It doesn't start with the first number, it starts with a int so i need to put current_min = nums[0]
#CORRECT!'''
'''### 6B) Guided Practice

**B1) Accumulator + count:** Compute the average of `[3, 6, 9, 12]` using `total` and `count`. Print the average.

*Hint:* Two variables, both start at `0`. Average = `total / count`.'''


'''nums = [3, 6, 9, 12]
count = 0
total = 0


for n in nums:
    count += 1
    total += n
print(count)
print(total)

average = total / count
print(average)'''


'''**B2) Filtering + rejects:** From `raw = [100, -1, 50, 0, 75]`, build `clean` keeping only `> 0`, and count `rejected`.

*Hint:* Use `else:` to increment `rejected`.'''

'''raw = [100, -1, 50, 0, 75]
clean =[]
rejected = 0

for number in raw:
    if number > 0:
        clean.append(number)
    else:
        rejected += 1

print(clean)
print(rejected)
'''
'''**B3) Running max on negatives:** Find the largest value in `scores = [-10, -20, -5, -15]` using a loop.

*Hint:* Start with `current_max = scores[0]`.'''

'''scores = [-10, -20, -5, -15]

current_max = scores[0]

for score in scores:
    if score > current_max:
        current_max = score
print(current_max)'''

'''**B4) Nested loop (duplicate check):** Given `nums = [1, 2, 2, 3]`, count how many index pairs `(i, j)` with `i < j` have equal values.

*Hint:* Use `range(len(nums))` for `i`, `range(i + 1, len(nums))` for `j`.'''

'''nums = [1, 2, 2, 3, 69, 70 , 10, 23, 69]

matches = 0

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            matches += 1

print(matches)''' #I DID NOT UNDERSTAND THIS YET WTF


#Semi-Guided drills
'''raw = ["100", "20", "oops", "", "003", "7", "-5"]

clean = []
rejected = 0


for item in raw:
    if item.isdigit():
        item = int(item)
        clean.append(item)
    else:
        rejected += 1



print(clean)     # expected: [100, 20, 3, 7]
print(rejected)  # expected: 3'''