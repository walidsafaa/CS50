expression = input("Expression: ").strip().split()

x = float(expression[0])

y = expression[1]

z = float(expression[2])

match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case "/":
        print(round(x / z, 1))
