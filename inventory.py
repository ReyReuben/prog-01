from product import Product

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print("\nProduct added successfully!")

    def display_products(self):
        if not self.products:
            print("\nNo products in the inventory.")
        else:
            print("\nProducts in the inventory:")
            for product in self.products:
                print(product)

    def update_stock(self, product_id, quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.update_quantity(quantity)
                break
        else:
            print("\nProduct not found.")

    def calculate_total_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        print(f"\nTotal value of inventory: ${total_value:.2f}")
