import tkinter as tk
from tkinter import filedialog, messagebox

def save_note():
    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file:
        with open(file, "w") as f:
            f.write(text_area.get(1.0, tk.END))
        messagebox.showinfo("Success", "Note saved successfully!")

def open_note():
    file = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )

    if file:
        with open(file, "r") as f:
            content = f.read()

        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, content)

root = tk.Tk()
root.title("Notes App")
root.geometry("600x400")

frame = tk.Frame(root)
frame.pack(pady=5)

open_btn = tk.Button(frame, text="Open Note", command=open_note)
open_btn.pack(side=tk.LEFT, padx=5)

save_btn = tk.Button(frame, text="Save Note", command=save_note)
save_btn.pack(side=tk.LEFT, padx=5)

text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
text_area.pack(expand=True, fill="both", padx=10, pady=10)

root.mainloop()