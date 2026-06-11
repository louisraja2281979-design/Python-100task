class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({
            "product": product,
            "quantity": quantity
        })
        print(f"{quantity} x {product.name} added to cart.")

    def remove_item(self, product_name):
        for item in self.items:
            if item["product"].name.lower() == product_name.lower():
                self.items.remove(item)
                print(f"{product_name} removed from cart.")
                return
        print("Product not found.")

    def view_cart(self):
        if not self.items:
            print("\nCart is empty.")
            return

        print("\n----- Shopping Cart -----")
        total = 0

        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            subtotal = product.price * quantity

            print(
                f"{product.name} | ₹{product.price} x {quantity} = ₹{subtotal}"
            )

            total += subtotal

        print("-------------------------")
        print(f"Total Amount: ₹{total}")

    def checkout(self):
        total = 0

        for item in self.items:
            total += item["product"].price * item["quantity"]

        print("\n===== Checkout =====")
        print(f"Total Amount: ₹{total}")
        print("Thank you for shopping!")
        self.items.clear()


# Products
p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 800)
p3 = Product("Keyboard", 1500)

# Cart
cart = ShoppingCart()

while True:
    print("\n1. Add Laptop")
    print("2. Add Mouse")
    print("3. Add Keyboard")
    print("4. View Cart")
    print("5. Remove Item")
    print("6. Checkout")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        qty = int(input("Quantity: "))
        cart.add_item(p1, qty)

    elif choice == "2":
        qty = int(input("Quantity: "))
        cart.add_item(p2, qty)

    elif choice == "3":
        qty = int(input("Quantity: "))
        cart.add_item(p3, qty)

    elif choice == "4":
        cart.view_cart()

    elif choice == "5":
        name = input("Enter product name: ")
        cart.remove_item(name)

    elif choice == "6":
        cart.checkout()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")