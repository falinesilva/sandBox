import sys

from PIL import Image, ImageOps

def main():
    try:
        a,b = get_argument(sys.argv)
        print(a,b)
        with Image.open(b) as shirt:
            size = shirt.size
        print(size)
        with Image.open(a) as img:
            ImageOps.fit(img, size).save('input_fit.jpg')
    except FileNotFoundError:
        sys.exit('Input does not exist')

def get_argument(input):
    extensions = ('.jpg', '.png', '.jpeg')
    if len(input) > 3:
        sys.exit("Too many command-line arguments")
    elif len(input) < 3:
        sys.exit("Too few command-line arguments")
    elif not input[2].endswith(extensions):
        sys.exit("Invalid output")
    for ext in extensions:
        if input[1].endswith(ext) and not input[2].endswith(ext):
            sys.exit('Input and output have different extensions')
    else:
        a = input[1]
        b = input[2]
        return a, b
    

if __name__ == "__main__":
    main()