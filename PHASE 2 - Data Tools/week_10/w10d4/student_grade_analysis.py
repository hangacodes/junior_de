import pandas as pd

grades = pd.DataFrame({
    "student_id": ["S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08"],
    "department": ["CS", "CS", "CS", None, "Math", "Math", "Math", "CS"],
    "course": ["Intro", "Intro", "Adv", "Intro", "Calc", "Stats", "Calc", "Adv"],
    "grade": [85, 92, 78, 65, 90, 88, 72, 95],
    "credits": [3, 3, 4, 3, 4, 3, 4, 4],
})

grades["department"] = grades["department"].fillna("Undeclared")
print(grades) 

#Output 1 :
summary = grades.groupby(by=["department", "course"]).agg(
    avg_grade = ("grade", "mean"),
    student_count = ("student_id", "count"),
    total_credits = ("grade", "sum")
)
print("---OUTPUT 1: Summary ---")
print(summary)

#Output 2 :
output2 = grades.pivot_table(index="department", columns="course", values="grade", aggfunc="mean")

print("---OUTPUT 2: Pivot table---")
print(output2)

#Output 3 :
grades["dept_avg_grade"] = grades.groupby("department")["grade"].transform("mean")
grades["rank_in_dept"] = grades.groupby("department")["grade"].rank(ascending=False, method="dense")
print("===OUTPUT 3: Row-Level context===")
print(grades)