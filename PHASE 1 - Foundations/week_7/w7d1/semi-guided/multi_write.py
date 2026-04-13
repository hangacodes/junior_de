def save_report(path, title, items):
    with open(path, "w", encoding="utf-8") as f:
        f.write(title + "\n")
        for item in items:
            f.write(f"- {item}\n")


save_report("week_7/w7d1/semi-guided/inventory.txt", "INVENTORY CHECK", ["screws: 500", "bolts: 230", "washers: 180"])

# Verify: read it back
with open("week_7/w7d1/semi-guided/inventory.txt", "r", encoding="utf-8") as f:
    print(f.read())

# Expected output:
# INVENTORY CHECK
# - screws: 500
# - bolts: 230
# - washers: 180