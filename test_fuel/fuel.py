def main():

    while True:
        try:
            user_fraction = input("Fraction: ")
            fraction = convert(user_fraction)
            result = gauge(fraction)
            print(result)
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

def convert(fraction):
    try:
        if '/' not in fraction:
            raise ValueError
        x, y = map(int, fraction.split('/', maxsplit=1))
        if not y > 0:
            raise ZeroDivisionError
        elif  x < 0 or x > y:
            raise ValueError
        else:
            percentage = int( (x / y) * 100)
            percentage = round(percentage)
        return percentage
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError

def gauge(percentage):
    if percentage <= 1:
        return("E")
    elif percentage >= 99:
        return("F")
    else:
        return(f"{int(percentage)}%")

if __name__== "__main__":
    main()
