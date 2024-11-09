# Initiate grocery list dictionary

grocery_list = {}

while True:
    try:
        # Get item to add
        item = input ().upper()


        # Check for control-d (EOFError to exit)
        if item == "CONTROL-D":
            raise EOFError

        if item in grocery_list:
            grocery_list[item] += 1

        # Add item to grocery list
        else:
            grocery_list[item] = 1

    except EOFError:
        for key in sorted(grocery_list.keys()):  # Sorting keys alphabetically
            print(f"{grocery_list[key]} {key}")
        exit()

    except ValueError:
        pass
