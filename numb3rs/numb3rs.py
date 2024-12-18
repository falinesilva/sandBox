import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    result = re.search(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-5][0-5])\.){3}[0-9]|[1-9][0-9]|1[0-9]{2}$",ip)
    if result:
        print (result[1])
    if result:
        return('True')
    else:
        return('False')


if __name__ == "__main__":
    main()
