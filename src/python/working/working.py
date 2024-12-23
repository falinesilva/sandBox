import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    hours = re.search(r"^(\d).*(AM|PM)", s)
    if hours:
        return (f"{hours[1]} {hours[2]}")


if __name__ == "__main__":
    main()
