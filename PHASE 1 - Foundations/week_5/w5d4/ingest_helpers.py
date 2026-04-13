lines = [
    "ts=2026-03-10; sensor=temp_01; reading=22.5; unit=C",
    "ts=2026-03-10; sensor=humidity_03; reading=bad_data; unit=%",
    "sensor=pressure_07; reading=1013"]


def parse_log(line, pair_sep=";", kv_sep="="):
    '''
    Docstring for parse_log
    
    :param line: This is the line of text
    :param pair_sep: Separates whole string into items 
    :param kv_sep: Separates the keys and values
    :if the lenght of the parts are == 2 (k and v), then we create the dict
    '''
    record = {}
    parts = line.split(pair_sep)
    for part in parts:
        if part.strip() == "":
            continue
        raw_parts = part.split(kv_sep)
        if len(raw_parts) == 2: 
            record[raw_parts[0].strip()] = raw_parts[1].strip()
    return record


def clean_log(record, required_keys=("ts", "sensor", "reading")):
    new_dict = {}
    for key in required_keys:
        if key in record:
            new_dict[key] = record[key].strip()

        else:
            new_dict[key] = "MISSING"
    return new_dict


def extract_reading(record, key="reading", default=0.0):
    try:
        return float(record[key].strip())
    except ValueError:
        return default

def count_sensors(records, key="sensor"):
    counts = {}
    for r in records:
        sensor = r.get(key, "UNKNOWN")
        counts[sensor] = counts.get(sensor, 0) + 1

    return counts

def format_alert(message, level="INFO", **meta):
    parts = [str(level) + ": " + str(message)]

    for k ,v in meta.items():
        parts.append(str(k) + "=" + str(v))
    
    return " | ".join(parts)

lines = [
    "ts=2026-03-10; sensor=temp_01; reading=22.5; unit=C",
    "ts=2026-03-10; sensor=humidity_03; reading=bad_data; unit=%",
    "sensor=pressure_07; reading=1013",
]

# Step 1: parse
records = []
for line in lines:
    records.append(parse_log(line))

# Step 2: clean
cleaned = []
for record in records:
    cleaned.append(clean_log(record))

# Step 3: extract readings
for record in cleaned:
    print(extract_reading(record))

# Step 4: count sensors
print(count_sensors(cleaned))

# Step 5: format an alert
print(format_alert("threshold exceeded", level="WARN", sensor="temp_01", reading=45.2))