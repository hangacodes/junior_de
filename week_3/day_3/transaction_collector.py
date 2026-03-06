count_valid = 0
total_amount = 0
count_invalid = 0
count_negative = 0
attempts = 0
while True: 
    amount = input("Enter amount (or 'done'): ").strip().lower()
    attempts += 1
    if attempts > 100:
        print("Stopped after 100 attempts")
        break

    if amount == "done":
        print("You are done")
        break
    
    if amount == "":
        count_invalid += 1
        continue

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid number. Please try again")
        count_invalid += 1
        continue
        
    if amount < 0:
        print("Negative ignored")
        count_negative += 1
        continue
    total_amount = total_amount + amount
    count_valid += 1


try: 
    average = total_amount / count_valid
except ZeroDivisionError:
    average = 0


print("===SUMMARY===\n")
print(f"Accepted count: {count_valid}")
print(f"Total sum: {total_amount}")
print(f"Average: {average}")
print(f"Invalid count: {count_invalid}")
print(f"Negative count: {count_negative}")