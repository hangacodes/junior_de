'''### 6C) Semi-Guided (45-60 min)

**Goal:** Build `parse_user_row` that converts a raw dict of strings into a clean dict of typed values, using all four clauses plus `as e`.'''

def parse_user_row(row):
    """
    row: dict with string values, e.g. {"user_id": "10", "age": "33", "city": "Helsinki"}
    Returns: cleaned dict with int conversions, or None if invalid.
    """
    try:
        user_id = int(row["user_id"])
        age = int(row["age"])
        city = row["city"].strip().title()
        #TODO: access row["user_id"] and row["age"], convert both to int
        #TODO: access row["city"] and strip it
        # Hint: KeyError if a key is missing, ValueError if conversion fails
        pass
    except KeyError as e:
        print(f"Missing key: {e}")
        #TODO: print which key was missing using e
        # Hint: `as e` gives you the key name — include it in the message
        return None
    except ValueError as e:
        print(f"Conversion failed: {e}")
        #TODO: print that a conversion failed, include e in the message
        return None
    else:
        return {"user_id": user_id, "age": age, "city": city}
        #TODO: return the cleaned dict (only if try succeeded)
        # Hint: build the dict here, not in try — keeps try minimal
        
    finally:
        print("processed row")
        #TODO: print "processed row" (runs every time, for logging)
        # Remember: this runs even when the function is about to return
       

# Test data — mix of good and bad
rows = [
    {"user_id": "10", "age": "33", "city": " Helsinki "},
    {"user_id": "x", "age": "33", "city": "Espoo"},
    {"user_id": "11", "city": "Turku"},
    {"user_id": "12", "age": "28", "city": " Oulu "},
]

good = []
bad_count = 0
for r in rows:
    result = parse_user_row(r)
    if result is not None:
        good.append(result)
    else:
        bad_count += 1

print("Good:", good)
print("Bad count:", bad_count)