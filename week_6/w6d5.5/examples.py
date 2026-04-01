class DataRecord:
    def __init__(self, record_id, status):
        self.record_id = record_id
        self.status = status.strip().lower()

    def summary(self):
        return self.record_id + " [" + self.status + "]"


class SensorRecord(DataRecord):
    def __init__(self, record_id, status, temp):
        super().__init__(record_id, status)
        self.temp = temp

    def summary(self):
        return self.record_id + ": temp=" + str(self.temp)

class OrderRecord(DataRecord):
    def __init__(self, record_id, status, customer, total):
        super().__init__(record_id, status)
        self.customer = customer
        self.total = total

    def summary(self):
        return self.record_id + ": " + self.customer + " $" + str(self.total)

records = [
    SensorRecord("S-001", "ok", 23.5),
    OrderRecord("O-010", "shipped", "Alice", 37.50),
    SensorRecord("S-002", "ok", 18.0),
]

for r in records:
    print(r.summary())    # Python picks the right summary() for each object