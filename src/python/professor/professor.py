import random

def generate_integer(level):
    if level == 1:
        n = random.randint(1, 9)
    elif level == 2:
        n = random.randint(1, 99)
    else:
        n = random.randint(1, 999)
    return n

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

def main():
    level = get_level()

# Generate list of problems
    problems = []
    for i in range(10):
        new_item = (f"{generate_integer(level)} + {generate_integer(level)}")
        problems.append(new_item)

# Ask user for answer to list of problems

    for item in problems:
        while True:
            try:
                response = int(input(f"{item} = "))
                answer = eval(item)
                if not response > 0:
                    pass
                elif response == answer:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
                pass

            
        

main()