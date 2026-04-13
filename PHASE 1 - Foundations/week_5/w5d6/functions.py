# # #Decomposition
# # def parse_line(line):
# #     """Step 1: split and clean a raw line."""
# #     parts = line.split(",")
# #     return parts[0].strip(), float(parts[1].strip())

# # def is_valid_amount(amount):
# #     """Step 2: check if amount is within range."""
# #     return 0 < amount <= 10000

# # def process_lines(lines):
# #     """Main: orchestrate steps 1 and 2."""
# #     results = []
# #     for line in lines:
# #         name, amount = parse_line(line)
# #         if is_valid_amount(amount):
# #             results.append({"name": name, "amount": amount})
# #     return results

'''Tier 1 - Basics: def, parameters, return (W5D1 + W5D2)'''

#**Function 1: `clean_text`**
#Write a function that takes a string, strips whitespace, converts to lowercase, and returns the result.

def clean_text(text:str) -> str:
    text = text.strip().lower()
    return text

print(clean_text("  HeLLo  "))
print(clean_text("WORLD"))


#**Function 2: `compute_average`**
#Write a function that takes a list of numbers and returns the average. If the list is empty, return `0.0`.

def compute_average(numbers: list) -> float:
    total = 0.0
    average = 0.0
    for number in numbers:
        total += number
    try:
        average = total / len(numbers)
    except ZeroDivisionError:
        return 0.0
    return average
        
print(compute_average([10, 20, 30]))
print(compute_average([]))


#**Function 3: `extract_field`**
#Write a function that takes a comma-separated string and an index, and returns the field at that index, stripped of whitespace.

def extract_field(csv: str, i: int) -> str:
    parts = csv.split(",")
    return parts[i].strip()

print(extract_field("Alice, 25, Berlin", 0))
print(extract_field("Alice, 25, Berlin  ", 2))


'''### TIER 2 — Scope Awareness *(W5D3)*'''
#**Function 4: `count_matches`**
#Write a function that takes a list of strings and a target string, and returns how many items in the list match the target (case-insensitive).

def count_matches(words: list, word: str) -> int:
    count = 0

    for w in words:
        w = w.strip().lower()
        if word.lower() == w:    
            count += 1
    return count

print(count_matches(["Apple", "banana", "APPLE"], "apple"))
print(count_matches(["x", "y", "z"], "a"))


#**Function 5: `running_max`**
#Write a function that takes a list of numbers and returns a new list where each element is the maximum value seen so far.

def running_max(numbers: list) -> list:
    if len(numbers) == 0:
        return []
    new_list = []
    current_max = numbers[0]
    for number in numbers:
        if number > current_max:
            current_max = number
        new_list.append(current_max)
    return new_list

print(running_max([3, 1, 4, 1, 5]))
print(running_max([5, 4, 3]))


#**Function 6: `build_frequency_map`**
#Write a function that takes a list of strings and returns a dict mapping each string to its count.
def build_frequency_map(items: list) -> dict:
    new_dict = {}
    for item in items:
        new_dict[item] = new_dict.get(item, 0) + 1
    return new_dict

print(build_frequency_map(["a", "b", "a", "c", "a"]))
print(build_frequency_map([]))


'''### TIER 3 — Defaults + Keyword Arguments *(W5D4)*'''
#**Function 7: `format_greeting`**
#Write a function that takes a `name` and an optional `title` (default `""`) and returns a greeting string. If title is provided, include it before the name.
def format_greeting(name:str, title = "") -> str:
    if title:
        return "Hello, " + title + " " + name + "!"
    return "Hello, " + title + name + "!"

print(format_greeting("Alice"))
print(format_greeting("Alice", title="Dr."))


#**Function 8: `filter_by_range`**
#Write a function that takes a list of numbers, an optional `low` (default `0`), and an optional `high` (default `100`), and returns a list of numbers within that range (inclusive).

def filter_by_range(numbers:list, low=0, high=100) -> list:
    new_list = []
    for number in numbers:
        if number >= low and number <= high:
            new_list.append(number)
    return new_list

print(filter_by_range([5, 150, 50, -3, 80]))
print(filter_by_range([5, 150, 50, -3, 80], low=10, high=60))


#**Function 9: `summarize_list`**
#Write a function that takes a list of numbers and an optional `label` (default `"Summary"`), and returns a formatted string with the count, min, max, and average.

def summarize_list(numbers:list, label="Summary") -> str:
    if len(numbers) == 0:
        return "No data to summarize!"
    avg = compute_average(numbers)
    count = len(numbers)
    lowest = min(numbers)
    highest = max(numbers)
    return (f"{label}: count={count}, min={lowest}, max={highest}, avg={avg}")

print(summarize_list([10, 20, 30]))
print(summarize_list([5, 15], label="Temps"))


'''### TIER 4 — Predicate Functions + Type Hints *(W5D5)*'''

#**Function 10: `is_valid_email`**
#Write a predicate function that returns `True` if a string contains exactly one `@` and at least one `.` after the `@`.

def is_valid_email(email: str) -> bool:
    email = email.strip().lower()

    if email.count("@") != 1:
        return False
    position = email.find("@")
    if "." not in email[position:]:
        return False
    return True

print(is_valid_email("test@example.com"))
print(is_valid_email("testexample.com"))
print(is_valid_email("test@@x.com"))



#**Function 11: `is_complete_record`**
#Write a predicate function that takes a dict and a list of required keys, and returns `True` if all required keys exist in the dict.

def is_complete_record(record:dict, required:list)-> bool:
    for item in required:
        if item not in record:
            return False
    return True

print(is_complete_record({"name": "A", "age": 25}, ["name", "age"]))
print(is_complete_record({"name": "A"}, ["name", "age"]))


#**Function 12: `has_outliers`**
#Write a predicate function that takes a list of numbers and a threshold, and returns `True` if any number is greater than the threshold.
def has_outliers(numbers:list, threshold)->bool:
    for number in numbers:
        if number > threshold:
            return True
    return False

print(has_outliers([10, 20, 150], 100))
print(has_outliers([10, 20, 30], 100))


'''### TIER 5 — Decomposition + Helper Functions *(putting it all together)*'''

#**Function 13: `categorize_readings`**
#Write a function that takes a list of string readings and two floats (`low`, `high`),
#and returns a dict with three keys:
# -`"valid"` (list of floats in range),
# -`"out_of_range"` (list of floats outside range),
# -and `"unparseable"` (list of original strings that couldn’t convert to float).


def categorize_readings(texts:list, low:float, high:float)-> dict:
    valid = []
    out_of_range = []
    unparsable = []

    #Convert text to float
    for text in texts:
        try:
            number = float(text)
            if number > low and number < high:
                valid.append(number)
            else:
                out_of_range.append(number)
        except ValueError:
            unparsable.append(text)

    
    return {
        "valid": valid,
        "out_of_range": out_of_range,
        "unparsable": unparsable
    }

print(categorize_readings(["23.1", "ERR", "150.0", "N/A", "18.5"], -40.0, 60.0))
# #→ {"valid": [23.1, 18.5], "out_of_range": [150.0], "unparseable": ["ERR", "N/A"]}


#**Function 14: `group_by_key`**
#Write a function that takes a list of dicts and a key name, and returns a dict-of-lists grouped by that key’s value.

def group_by_key(records:list, name:str)-> dict:
    grouped = {}

    for record in records:
        grouped.setdefault(record[name], []).append(record)
    return grouped

records = [
    {"category": "food", "amount": 10},
    {"category": "transport", "amount": 5},
    {"category": "food", "amount": 8},
]
print(group_by_key(records, "category"))
#→ {"food": [{"category": "food", "amount": 10}, {"category": "food", "amount": 8}],
#   "transport": [{"category": "transport", "amount": 5}]}


#**Function 15: `generate_report`**
#Write a function that takes the output of `categorize_readings`
#(Function 13) and returns a formatted report string.
# Use `summarize_list` (Function 9) inside it for the valid readings stats.

def generate_report(to_format):
    count_valid = len(to_format["valid"])
    count_invalid = len(to_format["out_of_range"])
    not_parsable = len(to_format["unparsable"])

    return (f"=== DATA QUALITY REPORT ===\nValid readings:{count_valid}\nOut of range:{count_invalid}\nUnparseable:{not_parsable}\n{summarize_list(to_format["valid"], "Valid stats — Summary")}\n=== END REPORT ===")



data = categorize_readings(["23.1", "ERR", "150.0", "18.5"], -40.0, 60.0)
print(generate_report(data))