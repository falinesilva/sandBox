def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length
    if len(s) > 6 or len(s) < 2:
        print("Length wrong")
        return False

    # Check that all characters are alphanumeric
    if not s.isalnum():
        print("Contains non-alphanumeric characters")
        return False

    # Check if first two characters are alphabetical
    if not s[:2].isalpha():
        print("First two characters are not alphabetical")
        return False

    # Check if the first digit (if any) is not '0'
    for char in s:
        if char.isdigit():
            if char == "0":
                print("First number is '0'")
                return False
            break

    # Check if all numbers, if present, come at the end
    has_seen_digit = False
    for char in s:
        if char.isdigit():
            has_seen_digit = True
        elif has_seen_digit:
            # If we see a letter after seeing a digit, it's invalid
            print("Numbers are not at the end")
            return False

    return True


main()
