import inflect
import sys
from datetime import date, datetime


def main():
    p = inflect.engine()
    today = date.today()
    birthday = date.fromisoformat(input("What's your birthday? ").replace('-', ''))
    timedif = (today - birthday).days * 24 * 60

    words = p.number_to_words(timedif).replace(' and ', ' ').replace('  ', ' ')

    print(f"{words.capitalize()} minutes")

if __name__ == "__main__":
    main()