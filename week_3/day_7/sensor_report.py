raw_readings = [
    "23.1", "ERR", "18.5", "", "45.2", "-3.0", "N/A",
    "72.8", "31.4", "bad", "0.0", "-41.5", "27.6", "",
    "15.9", "ERR", "38.7", "22.0", "55.1", "missing",
    "19.8", "-0.5", "ERR", "33.3", "61.2", "14.7",
    "29.0", "", "OFFLINE", "42.1"
] 
print("=== SENSOR DATA QUALITY REPORT ===")

parsed = []
unparseable = 0

for row in raw_readings:
    try:
        temp = float(row)
        parsed.append(temp)
    except ValueError:
        unparseable += 1

print("\n --- Input Summary ---")
print(f"Total readings received: {len(raw_readings)}")
print(f"Unparseable( non-numeric: {unparseable}")
print(f"Parseable readings: \t  {len(parsed)}")

range_low = -40.0
range_high = 60.0
out_of_range = []
clean = []

print("\n--- Range validation ---")
print(f"Valid range: {range_low} to {range_high}")
for temp in parsed:
    if temp < range_low:
        out_of_range.append(temp)
        print(f"\t-Too low: {temp}")
    elif temp > range_high:
        out_of_range.append(temp)
        print(f"\t-Too high: {temp}")
    else:
        clean.append(temp)

print(f"Out of range count:\t{len(out_of_range)}")
print(f"Clean readings:\t\t{len(clean)}")


if len(clean) > 0:
    highest_temp = clean[0]
    lowest_temp = clean[0]
    total = sum(clean)

    #Max
    for t in clean:
        if t > highest_temp:
            highest_temp = t
    #Min
    for t in clean:
        if t < lowest_temp:
            lowest_temp = t
    average = total / len(clean)
else:
    average = "N/A"
    total = 0
    highest_temp = "N/A"
    lowest_temp = "N/A"

print("\n--- Statitics (clean readings only) ---")
print(f"Lowest temp: {lowest_temp}")
print(f"Highest temp: {highest_temp}")
print(f"Total temp: {round(total, 2)}")
#Ternary expressions : Will be taught in week 4-5 maybe ?
#A one liner if/else built into an expressions
#value_if_true if condition else value_if_false
print(f"Average temp: {round(average, 2)if len(clean) > 0 else average}")

print("\n--- Quality Score ---")
clean_rate = (len(clean) / len(raw_readings)) * 100
print(f"Clean rate: {round(clean_rate, 2)}% ({len(clean)} of {len(raw_readings)})")
if clean_rate >= 80:
    print("Status: PASS")
else:
    print("Status NEEDS REVIEW ( below 80% threshold)")

print("=== END REPORT ===")