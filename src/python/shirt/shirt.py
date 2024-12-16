import sys

from PIL import Image

def get_argument(argument):
    if len(argument) > 3:
        sys.exit("Too many command-line arguments")
    elif len(argument) < 3:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[2].endswith('.jpeg', '.jpg', '.png'):
        sys.exit("Invalid output")
    elif #Check if input and output have the same extension at the end
    else:
        a = argument[1]
        b = argument[2]
        return a, b