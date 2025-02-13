# Extract youtube.com link from an embed block

import re
import sys


def main():
    print("Extract a 'youtube.com' link from 'iframe' block\n")
    print(parse(input("HTML: ")))


def parse(s):
    html = re.search(r"<iframe.*(http.*\.*youtube\.com/embed/.*\").*</iframe>$", s)
    if html:
        link = str(html[1])
        updated_link = link.replace('"', '').replace('youtube.com/embed/', 'youtu.be/').replace('', '')
        if 'http:' in updated_link:
            updated_link = updated_link.replace('http:', 'https:')
        if 'www.' in updated_link:
            updated_link = updated_link.replace('www.', '')
        return(updated_link)

if __name__ == "__main__":
    main()
