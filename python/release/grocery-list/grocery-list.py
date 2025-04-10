"""Create a grocery list"""

grocery_list = {}

print("Input items for a grocery list\nEnter 'E' to exit")

while True:
    try:
        item = input ("Item: ").upper()


        if item == "E":
            raise EOFError

        if item in grocery_list:
            grocery_list[item] += 1

        else:
            grocery_list[item] = 1

    except EOFError:
        print("Grocery List:")
        for key in sorted(grocery_list.keys()):# TODO: Later it could be output to clipboard or .txt file
            print(f"{grocery_list[key]} {key}") #TODO: Not obvious to user that the number on the left is the quantity
        exit()

    except ValueError:
        pass
