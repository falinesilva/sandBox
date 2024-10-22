def main():
# Ask user what time it is
    time = input ("What time is it? ")

    time_converted = (convert(time))

    if 7.0 <= time_converted <= 8.0:
        print ("breakfast time")
    if 12.0 <= time_converted <= 13.0:
        print ("lunch time")
    elif 18.0 <= time_converted <= 20.0:
        print ("dinner time")

def convert(time):

    hours, minutes = time.split(":")

    hours = float (hours)
    minutes = float (minutes) / 60

    time = (hours + minutes)
    return (time)

if __name__ == "__main__":
    main()
