import tkinter as tk
from tkinter import messagebox

students = []

def create_student():
    name = name_entry.get()
    age = age_entry.get()

    if name and age:
        students.append({"name": name, "age": age})
        refresh_list()
        clear_fields()
    else:
        messagebox.showwarning("Input Error", "Enter all fields")

def read_student():
    try:
        index = student_list.curselection()[0]
        student = students[index]

        name_entry.delete(0, tk.END)
        name_entry.insert(0, student["name"])

        age_entry.delete(0, tk.END)
        age_entry.insert(0, student["age"])

    except IndexError:
        messagebox.showwarning("Selection Error", "Select a student")

def update_student():
    try:
        index = student_list.curselection()[0]

        students[index]["name"] = name_entry.get()
        students[index]["age"] = age_entry.get()

        refresh_list()
        clear_fields()

    except IndexError:
        messagebox.showwarning("Selection Error", "Select a student")

def delete_student():
    try:
        index = student_list.curselection()[0]
        students.pop(index)

        refresh_list()
        clear_fields()

    except IndexError:
        messagebox.showwarning("Selection Error", "Select a student")

def refresh_list():
    student_list.delete(0, tk.END)

    for student in students:
        student_list.insert(
            tk.END,
            f"{student['name']} - Age: {student['age']}"
        )

def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

# GUI
root = tk.Tk()
root.title("Student Record CRUD App")
root.geometry("500x400")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root, width=30)
age_entry.pack(pady=5)

tk.Button(root, text="Create", command=create_student).pack(pady=2)
tk.Button(root, text="Read", command=read_student).pack(pady=2)
tk.Button(root, text="Update", command=update_student).pack(pady=2)
tk.Button(root, text="Delete", command=delete_student).pack(pady=2)

student_list = tk.Listbox(root, width=50, height=10)
student_list.pack(pady=10)

root.mainloop()