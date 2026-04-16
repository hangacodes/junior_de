import pandas as pd

df = pd.DataFrame([
    {"name": "Ava", "dept": "Data", "salary": 90000},
    {"name": "Bo", "dept": "Sales", "salary": 65000},
    {"name": "Cal", "dept": "Data", "salary": 78000},
    {"name": "Dee", "dept": "Data", "salary": 105000},
])

# # AND: both conditions must be True
# mask_and = (df["dept"] == "Data") & (df["salary"] >= 80000)
# print(df.loc[mask_and])
# #   name  dept  salary
# # 0  Ava  Data   90000
# # 3  Dee  Data  105000

# # OR: either condition can be True
# mask_or = (df["dept"] == "Sales") | (df["salary"] >= 100000)
# print(df.loc[mask_or])
# #   name   dept  salary
# # 1   Bo  Sales   65000
# # 3  Dee   Data  105000




# # Boolean indexing version:
# result1 = df.loc[(df["dept"] == "Data") & (df["salary"] >= 80000)]
# print(result1)
# # .query() version — same result, more readable:
# result2 = df.query("dept == 'Data' and salary >= 80000")
# print(result2)
# #   name  dept  salary
# # 0  Ava  Data   90000


# df2 = df

# # Ascending (default): lowest salary first
# print(df2.sort_values(by="salary"))

# # Descending: highest salary first
# print(df2.sort_values(by="salary", ascending=False))

# # Multi-column: by dept first, then by salary within each dept
# print(df2.sort_values(by=["dept", "salary"]))


filtered = df.loc[df["dept"] == "Data"]
print("Before reset:")
print(filtered)
# index: 0, 2, 3 (gap at 1)

clean = filtered.reset_index(drop=True)
print("\nAfter reset:")
print(clean)
# index: 0, 1, 2 (clean)
clean_with_orig = filtered.reset_index().rename(columns={"index":"original_position"})
print(clean_with_orig)


