#Order calculator

item_name = input("Enter a name: ").strip()
unit_price = input("Enter a price: ")
quantity = input("Enter a quantity: ")
coupon_code = input("Enter coupon code: ").strip().lower()

if item_name == "":
    print("ERROR: item name cannot be empty.")
else:
    print(f"Item: {item_name}")


if unit_price == "":
    print("ERROR: price cannot be empty.")
else:
    try:
        price = float(unit_price)
        if price < 0:
            print("ERROR: price cannot be negative")
        else:
            print(f"Price: {price}")
    except ValueError:
        print("ERROR: price must be a number")

if quantity == "":
    print("ERROR: quantity cannot be empty.")
else:
    try:
        qty = int(quantity)
        if qty < 1:
            print("ERROR: you must enter a valid quantity")
        else:
            print(f"Quantity: {qty}")
    except ValueError:
        print("ERROR: quantity must be a whole number.")

if coupon_code == "":
    print("You don't have a discount")
else:
    if coupon_code == "save10":
        print(f"Discounted applied: 10% off")
    else:
        print("Code is not valid")