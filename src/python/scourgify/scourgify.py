import sys
import csv

def main():

    original = []
    try:
        a,b = get_argument(sys.argv)
        print(a,b)
        with open(a) as file:
            reader = csv.DictReader(file)
            for row in reader:
                original.append(row)
    except FileNotFoundError:
        sys.exit(f'Could not read {a}')

    print(original[1])

def get_argument(argument):
    print(argument)
    print(len(argument))
    if len(argument) > 3:
        sys.exit("Too many command-line arguments")
    elif len(argument) < 3:
        sys.exit("Too few command-line arguments")
    else:
        a = argument[1]
        b = argument[2]
        return a,b

if __name__ == "__main__":
	main()