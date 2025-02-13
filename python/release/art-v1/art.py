def ascii_art(a):
    """Prints ASCII art from input"""

    import sys
    import random
    from pyfiglet import Figlet
    
    figlet = Figlet()

    fonts = list(figlet.getFonts())

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

    a = a.strip()
    a = figlet.renderText(a)
    return a


def main():
    """Prints user input as ASCII art"""
    s = input("Input: ")
    s = ascii_art(s)
    print(s)

if __name__ == "__main__":
    main()