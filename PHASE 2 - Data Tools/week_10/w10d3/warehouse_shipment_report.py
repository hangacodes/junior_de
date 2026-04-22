import pandas as pd

shipments = pd.DataFrame({
    "shipment_id": [5001, 5002, 5002, 5003, 5004, 5005, 5006, 5007],
    "warehouse": ["North", "North", "North", None, "South", "South", "East", "East"],
    "category": ["Electronics", "Furniture", "Furniture", "Electronics", None, "Clothing", "Electronics", "Furniture"],
    "weight_kg": [45.0, 120.5, 120.5, 30.0, 15.0, 8.5, 55.0, 200.0],
    "quantity": [3, 1, 1, 5, 10, 20, 2, 1]
})
#Validation before:
rows_before = (len(shipments))
weight_before = shipments["weight_kg"].sum()

#Fill missing keys
shipments["warehouse"] = shipments["warehouse"].fillna("UNASSIGNED")
shipments["category"] = shipments["category"].fillna("Uncategorized")

#Dedup
shipments = shipments.drop_duplicates(subset=["shipment_id"])

#Validation after
rows_after = len(shipments)
weight_after = shipments["weight_kg"].sum()

#Group and aggregate
report = shipments.groupby("warehouse")["weight_kg"].agg(["count", "sum", "mean", "min", "max"])

print("--- WAREHOUSE SHIPMENT REPORT ---\n")
print(report)

print("\n=== VALIDATION ===\n")
print(f"Rows: {rows_before} -> {rows_after}")
print(f"Total weight: {weight_before} -> {weight_after}")
print(f"Warehouses in output: {len(report)}")


# What Could Go Wrong:
# If warehouse names are inconsistent ("north" vs "North "), the report
# splits one warehouse into two groups. Fix: canonicalize warehouse names
# before grouping using .str.strip().str.lower() (from W10D2).