columns = ["id", "email", "email", "name", "status"]
for col in columns:
    if col == "email":
        columns.remove(col)
print(columns)