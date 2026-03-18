sales = {
    "monday": 1240.50,
    "tuesday": 890.00,
    "wednesday": 2105.75,
    "thursday": 1567.20,
    "friday": 3210.00,
}

# Print each day and its sales, formatted to 2 decimal places
# Expected output:
# monday → 1240.50
# tuesday → 890.00
# wednesday → 2105.75
# thursday → 1567.20
# friday → 3210.00 
for key in sales:
    print(f"{key} > {sales[key]:.2f}")