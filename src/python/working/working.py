import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        match = re.search(r"^(\d)(.*|:\d\d)(AM|PM) to (\d)(.*|:\d\d)(AM|PM)$", s)

        if not match:
            raise ValueError
        
        if 'PM' in match[3]:
            start_hours = (int(match[1]) + 12)
        else:
            start_hours = f"{int(match[1]):02}"
        if 'PM' in match [6]:
            end_hours = (int(match[4]) + 12)
        else:
            end_hours = f"{int(match[4]):02})"
        
        if not ':' in match[2]:
            start_minutes = (':00')
        else:
            start_minutes = match[2].strip()

        if not ':' in match[5]:
            finish_minutes = (':00')
        else:
            finish_minutes = match[5].strip()

        hours = (f"{start_hours}{start_minutes} to {end_hours}{finish_minutes}")
        return hours
    
    
    except ValueError:
        return ('ValueError')

if __name__ == "__main__":
    main()