import tkinter as tk
import sys

script_path = sys.argv[0]
# Create a function to perform arithmetic operations
def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create a function to add characters to the input field
def add_character(character):
    entry.insert(tk.END, character)

# Create a function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry field
entry = tk.Entry(root, width=25)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for numbers and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, command=lambda b=button: add_character(b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create a clear button
tk.Button(root, text="C", width=5, height=2, command=clear).grid(row=5, column=0)

# Run the application
root.mainloop()
