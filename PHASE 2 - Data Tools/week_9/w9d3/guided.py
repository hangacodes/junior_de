import pandas as pd

flights = pd.DataFrame(
    {
        "origin": ["HEL", "HEL", "TMP", "OUL", "TMP"],
        "dest": ["ARN", "CPH", "HEL", "HEL", "ARN"],
        "passengers": [180, 145, 72, 95, 68],
        "on_time": [True, False, True, True, False],
    },
    index=[1001, 1002, 1003, 1004, 1005],
)

# '''**B1 — Column selection + type check**
# Select the `passengers` column. Print it and its type. Then select `origin` and `dest` together as a DataFrame. Print and confirm the type.
# - Hint: single column → `df["col"]`, multiple → `df[["c1", "c2"]]`.'''

# print(flights["passengers"])
# print(type(flights["passengers"]))

# selection = flights[["origin", "dest"]]
# print("\nSelection:")
# print(selection)
# print(type(selection))


# '''**B2 — .loc label slice**
# Select flights 1002 through 1004 using `.loc`. Print the result and count the rows.
# - Hint: `.loc[1002:1004]` — remember label slices include both ends.'''


# selection1 = flights.loc["1002":"1004"]
# print(selection1)
# print(selection1.shape[0])


# '''**B3 — .iloc position slice**
# Select the middle three flights using `.iloc` (positions 1, 2, 3). Print and compare to B2.
# - Hint: `.iloc[1:4]` — stop is exclusive.'''

# selected = flights.iloc[1:4]
# print(selected)

# '''**B4 — Boolean mask filter + column select**
# Create a mask for delayed flights (`on_time == False`). Use it to select only the `origin`, `dest`, and `passengers` columns for delayed flights.
# - Hint: `mask = flights["on_time"] == False`, then `flights.loc[mask, ["origin", "dest", "passengers"]]`.'''

# delayed_flights = flights["on_time"] == False

# delayed = flights.loc[delayed_flights, ["origin", "dest", "passengers"]]
# print(delayed)

