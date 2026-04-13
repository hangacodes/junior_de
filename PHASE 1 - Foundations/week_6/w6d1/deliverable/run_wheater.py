import weather_utils

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
    clean_readings.append(weather_utils.parse_reading(line))

valid = (weather_utils.filter_valid(clean_readings))
for row in valid:
    print(row)

print(weather_utils.summarize(valid))


print(weather_utils.celsius_to_fahrenheit(valid[0]["temp"]))