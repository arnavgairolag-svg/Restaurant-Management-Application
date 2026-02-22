import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import os
from datetime import datetime

# simple price list
price_menu = {
    "Breakfast": 15,
    "Lunch": 18,
    "Dinner": 22,
    "Drinks": 8
}

# make sure order file exists
if not os.path.exists("Data.txt"):
    with open("Data.txt", "w") as f:
        f.write("0")

# small helper so it doesn’t crash
def get_number(entry):
    value = entry.get().strip()
    if value == "":
        return 0
    if not value.isdigit():
        messagebox.showerror("Invalid Input 😅", "Please enter whole numbers only.")
        raise ValueError
    return int(value)

# clears cost section only
def clear_bill():
    for entry in [Cost, Tax, Total]:
        entry.config(state="normal")
        entry.delete(0, tk.END)
        entry.config(state="readonly")

# receipt popup
def show_receipt(order_no, items, cost, tax, total):
    receipt = Toplevel(resturaunt)
    receipt.geometry("420x500")
    receipt.title("🧾 Receipt")
    receipt.configure(bg="#f8f5f2")

    title = tk.Label(
        receipt,
        text="🧾 Order Receipt",
        bg="#f8f5f2",
        fg="#344e41",
        font=("Segoe UI", 18, "bold")
    )
    title.pack(pady=15)

    box = tk.Frame(receipt, bg="white", bd=1, relief="solid")
    box.pack(padx=20, pady=10, fill="both", expand=True)

    content = tk.Text(
        box,
        bg="white",
        fg="#2f3e46",
        font=("Consolas", 11),
        bd=0
    )
    content.pack(padx=15, pady=15, fill="both", expand=True)

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    receipt_text = f"""
Order Number: {order_no}
Date: {now}
----------------------------------------
Breakfast  x{items[0]}
Lunch      x{items[1]}
Dinner     x{items[2]}
Drinks     x{items[3]}
----------------------------------------
Subtotal:   ${cost:.2f}
Tax (30%):  ${tax:.2f}
----------------------------------------
TOTAL:      ${total:.2f}
----------------------------------------
Thank you for dining with us 🌿
"""

    content.insert("1.0", receipt_text)
    content.config(state="disabled")

    tk.Button(
        receipt,
        text="Close",
        bg="#a3b18a",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        command=receipt.destroy
    ).pack(pady=15)

# main calculation
def calculate_total():
    try:
        b = get_number(Breakfast)
        l = get_number(Lunch)
        d = get_number(Dinner)
        dr = get_number(Drinks)
    except ValueError:
        return

    breakfast_bill = b * price_menu["Breakfast"]
    lunch_bill = l * price_menu["Lunch"]
    dinner_bill = d * price_menu["Dinner"]
    drinks_bill = dr * price_menu["Drinks"]

    with open("Data.txt", "r") as file:
        current_order = int(file.read())

    new_order = current_order + 1

    with open("Data.txt", "w") as file:
        file.write(str(new_order))

    Number.config(state="normal")
    Number.delete(0, tk.END)
    Number.insert(0, str(new_order))
    Number.config(state="readonly")

    subtotal = breakfast_bill + lunch_bill + dinner_bill + drinks_bill
    tax = round(subtotal * 0.30, 2)
    total = round(subtotal + tax, 2)

    clear_bill()

    Cost.config(state="normal")
    Cost.insert(0, f"{subtotal:.2f}")
    Cost.config(state="readonly")

    Tax.config(state="normal")
    Tax.insert(0, f"{tax:.2f}")
    Tax.config(state="readonly")

    Total.config(state="normal")
    Total.insert(0, f"{total:.2f}")
    Total.config(state="readonly")

    show_receipt(new_order, [b, l, d, dr], subtotal, tax, total)

# reset everything
def restart():
    Number.config(state="normal")
    Number.delete(0, tk.END)
    Number.config(state="readonly")

    for entry in [Breakfast, Lunch, Dinner, Drinks]:
        entry.delete(0, tk.END)

    clear_bill()

# price popup
def show_prices():
    prices = Toplevel(resturaunt)
    prices.geometry("350x300")
    prices.title("Menu Prices")
    prices.configure(bg="#f8f5f2")

    tk.Label(
        prices,
        text="🍽️ Menu Prices",
        bg="#f8f5f2",
        fg="#344e41",
        font=("Segoe UI", 16, "bold")
    ).pack(pady=15)

    tree = ttk.Treeview(prices, columns=("Item", "Price"), show="headings")
    tree.pack(pady=10)

    tree.heading("Item", text="Item")
    tree.heading("Price", text="Price ($)")

    for item, price in price_menu.items():
        tree.insert("", "end", values=(item, price))

    tk.Button(
        prices,
        text="Close",
        bg="#a3b18a",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        command=prices.destroy
    ).pack(pady=10)

# ---------------- MAIN WINDOW ----------------

resturaunt = tk.Tk()
resturaunt.geometry("760x560")
resturaunt.title("Restaurant Management System")
resturaunt.configure(bg="#f0ead2")

title = tk.Label(
    resturaunt,
    text="🍽️ Restaurant Management System",
    bg="#f0ead2",
    fg="#344e41",
    font=("Segoe UI", 24, "bold")
)
title.pack(pady=25)

order_frame = tk.Frame(resturaunt, bg="#f0ead2")
order_frame.pack(pady=10)

labels = ["🧾 Order No:", "🍳 Breakfast:", "🥪 Lunch:", "🍝 Dinner:", "🥤 Drinks:"]
entries = []

for i, text in enumerate(labels):
    tk.Label(order_frame, text=text, bg="#f0ead2",
             fg="#3a5a40", font=("Segoe UI", 12)).grid(row=i, column=0, pady=8, sticky="e")

    entry = tk.Entry(order_frame, width=20, font=("Segoe UI", 11))
    entry.grid(row=i, column=1, padx=10)

    entries.append(entry)

Number, Breakfast, Lunch, Dinner, Drinks = entries
Number.config(state="readonly")

bill_frame = tk.Frame(resturaunt, bg="#f0ead2")
bill_frame.pack(pady=25)

bill_labels = ["💰 Subtotal:", "🧾 Tax (30%):", "💵 Total:"]
bill_entries = []

for i, text in enumerate(bill_labels):
    tk.Label(bill_frame, text=text, bg="#f0ead2",
             fg="#3a5a40", font=("Segoe UI", 12)).grid(row=i, column=0, pady=8, sticky="e")

    entry = tk.Entry(bill_frame, width=20, font=("Segoe UI", 11), state="readonly")
    entry.grid(row=i, column=1, padx=10)

    bill_entries.append(entry)

Cost, Tax, Total = bill_entries

button_frame = tk.Frame(resturaunt, bg="#f0ead2")
button_frame.pack(pady=30)

buttons = [
    ("📋 Prices", "#588157", show_prices),
    ("🧮 Calculate", "#344e41", calculate_total),
    ("🔄 Restart", "#6c757d", restart),
    ("🚪 Exit", "#bc4749", resturaunt.destroy)
]

for i, (text, color, cmd) in enumerate(buttons):
    tk.Button(
        button_frame,
        text=text,
        width=15,
        bg=color,
        fg="white",
        font=("Segoe UI", 11, "bold"),
        command=cmd
    ).grid(row=0, column=i, padx=12)

resturaunt.mainloop()
