import json

catalog = {
    "store": "City Books",
    "last_updated": "2026-03-15",
    "books": [
        {"title": "Data Pipelines Pocket Reference", "author": "James Densmore", "price": 29.99, "stock": 3, "genres": ["tech", "data"]},
        {"title": "Designing Data-Intensive Applications", "author": "Martin Kleppmann", "price": 42.00, "stock": 0, "genres": ["tech", "systems"]},
        {"title": "The Pragmatic Programmer", "author": "Hunt and Thomas", "price": 35.50, "stock": 12, "genres": ["tech", "career"]},
        {"title": "Sapiens", "author": "Yuval Noah Harari", "price": 15.99, "stock": 8, "genres": ["history", "science"]},
        {"title": "Atomic Habits", "author": "James Clear", "price": 14.99, "stock": 0, "genres": ["self-help"]},
    ]
}

with open("week_7/w7d5/deliverable/catalog_input.json", "w") as f:
    json.dump(catalog, f, indent=2)

def load_catalog(path):
    try:
        with open(path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return None
    return data

def build_summary(catalog):
    summary = {
        "store": catalog["store"],
        "total_books": 0,
        "total_value": 0,
        "genres": {},
        "out_of_stock_count" : 0

    }
    summary["total_books"] = len(catalog["books"])
    for book in catalog["books"]:
        summary["total_value"] += book["price"] * book["stock"]
        if book["stock"] == 0:
            summary["out_of_stock_count"] += 1
        
        

        for genre in book["genres"]:
            summary["genres"][genre] = summary["genres"].get(genre, 0) + 1
    summary["total_value"] = round(summary["total_value"], 2)
    return summary

def find_restock_needed(catalog, threshold = 5):
    restock = []
    for book in catalog["books"]:
        if book["stock"] < threshold:
            restock.append({"title": book["title"], "author": book["author"], "stock": book["stock"]})
    return restock


data = load_catalog("week_7/w7d5/deliverable/catalog_input.json")
summary = build_summary(data)
restock = find_restock_needed(data)

with open("week_7/w7d5/deliverable/catalog_summary.json", "w") as f:
    json.dump(summary, f, indent=2)

with open("week_7/w7d5/deliverable/restock_alert.json", "w") as f:
    json.dump(restock, f, indent=2)

with open("week_7/w7d5/deliverable/catalog_summary.json", "r") as f:
    print(json.load(f))

with open("week_7/w7d5/deliverable/restock_alert.json", "r") as f:
    print(json.load(f))

