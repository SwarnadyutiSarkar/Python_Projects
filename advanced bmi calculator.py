import tkinter as tk

def calculate_bmi():
    height = float(height_entry.get()) / 100
    weight = float(weight_entry.get())
    bmi = weight / (height ** 2)
    result_label.config(text=f"BMI: {bmi:.2f}")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create labels and entries for height and weight
height_label = tk.Label(root, text="Height (cm):")
height_label.grid(row=0, column=0, padx=5, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=0, column=1, padx=5, pady=5)

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=1, column=0, padx=5, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, padx=5, pady=5)

# Create a button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()
