import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)

def on_button_click(event):
    button_text = event.widget.cget("text")
    if button_text == "=":
        try:
            expression = entry.get()
            result = evaluate_expression(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", str(e))
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)
root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button_text in buttons:
    button = tk.Button(root, text=button_text, font=('Arial', 18), height=2, width=4)
    button.grid(row=row_val, column=col_val)
    button.bind("<Button-1>", on_button_click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
