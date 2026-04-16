import pandas as pd

inventory = pd.DataFrame({
    "item": ["bolt", "nut", "washer", "screw", "rivet", "pin"],
    "category": ["fastener", "fastener", "fastener", "fastener", "fastener", "connector"],
    "qty": [500, 1200, 80, 350, 45, 900],
    "price": [2.50, 0.80, 0.35, 1.10, 3.20, 0.60],
})


'''**B1 — AND filter**
Keep only fasteners with qty below 100. Print the result.
- Hint: `(inventory["category"] == "fastener") & (inventory["qty"] < 100)`'''

filter_and = inventory.loc[(inventory["category"] == "fastener") & (inventory["qty"] < 100)]
print(filter_and)


'''**B2 — OR filter**
Keep items that are either connectors OR priced above 2.00. Print the result.
- Hint: `(inventory["category"] == "connector") | (inventory["price"] > 2.00)`'''

filter_or = inventory.loc[(inventory["category"] == "connector") | (inventory["price"] > 2.0)]
print(filter_or)

'''**B3 — .query() rewrite**
Rewrite B1 using `.query()`. Verify the results match.
- Hint: `inventory.query("category == 'fastener' and qty < 100")`'''

filter_query = inventory.query("category == 'connector' or price > 2.0 ")
print("Query:\n", filter_query)


'''**B4 — Sort + reset**
Sort the full inventory by price descending, then reset the index. Print the sorted DataFrame.
- Hint: `.sort_values(by="price", ascending=False).reset_index(drop=True)`'''

sorted_df = inventory.sort_values(by="price", ascending=False).reset_index(drop=True)
print("Sorted:\n",sorted_df)