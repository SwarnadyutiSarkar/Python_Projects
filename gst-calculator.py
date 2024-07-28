def calculate_gst(amount, gst_rate):
    """
    Calculate GST amount and total amount including GST.

    Parameters:
    amount (float): The original amount before GST.
    gst_rate (float): The GST rate as a percentage.

    Returns:
    tuple: A tuple containing (GST amount, total amount including GST)
    """
    gst_amount = (amount * gst_rate) / 100
    total_amount = amount + gst_amount
    return gst_amount, total_amount

def main():
    print("Indian GST Calculator")

    # Define available GST rates
    gst_rates = [5, 10, 18]

    # Input the original amount
    try:
        amount = float(input("Enter the original amount: ₹"))

        # Display GST rate options
        print("\nSelect GST rate from the following options:")
        for i, rate in enumerate(gst_rates, 1):
            print(f"{i}. {rate}%")

        # Input and validate GST rate choice
        choice = int(input("\nEnter your choice (1/2/3): "))

        if choice in [1, 2, 3]:
            gst_rate = gst_rates[choice - 1]
        else:
            print("Invalid choice. Please select a valid option.")
            return

        # Calculate GST and total amount
        gst_amount, total_amount = calculate_gst(amount, gst_rate)

        # Display results
        print(f"\nGST Rate: {gst_rate}%")
        print(f"GST Amount: ₹{gst_amount:.2f}")
        print(f"Total Amount (including GST): ₹{total_amount:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values for amount and choice.")

if __name__ == "__main__":
    main()
