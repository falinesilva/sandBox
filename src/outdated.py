# Initiate list of months

month_list = [
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
            day = slash_date [1]
            year = slash_date[2]
            print (year, month.zfill(2), day.zfill(2), sep ="-") # Print formatted date with padding
        elif "," in user_date: # Check for , in input
            print (",")
            # WIP
        else:
            raise TypeError
    except TypeError:
        pass