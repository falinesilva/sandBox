def main():
# Ask user what time it is
    time = input ("What time is it? ")

    time_converted = float (convert(time))

    if time_converted == 7 <= 8.0:
        print ("breakfast")
    if time_converted == 12.0 <= 13.0:
        print ("lunch")
    elif time_converted == 18.0 <= 20.0:
        print ("dinner")

def convert(time):

    hours, minutes = time.split(":")

    hours = float (hours)
    minutes = float (minutes)

    if minutes == 0 <= 30:
        minutes = 0.5
    elif minutes >= 30:
        minutes = 1.0

    time = (hours + minutes)
    return (time)

if __name__ == "__main__":
    main()
