import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    result = re.search(r"^([0-9]+[10-99]*[100-255]*\.){3}[0-9]+[10-99]*[100-255]*$",ip)
    if result:
        print (result[1])
    if result:
        return('True')
    else:
        return('False')


if __name__ == "__main__":
    main()
