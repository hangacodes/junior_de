readings = [10, 200, 30, -5, 0, 55, 101, 99]

clean_readings = []
count_invalid = 0




for number in readings:
    if number >= 1 and number <= 100:
        clean_readings.append(number)
    else:
        count_invalid += 1

print(f"Clean readings: {clean_readings}")
print(f"Valid count: {len(clean_readings)}")
print(f"Invalid count: {count_invalid}")
       
if len(clean_readings) == 0:
    print("No valid readings - skipping total/sum/min/sorted")
else:
    print(f"Total: {sum(clean_readings)}")
    print(f"Highest number: {max(clean_readings)}")
    print(f"Lowest number: {min(clean_readings)}")
    print(f"Sorted readings: {sorted(clean_readings)}")


print("===Summary===")
lst = [0, "Berlin"]

idx, city = lst
print("Index:" ,idx)
print(f"Index: {idx}")
print(f"City: {city}")

print(f"CleanReadings: {clean_readings}")
print("===SUMMARY===")
print(f"Today is : {clean_readings}")
print(f"Tomorrow is tomorrow: {[3,4,8]}")
print("I HAVE NO IDEEA: {what the fuck am i doing here}")