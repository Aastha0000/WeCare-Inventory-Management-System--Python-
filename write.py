from datetime import datetime

def write_products(products, filepath="products.txt"):
    """
    Writes the list of product dictionaries to a text file.

    Parameters:
    - products (list): List of product dictionaries.
    - filepath (str): File path to write the product data to (default is 'products.txt').
    """
    with open(filepath, "w") as file:
        for p in products:
            line = f"{p['name']}, {p['brand']}, {p['qty']}, {p['cost_price']}, {p['country']}\n"
            file.write(line)

def generate_customer_invoice(customer_name, items, total_amount):
    """
    Generates and writes a customer invoice with 13% VAT to a text file.

    Parameters:
    - customer_name (str): Name of the customer.
    - items (list): List of sold item dictionaries with name, brand, qty, free, and total.
    - total_amount (float): Total price before VAT.
    """

    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"customer_invoice_{customer_name}_{now}.txt"

    vat = round(total_amount * 0.13, 2)
    grand_total = round(total_amount + vat, 2)

    with open(filename, "w") as f:
        f.write("WeCare Customer Invoice\n")
        f.write("-" * 30 + "\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Customer: {customer_name}\n\n")
        f.write("Items:\n")

        for item in items:
            f.write(f"- {item['name']} ({item['brand']}) | Qty: {item['qty']}, Free: {item['free']}, Total: ₹{item['total']}\n")

        f.write("\n" + "-" * 30 + "\n")
        f.write(f"Subtotal: rs.{total_amount:.2f}\n")
        f.write(f"VAT (13%): rs.{vat:.2f}\n")
        f.write(f"Grand Total: rs.{grand_total:.2f}\n")
        f.write("-" * 30 + "\n")
        f.write("Thank you for your purchase!\n")

def generate_supplier_invoice(vendor_name, items, total_amount):
    """
    Generates and writes a supplier invoice to a text file.

    Parameters:
    - vendor_name (str): Name of the supplier.
    - items (list): List of item dictionaries with name, brand, qty, and cost_price.
    - total_amount (float): Total cost of supplied items.
    """
    now = datetime.now().strftime("%Y%m%d")
    filename = f"supplier_invoice_{vendor_name}_{now}.txt"

    with open(filename, "w") as f:
        f.write("WeCare Supplier Invoice\n")
        f.write("-" * 30 + "\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write(f"Supplier: {vendor_name}\n\n")
        f.write("Supplied Items:\n")

        for item in items:
            f.write(f"- {item['name']} ({item['brand']}) | Qty: {item['qty']}, Cost Price: ₹{item['cost_price']}\n")

        f.write("\n" + "-" * 30 + "\n")
        f.write(f"Total Cost: ₹{total_amount:.2f}\n")
        f.write("Stock successfully updated.\n")
        f.write("-" * 30 + "\n")
