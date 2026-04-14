import pandas as pd


classes = pd.DataFrame([
        {"class_name": "Yoga",     "instructor": "Maya",  "time_slot": "07:00", "attendees": 20, "full": True},
        {"class_name": "Spin",     "instructor": "Leo",   "time_slot": "09:00", "attendees": 14, "full": False},
        {"class_name": "HIIT",     "instructor": "Sara",  "time_slot": "11:00", "attendees": 25, "full": True},
        {"class_name": "Pilates",  "instructor": "Maya",  "time_slot": "13:00", "attendees": 10, "full": False},
        {"class_name": "Boxing",   "instructor": "Dan",   "time_slot": "17:30", "attendees": 18, "full": False},
        {"class_name": "Stretch",  "instructor": "Leo",   "time_slot": "19:00", "attendees": 22, "full": True}
],
        index=["CLS-01","CLS-02","CLS-03","CLS-04","CLS-05","CLS-06"]
)

print("\nClass names and instructors:")
print(classes[["class_name", "instructor"]])


print("\nClasses through 02 and 04 - by label:")
print(classes.loc["CLS-02":"CLS-04"])

print("\nClasses through 02 and 04 - by location:")
print(classes.iloc[1:4])

mask_available = classes["full"] == False
print("\nOpen classes:")
print(classes.loc[mask_available,["class_name", "instructor", "attendees"]])


classes.loc["CLS-01", "full"] = False
print("\nUpdated DataFrame:")
print(classes)
print(classes["attendees"].sum())

'''Selection bug'''
print("---------")
print("Bug testing")
# wrong mask — selects full classes instead of open ones
mask = classes["full"] == True
print(classes.loc[mask, "attendees"].sum())  # summing the wrong group

# quick check — print before summing
print(classes.loc[mask])  # you'd see full classes here and catch it

# correct mask
mask = classes["full"] == False
print(classes.loc[mask, "attendees"].sum())  # now summing open classes only