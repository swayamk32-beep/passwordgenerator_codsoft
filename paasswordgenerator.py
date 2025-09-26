import tkinter as tk
import random, string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            password_var.set("Enter valid length")
            return
        
        chars = ""
        if letters_var.get():
            chars += string.ascii_letters
        if numbers_var.get():
            chars += string.digits
        if symbols_var.get():
            chars += string.punctuation
        
        if chars == "":
            password_var.set("Select at least one option")
            return
        
        password = "".join(random.choice(chars) for _ in range(length))
        password_var.set(password)
    except ValueError:
        password_var.set("Enter a number")

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.configure(bg="#222")

tk.Label(root, text="🔐 Password Generator", font=("Arial", 18, "bold"), bg="#222", fg="white").pack(pady=10)

tk.Label(root, text="Enter password length:", font=("Arial", 12), bg="#222", fg="white").pack()
length_entry = tk.Entry(root, font=("Arial", 14), justify="center")
length_entry.pack(pady=5)

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters (A-Z, a-z)", variable=letters_var, font=("Arial", 12),
               bg="#222", fg="white", selectcolor="#444").pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Include Numbers (0-9)", variable=numbers_var, font=("Arial", 12),
               bg="#222", fg="white", selectcolor="#444").pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Include Symbols (!@#...)", variable=symbols_var, font=("Arial", 12),
               bg="#222", fg="white", selectcolor="#444").pack(anchor="w", padx=60)

tk.Button(root, text="Generate Password", font=("Arial", 14), bg="#0A9396", fg="white",
          command=generate_password).pack(pady=15)

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 14), width=30, justify="center", state="readonly")
password_entry.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), bg="#BB3E03", fg="white",
          command=copy_password).pack(pady=10)

root.mainloop()
