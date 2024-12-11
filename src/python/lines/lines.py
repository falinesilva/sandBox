import sys

def main():
    
   user_file = get_argument(sys.argv)
   print(user_file)

def get_argument(command_line):
    
    if len(command_line) > 2:
        sys.exit("Too many arguments")
    elif len(command_line) < 2:
        sys.exit("Too few arguments")
    elif not command_line[1].endswith('.py'):
        sys.exit("Not a python file")
    else:
        a = command_line[1]
        return a

if __name__ == "__main__":
	main()