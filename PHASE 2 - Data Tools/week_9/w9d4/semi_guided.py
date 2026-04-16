import pandas as pd

# Apartment rental listings
listings = pd.DataFrame({
    "address": ["Elm St 4", "Oak Ave 12", "Pine Rd 7", "Elm St 18", "Birch Ln 3", "Oak Ave 5"],
    "district": ["central", "suburbs", "central", "central", "suburbs", "suburbs"],
    "rent_eur": [1200, 850, 1500, 1050, 700, 950],
    "sqm": [55, 82, 45, 70, 95, 60],
    "available": [True, True, False, True, True, True],
})

#TODO 1: Filter to available apartments in the central district.
central_available = listings.loc[(listings["district"] == "central") & (listings["available"] == True)]
print(central_available)

#TODO 2: Sort the filtered results by rent_eur ascending (cheapest first).
#   Reset the index.
cheapest_central = central_available.sort_values(by="rent_eur").reset_index(drop=True)
print(cheapest_central)

#TODO 3: Write a function affordable_central(df, max_rent) that:
#   - filters to available + central + rent_eur <= max_rent
#   - sorts by rent ascending
#   - resets the index
#   - returns the result

#   Call it with max_rent=1200 and print the result.
def affordable_central(df, max_rent):
    affordable = df.loc[(df["available"]== True) & (df["district"]== "central") & (df["rent_eur"] <= max_rent)]
    affordable = affordable.sort_values(by="rent_eur").reset_index(drop=True)

    return affordable

#TODO 4: Rewrite the filter fromTODO 1 using .query().
filter_query = listings.query("district == 'central' and available == True")
print(filter_query)


affordable = affordable_central(listings, 1100)
print(affordable)