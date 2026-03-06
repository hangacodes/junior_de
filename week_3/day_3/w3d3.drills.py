#What prints ? 
'''x = 5
while x > 2:
    print(x)
    x = x - 1'''

#spot the bug:
'''x = 3
while x > 0:
    print(x)        #missing x = x - 1
    x = x - 1'''

#**A3 — Trace:** Convert this `for` loop into a `while` loop that produces the same output:
'''total = 0
for n in range(1, 6):
    total = total + n
print(total)
'''
'''total = 0
n = [1, 2, 3, 4, 5]
banana = 0
while banana < len(n):
    total = total + n[banana]
    banana = banana + 1

print(total)
'''
'''number = input("Guess the number: ")


try:
   
    while True:
        number = input("Guess the number: ")
        number = int(number)
    
        if 1<= number <= 10:
            print("Thanks!")
            break
except ValueError:
    print("You must enter a valid number(whole)")'''

'''items = ["A", "B", "C", "STOP", "D", "E"]
i = 0
count = 0
while i < len(items):
    if items[i] == "STOP":
        break
    i = i + 1
    count = count + 1
print(count)
'''

'''names = ["  alice", "", "BOB  ", "   ", "cora"]

clean_names = []
i = 0

while i < len(names):
    name = names[i].strip()
    if name == "":
        i = i + 1
        continue
    clean_names.append(name)
    i = i + 1

print(clean_names)
print(i)'''

#semi-guided

'''readings = [3, 0, 5, 2, -1, 99]
i = 0 
total = 0

while readings[i] >= 0:
    
   
    total = total + readings[i]
    i = i + 1
print(total)'''

'''ages = [12, 15, 17, 19, 16]
i = 0
answer = -1

while i < len(ages):
    if ages[i] >= 18:
        answer = i
        break
    i = i + 1
print(answer)  # expected: 3'''