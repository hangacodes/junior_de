def parse_reading(line):
    parts = line.split(",")
    station = parts[0].strip().lower()
    unit = parts[2].strip().lower()
    try:
        temp = float(parts[1].strip())
    except ValueError:
        return False
    
    return {
        "station": station,
        "temp": temp,
        "unit": unit
    }
    #if a line has only 2 fields - parts[2] raises IndexError
def celsius_to_fahrenheit(c):
    fahrenheit = c * 9/5 + 32

    return fahrenheit

def is_temp_valid(temp, low=-50.0, high=60.0):
    
    return low <= temp <= high
      
    
def filter_valid(readings, low=-50.0, high=60.0):
    valid_readings = []
    for line in readings:
        if  is_temp_valid(line["temp"], low, high):
            valid_readings.append(line)
    return valid_readings

def summarize(readings):
    if len(readings) == 0:
        return {"count": 0, "min": None, "max": None, "avg": None}
    count = 0
    highest = readings[0]["temp"]
    lowest = readings[0]["temp"]
    total = 0
    for line in readings:
        if line["temp"] > highest:
            highest = line["temp"]
        if line["temp"] < lowest:
            lowest = line["temp"]
        count+= 1
        total += line["temp"]

    avg = total / count
    return {
        "count": count,
        "max": highest,
        "min": lowest,
        "avg": round(avg, 2)
    }

if __name__=="__main__":
    raw_lines = [
    "  StationA , 23.5, celsius ",
    "StationB,  -3.0 ,celsius",
    " stationC, 45.2, celsius",
    "StationD , 72.8,celsius",
    "StationE,18.5,  celsius",
    "  StationF, -55.0, celsius ",
    "StationG, 31.4, celsius",
    "StationH, 0.0 , fahrenheit",
]
    clean_readings = []
    valid_range = []
    for line in raw_lines:
        clean_readings.append(parse_reading(line))    
        valid = (filter_valid(clean_readings))
    for row in valid:
        print(row)

    print(summarize(valid))