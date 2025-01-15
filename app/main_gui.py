import tkinter as tk
from tkinter import messagebox
from converter import convert


def convert_currency():
    """
    Handle the conversion request from the GUI.
    Retrieves input, calls the converter, and displays the result.
    """
    try:
        amount = float(amount_entry.get())
        base_currency = base_currency_entry.get().strip().upper()
        target_currencies = target_currencies_entry.get().strip().upper().split(',')

        if not base_currency or not target_currencies:
            raise ValueError("Base currency and target currencies are required!")

        result = convert(amount, base_currency, target_currencies)
        result_text = f"Conversion Results:\n"
        for currency, converted_amount in result.items():
            result_text += f"{currency}: {converted_amount:.2f}\n"

        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Ensure the amount is numeric and currencies are valid.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Currency Converter")

# Input fields
tk.Label(root, text="Amount:").grid(row=0, column=0, padx=10, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Base Currency:").grid(row=1, column=0, padx=10, pady=5)
base_currency_entry = tk.Entry(root)
base_currency_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Target Currencies (comma-separated):").grid(row=2, column=0, padx=10, pady=5)
target_currencies_entry = tk.Entry(root)
target_currencies_entry.grid(row=2, column=1, padx=10, pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result display
result_label = tk.Label(root, text="", justify="left", anchor="w")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Run the main loop
root.mainloop()
