import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        match = re.search(r"^(\d)(.*|:\d\d)(AM|PM) to (\d)(.*|:\d\d)(AM|PM)$", s)
        if match:
            print(match[1]) # Start hours
            print(match[2]) # Start minutes
            print(match[3]) # Start AM|PM
            print(match[4]) # Finish hours
            print(match[5]) # Finish minutes
            print(match[6]) # Finish AM|PM
        if not match:
            raise ValueError
    except ValueError:
        return ('ValueError')

if __name__ == "__main__":
    main()
