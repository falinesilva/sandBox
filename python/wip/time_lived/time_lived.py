"""
Calculates the number of minutes since a given birthdate.

Usage:
    python minutes_since_birth.py
"""

import inflect
import sys
from datetime import date, datetime


def minutes(s):
    p = inflect.engine()

    try:
        birthday = date.fromisoformat(s.replace("-", ""))

        today = date.today()

        timedif = (today - birthday).days * 24 * 60

        words = p.number_to_words(timedif).replace(" and ", " ").replace("  ", " ")

        return f"{words.capitalize()} minutes"

    except ValueError:
        sys.exit(1)

    except TypeError:
        sys.exit(1)


def main():

    print(minutes(input("What's your birthday? ")))


if __name__ == "__main__":
    main()