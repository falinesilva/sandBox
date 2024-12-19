import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    html = re.search(r".*(src=\"http.*youtube.*title=).*", s)
    if html:
        link = html[1]
        link.replace('src="', '')
        print(link)
        return(link)
    
if __name__ == "__main__":
    main()
