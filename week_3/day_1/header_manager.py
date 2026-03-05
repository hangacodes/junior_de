user_csv_raw = input("Enter a CSV header row: ").strip().lower()
user_csv = user_csv_raw.replace(" ", "")
try:
    parts = user_csv.split(",")

    print(repr(parts))
    if user_csv == "":
        print("ERROR: CSV header row cannot be empty")

except ValueError:
    print("ERROR: please enter a valid CSV header row")


if "id" not in parts:
    parts.insert(0, "id")

if "email" not in parts:
    parts.append("email")

to_remove = input(f"Remove a column from: {parts} ")

if to_remove == "":
    print("Removing was skipped")
elif to_remove in parts:
    parts.remove(to_remove)
    print(f"Column '{to_remove}' was removed.")
else:
    print("Column not found. Nothing was removed")

print(f"Current list columns: {parts}")
remove_by_index = input("Enter a index number that you want to remove.")

if remove_by_index == "":
    print("Removal by index was skipped")
else:
    try:
        remove_by_index = int(remove_by_index)
        if remove_by_index >= len(parts):
            print(f"Please select a number up to: {len(parts)- 1} ")
        elif remove_by_index < 0:
            print("Index can't be negative")
        else:
            parts.pop(remove_by_index)
    except ValueError:
        print("Please enter a number.")

print(parts)
print(len(parts))