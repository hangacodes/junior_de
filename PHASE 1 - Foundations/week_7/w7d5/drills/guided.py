'''**B1: Round-trip test**
Create a Python dict with at least 4 keys (including an int, a bool, and a list).
Convert it to a JSON string with `json.dumps()`, then back to Python with `json.loads()`. Print both and confirm they match.
*Hint:* Use `indent=2` in `dumps()` for readable output. Check that the restored dict’s types match the original.'''
import json

workouts = {"name" : "Chest day",
            "hours": 2,
            "finished": False,
            "exercises": ["bench press", "seated flies", "pushups",  "incline bench"]
            }

json_string = json.dumps(workouts, indent=2)
print(json_string)
print(type(json_string))
print("\n")
back_to_python = json.loads(json_string)

print(repr(back_to_python))
print(type(back_to_python))
print(type(workouts))

'''**B2: Write and read a JSON file**
Write your dict from B1 to a file called `b2_output.json` using `json.dump()`. Then read it back with `json.load()` and print the result.
*Hint:* `json.dump(data, f, indent=2)` inside a `with open("b2_output.json", "w")` block. `json.load(f)` inside a `with open("b2_output.json", "r")` block.'''


with open("week_7/w7d5/drills/b2_output.json", "w") as f:
    json.dump(workouts, f, indent=2)

with open("week_7/w7d5/drills/b2_output.json", "r") as f:
    print(json.load(f))

'''
**B3: Navigate nested JSON**
Given this JSON string, extract and print the second employee’s name and their first skill:'''

json_text = '{"dept": "eng", "employees": [{"name": "Li", "skills": ["python"]}, {"name": "Sam", "skills": ["sql", "bash"]}]}'

data = json.loads(json_text)
print(data["employees"][1]["name"])
print(data["employees"][1]["skills"][0])

'''**B4: Loop nested data and accumulate**
Using the same data from B3, loop through all employees and build a flat list of ALL skills across all employees. Print the combined list.
*Hint:* Outer loop over `data["employees"]`, inner loop over `employee["skills"]`, append each skill to a flat list.'''

skills = []
for employee in data["employees"]:
    for i in employee["skills"]:
        skills.append(i)

print(skills)