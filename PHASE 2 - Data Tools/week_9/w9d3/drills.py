import pandas as pd

products = pd.DataFrame(
    {
        "name": ["laptop", "mouse", "keyboard", "monitor"],
        "price": [999, 25, 75, 350],
        "in_stock": [True, True, False, True],
    },
    index=["P1", "P2", "P3", "P4"],
)

'''**A1 — Predict:** What does `products["price"]` return — a Series or a DataFrame? What does `products[["name", "price"]]` return?'''

# A series
print(type(products["price"]))


'''**A2 — Predict:** What does `products.loc["P2":"P3"]` print? How many rows? (Remember: `.loc` slicing is end-inclusive.)'''

# 2 rows
print(products.loc["P2":"P3"])

'''**A3 — Trace:** After `mask = products["price"] > 100`, what are the True/False values for each index label?'''

#P1 - True, P2- False , P3- False and P4 - True

mask = products["price"] > 100
print(mask)

'''**A4 — Spot:** A developer writes `products[mask]["in_stock"] = False` to mark expensive items as out of stock. What’s wrong with this pattern, and what’s the fix?'''

#Gives a ChainingAssignmentError
# fix : products[mask, "in_stock"] = False

products.loc[mask, "in_stock"] = False

print(products)

