total_seconds = 367
minutes = total_seconds // 60
remaining_seconds = total_seconds % 60

print(minutes)
print(remaining_seconds)

print(f"Total seconds:{total_seconds}")
print(f"Time: {minutes} minutes and {remaining_seconds} seconds")
print("\n")

print("Activation drills")
print("Drill 1:")
a = 7
b = 5
print(a+b)
print(a*b)

print("\n")
print("Drill 2:")

x = 20
y = 6
print(x/y)
print(f"{x/y:.2f}")
print(x//y)
print(x%y)

print("\n")
print("Drill 3:")
print(8 + 2 * 5) #predicting 18

print("\n")
print("Drill 4:")
print((8 + 2) * 5) #predicting 50

print("\n")
print("Semi-guided drills")
print("Drill 1:")

bill = 42.50
tip_rate = 0.15

tip = bill * tip_rate
total = bill + tip

print(f"Bill: ${bill:.2f}")
print(f"Tip: ${tip:.2f}")
print(f"Total: ${total:.2f}")

print("\n")
print("Drill 2:")

items = 53
box_size = 6

full_boxes = items // box_size
leftover_items = items % box_size

print(f"Full boxes:{full_boxes}")
print(f"Leftover items:{leftover_items}")

#Add one final print line combining both results in a single sentence

print(f"There are {full_boxes} full boxes, with {leftover_items} leftover items.")
