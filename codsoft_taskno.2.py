import tkinter as tk
from tkinter import messagebox

# Function to perform operations
def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result = a + b
            output.set(f"Addition of {int(a)} and {int(b)} is {result}")
        elif operation == "Subtraction":
            result = a - b
            output.set(f"Subtraction of {int(a)} and {int(b)} is {result}")
        elif operation == "Multiplication":
            result = a * b
            output.set(f"Multiplication of {int(a)} and {int(b)} is {result}")
        elif operation == "Division":
            if b != 0:
                result = a / b
                output.set(f"Division of {int(a)} and {int(b)} is {result}")
            else:
                output.set("Error! Division by zero is not allowed.")
        elif operation == "Modulus":
            result = a % b
            output.set(f"Modulus of {int(a)} and {int(b)} is {result}")
        else:
            output.set("Please select an operation.")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# GUI Setup
root = tk.Tk()
root.title("Simple Arithmetic Calculator")
root.geometry("400x400")
root.config(bg="#f0f0f0")

tk.Label(root, text="******** Welcome! ********", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)
tk.Label(root, text="Enter the numbers:", font=("Arial", 12), bg="#f0f0f0").pack()

entry1 = tk.Entry(root, width=20, font=("Arial", 12))
entry1.pack(pady=5)
entry2 = tk.Entry(root, width=20, font=("Arial", 12))
entry2.pack(pady=5)

tk.Label(root, text="Choose the operation:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)

operation_var = tk.StringVar()
operation_menu = tk.OptionMenu(root, operation_var, "Addition", "Subtraction", "Multiplication", "Division", "Modulus")
operation_menu.config(width=20, font=("Arial", 11))
operation_menu.pack(pady=5)

tk.Button(root, text="Calculate", command=calculate, bg="#4CAF50", fg="white", font=("Arial", 12), width=15).pack(pady=15)

output = tk.StringVar()
tk.Label(root, textvariable=output, font=("Arial", 12), fg="blue", wraplength=350, justify="center", bg="#f0f0f0").pack(pady=10)

tk.Label(root, text="******** Thanks for using! ********", font=("Arial", 10, "italic"), bg="#f0f0f0").pack(pady=20)

root.mainloop()
