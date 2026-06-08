import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task!")

# Main Window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

# Title
title = tk.Label(root, text="My To-Do List", font=("Arial", 16))
title.pack(pady=10)

# Entry
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Add Button
add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

# Task List
task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)

# Delete Button
delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)

root.mainloop()