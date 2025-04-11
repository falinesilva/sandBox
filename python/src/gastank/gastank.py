def fuel(s):

    def convert(fraction):
        try:
            if "/" not in fraction: # TODO: Replace this with regex
                raise ValueError
            x, y = map(int, fraction.split("/", maxsplit=1))
            if not y > 0:
                raise ZeroDivisionError
            elif x < 0 or x > y:
                raise ValueError
            else:
                percentage = int((x / y) * 100)
                percentage = round(percentage)
            return percentage
        except ValueError:
            print("ValueError: Invalid")
            exit(1)
        except ZeroDivisionError:
            print("ZeroDivisionError: Invalid")            
            exit(2)
    def gauge(percentage):
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return f"{int(percentage)}%"

    while True:
        try:
            fraction = convert(s)
            result = gauge(fraction)
            return result
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def main():
    print((fuel(input("Gas: "))))


if __name__ == "__main__":
    main()
