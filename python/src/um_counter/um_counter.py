"""
Counts how many times 'um' appears as a standalone word in user input.
"""

import re
import sys


def main():

    print(count(input("Text: ")))


def count(s):
    ums = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(ums)


if __name__ == "__main__":
    main()
