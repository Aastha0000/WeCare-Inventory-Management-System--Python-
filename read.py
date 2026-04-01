def read_products(filepath="products.txt"):
    """
    Reads product data from a file.
    Returns a list of product dictionaries.
    """
    products = []
    with open(filepath, "r") as file:
        for line in file:
            if line.strip():
                name, brand, qty, cost, country = line.strip().split(", ")
                products.append({
                    "name": name,
                    "brand": brand,
                    "qty": int(qty),
                    "cost_price": float(cost),
                    "country": country
                })
    return products
