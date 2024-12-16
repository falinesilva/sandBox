import sys
import csv

def main():

    after = []
    try:
        a,b = get_argument(sys.argv)
        with open(a) as file:
            reader = csv.DictReader(file)
            for row in reader:
                extracted = {}
                last,first = ((row['name'].split(',')))
                house = row['house']
                extracted['first'] = first
                extracted['last'] = last
                extracted ['house'] = house
                after.append(extracted)
            print(after)
            

            


    except FileNotFoundError:
        sys.exit(f'Could not read {a}')

def get_argument(argument):
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