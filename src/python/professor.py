import random

def main():
    level = get_level()
    print(level)


def get_level():

    # Prompt user for a level 1, 2, or 3
    while True:
        try:
            level = int(input("Level: "))
            if level not in {1, 2, 3}:
                raise ValueError
            else:
                return level
                break
        except ValueError:
            print("ValueError")
            pass

# def generate_integer(level):
    
    


main()