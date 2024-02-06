import numpy as np
import tkinter as tk
from tkinter import ttk

def calculate_minimum_volume():
    c = float(concentration_entry.get())
    mdaa = int(mdaa_entry.get())
    desired_probability = float(probability_entry.get())
    
    v = 1.0
    while True:
        lambda_val = c * v / 1000
        prob = 1 - sum([(2.71828 ** -lambda_val) * (lambda_val ** i) / np.math.factorial(i) for i in range(mdaa)])
        if prob >= desired_probability:
            result_label.config(text=f"Minimum Sampling Volume: {v} L")
            break
        v += 1.0

# Create main window
root = tk.Tk()
root.title("Minimum Sampling Volume Calculator")

# Create labels and entries for user input
ttk.Label(root, text="MP Concentration (particles/m^3):").grid(row=0, column=0, padx=10, pady=5)
concentration_entry = ttk.Entry(root)
concentration_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Limit of detection (of particle):").grid(row=1, column=0, padx=10, pady=5)
mdaa_entry = ttk.Entry(root)
mdaa_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Desired Probability:").grid(row=2, column=0, padx=10, pady=5)
probability_entry = ttk.Entry(root)
probability_entry.grid(row=2, column=1, padx=10, pady=5)

# Create a button to calculate the minimum volume
calculate_button = ttk.Button(root, text="Calculate", command=calculate_minimum_volume)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create a label to display the result
result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()