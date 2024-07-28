import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        operator = combo_operator.get()
        result = switch(operator, a, b)
        label_result.config(text=f"The result of the mathematical operation is: {result}", font=("Helvetica", 16))
    except ValueError:
        label_result.config(text="Please enter valid numbers", font=("Helvetica", 16))

def switch(c, a, b):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '/':
        return a / b
    elif c == '*':
        return a * b
    else:
        return "Invalid"

root = tk.Tk()
root.title("Calculator")

label_a = tk.Label(root, text="Please input your first number:")
label_a.pack(pady=5)

entry_a = tk.Entry(root)
entry_a.pack(pady=5)

label_b = tk.Label(root, text="Please input your second number:")
label_b.pack(pady=5)

entry_b = tk.Entry(root)
entry_b.pack(pady=5)

label_operator = tk.Label(root, text="Please Enter the arithmetic operator (+, -, /, *):")
label_operator.pack(pady=5)

combo_operator = ttk.Combobox(root, values=['+', '-', '/', '*'])
combo_operator.pack(pady=5)

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 16))
label_result.pack(pady=10)

root.mainloop()
