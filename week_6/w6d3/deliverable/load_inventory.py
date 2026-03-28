#Main
import parse_product
lines = [
    "|Widget|9.99|50",
    "|Gadget|BAD_PRICE|30",
    "|Sprocket|4.50",
    "|Bolt|0.75|200",
    "|EmptyID|5.00|10",
    "|Nut|2.25|150\n",
    "|Washer|1.50|abc_qty",
]


def load_inventory(lines):
    products_list = []
    processed = 0
    rejected = 0
    loaded = 0
    for line in lines:
        
        try:
            record = parse_product.parse_product(line)
        
        except ValueError as e:
            rejected += 1
            print(f"Bad number: {e}")
        except IndexError as e:
            rejected += 1
            print(f"Missing field: {e}")
        else:   #an empty ID passes through without exceptions
            if record["product_id"] == "":
                rejected += 1
            else:
                products_list.append(record)
                loaded += 1
        finally:
            processed += 1
    
    return products_list, {
        "processed":processed,
        "loaded":loaded,
        "rejected":rejected
    }


def print_report(products, stats):
    total = 0
    print("Stats summary:")
    for k, v in stats.items():
        print(k,v)
    if len(products) == 0:
        print("No valid products loaded")
    for product in products:
        print(product)
        total += product["price"] * product["quantity"]
    print(f"Total inventory value: {total:.2f}")

if __name__ == "__main__":    
    try:
        products, stats = load_inventory(lines)
        print_report(products, stats)
    except Exception as e:
        print(f"Something went wrong: {e}")