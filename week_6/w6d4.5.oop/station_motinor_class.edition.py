class SensorReading:
    def __init__(self, station, temp, unit):
        self.station = station.strip().lower()
        self.temp = float(temp)
        self.unit = unit.strip().lower()

    def is_in_range(self, low=-40.0, high=60.0):
        return low <= self.temp <= high
    
    def to_fahrenheit(self):
        return self.temp * 9/5 + 32
    
class LogEntry:
    def __init__(self, level, service, message):
        self.level = level.strip().upper()
        self.service = service.strip().lower()
        self.message = message.strip()

    def is_error(self):
        return self.level == "ERROR"
    
    def format_line(self):
        formatted = " | ".join([self.level, self.service,self.message])
        return formatted

    
class ReadingBatch:
    def __init__(self, readings):
        self.readings = readings

    def valid_readings(self, low=-40.0, high=60.0):
        valid = []
        for reading in self.readings:
            if reading.is_in_range(low, high):
                valid.append(reading)
        return valid
    def count_valid(self):
        return len(self.valid_readings())
        

    def average_temp(self):
        valid = self.valid_readings()
        if len(valid) == 0:
            return 0.0
        total = 0
        for r in valid:
            total += r.temp
        return round(total / len(valid), 2)
    
    def summary(self):
        lines = []
        lines.append(f"Total readings: {str(len(self.readings))}")
        lines.append(f"Valid readings: {str(self.count_valid())}")
        lines.append(f"Average temp: {str(self.average_temp())}")
        return "\n".join(lines)

raw_lines = [
    "  StationA , 23.5, celsius",
    "StationB,  -3.0 ,celsius",
    " stationC, 45.2, celsius",
    "StationD , 72.8,celsius",
    "StationE,18.5,  celsius",
    "  StationF, -55.0, celsius",
    "StationG, 31.4, celsius",
    "StationH, 0.0, celsius",
]
readings = []
for line in raw_lines:
    parts = line.split(",")
    r = SensorReading(parts[0],float(parts[1].strip()), parts[2])
    readings.append(r)

batch = ReadingBatch(readings)

print("=== SENSOR STATION MONITOR ===")
print("\n--- All Readings ---")
for r in readings:
    f_temp = round(r.to_fahrenheit(), 2)
    status = "VALID" if r.is_in_range() else "OUT OF RANGE"
    print(f"{r.station}: {str(r.temp)}C ({str(f_temp)}F) -> {status}")

print("\n---Batch Summary---")
print(batch.summary())

out_count = len(readings) - batch.count_valid()

logs = [
    LogEntry("INFO", "monitor", "batch processed"),
    LogEntry("WARN", "monitor", str(out_count)+ "readings out of range")
]

print("\n--- Log Entries ---")
for log in logs:
    print(log.format_line())

print("\n=== END MONITOR ===")