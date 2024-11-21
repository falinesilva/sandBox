import sys
import random
from pyfiglet import Figlet

# Initialize figlet
figlet = Figlet()

# Initalize list of fonts
fonts = list (figlet.getFonts())

# Checks usage
length = len(sys.argv)
if length not in {0, 1, 3}:
    sys.exit("Invalid Usage")

elif length == 3 and sys.argv[1] not in {"--f", "-f", "-font" "--font"}:
    sys.exit("Invalid Usage")

elif length == 3 and sys.argv[2] not in fonts:
    sys.exit("Invalid Usage")

elif length == 3:
    figlet.setFont(font=sys.argv[2])

elif length == 1:
    figlet.setFont(font=random.choice(fonts))

else:
    pass

# Ask user for a string
a = str(input("Input: ")).strip()

# Print string in desired font
print((figlet.renderText(a)))