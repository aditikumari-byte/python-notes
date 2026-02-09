import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        a = float(entry1.get())
        b = float(entry2.get())

        if operation == "add":
            result = a + b
        elif operation == "sub":
            result = a - b
        elif operation == "mul":
            result = a * b
        elif operation == "div":
            if b == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = a / b

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")

# Inputs
tk.Label(root, text="First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Buttons
tk.Button(root, text="Add", width=15, command=lambda: calculate("add")).pack(pady=2)
tk.Button(root, text="Subtract", width=15, command=lambda: calculate("sub")).pack(pady=2)
tk.Button(root, text="Multiply", width=15, command=lambda: calculate("mul")).pack(pady=2)
tk.Button(root, text="Divide", width=15, command=lambda: calculate("div")).pack(pady=2)

# Result
result_label = tk.Label(root, text="Result:")
result_label.pack(pady=10)

root.mainloop()