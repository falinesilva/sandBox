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
            pass

def main():
    level = get_level()

# Generate list of problems
    problems = []
    for i in range(10):
        new_item = (f"{generate_integer(level)} + {generate_integer(level)}")
        problems.append(new_item)

# Ask user for answer to list of problems and track score
    score = 0
    for item in problems:
        attempts = 0
        while True:
            try:
                response = int(input(f"{item} = ")) # Ask use for answer to problem
                answer = eval(item) # Evaluate answer
                if not response > 0 or response != answer:
                    raise ValueError # If input is invalid or wrong, raise ValueError
                else:
                    score += 1 # If answer is correct, add point to score and continue
                    print("Score:",score)
                    break
            except ValueError:
                print("EEE")
                attempts += 1
                print ("Attempts",attempts)
                if attempts > 2: # If user enters invalid or wrong answer 3 times, continue to next
                    break
                pass
    print("Score:", score)
main()