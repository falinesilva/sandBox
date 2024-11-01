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

    # Check that all characters are alphanumeric
    for i in s:
        if not i.isalnum():
            return False

    # Check if first two characters are alphabetical
    if not s[0:1].isalpha():
        return False

    # Check if first number is 0
    if s[2] == "0":
            return False

    for c in s[:2]:
        if c.isdigit() and s[4].salpha:
            return False

    # Check if all numbers come at the end.
    if s[-1].isalpha() and not s[-2].isalpha():
        return False

    if s[-3].isalpha() and s[-4].isdigit():
         return False

    x = len(s) // 2

    if s[x].isdigit():
        return False

    else:
        return True


main()
