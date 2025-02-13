def main():
    """
    Main function to simulate a simple menu-based ordering system.
    Allows users to add items to their order and displays the total.
    """
    
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    total = float(0.00)

    print("Enter 'exit' to quit.")

    while True:
        try:
            item = input("Item: ").strip().title()
            if item.lower() == "exit":
                print(f"Final total: ${total:.2f}")
                raise EOFError
            if item not in menu:
                print("Item not on the menu.")
                raise ValueError

            price = menu[item]
            total += price
            formatted_total = f"${total:.2f}"
            print("Total:", formatted_total)

        except EOFError:
            exit()
        except ValueError:
            pass


main()
