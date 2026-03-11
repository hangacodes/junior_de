sales = {"apples": 4, "bread": 2, "apples": 7}
total = 0
for item, qty in sales.items():
    if qty > 3:
        total += qty
print(total)

