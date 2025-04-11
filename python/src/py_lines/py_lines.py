"""See how many lines a python file has"""

import sys

def filter(lines):
    filtered_lines = []
    for line in lines:
        line = line.lstrip()
        if line != '':
            if not line.startswith('#'):
                filtered_lines.append(line)

    return(len(filtered_lines))

def get_argument(command_line):

    if len(command_line) > 2:
        sys.exit("Too many command-line arguments")
    elif len(command_line) < 2:
        sys.exit("Too few command-line arguments")
    elif not command_line[1].endswith('.py'):
        sys.exit("Not a python file")
    else:
        a = command_line[1]
        return a

def main(): # TODO: Abstract away and simplify main()

    user_file = get_argument(sys.argv)

    try:
        with open(user_file) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(filter(lines))

if __name__ == "__main__":
	main()
