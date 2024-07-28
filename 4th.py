import random
import tkinter as tk
from tkinter import messagebox

character1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
character2 = character1 + ['1','2','3','4','5','6','7','8','9']
character3 = character2 + ['!','`','#','@','$','%','^','&','*']

def generate_password():
    try:
        length = int(entry_length.get())
        complexity = int(entry_complexity.get())
        
        if complexity == 1:
            password_list = random.choices(character1, k=length)
        elif complexity == 2:
            password_list = random.choices(character2, k=length)
        elif complexity == 3:
            password_list = random.choices(character3, k=length)
        else:
            raise ValueError("Invalid complexity level")
        
        password = ''.join(password_list)
        messagebox.showinfo("Generated Password", f"The generated password is: {password}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter the length of the password:").grid(row=0, column=0, padx=10, pady=10)
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter the complexity (1, 2, or 3):").grid(row=1, column=0, padx=10, pady=10)
entry_complexity = tk.Entry(root)
entry_complexity.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Generate Password", command=generate_password).grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
