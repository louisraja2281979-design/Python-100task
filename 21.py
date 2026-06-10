import tkinter as tk
from tkinter import messagebox

def generate_resume():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    skills = skills_text.get("1.0", tk.END).strip()
    education = education_text.get("1.0", tk.END).strip()
    experience = experience_text.get("1.0", tk.END).strip()

    if not name:
        messagebox.showerror("Error", "Please enter your name")
        return

    resume = f"""
==============================
          RESUME
==============================

Name: {name}
Email: {email}
Phone: {phone}

SKILLS
------
{skills}

EDUCATION
---------
{education}

EXPERIENCE
----------
{experience}
"""

    filename = f"{name.replace(' ', '_')}_Resume.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(resume)

    messagebox.showinfo("Success", f"Resume saved as {filename}")

# Main Window
root = tk.Tk()
root.title("Resume Builder")
root.geometry("600x700")

# Name
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=50)
name_entry.pack()

# Email
tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=50)
email_entry.pack()

# Phone
tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root, width=50)
phone_entry.pack()

# Skills
tk.Label(root, text="Skills").pack()
skills_text = tk.Text(root, height=5, width=60)
skills_text.pack()

# Education
tk.Label(root, text="Education").pack()
education_text = tk.Text(root, height=5, width=60)
education_text.pack()

# Experience
tk.Label(root, text="Experience").pack()
experience_text = tk.Text(root, height=5, width=60)
experience_text.pack()

# Button
tk.Button(root, text="Generate Resume",
          command=generate_resume,
          bg="green", fg="white").pack(pady=10)

root.mainloop()