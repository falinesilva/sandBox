import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        match = re.search(r"^(\d{1,2})(.*|:\d\d)(AM|PM) to (\d{1,2})(.*|:\d\d)(AM|PM)$", s)

        # Check for match
        if not match:
            raise ValueError
        else:
            print(match[4])
            print(match[6])
        # Check both hours
        if int(match[1]) > 12 or int(match[4]) > 12:
            raise ValueError
        
        # Check start time hours
        if 'PM' in match[3] and int(match[1]) < 12:
            start_hours = (int(match[1]) + 12)
        elif 'PM' in match[3] and int(match[1]) == 12:
            start_hours = 12
        elif 'AM' in match[3] and int(match[1]) == 12:
            start_hours = f"{00:02}"
        else:
            start_hours = f"{int(match[1]):02}"
        
        # Check start time minutes
        if not ':' in match[2]:
            start_minutes = '00'
        else:
            start_minutes = match[2].strip().replace(':', '')

        # Check finish time hours
        print(match[4], match[6])
        if 'PM' in match[6] and int(match[4]) < 12:
            finish_hours = (int(match[4]) + 12)
        elif 'PM' in match[6] and int(match[4]) == 12:
            finish_hours = 12
        elif 'AM' in match[6] and int(match[4]) == 12:
            finish_hours = f"{00:02}"
        else:
            finish_hours = f"{int(match[4]):02}"
        
        # Check finish time minutes
        if not ':' in match[5]:
            finish_minutes = '00'
        else:
            finish_minutes = match[5].strip().replace(':', '')
        
        # Check both minutes
        if int(start_minutes) > 59 or int(finish_minutes) > 59:
            raise ValueError
        
        # Format final output
        hours = (f"{start_hours}:{start_minutes} to {finish_hours}:{finish_minutes}")
        return hours
    
    except ValueError:
        return 'ValueError'

if __name__ == "__main__":
    main()