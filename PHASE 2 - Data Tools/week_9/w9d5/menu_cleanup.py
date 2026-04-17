import pandas as pd

df = pd.DataFrame({
    "Item Name" : ["Scallops" , "Ahi Poke", "FILLET", "brOwnie", "the Usual Pizza", "Ahi Tacos"],
    "Category": ["Main", "appeTIzer", "main", "dessert", "MAIN", "   appetizer"],
    "Raw Cost": ["$19.80", "$10.80", "$15.30", "$3.20", "$5.00", "$6.50"],
    "Serving Size": ["0" , "200", "180", "100", "330", "200"],
    "Allergens": ["shellfish", "fish, soy", "none", "dairy, gluten", "gluten, dairy", "fish"]
})

df = df.rename(columns={"Item Name": "item_name", "Category":"category","Raw Cost":"raw_cost", "Serving Size":"serving_size","Allergens":"allergens"})
df["item_name"] = df["item_name"].str.strip().str.lower()
df["category"] = df["category"].str.strip().str.lower()
df["raw_cost"] = df["raw_cost"].str.replace("$", "").astype(float)
df["serving_size"] = df["serving_size"].astype(int)
df["cost_per_serving"] = df["raw_cost"] / df["serving_size"]
df["menu_price"] = df["cost_per_serving"] * 3.0
df["menu_price"] = round(df["menu_price"], 2)
df = df.drop(columns=["raw_cost"])
df = df.sort_values(by=["menu_price"], ascending=False)
print(df)
print(df.columns.to_list())


# If serving_size was "0", cost_per_serving would be inf (infinity).
# Catch it: print(menu["cost_per_serving"].max()) — if inf, check for zeros. - if any value is inf , it will always win .max()
# What Could Go Wrong: astype(float) on "$9.50" → ValueError. Clean $ first.