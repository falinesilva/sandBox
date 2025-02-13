# Convert range of hours from 12HR to 24HR

import re
import sys

"""Convert 12HR range to 24HR format (e.g. 9AM to 5PM)"""

def main():
    print(convert(input("Input Example: 9AM to 5PM\nHours: ")))

def convert(s):
    try:
        match = re.search(r"^(\d{1,2})(.*|:\d\d)(AM|PM) to (\d)(.*|:\d\d)(AM|PM)$", s)
        if not match:
            raise ValueError # TODO: Allow for space between number and AM/PM and allow lowercase am/pm

        if int(match[1]) > 12 or int(match[4]) > 12:
            raise ValueError
        if 'PM' in match[3]:
            start_hours = (int(match[1]) + 12)
        elif 'AM' in match[3] and int(match[1] == 12):
            start_hours = 00
        else:
            start_hours = f"{int(match[1]):02}"
        if 'PM' in match [6]:
            end_hours = (int(match[4]) + 12)
        else:
            end_hours = f"{int(match[4]):02}"

        if not ':' in match[2]:
            start_minutes = '00'
        else:
            start_minutes = match[2].strip().replace(':', '')

        if not ':' in match[5]:
            finish_minutes = '00'
        else:
            finish_minutes = match[5].strip().replace(':', '')

        if int(start_minutes) > 59 or int(finish_minutes) > 59:
            raise ValueError

        hours = (f"{start_hours}:{start_minutes} to {end_hours}:{finish_minutes}")
        return hours


    except ValueError:
        sys.exit('Wrong format.')

if __name__ == "__main__":
    main()
