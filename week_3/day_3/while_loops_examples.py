'''data = ["5", "7", "done", "9"]
i = 0
total = 0
while i < len(data):
    if data[i] == "done":
        break              # sentinel detected → exit
    total = total + int(data[i])
    i = i + 1
print(total)  # 12 — "9" never reached
print(i)'''

'''names = ["alice", "bob", "STOP", "cora"]
i = 0
while i < len(names):
    if names[i] == "STOP":
        print("hit sentinel at index", i)  # hit sentinel at index 2
        break
    print(names[i])
    i = i + 1
print("loop ended")
# output: alice → bob → hit sentinel at index 2 → loop ended
print(i)'''

'''inputs = [ "10", "5", "done", "99"]
i = 0
total = 0

while i < len(inputs):
    if inputs[i] == "done":
        break
    total = total + int(inputs[i])
    i = i + 1

print(total)
'''

'''rows = ["alice", "", "bob", "   ", "cora"]

i= 0
clean = []

while i < len(rows):
    if rows[i].strip() == "":
       continue
       i = i + 1
    clean.append(rows[i].strip())
    i = i + 1
print(clean)'''

'''nums = [ 4, 8, 15, 16, 23, 42]

i = 0 
found = False

while i < len(nums):
    if nums[i] > 20:
        found = True
        break
    i = i + 1

if found:
    print("first >20 at index", i)
else:
    print("none found")'''

#retry loops
responses = ["fail", "fail", "fail", "fail", "fail", "success"]
max_attempts = 5
attempts = 0
i = 0

while True:
    
    if attempts > max_attempts:
        print("giving up after", max_attempts, "tries")
        break
    if responses[i] == "success":
        print("succes on attempt", attempts)
        break
    attempts = attempts + 1
    i = i + 1
