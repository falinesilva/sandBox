import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        match = re.search(r"^(\d)(.*|:\d\d)(AM|PM) to (\d)(.*|:\d\d)(AM|PM)$", s)
        if match:
            print(match[1]) # Start hours
            print(match[2]) # Start minutes
            print(match[3]) # Start AM|PM
            print(match[4]) # Finish hours
            print(match[5]) # Finish minutes
            print(match[6]) # Finish AM|PM
        if not match:
            raise ValueError
        
        if 'PM' in match[3]:
            print('Starts in PM')
            start_hours = (int(match[1]) + 12)
        else:
            start_hours = (f"{match[1]:02}")
        if 'PM' in match [6]:
            print('Ends in PM')
            end_hours = (int(match[4]) + 12)
        else:
            end_hours = (f"{match[4]:02}")
        
        hours = (f"{start_hours}{match[2]}to {end_hours}{match[5]}")
        return hours
    except ValueError:
        return ('ValueError')

if __name__ == "__main__":
    main()