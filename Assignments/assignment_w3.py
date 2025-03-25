import tkinter as tk
from tkinter import messagebox

def convert(x):
    x = float(x)
    y = (x*9/5)+32
    return y


def cal():
    a = entry.get()
    result = convert(a)
    result_label.config(text=f"Result: {result}")
    
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("200x300")


Label = tk.Label(root, text="input")
Label.grid(row=0, column=0, padx=5, pady=5)
entry = tk.Entry(root)
entry.grid(row=0, column=1)


calculate_button = tk.Button(root, text="Convert", command=cal)
calculate_button.grid(row=2, column=1, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=1, pady=10)

root.mainloop()