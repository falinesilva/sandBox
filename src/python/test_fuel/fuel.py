def main():
    # Get input from the user
    while True:
        try:
            user_fraction = input("Fraction: ")
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
    user_fraction_converted = convert(user_fraction)
    
    gauge_result = gauge(user_fraction_converted)

    # Print percentage
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{int(percentage)}%")
def convert(fraction):
# Convery to fraction
    x, y = map(int, fraction.split('/'))
    if y == 0 or y < x:
        raise ValueError("Denominator cannot be zero.")
def gauge(percentage):
    # Process percentage
    percentage = (x / y) * 100
    percentage = round(percentage)


if __name__== "__main__":
    main()
