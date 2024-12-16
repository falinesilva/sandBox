import sys
import csv


def main():

    after = []
    try:
        a, b = get_argument(sys.argv)
        with open(a) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(",")
                after.append({"first": first, "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {a}")

    with open(b, 'w', newline = '') as after_file:
        fieldnames = after[0]
        writer = csv.DictWriter(after_file, fieldnames=fieldnames)

        writer.writeheader()
        for item in after:
            writer.writerow(item)


def get_argument(argument):
    if len(argument) > 3:
        sys.exit("Too many command-line arguments")
    elif len(argument) < 3:
        sys.exit("Too few command-line arguments")
    else:
        a = argument[1]
        b = argument[2]
        return a, b


if __name__ == "__main__":
    main()
