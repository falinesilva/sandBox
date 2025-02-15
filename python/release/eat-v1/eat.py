"""Input the time and output the meal time"""

def convert(time):

    try:
        hours, minutes = time.split(":")

        hours = float(hours)
        minutes = float(minutes) / 60

        time = hours + minutes

        if 7.0 <= time <= 8.0:
            return "breakfast time"
        if 12.0 <= time <= 13.0:
            return "lunch time"
        elif 18.0 <= time <= 20.0:
            return "dinner time"

        return time
    except ValueError:
        print("ValueError: Invalid Format")
        exit()

def main():

    time = input("What time is it? ")

    print(convert(time))

if __name__ == "__main__":
    main()
