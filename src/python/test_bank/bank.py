def main():
    # Get greeting from user
    greeting = input("Greeting: ")

    # Get value of the greeing
    response = value(greeting)

    # Print value of the greeting
    print(f"${response}")


def value(greeting):

    greeting = greeting.lower().strip()

    # Return $100 if greeting does not start with h
    if greeting.startswith("h") == 0:
        return 100

    # Return $20 if greet starts with h but does not equal hello

    elif greeting.startswith("h") and greeting.startswith("hello") == 0:
        return 20

    # Otherwise Return $0
    else:
        return 0


if __name__ == "__main__":
    main()
