# Recipe Book App

recipes = {}

while True:
    print("\n===== Recipe Book App =====")
    print("1. Add Recipe")
    print("2. View All Recipes")
    print("3. Search Recipe")
    print("4. Delete Recipe")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter recipe name: ")
        ingredients = input("Enter ingredients (comma-separated): ")
        instructions = input("Enter cooking instructions: ")

        recipes[name] = {
            "ingredients": ingredients,
            "instructions": instructions
        }

        print(f"'{name}' recipe added successfully!")

    elif choice == "2":
        if not recipes:
            print("No recipes found.")
        else:
            print("\n--- All Recipes ---")
            for name, details in recipes.items():
                print(f"\nRecipe: {name}")
                print(f"Ingredients: {details['ingredients']}")
                print(f"Instructions: {details['instructions']}")

    elif choice == "3":
        name = input("Enter recipe name to search: ")

        if name in recipes:
            print(f"\nRecipe: {name}")
            print(f"Ingredients: {recipes[name]['ingredients']}")
            print(f"Instructions: {recipes[name]['instructions']}")
        else:
            print("Recipe not found.")

    elif choice == "4":
        name = input("Enter recipe name to delete: ")

        if name in recipes:
            del recipes[name]
            print("Recipe deleted successfully!")
        else:
            print("Recipe not found.")

    elif choice == "5":
        print("Exiting Recipe Book App...")
        break

    else:
        print("Invalid choice. Please try again.")