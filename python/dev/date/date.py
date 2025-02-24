""" 
WIP: This script is a work in progress. Functionality may change. 
Converts a user-input date from MM/DD/YYYY or Month Day, Year format to YYYY-MM-DD.  
"""

# TODO: Add unit tests to validate date formatting.
# Issue: An incomplete year (e.g. '199') is still being output without error as '199'.  
# Expected: Ensure the year is formatted correctly (e.g., YYYY).  
# Also, clarify the acceptable format to avoid confusion.

# List of months

months_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# Prompt user for date in MM-DD-YYYY format or written out (i.e. September 8th, 1636)

while True:
    try:
        user_date = ""
        user_date = input("Date: ").strip('"').strip()
        if "/" in user_date:
            slash_date = user_date.split("/")
            month = int(slash_date[0])
            if month > 12:
                raise TypeError
            day = int(slash_date[1])
            if day < 1 or day > 31:
                raise TypeError
            year = slash_date[2]
            print(year, str(month).zfill(2), str(day).zfill(2), sep="-")
            exit()
        elif "," in user_date:
            comma_date = user_date.split()
            year = comma_date[2]
            day = int(
                comma_date[1]
                .replace(",", "")
                .replace("st", "")
                .replace("rd", "")
                .replace("nd", "")
                .replace("th", "")
            )
            if day > 31:
                raise TypeError
            month = comma_date[0].strip(",")
            month = str(months_list.index(comma_date[0]) + 1)
            if int(month) < 1 or int(month) > 12:
                raise TypeError
            print(year, str(month).zfill(2), str(day).zfill(2), sep="-")
            exit()
        else:
            raise TypeError
    except ValueError:

        print("Usage: Format example: September 8th, 1636")
        exit()
    except TypeError:
        print("Usage: Format example: September 8th, 1636")
        pass