from read import read_products
from write import write_products, generate_customer_invoice, generate_supplier_invoice

def display_products():
    """
    Shows all products with selling price (cost × 2).
    """
    products = read_products()
    print("\nAvailable Products (Selling Price = 200% markup):")
    for p in products:
        sell_price = p['cost_price'] * 2
        print(f"{p['name']} | Brand: {p['brand']} | Stock: {p['qty']} | Price: rs. {sell_price} | Origin: {p['country']}")

def handle_sale():
    """
    Handles selling a product.
    Updates quantity, applies offer, and generates invoice.
    """
    products = read_products()
    customer_name = input("Enter customer name: ")
    items_bought = []
    total_amount = 0

    while True:
        product_name = input("Enter product name to buy (or 'done' to finish): ")
        if product_name.lower() == 'done':
            break
        quantity = int(input("Enter quantity: "))
        for p in products:
            if p['name'].lower() == product_name.lower():
                free_items = quantity // 3
                if p['qty'] >= (quantity + free_items):
                    p['qty'] -= (quantity + free_items)
                    amount = quantity * p['cost_price'] * 2
                    items_bought.append({
                        "name": p['name'],
                        "brand": p['brand'],
                        "qty": quantity,
                        "free": free_items,
                        "total": amount
                    })
                    total_amount += amount
                else:
                    print("Not enough stock.")
                break
        else:
            print("Product not found.")

    write_products(products)
    generate_customer_invoice(customer_name, items_bought, total_amount)

def handle_restock():
    """
    Adds new products to the inventory and generates supplier invoice.
    """
    products = read_products()
    vendor = input("Enter vendor name: ")
    restocked_items = []
    total_cost = 0

    while True:
        name = input("Enter product name to restock (or 'done'): ")
        if name.lower() == 'done':
            break
        qty = int(input("Enter quantity: "))
        new_price = float(input("Enter new cost price: "))
        found = False
        for p in products:
            if p['name'].lower() == name.lower():
                p['qty'] += qty
                p['cost_price'] = new_price
                restocked_items.append({**p, "qty": qty})
                total_cost += qty * new_price
                found = True
                break
        if not found:
            brand = input("Enter brand: ")
            country = input("Enter country of origin: ")
            products.append({
                "name": name,
                "brand": brand,
                "qty": qty,
                "cost_price": new_price,
                "country": country
            })
            restocked_items.append({
                "name": name,
                "brand": brand,
                "qty": qty,
                "cost_price": new_price
            })
            total_cost += qty * new_price

    write_products(products)
    generate_supplier_invoice(vendor, restocked_items, total_cost)
    