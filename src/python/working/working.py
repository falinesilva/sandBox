import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r"^(\d)(.*|:\d\d)(AM|PM) to .*", s)
    if match:
        print(match[1]) # Start hours
        print(match[2])# Start minutes
        print(match[3]) # Start AM|PM


if __name__ == "__main__":
    main()
