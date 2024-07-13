import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Database setup
conn = sqlite3.connect('indian_food_bills.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS bills
             (id INTEGER PRIMARY KEY, item TEXT, quantity INTEGER, price REAL, total REAL)''')
conn.commit()

# Main application window
root = tk.Tk()
root.title("Advanced Bill Management System")
root.geometry("1000x700")
root.configure(bg="#282c34")

# Colors
bg_color = "#282c34"
header_color = "#61dafb"
button_colors = ["#FF5733", "#3498db", "#FFC300", "#FF69B4", "#2c3e50", "#ecf0f1", "#9b59b6", "#2ecc71"]
menu_bg_color = "#27ae60"  # Green background for menu items

# Header Label
header = tk.Label(root, text="Advanced Bill Management System", bg=header_color, fg="white", font=("Helvetica", 24))
header.grid(row=0, column=0, columnspan=4, pady=20, sticky="ew")

# Food options with emojis
food_items = [
    ("🍗 Chicken Curry", 350),
    ("🧀 Paneer Tikka", 250),
    ("🍚 Biryani", 200),
    ("🥞 Masala Dosa", 100),
    ("🍲 Chole Bhature", 150),
    ("🍮 Gulab Jamun", 50),
    ("🥟 Samosa", 20),
    ("🍥 Rasgulla", 50),
    ("🍲 Dal Makhani", 180),
    ("🍞 Naan", 30),
    ("🍛 Kofta", 220),
    ("🥘 Pav Bhaji", 120)
]

food_dict = {item[0]: item[1] for item in food_items}

# Frame for food items
items_frame = tk.Frame(root, bg=bg_color)
items_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Create radio buttons and quantity adjustment buttons for food items
item_vars = {}
quantity_vars = {}
for item, price in food_items:
    item_var = tk.IntVar(value=0)
    item_vars[item] = item_var
    
    # Horizontal frame for each item
    item_frame = tk.Frame(items_frame, bg=menu_bg_color)  # Green background for menu items
    item_frame.pack(anchor='w', padx=10, pady=5, fill='x')

    # Radio button for item selection
    rb = tk.Radiobutton(item_frame, text=f"{item} - ₹{price}", variable=item_var, value=1, bg=menu_bg_color, fg="white", font=("Helvetica", 12))
    rb.pack(side=tk.LEFT)

    # Quantity adjustment buttons
    quantity_var = tk.IntVar(value=0)  # Start with quantity 0
    quantity_vars[item] = quantity_var
    
    minus_button = tk.Button(item_frame, text="-", command=lambda i=item: decrease_quantity(i), font=("Helvetica", 10), width=2, bg=button_colors[0], fg="white")
    minus_button.pack(side=tk.LEFT, padx=(10, 2))
    
    quantity_label = tk.Label(item_frame, textvariable=quantity_var, bg=menu_bg_color, fg="white", font=("Helvetica", 12))
    quantity_label.pack(side=tk.LEFT, padx=2)
    
    plus_button = tk.Button(item_frame, text="+", command=lambda i=item: increase_quantity(i), font=("Helvetica", 10), width=2, bg=button_colors[1], fg="white")
    plus_button.pack(side=tk.LEFT, padx=(2, 10))

# Functions to adjust quantity
def increase_quantity(item):
    quantity_vars[item].set(quantity_vars[item].get() + 1)

def decrease_quantity(item):
    current_quantity = quantity_vars[item].get()
    if current_quantity > 0:
        quantity_vars[item].set(current_quantity - 1)
    else:
        messagebox.showwarning("Warning", "Minimum quantity reached (0)")

# Treeview for displaying bills
columns = ('#1', '#2', '#3', '#4')
tree = ttk.Treeview(root, columns=columns, show='headings', height=10)
tree.heading('#1', text='Item')
tree.heading('#2', text='Quantity')
tree.heading('#3', text='Price (INR)')
tree.heading('#4', text='Total (INR)')
tree.grid(row=8, column=0, columnspan=4, pady=20, padx=20)

# Functions
def add_items():
    for item, item_var in item_vars.items():
        if item_var.get() == 1:
            try:
                quantity = quantity_vars[item].get()
                price = food_dict[item]
                total = quantity * price
                c.execute("INSERT INTO bills (item, quantity, price, total) VALUES (?, ?, ?, ?)", (item, quantity, price, total))
                conn.commit()
            except ValueError:
                messagebox.showerror("Error", f"Please enter a valid quantity for {item}")
    messagebox.showinfo("Success", "Items added to bill successfully!")
    load_bills()
    clear_entries()

def clear_entries():
    for item_var in item_vars.values():
        item_var.set(0)
    for quantity_var in quantity_vars.values():
        quantity_var.set(0)  # Reset quantity to 0 after clearing

def load_bills():
    for row in tree.get_children():
        tree.delete(row)
    c.execute("SELECT item, quantity, price, total FROM bills")
    rows = c.fetchall()
    for row in rows:
        tree.insert('', tk.END, values=row)
    calculate_grand_total()

def calculate_grand_total():
    c.execute("SELECT SUM(total) FROM bills")
    grand_total = c.fetchone()[0]
    if grand_total:
        grand_total_label.config(text=f"Grand Total: ₹{grand_total:.2f}")
    else:
        grand_total_label.config(text="Grand Total: ₹0.00")

def generate_receipt():
    receipt_window = tk.Toplevel(root)
    receipt_window.title("Receipt")
    receipt_text = tk.Text(receipt_window, wrap='word', fg="white")
    receipt_text.pack(expand=1, fill='both')
    
    # Hotel name at the top in bold, red font
    hotel_name = "Hotel Paradise"
    receipt_text.insert(tk.END, hotel_name + "\n\n", "hotel_name")
    receipt_text.tag_configure("hotel_name", font=("Helvetica", 16, "bold"), foreground="red")
    
    receipt_text.insert(tk.END, "Item\tQuantity\tPrice (INR)\tTotal (INR)\n")
    receipt_text.insert(tk.END, "-"*60 + "\n")
    
    c.execute("SELECT item, quantity, price, total FROM bills")
    rows = c.fetchall()
    
    # Iterate over rows and insert them into the receipt text with green background
    for row in rows:
        receipt_text.insert(tk.END, f"{row[0]}\t{row[1]}\t₹{row[2]:.2f}\t₹{row[3]:.2f}\n", "item_row")
        receipt_text.tag_configure("item_row", background="green", foreground="white", font=("Helvetica", 12))
    
    receipt_text.insert(tk.END, "-"*60 + "\n")
    
    c.execute("SELECT SUM(total) FROM bills")
    grand_total = c.fetchone()[0]
    
    if grand_total:
        receipt_text.insert(tk.END, f"Your total bill is: ₹{grand_total:.2f}\n")
    else:
        receipt_text.insert(tk.END, "Your total bill is: ₹0.00\n")
    
    receipt_text.insert(tk.END, "\nThanks for visiting! 😊")

# Buttons
buttons = [
    ("Add Items", add_items, button_colors[2]),
    ("Load Bills", load_bills, button_colors[3]),
    ("Generate Bill", generate_receipt, button_colors[4]),
]
for i, (text, command, color) in enumerate(buttons):
    tk.Button(root, text=text, command=command, bg=color, fg="white", font=("Helvetica", 12)).grid(row=5+i//2, column=i%2, padx=10, pady=10, sticky="ew")

# Grand Total Label
grand_total_label = tk.Label(root, text="Grand Total: ₹0.00", bg=header_color, fg="white", font=("Helvetica", 16))
grand_total_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Load existing bills on startup
load_bills()
root.mainloop()

# Close the database connection
conn.close()
