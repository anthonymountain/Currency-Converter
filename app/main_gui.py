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

        result_label.config(text=result_text, fg="#00FF00")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Ensure the amount is numeric and currencies are valid.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Create the main Tkinter window
root = tk.Tk()
root.title("Currency Converter 2000s Edition")
root.geometry("600x400")
root.configure(bg="#FF13F0")  # Hot pink background

# Fonts and styles
sans = ("Comic Sans MS", 12, "bold")
papyrus = ("Papyrus", 14, "bold")

# Gradient background simulation
canvas = tk.Canvas(root, width=600, height=400, highlightthickness=0)
canvas.place(x=0, y=0)

for i in range(400):
    red = max(255 - i, 0)  # Ensure the value doesn't go below 0
    gradient_color = f"#{red:02x}13F0"
    canvas.create_line(0, i, 600, i, fill=gradient_color)

# Input fields
tk.Label(root, text="ur $$:", font=sans, bg="#00FF00", fg="#FF13F0").grid(row=0, column=0, padx=10, pady=5, sticky="e")
amount_entry = tk.Entry(root, font=("Arial", 12), bg="#00FFFF", fg="#0000FF", bd=5, relief="groove")
amount_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="type of $$ u have:", font=sans, bg="#00FF00", fg="#FF13F0").grid(row=1, column=0, padx=10, pady=5, sticky="e")
base_currency_entry = tk.Entry(root, font=("Arial", 12), bg="#00FFFF", fg="#0000FF", bd=5, relief="ridge")
base_currency_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="$$ u want 2 get (comma-separated):", font=sans, bg="#00FF00", fg="#FF13F0").grid(row=2, column=0, padx=10, pady=5, sticky="e")
target_currencies_entry = tk.Entry(root, font=("Arial", 12), bg="#00FFFF", fg="#0000FF", bd=5, relief="sunken")
target_currencies_entry.grid(row=2, column=1, padx=10, pady=5)

# Convert button
convert_button = tk.Button(root, text="clik 2 get", font=papyrus, bg="#FF5F00", fg="#1E90FF", bd=8, relief="ridge", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, pady=20)

# Result display
result_label = tk.Label(root, text="", justify="left", anchor="w", font=("Arial", 12, "bold"), bg="#FF13F0", fg="#00FF00")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")

# Run the main loop
root.mainloop()
