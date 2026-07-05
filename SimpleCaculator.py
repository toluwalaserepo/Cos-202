print("Simple Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Choose an operation (+, -, *, /): ")

match operator:
    case "+":
        print("Answer =", num1 + num2)

    case "-":
        print("Answer =", num1 - num2)

    case "*":
        print("Answer =", num1 * num2)

    case "/":
        if num2 != 0:
            print("Answer =", num1 / num2)
        else:
            print("Error! Division by zero is not allowed.")

    case _:
        print("Invalid operator.")
