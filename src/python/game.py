import random

# User provides a positive integer input
while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        pass

# Handle edge case when the user inputs 1
if n > 1:
    rand_n = random.randrange(1, n)
    print(n)
elif n == 1:
    rand_n = 1

# Prompt user to guess n
while True:
    try:
        answer = int(input("Guess: "))
        if answer < 0:
            raise ValueError
        elif answer < rand_n:
            print("Too small!")
        elif answer > rand_n:
            print("Too large!")
        else:
            print("Just right!")
    except ValueError:
        pass
