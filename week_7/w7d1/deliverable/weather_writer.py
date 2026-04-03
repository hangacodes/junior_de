def write_daily_report(path, station_id, readings):
    highest = readings[0]
    lowest = readings[0]
    total = 0
    if len(readings) == 0:
         return None
    for r in readings:
            if r > highest:
                highest = r

            if r < lowest:
                lowest = r

            total += r
    average = total / len(readings)
    with open(path, "w", encoding="utf-8") as f:
        f.write(station_id+":\n")
        f.write(f"Number or readings: {len(readings)}\n")
        f.write(f"Highest reading: {highest}\n")
        f.write(f"Lowest reading: {lowest}\n")
        f.write(f"Average: {average:.1f}")
    


station_id = "ST-042"
readings = [18, 22, 19, 25, 21, 17, 23, 34, 49, 22, 10, 38, 28, 30 , 23, 34]
average = round(sum(readings)) / len(readings)
write_daily_report("week_7/w7d1/deliverable/daily_report.txt", station_id, readings )

def append_to_history(path, station_id, avg_reading):
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"station_id={station_id} avg={round(avg_reading, 1)}\n")
    
append_to_history("week_7/w7d1/deliverable/weather_history.log", station_id, average)

with open("week_7/w7d1/deliverable/weather_history.log", "r", encoding="utf-8") as f:
    print(f.read())