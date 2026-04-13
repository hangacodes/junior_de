# #**A1 — Predict:** What prints?
# class Item:
#     def __init__(self, name):
#         self.name = name

# a = Item("wrench")
# print(a)

# #**A2 — Predict:** What prints?

# class Item:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return "Item: " + self.name

# a = Item("wrench")
# print(a)
# print(str(a)) #Item: wrench two times

# #**A3 — Predict:** What does `order.total` return?
# class Order:
#     def __init__(self, qty, price):
#         self.qty = qty
#         self.price = price

#     @property
#     def total(self):
#         return self.qty * self.price

# order = Order(4, 10.0)
# print(order.total)  #40
# order.qty = 6
# print(order.total)      #60

# #**A4 — Spot the bug:**
# from dataclasses import dataclass

# @dataclass
# class Record:
#     name: str
#     score: int

# r = Record("Ada", 88)
# print(r.name)
# print(r.score)
# r2 = Record("Ada", 88)
# print(r == r2)
# print(r.summary())

'''Guided Drills'''

# '''**B1 — Add `__str__` and `__repr__` to LogEntry**

# Task: Write a `LogEntry` class with `level`, `service`, `message`. Add `__str__` returning `"ERROR | auth | login failed"` format.
# Add `__repr__` returning `"LogEntry('ERROR', 'auth', 'login failed')"` format.

# - Hint: Use `repr(self.level)` inside `__repr__` to get quoted strings
# - Test: `print(LogEntry("ERROR", "auth", "crash"))` → `ERROR | auth | crash`'''

# class LogEntry:
#     def __init__(self, level, service, message):
#         self.level = level
#         self.service = service
#         self.message = message
#     def __str__(self):
#         return f"{self.level} | {self.service} | {self.message}"
    
#     def __repr__(self):
#         return f"{repr(self.level)} | {repr(self.service)} | {repr(self.message)}"
    
# log = LogEntry("ERROR", "auth", "crash")
# print(log)
# print(repr(log))

# '''**B2 — `@property` for computed field**

# Task: Write a `Transaction` class with `amount` and `discount`.
# Add a `@property` called `net` that returns `amount - discount`.
# Add a `@property` called `is_profitable` that returns `True` if `net > 0`.

# - Hint: `@property` goes on the line above `def net(self):`
# - Test: `Transaction(100, 10).net` → `90` (no parentheses)'''


# class Transaction:
#     def __init__(self, amount , discount):
#         self.amount = amount
#         self.discount = discount

#     @property
#     def net(self):
#         return self.amount - self.discount
    
#     @property
#     def is_profitable(self):
#         return self.net > 0
    

# print(Transaction(100, 10).net)
# print(Transaction(100, 100).is_profitable)
# print(Transaction(100, 10).is_profitable)


# '''**B3 — Dataclass version of SensorReading**

# Task: Rewrite the W6D4 `SensorReading` class as a `@dataclass`. Keep `station`, `temp`, `unit` as fields (with `unit` defaulting to `"celsius"`). Add `to_fahrenheit()` as a regular method.

# - Hint: `from dataclasses import dataclass`, then `@dataclass` above the class
# - Test: `SensorReading("stA", 23.5)` should print with auto-generated `__repr__`'''
# from dataclasses import dataclass
# @dataclass
# class SensorReading:
#     station :str
#     temp: float
#     unit: str = "celsius"
    
#     def to_fahrenheit(self):
#         return self.temp * 9/5 + 32
    

# reading = SensorReading("stA", 23.5)
# print(reading)
# print(reading.to_fahrenheit())

# '''**B4 — `__eq__` for custom equality**

# Task: Write a `ScoreRecord` class (without dataclass) with `player` and `score`. Add `__eq__` so two records with the same player and score are equal.

# - Hint: `return self.player == other.player and self.score == other.score`
# - Test: `ScoreRecord("Ada", 88) == ScoreRecord("Ada", 88)` → `True`'''

# class ScoreRecord:
#     def __init__(self, player, score):
#         self.player = player
#         self.score = score

#     def __eq__(self, other):
#         return self.player == other.player and self.score == other.score
    
# print(ScoreRecord("Ada", 88) == ScoreRecord("Ada", 88))

