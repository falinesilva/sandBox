"""Input a few item to see how many calories it has"""

def main():

    sheet = {
        "apple": "130",
        "calories": "130",
        "avocado": "50",
        "banana": "110",
        "cantaloupe": "50",
        "gratefruit": "60",
        "grapes": "90",
        "honeydew melon": "50",
        "kiwifruit": "90",
        "lemon": "15",
        "lime": "20",
        "nectarine": "60",
        "orange": "80",
        "peach": "60",
        "pear": "100",
        "pineapple": "50",
        "plums": "70",
        "strawberries": "50",
        "sweet cherries": "100",
        "tangerine": "50",
        "watermelon": "80",
    }

    fruit = input("Item: ")
    fruit = fruit.lower()

    if fruit not in sheet:
        print("Not in list")
        return False

    if is_valid(fruit):
        print("Calories:", sheet[fruit])


def is_valid(s):
    for c in s:
        if c.isalpha() or c.isspace():
            return True
    else:
        return False


main()
