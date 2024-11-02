def main():
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

main()
