def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = map(int, fraction.split('/'))
            # Check if y is zero to avoid division by zero
            x = round(x)
            y = round(y)
            if y == 0:
                raise ValueError("Denominator cannot be zero.")
            # Calculate the percentage
            percentage = (x / y) * 100
            # Display 'E' for empty (1% or less) and 'F' for full (99% or more)
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

main()
