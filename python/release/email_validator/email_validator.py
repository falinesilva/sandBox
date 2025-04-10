"""
Validates an email address using the validators library and prints whether it is valid.
"""

import validators

def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
