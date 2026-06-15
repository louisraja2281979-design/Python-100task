employees = []
products = []
sales = []

while True:
    print("\n===== ERP MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Add Product")
    print("4. View Products")
    print("5. Record Sale")
    print("6. View Sales")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        name = input("Employee Name: ")
        department = input("Department: ")
        employees.append({"name": name, "department": department})
        print("Employee Added Successfully!")

    elif choice == "2":
        print("\n--- Employees ---")
        if not employees:
            print("No Employees Found!")
        else:
            for emp in employees:
                print(f"Name: {emp['name']} | Department: {emp['department']}")

    elif choice == "3":
        name = input("Product Name: ")
        price = float(input("Product Price: "))
        products.append({"name": name, "price": price})
        print("Product Added Successfully!")

    elif choice == "4":
        print("\n--- Products ---")
        if not products:
            print("No Products Found!")
        else:
            for product in products:
                print(f"Product: {product['name']} | Price: ₹{product['price']}")

    elif choice == "5":
        product = input("Product Name: ")
        qty = int(input("Quantity: "))
        sales.append({"product": product, "qty": qty})
        print("Sale Recorded Successfully!")

    elif choice == "6":
        print("\n--- Sales ---")
        if not sales:
            print("No Sales Found!")
        else:
            for sale in sales:
                print(f"Product: {sale['product']} | Quantity: {sale['qty']}")

    elif choice == "7":
        print("Thank You for Using ERP System!")
        break

    else:
        print("Invalid Choice!")