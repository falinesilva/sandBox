def convert_camel_to_snake(name):
    """
    Converts a camelCase string to snake_case.
    """
    s = ""
    for c in name:
        if c.isupper():
            s += "_" + c.lower()
        elif c.islower():
            s += c
        else:
            break

    print("snake_case:", s)

if __name__ == "__main__":
    print("Convert camelCase to snake_case")
    s = (input("Input: "))
    output = convert_camel_to_snake(s)
    exit(0)