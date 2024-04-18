import tkinter as tk
from tkinter import ttk, messagebox

class UnitConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")

        # Create comboboxes for unit selection
        self.from_unit_combo = ttk.Combobox(root, values=["Meter", "Foot", "Inch", "Kilogram", "Pound", "Celsius", "Fahrenheit", "Liter", "Gallon"])
        self.from_unit_combo.set("Meter")
        self.from_unit_combo.pack(pady=10)

        self.to_unit_combo = ttk.Combobox(root, values=["Meter", "Foot", "Inch", "Kilogram", "Pound", "Celsius", "Fahrenheit", "Liter", "Gallon"])
        self.to_unit_combo.set("Foot")
        self.to_unit_combo.pack(pady=10)

        # Create entry for value to convert
        ttk.Label(root, text="Enter Value:").pack(pady=10)
        self.value_entry = ttk.Entry(root)
        self.value_entry.pack(pady=10)

        # Create button to perform conversion
        self.convert_button = ttk.Button(root, text="Convert", command=self.convert_units)
        self.convert_button.pack(pady=20)

        # Create label to display result
        self.result_label = ttk.Label(root, text="")
        self.result_label.pack(pady=10)

        # Define conversion factors
        self.conversion_factors = {
            ("Meter", "Foot"): 3.28084,
            ("Foot", "Inch"): 12,
            ("Kilogram", "Pound"): 2.20462,
            ("Celsius", "Fahrenheit"): 1.8,
            ("Liter", "Gallon"): 0.264172
        }

    def convert_units(self):
        from_unit = self.from_unit_combo.get()
        to_unit = self.to_unit_combo.get()
        value = self.value_entry.get()

        if not value:
            messagebox.showwarning("Warning", "Please enter a value!")
            return

        try:
            value = float(value)
            if from_unit == to_unit:
                result = value
            elif (from_unit, to_unit) in self.conversion_factors:
                factor = self.conversion_factors[(from_unit, to_unit)]
                result = value * factor
            elif (to_unit, from_unit) in self.conversion_factors:
                factor = 1 / self.conversion_factors[(to_unit, from_unit)]
                result = value * factor
            else:
                messagebox.showwarning("Warning", "Unsupported conversion!")
                return

            self.result_label.config(text=f"{value} {from_unit} = {result:.2f} {to_unit}")

        except ValueError:
            messagebox.showerror("Error", "Invalid value! Please enter a valid number.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverter(root)
    root.mainloop()
