# #**A1 — Predict:** What prints?
# class Box:
#     def __init__(self, label):
#         self.label = label

# b = Box("tools")
# print(b.label)      #tools
# print(type(b))      #__main__ something

# #**A2 — Spot the bug:**
# class Sensor:
#     def __init__(self, name, value):
#         self.name = name
#         self.value = value      #this line was missing "self."

# s = Sensor("temp", 22.5)
# print(s.value)

# #**A3 — Predict:** What does `result` contain?
# class Counter:
#     def __init__(self):
#         self.count = 0

#     def increment(self):
#         self.count = self.count + 1

# c = Counter()
# c.increment()
# c.increment()
# c.increment()
# result = c.count
# print(result)   #3

# #**A4 — Spot the bug:**
# class Greeter:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):        #missing the self parameter between paranthesis
#         return "Hello, " + self.name

# g = Greeter("Cristian")
# print(g.greet())

'''Guided Drills'''
# '''**B1 — LogEntry class**

# Task: Write a `LogEntry` class with `__init__` taking `level`, `service`, `message`. Store all three as attributes. Add a method `is_error()` that returns `True` if `self.level == "ERROR"`.

# - Hint: Clean `level` with `.upper()` and `service` with `.strip().lower()` inside `__init__`
# - Test: `LogEntry("error", " Auth ", "login").is_error()` → `True`'''

# class LogEntry:
#     def __init__(self, level, service, message):
#         self.level = level.upper()
#         self.service = service.strip().lower()
#         self.message = message

#     def is_error(self):
#         if self.level == "ERROR":
#             return True
# print(LogEntry("error", " Auth ", "login").is_error())

'''**B2 — Transaction class with net calculation**

# Task: Write a `Transaction` class with `__init__` taking `user`, `category`, `amount`, `discount`. Add a method `net()` that returns `amount - discount`.

# - Hint: All four values become `self.xxx` attributes
# - Test: `Transaction("Ava", "tech", 100.0, 10.0).net()` → `90.0`'''

# class Transaction:
#     def __init__(self,user, category, amount, discount):
#         self.user = user.title()
#         self.category = category
#         self.amount = amount
#         self.discount = discount

#     def net(self):
#         return self.amount - self.discount
        
# print(Transaction("Ava", "tech", 100.0, 10.0).net())


# '''**B3 — SensorReading with Fahrenheit conversion**

# Task: Write a `SensorReading` class with `station`, `temp`, `unit`. Add `to_fahrenheit()` returning `self.temp * 9/5 + 32`. Add `is_in_range(low, high)` returning a boolean.

# - Hint: Use default parameters: `def is_in_range(self, low=-40.0, high=60.0)`
# - Test: `SensorReading("stA", 23.5, "celsius").to_fahrenheit()` → `74.3`'''


# class SensorReading:
#     def __init__(self, station, temp, unit):
#         self.station = station
#         self.temp = temp
#         self.unit = unit

#     def to_fahrenheit(self):
#         return self.temp * 9/5 + 32
    
#     def is_in_range(self, low=-40.0, high=60.0):
#         return low <= self.temp <= high
    
# a = SensorReading("stA", 23.5, "celsius")
# print(a.is_in_range())
# print(a.to_fahrenheit())

# '''**B4 — ScoreRecord with grade label**

# Task: Write a `ScoreRecord` class with `player` and `score`. Add `grade()` that returns `"A"` for 90+, `"B"` for 80+, `"C"` for 70+, `"D"` for 60+, `"F"` otherwise.

# - Hint: Use the `if/elif/else` chain from W2D3 inside the method
# - Test: `ScoreRecord("Ada", 88).grade()` → `"B"`'''

# class ScoreRecord:
#     def __init__(self, player, score):
#         self.player = player
#         self.score = score


#     def grade(self):
#         if self.score >= 90:
#             return "A"
#         elif self.score >= 80:
#             return "B"
#         elif self.score >= 70:
#             return "C"
#         elif self.score >= 60:
#             return "D"
#         else:
#             return "F"
        
# print(ScoreRecord("Ada", 88).grade())

