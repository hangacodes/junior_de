print("=== Guided Drills ===")
print("1:")
age = 16
is_adult = age >= 18
print(is_adult)
print("\n")

print("2:")
country = "USA"
is_two_chars = len(country) == 2
print(is_two_chars)
print("\n")

print("3:")
raw_count = "50"
print(raw_count == 50)
print(int(raw_count) == 50)
print("\n")

print("4:")
print(bool(""))
print(bool(" "))
print(bool("0"))
print(bool(0))

print("\n=== Semi-Guided Drills ===")

#Fill the ??? 
row = "li,28,FR"
parts = row.split(",")
name = parts[0]
age = int(parts[1])
country = parts[2]

# Create three validation flags
name_not_empty = name != ""           # True if name is not ""
age_nonnegative = age >= 0        # True if age >= 0
country_two_chars = len(country) == 2        # True if country length == 2

print(f"name_not_empty={name_not_empty}")
print(f"age_nonnegative={age_nonnegative}")
print(f"country_two_chars={country_two_chars}")