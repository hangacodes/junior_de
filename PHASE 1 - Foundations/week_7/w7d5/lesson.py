import json

# # This is a JSON string (text, not a Python dict yet)
# json_text = '{"name": "Ana", "age": 29, "active": true, "city": null}'

# # Parse it into a Python dict
# data = json.loads(json_text)
# print(data)
# print(type(data))
# print(data["name"])
# # output: {'name': 'Ana', 'age': 29, 'active': True, 'city': None}
# # output: <class 'dict'>
# # output: Ana

# '''json.load() and json.dump()'''
# # Python dict → JSON string
# employee = {"name": "Bo", "age": 31, "remote": True}
# json_text = json.dumps(employee)
# print(json_text)                    # output: {"name": "Bo", "age": 31, "remote": true}
# print(type(employee))               # output: <class 'dict'> ← before converting with dumps()
# print(type(json_text))              # output: <class 'str'>  ← it's a string now

# # JSON string → Python dict
# restored = json.loads(json_text)
# print(restored)                     # output: {'name': 'Bo', 'age': 31, 'remote': True}
# print(type(restored))               # output: <class 'dict'>  ← it's a dict again
# print(restored["age"] + 1)          # output: 32  ← types are preserved

# # Pretty-printing with indent
# pretty = json.dumps(employee, indent=1)    # indent= for human-readable output
# print(pretty)
# # output:
# # {
# #   "name": "Bo",
# #   "age": 31,
# #   "remote": true
# # }



# # Write Python data to a JSON file
# team = {"project": "pipeline", "members": ["Ana", "Bo", "Cy"]}

# with open("week_7/w7d5/team.json", "w") as f:
#     json.dump(team, f, indent=2)         # dump to file (no 's')
# # team.json now contains formatted JSON text

# # Read JSON file back into Python
# with open("week_7/w7d5/team.json", "r") as f:
#     loaded = json.load(f)                # load from file (no 's')

# print(loaded)
# print(loaded["members"][0])
# # output: {'project': 'pipeline', 'members': ['Ana', 'Bo', 'Cy']}
# # output: Ana




json_text = '''{
    "company": "Acme",
    "departments": [
        {
            "name": "Engineering",
            "head": "Dana",
            "employees": [
                {"id": 1, "name": "Eve", "skills": ["python", "sql"]},
                {"id": 2, "name": "Fay", "skills": ["java", "docker"]}
            ]
        }
    ]
}'''

data = json.loads(json_text)

# Step by step into the structure
dept = data["departments"][0]              # first department (a dict)
print(dept["name"])                        # output: Engineering

employees = dept["employees"]              # list of employee dicts
print(employees[1]["name"])                # output: Fay

skills = employees[0]["skills"]            # list of strings
print(skills[1])                           # output: sql

# One-liner deep access
print(data["departments"][0]["employees"][0]["skills"][0])
# output: python