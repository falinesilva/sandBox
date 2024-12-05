def main():
    # Get input from the user
    user_fraction = input("Fraction: ")
    user_fraction_converted = convert(user_fraction)
    gauge_result = 

    # Print percentage
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = map(int, fraction.split('/'))
            if y == 0 or y < x:
                raise ValueError("Denominator cannot be zero.")
            percentage = (x / y) * 100
            percentage = round(percentage)

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{int(percentage)}%")
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
def convert(fraction):
# Convery to fraction

def gauge(percentage):
# Process percentage


if __name__== "__main__":
    main()
