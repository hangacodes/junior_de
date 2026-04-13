# file: score_utils.py

def parse_score_line(line):
    
    parts = line.split(",")
    name = parts[0].strip().title()
    try:
        score = int(parts[1].strip())
    except ValueError:
        return False
    
    return {
        "name":name,
        "score": score
    }
    
    # line format: "PlayerName,score_value"
    #TODO: split on comma, strip the name, convert score to int
    #TODO: return a dict like {"player": "Ada", "score": 88}
    # Hint: use .split(",") from W1D6, .strip().title() for names, int() for score
    

def filter_passing(records, threshold=60):
    passed = []
    for record in records:
        if record["score"] >= threshold:
            passed.append(record)
    return passed
    #TODO: return a list of records where score >= threshold
    # Hint: accumulator pattern from W3D4, default parameter from W5D4
    pass

def top_scorer(records):
    best = records[0]
    for record in records:
        if record["score"] > best["score"]:
            best = record
            
    return best
    #TODO: return the dict with the highest score (running-max from W3D4)
    # Hint: initialize best = records[0], loop and compare
    pass

def average_score(records):
    total = 0
    if len(records) == 0:
        return 0.0
    
    for record in records:
        total += record["score"]
    average = total / len(records)
    return average
    #TODO: compute average score across all records
    # Hint: accumulator for total, divide by len(records)
    # Guard against empty list (return 0.0 if no records)
    pass



if __name__ == "__main__":
    raw_lines = [
    "  ada , 88",
    "BOB, 45",
    "Cara,  91",
    " dee,60 ",
    "EVE ,  73"]
    
    records = []
    for line in raw_lines:
        records.append(parse_score_line(line))  
    print(records)
    print(filter_passing(records))

    print(top_scorer(records))
    print(average_score(records))
    #TODO: write 2-3 quick tests using print()
    pass