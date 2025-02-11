def main():

# Dict with fruits and their calorie levels
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
        "watermelon": "80"
    }

# Get input and convert to lowercase to match dict
    fruit = input ("Item: ")
    fruit = fruit.lower()

# Is input in sheet
    if fruit not in sheet:
        return False

# Validate input.
    if is_valid(fruit):
        print ("Calories:",sheet[fruit])

def is_valid(s):
    for c in s:
        if c.isalpha() or c.isspace(): # Check if c is alphanumeric or a whitespace
            return True
    else:
        return False
main()
