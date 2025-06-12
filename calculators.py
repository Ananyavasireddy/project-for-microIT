import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        result_label.config(text=f"Result: {result:.2f}", fg="#00ff7f")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.title("🧮 Stylish Calculator")
root.geometry("350x300")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# Fonts and Colors
label_font = ("Arial", 12, "bold")
entry_font = ("Courier", 12)
button_font = ("Arial", 12, "bold")

# Title
tk.Label(root, text="Simple Calculator", font=("Arial", 16, "bold"),
         fg="#00ffcc", bg="#1e1e1e").pack(pady=10)

# Input Frame
input_frame = tk.Frame(root, bg="#1e1e1e")
input_frame.pack(pady=5)

tk.Label(input_frame, text="First Number:", font=label_font, fg="white", bg="#1e1e1e")\
    .grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry1 = tk.Entry(input_frame, font=entry_font, width=15, bg="#2e2e2e", fg="white", insertbackground='white')
entry1.grid(row=0, column=1, pady=5)

tk.Label(input_frame, text="Second Number:", font=label_font, fg="white", bg="#1e1e1e")\
    .grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry2 = tk.Entry(input_frame, font=entry_font, width=15, bg="#2e2e2e", fg="white", insertbackground='white')
entry2.grid(row=1, column=1, pady=5)

# Operation
tk.Label(input_frame, text="Operation:", font=label_font, fg="white", bg="#1e1e1e")\
    .grid(row=2, column=0, padx=10, pady=5, sticky="e")
operation_var = tk.StringVar(value='+')
operation_menu = tk.OptionMenu(input_frame, operation_var, '+', '-', '*', '/')
operation_menu.config(font=label_font, bg="#3e3e3e", fg="white", width=5)
operation_menu.grid(row=2, column=1, pady=5)

# Calculate Button
calculate_button = tk.Button(root, text="✅ Calculate", font=button_font,
                             command=calculate, bg="#00cc66", fg="white",
                             activebackground="#00ff88", relief=tk.FLAT)
calculate_button.pack(pady=15)

# Result
result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"),
                        fg="white", bg="#1e1e1e")
result_label.pack(pady=10)

# Start GUI
root.mainloop()