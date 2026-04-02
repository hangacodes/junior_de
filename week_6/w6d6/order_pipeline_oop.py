from dataclasses import dataclass

@dataclass
class Order:
    order_id: str
    customer: str
    product: str
    quantity: int
    unit_price: float
    status: str

    @property
    def total(self):
        return self.quantity * self.unit_price
    
    @property
    def is_high_value(self):
        return self.total >= 50.0
    
    def __str__(self):
        return f"{self.order_id}: {self.customer} - {self.product.title()} x{str(self.quantity)} @ ${str(self.unit_price):.2f} = ${str(self.total):.2f} [{self.status.lower()}]"
    
class OrderParser:
    def __init__(self):
        pass

    def parse_line(self, line:str):
        fields = line.split("|")
        if len(fields) != 6:
            return None
        if fields[1].strip() == "" or fields[2].strip() == "":
            return None
        try:
            qty = int(fields[3].strip())
            unit_price = float(fields[4].strip())
        except ValueError:
            return None
        return Order(
            order_id=fields[0].strip(),
            customer=fields[1].strip(),
            product=fields[2].strip(),
            quantity=qty,
            unit_price=unit_price,
            status=fields[5].strip()
        )
    

    def parse_all(self, lines:list) -> tuple:
        valid_orders = []
        rejected_count = 0
        for line in lines:
            result = self.parse_line(line)
            if result is None:
                rejected_count +=1
            else:
                valid_orders.append(result)

        return valid_orders, rejected_count
    
class OrderReport:
    def __init__(self, orders:list):
        self.orders = orders

    @property
    def total_revenue(self):
        total_revenue = 0
        for order in self.orders:
            total_revenue += order.total
        return total_revenue
    @property
    def high_value_count(self):
        count = 0
        for order in self.orders:
            if order.total >= 50.0:
                count += 1
        return count
    
    def group_by_status(self):
        groupped = {}
        for order in self.orders:
            groupped.setdefault(order.status, []).append(order)
        return groupped
    
    def status_summary(self):
        status_summary = {}
        for k, v in self.group_by_status().items():
            count = len(v)
            total_revenue = 0
            for order in v:
                total_revenue += order.total
            status_summary[k] = {"count": count, "revenue": round(total_revenue, 2)}
        return status_summary
    
    def top_customers(self):
        customer_totals = {}
        for order in self.orders:
            customer_totals[order.customer] = customer_totals.get(order.customer, 0) + order.total
    
        top_customer = None
        best_total = 0
        for name, spent in customer_totals.items():
            if spent > best_total:
                best_total = spent
                top_customer = name
        return top_customer, round(best_total)

    def __str__(self):
        lines = []
        lines.append("=== ORDER PROCESSING REPORT ===")
        lines.append(f"Total orders: {len(self.orders) + self._rejected}")
        lines.append(f"Valid orders:{len(self.orders)}")
        lines.append(f"Rejected lines:{self._rejected}")
        lines.append("")
        lines.append("--- By Status ---")
        summary = self.status_summary()
        for status in sorted(summary.keys()):
            info = summary[status]
            lines.append(f"{status}: {info['count']} orders, ${info['revenue']:.2f} revenue")
        lines.append("")
        top_name, top_spent = self.top_customers()
        lines.append(f"Top customer:{top_name} (${top_spent:.2f})")
        
        lines.append(f"High-value orders (>=$50.00):{self.high_value_count}")
        lines.append("")
        lines.append("=== END REPORT ===")
        return "\n".join(lines)
    
raw_orders = [
    "ORD001 | Alice | Widget A | 3 | 12.50 | shipped",
    "ORD002 | Bob | Widget B | 1 | 45.00 | pending",
    "ORD003 | Alice | Widget C | 2 | 8.75 | shipped",
    "ORD004 | Charlie | | 5 | 10.00 | shipped",
    "ORD005 | Bob | Widget A | abc | 12.50 | pending",
    "ORD006 | Alice | Widget B | 1 | 45.00 | cancelled",
    "ORD007 | Dave | Widget A | 4 | 12.50 | shipped",
    "ORD008 | | Widget C | 2 | 8.75 | pending",
    "ORD009 | Charlie | Widget B | 1 | | shipped",
    "ORD010 | Bob | Widget A | 2 | 12.50 | shipped",
    "ORD011 | Alice | Widget A | 1 | 12.50 | shipped",
    "ORD012 | Dave | Widget C | 3 | 8.75 | pending",
    "MALFORMED LINE WITH NO PIPES",
    "ORD013 | Charlie | Widget A | 2 | 12.50 | shipped",
    "ORD014 | Alice | Widget B | 1 | 45.00 | shipped",
]
    
if __name__ == "__main__":
    parser = OrderParser()
    orders, rejected = parser.parse_all(raw_orders)
    report = OrderReport(orders)
    report._rejected = rejected
    print(report)