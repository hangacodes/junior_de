import pandas as pd


sensors = pd.DataFrame({
    "sensor_id": ["S1", "S2", "S3", "S4", "S5"],
    "location": ["roof", "basement", "roof", "lobby", "roof"],
    "temp_c": [22.5, 18.0, 25.1, 19.8, 21.0],
    "active": [True, False, True, True, True],
})

'''**A1 — Predict:**
What does `(sensors["location"] == "roof") & (sensors["temp_c"] > 22)` produce?
List the True/False values for each row.'''

#S1 - True
#S2 - False
#S3 - True
#S4 - False
#S5 - False
new = sensors.loc[(sensors["location"] == "roof") & (sensors["temp_c"] > 22)]
print(new)


'''**A2 — Spot:**
A developer writes `sensors[sensors["location"] == "roof" and sensors["active"] == True]`.
What error do they get, and what's the fix?'''

#ValueError - The truth value of a Series is ambiguous 
#The fix: 

a2= sensors.loc[(sensors["location"]=="roof") & (sensors["active"] == True)]
print(a2)


'''**A3 — Predict:**
After `sensors.sort_values(by="temp_c", ascending=False)`, which sensor_id is in the first row?'''

#S3

print(sensors.sort_values(by="temp_c", ascending=False))


'''**A4 — Predict:**
After filtering to `location == "roof"` (3 rows), what does the index look like before and after `reset_index(drop=True)`?'''

#before : 0, 2, 4
#after: 0 , 1 ,2...

filt = sensors.loc[sensors["location"] == "roof"].reset_index(drop=True)
print(filt)