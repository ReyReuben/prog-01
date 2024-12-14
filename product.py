class Product:
    def __init__(self, product_id, name, product_description, price, quantity):
        self.product_id = product_id
        self.name = name
        self.product_description = product_description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Description: {self.product_description}, Price: ${self.price}, Quantity: {self.quantity}"

    def update_quantity(self, quantity):
        self.quantity += quantity
        print(f"\nUpdated quantity for {self.name} to {self.quantity}.")
