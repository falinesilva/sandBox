import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    html = re.search(r"<iframe.*(http.*\.*youtube\.com/embed/.*\").*</iframe>$", s)
    if html:
        link = str(html[1])
        updated_link = link.replace('"', '').replace('youtube.com/embed/', 'youtu.be/').replace('', '')
        if 'http:' in updated_link:
            updated_link.replace('http:', 'https:')
        return(updated_link)

if __name__ == "__main__":
    main()
