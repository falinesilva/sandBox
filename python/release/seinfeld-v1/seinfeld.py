def main():
    """
    youtube.com/watch?v=IN6cJ_wGmsk
    Prompts for a greeting and prints a value.
    """
    
    greeting = input("Greeting: ")
    greeting = greeting.lower().strip()

    if greeting.startswith("h") == 0:
        print("$100")
    elif greeting.startswith("h") and greeting.startswith("hello") == 0:
        print("$20")
    else:
        print("$0")

main()
