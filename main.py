from operation import display_products, handle_sale, handle_restock

def main():
    """
    Runs the menu of the WeCare system.
    Lets user view, sell, or restock products.
    """
    while True:
        print("\n--- WeCare Store Management ---")
        print("1. Show Products")
        print("2. Sell Product")
        print("3. Restock Product")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            display_products()
        elif choice == '2':
            handle_sale()
        elif choice == '3':
            handle_restock()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
