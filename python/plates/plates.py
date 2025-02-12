def main():

    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

   # Check length
    if len(s) > 6 or len(s) < 2:
        return False

    # Check if first two characters are alphabetical
    if not s[0:2].isalpha():
        return False

    # Check numbers in plate
    for i, c in enumerate(s):
        if c.isdigit():
            # Found the first digit
            if c == "0":
                return False
            # Check if all remaining characters are digits
            elif all(char.isdigit() for char in s[i:]):
                break
            else:
                return False

    # Check that all characters are alphanumeric
    for i in s:
        if not i.isalnum():
            return False

    return True


main()