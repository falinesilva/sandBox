"""Calculate a math expression"""

while True:
    try:
        expression = input("Math Expression: ")

        x, y, z = expression.split(" ")

        x = float(x)

        z = float(z)

        match (y):
            case "+":
                print(float(x + z))
            case "-":
                print(float(x - z))
            case "*":
                print(float(x * z))
            case "/":
                print(float(x / z))
    except ValueError:
        print("Invalid")
        pass
