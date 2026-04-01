'''### 6C) Semi-guided drill

**Goal:** Build an `OrderRecord` class and process a list of orders — replacing the dict-based pattern from W5D7.

Starter code:
'''

class OrderRecord:
    def __init__(self, order_id, customer, product, quantity, unit_price, status):
        self.order_id = order_id
        self.customer = customer.strip().title()
        self.product = product
        self.quantity = quantity
        self.unit_price = unit_price
        self.status = status.strip().lower()

        #TODO: store all six values as attributes
        #TODO: clean customer with .strip().title(), status with .strip().lower()
        

    def total(self):
        result = self.quantity * self.unit_price
        return result
        #TODO: return quantity * unit_price
        

    def is_high_value(self, threshold=50.0):
        if self.total() >= threshold:
            return True
        else:
            return False
        #TODO: return True if total() >= threshold
        

    def to_csv(self):
        return ",".join([self.order_id, self.customer, self.product, str(self.quantity), str(self.unit_price), self.status, str(self.total())])
        #TODO: return a comma-separated string of all fields + total
        # Hint: use str() for numbers, ",".join() from W1D6
        

# Test data (same orders from your W5D7 project)
raw_orders = [
    "ORD001 | Alice | Widget A | 3 | 12.50 | shipped",
    "ORD002 | Bob | Widget B | 1 | 45.00 | pending",
    "ORD003 | Alice | Widget C | 2 | 8.75 | shipped",
]

orders = []
for line in raw_orders:
    parts = line.split("|")
    order = OrderRecord(
        parts[0].strip(),
        parts[1].strip(),
        parts[2].strip(),
        int(parts[3].strip()),
        float(parts[4].strip()),
        parts[5].strip()
    )
    orders.append(order)
    total = 0

for order in orders:
    print(f"Customer: {order.customer}, total order:{order.total()} - high value order: {order.is_high_value()}")
#TODO: print each order's customer, total, and whether it's high-value
#TODO: compute total revenue across all orders using an accumulator
total = 0
for order in orders:
    total += order.total()
print(total)