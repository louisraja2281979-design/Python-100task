import tkinter as tk
from tkinter import messagebox

# Vote counts
votes = {
    "Python": 0,
    "Java": 0,
    "C++": 0
}

def submit_vote():
    choice = selected_option.get()

    if choice == "":
        messagebox.showwarning("Warning", "Please select an option!")
        return

    votes[choice] += 1
    update_results()

    messagebox.showinfo("Success", f"You voted for {choice}")

def update_results():
    result_text.set(
        f"Python: {votes['Python']} votes\n"
        f"Java: {votes['Java']} votes\n"
        f"C++: {votes['C++']} votes"
    )

# Main Window
root = tk.Tk()
root.title("Poll Voting App")
root.geometry("400x350")

title = tk.Label(root, text="Favorite Programming Language",
                 font=("Arial", 14, "bold"))
title.pack(pady=10)

selected_option = tk.StringVar()

tk.Radiobutton(root, text="Python",
               variable=selected_option,
               value="Python").pack()

tk.Radiobutton(root, text="Java",
               variable=selected_option,
               value="Java").pack()

tk.Radiobutton(root, text="C++",
               variable=selected_option,
               value="C++").pack()

tk.Button(root, text="Submit Vote",
          command=submit_vote,
          bg="green", fg="white").pack(pady=10)

tk.Label(root, text="Results",
         font=("Arial", 12, "bold")).pack()

result_text = tk.StringVar()
result_text.set("Python: 0 votes\nJava: 0 votes\nC++: 0 votes")

tk.Label(root, textvariable=result_text,
         font=("Arial", 11)).pack(pady=10)

root.mainloop()