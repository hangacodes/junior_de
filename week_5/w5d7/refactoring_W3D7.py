'''## 4 REFACTOR A — W3D7 Sensor Data Quality Reporter'''

'''Below is a version of the W3D7 sensor report script.
This is representative of the flat, top-to-bottom style you wrote in Week 3.
**If your actual script is different, use yours instead** — the refactoring process is the same.'''
# w3d7_sensor_report.py — ORIGINAL (flat version)

raw_readings = [
    "23.1", "ERR", "18.5", "", "45.2", "-3.0", "N/A",
    "72.8", "31.4", "bad", "0.0", "-41.5", "27.6", "",
    "15.9", "ERR", "38.7", "22.0", "55.1", "missing",
    "19.8", "-0.5", "ERR", "33.3", "61.2", "14.7",
    "29.0", "", "OFFLINE", "42.1"
]

# print("=== SENSOR DATA QUALITY REPORT ===")

# # --- Parsing ---
# parsed = []
# unparseable = 0

# for row in raw_readings:
#     try:
#         temp = float(row)
#         parsed.append(temp)
#     except ValueError:
#         unparseable += 1

# print(f"\n--- Input Summary ---")
# print(f"Total readings received:{len(raw_readings)}")
# print(f"Unparseable (non-numeric):{unparseable}")
# print(f"Parseable readings:{len(parsed)}")

# # --- Range validation ---
# range_low = -40.0
# range_high = 60.0
# out_of_range = []
# clean = []

# print(f"\n--- Range Validation ---")
# print(f"Valid range:{range_low} to{range_high}")
# for temp in parsed:
#     if temp < range_low:
#         out_of_range.append(temp)
#         print(f"\t- Too low:{temp}")
#     elif temp > range_high:
#         out_of_range.append(temp)
#         print(f"\t- Too high:{temp}")
#     else:
#         clean.append(temp)

# print(f"Out of range count:{len(out_of_range)}")
# print(f"Clean readings:{len(clean)}")

# # --- Statistics ---
# if len(clean) > 0:
#     highest_temp = clean[0]
#     lowest_temp = clean[0]
#     total = 0

#     for t in clean:
#         total += t
#         if t > highest_temp:
#             highest_temp = t
#         if t < lowest_temp:
#             lowest_temp = t

#     average = total / len(clean)

#     print(f"\n--- Statistics (clean readings only) ---")
#     print(f"Lowest temp:{lowest_temp}")
#     print(f"Highest temp:{highest_temp}")
#     print(f"Total:{round(total, 2)}")
#     print(f"Average temp:{round(average, 2)}")
# else:
#     print("\n--- Statistics ---")
#     print("No clean readings to analyze.")

# # --- Quality score ---
# clean_rate = (len(clean) / len(raw_readings)) * 100
# print(f"\n--- Quality Score ---")
# print(f"Clean rate:{round(clean_rate, 2)}% ({len(clean)} of{len(raw_readings)})")
# if clean_rate >= 80:
#     print("Status: PASS")
# else:
#     print("Status: NEEDS REVIEW (below 80% threshold)")

# print("\n=== END REPORT ===")


'''**Function 1: `parse_readings(raw: list) -> tuple`**
- Takes the raw list of strings
- Returns a tuple: `(parsed_list, unparseable_count)`
- Contains the `try/except` parsing loop'''

def parse_readings(raw: list) -> tuple:
    parsed = []
    unparseable = 0
    for row in raw:
        try:
            temp = float(row)
            parsed.append(temp)
        except ValueError:
            unparseable += 1

    return parsed, unparseable

'''**Function 2: `validate_range(parsed: list, low: float, high: float) -> tuple`**
- Takes the parsed float list and range boundaries
- Returns a tuple: `(clean_list, out_of_range_list)`
- Contains the range-checking loop'''

def validate_range(parsed: list, low=-40.0, high=60.0)-> tuple:
    
    out_of_range = []
    clean = []


    for temp in parsed:
        if temp < low:
            out_of_range.append(temp)
            print(f"\t- Too low:{temp}")
        elif temp > high:
            out_of_range.append(temp)
            print(f"\t- Too high:{temp}")
        else:
            clean.append(temp) 

    return clean, out_of_range


'''**Function 3: `compute_stats(clean: list) -> dict`**
- Takes the clean readings list
- Returns a dict with keys: `"count"`, `"min"`, `"max"`, `"total"`, `"average"`
- Returns `{"count": 0, "min": None, "max": None, "total": 0, "average": None}` for empty input
- Uses running min/max with a loop (same logic as original)'''



def compute_stats(clean: list) -> dict:
    if len(clean) == 0:
        return {"count": 0,
                "min": None, 
                "max": None,
                "total":0,
                "average": None
    }
    count = len(clean)
    highest_temp = clean[0]
    lowest_temp = clean[0]
    total = 0
    
    for temp in clean:
        total += temp
        if temp > highest_temp:
            highest_temp = temp
        if temp < lowest_temp:
            lowest_temp = temp
    average = total / len(clean)
    return {"count": count,
            "min": lowest_temp, 
            "max": highest_temp,
            "total": total,
            "average": average
    }


'''**Function 4: `compute_quality_score(clean_count: int, total_count: int) -> tuple`**
- Returns a tuple: `(rate_float, pass_or_fail_string)`
- E.g., `(56.67, "NEEDS REVIEW")`'''

def compute_quality_score(clean_count: int, total_count: int) -> tuple:
    status = None
    clean_rate = clean_count / total_count * 100
    if clean_rate >= 80:
        status = "PASS"
    else:
        status = "NEEDS REVIEW (below 80% threshold)"

    return clean_rate, status

'''**Function 6: `main() -> None`**
- Defines `raw_readings`
- Calls functions 1-5 in order
- Passes results from each step to the next'''

def main():
    raw_readings = [
    "23.1", "ERR", "18.5", "", "45.2", "-3.0", "N/A",
    "72.8", "31.4", "bad", "0.0", "-41.5", "27.6", "",
    "15.9", "ERR", "38.7", "22.0", "55.1", "missing",
    "19.8", "-0.5", "ERR", "33.3", "61.2", "14.7",
    "29.0", "", "OFFLINE", "42.1"
]

    parsed, unparseable = parse_readings(raw_readings)
    clean, out_of_range =validate_range(parsed)
    stats = compute_stats(clean)
    quality = compute_quality_score(len(clean), len(raw_readings)) 
    print_report(raw_readings, parsed, unparseable, clean, out_of_range, stats, quality)

'''**Function 5: `print_report(raw: list, parsed: list, unparseable: int, clean: list, out_of_range: list, stats: dict, quality: tuple) -> None`**
- This is the one function that prints. It produces the full report.
- Calls no other functions — it just formats and prints the data it receives.'''
def print_report(raw: list, parsed: list, unparseable: int, clean: list, out_of_range: list, stats: dict, quality: tuple) -> None:
    print("=== SENSOR DATA QUALITY REPORT ===")
    print("\n")
    print("--- Input Summary ---")
    print(f"Total readings received: {len(raw)}")
    print(f"Unparseable(non-numeric): {unparseable}")
    print(f"Parseable readings: {len(parsed)}")
    print("\n")
    print("--- Range Validation ---")
    print("Valid range: -40.0 to 60.0 ")
    for temp in out_of_range:
        if temp < -40.0:
            print(f"\t- Too low:{temp}")
        else:
            print(f"\t- Too high:{temp}")
    print(f"Out of range count: {len(out_of_range)}")
    print(f"Clean readings: {len(clean)}")
    print("--- Statistics (clean readings only) ---")
    print("\n")
    if stats["count"] > 0:
        print(f"\n--- Statistics (clean readings only) ---")
        print(f"Lowest temp:{stats["min"]}")
        print(f"Highest temp:{stats["max"]}")
        print(f"Total:{stats["total"]:.2f}")
        print(f"Average temp:{stats["average"]:.2f}")
    else:
        print("\n--- Statistics ---")
        print("No clean readings to analyze.")

    print("--- Quality Score ---")
    clean_rate, status = quality
    print(f"Clean rate: {clean_rate:.2f}% ({len(clean)} of{len(raw)})")
    print(f"Status: {status}")
    print("\n=== END REPORT ===")




if __name__ == "__main__":
    main()