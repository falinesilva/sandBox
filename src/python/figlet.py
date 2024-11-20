import sys
import random
from pyfiglet import Figlet

# Initialize figlet
figlet = Figlet()

# Initalize list of fonts
fonts = list (figlet.getFonts())

# Checks the amount of arguments
length = len(sys.argv)
if length not in {0, 3}:
    print(length)
    sys.exit("Invalid arguments")

# Check second argument
elif length == 3 and sys.argv[1] not in {"--f", "--font"}:
    print(sys.argv[2])
    sys.exit("Invalid arguments2")

# Checks that the font is valid
elif sys.argv[2] not in fonts:
    sys.exit("Invalid font")
else:
    pass

# Ask user for a string
a = str(input("Input: ")).strip()

# Print string in desired font
print((figlet.renderText(a)))