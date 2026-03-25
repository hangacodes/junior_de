# file: run_scores.py
import score_utils

raw_lines = [
    "  ada , 88",
    "BOB, 45",
    "Cara,  91",
    " dee,60 ",
    "EVE ,  73"
]
records = []
for line in raw_lines:
    records.append(score_utils.parse_score_line(line))  
print(records)
print(score_utils.filter_passing(records))

print(score_utils.top_scorer(records))
print(score_utils.average_score(records))

#TODO: parse each line into a record using score_utils.parse_score_line
#TODO: print the parsed records
#TODO: print passing students (threshold 60) using score_utils.filter_passing
#TODO: print the top scorer using score_utils.top_scorer
#TODO: print the average using score_utils.average_score