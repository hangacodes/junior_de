def summarize_grades(path):
    summary = {
        "total_students": 0,
        "subject_counts": {},
        "highest": None,
        "failing": []
        }
    highest_grade = 0
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            header = f.readline()
            
            for line in f:
                cleaned = line.strip()
                if cleaned == "":
                    continue

                parts = cleaned.split(",")
                if len(parts) != 3:
                    continue
                
                name = parts[0].strip().title()
                subject = parts[1].strip().lower()
                try:
                    grade = int(parts[2].strip())
                except ValueError as e:
                    continue
                summary["total_students"] += 1

                #Count Subjects:
                if subject in summary["subject_counts"]:
                    summary["subject_counts"][subject] += 1
                else:
                    summary["subject_counts"][subject] = 1

                #Track highest:
                if grade > highest_grade:
                    highest_grade = grade
                    summary["highest"] = cleaned

                #Collect Failing:
                if grade < 60:
                    summary["failing"].append(cleaned)
        
    
    except FileNotFoundError:
        return summary

    return summary
    

with open("week_7/w7d2/deliverable/grades.txt", "w", encoding="utf-8") as f:
    f.write("name,subject,grade\n")
    f.write("Ada,Math,92\n")
    f.write("Lin,Science,55\n")
    f.write("Max,Math,78\n")
    f.write("Zoe,Science,98\n")
    f.write("Ray,Math,42\n")
    f.write("\n")
    f.write("Eve,Science,67\n")


result = summarize_grades("week_7/w7d2/deliverable/grades.txt")
print(f"Total students:{result['total_students']}")
print(f"Subject counts:{result['subject_counts']}")
print(f"Highest:{result['highest']}")
print(f"Failing:{result['failing']}")