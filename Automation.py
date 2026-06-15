class WorkflowBuilder:
    def __init__(self):
        self.steps = []

    def add_step(self):
        step = input("Enter workflow step: ")
        self.steps.append(step)
        print("Step added successfully!")

    def view_workflow(self):
        if not self.steps:
            print("\nNo workflow steps found.")
            return

        print("\n=== WORKFLOW ===")
        for i, step in enumerate(self.steps, 1):
            print(f"{i}. {step}")

    def run_workflow(self):
        if not self.steps:
            print("\nNo workflow to execute.")
            return

        print("\nExecuting Workflow...")
        for step in self.steps:
            print(f"Running: {step}")
        print("Workflow Completed!")

    def menu(self):
        while True:
            print("\n=== AUTOMATION WORKFLOW BUILDER ===")
            print("1. Add Step")
            print("2. View Workflow")
            print("3. Run Workflow")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_step()
            elif choice == "2":
                self.view_workflow()
            elif choice == "3":
                self.run_workflow()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")

app = WorkflowBuilder()
app.menu()