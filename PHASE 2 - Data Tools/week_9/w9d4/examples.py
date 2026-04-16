import pandas as pd

'''Combining conditions : AND vs OR'''


packages = pd.DataFrame({
    "carrier": ["DHL", "UPS", "DHL", "FedEx", "UPS", "FanCurier"],
    "weight_kg": [2.5, 120.0, 0.8, 5.0, 18.0, 69.23],
    "express": [True, False, False, True, False, True]

})

#AND: heave DHL packages:
heavy_dhl = packages.loc[(packages["carrier"] == 'DHL') & (packages["weight_kg"] > 2.0)]

print("Heavy DHL:\n", heavy_dhl)

#OR: express OR over 10kg

urgent = packages.loc[(packages["weight_kg"] > 10.0) | (packages["express"] == True)]

print("Urgent:\n", urgent)


'''.query() vs boolean indexing: same result, different syntax'''

second_df = pd.DataFrame({
    "city": ["Helsinki", "Espoo", "Tampere", "Helsinki"],
    "temp_c": [2.5, -1.0, -5.2, 3.1],
    "wind_km": [18, 25, 12, 30]
})

#Boolean indexing
result1 = second_df.loc[(second_df["city"]== "Helsinki") & (second_df["wind_km"]> 20)]

print("Boolean indexing:\n", result1)

#.query() - same filter, more readable:
result2 = second_df.query("city == 'Helsinki' and wind_km > 20")
print("\nquery:\n", result2)


'''Sorting by one column and by multiple columns'''

scores = pd.DataFrame({
    "student": ["Michael", "John", "Collin", "Maria"],
    "subject": ["math", "science", "math", "science"],
    "score": [79, 49, 80, 97]
    
})

#Single column descending:
print("By score ( highest first):")
print(scores.sort_values(by="score", ascending=False))

#Multi-column: subject first, then score within each subject
print("By subject, then score:")
print(scores.sort_values(by=["subject", "score"], ascending=[True, False]))


'''Filter + sort + reset: the full pipeline'''

df = pd.DataFrame({
    "product": ["bolt", "nut", "washer", "screw", "bolt"],
    "warehouse": ["WH-N", "WH-S", "WH-N", "WH-E", "WH-S"],
    "qty":[500, 1200, 800, 350, 150]
})

def low_stock_report(df, threshold):
    '''Filter to items below threshold, sort ascending, reset index.'''

    mask = df["qty"] < threshold
    result= (
        df.loc[mask].sort_values(by="qty").reset_index(drop=True)
    )

    print(f"Items below {threshold} units:")
    print(result)
    return result


low_stock_report(df, 500)
low_stock_report(df, 1000)

'''This is the most common real-world pattern: filter → sort → reset → use.
Wrapping it in a function makes it reusable — the same function works for any threshold.'''