from inventory import Inventory
from product import Product

def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management Menu:")
        print("1. Add Product")
        print("2. Display Products")
        print("3. Update Product Stock")
        print("4. Calculate Total Value of Inventory")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            product_description = input("Enter product description: ")
            price = float(input("Enter price per unit: "))
            quantity = int(input("Enter quantity in stock: "))
            product = Product(product_id, name, product_description, price, quantity)
            inventory.add_product(product)
        elif choice == '2':
            inventory.display_products()
        elif choice == '3':
            product_id = input("Enter product ID to update: ")
            quantity = int(input("Enter quantity to add (positive number) or subtract (negative number): "))
            inventory.update_stock(product_id, quantity)
        elif choice == '4':
            inventory.calculate_total_value()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
