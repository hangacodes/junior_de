# class SensorReading:
#     def __init__(self, station, temp, unit):
#         self.station = station
#         self.temp = temp
#         self.unit = unit

#     def __repr__(self):
#         return f"LogEntry ({repr(self.station)}, {repr(self.unit)})"

#     def __str__(self):
#         return f"{self.station}: {str(self.temp)}°{self.unit[0].upper()}"

# reading = SensorReading("stationA", 23.5, "celsius")
# print(reading)
# print("Reading is: " + str(reading))
# print(repr(reading))


# class OrderRecord:
#     def __init__(self, customer, quantity, unit_price):
#         self.customer = customer
#         self.quantity = quantity
#         self.unit_price = unit_price

#     @property
#     def total(self):
#         return self.quantity * self.unit_price

# order = OrderRecord("Alice", 3, 12.50)
# print(order.total)        # no parentheses — looks like an attribute
# order.quantity = 5         # change quantity
# print(order.total)         # total updates automatically

# class SensorReading:
#     def __init__(self, station, temp):
#         self.station = station
#         self.temp = temp

#     def __eq__(self, other):
#         return self.station == other.station and self.temp == other.temp

# a = SensorReading("stA", 23.5)
# b = SensorReading("stA", 23.5)
# c = SensorReading("stB", 18.0)

# print(a == b)    # True — same data
# print(a == c)    # False — different data
# print(a is b)    # False — different objects in memory

from dataclasses import dataclass

# @dataclass
# class SensorReading:
#     station : str
#     temp : float
#     unit : str

# reading = SensorReading("stationA", 23.5, "celsius")
# reading2 = SensorReading("stationA", 23.5, "celsius")
# print(reading)
# print(reading.temp)
# print(reading == reading2)
# print(reading2.unit)

@dataclass
class Book:
    title: str
    author: str
    pages: int

    def __post_init__(self):
        if self.pages <= 0:
            raise ValueError("A book needs at least one page")
    
book = Book("me " ,"mine" ,0)