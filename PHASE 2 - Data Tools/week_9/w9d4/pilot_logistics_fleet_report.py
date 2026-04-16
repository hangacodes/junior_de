import pandas as pd

fleet = pd.DataFrame({
    "vehicle_id": ["V01", "V02", "V03", "V04", "V05", "V06", "V07", "V08", "V09", "V10"],
    "type": ["van", "truck", "car", "van", "truck", "car", "van", "car", "truck", "truck"],
    "mileage_km": [120000, 85000, 45000, 200000, 310000, 15000, 95000, 60000, 175000, 230000],
    "fuel_type": ["diesel", "diesel", "petrol", "petrol", "diesel", "electric", "electric", "petrol", "diesel", "diesel"],
    "needs_service": [True, False, False, True, True, False, True, False, True, True],
})

#Report A
filter_service = fleet.loc[fleet["needs_service"] == True].sort_values(by="mileage_km", ascending=False).reset_index(drop=True)
print("Vehicle needs service:\n",filter_service)

#Report B
filter_diesel = fleet.query("fuel_type == 'diesel' and mileage_km > 100000").sort_values(by="mileage_km", ascending=False).reset_index(drop=True)
print("High mileage diesels:\n", filter_diesel)

#Report C

def summary_by_type(df, vehicle_type):
    mask = df["type"] == vehicle_type
    filtered = df.loc[mask]
    count = filtered.shape[0]
    
    if count > 0:
        top_mileage = filtered.sort_values(by="mileage_km", ascending=False).iloc[0]
        print(f"\n---{vehicle_type} ({count} vehicles) ---")
        print(f"Highest mileage: {top_mileage['vehicle_id']} at {top_mileage['mileage_km']} km")
    else:
        print(f"\n---{vehicle_type}: no vehicles ---")


   

summary_by_type(fleet, "van")
summary_by_type(fleet, "truck")

mask = fleet["mileage_km"] >= 100000
print(mask.value_counts()) 
#-“If a filter condition is wrong (e.g., `>` instead of `>=`)
#what’s the easiest way to catch the mistake before sending the report?”

#Print the mask before filtering and check if the count looks right
'''
mask = df["mileage_km"] >= 100000
print(mask.value_counts()) 
'''


#**What Could Go Wrong:** What happens if you use `and` instead of `&` in a compound mask? What error message do you see?

#Value Error: The truth value of a Series is ambiguous