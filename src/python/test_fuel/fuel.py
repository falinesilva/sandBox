def main():

    while True:
        try:
            user_input = input("Fraction: ")
            x, y = map(int, user_input.split('/'))
            if y == 0 or y < x:
                raise ValueError
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def convert(fraction):

def gauge(percentage):

    percentage = 


if __name__== "__main__":
    main()
