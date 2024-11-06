# Initiate grocery list dictionary

grocery_list = []

while True:
    try:
        # Get item to add
        item = input ().upper()


        # Check for control-d (EOFError to exit)
        if item == "CONTROL-D":
            raise EOFError


        # Add item to grocery list
        if item not in grocery_list:
            grocery_list.append(item)

    except EOFError:
        grocery_list = sorted(grocery_list) # Sort list

        for index, item in enumerate(grocery_list, 1):
            print(f"{index} {item}")
        exit() # Exit after printing

    except ValueError:
        pass
