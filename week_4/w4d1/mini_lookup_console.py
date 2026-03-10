inventory = {"sku1": 9.99,
             "sku2": 12.99,
             "sku3": 26.23,
             "sku4": 505.0,
             "sku5": 11.11,
             "sku6": 69.00,
             "sku7": 2.80
}

while True:
    action = input("Enter an action ('lookup','set' or 'quit'): ")
    if action == "quit":
        break
    elif action == "lookup":
        lookup = input("Enter a SKU(e.g 'sku1'): ")
        print(inventory.get(lookup, "Unknown sku"))
    elif action == "set":
        set = input("Enter a SKU(e.g 'sku1'): ")
        set_price = input("Enter a price for your SKU: ")
        try:
            set_price = float(set_price)
            inventory[set] = set_price
        except ValueError:
            print("Price invalid, try again")
    else:
        print("This is an unknown action, please try again")