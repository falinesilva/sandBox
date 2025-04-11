import sys

from PIL import ImageOps
from PIL import Image


def main():
    try:
        a, b = get_argument(sys.argv)
        print(a, b)

        with Image.open(a) as img, Image.open("shirt.png") as overlay:
            size = overlay.size
            resized = ImageOps.fit(img, size)
            resized.paste(overlay, (0, 0), overlay)
            resized.save(b)
    except FileNotFoundError:
        sys.exit("Input does not exist")


def get_argument(input):
    extensions = (".jpg", ".png", ".jpeg")
    if len(input) > 3:
        sys.exit("Too many command-line arguments")
    elif len(input) < 3:
        sys.exit("Too few command-line arguments")
    elif not input[2].endswith(extensions):
        sys.exit("Invalid output")
    for ext in extensions:
        if input[1].endswith(ext) and not input[2].endswith(ext):
            sys.exit("Input and output have different extensions")
    else:
        a = input[1]
        b = input[2]
        return a, b


if __name__ == "__main__":
    main()
