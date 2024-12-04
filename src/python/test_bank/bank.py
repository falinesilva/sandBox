def main():
    # Get greeting from user
    greeting = input("Greeting: ").lower().strip()

    # Get value of the greeing
    response = value(greeting)

    # Print value of the greeting
    print(f"${response}")


def value(greeting):
    
    # Return 0 if the greeting is 'hello'
    if greeting == ("hello"):
        return 0
    
    # Return 100 if the greeting does not start with 'h'
    elif not greeting.startswith("h"):
        return 100
    
    # Return 20 if the greeting starts with 'h' but is not 'hello'
    else:
        return 20


if __name__ == "__main__":
    main()