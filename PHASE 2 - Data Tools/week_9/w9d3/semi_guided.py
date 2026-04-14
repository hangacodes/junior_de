import pandas as pd

# Apartment listings in a city
listings = pd.DataFrame(
    {
        "address": ["Elm St 4", "Oak Ave 12", "Pine Rd 7", "Elm St 18", "Birch Ln 3", "Oak Ave 5"],
        "sqm": [55, 82, 45, 70, 95, 60],
        "rent_eur": [850, 1200, 700, 1050, 1400, 950],
        "available": [True, True, False, True, False, True],
    },
    index=["A01", "A02", "A03", "A04", "A05", "A06"],
)

#TODO 1: Select just the "rent_eur" column. Print it and confirm it's a Series.
print(listings["rent_eur"])
print(type(listings["rent_eur"]))

#TODO 2: Select listings A02 through A04 using .loc. Print the result.
#   Then select the same rows using .iloc (figure out the positions).
#   Print both and confirm they match.
first_selection = listings.loc["A02":"A04"]
pos_1st_selection = listings.iloc[1:4]
print(first_selection)
print(pos_1st_selection)

#TODO 3: Create a boolean mask for available apartments (available == True).
#   Use it to filter listings and select only address and rent_eur columns.
#   Print the result.
mask = listings["available"] == True
filter = listings.loc[mask, ["address", "rent_eur"]]
print(filter)

#TODO 4: The apartment at A03 just became available. Update its "available"
#   value to True using .loc (the safe pattern). Print the updated DataFrame.

listings.loc["A03", "available"] = True
print(listings)