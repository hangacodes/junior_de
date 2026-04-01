# #**A1 — Predict:** What prints?class Animal:
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return self.name + " says hello"

# class Dog(Animal):
#     pass

# d = Dog("Rex")
# print(d.speak())    #Rex says hello

# #**A2 — Predict:** What prints?

# class Base:
#     def label(self):
#         return "BASE"

# class Child(Base):
#     def label(self):
#         return "CHILD"

# b = Base()
# c = Child()
# print(b.label())        #BASE
# print(c.label())        #CHILD

# #**A3 — Spot the bug:**
# class DataRecord:
#     def __init__(self, record_id):
#         self.record_id = record_id

# class SensorRecord(DataRecord):
#     def __init__(self, record_id, temp):
#         super().__init__(record_id)     #This line was missing
#         self.temp = temp

# s = SensorRecord("S-001", 23.5)
# print(s.record_id)

# #**A4 — Predict:** Does this work?

# class DataRecord:
#     def __init__(self, record_id, status):
#         self.record_id = record_id
#         self.status = status

#     def is_valid(self):
#         return self.status == "ok"

# class LogRecord(DataRecord):
#     def __init__(self, record_id, status, level):
#         super().__init__(record_id, status)
#         self.level = level

# log = LogRecord("L-001", "ok", "INFO")
# print(log.is_valid())
# #Yes ofc , why wouldn't it work ?

'''### 6B) Guided drills'''

# '''**B1 — Basic child class**

# Task: Create a parent `DataRecord` with `record_id` and `status`. Create a child `LogRecord` that adds `level` and `message`. Use `super().__init__()`.

# - Hint: `LogRecord.__init__` takes 4 params: `self, record_id, status, level, message`
# - Test: `LogRecord("L-01", "ok", "WARN", "slow response").level` → `"WARN"`'''

# class DataRecord:
#     def __init__(self, record_id, status):
#         self.record_id = record_id
#         self.status = status


# class LogRecord(DataRecord):
#     def __init__(self, record_id, status, level, message):
#         super().__init__(record_id, status)
#         self.level = level
#         self.message = message

# print(LogRecord("L-01", "ok", "WARN", "slow response").level)

# '''**B2 — Override a method**

# Task: Using the `DataRecord` from B1 (which has `summary()` returning `record_id + " [" + status + "]"`), override `summary()` in `LogRecord` to include the level.

# - Hint: Child's `summary()` returns something like `"L-01 [ok] WARN: slow response"`
# - Test: `LogRecord("L-01", "ok", "WARN", "slow response").summary()`'''

# class DataRecord:
#     def __init__(self, record_id, status):
#         self.record_id = record_id
#         self.status = status

#     def summary(self):
#         return self.record_id + " [" + self.status + "]" 
    
# class LogRecord(DataRecord):
#     def __init__(self, record_id, status, level, message):
#         super().__init__(record_id, status)
#         self.level = level
#         self.message = message

#     def summary(self):
#         return self.record_id + " [" + self.status + "] " + self.level + " " + self.message
    
# print(LogRecord("L-01", "ok", "WARN", "slow response").summary())
# print(DataRecord("L-02", "not ok").summary())

# '''**B3 — Polymorphism loop**

# Task: Create `SensorRecord(DataRecord)` with `temp` and its own `summary()`. Create a mixed list of `LogRecord` and `SensorRecord`, loop through, and call `summary()` on each.

# - Hint: Python picks the right `summary()` based on object type
# - Test: Mixed list should print different formats per object'''

# class DataRecord:
#     def __init__(self, record_id, status):
#         self.record_id = record_id
#         self.status = status

#     def summary(self):
#         return self.record_id + " [" + self.status + "]" 
    
# class SensorRecord(DataRecord):
#     def __init__(self, record_id, status, temp):
#         super().__init__(record_id, status)
#         self.temp = temp

#     def summary(self):
#         return self.record_id + ": " + self.status + " " + str(self.temp) + " celsius"
    
# records = [
#     SensorRecord("S-001", "ok", 23.5),
#     DataRecord("T-005", "ok"),
#     SensorRecord("S-002", "fail", -55.0),
#     DataRecord("T-006", "ok"),
# ]

# for r in records:
#     print(r.summary())


'''**B4 — Composition example**

Task: Create a `RecordBatch` class that takes a list of `DataRecord` objects (composition). Add `valid_count()` and `invalid_count()` methods.

- Hint: `RecordBatch` does NOT inherit from `DataRecord` — it contains records
- Test: `RecordBatch([...]).valid_count()` should return count of records where `is_valid()` is True'''
class DataRecord:
    def __init__(self, record_id, status):
        self.record_id = record_id
        self.status = status

    def is_valid(self):
        return self.status == "ok"
    
    def summary(self):
        return self.record_id + " [" + self.status + "]" 
class RecordBatch:
    def __init__(self, records):
        self.records = records

    def valid_count(self):
        count = 0
        for r in self.records:
            if r.is_valid():
                count += 1
        return count
    def invalid_count(self):
        return len(self.records) - self.valid_count()

records = [
    DataRecord("S-001", "ok"),
    DataRecord("T-005", "ok"),
    DataRecord("S-002", "fail"),
    DataRecord("T-006", "ok"),
]
count = RecordBatch(records)
print(count.valid_count())
print(count.invalid_count())