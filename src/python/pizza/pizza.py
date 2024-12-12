import tabulate
from tabulate import tabulate
import sys
import csv

def main():
    user_file = get_argument(sys.argv)
   
    try:
        with open(user_file) as csvfile:
            reader = csv.reader(csvfile)
    except FileNotFoundError:
        sys.exit("File does not exist")

        print(reader)


def get_argument(command_line):
    
    if len(command_line) > 2:
        sys.exit("Too many command-line arguments")
    elif len(command_line) < 2:
        sys.exit("Too few command-line arguments")
    elif not command_line[1].endswith('.csv'):
        sys.exit("Not a CSV file")
    else:
        a = command_line[1]
        return a

if __name__ == "__main__":
	main()