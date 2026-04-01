class DataSource:
    def __init__(self, name, source_type):
        self.name = name.strip().lower()
        self.source_type = source_type

    def is_ready(self):
        return True
    
    def describe(self):
        return self.name + " (" + self.source_type + ")"

    def load(self):
        return []
    
class CsvSource(DataSource):
    def __init__(self, name, lines):
        super().__init__(name, source_type = "csv")
        self.lines = lines

    def load(self):
        result = []
        
        for line in self.lines:
            fields = line.split(",")
            cleaned = []
            for field in fields:
                cleaned.append(field.strip())
            result.append({"fields": cleaned, "raw": line})


        return result
    def describe(self):
        return f" {self.name} ({self.source_type}) {len(self.lines)}"  


class ApiSource(DataSource):
    def __init__(self, name, records):
        super().__init__(name, source_type="api")
        self.records = records

    def load(self):
        return self.records
    
    def is_ready(self):
        if len(self.records) == 0:
            return False
        return True
    def describe(self):
        return f" {self.name} ({self.source_type}) {len(self.records)}"  
    
class Pipeline:
    def __init__(self, sources):
        self.sources = sources

    def run(self):
        all_records = []
        skipped = 0
        for source in self.sources:
            if not source.is_ready():
                skipped += 1
                continue
            loaded = source.load()
            for record in loaded:
                all_records.append(record)
        return all_records, skipped
    
    def report(self):
        loaded, skipped = self.run()
        lines = []
        lines.append("=== PIPELINE RUN REPORT ===")
        lines.append("\nSources:")
        for source in self.sources:
            lines.append(f"   {source.describe()}")
        active = len(self.sources) - skipped
        lines.append(f"\nRun results:")
        lines.append(f"   Loaded: {len(loaded)} records from {active} sources")
        lines.append(f"   Skipped: {skipped} source (not ready)")
        lines.append("\n=== End Report ===")

        return "\n".join(lines)

csv_lines = [
    "ORD001, Alice, 37.50, shipped",
    "ORD002, Bob, 45.00, pending",
    "ORD003, Alice, 8.75, shipped",
]

api_records = [
    {"id": "S-001", "temp": 23.5, "status": "ok"},
    {"id": "S-002", "temp": 72.8, "status": "fail"},
]

empty_api = []

sources = [
    CsvSource("order_feed", csv_lines),
    ApiSource("sensor_api", api_records),
    ApiSource("empty_api", empty_api),
]

pipeline = Pipeline(sources)
print(pipeline.report())