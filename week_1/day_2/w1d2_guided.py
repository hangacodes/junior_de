'''
#Problem 1: Fix the variable name
#Goal: Create a variable for a city using snake_case. Hint: no spaces, use underscores. Style: home_city = "...".'''

city_name = "Moscow"
print(city_name)
print("\n")

''' **Problem 2: Make the types match the meaning**
Goal: Create `row_count` (int), `success_rate` (float), `file_name` (str), `has_header` (bool) and print each type. Hint: use `True`/`False` with capital first letter.'''

row_count = 2300
success_rate = 9.2
file_name = "Guided_drills"
has_header = False
print(type(row_count))
print(type(success_rate))
print(type(file_name))
print(type(has_header))
print("\n")

'''**Problem 3: Convert `"250"` into a number (int)**
Goal: Start with `raw = "250"`, create `converted = int(raw)`, print both types. Hint: keep the original variable, create a new one for the converted value.'''

raw = "250"
raw_int = (int(raw))
print(type(raw))
print(type(raw_int))
print("\n")

'''**Problem 4: Convert `"3.50"` into a number (float)**
Goal: Start with `raw_price = "3.50"`, convert to float, print the type. Hint: use `float(...)`.'''

raw_price = "3.50"
raw_price_float = float(raw_price)
print(type(raw_price))
print(type(raw_price_float))
print("\n")

'''**Problem 5: Convert 2026 into a string for display**
Goal: Start with `year = 2026`, make `year_text = str(year)`, print both types. Hint: if it prints `2026`, that does not prove it is an int — check `type()`.'''
year = 2026
year_text = str(year)
print(type(year))
print(type(year_text))
print("\n")

'''**Problem 6: Create a “data pipeline settings” block**
Goal: Create `source_system` (str), `batch_size` (int), `timeout_seconds` (float), `dry_run` (bool). Print each on its own line.'''

source_system = "junior_database"
batch_size = 33
timeout_seconds = 3.3
dry_run = True

print(source_system)
print(batch_size)
print(timeout_seconds)
print(dry_run)