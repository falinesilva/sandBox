def main():

    # Define menu
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    total = float(0.00)
    # Get order
    while True:
        try:
            item = str (input("Item: "))
            if item == "control-d":
                raise EOFError
            if item not in menu:
                raise ValueError
            if item in menu:
                price = float(menu[item])
                total += price
                formatted_total = f"{total:.2f}"
                print ("Total: $",formatted_total,)
        except EOFError:
            exit()
        except ValueError:
            pass


main()
