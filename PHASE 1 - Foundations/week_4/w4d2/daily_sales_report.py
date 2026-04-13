sales_by_sku = {"sku_001": 3, "sku_002": 0, "sku_003": 8, "sku_004": 1}
price_by_sku = {"sku_001": 9.99, "sku_002": 5.00, "sku_003": 2.50, "sku_004": 100.00}


total_units = 0
total_revenue = 0
print("=== DAILY SALES REPORT ===")

for sku, price in sorted(price_by_sku.items()):
    sales = sales_by_sku.get(sku, 0)
    total_units += sales
    total_revenue = total_revenue + sales * price
    print(f"{sku} | qty={sales} | revenue={sales * price:.2f}")
print(f"\nTOTAL UNITS: {total_units}")
print(f"TOTAL REVENUE: {total_revenue:.2f}")

inactive = []
for sku, sales in sales_by_sku.items():
    if sales == 0:
        inactive.append(sku)
        
print(f"INACTIVE: {inactive}")

        
