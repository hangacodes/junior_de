def write_stock_report(path, products):
    total = 0
    with open(path, "w", encoding="utf-8") as f:
        f.write("DAILY STOCK REPORT\n")
        for record in products:
            name = record["name"]
            qty = record["quantity"]
            price = record["price"]
            line = f"{name}: qty={qty} price={price}"
            f.write(line.rstrip("\n") + "\n")
            total += qty
        f.write(f"Total items: {total}\n")


def log_restock_needed(path, products, threshold):
    with open(path, "a", encoding="utf-8") as f:
        for product in products:
            if product["quantity"] < threshold:
                name = product["name"]
                qty = product["quantity"]
                line = f"RESTOCK:{name} (qty={qty})"                
                f.write(line.rstrip("\n")+ "\n")

products = [
    {"name": "screws", "quantity": 500, "price": 0.05},
    {"name": "bolts", "quantity": 12, "price": 0.12},
    {"name": "washers", "quantity": 3, "price": 0.03},
    {"name": "nails", "quantity": 800, "price": 0.02},
    {"name": "brackets", "quantity": 7, "price": 1.50},
]
threshold = 15

write_stock_report("week_7/w7d3/deliverable/stock_report.txt", products)
log_restock_needed("week_7/w7d3/deliverable/restock.log", products, threshold)

# Verify
print("=== Stock Report ===")
with open("week_7/w7d3/deliverable/stock_report.txt", "r", encoding="utf-8") as f:
    print(f.read())

print("=== Restock Log ===")
with open("week_7/w7d3/deliverable/restock.log", "r", encoding="utf-8") as f:
    print(f.read())