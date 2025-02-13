def calculate_change(due_amount=50):
    """
    Prompts the user to insert coins and calculates the change owed.
    
    Parameters:
        due_amount (int): The total amount to be paid (default is 50).
    """
    paid = 0
    change = 0

    while paid < due_amount:
        print("Amount Due:", due_amount - paid)
        coin = int(input("Insert Coin: "))

        if coin in [25, 10, 5]:
            paid += coin
        else:
            print("Invalid coin.")

    change = paid - due_amount
    print("Change Owed:", change)

def main():
    """Starts the coin insertion process with a default due amount of 50."""
    calculate_change(50)

if __name__ == "__main__":
    main()
