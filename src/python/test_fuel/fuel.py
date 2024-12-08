def main():

    x = input("Fraction: ")
    
    fraction = convert(x)
    print(fraction)

    
def convert(fraction):
    while True:
        try:
            if '/' not in fraction:
                raise ValueError
            x, y = map(int, fraction.split('/', maxsplit=2))
            if x > y:
                raise ZeroDivisionError
        
            percentage = int( (x / y) * 100)
            percentage = round(percentage)
            return percentage
        except ValueError:
            print("ValueError")    
            break
        except ZeroDivisionError:
            break

# def gauge(percentage):
    #if percentage <= 1:
             #       print("E")
              #  elif percentage >= 99:
              #      print("F")
               # else:
                #    print(f"{int(percentage)}%")

if __name__== "__main__":
    main()
