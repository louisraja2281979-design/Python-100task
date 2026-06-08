import tkinter as tk
from tkinter import messagebox

rates = {
    "USD": 1.0,
    "INR": 83.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 156.0
}

def convert():
    try:
        amount = float(amount_entry.get())

        from_currency = from_var.get()
        to_currency = to_var.get()

        usd_amount = amount / rates[from_currency]
        converted = usd_amount * rates[to_currency]

        result_label.config(
            text=f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}"
        )

    except ValueError:
        messagebox.showerror("Error", "Enter a valid amount")

root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x250")

tk.Label(root, text="Amount").pack(pady=5)

amount_entry = tk.Entry(root)
amount_entry.pack()

currencies = list(rates.keys())

from_var = tk.StringVar(value="USD")
to_var = tk.StringVar(value="INR")

tk.Label(root, text="From Currency").pack(pady=5)
tk.OptionMenu(root, from_var, *currencies).pack()

tk.Label(root, text="To Currency").pack(pady=5)
tk.OptionMenu(root, to_var, *currencies).pack()

tk.Button(
    root,
    text="Convert",
    command=convert
).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()