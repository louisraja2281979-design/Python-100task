from tkinter import *

def register():
    print("Registration Successful")

root = Tk()
root.title("Registration Form")
root.geometry("300x300")

Label(root, text="Registration Form", font=("Arial", 14)).pack(pady=10)

Label(root, text="Name").pack()
Entry(root).pack()

Label(root, text="Email").pack()
Entry(root).pack()

Label(root, text="Password").pack()
Entry(root, show="*").pack()

Label(root, text="Phone").pack()
Entry(root).pack()

Button(root, text="Register", command=register).pack(pady=10)

root.mainloop()