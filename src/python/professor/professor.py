import random

def main():
    level = get_level()
    print(level)

problems = []

for i in range(10):
    y = generate_integer(level)
    

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

def generate_integer(level):
    if level == 1:
        n = random.randint(9)
    elif level == 2:
        n = random.randint(99)
    else:
        n = random.randint(999)
    return n
    
    

main()