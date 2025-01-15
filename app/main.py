from converter import convert


def main():
    """
    Main function to handle command-line interaction for the currency converter.
    Prompts the user for input and displays the conversion results.
    """
    try:
        amount = float(input("Enter amount: "))
        base = input("Enter base currency: ").strip().upper()
        targets = input("Enter target currencies (comma-separated): ").strip().upper().split(',')
        result = convert(amount, base, targets)
        print("Conversion Results:")
        for currency, converted_amount in result.items():
            print(f"{currency}: {converted_amount:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the amount.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
