# Attendance Management System

attendance = {}

while True:
    print("\n--- Attendance Management System ---")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        status = input("Present (P) / Absent (A): ").upper()

        if status in ["P", "A"]:
            attendance[name] = status
            print("Attendance marked successfully!")
        else:
            print("Invalid status!")

    elif choice == "2":
        print("\nAttendance Report")
        print("-----------------")

        if len(attendance) == 0:
            print("No records found.")
        else:
            for name, status in attendance.items():
                print(f"{name} : {status}")

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid choice!")