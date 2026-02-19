total_seconds = 367
minutes = total_seconds // 60
remaining_seconds = total_seconds % 60

print(minutes)
print(remaining_seconds)

print(f"Total seconds:{total_seconds}")
print(f"Time: {minutes} minutes and {remaining_seconds} seconds")


print("\nActivation drills")
print("Drill 1:")
a = 7
b = 5
print(a+b)
print(a*b)

print("\nDrill 2:")

x = 20
y = 6
print(x/y)
print(f"{x/y:.2f}")
print(x//y)
print(x%y)


print("\nDrill 3:")
print(8 + 2 * 5) #predicting 18

print("\nDrill 4:")
print((8 + 2) * 5) #predicting 50

print("\nSemi-guided drills")
print("Drill 1:")

bill = 42.50
tip_rate = 0.15

tip = bill * tip_rate
total = bill + tip

print(f"Bill: ${bill:.2f}")
print(f"Tip: ${tip:.2f}")
print(f"Total: ${total:.2f}")
#Add one more print line that shows a thank-you message on a new line using \n
print("\nThank you!")


print("\nDrill 2:")

items = 53
box_size = 6

full_boxes = items // box_size
leftover_items = items % box_size

print(f"Full boxes:{full_boxes}")
print(f"Leftover items:{leftover_items}")

#Add one final print line combining both results in a single sentence

print(f"There are {full_boxes} full boxes, with {leftover_items} leftover items.")

#I forgot about the guided practice with hints so here they are :

print("\nGuided practice ( with hints")

print("\nB1:")
#You have total_seconds = 367. Compute minutes (whole minutes) and seconds (remaining seconds). Hint: use // 60 and % 60.
total_seconds = 367
minutes = total_seconds // 60
remaining_seconds = total_seconds % 60

print("\nB2:")
#Using minutes and seconds from B1, print exactly: Time: Xm Ys. Hint: print(f"Time: {minutes}m {seconds}s")
print(f"Time: {minutes}m{remaining_seconds}s")

print("\nB3:")
#Someone wrote print(10 + 14 / 2) to compute the average of 10 and 14. Fix it to print 12.0. Hint: wrap the sum in parentheses.
print((10+14) / 2)

print("\nB4:")
#Set subtotal = 19.9 and tax_rate = 0.07. Compute tax = subtotal * tax_rate and print: Tax: €X.XX. Hint: use :.2f.

subtotal = 19.9
tax_rate = 0.07
tax = subtotal * tax_rate

print(f"Tax: ${tax:.2f}")

print("\nNote:\nThese are a little too easy especially after doing the activation, that's probably why I skipped them at first.\nI guess they are good to just get used to write code.")