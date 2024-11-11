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
        "December"
    ]

# Prompt user for date in MM-DD-YYYY format or written out (i.e. September 8th, 1636)

while True:
    try:
        user_date = "" # Reset input each loop
        user_date = input("Date: ")
        if "/" in user_date: # Check for / in input
            slash_date = user_date.split("/") # Split string to list
            month = slash_date[0]
            if month > 12:
                raise TypeError
            day = slash_date [1]
            if day > 31:
                raise TypeError
            year = slash_date[2]
            print (year, month.zfill(2), day.zfill(2), sep ="-") # Print formatted date with padding
            exit()
        elif "," in user_date: # Check for , in input
            comma_date = user_date.split()
            year = comma_date[2]
            day = comma_date [1].replace(',', '').replace('st', '').replace('rd', '').replace('nd', '').replace('th', '')
            if day > 31:
                raise TypeError
            month = comma_date[0]
            if month > 12:
                raise TypeError
            month_numbered = str (months_list.index(comma_date[0]) + 1)
            print (year, month_numbered.zfill(2), day.zfill(2), sep = "-")
            exit()
        else:
            raise TypeError
    except TypeError:
        pass
