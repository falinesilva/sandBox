"""Input the time and output meal time"""

def main():

    time = input ("What time is it? ")

    print(convert(time))


def convert(time):

    hours, minutes = time.split(":")

    hours = float (hours)
    minutes = float (minutes) / 60

    time = (hours + minutes)
    
    if 7.0 <= time <= 8.0:
        return ("breakfast time")
    if 12.0 <= time <= 13.0:
        return ("lunch time")
    elif 18.0 <= time <= 20.0:
        return ("dinner time")
    
    return (time)

if __name__ == "__main__":
    main()
