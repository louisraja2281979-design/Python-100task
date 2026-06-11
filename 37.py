class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class FoodOrderingApp:
    def __init__(self):
        self.menu = [
            FoodItem("Pizza", 250),
            FoodItem("Burger", 120),
            FoodItem("Pasta", 180),
            FoodItem("Sandwich", 100),
            FoodItem("French Fries", 90),
            FoodItem("Cold Drink", 50)
        ]
        self.cart = []

    def show_menu(self):
        print("\n===== FOOD MENU =====")
        for i, item in enumerate(self.menu, start=1):
            print(f"{i}. {item.name} - ₹{item.price}")

    def add_to_cart(self):
        self.show_menu()

        try:
            choice = int(input("\nEnter item number: "))
            quantity = int(input("Enter quantity: "))

            if 1 <= choice <= len(self.menu):
                item = self.menu[choice - 1]
                self.cart.append((item, quantity))
                print(f"{quantity} x {item.name} added to cart.")
            else:
                print("Invalid item number.")

        except ValueError:
            print("Please enter valid numbers.")

    def view_cart(self):
        if not self.cart:
            print("\nCart is empty.")
            return

        print("\n===== YOUR CART =====")
        total = 0

        for item, quantity in self.cart:
            subtotal = item.price * quantity
            total += subtotal

            print(
                f"{item.name} x {quantity} = ₹{subtotal}"
            )

        print("--------------------")
        print(f"Total Amount: ₹{total}")

    def checkout(self):
        if not self.cart:
            print("\nCart is empty.")
            return

        total = sum(
            item.price * quantity
            for item, quantity in self.cart
        )

        print("\n===== BILL =====")
        self.view_cart()
        print("\nOrder Placed Successfully!")
        print("Thank you for ordering.")
        self.cart.clear()

    def run(self):
        while True:
            print("\n===== ONLINE FOOD ORDERING APP =====")
            print("1. View Menu")
            print("2. Add to Cart")
            print("3. View Cart")
            print("4. Checkout")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.show_menu()

            elif choice == "2":
                self.add_to_cart()

            elif choice == "3":
                self.view_cart()

            elif choice == "4":
                self.checkout()

            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    app = FoodOrderingApp()
    app.run()