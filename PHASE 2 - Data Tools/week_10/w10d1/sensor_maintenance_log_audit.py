import pandas as pd

sensor_log = pd.DataFrame({
    "timestamp": [1, 2, 3, 4, 5, 6, 7, 8],
    "sensor_id": ["S01", "S01", None, "S02", "S02", "S03", "S03", None],
    "location": ["Floor1", None, "Floor2", "Floor2", None, None, "Floor3", "Floor3"],
    "reading": [22.1, None, 21.8, None, None, 19.5, None, 20.0],
    "priority": ["high", None, "low", None, "high", None, None, "low"]
})
print("Null rates before:")
for col in sensor_log.columns:
    missing = sum(sensor_log[col].isna())
    rate = missing / len(sensor_log)
    print(f"{col}:{missing} missing ({rate * 100:.1f}%)")
print(f"Rows before: {len(sensor_log)}")
df = sensor_log[sensor_log["sensor_id"].notna()]
df["location"] = df["location"].fillna("UNASSIGNED")
df = df.sort_values(by="timestamp")
df["reading"] = df["reading"].ffill()
df["priority"] = df["priority"].fillna("normal")
print(df)

print("Null rates after:")
for col in df.columns:
    missing = sum(df[col].isna())
    rate = missing / len(df)
    print(f"{col}:{missing} missing ({rate * 100:.1f}%)")
print(f"Rows after: {len(df)}")

#Note:
#I dropped missing sensor_id rows because if there is no sensor_id than nothing else makes sense to have.
#We ffilled instead of adding the constant 0 because if a sensor failed for a moment, the temperature probably didn't drop to 0 , but it was somewhere around the one before
#I filled priority with normal because it makes sense - if is not high priority than the other option is normal
#We sort before we ffill because we want the readings to be in a good order before we fill it with the next temperature

#**What Could Go Wrong:**
# If sensor readings jump from 22°C to 5°C between consecutive rows, does forward-fill still make sense? When would you choose `fillna()` with a constant instead of `ffill()`?
'''Forward-fill stops making sense.
If the data is genuinely volatile — temperatures swinging wildly between timestamps — then the previous reading is a bad assumption for the missing one.
You'd be filling with a value that has nothing to do with reality.'''