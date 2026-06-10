# Daily Expense Tracker

expenses = []

while True:
    print("\n===== Daily Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item = input("Enter expense name: ")
        amount = float(input("Enter amount: ₹"))
        expenses.append((item, amount))
        print("Expense added successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nExpenses:")
            for i, (item, amount) in enumerate(expenses, start=1):
                print(f"{i}. {item} - ₹{amount:.2f}")

    elif choice == "3":
        total = sum(amount for item, amount in expenses)
        print(f"\nTotal Expense: ₹{total:.2f}")

    elif choice == "4":
        print("Thank you for using Daily Expense Tracker!")
        break

    else:
        print("Invalid choice! Please enter 1-4.")