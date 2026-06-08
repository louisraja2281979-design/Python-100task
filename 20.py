import tkinter as tk
from tkinter import ttk
import markdown

def update_preview(event=None):
    md_text = text_input.get("1.0", tk.END)
    html = markdown.markdown(md_text)

    preview.config(state="normal")
    preview.delete("1.0", tk.END)
    preview.insert(tk.END, html)
    preview.config(state="disabled")

# Main Window
root = tk.Tk()
root.title("Markdown Previewer")
root.geometry("900x500")

# Left Frame - Markdown Input
left_frame = ttk.Frame(root)
left_frame.pack(side="left", fill="both", expand=True)

ttk.Label(left_frame, text="Markdown Input").pack()

text_input = tk.Text(left_frame, wrap="word")
text_input.pack(fill="both", expand=True, padx=5, pady=5)
text_input.bind("<KeyRelease>", update_preview)

# Right Frame - HTML Preview
right_frame = ttk.Frame(root)
right_frame.pack(side="right", fill="both", expand=True)

ttk.Label(right_frame, text="HTML Preview").pack()

preview = tk.Text(right_frame, wrap="word", state="disabled")
preview.pack(fill="both", expand=True, padx=5, pady=5)

# Sample Markdown
sample = """# Markdown Previewer

## Features
- Live Preview
- Simple UI
- Python Tkinter

**Bold Text**

*Italic Text*
"""

text_input.insert("1.0", sample)
update_preview()

root.mainloop()