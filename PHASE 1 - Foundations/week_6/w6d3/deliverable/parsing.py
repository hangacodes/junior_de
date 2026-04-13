#Product parser
def parse_product(line):
    line = line.strip()
    parts = line.split("|")
    product_id = parts[0].strip()
    name = parts[1].strip()
    price = float(parts[2].strip())
    quantity = int(parts[3].strip())
    return {"product_id":product_id, "name":name, "price":price, "quantity":quantity}



if __name__ == "__main__":
    print("Doens't matter")