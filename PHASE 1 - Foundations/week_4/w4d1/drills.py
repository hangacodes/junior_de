'''Create `zones = {"FI": "Nordics", "DE": "EU", "US": "International"}`.
Set `country_code = "FI"` and print the zone. Then set `country_code = "FR"` and print a friendly “missing” message instead of crashing.
*Hint:* Use `if country_code in zones:` before `zones[country_code]`.'''
# zones = {"FI": "Nordics", "DE": "EU", "US": "International"}
# country_code = "FI"
# print(zones[country_code])

# country_code = "FR"
# if country_code in zones:
#     print(zones[country_code])
# else:
#     print(f"Country code missing: {country_code} not found")


'''**B2) Counter warm-up (single key update)**

Start with `counts = {"click": 0}`. Update `"click"` three times (simulating 3 clicks) and print the final dict.

*Hint:* `counts["click"] = counts["click"] + 1` each time.'''

counts = {"click": 0}

# counts["click"] += 1
# counts["click"] += 1
# counts["click"] += 1
# for clicks in range(3):
#     counts["click"] += 1
# print(counts)

'''**B3) Safe lookup with default**

Given `errors = {400: "Bad Request", 404: "Not Found"}`, print the message for status code `500` using a default of `"Unknown"`.'''

# errors = {400: "Bad Request", 404: "Not Found"}

# print(errors.get(500, "Unknown"))

'''### 6C) Semi-Guided

**C1) Build a dict from two lists**'''


# names = ["Ana", "Bo", "Cy"]
# scores = [10, 7, 12]

# result = {}
#TODO: loop with range(len(names)) to build name → score mapping
# for n in range(len(names)):
#     result[names[n]] = scores[n]
# print(result)  # expected: {'Ana': 10, 'Bo': 7, 'Cy': 12}


#C2) NORMALIZE A CATEGORY CODE
category_map = {"A": "Apparel", "B": "Books", "C": "Computers"}

code = "B"
full = category_map.get(code, "Unknown Category")

print(full)  # expected: Books
