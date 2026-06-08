name = input("Enter Name: ")
email = input("Enter Email: ")
password = input("Enter Password: ")

errors = []

# Name validation
if len(name.strip()) == 0:
    errors.append("Name is required")

# Email validation
if "@" not in email or "." not in email:
    errors.append("Invalid email address")

# Password validation
if len(password) < 6:
    errors.append("Password must be at least 6 characters")

# Display result
if errors:
    print("\nValidation Errors:")
    for error in errors:
        print("-", error)
else:
    print("\nRegistration Successful!"