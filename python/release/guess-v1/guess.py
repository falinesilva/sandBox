"""Number guessing game"""

import random
import sys

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        pass

if n > 1:
    rand_n = random.randrange(1, n)
    print(n)
elif n == 1:
    rand_n = 1

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
            sys.exit("Just right!")
    except ValueError:
        pass
