#Drills :
#Activation
'''#A1 — Predict: What does this print if user types 5?
x = input("Number: ")
print(x * 3)
print("\n")
#Will print 555'''

'''#**A2 — Predict:** What happens if user types `hello`?
n = int(input("Number: "))
print(n + 10)
print("\n")
#This is gonna be ValueError'''

'''#**A3 — Spot the issue:** Why might this print “Equal” unexpectedly?
age = input("Age: ")
if age == 18:
    print("Equal")

#There is no way this prints equal, even if the user inputs 18, the 18 will be a string'''

#Guided Drills :

'''**B1 — Safe age with validation**

Prompt for age. Handle empty input, conversion failure, and negative ages. On success, print next year’s age.'''
#Hints: .strip(), check == "", try/except ValueError, if age < 0

'''age = input("Age: ").strip()


if age == "":
    print("Error: age cannot be empty")
else:
    try:
        if int(age) < 0:
            print("Error: age cannot be negative")
        else:
            print(f"Next year's age: {int(age) + 1}")
    except ValueError:
        print("Error: enter a whole number, not a text")'''

'''**B2 — Price with tax**

Prompt for price (float). Reject empty, non-numeric, and negative values. On success, print price x 1.19.'''

'''
price = input("Enter price: ").strip()

if price == "":
    print("Error: price cannot be empty")
else:
    try:
        price = float(price)
        if price < 0:
            print("Error: price cannot be negative")
        else:
            print(f"Price with tax: {price * 1.19}")
    except ValueError:
        print("Error: price must be a number")'''


'''**B3 — Yes/No validator**

Ask “Continue? (yes/no)”. Normalize with `.strip().lower()`. Accept only exact `"yes"` or `"no"`, print error otherwise.'''

'''answer = input("Continue? (yes/no): ").strip().lower()

if answer == "yes":
    print("You chose yes")
elif answer == "no":
    print("You chose no")
else:
    print("Error: please type exactly yes or no")    '''

'''**B4 — Quantity must be positive**

Prompt for quantity (int). Must be >= 1. Print “OK” or specific error message.'''

'''quantity = input("Enter a quantity:")

if quantity == "":
    print("ERROR: quantity cannot be empty")
else:
    try:
        quantity = int(quantity)
        if quantity < 1:
            print("ERROR: quantity cannot be less than 1")
        else: 
            print("OK")
    except ValueError:
        print("ERROR: quantity must be a number")'''

#Semi-Guided Drills
#**C1 — Safe integer with empty check**
'''raw = input("Enter a whole number: ").strip()

#TODO: if raw is empty, print error
#TODO: else try to convert with int()
#   - if conversion works, print the number × 5
#   - if conversion fails (except ValueError), print helpful message

if raw == "":
    print("ERROR: raw cannot be empty.")
else:
    try:
        raw = int(raw)
        print(f"Your number x 5 = {raw * 5}")
    except ValueError:
        print("ERROR: you must type a number")'''

#**C2 — Temperature converter (C → F)**
'''c_text = input("Celsius: ").strip()

#TODO: handle empty input
#TODO: try float conversion
#TODO: reject values below -273.15 (absolute zero)
#TODO: else convert to Fahrenheit and print
# Formula: F = C * 9/5 + 32

if c_text == "":
    print("ERROR: field cannot be empty")
else:
    try:
        temp = float(c_text)
        if temp < -273.15:
            print("ERROR: temperature out of range")
        else:
            f = temp * 9/5 + 32
            print(f"Fahrenheit: {f}")
    except ValueError:
        print("ERROR: you must type a number")'''

#**C3 — Username rules (no spaces allowed)**
username = input("Username: ").strip()

#TODO: if empty -> error
#TODO: elif username contains a space -> error
#       Hint: username.find(" ") != -1
#TODO: else -> print "Username accepted"
                  
if username == "":
    print("ERROR: enter a username")
else:
    if username.find(" ") != -1:
        print("ERROR: username cannot have whitespaces")
    else:
        print("Username accepted")